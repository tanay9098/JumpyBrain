# `src/utils/sound.js`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import { Howl } from "howler";
     | Import for the tab-switch alert sound: `import { Howl } from "howler";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   2 | 
     | Blank line in `src/utils/sound.js` (the tab-switch alert sound), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   3 | export const tabAlertSound = new Howl({
     | Named export from the tab-switch alert sound: `export const tabAlertSound = new Howl({`.

   4 |   src: ["/sounds/tab-alert.mp3"],
     | In `the top of the file` (src/utils/sound.js): statement `src: ["/sounds/tab-alert.mp3"],`. It runs when the top of the file runs, in order, before the next line of the same function.

   5 |   volume: 0.5
     | In `the top of the file` (src/utils/sound.js): statement `volume: 0.5`. It runs when the top of the file runs, in order, before the next line of the same function.

   6 | });
     | In `the top of the file` (src/utils/sound.js): `});` closes export const tabAlertSound = new Howl({ (opened on line 3). Names declared inside that block end here.

