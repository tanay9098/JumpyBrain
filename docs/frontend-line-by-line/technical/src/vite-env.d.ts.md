# `src/vite-env.d.ts`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | /// <reference types="vite/client" />
     | Comment inside the top of the file. Not executed. It documents the next code: / <reference types="vite/client" />

   2 | /// <reference types="vite-plugin-pwa/client" />
     | Comment inside the top of the file. Not executed. It documents the next code: / <reference types="vite-plugin-pwa/client" />

   3 | 
     | Blank line in `src/vite-env.d.ts` (TypeScript's knowledge of Vite globals), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   4 | declare const __FUNDING_URL__: string
     | In `the top of the file` (src/vite-env.d.ts): statement `declare const __FUNDING_URL__: string`. It runs when the top of the file runs, in order, before the next line of the same function.

