// Service worker mínimo requerido por TWA (Trusted Web Activity).
// Sin caché: pasa todo a la red para no servir contenido obsoleto.
self.addEventListener('install', () => self.skipWaiting());
self.addEventListener('activate', (e) => e.waitUntil(self.clients.claim()));
self.addEventListener('fetch', () => {});
