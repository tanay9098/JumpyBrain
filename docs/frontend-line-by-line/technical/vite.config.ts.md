# `vite.config.ts`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import { defineConfig } from 'vite'
     | Import for the Vite build and dev-server setup: `import { defineConfig } from 'vite'`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   2 | import react from '@vitejs/plugin-react'
     | Import for the Vite build and dev-server setup: `import react from '@vitejs/plugin-react'`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   3 | import { VitePWA } from 'vite-plugin-pwa'
     | Import for the Vite build and dev-server setup: `import { VitePWA } from 'vite-plugin-pwa'`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   4 | import fs from 'node:fs'
     | Import for the Vite build and dev-server setup: `import fs from 'node:fs'`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   5 | import path from 'node:path'
     | Import for the Vite build and dev-server setup: `import path from 'node:path'`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   6 | import { fileURLToPath } from 'node:url'
     | Import for the Vite build and dev-server setup: `import { fileURLToPath } from 'node:url'`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   7 | 
     | Blank line in `vite.config.ts` (the Vite build and dev-server setup), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   8 | const __dirname = path.dirname(fileURLToPath(import.meta.url))
     | In `the top of the file` (vite.config.ts): `__dirname` is assigned `path.dirname(fileURLToPath(import.meta.url))`. Later lines in this function read that name.

   9 | 
     | Blank line in `vite.config.ts` (the Vite build and dev-server setup), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  10 | // Read the Buy Me a Coffee username from the repo's FUNDING.yml so the
     | Comment inside the top of the file. Not executed. It documents the next code: Read the Buy Me a Coffee username from the repo's FUNDING.yml so the

  11 | // in-app support button and the GitHub sponsor button stay in sync.
     | Comment inside the top of the file. Not executed. It documents the next code: in-app support button and the GitHub sponsor button stay in sync.

  12 | function readFundingUrl() {
     | In `readFundingUrl` (vite.config.ts): statement `function readFundingUrl() {`. It runs when readFundingUrl runs, in order, before the next line of the same function.

  13 |   const fallback = 'https://buymeacoffee.com/tanaydwivedi'
     | In `readFundingUrl` (vite.config.ts): `fallback` is assigned `'https://buymeacoffee.com/tanaydwivedi'`. Later lines in this function read that name.

  14 |   try {
     | In `readFundingUrl` (vite.config.ts): error path `try {`.

  15 |     const yaml = fs.readFileSync(path.resolve(__dirname, '../.github/FUNDING.yml'), 'utf-8')
     | In `readFundingUrl` (vite.config.ts): `yaml` is assigned `fs.readFileSync(path.resolve(__dirname, '../.github/FUNDING.yml'), 'utf-8')`. Later lines in this function read that name.

  16 |     const match = yaml.match(/^buy_me_a_coffee:\s*(\S+)\s*$/m)
     | In `readFundingUrl` (vite.config.ts): `match` is assigned `yaml.match(/^buy_me_a_coffee:\s*(\S+)\s*$/m)`. Later lines in this function read that name.

  17 |     return match ? `https://buymeacoffee.com/${match[1]}` : fallback
     | In `readFundingUrl` (vite.config.ts): return `return match ? `https://buymeacoffee.com/${match[1]}` : fallback`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  18 |   } catch {
     | In `readFundingUrl` (vite.config.ts): `} catch {` closes try { (opened on line 14). Names declared inside that block end here.

  19 |     return fallback
     | In `readFundingUrl` (vite.config.ts): return `return fallback`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  20 |   }
     | In `readFundingUrl` (vite.config.ts): `}` closes } catch { (opened on line 18). Names declared inside that block end here.

  21 | }
     | In `readFundingUrl` (vite.config.ts): `}` closes readFundingUrl (opened on line 12). Names declared inside that block end here.

  22 | 
     | Blank line in `vite.config.ts` (the Vite build and dev-server setup), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  23 | export default defineConfig({
     | Default export of the Vite build and dev-server setup: `export default defineConfig({`. Importers that write `import X from 'vite.config.ts'` receive this value.

  24 |   define: {
     | In `the top of the file` (vite.config.ts): statement `define: {`. It runs when the top of the file runs, in order, before the next line of the same function.

  25 |     __FUNDING_URL__: JSON.stringify(readFundingUrl()),
     | In `the top of the file` (vite.config.ts): statement `__FUNDING_URL__: JSON.stringify(readFundingUrl()),`. It runs when the top of the file runs, in order, before the next line of the same function.

  26 |   },
     | In `the top of the file` (vite.config.ts): `},` closes define: { (opened on line 24). Names declared inside that block end here.

  27 |   plugins: [
     | In `the top of the file` (vite.config.ts): statement `plugins: [`. It runs when the top of the file runs, in order, before the next line of the same function.

  28 |     react(),
     | In `the top of the file` (vite.config.ts): statement `react(),`. It runs when the top of the file runs, in order, before the next line of the same function.

  29 |     VitePWA({
     | In `the top of the file` (vite.config.ts): statement `VitePWA({`. It runs when the top of the file runs, in order, before the next line of the same function.

  30 |       registerType: 'autoUpdate',
     | In `the top of the file` (vite.config.ts): The PWA service worker updates itself when a new build is published. Code: `registerType: 'autoUpdate',`.

  31 |       includeAssets: [
     | In `the top of the file` (vite.config.ts): statement `includeAssets: [`. It runs when the top of the file runs, in order, before the next line of the same function.

  32 |         'favicon.svg',
     | In `the top of the file` (vite.config.ts): statement `'favicon.svg',`. It runs when the top of the file runs, in order, before the next line of the same function.

  33 |         'favicon-32.png',
     | In `the top of the file` (vite.config.ts): statement `'favicon-32.png',`. It runs when the top of the file runs, in order, before the next line of the same function.

  34 |         'apple-touch-icon.png',
     | In `the top of the file` (vite.config.ts): statement `'apple-touch-icon.png',`. It runs when the top of the file runs, in order, before the next line of the same function.

  35 |         'icons/favicon-16.png',
     | In `the top of the file` (vite.config.ts): statement `'icons/favicon-16.png',`. It runs when the top of the file runs, in order, before the next line of the same function.

  36 |         'icons/favicon-32.png',
     | In `the top of the file` (vite.config.ts): statement `'icons/favicon-32.png',`. It runs when the top of the file runs, in order, before the next line of the same function.

  37 |         'icons/icon-192.png',
     | In `the top of the file` (vite.config.ts): statement `'icons/icon-192.png',`. It runs when the top of the file runs, in order, before the next line of the same function.

  38 |         'icons/icon-512.png',
     | In `the top of the file` (vite.config.ts): statement `'icons/icon-512.png',`. It runs when the top of the file runs, in order, before the next line of the same function.

  39 |         'icons/maskable-icon-192.png',
     | In `the top of the file` (vite.config.ts): statement `'icons/maskable-icon-192.png',`. It runs when the top of the file runs, in order, before the next line of the same function.

  40 |         'icons/maskable-icon-512.png',
     | In `the top of the file` (vite.config.ts): statement `'icons/maskable-icon-512.png',`. It runs when the top of the file runs, in order, before the next line of the same function.

  41 |         'logo-icon.svg',
     | In `the top of the file` (vite.config.ts): statement `'logo-icon.svg',`. It runs when the top of the file runs, in order, before the next line of the same function.

  42 |       ],
     | In `the top of the file` (vite.config.ts): statement `],`. It runs when the top of the file runs, in order, before the next line of the same function.

  43 |       manifest: {
     | In `the top of the file` (vite.config.ts): statement `manifest: {`. It runs when the top of the file runs, in order, before the next line of the same function.

  44 |         name: 'JumpyBrain',
     | In `the top of the file` (vite.config.ts): statement `name: 'JumpyBrain',`. It runs when the top of the file runs, in order, before the next line of the same function.

  45 |         short_name: 'JumpyBrain',
     | In `the top of the file` (vite.config.ts): statement `short_name: 'JumpyBrain',`. It runs when the top of the file runs, in order, before the next line of the same function.

  46 |         description: 'Focus better. Do more. Feel calm — ADHD-friendly productivity.',
     | In `the top of the file` (vite.config.ts): statement `description: 'Focus better. Do more. Feel calm — ADHD-friendly productivity.',`. It runs when the top of the file runs, in order, before the next line of the same function.

  47 |         theme_color: '#6366f1',
     | In `the top of the file` (vite.config.ts): statement `theme_color: '#6366f1',`. It runs when the top of the file runs, in order, before the next line of the same function.

  48 |         background_color: '#0f1020',
     | In `the top of the file` (vite.config.ts): statement `background_color: '#0f1020',`. It runs when the top of the file runs, in order, before the next line of the same function.

  49 |         display: 'standalone',
     | In `the top of the file` (vite.config.ts): statement `display: 'standalone',`. It runs when the top of the file runs, in order, before the next line of the same function.

  50 |         start_url: '/',
     | In `the top of the file` (vite.config.ts): statement `start_url: '/',`. It runs when the top of the file runs, in order, before the next line of the same function.

  51 |         orientation: 'portrait',
     | In `the top of the file` (vite.config.ts): statement `orientation: 'portrait',`. It runs when the top of the file runs, in order, before the next line of the same function.

  52 |         categories: ['productivity', 'lifestyle'],
     | In `the top of the file` (vite.config.ts): statement `categories: ['productivity', 'lifestyle'],`. It runs when the top of the file runs, in order, before the next line of the same function.

  53 |         icons: [
     | In `the top of the file` (vite.config.ts): statement `icons: [`. It runs when the top of the file runs, in order, before the next line of the same function.

  54 |           {
     | In `the top of the file` (vite.config.ts): statement `{`. It runs when the top of the file runs, in order, before the next line of the same function.

  55 |             src: '/icons/favicon-16.png',
     | In `the top of the file` (vite.config.ts): statement `src: '/icons/favicon-16.png',`. It runs when the top of the file runs, in order, before the next line of the same function.

  56 |             sizes: '16x16',
     | In `the top of the file` (vite.config.ts): statement `sizes: '16x16',`. It runs when the top of the file runs, in order, before the next line of the same function.

  57 |             type: 'image/png',
     | In `the top of the file` (vite.config.ts): statement `type: 'image/png',`. It runs when the top of the file runs, in order, before the next line of the same function.

  58 |           },
     | In `the top of the file` (vite.config.ts): `},` closes { (opened on line 54). Names declared inside that block end here.

  59 |           {
     | In `the top of the file` (vite.config.ts): statement `{`. It runs when the top of the file runs, in order, before the next line of the same function.

  60 |             src: '/icons/favicon-32.png',
     | In `the top of the file` (vite.config.ts): statement `src: '/icons/favicon-32.png',`. It runs when the top of the file runs, in order, before the next line of the same function.

  61 |             sizes: '32x32',
     | In `the top of the file` (vite.config.ts): statement `sizes: '32x32',`. It runs when the top of the file runs, in order, before the next line of the same function.

  62 |             type: 'image/png',
     | In `the top of the file` (vite.config.ts): statement `type: 'image/png',`. It runs when the top of the file runs, in order, before the next line of the same function.

  63 |           },
     | In `the top of the file` (vite.config.ts): `},` closes { (opened on line 59). Names declared inside that block end here.

  64 |           {
     | In `the top of the file` (vite.config.ts): statement `{`. It runs when the top of the file runs, in order, before the next line of the same function.

  65 |             src: '/icons/icon-192.png',
     | In `the top of the file` (vite.config.ts): statement `src: '/icons/icon-192.png',`. It runs when the top of the file runs, in order, before the next line of the same function.

  66 |             sizes: '192x192',
     | In `the top of the file` (vite.config.ts): statement `sizes: '192x192',`. It runs when the top of the file runs, in order, before the next line of the same function.

  67 |             type: 'image/png',
     | In `the top of the file` (vite.config.ts): statement `type: 'image/png',`. It runs when the top of the file runs, in order, before the next line of the same function.

  68 |             purpose: 'any',
     | In `the top of the file` (vite.config.ts): statement `purpose: 'any',`. It runs when the top of the file runs, in order, before the next line of the same function.

  69 |           },
     | In `the top of the file` (vite.config.ts): `},` closes { (opened on line 64). Names declared inside that block end here.

  70 |           {
     | In `the top of the file` (vite.config.ts): statement `{`. It runs when the top of the file runs, in order, before the next line of the same function.

  71 |             src: '/icons/icon-512.png',
     | In `the top of the file` (vite.config.ts): statement `src: '/icons/icon-512.png',`. It runs when the top of the file runs, in order, before the next line of the same function.

  72 |             sizes: '512x512',
     | In `the top of the file` (vite.config.ts): statement `sizes: '512x512',`. It runs when the top of the file runs, in order, before the next line of the same function.

  73 |             type: 'image/png',
     | In `the top of the file` (vite.config.ts): statement `type: 'image/png',`. It runs when the top of the file runs, in order, before the next line of the same function.

  74 |             purpose: 'any',
     | In `the top of the file` (vite.config.ts): statement `purpose: 'any',`. It runs when the top of the file runs, in order, before the next line of the same function.

  75 |           },
     | In `the top of the file` (vite.config.ts): `},` closes { (opened on line 70). Names declared inside that block end here.

  76 |           {
     | In `the top of the file` (vite.config.ts): statement `{`. It runs when the top of the file runs, in order, before the next line of the same function.

  77 |             src: '/icons/maskable-icon-192.png',
     | In `the top of the file` (vite.config.ts): statement `src: '/icons/maskable-icon-192.png',`. It runs when the top of the file runs, in order, before the next line of the same function.

  78 |             sizes: '192x192',
     | In `the top of the file` (vite.config.ts): statement `sizes: '192x192',`. It runs when the top of the file runs, in order, before the next line of the same function.

  79 |             type: 'image/png',
     | In `the top of the file` (vite.config.ts): statement `type: 'image/png',`. It runs when the top of the file runs, in order, before the next line of the same function.

  80 |             purpose: 'maskable',
     | In `the top of the file` (vite.config.ts): statement `purpose: 'maskable',`. It runs when the top of the file runs, in order, before the next line of the same function.

  81 |           },
     | In `the top of the file` (vite.config.ts): `},` closes { (opened on line 76). Names declared inside that block end here.

  82 |           {
     | In `the top of the file` (vite.config.ts): statement `{`. It runs when the top of the file runs, in order, before the next line of the same function.

  83 |             src: '/icons/maskable-icon-512.png',
     | In `the top of the file` (vite.config.ts): statement `src: '/icons/maskable-icon-512.png',`. It runs when the top of the file runs, in order, before the next line of the same function.

  84 |             sizes: '512x512',
     | In `the top of the file` (vite.config.ts): statement `sizes: '512x512',`. It runs when the top of the file runs, in order, before the next line of the same function.

  85 |             type: 'image/png',
     | In `the top of the file` (vite.config.ts): statement `type: 'image/png',`. It runs when the top of the file runs, in order, before the next line of the same function.

  86 |             purpose: 'maskable',
     | In `the top of the file` (vite.config.ts): statement `purpose: 'maskable',`. It runs when the top of the file runs, in order, before the next line of the same function.

  87 |           },
     | In `the top of the file` (vite.config.ts): `},` closes { (opened on line 82). Names declared inside that block end here.

  88 |         ],
     | In `the top of the file` (vite.config.ts): statement `],`. It runs when the top of the file runs, in order, before the next line of the same function.

  89 |       },
     | In `the top of the file` (vite.config.ts): `},` closes manifest: { (opened on line 43). Names declared inside that block end here.

  90 |       workbox: {
     | In `the top of the file` (vite.config.ts): statement `workbox: {`. It runs when the top of the file runs, in order, before the next line of the same function.

  91 |         // index.html is deliberately left out of precaching: a precached
     | Comment inside the top of the file. Not executed. It documents the next code: index.html is deliberately left out of precaching: a precached

  92 |         // shell is served straight from the service worker's own cache on
     | Comment inside the top of the file. Not executed. It documents the next code: shell is served straight from the service worker's own cache on

  93 |         // every navigation, bypassing the Cache-Control headers on
     | Comment inside the top of the file. Not executed. It documents the next code: every navigation, bypassing the Cache-Control headers on

  94 |         // /index.html (see vercel.json) entirely. That let a stale shell
     | Comment inside the top of the file. Not executed. It documents the next code: /index.html (see vercel.json) entirely. That let a stale shell

  95 |         // referencing deleted hashed asset URLs get stuck serving forever
     | Comment inside the top of the file. Not executed. It documents the next code: referencing deleted hashed asset URLs get stuck serving forever

  96 |         // on tabs with an already-installed service worker. Leaving html
     | Comment inside the top of the file. Not executed. It documents the next code: on tabs with an already-installed service worker. Leaving html

  97 |         // off this list means navigation requests hit the network (or the
     | Comment inside the top of the file. Not executed. It documents the next code: off this list means navigation requests hit the network (or the

  98 |         // browser's own HTTP cache, which does respect those headers)
     | Comment inside the top of the file. Not executed. It documents the next code: browser's own HTTP cache, which does respect those headers)

  99 |         // instead of the precache. vite-plugin-pwa otherwise defaults to a
     | Comment inside the top of the file. Not executed. It documents the next code: instead of the precache. vite-plugin-pwa otherwise defaults to a

 100 |         // navigateFallback of 'index.html', which registers a Workbox
     | Comment inside the top of the file. Not executed. It documents the next code: navigateFallback of 'index.html', which registers a Workbox

 101 |         // NavigationRoute serving all navigations from the precache too --
     | Comment inside the top of the file. Not executed. It documents the next code: NavigationRoute serving all navigations from the precache too --

 102 |         // disable that as well so navigations are never SW-intercepted.
     | Comment inside the top of the file. Not executed. It documents the next code: disable that as well so navigations are never SW-intercepted.

 103 |         navigateFallback: undefined,
     | In `the top of the file` (vite.config.ts): Disabled on purpose so the service worker does not serve a stale index.html for every navigation. Code: `navigateFallback: undefined,`.

 104 |         globPatterns: ['**/*.{js,css,ico,png,svg}'],
     | In `the top of the file` (vite.config.ts): `globPatterns: ['**/*.{js,css,ico,png,svg}'],` closes workbox: { (opened on line 90). Names declared inside that block end here.

 105 |         globIgnores: ['**/audio/**', '**/sounds/**'],
     | In `the top of the file` (vite.config.ts): statement `globIgnores: ['**/audio/**', '**/sounds/**'],`. It runs when the top of the file runs, in order, before the next line of the same function.

 106 |         runtimeCaching: [
     | In `the top of the file` (vite.config.ts): statement `runtimeCaching: [`. It runs when the top of the file runs, in order, before the next line of the same function.

 107 |           {
     | In `the top of the file` (vite.config.ts): statement `{`. It runs when the top of the file runs, in order, before the next line of the same function.

 108 |             urlPattern: /\.mp3$/i,
     | In `the top of the file` (vite.config.ts): statement `urlPattern: /\.mp3$/i,`. It runs when the top of the file runs, in order, before the next line of the same function.

 109 |             handler: 'CacheFirst',
     | In `the top of the file` (vite.config.ts): statement `handler: 'CacheFirst',`. It runs when the top of the file runs, in order, before the next line of the same function.

 110 |             options: {
     | In `the top of the file` (vite.config.ts): statement `options: {`. It runs when the top of the file runs, in order, before the next line of the same function.

 111 |               cacheName: 'audio-cache',
     | In `the top of the file` (vite.config.ts): statement `cacheName: 'audio-cache',`. It runs when the top of the file runs, in order, before the next line of the same function.

 112 |               expiration: {
     | In `the top of the file` (vite.config.ts): statement `expiration: {`. It runs when the top of the file runs, in order, before the next line of the same function.

 113 |                 maxEntries: 10,
     | In `the top of the file` (vite.config.ts): statement `maxEntries: 10,`. It runs when the top of the file runs, in order, before the next line of the same function.

 114 |                 maxAgeSeconds: 60 * 60 * 24 * 30,
     | In `the top of the file` (vite.config.ts): statement `maxAgeSeconds: 60 * 60 * 24 * 30,`. It runs when the top of the file runs, in order, before the next line of the same function.

 115 |               },
     | In `the top of the file` (vite.config.ts): `},` closes expiration: { (opened on line 112). Names declared inside that block end here.

 116 |             },
     | In `the top of the file` (vite.config.ts): `},` closes options: { (opened on line 110). Names declared inside that block end here.

 117 |           },
     | In `the top of the file` (vite.config.ts): `},` closes { (opened on line 107). Names declared inside that block end here.

 118 |           {
     | In `the top of the file` (vite.config.ts): statement `{`. It runs when the top of the file runs, in order, before the next line of the same function.

 119 |             urlPattern: /^https:\/\/.*\/api\/.*/i,
     | In `the top of the file` (vite.config.ts): statement `urlPattern: /^https:\/\/.*\/api\/.*/i,`. It runs when the top of the file runs, in order, before the next line of the same function.

 120 |             handler: 'NetworkFirst',
     | In `the top of the file` (vite.config.ts): statement `handler: 'NetworkFirst',`. It runs when the top of the file runs, in order, before the next line of the same function.

 121 |             options: {
     | In `the top of the file` (vite.config.ts): statement `options: {`. It runs when the top of the file runs, in order, before the next line of the same function.

 122 |               cacheName: 'api-cache',
     | In `the top of the file` (vite.config.ts): statement `cacheName: 'api-cache',`. It runs when the top of the file runs, in order, before the next line of the same function.

 123 |               expiration: {
     | In `the top of the file` (vite.config.ts): statement `expiration: {`. It runs when the top of the file runs, in order, before the next line of the same function.

 124 |                 maxEntries: 50,
     | In `the top of the file` (vite.config.ts): statement `maxEntries: 50,`. It runs when the top of the file runs, in order, before the next line of the same function.

 125 |                 maxAgeSeconds: 60 * 5,
     | In `the top of the file` (vite.config.ts): statement `maxAgeSeconds: 60 * 5,`. It runs when the top of the file runs, in order, before the next line of the same function.

 126 |               },
     | In `the top of the file` (vite.config.ts): `},` closes expiration: { (opened on line 123). Names declared inside that block end here.

 127 |               networkTimeoutSeconds: 10,
     | In `the top of the file` (vite.config.ts): statement `networkTimeoutSeconds: 10,`. It runs when the top of the file runs, in order, before the next line of the same function.

 128 |             },
     | In `the top of the file` (vite.config.ts): `},` closes options: { (opened on line 121). Names declared inside that block end here.

 129 |           },
     | In `the top of the file` (vite.config.ts): `},` closes { (opened on line 118). Names declared inside that block end here.

 130 |           {
     | In `the top of the file` (vite.config.ts): statement `{`. It runs when the top of the file runs, in order, before the next line of the same function.

 131 |             urlPattern: /^https:\/\/fonts\.googleapis\.com\/.*/i,
     | In `the top of the file` (vite.config.ts): statement `urlPattern: /^https:\/\/fonts\.googleapis\.com\/.*/i,`. It runs when the top of the file runs, in order, before the next line of the same function.

 132 |             handler: 'CacheFirst',
     | In `the top of the file` (vite.config.ts): statement `handler: 'CacheFirst',`. It runs when the top of the file runs, in order, before the next line of the same function.

 133 |             options: {
     | In `the top of the file` (vite.config.ts): statement `options: {`. It runs when the top of the file runs, in order, before the next line of the same function.

 134 |               cacheName: 'google-fonts-cache',
     | In `the top of the file` (vite.config.ts): statement `cacheName: 'google-fonts-cache',`. It runs when the top of the file runs, in order, before the next line of the same function.

 135 |               expiration: {
     | In `the top of the file` (vite.config.ts): statement `expiration: {`. It runs when the top of the file runs, in order, before the next line of the same function.

 136 |                 maxEntries: 10,
     | In `the top of the file` (vite.config.ts): statement `maxEntries: 10,`. It runs when the top of the file runs, in order, before the next line of the same function.

 137 |                 maxAgeSeconds: 60 * 60 * 24 * 365,
     | In `the top of the file` (vite.config.ts): statement `maxAgeSeconds: 60 * 60 * 24 * 365,`. It runs when the top of the file runs, in order, before the next line of the same function.

 138 |               },
     | In `the top of the file` (vite.config.ts): `},` closes expiration: { (opened on line 135). Names declared inside that block end here.

 139 |             },
     | In `the top of the file` (vite.config.ts): `},` closes options: { (opened on line 133). Names declared inside that block end here.

 140 |           },
     | In `the top of the file` (vite.config.ts): `},` closes { (opened on line 130). Names declared inside that block end here.

 141 |         ],
     | In `the top of the file` (vite.config.ts): statement `],`. It runs when the top of the file runs, in order, before the next line of the same function.

 142 |       },
     | In `the top of the file` (vite.config.ts): `},` closes workbox: { (opened on line 90). Names declared inside that block end here.

 143 |       devOptions: {
     | In `the top of the file` (vite.config.ts): statement `devOptions: {`. It runs when the top of the file runs, in order, before the next line of the same function.

 144 |         enabled: true,
     | In `the top of the file` (vite.config.ts): statement `enabled: true,`. It runs when the top of the file runs, in order, before the next line of the same function.

 145 |       },
     | In `the top of the file` (vite.config.ts): `},` closes devOptions: { (opened on line 143). Names declared inside that block end here.

 146 |     }),
     | In `the top of the file` (vite.config.ts): `}),` closes VitePWA({ (opened on line 29). Names declared inside that block end here.

 147 |   ],
     | In `the top of the file` (vite.config.ts): statement `],`. It runs when the top of the file runs, in order, before the next line of the same function.

 148 |   server: {
     | In `the top of the file` (vite.config.ts): statement `server: {`. It runs when the top of the file runs, in order, before the next line of the same function.

 149 |     port: 5173,
     | In `the top of the file` (vite.config.ts): The Vite dev server listens on 5173. Code: `port: 5173,`.

 150 |     proxy: {
     | In `the top of the file` (vite.config.ts): statement `proxy: {`. It runs when the top of the file runs, in order, before the next line of the same function.

 151 |       '/api': {
     | In `the top of the file` (vite.config.ts): statement `'/api': {`. It runs when the top of the file runs, in order, before the next line of the same function.

 152 |         target: 'http://localhost:3001',
     | In `the top of the file` (vite.config.ts): Dev-server proxy: browser calls to /api are forwarded to localhost:3001. Code: `target: 'http://localhost:3001',`.

 153 |         changeOrigin: true,
     | In `the top of the file` (vite.config.ts): statement `changeOrigin: true,`. It runs when the top of the file runs, in order, before the next line of the same function.

 154 |       },
     | In `the top of the file` (vite.config.ts): `},` closes '/api': { (opened on line 151). Names declared inside that block end here.

 155 |     },
     | In `the top of the file` (vite.config.ts): `},` closes proxy: { (opened on line 150). Names declared inside that block end here.

 156 |   },
     | In `the top of the file` (vite.config.ts): `},` closes server: { (opened on line 148). Names declared inside that block end here.

 157 | })
     | In `the top of the file` (vite.config.ts): `})` closes export default defineConfig({ (opened on line 23). Names declared inside that block end here.

