# `eslint.config.js`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import js from '@eslint/js'
     | Import for lint rules for the frontend: `import js from '@eslint/js'`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   2 | import globals from 'globals'
     | Import for lint rules for the frontend: `import globals from 'globals'`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   3 | import reactHooks from 'eslint-plugin-react-hooks'
     | Import for lint rules for the frontend: `import reactHooks from 'eslint-plugin-react-hooks'`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   4 | import reactRefresh from 'eslint-plugin-react-refresh'
     | Import for lint rules for the frontend: `import reactRefresh from 'eslint-plugin-react-refresh'`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   5 | import { defineConfig, globalIgnores } from 'eslint/config'
     | Import for lint rules for the frontend: `import { defineConfig, globalIgnores } from 'eslint/config'`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   6 | 
     | Blank line in `eslint.config.js` (lint rules for the frontend), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   7 | export default defineConfig([
     | Default export of lint rules for the frontend: `export default defineConfig([`. Importers that write `import X from 'eslint.config.js'` receive this value.

   8 |   globalIgnores(['dist']),
     | In `the top of the file` (eslint.config.js): statement `globalIgnores(['dist']),`. It runs when the top of the file runs, in order, before the next line of the same function.

   9 |   {
     | In `the top of the file` (eslint.config.js): statement `{`. It runs when the top of the file runs, in order, before the next line of the same function.

  10 |     files: ['**/*.{js,jsx}'],
     | In `the top of the file` (eslint.config.js): `files: ['**/*.{js,jsx}'],` closes { (opened on line 9). Names declared inside that block end here.

  11 |     extends: [
     | In `the top of the file` (eslint.config.js): statement `extends: [`. It runs when the top of the file runs, in order, before the next line of the same function.

  12 |       js.configs.recommended,
     | In `the top of the file` (eslint.config.js): statement `js.configs.recommended,`. It runs when the top of the file runs, in order, before the next line of the same function.

  13 |       reactHooks.configs['recommended-latest'],
     | In `the top of the file` (eslint.config.js): statement `reactHooks.configs['recommended-latest'],`. It runs when the top of the file runs, in order, before the next line of the same function.

  14 |       reactRefresh.configs.vite,
     | In `the top of the file` (eslint.config.js): statement `reactRefresh.configs.vite,`. It runs when the top of the file runs, in order, before the next line of the same function.

  15 |     ],
     | In `the top of the file` (eslint.config.js): statement `],`. It runs when the top of the file runs, in order, before the next line of the same function.

  16 |     languageOptions: {
     | In `the top of the file` (eslint.config.js): statement `languageOptions: {`. It runs when the top of the file runs, in order, before the next line of the same function.

  17 |       ecmaVersion: 2020,
     | In `the top of the file` (eslint.config.js): statement `ecmaVersion: 2020,`. It runs when the top of the file runs, in order, before the next line of the same function.

  18 |       globals: { ...globals.browser, __FUNDING_URL__: 'readonly' },
     | In `the top of the file` (eslint.config.js): `globals: { ...globals.browser, __FUNDING_URL__: 'readonly' },` closes languageOptions: { (opened on line 16). Names declared inside that block end here.

  19 |       parserOptions: {
     | In `the top of the file` (eslint.config.js): statement `parserOptions: {`. It runs when the top of the file runs, in order, before the next line of the same function.

  20 |         ecmaVersion: 'latest',
     | In `the top of the file` (eslint.config.js): statement `ecmaVersion: 'latest',`. It runs when the top of the file runs, in order, before the next line of the same function.

  21 |         ecmaFeatures: { jsx: true },
     | In `the top of the file` (eslint.config.js): `ecmaFeatures: { jsx: true },` closes parserOptions: { (opened on line 19). Names declared inside that block end here.

  22 |         sourceType: 'module',
     | In `the top of the file` (eslint.config.js): statement `sourceType: 'module',`. It runs when the top of the file runs, in order, before the next line of the same function.

  23 |       },
     | In `the top of the file` (eslint.config.js): `},` closes parserOptions: { (opened on line 19). Names declared inside that block end here.

  24 |     },
     | In `the top of the file` (eslint.config.js): `},` closes languageOptions: { (opened on line 16). Names declared inside that block end here.

  25 |     rules: {
     | In `the top of the file` (eslint.config.js): statement `rules: {`. It runs when the top of the file runs, in order, before the next line of the same function.

  26 |       'no-unused-vars': ['error', { varsIgnorePattern: '^[A-Z_]' }],
     | In `the top of the file` (eslint.config.js): `'no-unused-vars': ['error', { varsIgnorePattern: '^[A-Z_]' }],` closes rules: { (opened on line 25). Names declared inside that block end here.

  27 |     },
     | In `the top of the file` (eslint.config.js): `},` closes rules: { (opened on line 25). Names declared inside that block end here.

  28 |   },
     | In `the top of the file` (eslint.config.js): `},` closes { (opened on line 9). Names declared inside that block end here.

  29 | ])
     | In `the top of the file` (eslint.config.js): statement `])`. It runs when the top of the file runs, in order, before the next line of the same function.

