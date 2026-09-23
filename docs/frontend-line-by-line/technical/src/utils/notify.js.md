# `src/utils/notify.js`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | export function notify(title, body) {
     | Named export from desktop notifications for deadlines and focus nudges: `export function notify(title, body) {`.

   2 |   if (!("Notification" in window)) return;
     | In `notify` (src/utils/notify.js): branch `if (!("Notification" in window)) return;`. Only one side runs.

   3 | 
     | Blank line in `src/utils/notify.js` (desktop notifications for deadlines and focus nudges), inside notify. The parser skips it. It separates the previous statement from the next so the function is readable.

   4 |   if (Notification.permission === "granted") {
     | In `notify` (src/utils/notify.js): branch `if (Notification.permission === "granted") {`. Only one side runs.

   5 |     const n = new Notification(title, {
     | In `notify` (src/utils/notify.js): `n` is assigned `new Notification(title, {`. Later lines in this function read that name.

   6 |       body,
     | In `notify` (src/utils/notify.js): statement `body,`. It runs when notify runs, in order, before the next line of the same function.

   7 |       icon: "/icons/icon-192.png"
     | In `notify` (src/utils/notify.js): statement `icon: "/icons/icon-192.png"`. It runs when notify runs, in order, before the next line of the same function.

   8 |     });
     | In `notify` (src/utils/notify.js): `});` closes const n = new Notification(title, { (opened on line 5). Names declared inside that block end here.

   9 |     n.onclick = () => {
     | In `notify` (src/utils/notify.js): statement `n.onclick = () => {`. It runs when notify runs, in order, before the next line of the same function.

  10 |       window.focus();
     | In `notify` (src/utils/notify.js): statement `window.focus();`. It runs when notify runs, in order, before the next line of the same function.

  11 |       n.close();
     | In `notify` (src/utils/notify.js): statement `n.close();`. It runs when notify runs, in order, before the next line of the same function.

  12 |     };
     | In `notify` (src/utils/notify.js): `};` closes n.onclick = () => { (opened on line 9). Names declared inside that block end here.

  13 |   }
     | In `notify` (src/utils/notify.js): `}` closes if (Notification.permission === "granted (opened on line 4). Names declared inside that block end here.

  14 | }
     | In `notify` (src/utils/notify.js): `}` closes notify (opened on line 1). Names declared inside that block end here.

