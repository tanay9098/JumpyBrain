# `src/components/Affirmations.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import { forwardRef, useImperativeHandle, useState } from "react";
     | Borrows React so this file can remember things and draw the screen.

   2 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   3 | const messages = {
     | Five encouragement strings keyed by context: tab-change, day-start, day-end, task-complete, task-incomplete. Affirmations shows one of them.

   4 |   "tab-change": "Noticed a tab switch — one slow breath, then come back. You’ve got this.",
     | Inside the top of the file, this line runs as written: "tab-change": "Noticed a tab switch — one slow breath, then come back. You’ve got this.",. It happens in order, after the line above it and before the line below it.

   5 |   "day-start": "Good morning — pick 2 focus tasks and start small.",
     | Inside the top of the file, this line runs as written: "day-start": "Good morning — pick 2 focus tasks and start small.",. It happens in order, after the line above it and before the line below it.

   6 |   "day-end": "You did a lot today. Note one small win — celebrate it.",
     | Inside the top of the file, this line runs as written: "day-end": "You did a lot today. Note one small win — celebrate it.",. It happens in order, after the line above it and before the line below it.

   7 |   "task-complete": "Nice work! Fist bump 👊 — celebrate briefly, then keep going.",
     | Inside the top of the file, this line runs as written: "task-complete": "Nice work! Fist bump 👊 — celebrate briefly, then keep going.",. It happens in order, after the line above it and before the line below it.

   8 |   "task-incomplete": "It’s fine. Break it down smaller and try again.",
     | Inside the top of the file, this line runs as written: "task-incomplete": "It’s fine. Break it down smaller and try again.",. It happens in order, after the line above it and before the line below it.

   9 | };
     | This ends const messages = { (opened on line 3).

  10 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  11 | const Affirmations = forwardRef((props, ref) => {
     | This gives a short name to a value so the rest of the top of the file can use it.

  12 |   const [msg, setMsg] = useState("Ready when you are.");
     | This gives a short name to a value so the rest of the top of the file can use it.

  13 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  14 |   useImperativeHandle(ref, () => ({
     | Inside the top of the file, this line runs as written: useImperativeHandle(ref, () => ({. It happens in order, after the line above it and before the line below it.

  15 |     random() {
     | Inside the top of the file, this line runs as written: random() {. It happens in order, after the line above it and before the line below it.

  16 |       const arr = Object.values(messages);
     | This gives a short name to a value so the rest of the top of the file can use it.

  17 |       const m = arr[Math.floor(Math.random() * arr.length)];
     | This gives a short name to a value so the rest of the top of the file can use it.

  18 |       setMsg(m);
     | Inside the top of the file, this line runs as written: setMsg(m);. It happens in order, after the line above it and before the line below it.

  19 |       return m;
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  20 |     },
     | This ends random() { (opened on line 15).

  21 |     messageForContext(ctx) {
     | Inside the top of the file, this line runs as written: messageForContext(ctx) {. It happens in order, after the line above it and before the line below it.

  22 |       const m = messages[ctx] || this.random();
     | This gives a short name to a value so the rest of the top of the file can use it.

  23 |       setMsg(m);
     | Inside the top of the file, this line runs as written: setMsg(m);. It happens in order, after the line above it and before the line below it.

  24 |       return m;
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  25 |     },
     | This ends messageForContext(ctx) { (opened on line 21).

  26 |   }));
     | This ends useImperativeHandle(ref, () => ({ (opened on line 14).

  27 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  28 |   return <div className="affirmation-card">{msg}</div>;
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  29 | });
     | This ends const Affirmations = forwardRef((props, ref) =>  (opened on line 11).

  30 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  31 | export default Affirmations;
     | This tells other files: the main thing in this file is this.

