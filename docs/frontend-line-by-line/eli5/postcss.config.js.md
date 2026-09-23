# `postcss.config.js`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | export default {
     | This tells other files: the main thing in this file is this.

   2 |   plugins: {
     | Inside the top of the file, this line runs as written: plugins: {. It happens in order, after the line above it and before the line below it.

   3 |     tailwindcss: {},
     | This ends plugins: { (opened on line 2).

   4 |     autoprefixer: {},
     | This ends plugins: { (opened on line 2).

   5 |   },
     | This ends plugins: { (opened on line 2).

   6 | }
     | This ends export default { (opened on line 1).

