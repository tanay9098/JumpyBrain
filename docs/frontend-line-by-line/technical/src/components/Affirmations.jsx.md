# `src/components/Affirmations.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import { forwardRef, useImperativeHandle, useState } from "react";
     | Import for short encouragement lines the timer and mindfulness can request: `import { forwardRef, useImperativeHandle, useState } from "react";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   2 | 
     | Blank line in `src/components/Affirmations.jsx` (short encouragement lines the timer and mindfulness can request), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   3 | const messages = {
     | In `the top of the file` (src/components/Affirmations.jsx): `messages`: Five encouragement strings keyed by context: tab-change, day-start, day-end, task-complete, task-incomplete. Affirmations shows one of them. The code is `const messages = {`.

   4 |   "tab-change": "Noticed a tab switch — one slow breath, then come back. You’ve got this.",
     | In `the top of the file` (src/components/Affirmations.jsx): statement `"tab-change": "Noticed a tab switch — one slow breath, then come back. You’ve got this.",`. It runs when the top of the file runs, in order, before the next line of the same function.

   5 |   "day-start": "Good morning — pick 2 focus tasks and start small.",
     | In `the top of the file` (src/components/Affirmations.jsx): statement `"day-start": "Good morning — pick 2 focus tasks and start small.",`. It runs when the top of the file runs, in order, before the next line of the same function.

   6 |   "day-end": "You did a lot today. Note one small win — celebrate it.",
     | In `the top of the file` (src/components/Affirmations.jsx): statement `"day-end": "You did a lot today. Note one small win — celebrate it.",`. It runs when the top of the file runs, in order, before the next line of the same function.

   7 |   "task-complete": "Nice work! Fist bump 👊 — celebrate briefly, then keep going.",
     | In `the top of the file` (src/components/Affirmations.jsx): statement `"task-complete": "Nice work! Fist bump 👊 — celebrate briefly, then keep going.",`. It runs when the top of the file runs, in order, before the next line of the same function.

   8 |   "task-incomplete": "It’s fine. Break it down smaller and try again.",
     | In `the top of the file` (src/components/Affirmations.jsx): statement `"task-incomplete": "It’s fine. Break it down smaller and try again.",`. It runs when the top of the file runs, in order, before the next line of the same function.

   9 | };
     | In `the top of the file` (src/components/Affirmations.jsx): `};` closes const messages = { (opened on line 3). Names declared inside that block end here.

  10 | 
     | Blank line in `src/components/Affirmations.jsx` (short encouragement lines the timer and mindfulness can request), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  11 | const Affirmations = forwardRef((props, ref) => {
     | In `the top of the file` (src/components/Affirmations.jsx): `Affirmations` is assigned `forwardRef((props, ref) => {`. Later lines in this function read that name.

  12 |   const [msg, setMsg] = useState("Ready when you are.");
     | In `the top of the file` (src/components/Affirmations.jsx): React state `msg, setMsg`. The value survives re-renders. Calling the setter re-renders this component. `const [msg, setMsg] = useState("Ready when you are.");`

  13 | 
     | Blank line in `src/components/Affirmations.jsx` (short encouragement lines the timer and mindfulness can request), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  14 |   useImperativeHandle(ref, () => ({
     | In `the top of the file` (src/components/Affirmations.jsx): statement `useImperativeHandle(ref, () => ({`. It runs when the top of the file runs, in order, before the next line of the same function.

  15 |     random() {
     | In `the top of the file` (src/components/Affirmations.jsx): statement `random() {`. It runs when the top of the file runs, in order, before the next line of the same function.

  16 |       const arr = Object.values(messages);
     | In `the top of the file` (src/components/Affirmations.jsx): `arr` is assigned `Object.values(messages);`. Later lines in this function read that name.

  17 |       const m = arr[Math.floor(Math.random() * arr.length)];
     | In `the top of the file` (src/components/Affirmations.jsx): `m` is assigned `arr[Math.floor(Math.random() * arr.length)];`. Later lines in this function read that name.

  18 |       setMsg(m);
     | In `the top of the file` (src/components/Affirmations.jsx): statement `setMsg(m);`. It runs when the top of the file runs, in order, before the next line of the same function.

  19 |       return m;
     | In `the top of the file` (src/components/Affirmations.jsx): return `return m;`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  20 |     },
     | In `the top of the file` (src/components/Affirmations.jsx): `},` closes random() { (opened on line 15). Names declared inside that block end here.

  21 |     messageForContext(ctx) {
     | In `the top of the file` (src/components/Affirmations.jsx): statement `messageForContext(ctx) {`. It runs when the top of the file runs, in order, before the next line of the same function.

  22 |       const m = messages[ctx] || this.random();
     | In `the top of the file` (src/components/Affirmations.jsx): `m` is assigned `messages[ctx] || this.random();`. Later lines in this function read that name.

  23 |       setMsg(m);
     | In `the top of the file` (src/components/Affirmations.jsx): statement `setMsg(m);`. It runs when the top of the file runs, in order, before the next line of the same function.

  24 |       return m;
     | In `the top of the file` (src/components/Affirmations.jsx): return `return m;`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  25 |     },
     | In `the top of the file` (src/components/Affirmations.jsx): `},` closes messageForContext(ctx) { (opened on line 21). Names declared inside that block end here.

  26 |   }));
     | In `the top of the file` (src/components/Affirmations.jsx): `}));` closes useImperativeHandle(ref, () => ({ (opened on line 14). Names declared inside that block end here.

  27 | 
     | Blank line in `src/components/Affirmations.jsx` (short encouragement lines the timer and mindfulness can request), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  28 |   return <div className="affirmation-card">{msg}</div>;
     | In `the top of the file` (src/components/Affirmations.jsx): return `return <div className="affirmation-card">{msg}</div>;`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  29 | });
     | In `the top of the file` (src/components/Affirmations.jsx): `});` closes const Affirmations = forwardRef((props, ref) =>  (opened on line 11). Names declared inside that block end here.

  30 | 
     | Blank line in `src/components/Affirmations.jsx` (short encouragement lines the timer and mindfulness can request), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  31 | export default Affirmations;
     | Default export of short encouragement lines the timer and mindfulness can request: `export default Affirmations;`. Importers that write `import X from 'src/components/Affirmations.jsx'` receive this value.

