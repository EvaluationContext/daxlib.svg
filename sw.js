---
permalink: /sw.js
---

// Service Worker for PWA cache (Chirpy-style, Jekyll-processed)
const CACHE_NAME = 'ec-colour-{{ site.time | date: "%Y%m%d%H%M%S" }}';
const RESOURCES_TO_PRECACHE = [
  '{{ site.baseurl }}/',
  '{{ site.baseurl }}/index.html',
  '{{ site.baseurl }}/assets/css/google-light.css',
  '{{ site.baseurl }}/assets/css/highlightjs-badge-custom.css',
  '{{ site.baseurl }}/assets/js/highlight/languages/dax.js',
  // Add more resources as needed
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(RESOURCES_TO_PRECACHE))
  );
  self.skipWaiting();
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(
        keys.filter(key => key !== CACHE_NAME)
            .map(key => caches.delete(key))
      )
    )
  );
  self.clients.claim();
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => response || fetch(event.request))
  );
});
