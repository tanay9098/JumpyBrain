# `src/components/focus-shield/Sheet.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import React, { useEffect } from "react";
     | Borrows React so this file can remember things and draw the screen.

   2 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   3 | // Bottom sheet on mobile, centered modal on desktop — same markup, responsive CSS (see
     | A note written for people. The app does not run it.

   4 | // .fs-sheet-overlay / .fs-sheet in styles.css) does the rest. Shared by every Focus Shield
     | A note written for people. The app does not run it.

   5 | // modal so we don't reimplement open/close/escape/backdrop handling per flow.
     | A note written for people. The app does not run it.

   6 | export default function Sheet({ open, onClose, title, children, labelledBy }) {
     | This starts Sheet. Shared dialog. Escape or backdrop calls onClose. Renders null when open is false. CSS decides bottom sheet vs centered modal.

   7 |   useEffect(() => {
     | This is an extra job that happens after the picture is drawn.

   8 |     if (!open) return;
     | This asks a yes-or-no question. The next bit runs only on yes.

   9 |     function onKey(e) {
     | Inside onKey, this line runs as written: function onKey(e) {. It happens in order, after the line above it and before the line below it.

  10 |       if (e.key === "Escape") onClose();
     | This asks a yes-or-no question. The next bit runs only on yes.

  11 |     }
     | This ends onKey (opened on line 9).

  12 |     document.addEventListener("keydown", onKey);
     | Inside Sheet, this line runs as written: document.addEventListener("keydown", onKey);. It happens in order, after the line above it and before the line below it.

  13 |     return () => document.removeEventListener("keydown", onKey);
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  14 |   }, [open, onClose]);
     | This ends effect in Sheet (opened on line 7).

  15 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  16 |   if (!open) return null;
     | This asks a yes-or-no question. The next bit runs only on yes.

  17 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  18 |   return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  19 |     <>
     | This draws one piece of the page while Sheet is showing.

  20 |       <div className="fs-sheet-overlay" onClick={onClose} aria-hidden="true" />
     | This draws one piece of the page while Sheet is showing.

  21 |       <div className="fs-sheet" role="dialog" aria-modal="true" aria-labelledby={labelledBy}>
     | This draws one piece of the page while Sheet is showing.

  22 |         <div className="bottom-sheet-handle" aria-hidden="true" />
     | This draws one piece of the page while Sheet is showing.

  23 |         <div className="fs-sheet-header">
     | This draws one piece of the page while Sheet is showing.

  24 |           <h2 id={labelledBy} className="fs-sheet-title">{title}</h2>
     | This draws one piece of the page while Sheet is showing.

  25 |           <button type="button" className="fs-sheet-close" onClick={onClose} aria-label="Close">
     | This draws one piece of the page while Sheet is showing.

  26 |             ×
     | Inside Sheet, this line runs as written: ×. It happens in order, after the line above it and before the line below it.

  27 |           </button>
     | This ends a drawing that Sheet started just above.

  28 |         </div>
     | This ends a drawing that Sheet started just above.

  29 |         <div className="fs-sheet-body">{children}</div>
     | This draws one piece of the page while Sheet is showing.

  30 |       </div>
     | This ends a drawing that Sheet started just above.

  31 |     </>
     | This ends a drawing that Sheet started just above.

  32 |   );
     | This closes a box of instructions that opened above.

  33 | }
     | This ends Sheet (opened on line 6).

