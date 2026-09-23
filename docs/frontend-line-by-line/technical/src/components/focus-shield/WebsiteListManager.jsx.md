# `src/components/focus-shield/WebsiteListManager.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import React, { useMemo, useState } from "react";
     | Import for search, add, edit, and bulk-edit one domain list: `import React, { useMemo, useState } from "react";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   2 | import WebsiteRow from "./WebsiteRow";
     | Import for search, add, edit, and bulk-edit one domain list: `import WebsiteRow from "./WebsiteRow";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   3 | import AddWebsiteSheet from "./AddWebsiteSheet";
     | Import for search, add, edit, and bulk-edit one domain list: `import AddWebsiteSheet from "./AddWebsiteSheet";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   4 | import EditRuleSheet from "./EditRuleSheet";
     | Import for search, add, edit, and bulk-edit one domain list: `import EditRuleSheet from "./EditRuleSheet";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   5 | import { categoryForDomain } from "../../utils/focusShield";
     | Import for search, add, edit, and bulk-edit one domain list: `import { categoryForDomain } from "../../utils/focusShield";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   6 | 
     | Blank line in `src/components/focus-shield/WebsiteListManager.jsx` (search, add, edit, and bulk-edit one domain list), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   7 | // Generic add/edit/delete/search/bulk-action manager for one list of domains — reused for
     | Comment inside the top of the file. Not executed. It documents the next code: Generic add/edit/delete/search/bulk-action manager for one list of domains — reused for

   8 | // both "Blocked Websites" and "Whitelisted Websites" so the two sections never drift apart.
     | Comment inside the top of the file. Not executed. It documents the next code: both "Blocked Websites" and "Whitelisted Websites" so the two sections never drift apart.

   9 | export default function WebsiteListManager({
     | Defines `WebsiteListManager` in search, add, edit, and bulk-edit one domain list. One list, used twice: blocked sites and whitelist. Search, selection, bulk enable/disable/delete, add sheet, edit sheet.

  10 |   title,
     | In `WebsiteListManager` (src/components/focus-shield/WebsiteListManager.jsx): statement `title,`. It runs when WebsiteListManager runs, in order, before the next line of the same function.

  11 |   description,
     | In `WebsiteListManager` (src/components/focus-shield/WebsiteListManager.jsx): statement `description,`. It runs when WebsiteListManager runs, in order, before the next line of the same function.

  12 |   items,
     | In `WebsiteListManager` (src/components/focus-shield/WebsiteListManager.jsx): statement `items,`. It runs when WebsiteListManager runs, in order, before the next line of the same function.

  13 |   onChange,
     | In `WebsiteListManager` (src/components/focus-shield/WebsiteListManager.jsx): event prop `onChange,`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

  14 |   target,
     | In `WebsiteListManager` (src/components/focus-shield/WebsiteListManager.jsx): statement `target,`. It runs when WebsiteListManager runs, in order, before the next line of the same function.

  15 |   emptyIcon,
     | In `WebsiteListManager` (src/components/focus-shield/WebsiteListManager.jsx): statement `emptyIcon,`. It runs when WebsiteListManager runs, in order, before the next line of the same function.

  16 |   emptyTitle,
     | In `WebsiteListManager` (src/components/focus-shield/WebsiteListManager.jsx): statement `emptyTitle,`. It runs when WebsiteListManager runs, in order, before the next line of the same function.

  17 |   emptyBody,
     | In `WebsiteListManager` (src/components/focus-shield/WebsiteListManager.jsx): statement `emptyBody,`. It runs when WebsiteListManager runs, in order, before the next line of the same function.

  18 | }) {
     | In `WebsiteListManager` (src/components/focus-shield/WebsiteListManager.jsx): `}) {` closes WebsiteListManager (opened on line 9). Names declared inside that block end here.

  19 |   const [search, setSearch] = useState("");
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): React state `search, setSearch`. The value survives re-renders. Calling the setter re-renders this component. `const [search, setSearch] = useState("");`

  20 |   const [selected, setSelected] = useState(() => new Set());
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): React state `selected, setSelected`. The value survives re-renders. Calling the setter re-renders this component. `const [selected, setSelected] = useState(() => new Set());`

  21 |   const [addOpen, setAddOpen] = useState(false);
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): React state `addOpen, setAddOpen`. The value survives re-renders. Calling the setter re-renders this component. `const [addOpen, setAddOpen] = useState(false);`

  22 |   const [editing, setEditing] = useState(null);
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): React state `editing, setEditing`. The value survives re-renders. Calling the setter re-renders this component. `const [editing, setEditing] = useState(null);`

  23 | 
     | Blank line in `src/components/focus-shield/WebsiteListManager.jsx` (search, add, edit, and bulk-edit one domain list), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  24 |   const filtered = useMemo(() => {
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): A memoized value `filtered`, recomputed only when its dependency array changes. `const filtered = useMemo(() => {`

  25 |     const q = search.trim().toLowerCase();
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): `q` is assigned `search.trim().toLowerCase();`. Later lines in this function read that name.

  26 |     if (!q) return items;
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): branch `if (!q) return items;`. Only one side runs.

  27 |     return items.filter(
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): return `return items.filter(`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  28 |       (e) =>
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): statement `(e) =>`. It runs when the top of the file runs, in order, before the next line of the same function.

  29 |         e.value.toLowerCase().includes(q) ||
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): statement `e.value.toLowerCase().includes(q) ||`. It runs when the top of the file runs, in order, before the next line of the same function.

  30 |         (e.label || "").toLowerCase().includes(q) ||
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): statement `(e.label || "").toLowerCase().includes(q) ||`. It runs when the top of the file runs, in order, before the next line of the same function.

  31 |         categoryForDomain(e.value).toLowerCase().includes(q)
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): statement `categoryForDomain(e.value).toLowerCase().includes(q)`. It runs when the top of the file runs, in order, before the next line of the same function.

  32 |     );
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): statement `);`. It runs when the top of the file runs, in order, before the next line of the same function.

  33 |   }, [items, search]);
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): `}, [items, search]);` closes const filtered = useMemo(() => { (opened on line 24). Names declared inside that block end here.

  34 | 
     | Blank line in `src/components/focus-shield/WebsiteListManager.jsx` (search, add, edit, and bulk-edit one domain list), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  35 |   const existingValues = useMemo(() => new Set(items.map((e) => e.value)), [items]);
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): A memoized value `existingValues`, recomputed only when its dependency array changes. `const existingValues = useMemo(() => new Set(items.map((e) => e.value)), [items]);`

  36 | 
     | Blank line in `src/components/focus-shield/WebsiteListManager.jsx` (search, add, edit, and bulk-edit one domain list), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  37 |   function toggleSelect(value) {
     | Defines `toggleSelect` in search, add, edit, and bulk-edit one domain list. Adds or removes a domain from the selection Set.

  38 |     setSelected((prev) => {
     | In `toggleSelect` (src/components/focus-shield/WebsiteListManager.jsx): statement `setSelected((prev) => {`. It runs when toggleSelect runs, in order, before the next line of the same function.

  39 |       const next = new Set(prev);
     | In `toggleSelect` (src/components/focus-shield/WebsiteListManager.jsx): `next` is assigned `new Set(prev);`. Later lines in this function read that name.

  40 |       if (next.has(value)) next.delete(value);
     | In `toggleSelect` (src/components/focus-shield/WebsiteListManager.jsx): branch `if (next.has(value)) next.delete(value);`. Only one side runs.

  41 |       else next.add(value);
     | In `toggleSelect` (src/components/focus-shield/WebsiteListManager.jsx): statement `else next.add(value);`. It runs when toggleSelect runs, in order, before the next line of the same function.

  42 |       return next;
     | In `toggleSelect` (src/components/focus-shield/WebsiteListManager.jsx): return `return next;`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  43 |     });
     | In `toggleSelect` (src/components/focus-shield/WebsiteListManager.jsx): `});` closes setSelected((prev) => { (opened on line 38). Names declared inside that block end here.

  44 |   }
     | In `toggleSelect` (src/components/focus-shield/WebsiteListManager.jsx): `}` closes toggleSelect (opened on line 37). Names declared inside that block end here.

  45 | 
     | Blank line in `src/components/focus-shield/WebsiteListManager.jsx` (search, add, edit, and bulk-edit one domain list), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  46 |   function clearSelection() {
     | Defines `clearSelection` in search, add, edit, and bulk-edit one domain list. Empties that Set.

  47 |     setSelected(new Set());
     | In `clearSelection` (src/components/focus-shield/WebsiteListManager.jsx): statement `setSelected(new Set());`. It runs when clearSelection runs, in order, before the next line of the same function.

  48 |   }
     | In `clearSelection` (src/components/focus-shield/WebsiteListManager.jsx): `}` closes clearSelection (opened on line 46). Names declared inside that block end here.

  49 | 
     | Blank line in `src/components/focus-shield/WebsiteListManager.jsx` (search, add, edit, and bulk-edit one domain list), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  50 |   function updateEntry(value, patch) {
     | Defines `updateEntry` in search, add, edit, and bulk-edit one domain list. Maps the array, replacing the entry with this domain. onChange bubbles to FocusShieldPage.update, which autosaves.

  51 |     onChange(items.map((e) => (e.value === value ? { ...e, ...patch } : e)));
     | In `updateEntry` (src/components/focus-shield/WebsiteListManager.jsx): event prop `onChange(items.map((e) => (e.value === value ? { ...e, ...patch } : e)));`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

  52 |   }
     | In `updateEntry` (src/components/focus-shield/WebsiteListManager.jsx): `}` closes updateEntry (opened on line 50). Names declared inside that block end here.

  53 | 
     | Blank line in `src/components/focus-shield/WebsiteListManager.jsx` (search, add, edit, and bulk-edit one domain list), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  54 |   function deleteEntry(value) {
     | Defines `deleteEntry` in search, add, edit, and bulk-edit one domain list. Filters the domain out and also drops it from the selection.

  55 |     onChange(items.filter((e) => e.value !== value));
     | In `deleteEntry` (src/components/focus-shield/WebsiteListManager.jsx): event prop `onChange(items.filter((e) => e.value !== value));`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

  56 |     setSelected((prev) => {
     | In `deleteEntry` (src/components/focus-shield/WebsiteListManager.jsx): statement `setSelected((prev) => {`. It runs when deleteEntry runs, in order, before the next line of the same function.

  57 |       const next = new Set(prev);
     | In `deleteEntry` (src/components/focus-shield/WebsiteListManager.jsx): `next` is assigned `new Set(prev);`. Later lines in this function read that name.

  58 |       next.delete(value);
     | In `deleteEntry` (src/components/focus-shield/WebsiteListManager.jsx): statement `next.delete(value);`. It runs when deleteEntry runs, in order, before the next line of the same function.

  59 |       return next;
     | In `deleteEntry` (src/components/focus-shield/WebsiteListManager.jsx): return `return next;`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  60 |     });
     | In `deleteEntry` (src/components/focus-shield/WebsiteListManager.jsx): `});` closes setSelected((prev) => { (opened on line 56). Names declared inside that block end here.

  61 |   }
     | In `deleteEntry` (src/components/focus-shield/WebsiteListManager.jsx): `}` closes deleteEntry (opened on line 54). Names declared inside that block end here.

  62 | 
     | Blank line in `src/components/focus-shield/WebsiteListManager.jsx` (search, add, edit, and bulk-edit one domain list), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  63 |   function bulkSetEnabled(enabled) {
     | Defines `bulkSetEnabled` in search, add, edit, and bulk-edit one domain list. Sets enabled on every selected row.

  64 |     onChange(items.map((e) => (selected.has(e.value) ? { ...e, enabled } : e)));
     | In `bulkSetEnabled` (src/components/focus-shield/WebsiteListManager.jsx): event prop `onChange(items.map((e) => (selected.has(e.value) ? { ...e, enabled } : e)));`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

  65 |   }
     | In `bulkSetEnabled` (src/components/focus-shield/WebsiteListManager.jsx): `}` closes bulkSetEnabled (opened on line 63). Names declared inside that block end here.

  66 | 
     | Blank line in `src/components/focus-shield/WebsiteListManager.jsx` (search, add, edit, and bulk-edit one domain list), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  67 |   function bulkDelete() {
     | Defines `bulkDelete` in search, add, edit, and bulk-edit one domain list. Removes every selected row.

  68 |     onChange(items.filter((e) => !selected.has(e.value)));
     | In `bulkDelete` (src/components/focus-shield/WebsiteListManager.jsx): event prop `onChange(items.filter((e) => !selected.has(e.value)));`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

  69 |     clearSelection();
     | In `bulkDelete` (src/components/focus-shield/WebsiteListManager.jsx): statement `clearSelection();`. It runs when bulkDelete runs, in order, before the next line of the same function.

  70 |   }
     | In `bulkDelete` (src/components/focus-shield/WebsiteListManager.jsx): `}` closes bulkDelete (opened on line 67). Names declared inside that block end here.

  71 | 
     | Blank line in `src/components/focus-shield/WebsiteListManager.jsx` (search, add, edit, and bulk-edit one domain list), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  72 |   function handleAdd(newEntries) {
     | Defines `handleAdd` in search, add, edit, and bulk-edit one domain list. Trims the name and calls onAdd, then clears the inputs.

  73 |     onChange([...items, ...newEntries]);
     | In `handleAdd` (src/components/focus-shield/WebsiteListManager.jsx): event prop `onChange([...items, ...newEntries]);`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

  74 |   }
     | In `handleAdd` (src/components/focus-shield/WebsiteListManager.jsx): `}` closes handleAdd (opened on line 72). Names declared inside that block end here.

  75 | 
     | Blank line in `src/components/focus-shield/WebsiteListManager.jsx` (search, add, edit, and bulk-edit one domain list), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  76 |   return (
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  77 |     <section className="profile-settings-card">
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): Opens it. A grouped block on the settings-style pages. Source: `<section className="profile-settings-card">`

  78 |       <div className="profile-settings-card-header fs-section-header">
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="profile-settings-card-header fs-section-header">`

  79 |         <div>
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): Opens it. A box that groups the elements inside it. Source: `<div>`

  80 |           <h2 className="profile-settings-card-title">{title}</h2>
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): JSX `<h2>`. React will create this node when the parent renders.. className chooses the CSS rules from styles.css Source: `<h2 className="profile-settings-card-title">{title}</h2>`

  81 |           <p className="profile-settings-card-desc">{description}</p>
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): Opens it. A paragraph. Source: `<p className="profile-settings-card-desc">{description}</p>`

  82 |         </div>
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  83 |         <button type="button" className="btn btn-primary btn-sm" onClick={() => setAddOpen(true)}>
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button type="button" className="btn btn-primary btn-sm" onClick={() => setAddOpen(true)}>`

  84 |           + Add website
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): statement `+ Add website`. It runs when the top of the file runs, in order, before the next line of the same function.

  85 |         </button>
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

  86 |       </div>
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  87 | 
     | Blank line in `src/components/focus-shield/WebsiteListManager.jsx` (search, add, edit, and bulk-edit one domain list), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  88 |       {items.length > 0 && (
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): statement `{items.length > 0 && (`. It runs when the top of the file runs, in order, before the next line of the same function.

  89 |         <div className="fs-toolbar">
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="fs-toolbar">`

  90 |           <input
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): Opens it. A text or date field. If value and onChange are set, React owns what it shows. Source: `<input`

  91 |             type="search"
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): statement `type="search"`. It runs when the top of the file runs, in order, before the next line of the same function.

  92 |             className="input"
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): statement `className="input"`. It runs when the top of the file runs, in order, before the next line of the same function.

  93 |             style={{ maxWidth: 260 }}
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): `style={{ maxWidth: 260 }}` closes }) { (opened on line 18). Names declared inside that block end here.

  94 |             placeholder="Search domain, name, category…"
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): statement `placeholder="Search domain, name, category…"`. It runs when the top of the file runs, in order, before the next line of the same function.

  95 |             value={search}
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): `value={search}` closes }) { (opened on line 18). Names declared inside that block end here.

  96 |             onChange={(e) => setSearch(e.target.value)}
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): event prop `onChange={(e) => setSearch(e.target.value)}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

  97 |             aria-label={`Search ${title.toLowerCase()}`}
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): `aria-label={`Search ${title.toLowerCase()}`}` closes }) { (opened on line 18). Names declared inside that block end here.

  98 |           />
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): statement `/>`. It runs when the top of the file runs, in order, before the next line of the same function.

  99 |           {selected.size > 0 && (
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): statement `{selected.size > 0 && (`. It runs when the top of the file runs, in order, before the next line of the same function.

 100 |             <div className="fs-bulk-toolbar" role="toolbar" aria-label="Bulk actions">
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="fs-bulk-toolbar" role="toolbar" aria-label="Bulk actions">`

 101 |               <span className="text-xs text-muted">{selected.size} selected</span>
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): Opens it. An inline box. Source: `<span className="text-xs text-muted">{selected.size} selected</span>`

 102 |               <button type="button" className="btn btn-ghost btn-sm" onClick={() => bulkSetEnabled(true)}>Enable</button>
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button type="button" className="btn btn-ghost btn-sm" onClick={() => bulkSetEnabled(true)}>Enable</button>`

 103 |               <button type="button" className="btn btn-ghost btn-sm" onClick={() => bulkSetEnabled(false)}>Disable</button>
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button type="button" className="btn btn-ghost btn-sm" onClick={() => bulkSetEnabled(false)}>Disable</button>`

 104 |               <button type="button" className="btn btn-danger btn-sm" onClick={bulkDelete}>Delete</button>
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button type="button" className="btn btn-danger btn-sm" onClick={bulkDelete}>Delete</button>`

 105 |               <button type="button" className="btn btn-ghost btn-sm" onClick={clearSelection} aria-label="Clear selection">✕</button>
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button type="button" className="btn btn-ghost btn-sm" onClick={clearSelection} aria-label="Clear selection">✕</button>`

 106 |             </div>
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 107 |           )}
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): `)}` closes }) { (opened on line 18). Names declared inside that block end here.

 108 |         </div>
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 109 |       )}
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): `)}` closes }) { (opened on line 18). Names declared inside that block end here.

 110 | 
     | Blank line in `src/components/focus-shield/WebsiteListManager.jsx` (search, add, edit, and bulk-edit one domain list), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

 111 |       {items.length === 0 ? (
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): statement `{items.length === 0 ? (`. It runs when the top of the file runs, in order, before the next line of the same function.

 112 |         <div className="empty-state">
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="empty-state">`

 113 |           <div className="empty-state-icon">{emptyIcon}</div>
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="empty-state-icon">{emptyIcon}</div>`

 114 |           <div className="empty-state-title">{emptyTitle}</div>
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="empty-state-title">{emptyTitle}</div>`

 115 |           <p className="empty-state-body">{emptyBody}</p>
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): Opens it. A paragraph. Source: `<p className="empty-state-body">{emptyBody}</p>`

 116 |           <button type="button" className="btn btn-primary btn-sm" onClick={() => setAddOpen(true)}>
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button type="button" className="btn btn-primary btn-sm" onClick={() => setAddOpen(true)}>`

 117 |             + Add website
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): statement `+ Add website`. It runs when the top of the file runs, in order, before the next line of the same function.

 118 |           </button>
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

 119 |         </div>
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 120 |       ) : filtered.length === 0 ? (
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): statement `) : filtered.length === 0 ? (`. It runs when the top of the file runs, in order, before the next line of the same function.

 121 |         <p className="text-sm text-muted" style={{ padding: "12px 0" }}>
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): Opens it. A paragraph. Source: `<p className="text-sm text-muted" style={{ padding: "12px 0" }}>`

 122 |           No sites match "{search}".
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): `No sites match "{search}".` closes }) { (opened on line 18). Names declared inside that block end here.

 123 |         </p>
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): Closes it. A paragraph. Source: `</p>`

 124 |       ) : (
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): statement `) : (`. It runs when the top of the file runs, in order, before the next line of the same function.

 125 |         <div className="fs-row-list">
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="fs-row-list">`

 126 |           {filtered.map((entry) => (
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): iteration `{filtered.map((entry) => (`.

 127 |             <WebsiteRow
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): Opens it. One domain row. Source: `<WebsiteRow`

 128 |               key={entry.value}
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): `key={entry.value}` closes }) { (opened on line 18). Names declared inside that block end here.

 129 |               entry={entry}
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): `entry={entry}` closes }) { (opened on line 18). Names declared inside that block end here.

 130 |               selected={selected.has(entry.value)}
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): `selected={selected.has(entry.value)}` closes }) { (opened on line 18). Names declared inside that block end here.

 131 |               onToggleSelect={() => toggleSelect(entry.value)}
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): statement `onToggleSelect={() => toggleSelect(entry.value)}`. It runs when the top of the file runs, in order, before the next line of the same function.

 132 |               onToggleEnabled={(v) => updateEntry(entry.value, { enabled: v })}
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): statement `onToggleEnabled={(v) => updateEntry(entry.value, { enabled: v })}`. It runs when the top of the file runs, in order, before the next line of the same function.

 133 |               onEdit={() => setEditing(entry)}
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): statement `onEdit={() => setEditing(entry)}`. It runs when the top of the file runs, in order, before the next line of the same function.

 134 |               onDelete={() => deleteEntry(entry.value)}
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): statement `onDelete={() => deleteEntry(entry.value)}`. It runs when the top of the file runs, in order, before the next line of the same function.

 135 |             />
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): statement `/>`. It runs when the top of the file runs, in order, before the next line of the same function.

 136 |           ))}
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): `))}` closes }) { (opened on line 18). Names declared inside that block end here.

 137 |         </div>
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 138 |       )}
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): `)}` closes }) { (opened on line 18). Names declared inside that block end here.

 139 | 
     | Blank line in `src/components/focus-shield/WebsiteListManager.jsx` (search, add, edit, and bulk-edit one domain list), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

 140 |       <AddWebsiteSheet
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): Opens it. Add-site dialog. Source: `<AddWebsiteSheet`

 141 |         open={addOpen}
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): `open={addOpen}` closes }) { (opened on line 18). Names declared inside that block end here.

 142 |         onClose={() => setAddOpen(false)}
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): statement `onClose={() => setAddOpen(false)}`. It runs when the top of the file runs, in order, before the next line of the same function.

 143 |         existingValues={existingValues}
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): `existingValues={existingValues}` closes }) { (opened on line 18). Names declared inside that block end here.

 144 |         onAdd={handleAdd}
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): `onAdd={handleAdd}` closes }) { (opened on line 18). Names declared inside that block end here.

 145 |         target={target}
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): `target={target}` closes }) { (opened on line 18). Names declared inside that block end here.

 146 |       />
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): statement `/>`. It runs when the top of the file runs, in order, before the next line of the same function.

 147 | 
     | Blank line in `src/components/focus-shield/WebsiteListManager.jsx` (search, add, edit, and bulk-edit one domain list), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

 148 |       <EditRuleSheet
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): Opens it. Edit-one-rule dialog. Source: `<EditRuleSheet`

 149 |         open={!!editing}
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): `open={!!editing}` closes }) { (opened on line 18). Names declared inside that block end here.

 150 |         entry={editing}
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): `entry={editing}` closes }) { (opened on line 18). Names declared inside that block end here.

 151 |         onClose={() => setEditing(null)}
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): statement `onClose={() => setEditing(null)}`. It runs when the top of the file runs, in order, before the next line of the same function.

 152 |         onSave={(updated) => { updateEntry(editing.value, updated); setEditing(null); }}
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): statement `onSave={(updated) => { updateEntry(editing.value, updated); setEditing(null); }}`. It runs when the top of the file runs, in order, before the next line of the same function.

 153 |         onDelete={() => { deleteEntry(editing.value); setEditing(null); }}
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): statement `onDelete={() => { deleteEntry(editing.value); setEditing(null); }}`. It runs when the top of the file runs, in order, before the next line of the same function.

 154 |       />
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): statement `/>`. It runs when the top of the file runs, in order, before the next line of the same function.

 155 |     </section>
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): Closes it. A grouped block on the settings-style pages. Source: `</section>`

 156 |   );
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): statement `);`. It runs when the top of the file runs, in order, before the next line of the same function.

 157 | }
     | In `the top of the file` (src/components/focus-shield/WebsiteListManager.jsx): `}` closes }) { (opened on line 18). Names declared inside that block end here.

