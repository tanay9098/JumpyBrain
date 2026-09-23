# `capacitor.config.ts`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import type { CapacitorConfig } from '@capacitor/cli';
     | Import for Capacitor's native app id and web dir: `import type { CapacitorConfig } from '@capacitor/cli';`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   2 | 
     | Blank line in `capacitor.config.ts` (Capacitor's native app id and web dir), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   3 | const config: CapacitorConfig = {
     | In `the top of the file` (capacitor.config.ts): declaration `const config: CapacitorConfig = {`.

   4 |   appId: 'com.jumpybrain.app',
     | In `the top of the file` (capacitor.config.ts): statement `appId: 'com.jumpybrain.app',`. It runs when the top of the file runs, in order, before the next line of the same function.

   5 |   appName: 'JumpyBrain',
     | In `the top of the file` (capacitor.config.ts): statement `appName: 'JumpyBrain',`. It runs when the top of the file runs, in order, before the next line of the same function.

   6 |   webDir: 'dist',
     | In `the top of the file` (capacitor.config.ts): statement `webDir: 'dist',`. It runs when the top of the file runs, in order, before the next line of the same function.

   7 |   server: {
     | In `the top of the file` (capacitor.config.ts): statement `server: {`. It runs when the top of the file runs, in order, before the next line of the same function.

   8 |     androidScheme: 'https',
     | In `the top of the file` (capacitor.config.ts): statement `androidScheme: 'https',`. It runs when the top of the file runs, in order, before the next line of the same function.

   9 |   },
     | In `the top of the file` (capacitor.config.ts): `},` closes server: { (opened on line 7). Names declared inside that block end here.

  10 | };
     | In `the top of the file` (capacitor.config.ts): `};` closes const config: CapacitorConfig = { (opened on line 3). Names declared inside that block end here.

  11 | 
     | Blank line in `capacitor.config.ts` (Capacitor's native app id and web dir), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  12 | export default config;
     | Default export of Capacitor's native app id and web dir: `export default config;`. Importers that write `import X from 'capacitor.config.ts'` receive this value.

