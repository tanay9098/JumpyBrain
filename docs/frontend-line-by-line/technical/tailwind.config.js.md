# `tailwind.config.js`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | /** @type {import('tailwindcss').Config} */
     | Comment inside the top of the file. Not executed. Text: /** @type {import('tailwindcss').Config} */

   2 | export default {
     | Default export of Tailwind content paths and theme: `export default {`. Importers that write `import X from 'tailwind.config.js'` receive this value.

   3 |   content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
     | In `the top of the file` (tailwind.config.js): `content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],` closes export default { (opened on line 2). Names declared inside that block end here.

   4 |   theme: {
     | In `the top of the file` (tailwind.config.js): statement `theme: {`. It runs when the top of the file runs, in order, before the next line of the same function.

   5 |     extend: {
     | In `the top of the file` (tailwind.config.js): statement `extend: {`. It runs when the top of the file runs, in order, before the next line of the same function.

   6 |       colors: {
     | In `the top of the file` (tailwind.config.js): statement `colors: {`. It runs when the top of the file runs, in order, before the next line of the same function.

   7 |         accent: 'var(--accent)',
     | In `the top of the file` (tailwind.config.js): statement `accent: 'var(--accent)',`. It runs when the top of the file runs, in order, before the next line of the same function.

   8 |         'accent-light': 'var(--accent-light)',
     | In `the top of the file` (tailwind.config.js): statement `'accent-light': 'var(--accent-light)',`. It runs when the top of the file runs, in order, before the next line of the same function.

   9 |         'bg-primary': 'var(--bg-primary)',
     | In `the top of the file` (tailwind.config.js): statement `'bg-primary': 'var(--bg-primary)',`. It runs when the top of the file runs, in order, before the next line of the same function.

  10 |         'bg-secondary': 'var(--bg-secondary)',
     | In `the top of the file` (tailwind.config.js): statement `'bg-secondary': 'var(--bg-secondary)',`. It runs when the top of the file runs, in order, before the next line of the same function.

  11 |         'text-primary': 'var(--text-primary)',
     | In `the top of the file` (tailwind.config.js): statement `'text-primary': 'var(--text-primary)',`. It runs when the top of the file runs, in order, before the next line of the same function.

  12 |         'text-secondary': 'var(--text-secondary)',
     | In `the top of the file` (tailwind.config.js): statement `'text-secondary': 'var(--text-secondary)',`. It runs when the top of the file runs, in order, before the next line of the same function.

  13 |       },
     | In `the top of the file` (tailwind.config.js): `},` closes colors: { (opened on line 6). Names declared inside that block end here.

  14 |     },
     | In `the top of the file` (tailwind.config.js): `},` closes extend: { (opened on line 5). Names declared inside that block end here.

  15 |   },
     | In `the top of the file` (tailwind.config.js): `},` closes theme: { (opened on line 4). Names declared inside that block end here.

  16 |   plugins: [],
     | In `the top of the file` (tailwind.config.js): statement `plugins: [],`. It runs when the top of the file runs, in order, before the next line of the same function.

  17 | }
     | In `the top of the file` (tailwind.config.js): `}` closes export default { (opened on line 2). Names declared inside that block end here.

