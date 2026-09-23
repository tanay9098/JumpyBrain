# `tailwind.config.js`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | /** @type {import('tailwindcss').Config} */
     | A note for people. The app skips this line.

   2 | export default {
     | This tells other files: the main thing in this file is this.

   3 |   content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
     | This ends export default { (opened on line 2).

   4 |   theme: {
     | Inside the top of the file, this line runs as written: theme: {. It happens in order, after the line above it and before the line below it.

   5 |     extend: {
     | Inside the top of the file, this line runs as written: extend: {. It happens in order, after the line above it and before the line below it.

   6 |       colors: {
     | Inside the top of the file, this line runs as written: colors: {. It happens in order, after the line above it and before the line below it.

   7 |         accent: 'var(--accent)',
     | Inside the top of the file, this line runs as written: accent: 'var(--accent)',. It happens in order, after the line above it and before the line below it.

   8 |         'accent-light': 'var(--accent-light)',
     | Inside the top of the file, this line runs as written: 'accent-light': 'var(--accent-light)',. It happens in order, after the line above it and before the line below it.

   9 |         'bg-primary': 'var(--bg-primary)',
     | Inside the top of the file, this line runs as written: 'bg-primary': 'var(--bg-primary)',. It happens in order, after the line above it and before the line below it.

  10 |         'bg-secondary': 'var(--bg-secondary)',
     | Inside the top of the file, this line runs as written: 'bg-secondary': 'var(--bg-secondary)',. It happens in order, after the line above it and before the line below it.

  11 |         'text-primary': 'var(--text-primary)',
     | Inside the top of the file, this line runs as written: 'text-primary': 'var(--text-primary)',. It happens in order, after the line above it and before the line below it.

  12 |         'text-secondary': 'var(--text-secondary)',
     | Inside the top of the file, this line runs as written: 'text-secondary': 'var(--text-secondary)',. It happens in order, after the line above it and before the line below it.

  13 |       },
     | This ends colors: { (opened on line 6).

  14 |     },
     | This ends extend: { (opened on line 5).

  15 |   },
     | This ends theme: { (opened on line 4).

  16 |   plugins: [],
     | Inside the top of the file, this line runs as written: plugins: [],. It happens in order, after the line above it and before the line below it.

  17 | }
     | This ends export default { (opened on line 2).

