# `capacitor.config.ts`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import type { CapacitorConfig } from '@capacitor/cli';
     | This file borrows a tool another file already made.

   2 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   3 | const config: CapacitorConfig = {
     | This gives a short name to a value so the rest of the top of the file can use it.

   4 |   appId: 'com.jumpybrain.app',
     | Inside the top of the file, this line runs as written: appId: 'com.jumpybrain.app',. It happens in order, after the line above it and before the line below it.

   5 |   appName: 'JumpyBrain',
     | Inside the top of the file, this line runs as written: appName: 'JumpyBrain',. It happens in order, after the line above it and before the line below it.

   6 |   webDir: 'dist',
     | Inside the top of the file, this line runs as written: webDir: 'dist',. It happens in order, after the line above it and before the line below it.

   7 |   server: {
     | Inside the top of the file, this line runs as written: server: {. It happens in order, after the line above it and before the line below it.

   8 |     androidScheme: 'https',
     | Inside the top of the file, this line runs as written: androidScheme: 'https',. It happens in order, after the line above it and before the line below it.

   9 |   },
     | This ends server: { (opened on line 7).

  10 | };
     | This ends const config: CapacitorConfig = { (opened on line 3).

  11 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  12 | export default config;
     | This tells other files: the main thing in this file is this.

