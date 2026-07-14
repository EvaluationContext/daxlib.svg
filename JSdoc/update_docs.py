import re
import json
import yaml
from pathlib import Path
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict


@dataclass
class FunctionParameter:
    """Represents a function parameter."""
    name: str
    type: str
    description: str
    optional: bool = False
    default_value: Optional[str] = None


def parse_function_signature(function_body: str) -> List[Dict]:
    """Extract parameter names, types, and default values from a DAX UDF signature.

    A DAX UDF signature has the form:
        ( name1 : TYPE [SUBTYPE ...] [= DEFAULT], name2 : TYPE [= DEFAULT], ... ) => ...

    Returns a list of dicts with keys: name, type, default (or None).
    """
    if '(' not in function_body:
        return []

    start = function_body.index('(')
    depth = 0
    end = -1
    for i in range(start, len(function_body)):
        ch = function_body[i]
        if ch == '(':
            depth += 1
        elif ch == ')':
            depth -= 1
            if depth == 0:
                end = i
                break

    if end < 0:
        return []

    signature_body = function_body[start + 1:end]

    # Split params on commas at depth 0 (respect nested parens for defaults like BLANK())
    params: List[str] = []
    depth = 0
    current: List[str] = []
    for ch in signature_body:
        if ch == '(':
            depth += 1
            current.append(ch)
        elif ch == ')':
            depth -= 1
            current.append(ch)
        elif ch == ',' and depth == 0:
            piece = ''.join(current).strip()
            if piece:
                params.append(piece)
            current = []
        else:
            current.append(ch)
    tail = ''.join(current).strip()
    if tail:
        params.append(tail)

    result: List[Dict] = []
    for p in params:
        default = None
        # Split on the first '=' at depth 0
        eq_idx = -1
        depth = 0
        for i, ch in enumerate(p):
            if ch == '(':
                depth += 1
            elif ch == ')':
                depth -= 1
            elif ch == '=' and depth == 0:
                eq_idx = i
                break

        if eq_idx >= 0:
            default = p[eq_idx + 1:].strip()
            name_type = p[:eq_idx].strip()
        else:
            name_type = p.strip()

        if ':' in name_type:
            name, type_str = name_type.split(':', 1)
            name = name.strip()
            type_str = type_str.strip().upper()
        else:
            name = name_type.strip()
            type_str = ''

        result.append({'name': name, 'type': type_str, 'default': default})

    return result


@dataclass
class FunctionMetadata:
    """Represents extracted function metadata."""
    name: str
    short_name: str  # e.g., "Hex.Theme" from "EvaluationContext.Colour.Hex.Theme"
    description: str
    parameters: List[FunctionParameter]
    return_type: str
    return_description: str
    code: str
    example: Optional[str] = None
    author: Optional[str] = None
    version: Optional[str] = None
    since: Optional[str] = None
    see: Optional[List[str]] = None
    deprecated: Optional[str] = None

def parse_tmdl_functions(tmdl_path: Path) -> List[FunctionMetadata]:
    """
    Parse TMDL file and extract function metadata from JSDoc comments.
    
    Args:
        tmdl_path: Path to the functions.tmdl file
        
    Returns:
        List of FunctionMetadata objects
    """
    content = tmdl_path.read_text(encoding='utf-8')
    functions = []
    
    # Split by annotation blocks to separate functions
    # Each function ends with annotation lines
    function_blocks = re.split(
        r'(\n\s*annotation\s+DAXLIB_PackageVersion\s*=.*?\n)',
        content
    )
    
    # Process pairs: function_code + annotation
    i = 0
    while i < len(function_blocks):
        block = function_blocks[i]
        
        # Look for JSDoc comment + function definition
        func_match = re.search(
            r"((?:///.*\n)+)"  # JSDoc comments
            r"\s*"
            r"function\s+'([^']+)'\s*="  # function 'name' =
            r"(.*)",  # Function body (rest of block)
            block,
            re.DOTALL | re.MULTILINE
        )
        
        if func_match:
            jsdoc_block = func_match.group(1)
            function_name = func_match.group(2).strip()
            function_body = func_match.group(3).strip()
        
            # Extract short name (e.g., "Element.Rect" from "DaxLib.SVG.Element.Rect")
            short_name = function_name.replace('DaxLib.SVG.', '')
        
            # Parse JSDoc comments
            description_lines = []
            parameters = []
            return_type = ""
            return_description = ""
            custom_example = None  # For @example tag
            author = None
            version = None
            since = None
            see_also = []
            deprecated = None
        
            for line in jsdoc_block.split('\n'):
                line = line.strip().lstrip('/').strip()
            
                if line.startswith('@param'):
                    # Parse: @param {type} name – description
                    # or: @param {type} [name] – description (optional)
                    # or: @param {type} [name=default] – description (optional with default)
                    
                    # Try optional parameter with default value first
                    param_match = re.match(r'@param\s+\{([^}]+)\}\s+\[(\w+)=([^\]]+)\]\s+–\s+(.*)', line)
                    if param_match:
                        param_type = param_match.group(1)
                        param_name = param_match.group(2)
                        default_value = param_match.group(3)
                        param_desc = param_match.group(4)
                        parameters.append(FunctionParameter(param_name, param_type, param_desc, optional=True, default_value=default_value))
                    else:
                        # Try optional parameter without default value
                        param_match = re.match(r'@param\s+\{([^}]+)\}\s+\[(\w+)\]\s+–\s+(.*)', line)
                        if param_match:
                            param_type = param_match.group(1)
                            param_name = param_match.group(2)
                            param_desc = param_match.group(3)
                            parameters.append(FunctionParameter(param_name, param_type, param_desc, optional=True))
                        else:
                            # Try required parameter
                            param_match = re.match(r'@param\s+\{([^}]+)\}\s+(\w+)\s+–\s+(.*)', line)
                            if param_match:
                                param_type = param_match.group(1)
                                param_name = param_match.group(2)
                                param_desc = param_match.group(3)
                                # Check if description starts with "Optional:" to detect optional params
                                is_optional = param_desc.strip().startswith('Optional:') or param_desc.strip().startswith('Optional ')
                                if is_optional:
                                    # Strip the "Optional:" prefix from the description
                                    param_desc = re.sub(r'^Optional:\s*', '', param_desc.strip())
                                    param_desc = re.sub(r'^Optional\s+', '', param_desc.strip())
                                parameters.append(FunctionParameter(param_name, param_type, param_desc, optional=is_optional))
                elif line.startswith('@example'):
                    # Parse: @example function call or description
                    example_match = re.match(r'@example\s+(.*)', line)
                    if example_match:
                        custom_example = example_match.group(1)
                elif line.startswith('@author'):
                    # Parse: @author Name
                    author_match = re.match(r'@author\s+(.*)', line)
                    if author_match:
                        author = author_match.group(1)
                elif line.startswith('@version'):
                    # Parse: @version 1.0.0
                    version_match = re.match(r'@version\s+(.*)', line)
                    if version_match:
                        version = version_match.group(1)
                elif line.startswith('@since'):
                    # Parse: @since 1.0.0 or @since 2024-01-01
                    since_match = re.match(r'@since\s+(.*)', line)
                    if since_match:
                        since = since_match.group(1)
                elif line.startswith('@see'):
                    # Parse: @see RelatedFunction or @see https://url
                    see_match = re.match(r'@see\s+(.*)', line)
                    if see_match:
                        see_also.append(see_match.group(1))
                elif line.startswith('@deprecated'):
                    # Parse: @deprecated Use NewFunction instead
                    deprecated_match = re.match(r'@deprecated\s+(.*)', line)
                    if deprecated_match:
                        deprecated = deprecated_match.group(1)
                    else:
                        deprecated = "This function is deprecated"
                elif line.startswith('@returns'):
                    # Parse: @returns {type} description
                    return_match = re.match(r'@returns\s+\{([^}]+)\}\s+(.*)', line)
                    if return_match:
                        return_type = return_match.group(1).upper()
                        return_description = return_match.group(2)
                elif line and not line.startswith('@'):
                    # Description line
                    description_lines.append(line.strip())
        
            description = ' '.join(description_lines).strip()

            # Parse the actual DAX function signature to pick up default values
            # declared with the new UDF optional-parameter syntax (`name: TYPE = DEFAULT`).
            # The signature is authoritative for optionality and default expressions;
            # JSDoc metadata (types, descriptions) is preserved.
            sig_params = parse_function_signature(function_body)
            sig_by_name = {sp['name']: sp for sp in sig_params}

            for param in parameters:
                sp = sig_by_name.get(param.name)
                if sp is None:
                    continue
                if sp.get('default') is not None:
                    param.optional = True
                    param.default_value = sp['default']

            # Extract function code (clean up formatting and remove annotations)
            # Split function body to remove annotations
            body_lines = function_body.split('\n')
            clean_body_lines = []
            for line in body_lines:
                # Stop at annotation lines
                if 'annotation DAXLIB_' in line:
                    break
                clean_body_lines.append(line)
            
            # Reconstruct the clean function body
            clean_body = '\n'.join(clean_body_lines).rstrip()
            
            # Ensure opening parenthesis has proper indentation (2 tabs)
            # The function body starts with whitespace + (, we need to ensure it has 2 tabs
            if clean_body.lstrip().startswith('('):
                # Remove leading whitespace and add 2 tabs
                clean_body = '\t\t' + clean_body.lstrip()
            
            code = f"function '{function_name}' =\n{clean_body}"
        
            # Only use custom example if provided (no auto-generation)
            example = custom_example
        
            functions.append(FunctionMetadata(
                name=function_name,
                short_name=short_name,
                description=description,
                parameters=parameters,
                return_type=return_type,
                return_description=return_description,
                code=code,
                example=example,
                author=author,
                version=version,
                since=since,
                see=see_also if see_also else None,
                deprecated=deprecated
            ))
        
        # Move to next block
        i += 1
    
    return functions


def generate_example(function_name: str, parameters: List[FunctionParameter]) -> str:
    """
    Generate a basic example usage for a function.
    This is just a fallback - use @example tag for better examples.
    
    Args:
        function_name: Full function name
        parameters: List of function parameters
        
    Returns:
        Example DAX code as string
    """
    # Create simple placeholder example
    if len(parameters) == 0:
        return f"{function_name}()"
    
    # Create generic parameter placeholders
    param_names = [p.name for p in parameters]
    params_str = ', '.join(param_names)
    return f"{function_name}({params_str})"


def type_to_label(dax_type: str) -> str:
    """
    Convert DAX type to HTML span with proper class.
    
    Args:
        dax_type: DAX type (STRING, INT64, DOUBLE, DECIMAL, etc.)
        
    Returns:
        HTML span element(s) — one pill per word for multi-word types
    """
    type_map = {
        'STRING': ('string', 'STRING'),
        'INT64': ('int64', 'INT64'),
        'INT': ('int64', 'INT64'),
        'INTEGER': ('int64', 'INT64'),
        'DOUBLE': ('number', 'DOUBLE'),
        'NUMBER': ('number', 'DOUBLE'),
        'NUMERIC': ('number', 'NUMERIC'),
        'DECIMAL': ('number', 'DECIMAL'),
        'BOOLEAN': ('boolean', 'BOOLEAN'),
        'TABLE': ('table', 'TABLE'),
        'ANYREF': ('anyref', 'ANYREF'),
        'EXPR': ('expr', 'EXPR'),
        'VAL': ('val', 'VAL'),
    }
    
    words = dax_type.strip().split()
    pills = []
    for word in words:
        css_class, display_text = type_map.get(word.upper(), ('string', word.upper()))
        pills.append(f'<span class="type-label {css_class}">{display_text}</span>')
    return ' '.join(pills)


def create_syntax_section(func: FunctionMetadata) -> str:
    """
    Create the Syntax tab content.
    
    Args:
        func: Function metadata
        
    Returns:
        Markdown string for syntax section
    """
    lines = ['=== "Syntax"', '', '    ```dax']
    
    # Function signature - do NOT use brackets in code sample
    param_parts = []
    for p in func.parameters:
        param_parts.append(p.name)
    param_list = ', '.join(param_parts)
    lines.append(f'    {func.name}( {param_list} )')
    lines.append('    ```')
    lines.append('')
    
    # Parameters table
    if func.parameters:
        lines.append('    | Parameter | Type | Required | Default | Description |')
        lines.append('    |:---:|:---:|:---:|:---:|---|')

        for param in func.parameters:
            type_label = type_to_label(param.type)
            # Use :material-close: for optional, :material-check: for required
            required_icon = ':material-close:' if param.optional else ':material-check:'
            default_cell = f'`#!dax {param.default_value}`' if param.default_value else ''
            lines.append(
                f'    | {param.name} | {type_label} | {required_icon} | {default_cell} | {param.description} |'
            )

        lines.append('')
    
    # Return type
    return_label = type_to_label(func.return_type)
    lines.append(f'    {return_label} {func.return_description}')
    
    return '\n'.join(lines)


def create_example_section(func: FunctionMetadata) -> str:
    """
    Create the Example tab content.
    
    Args:
        func: Function metadata
        
    Returns:
        Markdown string for example section, or empty string if no example exists
    """
    # Only generate example section if an example exists
    if not func.example:
        return ""
    
    lines = ['=== "Example"', '', '    ```dax']
    lines.append(f'    {func.example}')
    lines.append('    ```')
    
    return '\n'.join(lines)


def create_definition_section(func: FunctionMetadata) -> str:
    """
    Create the Definition tab content.
    
    Args:
        func: Function metadata
        
    Returns:
        Markdown string for definition section
    """
    lines = ['=== "Definition"', '', '    ```dax']
    
    # Add function code with proper indentation
    # Annotations already removed during parsing
    for line in func.code.split('\n'):
        lines.append(f'    {line}')
    
    lines.append('    ```')
    
    return '\n'.join(lines)


def get_doc_path(base_dir: Path, func: FunctionMetadata, custom_mapping: Optional[Dict] = None) -> Path:
    """
    Determine the appropriate documentation path based on function type.
    
    Args:
        base_dir: Base docs directory
        func: Function metadata
        custom_mapping: Optional custom mapping from config (pattern_match or function_paths)
        
    Returns:
        Path to the documentation file
    """
    short_name = func.short_name
    filename = f"{func.short_name}.md"
    
    # Check custom mapping first
    if custom_mapping:
        # Check for exact function name match
        if 'function_paths' in custom_mapping and short_name in custom_mapping['function_paths']:
            custom_path = custom_mapping['function_paths'][short_name]
            return Path(custom_path) if Path(custom_path).is_absolute() else base_dir / custom_path / filename
        
        # Check pattern matching
        if 'pattern_match' in custom_mapping:
            for pattern, subfolder in custom_mapping['pattern_match'].items():
                # Split pattern by | for OR matching
                patterns = [p.strip() for p in pattern.split('|')]
                if any(p in short_name for p in patterns):
                    return base_dir / subfolder / filename
    
    # Default pattern matching
    if any(x in short_name for x in ['ToHex', 'ToInt']):
        subfolder = 'conversion'
    elif any(x in short_name for x in ['Theme', 'Interpolate', 'LinearTheme']):
        subfolder = 'theming'
    elif short_name.startswith('Hex.'):
        subfolder = 'hex-manipulation'
    else:
        subfolder = 'conversion'  # Default
    
    return base_dir / subfolder / filename


def save_function_metadata(output_dir: Path, func: FunctionMetadata) -> Path:
    """
    Save function metadata to a JSON file for use with Jinja templates.
    
    Args:
        output_dir: Directory to save JSON files
        func: Function metadata
        
    Returns:
        Path to the saved JSON file
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Convert to dictionary, handling the dataclass nested structure
    func_dict = {
        'name': func.name,
        'short_name': func.short_name,
        'description': func.description,
        'parameters': [
            {
                'name': p.name,
                'type': p.type,
                'type_label': type_to_label(p.type),
                'description': p.description,
                'optional': p.optional,
                'default_value': p.default_value
            }
            for p in func.parameters
        ],
        'return_type': func.return_type,
        'return_type_label': type_to_label(func.return_type),
        'return_description': func.return_description,
        'code': func.code,
        'example': func.example,
        'author': func.author,
        'version': func.version,
        'since': func.since,
        'see': func.see,
        'deprecated': func.deprecated,
        # Pre-rendered sections for convenience
        'sections': {
            'syntax': create_syntax_section(func),
            'example': create_example_section(func),
            'definition': create_definition_section(func)
        }
    }
    
    # Save to JSON file named after the function
    json_path = output_dir / f"{func.name}.json"
    with json_path.open('w', encoding='utf-8') as f:
        json.dump(func_dict, f, indent=2, ensure_ascii=False)
    
    return json_path


def load_extended_content(base_dir: Path, func: FunctionMetadata, content_type: str) -> Optional[str]:
    """
    Load extended content for a function if it exists.
    
    Args:
        base_dir: Base directory containing extended_content folder
        func: Function metadata
        content_type: Type of content ('pretab' or 'tabs')
        
    Returns:
        Content string if file exists (with trailing whitespace stripped), None otherwise
    """
    extended_dir = base_dir / 'extended_content'
    filename = f"{func.short_name}.{content_type}.md"
    filepath = extended_dir / filename
    
    if filepath.exists():
        try:
            # Read and strip trailing whitespace/newlines
            return filepath.read_text(encoding='utf-8').rstrip()
        except Exception as e:
            print(f"Warning: Could not read {filepath}: {e}")
            return None
    
    return None


def create_page_from_template(template_path: Path, output_path: Path, func: FunctionMetadata, extended_content_dir: Optional[Path] = None) -> bool:
    """
    Create a documentation page from a Jinja template.
    
    Args:
        template_path: Path to the Jinja template file
        output_path: Path where the markdown file should be created
        func: Function metadata
        extended_content_dir: Optional directory containing extended content files
        
    Returns:
        True if created successfully
    """
    try:
        from jinja2 import Template
        
        # Read template
        template_content = template_path.read_text(encoding='utf-8')
        template = Template(template_content)
        
        # Load extended content if directory provided
        pretab_content = None
        additional_tabs = None
        if extended_content_dir:
            pretab_content = load_extended_content(extended_content_dir.parent, func, 'pretab')
            additional_tabs = load_extended_content(extended_content_dir.parent, func, 'tabs')
        
        # Prepare context
        context = {
            'name': func.name,
            'short_name': func.short_name,
            'description': func.description,
            'parameters': func.parameters,
            'return_type': func.return_type,
            'return_type_label': type_to_label(func.return_type),
            'return_description': func.return_description,
            'code': func.code,
            'example': func.example,
            'syntax_section': create_syntax_section(func),
            'example_section': create_example_section(func),
            'definition_section': create_definition_section(func),
            'pretab_content': pretab_content,
            'additional_tabs': additional_tabs,
        }
        
        # Render template
        rendered = template.render(**context)
        
        # Ensure directory exists
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Write content
        output_path.write_text(rendered, encoding='utf-8')
        return True
        
    except ImportError:
        print("Warning: jinja2 not installed. Install with: pip install jinja2")
        return False
    except Exception as e:
        print(f"Error creating page from template: {e}")
        return False


def main():
    """Main execution function."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Parse TMDL functions and generate documentation data')
    parser.add_argument('config', type=str,
                       help='Path to YAML configuration file')
    
    args = parser.parse_args()
    
    # Load configuration from YAML
    config_path = Path(args.config)
    if not config_path.exists():
        print(f"Error: Config file not found: {config_path}")
        return
    
    with config_path.open('r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    
    print(f"Loaded configuration from: {config_path}")
    
    # Paths - script is now in JSdoc folder, so go up one level to root
    script_dir = Path(__file__).parent
    root_dir = script_dir.parent
    
    # Get paths from config (required)
    if 'source' not in config:
        print("Error: 'source' not specified in config file")
        return
    if 'destination' not in config:
        print("Error: 'destination' not specified in config file")
        return
    
    docs_dir = root_dir / config['destination']
    output_dir = script_dir / config.get('output_dir', 'parsed_functions')
    template_path = config.get('template', None)
    
    # Resolve source TMDL file(s) — supports a single string, a glob, or a list
    import glob as glob_mod
    source_cfg = config['source']
    if isinstance(source_cfg, str):
        source_entries = [source_cfg]
    elif isinstance(source_cfg, list):
        source_entries = source_cfg
    else:
        print(f"Error: 'source' must be a string or list, got {type(source_cfg).__name__}")
        return
    
    tmdl_paths: List[Path] = []
    for entry in source_entries:
        resolved = sorted(root_dir.glob(entry))  # supports globs and plain paths
        if not resolved:
            print(f"Warning: No files matched source entry: {entry}")
        tmdl_paths.extend(resolved)
    
    if not tmdl_paths:
        print("Error: No source TMDL files found")
        return
    
    print(f"Documentation directory: {docs_dir}")
    print(f"Metadata output: {output_dir}")
    if template_path:
        print(f"Using template: {template_path}")
    
    # Parse functions from all source files
    functions: List[FunctionMetadata] = []
    for tmdl_path in tmdl_paths:
        print(f"Parsing functions from: {tmdl_path}")
        file_functions = parse_tmdl_functions(tmdl_path)
        print(f"  Found {len(file_functions)} functions in {tmdl_path.name}")
        functions.extend(file_functions)
    
    print(f"Total functions found: {len(functions)}")
    print(f"Saving metadata to: {output_dir}")
    
    # Extended content directory
    extended_content_dir = script_dir / 'extended_content'
    
    # Save metadata and create/update pages
    saved_count = 0
    created_count = 0
    updated_count = 0
    
    # Get custom path mapping from config
    custom_mapping = config.get('path_mapping', None)
    
    for func in functions:
        # Save JSON metadata
        json_path = save_function_metadata(output_dir, func)
        saved_count += 1
        print(f"\n✓ Saved metadata: {json_path.name}")
        
        # Always create/update pages when running with config
        doc_path = get_doc_path(docs_dir, func, custom_mapping)
        
        if not doc_path.exists():
            print(f"  Creating page: {doc_path}")
            
            if not template_path:
                print(f"  ✗ No template specified in config file")
                continue
            
            # Use Jinja template
            template_file = root_dir / template_path if not Path(template_path).is_absolute() else Path(template_path)
            if template_file.exists():
                if create_page_from_template(template_file, doc_path, func, extended_content_dir):
                    created_count += 1
                    print(f"  ✓ Created from template")
                else:
                    print(f"  ✗ Failed to create from template")
            else:
                print(f"  ✗ Template not found: {template_file}")
        else:
            print(f"  Updating page: {doc_path.name}")
            
            if not template_path:
                print(f"  ✗ No template specified in config file")
                continue
            
            # Use Jinja template
            template_file = root_dir / template_path if not Path(template_path).is_absolute() else Path(template_path)
            if template_file.exists():
                if create_page_from_template(template_file, doc_path, func, extended_content_dir):
                    updated_count += 1
                    print(f"  ✓ Updated from template")
                else:
                    print(f"  ✗ Failed to update from template")
            else:
                print(f"  ✗ Template not found: {template_file}")
    
    # Create summary JSON with all functions
    summary_path = output_dir / '_all_functions.json'
    summary_data = {
        'functions': [
            {
                'name': f.name,
                'short_name': f.short_name,
                'description': f.description,
                'json_file': f"{f.name}.json"
            }
            for f in functions
        ],
        'total_count': len(functions),
        'categories': {
            'conversion': [f.short_name for f in functions if any(x in f.short_name for x in ['ToHex', 'ToInt'])],
            'hex_manipulation': [f.short_name for f in functions if f.short_name.startswith('Hex.') and not any(x in f.short_name for x in ['Theme', 'Interpolate', 'LinearTheme'])],
            'themes': [f.short_name for f in functions if any(x in f.short_name for x in ['Theme', 'Interpolate', 'LinearTheme'])]
        }
    }
    
    with summary_path.open('w', encoding='utf-8') as f:
        json.dump(summary_data, f, indent=2, ensure_ascii=False)
    
    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  Functions parsed: {len(functions)}")
    print(f"  Metadata files saved: {saved_count}")
    print(f"  New pages created: {created_count}")
    print(f"  Existing pages updated: {updated_count}")
    print(f"  Summary file: {summary_path}")
    print(f"{'='*60}")
    print(f"\n✓ Documentation generation complete!")


if __name__ == '__main__':
    main()
