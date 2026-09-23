# `src/components/focus-shield/Sheet.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import React, { useEffect } from "react";
     | Import for the shared popup/bottom-sheet frame: `import React, { useEffect } from "react";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   2 | 
     | Blank line in `src/components/focus-shield/Sheet.jsx` (the shared popup/bottom-sheet frame), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   3 | // Bottom sheet on mobile, centered modal on desktop — same markup, responsive CSS (see
     | Comment inside the top of the file. Not executed. It documents the next code: Bottom sheet on mobile, centered modal on desktop — same markup, responsive CSS (see

   4 | // .fs-sheet-overlay / .fs-sheet in styles.css) does the rest. Shared by every Focus Shield
     | Comment inside the top of the file. Not executed. It documents the next code: .fs-sheet-overlay / .fs-sheet in styles.css) does the rest. Shared by every Focus Shield

   5 | // modal so we don't reimplement open/close/escape/backdrop handling per flow.
     | Comment inside the top of the file. Not executed. It documents the next code: modal so we don't reimplement open/close/escape/backdrop handling per flow.

   6 | export default function Sheet({ open, onClose, title, children, labelledBy }) {
     | Defines `Sheet` in the shared popup/bottom-sheet frame. Shared dialog. Escape or backdrop calls onClose. Renders null when open is false. CSS decides bottom sheet vs centered modal.

   7 |   useEffect(() => {
     | In `Sheet` (src/components/focus-shield/Sheet.jsx): opens or continues an effect — `useEffect(() => {`. The effect body runs after paint, and its cleanup runs before the next effect and on unmount.

   8 |     if (!open) return;
     | In `Sheet` (src/components/focus-shield/Sheet.jsx): branch `if (!open) return;`. Only one side runs.

   9 |     function onKey(e) {
     | In `onKey` (src/components/focus-shield/Sheet.jsx): event prop `function onKey(e) {`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

  10 |       if (e.key === "Escape") onClose();
     | In `onKey` (src/components/focus-shield/Sheet.jsx): branch `if (e.key === "Escape") onClose();`. Only one side runs.

  11 |     }
     | In `onKey` (src/components/focus-shield/Sheet.jsx): `}` closes onKey (opened on line 9). Names declared inside that block end here.

  12 |     document.addEventListener("keydown", onKey);
     | In `Sheet` (src/components/focus-shield/Sheet.jsx): event prop `document.addEventListener("keydown", onKey);`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

  13 |     return () => document.removeEventListener("keydown", onKey);
     | In `Sheet` (src/components/focus-shield/Sheet.jsx): return `return () => document.removeEventListener("keydown", onKey);`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  14 |   }, [open, onClose]);
     | In `Sheet` (src/components/focus-shield/Sheet.jsx): `}, [open, onClose]);` closes effect in Sheet (opened on line 7). Names declared inside that block end here.

  15 | 
     | Blank line in `src/components/focus-shield/Sheet.jsx` (the shared popup/bottom-sheet frame), inside Sheet. The parser skips it. It separates the previous statement from the next so the function is readable.

  16 |   if (!open) return null;
     | In `Sheet` (src/components/focus-shield/Sheet.jsx): branch `if (!open) return null;`. Only one side runs.

  17 | 
     | Blank line in `src/components/focus-shield/Sheet.jsx` (the shared popup/bottom-sheet frame), inside Sheet. The parser skips it. It separates the previous statement from the next so the function is readable.

  18 |   return (
     | In `Sheet` (src/components/focus-shield/Sheet.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  19 |     <>
     | In `Sheet` (src/components/focus-shield/Sheet.jsx): JSX `<element>`. React will create this node when the parent renders. Source: `<>`

  20 |       <div className="fs-sheet-overlay" onClick={onClose} aria-hidden="true" />
     | In `Sheet` (src/components/focus-shield/Sheet.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="fs-sheet-overlay" onClick={onClose} aria-hidden="true" />`

  21 |       <div className="fs-sheet" role="dialog" aria-modal="true" aria-labelledby={labelledBy}>
     | In `Sheet` (src/components/focus-shield/Sheet.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="fs-sheet" role="dialog" aria-modal="true" aria-labelledby={labelledBy}>`

  22 |         <div className="bottom-sheet-handle" aria-hidden="true" />
     | In `Sheet` (src/components/focus-shield/Sheet.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="bottom-sheet-handle" aria-hidden="true" />`

  23 |         <div className="fs-sheet-header">
     | In `Sheet` (src/components/focus-shield/Sheet.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="fs-sheet-header">`

  24 |           <h2 id={labelledBy} className="fs-sheet-title">{title}</h2>
     | In `Sheet` (src/components/focus-shield/Sheet.jsx): JSX `<h2>`. React will create this node when the parent renders.. className chooses the CSS rules from styles.css Source: `<h2 id={labelledBy} className="fs-sheet-title">{title}</h2>`

  25 |           <button type="button" className="fs-sheet-close" onClick={onClose} aria-label="Close">
     | In `Sheet` (src/components/focus-shield/Sheet.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button type="button" className="fs-sheet-close" onClick={onClose} aria-label="Close">`

  26 |             ×
     | In `Sheet` (src/components/focus-shield/Sheet.jsx): statement `×`. It runs when Sheet runs, in order, before the next line of the same function.

  27 |           </button>
     | In `Sheet` (src/components/focus-shield/Sheet.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

  28 |         </div>
     | In `Sheet` (src/components/focus-shield/Sheet.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  29 |         <div className="fs-sheet-body">{children}</div>
     | In `Sheet` (src/components/focus-shield/Sheet.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="fs-sheet-body">{children}</div>`

  30 |       </div>
     | In `Sheet` (src/components/focus-shield/Sheet.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  31 |     </>
     | In `Sheet` (src/components/focus-shield/Sheet.jsx): JSX `<element>`. This closes that element. Source: `</>`

  32 |   );
     | In `Sheet` (src/components/focus-shield/Sheet.jsx): statement `);`. It runs when Sheet runs, in order, before the next line of the same function.

  33 | }
     | In `Sheet` (src/components/focus-shield/Sheet.jsx): `}` closes Sheet (opened on line 6). Names declared inside that block end here.

