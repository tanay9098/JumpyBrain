# `src/components/focus-shield/Toggle.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import React from "react";
     | Borrows React so this file can remember things and draw the screen.

   2 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   3 | // Shared on/off switch — used by the Focus Shield master toggle and per-row enable switches.
     | A note written for people. The app does not run it.

   4 | export default function Toggle({ checked, onChange, disabled, label }) {
     | This starts Toggle. A button with role=switch. Click calls onChange with the opposite boolean. It does not store the boolean itself.

   5 |   return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

   6 |     <button
     | This draws one piece of the page while Toggle is showing.

   7 |       type="button"
     | Inside Toggle, this line runs as written: type="button". It happens in order, after the line above it and before the line below it.

   8 |       role="switch"
     | Inside Toggle, this line runs as written: role="switch". It happens in order, after the line above it and before the line below it.

   9 |       aria-checked={checked}
     | This ends Toggle (opened on line 4).

  10 |       aria-label={label}
     | This ends Toggle (opened on line 4).

  11 |       disabled={disabled}
     | This ends Toggle (opened on line 4).

  12 |       onClick={() => onChange(!checked)}
     | This decides what happens when you press.

  13 |       className="fs-toggle"
     | Inside Toggle, this line runs as written: className="fs-toggle". It happens in order, after the line above it and before the line below it.

  14 |       data-checked={checked || undefined}
     | This ends Toggle (opened on line 4).

  15 |     >
     | Inside Toggle, this line runs as written: >. It happens in order, after the line above it and before the line below it.

  16 |       <span className="fs-toggle-knob" />
     | This draws one piece of the page while Toggle is showing.

  17 |     </button>
     | This ends a drawing that Toggle started just above.

  18 |   );
     | This closes a box of instructions that opened above.

  19 | }
     | This ends Toggle (opened on line 4).

