# `src/components/focus-shield/WebsiteRow.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import React, { useEffect, useRef, useState } from "react";
     | Import for one website row: `import React, { useEffect, useRef, useState } from "react";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   2 | import { categoryForDomain } from "../../utils/focusShield";
     | Import for one website row: `import { categoryForDomain } from "../../utils/focusShield";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   3 | import Toggle from "./Toggle";
     | Import for one website row: `import Toggle from "./Toggle";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   4 | 
     | Blank line in `src/components/focus-shield/WebsiteRow.jsx` (one website row), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   5 | function RowMenu({ onEdit, onDelete, domain }) {
     | Defines `RowMenu` in one website row. Opens a menu that closes on outside click or Escape.

   6 |   const [open, setOpen] = useState(false);
     | In `RowMenu` (src/components/focus-shield/WebsiteRow.jsx): React state `open, setOpen`. The value survives re-renders. Calling the setter re-renders this component. `const [open, setOpen] = useState(false);`

   7 |   const ref = useRef(null);
     | In `RowMenu` (src/components/focus-shield/WebsiteRow.jsx): A ref `ref`. `.current` survives re-renders and writing it does not re-render. `const ref = useRef(null);`

   8 | 
     | Blank line in `src/components/focus-shield/WebsiteRow.jsx` (one website row), inside RowMenu. The parser skips it. It separates the previous statement from the next so the function is readable.

   9 |   useEffect(() => {
     | In `RowMenu` (src/components/focus-shield/WebsiteRow.jsx): opens or continues an effect — `useEffect(() => {`. The effect body runs after paint, and its cleanup runs before the next effect and on unmount.

  10 |     if (!open) return;
     | In `RowMenu` (src/components/focus-shield/WebsiteRow.jsx): branch `if (!open) return;`. Only one side runs.

  11 |     function onDocClick(e) {
     | In `onDocClick` (src/components/focus-shield/WebsiteRow.jsx): statement `function onDocClick(e) {`. It runs when onDocClick runs, in order, before the next line of the same function.

  12 |       if (ref.current && !ref.current.contains(e.target)) setOpen(false);
     | In `onDocClick` (src/components/focus-shield/WebsiteRow.jsx): branch `if (ref.current && !ref.current.contains(e.target)) setOpen(false);`. Only one side runs.

  13 |     }
     | In `onDocClick` (src/components/focus-shield/WebsiteRow.jsx): `}` closes onDocClick (opened on line 11). Names declared inside that block end here.

  14 |     function onKey(e) {
     | In `onKey` (src/components/focus-shield/WebsiteRow.jsx): event prop `function onKey(e) {`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

  15 |       if (e.key === "Escape") setOpen(false);
     | In `onKey` (src/components/focus-shield/WebsiteRow.jsx): branch `if (e.key === "Escape") setOpen(false);`. Only one side runs.

  16 |     }
     | In `onKey` (src/components/focus-shield/WebsiteRow.jsx): `}` closes onKey (opened on line 14). Names declared inside that block end here.

  17 |     document.addEventListener("mousedown", onDocClick);
     | In `RowMenu` (src/components/focus-shield/WebsiteRow.jsx): statement `document.addEventListener("mousedown", onDocClick);`. It runs when RowMenu runs, in order, before the next line of the same function.

  18 |     document.addEventListener("keydown", onKey);
     | In `RowMenu` (src/components/focus-shield/WebsiteRow.jsx): event prop `document.addEventListener("keydown", onKey);`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

  19 |     return () => {
     | In `RowMenu` (src/components/focus-shield/WebsiteRow.jsx): return `return () => {`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  20 |       document.removeEventListener("mousedown", onDocClick);
     | In `RowMenu` (src/components/focus-shield/WebsiteRow.jsx): statement `document.removeEventListener("mousedown", onDocClick);`. It runs when RowMenu runs, in order, before the next line of the same function.

  21 |       document.removeEventListener("keydown", onKey);
     | In `RowMenu` (src/components/focus-shield/WebsiteRow.jsx): event prop `document.removeEventListener("keydown", onKey);`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

  22 |     };
     | In `RowMenu` (src/components/focus-shield/WebsiteRow.jsx): `};` closes return () => { (opened on line 19). Names declared inside that block end here.

  23 |   }, [open]);
     | In `RowMenu` (src/components/focus-shield/WebsiteRow.jsx): `}, [open]);` closes effect in RowMenu (opened on line 9). Names declared inside that block end here.

  24 | 
     | Blank line in `src/components/focus-shield/WebsiteRow.jsx` (one website row), inside RowMenu. The parser skips it. It separates the previous statement from the next so the function is readable.

  25 |   return (
     | In `RowMenu` (src/components/focus-shield/WebsiteRow.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  26 |     <div className="fs-row-menu" ref={ref}>
     | In `RowMenu` (src/components/focus-shield/WebsiteRow.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="fs-row-menu" ref={ref}>`

  27 |       <button
     | In `RowMenu` (src/components/focus-shield/WebsiteRow.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button`

  28 |         type="button"
     | In `RowMenu` (src/components/focus-shield/WebsiteRow.jsx): statement `type="button"`. It runs when RowMenu runs, in order, before the next line of the same function.

  29 |         className="fs-row-menu-btn"
     | In `RowMenu` (src/components/focus-shield/WebsiteRow.jsx): statement `className="fs-row-menu-btn"`. It runs when RowMenu runs, in order, before the next line of the same function.

  30 |         aria-haspopup="menu"
     | In `RowMenu` (src/components/focus-shield/WebsiteRow.jsx): statement `aria-haspopup="menu"`. It runs when RowMenu runs, in order, before the next line of the same function.

  31 |         aria-expanded={open}
     | In `RowMenu` (src/components/focus-shield/WebsiteRow.jsx): `aria-expanded={open}` closes RowMenu (opened on line 5). Names declared inside that block end here.

  32 |         aria-label={`More actions for ${domain}`}
     | In `RowMenu` (src/components/focus-shield/WebsiteRow.jsx): `aria-label={`More actions for ${domain}`}` closes RowMenu (opened on line 5). Names declared inside that block end here.

  33 |         onClick={() => setOpen((o) => !o)}
     | In `RowMenu` (src/components/focus-shield/WebsiteRow.jsx): event prop `onClick={() => setOpen((o) => !o)}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

  34 |       >
     | In `RowMenu` (src/components/focus-shield/WebsiteRow.jsx): statement `>`. It runs when RowMenu runs, in order, before the next line of the same function.

  35 |         ⋮
     | In `RowMenu` (src/components/focus-shield/WebsiteRow.jsx): statement `⋮`. It runs when RowMenu runs, in order, before the next line of the same function.

  36 |       </button>
     | In `RowMenu` (src/components/focus-shield/WebsiteRow.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

  37 |       {open && (
     | In `RowMenu` (src/components/focus-shield/WebsiteRow.jsx): statement `{open && (`. It runs when RowMenu runs, in order, before the next line of the same function.

  38 |         <div className="fs-row-menu-list" role="menu">
     | In `RowMenu` (src/components/focus-shield/WebsiteRow.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="fs-row-menu-list" role="menu">`

  39 |           <button type="button" role="menuitem" onClick={() => { setOpen(false); onEdit(); }}>
     | In `RowMenu` (src/components/focus-shield/WebsiteRow.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button type="button" role="menuitem" onClick={() => { setOpen(false); onEdit(); }}>`

  40 |             Edit
     | In `RowMenu` (src/components/focus-shield/WebsiteRow.jsx): statement `Edit`. It runs when RowMenu runs, in order, before the next line of the same function.

  41 |           </button>
     | In `RowMenu` (src/components/focus-shield/WebsiteRow.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

  42 |           <button type="button" role="menuitem" className="fs-row-menu-danger" onClick={() => { setOpen(false); onDelete(); }}>
     | In `RowMenu` (src/components/focus-shield/WebsiteRow.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button type="button" role="menuitem" className="fs-row-menu-danger" onClick={() => { setOpen(false); onDelete(); }}>`

  43 |             Delete
     | In `RowMenu` (src/components/focus-shield/WebsiteRow.jsx): statement `Delete`. It runs when RowMenu runs, in order, before the next line of the same function.

  44 |           </button>
     | In `RowMenu` (src/components/focus-shield/WebsiteRow.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

  45 |         </div>
     | In `RowMenu` (src/components/focus-shield/WebsiteRow.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  46 |       )}
     | In `RowMenu` (src/components/focus-shield/WebsiteRow.jsx): `)}` closes RowMenu (opened on line 5). Names declared inside that block end here.

  47 |     </div>
     | In `RowMenu` (src/components/focus-shield/WebsiteRow.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  48 |   );
     | In `RowMenu` (src/components/focus-shield/WebsiteRow.jsx): statement `);`. It runs when RowMenu runs, in order, before the next line of the same function.

  49 | }
     | In `RowMenu` (src/components/focus-shield/WebsiteRow.jsx): `}` closes RowMenu (opened on line 5). Names declared inside that block end here.

  50 | 
     | Blank line in `src/components/focus-shield/WebsiteRow.jsx` (one website row), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  51 | export default function WebsiteRow({ entry, selected, onToggleSelect, onToggleEnabled, onEdit, onDelete }) {
     | Defines `WebsiteRow` in one website row. Checkbox, name, domain, category badge, enable switch, and the ⋮ menu.

  52 |   const category = categoryForDomain(entry.value);
     | In `WebsiteRow` (src/components/focus-shield/WebsiteRow.jsx): `category` is assigned `categoryForDomain(entry.value);`. Later lines in this function read that name.

  53 |   const enabled = entry.enabled !== false;
     | In `WebsiteRow` (src/components/focus-shield/WebsiteRow.jsx): `enabled` is assigned `entry.enabled !== false;`. Later lines in this function read that name.

  54 | 
     | Blank line in `src/components/focus-shield/WebsiteRow.jsx` (one website row), inside WebsiteRow. The parser skips it. It separates the previous statement from the next so the function is readable.

  55 |   return (
     | In `WebsiteRow` (src/components/focus-shield/WebsiteRow.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  56 |     <div className={`fs-row${selected ? " fs-row--selected" : ""}`}>
     | In `WebsiteRow` (src/components/focus-shield/WebsiteRow.jsx): Opens it. A box that groups the elements inside it. Source: `<div className={`fs-row${selected ? " fs-row--selected" : ""}`}>`

  57 |       <input
     | In `WebsiteRow` (src/components/focus-shield/WebsiteRow.jsx): Opens it. A text or date field. If value and onChange are set, React owns what it shows. Source: `<input`

  58 |         type="checkbox"
     | In `WebsiteRow` (src/components/focus-shield/WebsiteRow.jsx): statement `type="checkbox"`. It runs when WebsiteRow runs, in order, before the next line of the same function.

  59 |         className="fs-row-checkbox"
     | In `WebsiteRow` (src/components/focus-shield/WebsiteRow.jsx): statement `className="fs-row-checkbox"`. It runs when WebsiteRow runs, in order, before the next line of the same function.

  60 |         checked={selected}
     | In `WebsiteRow` (src/components/focus-shield/WebsiteRow.jsx): `checked={selected}` closes WebsiteRow (opened on line 51). Names declared inside that block end here.

  61 |         onChange={onToggleSelect}
     | In `WebsiteRow` (src/components/focus-shield/WebsiteRow.jsx): event prop `onChange={onToggleSelect}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

  62 |         aria-label={`Select ${entry.value}`}
     | In `WebsiteRow` (src/components/focus-shield/WebsiteRow.jsx): `aria-label={`Select ${entry.value}`}` closes WebsiteRow (opened on line 51). Names declared inside that block end here.

  63 |       />
     | In `WebsiteRow` (src/components/focus-shield/WebsiteRow.jsx): statement `/>`. It runs when WebsiteRow runs, in order, before the next line of the same function.

  64 |       <div className="fs-row-main">
     | In `WebsiteRow` (src/components/focus-shield/WebsiteRow.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="fs-row-main">`

  65 |         <div className="fs-row-domain">
     | In `WebsiteRow` (src/components/focus-shield/WebsiteRow.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="fs-row-domain">`

  66 |           {entry.label ? <span>{entry.label}</span> : null}
     | In `WebsiteRow` (src/components/focus-shield/WebsiteRow.jsx): `{entry.label ? <span>{entry.label}</span> : null}` closes WebsiteRow (opened on line 51). Names declared inside that block end here.

  67 |           <span className={entry.label ? "fs-row-domain-sub" : ""}>{entry.value}</span>
     | In `WebsiteRow` (src/components/focus-shield/WebsiteRow.jsx): Opens it. An inline box. Source: `<span className={entry.label ? "fs-row-domain-sub" : ""}>{entry.value}</span>`

  68 |         </div>
     | In `WebsiteRow` (src/components/focus-shield/WebsiteRow.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  69 |         <div className="fs-row-meta">
     | In `WebsiteRow` (src/components/focus-shield/WebsiteRow.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="fs-row-meta">`

  70 |           <span className="badge badge-violet">{category}</span>
     | In `WebsiteRow` (src/components/focus-shield/WebsiteRow.jsx): Opens it. An inline box. Source: `<span className="badge badge-violet">{category}</span>`

  71 |           {!enabled && <span className="badge" style={{ background: "var(--border)", color: "var(--muted)" }}>Disabled</span>}
     | In `WebsiteRow` (src/components/focus-shield/WebsiteRow.jsx): `{!enabled && <span className="badge" style={{ background: "var(--border)", color: "var(--muted)" }}>Disabled</span>}` closes WebsiteRow (opened on line 51). Names declared inside that block end here.

  72 |           {entry.notes && <span className="text-xs text-muted fs-row-notes">{entry.notes}</span>}
     | In `WebsiteRow` (src/components/focus-shield/WebsiteRow.jsx): `{entry.notes && <span className="text-xs text-muted fs-row-notes">{entry.notes}</span>}` closes WebsiteRow (opened on line 51). Names declared inside that block end here.

  73 |         </div>
     | In `WebsiteRow` (src/components/focus-shield/WebsiteRow.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  74 |       </div>
     | In `WebsiteRow` (src/components/focus-shield/WebsiteRow.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  75 |       <div className="fs-row-actions">
     | In `WebsiteRow` (src/components/focus-shield/WebsiteRow.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="fs-row-actions">`

  76 |         <Toggle checked={enabled} onChange={onToggleEnabled} label={`${enabled ? "Disable" : "Enable"} ${entry.value}`} />
     | In `WebsiteRow` (src/components/focus-shield/WebsiteRow.jsx): Opens it. On/off switch. The parent owns the boolean. Source: `<Toggle checked={enabled} onChange={onToggleEnabled} label={`${enabled ? "Disable" : "Enable"} ${entry.value}`} />`

  77 |         <RowMenu domain={entry.value} onEdit={onEdit} onDelete={onDelete} />
     | In `WebsiteRow` (src/components/focus-shield/WebsiteRow.jsx): JSX `<RowMenu>`. React will create this node when the parent renders. Source: `<RowMenu domain={entry.value} onEdit={onEdit} onDelete={onDelete} />`

  78 |       </div>
     | In `WebsiteRow` (src/components/focus-shield/WebsiteRow.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  79 |     </div>
     | In `WebsiteRow` (src/components/focus-shield/WebsiteRow.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  80 |   );
     | In `WebsiteRow` (src/components/focus-shield/WebsiteRow.jsx): statement `);`. It runs when WebsiteRow runs, in order, before the next line of the same function.

  81 | }
     | In `WebsiteRow` (src/components/focus-shield/WebsiteRow.jsx): `}` closes WebsiteRow (opened on line 51). Names declared inside that block end here.

