# `src/utils/sound.js`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import { Howl } from "howler";
     | Borrows a sound player.

   2 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   3 | export const tabAlertSound = new Howl({
     | This lets another file use this piece by its name.

   4 |   src: ["/sounds/tab-alert.mp3"],
     | Inside the top of the file, this line runs as written: src: ["/sounds/tab-alert.mp3"],. It happens in order, after the line above it and before the line below it.

   5 |   volume: 0.5
     | Inside the top of the file, this line runs as written: volume: 0.5. It happens in order, after the line above it and before the line below it.

   6 | });
     | This ends export const tabAlertSound = new Howl({ (opened on line 3).

