# `src/components/focus-shield/WebsiteRow.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import React, { useEffect, useRef, useState } from "react";
     | Borrows React so this file can remember things and draw the screen.

   2 | import { categoryForDomain } from "../../utils/focusShield";
     | This file borrows a tool another file already made.

   3 | import Toggle from "./Toggle";
     | This file borrows a tool another file already made.

   4 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   5 | function RowMenu({ onEdit, onDelete, domain }) {
     | This starts RowMenu. Opens a menu that closes on outside click or Escape.

   6 |   const [open, setOpen] = useState(false);
     | This gives a short name to a value so the rest of RowMenu can use it.

   7 |   const ref = useRef(null);
     | This gives a short name to a value so the rest of RowMenu can use it.

   8 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   9 |   useEffect(() => {
     | This is an extra job that happens after the picture is drawn.

  10 |     if (!open) return;
     | This asks a yes-or-no question. The next bit runs only on yes.

  11 |     function onDocClick(e) {
     | Inside onDocClick, this line runs as written: function onDocClick(e) {. It happens in order, after the line above it and before the line below it.

  12 |       if (ref.current && !ref.current.contains(e.target)) setOpen(false);
     | This asks a yes-or-no question. The next bit runs only on yes.

  13 |     }
     | This ends onDocClick (opened on line 11).

  14 |     function onKey(e) {
     | Inside onKey, this line runs as written: function onKey(e) {. It happens in order, after the line above it and before the line below it.

  15 |       if (e.key === "Escape") setOpen(false);
     | This asks a yes-or-no question. The next bit runs only on yes.

  16 |     }
     | This ends onKey (opened on line 14).

  17 |     document.addEventListener("mousedown", onDocClick);
     | Inside RowMenu, this line runs as written: document.addEventListener("mousedown", onDocClick);. It happens in order, after the line above it and before the line below it.

  18 |     document.addEventListener("keydown", onKey);
     | Inside RowMenu, this line runs as written: document.addEventListener("keydown", onKey);. It happens in order, after the line above it and before the line below it.

  19 |     return () => {
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  20 |       document.removeEventListener("mousedown", onDocClick);
     | Inside RowMenu, this line runs as written: document.removeEventListener("mousedown", onDocClick);. It happens in order, after the line above it and before the line below it.

  21 |       document.removeEventListener("keydown", onKey);
     | Inside RowMenu, this line runs as written: document.removeEventListener("keydown", onKey);. It happens in order, after the line above it and before the line below it.

  22 |     };
     | This ends return () => { (opened on line 19).

  23 |   }, [open]);
     | This ends effect in RowMenu (opened on line 9).

  24 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  25 |   return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  26 |     <div className="fs-row-menu" ref={ref}>
     | This draws one piece of the page while RowMenu is showing.

  27 |       <button
     | This draws one piece of the page while RowMenu is showing.

  28 |         type="button"
     | Inside RowMenu, this line runs as written: type="button". It happens in order, after the line above it and before the line below it.

  29 |         className="fs-row-menu-btn"
     | Inside RowMenu, this line runs as written: className="fs-row-menu-btn". It happens in order, after the line above it and before the line below it.

  30 |         aria-haspopup="menu"
     | Inside RowMenu, this line runs as written: aria-haspopup="menu". It happens in order, after the line above it and before the line below it.

  31 |         aria-expanded={open}
     | This ends RowMenu (opened on line 5).

  32 |         aria-label={`More actions for ${domain}`}
     | This ends RowMenu (opened on line 5).

  33 |         onClick={() => setOpen((o) => !o)}
     | This decides what happens when you press.

  34 |       >
     | Inside RowMenu, this line runs as written: >. It happens in order, after the line above it and before the line below it.

  35 |         ⋮
     | Inside RowMenu, this line runs as written: ⋮. It happens in order, after the line above it and before the line below it.

  36 |       </button>
     | This ends a drawing that RowMenu started just above.

  37 |       {open && (
     | Inside RowMenu, this line runs as written: {open && (. It happens in order, after the line above it and before the line below it.

  38 |         <div className="fs-row-menu-list" role="menu">
     | This draws one piece of the page while RowMenu is showing.

  39 |           <button type="button" role="menuitem" onClick={() => { setOpen(false); onEdit(); }}>
     | This draws one piece of the page while RowMenu is showing.

  40 |             Edit
     | Inside RowMenu, this line runs as written: Edit. It happens in order, after the line above it and before the line below it.

  41 |           </button>
     | This ends a drawing that RowMenu started just above.

  42 |           <button type="button" role="menuitem" className="fs-row-menu-danger" onClick={() => { setOpen(false); onDelete(); }}>
     | This draws one piece of the page while RowMenu is showing.

  43 |             Delete
     | Inside RowMenu, this line runs as written: Delete. It happens in order, after the line above it and before the line below it.

  44 |           </button>
     | This ends a drawing that RowMenu started just above.

  45 |         </div>
     | This ends a drawing that RowMenu started just above.

  46 |       )}
     | This ends RowMenu (opened on line 5).

  47 |     </div>
     | This ends a drawing that RowMenu started just above.

  48 |   );
     | This closes a box of instructions that opened above.

  49 | }
     | This ends RowMenu (opened on line 5).

  50 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  51 | export default function WebsiteRow({ entry, selected, onToggleSelect, onToggleEnabled, onEdit, onDelete }) {
     | This starts WebsiteRow. Checkbox, name, domain, category badge, enable switch, and the ⋮ menu.

  52 |   const category = categoryForDomain(entry.value);
     | This gives a short name to a value so the rest of WebsiteRow can use it.

  53 |   const enabled = entry.enabled !== false;
     | This gives a short name to a value so the rest of WebsiteRow can use it.

  54 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  55 |   return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  56 |     <div className={`fs-row${selected ? " fs-row--selected" : ""}`}>
     | This draws one piece of the page while WebsiteRow is showing.

  57 |       <input
     | This draws one piece of the page while WebsiteRow is showing.

  58 |         type="checkbox"
     | Inside WebsiteRow, this line runs as written: type="checkbox". It happens in order, after the line above it and before the line below it.

  59 |         className="fs-row-checkbox"
     | Inside WebsiteRow, this line runs as written: className="fs-row-checkbox". It happens in order, after the line above it and before the line below it.

  60 |         checked={selected}
     | This ends WebsiteRow (opened on line 51).

  61 |         onChange={onToggleSelect}
     | This ends WebsiteRow (opened on line 51).

  62 |         aria-label={`Select ${entry.value}`}
     | This ends WebsiteRow (opened on line 51).

  63 |       />
     | This closes a box of instructions that opened above.

  64 |       <div className="fs-row-main">
     | This draws one piece of the page while WebsiteRow is showing.

  65 |         <div className="fs-row-domain">
     | This draws one piece of the page while WebsiteRow is showing.

  66 |           {entry.label ? <span>{entry.label}</span> : null}
     | This ends WebsiteRow (opened on line 51).

  67 |           <span className={entry.label ? "fs-row-domain-sub" : ""}>{entry.value}</span>
     | This draws one piece of the page while WebsiteRow is showing.

  68 |         </div>
     | This ends a drawing that WebsiteRow started just above.

  69 |         <div className="fs-row-meta">
     | This draws one piece of the page while WebsiteRow is showing.

  70 |           <span className="badge badge-violet">{category}</span>
     | This draws one piece of the page while WebsiteRow is showing.

  71 |           {!enabled && <span className="badge" style={{ background: "var(--border)", color: "var(--muted)" }}>Disabled</span>}
     | This ends WebsiteRow (opened on line 51).

  72 |           {entry.notes && <span className="text-xs text-muted fs-row-notes">{entry.notes}</span>}
     | This ends WebsiteRow (opened on line 51).

  73 |         </div>
     | This ends a drawing that WebsiteRow started just above.

  74 |       </div>
     | This ends a drawing that WebsiteRow started just above.

  75 |       <div className="fs-row-actions">
     | This draws one piece of the page while WebsiteRow is showing.

  76 |         <Toggle checked={enabled} onChange={onToggleEnabled} label={`${enabled ? "Disable" : "Enable"} ${entry.value}`} />
     | This draws one piece of the page while WebsiteRow is showing.

  77 |         <RowMenu domain={entry.value} onEdit={onEdit} onDelete={onDelete} />
     | This draws one piece of the page while WebsiteRow is showing.

  78 |       </div>
     | This ends a drawing that WebsiteRow started just above.

  79 |     </div>
     | This ends a drawing that WebsiteRow started just above.

  80 |   );
     | This closes a box of instructions that opened above.

  81 | }
     | This ends WebsiteRow (opened on line 51).

