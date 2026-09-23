# `src/utils/notify.js`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | export function notify(title, body) {
     | This lets another file use this piece by its name.

   2 |   if (!("Notification" in window)) return;
     | This asks a yes-or-no question. The next bit runs only on yes.

   3 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   4 |   if (Notification.permission === "granted") {
     | This asks a yes-or-no question. The next bit runs only on yes.

   5 |     const n = new Notification(title, {
     | This gives a short name to a value so the rest of notify can use it.

   6 |       body,
     | Inside notify, this line runs as written: body,. It happens in order, after the line above it and before the line below it.

   7 |       icon: "/icons/icon-192.png"
     | Inside notify, this line runs as written: icon: "/icons/icon-192.png". It happens in order, after the line above it and before the line below it.

   8 |     });
     | This ends const n = new Notification(title, { (opened on line 5).

   9 |     n.onclick = () => {
     | Inside notify, this line runs as written: n.onclick = () => {. It happens in order, after the line above it and before the line below it.

  10 |       window.focus();
     | Inside notify, this line runs as written: window.focus();. It happens in order, after the line above it and before the line below it.

  11 |       n.close();
     | Inside notify, this line runs as written: n.close();. It happens in order, after the line above it and before the line below it.

  12 |     };
     | This ends n.onclick = () => { (opened on line 9).

  13 |   }
     | This ends if (Notification.permission === "granted (opened on line 4).

  14 | }
     | This ends notify (opened on line 1).

