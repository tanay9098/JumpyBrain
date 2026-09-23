# `postcss.config.js`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | export default {
     | Default export of PostCSS plugin list (Tailwind): `export default {`. Importers that write `import X from 'postcss.config.js'` receive this value.

   2 |   plugins: {
     | In `the top of the file` (postcss.config.js): statement `plugins: {`. It runs when the top of the file runs, in order, before the next line of the same function.

   3 |     tailwindcss: {},
     | In `the top of the file` (postcss.config.js): `tailwindcss: {},` closes plugins: { (opened on line 2). Names declared inside that block end here.

   4 |     autoprefixer: {},
     | In `the top of the file` (postcss.config.js): `autoprefixer: {},` closes plugins: { (opened on line 2). Names declared inside that block end here.

   5 |   },
     | In `the top of the file` (postcss.config.js): `},` closes plugins: { (opened on line 2). Names declared inside that block end here.

   6 | }
     | In `the top of the file` (postcss.config.js): `}` closes export default { (opened on line 1). Names declared inside that block end here.

