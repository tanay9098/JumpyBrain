# `vite.config.ts`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import { defineConfig } from 'vite'
     | This file borrows a tool another file already made.

   2 | import react from '@vitejs/plugin-react'
     | Borrows React so this file can remember things and draw the screen.

   3 | import { VitePWA } from 'vite-plugin-pwa'
     | This file borrows a tool another file already made.

   4 | import fs from 'node:fs'
     | This file borrows a tool another file already made.

   5 | import path from 'node:path'
     | This file borrows a tool another file already made.

   6 | import { fileURLToPath } from 'node:url'
     | This file borrows a tool another file already made.

   7 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   8 | const __dirname = path.dirname(fileURLToPath(import.meta.url))
     | This gives a short name to a value so the rest of the top of the file can use it.

   9 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  10 | // Read the Buy Me a Coffee username from the repo's FUNDING.yml so the
     | A note written for people. The app does not run it.

  11 | // in-app support button and the GitHub sponsor button stay in sync.
     | A note written for people. The app does not run it.

  12 | function readFundingUrl() {
     | Inside readFundingUrl, this line runs as written: function readFundingUrl() {. It happens in order, after the line above it and before the line below it.

  13 |   const fallback = 'https://buymeacoffee.com/tanaydwivedi'
     | This gives a short name to a value so the rest of readFundingUrl can use it.

  14 |   try {
     | Inside readFundingUrl, this line runs as written: try {. It happens in order, after the line above it and before the line below it.

  15 |     const yaml = fs.readFileSync(path.resolve(__dirname, '../.github/FUNDING.yml'), 'utf-8')
     | This gives a short name to a value so the rest of readFundingUrl can use it.

  16 |     const match = yaml.match(/^buy_me_a_coffee:\s*(\S+)\s*$/m)
     | This gives a short name to a value so the rest of readFundingUrl can use it.

  17 |     return match ? `https://buymeacoffee.com/${match[1]}` : fallback
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  18 |   } catch {
     | This ends try { (opened on line 14).

  19 |     return fallback
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  20 |   }
     | This ends } catch { (opened on line 18).

  21 | }
     | This ends readFundingUrl (opened on line 12).

  22 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  23 | export default defineConfig({
     | This tells other files: the main thing in this file is this.

  24 |   define: {
     | Inside the top of the file, this line runs as written: define: {. It happens in order, after the line above it and before the line below it.

  25 |     __FUNDING_URL__: JSON.stringify(readFundingUrl()),
     | Inside the top of the file, this line runs as written: __FUNDING_URL__: JSON.stringify(readFundingUrl()),. It happens in order, after the line above it and before the line below it.

  26 |   },
     | This ends define: { (opened on line 24).

  27 |   plugins: [
     | Inside the top of the file, this line runs as written: plugins: [. It happens in order, after the line above it and before the line below it.

  28 |     react(),
     | Inside the top of the file, this line runs as written: react(),. It happens in order, after the line above it and before the line below it.

  29 |     VitePWA({
     | Inside the top of the file, this line runs as written: VitePWA({. It happens in order, after the line above it and before the line below it.

  30 |       registerType: 'autoUpdate',
     | Inside the top of the file, this line runs as written: registerType: 'autoUpdate',. It happens in order, after the line above it and before the line below it.

  31 |       includeAssets: [
     | Inside the top of the file, this line runs as written: includeAssets: [. It happens in order, after the line above it and before the line below it.

  32 |         'favicon.svg',
     | Inside the top of the file, this line runs as written: 'favicon.svg',. It happens in order, after the line above it and before the line below it.

  33 |         'favicon-32.png',
     | Inside the top of the file, this line runs as written: 'favicon-32.png',. It happens in order, after the line above it and before the line below it.

  34 |         'apple-touch-icon.png',
     | Inside the top of the file, this line runs as written: 'apple-touch-icon.png',. It happens in order, after the line above it and before the line below it.

  35 |         'icons/favicon-16.png',
     | Inside the top of the file, this line runs as written: 'icons/favicon-16.png',. It happens in order, after the line above it and before the line below it.

  36 |         'icons/favicon-32.png',
     | Inside the top of the file, this line runs as written: 'icons/favicon-32.png',. It happens in order, after the line above it and before the line below it.

  37 |         'icons/icon-192.png',
     | Inside the top of the file, this line runs as written: 'icons/icon-192.png',. It happens in order, after the line above it and before the line below it.

  38 |         'icons/icon-512.png',
     | Inside the top of the file, this line runs as written: 'icons/icon-512.png',. It happens in order, after the line above it and before the line below it.

  39 |         'icons/maskable-icon-192.png',
     | Inside the top of the file, this line runs as written: 'icons/maskable-icon-192.png',. It happens in order, after the line above it and before the line below it.

  40 |         'icons/maskable-icon-512.png',
     | Inside the top of the file, this line runs as written: 'icons/maskable-icon-512.png',. It happens in order, after the line above it and before the line below it.

  41 |         'logo-icon.svg',
     | Inside the top of the file, this line runs as written: 'logo-icon.svg',. It happens in order, after the line above it and before the line below it.

  42 |       ],
     | Inside the top of the file, this line runs as written: ],. It happens in order, after the line above it and before the line below it.

  43 |       manifest: {
     | Inside the top of the file, this line runs as written: manifest: {. It happens in order, after the line above it and before the line below it.

  44 |         name: 'JumpyBrain',
     | Inside the top of the file, this line runs as written: name: 'JumpyBrain',. It happens in order, after the line above it and before the line below it.

  45 |         short_name: 'JumpyBrain',
     | Inside the top of the file, this line runs as written: short_name: 'JumpyBrain',. It happens in order, after the line above it and before the line below it.

  46 |         description: 'Focus better. Do more. Feel calm — ADHD-friendly productivity.',
     | Inside the top of the file, this line runs as written: description: 'Focus better. Do more. Feel calm — ADHD-friendly productivity.',. It happens in order, after the line above it and before the line below it.

  47 |         theme_color: '#6366f1',
     | Inside the top of the file, this line runs as written: theme_color: '#6366f1',. It happens in order, after the line above it and before the line below it.

  48 |         background_color: '#0f1020',
     | Inside the top of the file, this line runs as written: background_color: '#0f1020',. It happens in order, after the line above it and before the line below it.

  49 |         display: 'standalone',
     | Inside the top of the file, this line runs as written: display: 'standalone',. It happens in order, after the line above it and before the line below it.

  50 |         start_url: '/',
     | Inside the top of the file, this line runs as written: start_url: '/',. It happens in order, after the line above it and before the line below it.

  51 |         orientation: 'portrait',
     | Inside the top of the file, this line runs as written: orientation: 'portrait',. It happens in order, after the line above it and before the line below it.

  52 |         categories: ['productivity', 'lifestyle'],
     | Inside the top of the file, this line runs as written: categories: ['productivity', 'lifestyle'],. It happens in order, after the line above it and before the line below it.

  53 |         icons: [
     | Inside the top of the file, this line runs as written: icons: [. It happens in order, after the line above it and before the line below it.

  54 |           {
     | Inside the top of the file, this line runs as written: {. It happens in order, after the line above it and before the line below it.

  55 |             src: '/icons/favicon-16.png',
     | Inside the top of the file, this line runs as written: src: '/icons/favicon-16.png',. It happens in order, after the line above it and before the line below it.

  56 |             sizes: '16x16',
     | Inside the top of the file, this line runs as written: sizes: '16x16',. It happens in order, after the line above it and before the line below it.

  57 |             type: 'image/png',
     | Inside the top of the file, this line runs as written: type: 'image/png',. It happens in order, after the line above it and before the line below it.

  58 |           },
     | This ends { (opened on line 54).

  59 |           {
     | Inside the top of the file, this line runs as written: {. It happens in order, after the line above it and before the line below it.

  60 |             src: '/icons/favicon-32.png',
     | Inside the top of the file, this line runs as written: src: '/icons/favicon-32.png',. It happens in order, after the line above it and before the line below it.

  61 |             sizes: '32x32',
     | Inside the top of the file, this line runs as written: sizes: '32x32',. It happens in order, after the line above it and before the line below it.

  62 |             type: 'image/png',
     | Inside the top of the file, this line runs as written: type: 'image/png',. It happens in order, after the line above it and before the line below it.

  63 |           },
     | This ends { (opened on line 59).

  64 |           {
     | Inside the top of the file, this line runs as written: {. It happens in order, after the line above it and before the line below it.

  65 |             src: '/icons/icon-192.png',
     | Inside the top of the file, this line runs as written: src: '/icons/icon-192.png',. It happens in order, after the line above it and before the line below it.

  66 |             sizes: '192x192',
     | Inside the top of the file, this line runs as written: sizes: '192x192',. It happens in order, after the line above it and before the line below it.

  67 |             type: 'image/png',
     | Inside the top of the file, this line runs as written: type: 'image/png',. It happens in order, after the line above it and before the line below it.

  68 |             purpose: 'any',
     | Inside the top of the file, this line runs as written: purpose: 'any',. It happens in order, after the line above it and before the line below it.

  69 |           },
     | This ends { (opened on line 64).

  70 |           {
     | Inside the top of the file, this line runs as written: {. It happens in order, after the line above it and before the line below it.

  71 |             src: '/icons/icon-512.png',
     | Inside the top of the file, this line runs as written: src: '/icons/icon-512.png',. It happens in order, after the line above it and before the line below it.

  72 |             sizes: '512x512',
     | Inside the top of the file, this line runs as written: sizes: '512x512',. It happens in order, after the line above it and before the line below it.

  73 |             type: 'image/png',
     | Inside the top of the file, this line runs as written: type: 'image/png',. It happens in order, after the line above it and before the line below it.

  74 |             purpose: 'any',
     | Inside the top of the file, this line runs as written: purpose: 'any',. It happens in order, after the line above it and before the line below it.

  75 |           },
     | This ends { (opened on line 70).

  76 |           {
     | Inside the top of the file, this line runs as written: {. It happens in order, after the line above it and before the line below it.

  77 |             src: '/icons/maskable-icon-192.png',
     | Inside the top of the file, this line runs as written: src: '/icons/maskable-icon-192.png',. It happens in order, after the line above it and before the line below it.

  78 |             sizes: '192x192',
     | Inside the top of the file, this line runs as written: sizes: '192x192',. It happens in order, after the line above it and before the line below it.

  79 |             type: 'image/png',
     | Inside the top of the file, this line runs as written: type: 'image/png',. It happens in order, after the line above it and before the line below it.

  80 |             purpose: 'maskable',
     | Inside the top of the file, this line runs as written: purpose: 'maskable',. It happens in order, after the line above it and before the line below it.

  81 |           },
     | This ends { (opened on line 76).

  82 |           {
     | Inside the top of the file, this line runs as written: {. It happens in order, after the line above it and before the line below it.

  83 |             src: '/icons/maskable-icon-512.png',
     | Inside the top of the file, this line runs as written: src: '/icons/maskable-icon-512.png',. It happens in order, after the line above it and before the line below it.

  84 |             sizes: '512x512',
     | Inside the top of the file, this line runs as written: sizes: '512x512',. It happens in order, after the line above it and before the line below it.

  85 |             type: 'image/png',
     | Inside the top of the file, this line runs as written: type: 'image/png',. It happens in order, after the line above it and before the line below it.

  86 |             purpose: 'maskable',
     | Inside the top of the file, this line runs as written: purpose: 'maskable',. It happens in order, after the line above it and before the line below it.

  87 |           },
     | This ends { (opened on line 82).

  88 |         ],
     | Inside the top of the file, this line runs as written: ],. It happens in order, after the line above it and before the line below it.

  89 |       },
     | This ends manifest: { (opened on line 43).

  90 |       workbox: {
     | Inside the top of the file, this line runs as written: workbox: {. It happens in order, after the line above it and before the line below it.

  91 |         // index.html is deliberately left out of precaching: a precached
     | A note written for people. The app does not run it.

  92 |         // shell is served straight from the service worker's own cache on
     | A note written for people. The app does not run it.

  93 |         // every navigation, bypassing the Cache-Control headers on
     | A note written for people. The app does not run it.

  94 |         // /index.html (see vercel.json) entirely. That let a stale shell
     | A note written for people. The app does not run it.

  95 |         // referencing deleted hashed asset URLs get stuck serving forever
     | A note written for people. The app does not run it.

  96 |         // on tabs with an already-installed service worker. Leaving html
     | A note written for people. The app does not run it.

  97 |         // off this list means navigation requests hit the network (or the
     | A note written for people. The app does not run it.

  98 |         // browser's own HTTP cache, which does respect those headers)
     | A note written for people. The app does not run it.

  99 |         // instead of the precache. vite-plugin-pwa otherwise defaults to a
     | A note written for people. The app does not run it.

 100 |         // navigateFallback of 'index.html', which registers a Workbox
     | A note written for people. The app does not run it.

 101 |         // NavigationRoute serving all navigations from the precache too --
     | A note written for people. The app does not run it.

 102 |         // disable that as well so navigations are never SW-intercepted.
     | A note written for people. The app does not run it.

 103 |         navigateFallback: undefined,
     | Inside the top of the file, this line runs as written: navigateFallback: undefined,. It happens in order, after the line above it and before the line below it.

 104 |         globPatterns: ['**/*.{js,css,ico,png,svg}'],
     | This ends workbox: { (opened on line 90).

 105 |         globIgnores: ['**/audio/**', '**/sounds/**'],
     | Inside the top of the file, this line runs as written: globIgnores: ['**/audio/**', '**/sounds/**'],. It happens in order, after the line above it and before the line below it.

 106 |         runtimeCaching: [
     | Inside the top of the file, this line runs as written: runtimeCaching: [. It happens in order, after the line above it and before the line below it.

 107 |           {
     | Inside the top of the file, this line runs as written: {. It happens in order, after the line above it and before the line below it.

 108 |             urlPattern: /\.mp3$/i,
     | Inside the top of the file, this line runs as written: urlPattern: /\.mp3$/i,. It happens in order, after the line above it and before the line below it.

 109 |             handler: 'CacheFirst',
     | Inside the top of the file, this line runs as written: handler: 'CacheFirst',. It happens in order, after the line above it and before the line below it.

 110 |             options: {
     | Inside the top of the file, this line runs as written: options: {. It happens in order, after the line above it and before the line below it.

 111 |               cacheName: 'audio-cache',
     | Inside the top of the file, this line runs as written: cacheName: 'audio-cache',. It happens in order, after the line above it and before the line below it.

 112 |               expiration: {
     | Inside the top of the file, this line runs as written: expiration: {. It happens in order, after the line above it and before the line below it.

 113 |                 maxEntries: 10,
     | Inside the top of the file, this line runs as written: maxEntries: 10,. It happens in order, after the line above it and before the line below it.

 114 |                 maxAgeSeconds: 60 * 60 * 24 * 30,
     | Inside the top of the file, this line runs as written: maxAgeSeconds: 60 * 60 * 24 * 30,. It happens in order, after the line above it and before the line below it.

 115 |               },
     | This ends expiration: { (opened on line 112).

 116 |             },
     | This ends options: { (opened on line 110).

 117 |           },
     | This ends { (opened on line 107).

 118 |           {
     | Inside the top of the file, this line runs as written: {. It happens in order, after the line above it and before the line below it.

 119 |             urlPattern: /^https:\/\/.*\/api\/.*/i,
     | Inside the top of the file, this line runs as written: urlPattern: /^https:\/\/.*\/api\/.*/i,. It happens in order, after the line above it and before the line below it.

 120 |             handler: 'NetworkFirst',
     | Inside the top of the file, this line runs as written: handler: 'NetworkFirst',. It happens in order, after the line above it and before the line below it.

 121 |             options: {
     | Inside the top of the file, this line runs as written: options: {. It happens in order, after the line above it and before the line below it.

 122 |               cacheName: 'api-cache',
     | Inside the top of the file, this line runs as written: cacheName: 'api-cache',. It happens in order, after the line above it and before the line below it.

 123 |               expiration: {
     | Inside the top of the file, this line runs as written: expiration: {. It happens in order, after the line above it and before the line below it.

 124 |                 maxEntries: 50,
     | Inside the top of the file, this line runs as written: maxEntries: 50,. It happens in order, after the line above it and before the line below it.

 125 |                 maxAgeSeconds: 60 * 5,
     | Inside the top of the file, this line runs as written: maxAgeSeconds: 60 * 5,. It happens in order, after the line above it and before the line below it.

 126 |               },
     | This ends expiration: { (opened on line 123).

 127 |               networkTimeoutSeconds: 10,
     | Inside the top of the file, this line runs as written: networkTimeoutSeconds: 10,. It happens in order, after the line above it and before the line below it.

 128 |             },
     | This ends options: { (opened on line 121).

 129 |           },
     | This ends { (opened on line 118).

 130 |           {
     | Inside the top of the file, this line runs as written: {. It happens in order, after the line above it and before the line below it.

 131 |             urlPattern: /^https:\/\/fonts\.googleapis\.com\/.*/i,
     | Inside the top of the file, this line runs as written: urlPattern: /^https:\/\/fonts\.googleapis\.com\/.*/i,. It happens in order, after the line above it and before the line below it.

 132 |             handler: 'CacheFirst',
     | Inside the top of the file, this line runs as written: handler: 'CacheFirst',. It happens in order, after the line above it and before the line below it.

 133 |             options: {
     | Inside the top of the file, this line runs as written: options: {. It happens in order, after the line above it and before the line below it.

 134 |               cacheName: 'google-fonts-cache',
     | Inside the top of the file, this line runs as written: cacheName: 'google-fonts-cache',. It happens in order, after the line above it and before the line below it.

 135 |               expiration: {
     | Inside the top of the file, this line runs as written: expiration: {. It happens in order, after the line above it and before the line below it.

 136 |                 maxEntries: 10,
     | Inside the top of the file, this line runs as written: maxEntries: 10,. It happens in order, after the line above it and before the line below it.

 137 |                 maxAgeSeconds: 60 * 60 * 24 * 365,
     | Inside the top of the file, this line runs as written: maxAgeSeconds: 60 * 60 * 24 * 365,. It happens in order, after the line above it and before the line below it.

 138 |               },
     | This ends expiration: { (opened on line 135).

 139 |             },
     | This ends options: { (opened on line 133).

 140 |           },
     | This ends { (opened on line 130).

 141 |         ],
     | Inside the top of the file, this line runs as written: ],. It happens in order, after the line above it and before the line below it.

 142 |       },
     | This ends workbox: { (opened on line 90).

 143 |       devOptions: {
     | Inside the top of the file, this line runs as written: devOptions: {. It happens in order, after the line above it and before the line below it.

 144 |         enabled: true,
     | Inside the top of the file, this line runs as written: enabled: true,. It happens in order, after the line above it and before the line below it.

 145 |       },
     | This ends devOptions: { (opened on line 143).

 146 |     }),
     | This ends VitePWA({ (opened on line 29).

 147 |   ],
     | Inside the top of the file, this line runs as written: ],. It happens in order, after the line above it and before the line below it.

 148 |   server: {
     | Inside the top of the file, this line runs as written: server: {. It happens in order, after the line above it and before the line below it.

 149 |     port: 5173,
     | Inside the top of the file, this line runs as written: port: 5173,. It happens in order, after the line above it and before the line below it.

 150 |     proxy: {
     | Inside the top of the file, this line runs as written: proxy: {. It happens in order, after the line above it and before the line below it.

 151 |       '/api': {
     | Inside the top of the file, this line runs as written: '/api': {. It happens in order, after the line above it and before the line below it.

 152 |         target: 'http://localhost:3001',
     | Inside the top of the file, this line runs as written: target: 'http://localhost:3001',. It happens in order, after the line above it and before the line below it.

 153 |         changeOrigin: true,
     | Inside the top of the file, this line runs as written: changeOrigin: true,. It happens in order, after the line above it and before the line below it.

 154 |       },
     | This ends '/api': { (opened on line 151).

 155 |     },
     | This ends proxy: { (opened on line 150).

 156 |   },
     | This ends server: { (opened on line 148).

 157 | })
     | This ends export default defineConfig({ (opened on line 23).

