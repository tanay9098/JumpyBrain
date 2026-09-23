# `src/components/focus-shield/Toggle.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import React from "react";
     | Import for the shared on/off switch: `import React from "react";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   2 | 
     | Blank line in `src/components/focus-shield/Toggle.jsx` (the shared on/off switch), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   3 | // Shared on/off switch — used by the Focus Shield master toggle and per-row enable switches.
     | Comment inside the top of the file. Not executed. It documents the next code: Shared on/off switch — used by the Focus Shield master toggle and per-row enable switches.

   4 | export default function Toggle({ checked, onChange, disabled, label }) {
     | Defines `Toggle` in the shared on/off switch. A button with role=switch. Click calls onChange with the opposite boolean. It does not store the boolean itself.

   5 |   return (
     | In `Toggle` (src/components/focus-shield/Toggle.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

   6 |     <button
     | In `Toggle` (src/components/focus-shield/Toggle.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button`

   7 |       type="button"
     | In `Toggle` (src/components/focus-shield/Toggle.jsx): statement `type="button"`. It runs when Toggle runs, in order, before the next line of the same function.

   8 |       role="switch"
     | In `Toggle` (src/components/focus-shield/Toggle.jsx): statement `role="switch"`. It runs when Toggle runs, in order, before the next line of the same function.

   9 |       aria-checked={checked}
     | In `Toggle` (src/components/focus-shield/Toggle.jsx): `aria-checked={checked}` closes Toggle (opened on line 4). Names declared inside that block end here.

  10 |       aria-label={label}
     | In `Toggle` (src/components/focus-shield/Toggle.jsx): `aria-label={label}` closes Toggle (opened on line 4). Names declared inside that block end here.

  11 |       disabled={disabled}
     | In `Toggle` (src/components/focus-shield/Toggle.jsx): `disabled={disabled}` closes Toggle (opened on line 4). Names declared inside that block end here.

  12 |       onClick={() => onChange(!checked)}
     | In `Toggle` (src/components/focus-shield/Toggle.jsx): event prop `onClick={() => onChange(!checked)}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

  13 |       className="fs-toggle"
     | In `Toggle` (src/components/focus-shield/Toggle.jsx): statement `className="fs-toggle"`. It runs when Toggle runs, in order, before the next line of the same function.

  14 |       data-checked={checked || undefined}
     | In `Toggle` (src/components/focus-shield/Toggle.jsx): `data-checked={checked || undefined}` closes Toggle (opened on line 4). Names declared inside that block end here.

  15 |     >
     | In `Toggle` (src/components/focus-shield/Toggle.jsx): statement `>`. It runs when Toggle runs, in order, before the next line of the same function.

  16 |       <span className="fs-toggle-knob" />
     | In `Toggle` (src/components/focus-shield/Toggle.jsx): Opens it. An inline box. Source: `<span className="fs-toggle-knob" />`

  17 |     </button>
     | In `Toggle` (src/components/focus-shield/Toggle.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

  18 |   );
     | In `Toggle` (src/components/focus-shield/Toggle.jsx): statement `);`. It runs when Toggle runs, in order, before the next line of the same function.

  19 | }
     | In `Toggle` (src/components/focus-shield/Toggle.jsx): `}` closes Toggle (opened on line 4). Names declared inside that block end here.

