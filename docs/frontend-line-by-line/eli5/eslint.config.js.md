# `eslint.config.js`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import js from '@eslint/js'
     | This file borrows a tool another file already made.

   2 | import globals from 'globals'
     | This file borrows a tool another file already made.

   3 | import reactHooks from 'eslint-plugin-react-hooks'
     | Borrows React so this file can remember things and draw the screen.

   4 | import reactRefresh from 'eslint-plugin-react-refresh'
     | Borrows React so this file can remember things and draw the screen.

   5 | import { defineConfig, globalIgnores } from 'eslint/config'
     | This file borrows a tool another file already made.

   6 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   7 | export default defineConfig([
     | This tells other files: the main thing in this file is this.

   8 |   globalIgnores(['dist']),
     | Inside the top of the file, this line runs as written: globalIgnores(['dist']),. It happens in order, after the line above it and before the line below it.

   9 |   {
     | Inside the top of the file, this line runs as written: {. It happens in order, after the line above it and before the line below it.

  10 |     files: ['**/*.{js,jsx}'],
     | This ends { (opened on line 9).

  11 |     extends: [
     | Inside the top of the file, this line runs as written: extends: [. It happens in order, after the line above it and before the line below it.

  12 |       js.configs.recommended,
     | Inside the top of the file, this line runs as written: js.configs.recommended,. It happens in order, after the line above it and before the line below it.

  13 |       reactHooks.configs['recommended-latest'],
     | Inside the top of the file, this line runs as written: reactHooks.configs['recommended-latest'],. It happens in order, after the line above it and before the line below it.

  14 |       reactRefresh.configs.vite,
     | Inside the top of the file, this line runs as written: reactRefresh.configs.vite,. It happens in order, after the line above it and before the line below it.

  15 |     ],
     | Inside the top of the file, this line runs as written: ],. It happens in order, after the line above it and before the line below it.

  16 |     languageOptions: {
     | Inside the top of the file, this line runs as written: languageOptions: {. It happens in order, after the line above it and before the line below it.

  17 |       ecmaVersion: 2020,
     | Inside the top of the file, this line runs as written: ecmaVersion: 2020,. It happens in order, after the line above it and before the line below it.

  18 |       globals: { ...globals.browser, __FUNDING_URL__: 'readonly' },
     | This ends languageOptions: { (opened on line 16).

  19 |       parserOptions: {
     | Inside the top of the file, this line runs as written: parserOptions: {. It happens in order, after the line above it and before the line below it.

  20 |         ecmaVersion: 'latest',
     | Inside the top of the file, this line runs as written: ecmaVersion: 'latest',. It happens in order, after the line above it and before the line below it.

  21 |         ecmaFeatures: { jsx: true },
     | This ends parserOptions: { (opened on line 19).

  22 |         sourceType: 'module',
     | Inside the top of the file, this line runs as written: sourceType: 'module',. It happens in order, after the line above it and before the line below it.

  23 |       },
     | This ends parserOptions: { (opened on line 19).

  24 |     },
     | This ends languageOptions: { (opened on line 16).

  25 |     rules: {
     | Inside the top of the file, this line runs as written: rules: {. It happens in order, after the line above it and before the line below it.

  26 |       'no-unused-vars': ['error', { varsIgnorePattern: '^[A-Z_]' }],
     | This ends rules: { (opened on line 25).

  27 |     },
     | This ends rules: { (opened on line 25).

  28 |   },
     | This ends { (opened on line 9).

  29 | ])
     | Inside the top of the file, this line runs as written: ]). It happens in order, after the line above it and before the line below it.

