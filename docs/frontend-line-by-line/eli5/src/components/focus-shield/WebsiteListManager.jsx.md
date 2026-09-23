# `src/components/focus-shield/WebsiteListManager.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import React, { useMemo, useState } from "react";
     | Borrows React so this file can remember things and draw the screen.

   2 | import WebsiteRow from "./WebsiteRow";
     | This file borrows a tool another file already made.

   3 | import AddWebsiteSheet from "./AddWebsiteSheet";
     | This file borrows a tool another file already made.

   4 | import EditRuleSheet from "./EditRuleSheet";
     | This file borrows a tool another file already made.

   5 | import { categoryForDomain } from "../../utils/focusShield";
     | This file borrows a tool another file already made.

   6 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   7 | // Generic add/edit/delete/search/bulk-action manager for one list of domains — reused for
     | A note written for people. The app does not run it.

   8 | // both "Blocked Websites" and "Whitelisted Websites" so the two sections never drift apart.
     | A note written for people. The app does not run it.

   9 | export default function WebsiteListManager({
     | This starts WebsiteListManager. One list, used twice: blocked sites and whitelist. Search, selection, bulk enable/disable/delete, add sheet, edit sheet.

  10 |   title,
     | Inside WebsiteListManager, this line runs as written: title,. It happens in order, after the line above it and before the line below it.

  11 |   description,
     | Inside WebsiteListManager, this line runs as written: description,. It happens in order, after the line above it and before the line below it.

  12 |   items,
     | Inside WebsiteListManager, this line runs as written: items,. It happens in order, after the line above it and before the line below it.

  13 |   onChange,
     | Inside WebsiteListManager, this line runs as written: onChange,. It happens in order, after the line above it and before the line below it.

  14 |   target,
     | Inside WebsiteListManager, this line runs as written: target,. It happens in order, after the line above it and before the line below it.

  15 |   emptyIcon,
     | Inside WebsiteListManager, this line runs as written: emptyIcon,. It happens in order, after the line above it and before the line below it.

  16 |   emptyTitle,
     | Inside WebsiteListManager, this line runs as written: emptyTitle,. It happens in order, after the line above it and before the line below it.

  17 |   emptyBody,
     | Inside WebsiteListManager, this line runs as written: emptyBody,. It happens in order, after the line above it and before the line below it.

  18 | }) {
     | This ends WebsiteListManager (opened on line 9).

  19 |   const [search, setSearch] = useState("");
     | This gives a short name to a value so the rest of the top of the file can use it.

  20 |   const [selected, setSelected] = useState(() => new Set());
     | This gives a short name to a value so the rest of the top of the file can use it.

  21 |   const [addOpen, setAddOpen] = useState(false);
     | This gives a short name to a value so the rest of the top of the file can use it.

  22 |   const [editing, setEditing] = useState(null);
     | This gives a short name to a value so the rest of the top of the file can use it.

  23 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  24 |   const filtered = useMemo(() => {
     | This gives a short name to a value so the rest of the top of the file can use it.

  25 |     const q = search.trim().toLowerCase();
     | This gives a short name to a value so the rest of the top of the file can use it.

  26 |     if (!q) return items;
     | This asks a yes-or-no question. The next bit runs only on yes.

  27 |     return items.filter(
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  28 |       (e) =>
     | Inside the top of the file, this line runs as written: (e) =>. It happens in order, after the line above it and before the line below it.

  29 |         e.value.toLowerCase().includes(q) ||
     | Inside the top of the file, this line runs as written: e.value.toLowerCase().includes(q) ||. It happens in order, after the line above it and before the line below it.

  30 |         (e.label || "").toLowerCase().includes(q) ||
     | Inside the top of the file, this line runs as written: (e.label || "").toLowerCase().includes(q) ||. It happens in order, after the line above it and before the line below it.

  31 |         categoryForDomain(e.value).toLowerCase().includes(q)
     | Inside the top of the file, this line runs as written: categoryForDomain(e.value).toLowerCase().includes(q). It happens in order, after the line above it and before the line below it.

  32 |     );
     | This closes a box of instructions that opened above.

  33 |   }, [items, search]);
     | This ends const filtered = useMemo(() => { (opened on line 24).

  34 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  35 |   const existingValues = useMemo(() => new Set(items.map((e) => e.value)), [items]);
     | This gives a short name to a value so the rest of the top of the file can use it.

  36 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  37 |   function toggleSelect(value) {
     | This starts toggleSelect. Adds or removes a domain from the selection Set.

  38 |     setSelected((prev) => {
     | Inside toggleSelect, this line runs as written: setSelected((prev) => {. It happens in order, after the line above it and before the line below it.

  39 |       const next = new Set(prev);
     | This gives a short name to a value so the rest of toggleSelect can use it.

  40 |       if (next.has(value)) next.delete(value);
     | This asks a yes-or-no question. The next bit runs only on yes.

  41 |       else next.add(value);
     | Inside toggleSelect, this line runs as written: else next.add(value);. It happens in order, after the line above it and before the line below it.

  42 |       return next;
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  43 |     });
     | This ends setSelected((prev) => { (opened on line 38).

  44 |   }
     | This ends toggleSelect (opened on line 37).

  45 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  46 |   function clearSelection() {
     | This starts clearSelection. Empties that Set.

  47 |     setSelected(new Set());
     | Inside clearSelection, this line runs as written: setSelected(new Set());. It happens in order, after the line above it and before the line below it.

  48 |   }
     | This ends clearSelection (opened on line 46).

  49 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  50 |   function updateEntry(value, patch) {
     | This starts updateEntry. Maps the array, replacing the entry with this domain. onChange bubbles to FocusShieldPage.update, which autosaves.

  51 |     onChange(items.map((e) => (e.value === value ? { ...e, ...patch } : e)));
     | This ends updateEntry (opened on line 50).

  52 |   }
     | This ends updateEntry (opened on line 50).

  53 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  54 |   function deleteEntry(value) {
     | This starts deleteEntry. Filters the domain out and also drops it from the selection.

  55 |     onChange(items.filter((e) => e.value !== value));
     | Inside deleteEntry, this line runs as written: onChange(items.filter((e) => e.value !== value));. It happens in order, after the line above it and before the line below it.

  56 |     setSelected((prev) => {
     | Inside deleteEntry, this line runs as written: setSelected((prev) => {. It happens in order, after the line above it and before the line below it.

  57 |       const next = new Set(prev);
     | This gives a short name to a value so the rest of deleteEntry can use it.

  58 |       next.delete(value);
     | Inside deleteEntry, this line runs as written: next.delete(value);. It happens in order, after the line above it and before the line below it.

  59 |       return next;
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  60 |     });
     | This ends setSelected((prev) => { (opened on line 56).

  61 |   }
     | This ends deleteEntry (opened on line 54).

  62 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  63 |   function bulkSetEnabled(enabled) {
     | This starts bulkSetEnabled. Sets enabled on every selected row.

  64 |     onChange(items.map((e) => (selected.has(e.value) ? { ...e, enabled } : e)));
     | This ends bulkSetEnabled (opened on line 63).

  65 |   }
     | This ends bulkSetEnabled (opened on line 63).

  66 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  67 |   function bulkDelete() {
     | This starts bulkDelete. Removes every selected row.

  68 |     onChange(items.filter((e) => !selected.has(e.value)));
     | Inside bulkDelete, this line runs as written: onChange(items.filter((e) => !selected.has(e.value)));. It happens in order, after the line above it and before the line below it.

  69 |     clearSelection();
     | Inside bulkDelete, this line runs as written: clearSelection();. It happens in order, after the line above it and before the line below it.

  70 |   }
     | This ends bulkDelete (opened on line 67).

  71 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  72 |   function handleAdd(newEntries) {
     | This starts handleAdd. Trims the name and calls onAdd, then clears the inputs.

  73 |     onChange([...items, ...newEntries]);
     | Inside handleAdd, this line runs as written: onChange([...items, ...newEntries]);. It happens in order, after the line above it and before the line below it.

  74 |   }
     | This ends handleAdd (opened on line 72).

  75 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  76 |   return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  77 |     <section className="profile-settings-card">
     | This draws one piece of the page while the top of the file is showing.

  78 |       <div className="profile-settings-card-header fs-section-header">
     | This draws one piece of the page while the top of the file is showing.

  79 |         <div>
     | This draws one piece of the page while the top of the file is showing.

  80 |           <h2 className="profile-settings-card-title">{title}</h2>
     | This draws one piece of the page while the top of the file is showing.

  81 |           <p className="profile-settings-card-desc">{description}</p>
     | This draws one piece of the page while the top of the file is showing.

  82 |         </div>
     | This ends a drawing that the top of the file started just above.

  83 |         <button type="button" className="btn btn-primary btn-sm" onClick={() => setAddOpen(true)}>
     | This draws one piece of the page while the top of the file is showing.

  84 |           + Add website
     | Inside the top of the file, this line runs as written: + Add website. It happens in order, after the line above it and before the line below it.

  85 |         </button>
     | This ends a drawing that the top of the file started just above.

  86 |       </div>
     | This ends a drawing that the top of the file started just above.

  87 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  88 |       {items.length > 0 && (
     | Inside the top of the file, this line runs as written: {items.length > 0 && (. It happens in order, after the line above it and before the line below it.

  89 |         <div className="fs-toolbar">
     | This draws one piece of the page while the top of the file is showing.

  90 |           <input
     | This draws one piece of the page while the top of the file is showing.

  91 |             type="search"
     | Inside the top of the file, this line runs as written: type="search". It happens in order, after the line above it and before the line below it.

  92 |             className="input"
     | Inside the top of the file, this line runs as written: className="input". It happens in order, after the line above it and before the line below it.

  93 |             style={{ maxWidth: 260 }}
     | This ends }) { (opened on line 18).

  94 |             placeholder="Search domain, name, category…"
     | Inside the top of the file, this line runs as written: placeholder="Search domain, name, category…". It happens in order, after the line above it and before the line below it.

  95 |             value={search}
     | This ends }) { (opened on line 18).

  96 |             onChange={(e) => setSearch(e.target.value)}
     | This ends }) { (opened on line 18).

  97 |             aria-label={`Search ${title.toLowerCase()}`}
     | This ends }) { (opened on line 18).

  98 |           />
     | This closes a box of instructions that opened above.

  99 |           {selected.size > 0 && (
     | Inside the top of the file, this line runs as written: {selected.size > 0 && (. It happens in order, after the line above it and before the line below it.

 100 |             <div className="fs-bulk-toolbar" role="toolbar" aria-label="Bulk actions">
     | This draws one piece of the page while the top of the file is showing.

 101 |               <span className="text-xs text-muted">{selected.size} selected</span>
     | This draws one piece of the page while the top of the file is showing.

 102 |               <button type="button" className="btn btn-ghost btn-sm" onClick={() => bulkSetEnabled(true)}>Enable</button>
     | This draws one piece of the page while the top of the file is showing.

 103 |               <button type="button" className="btn btn-ghost btn-sm" onClick={() => bulkSetEnabled(false)}>Disable</button>
     | This draws one piece of the page while the top of the file is showing.

 104 |               <button type="button" className="btn btn-danger btn-sm" onClick={bulkDelete}>Delete</button>
     | This draws one piece of the page while the top of the file is showing.

 105 |               <button type="button" className="btn btn-ghost btn-sm" onClick={clearSelection} aria-label="Clear selection">✕</button>
     | This draws one piece of the page while the top of the file is showing.

 106 |             </div>
     | This ends a drawing that the top of the file started just above.

 107 |           )}
     | This ends }) { (opened on line 18).

 108 |         </div>
     | This ends a drawing that the top of the file started just above.

 109 |       )}
     | This ends }) { (opened on line 18).

 110 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 111 |       {items.length === 0 ? (
     | Inside the top of the file, this line runs as written: {items.length === 0 ? (. It happens in order, after the line above it and before the line below it.

 112 |         <div className="empty-state">
     | This draws one piece of the page while the top of the file is showing.

 113 |           <div className="empty-state-icon">{emptyIcon}</div>
     | This draws one piece of the page while the top of the file is showing.

 114 |           <div className="empty-state-title">{emptyTitle}</div>
     | This draws one piece of the page while the top of the file is showing.

 115 |           <p className="empty-state-body">{emptyBody}</p>
     | This draws one piece of the page while the top of the file is showing.

 116 |           <button type="button" className="btn btn-primary btn-sm" onClick={() => setAddOpen(true)}>
     | This draws one piece of the page while the top of the file is showing.

 117 |             + Add website
     | Inside the top of the file, this line runs as written: + Add website. It happens in order, after the line above it and before the line below it.

 118 |           </button>
     | This ends a drawing that the top of the file started just above.

 119 |         </div>
     | This ends a drawing that the top of the file started just above.

 120 |       ) : filtered.length === 0 ? (
     | This closes a box of instructions that opened above.

 121 |         <p className="text-sm text-muted" style={{ padding: "12px 0" }}>
     | This draws one piece of the page while the top of the file is showing.

 122 |           No sites match "{search}".
     | This ends }) { (opened on line 18).

 123 |         </p>
     | This ends a drawing that the top of the file started just above.

 124 |       ) : (
     | This closes a box of instructions that opened above.

 125 |         <div className="fs-row-list">
     | This draws one piece of the page while the top of the file is showing.

 126 |           {filtered.map((entry) => (
     | Inside the top of the file, this line runs as written: {filtered.map((entry) => (. It happens in order, after the line above it and before the line below it.

 127 |             <WebsiteRow
     | This draws one piece of the page while the top of the file is showing.

 128 |               key={entry.value}
     | This ends }) { (opened on line 18).

 129 |               entry={entry}
     | This ends }) { (opened on line 18).

 130 |               selected={selected.has(entry.value)}
     | This ends }) { (opened on line 18).

 131 |               onToggleSelect={() => toggleSelect(entry.value)}
     | This ends }) { (opened on line 18).

 132 |               onToggleEnabled={(v) => updateEntry(entry.value, { enabled: v })}
     | This ends }) { (opened on line 18).

 133 |               onEdit={() => setEditing(entry)}
     | This ends }) { (opened on line 18).

 134 |               onDelete={() => deleteEntry(entry.value)}
     | This ends }) { (opened on line 18).

 135 |             />
     | This closes a box of instructions that opened above.

 136 |           ))}
     | This ends }) { (opened on line 18).

 137 |         </div>
     | This ends a drawing that the top of the file started just above.

 138 |       )}
     | This ends }) { (opened on line 18).

 139 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 140 |       <AddWebsiteSheet
     | This draws one piece of the page while the top of the file is showing.

 141 |         open={addOpen}
     | This ends }) { (opened on line 18).

 142 |         onClose={() => setAddOpen(false)}
     | This ends }) { (opened on line 18).

 143 |         existingValues={existingValues}
     | This ends }) { (opened on line 18).

 144 |         onAdd={handleAdd}
     | This ends }) { (opened on line 18).

 145 |         target={target}
     | This ends }) { (opened on line 18).

 146 |       />
     | This closes a box of instructions that opened above.

 147 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 148 |       <EditRuleSheet
     | This draws one piece of the page while the top of the file is showing.

 149 |         open={!!editing}
     | This ends }) { (opened on line 18).

 150 |         entry={editing}
     | This ends }) { (opened on line 18).

 151 |         onClose={() => setEditing(null)}
     | This ends }) { (opened on line 18).

 152 |         onSave={(updated) => { updateEntry(editing.value, updated); setEditing(null); }}
     | This ends }) { (opened on line 18).

 153 |         onDelete={() => { deleteEntry(editing.value); setEditing(null); }}
     | This ends }) { (opened on line 18).

 154 |       />
     | This closes a box of instructions that opened above.

 155 |     </section>
     | This ends a drawing that the top of the file started just above.

 156 |   );
     | This closes a box of instructions that opened above.

 157 | }
     | This ends }) { (opened on line 18).

