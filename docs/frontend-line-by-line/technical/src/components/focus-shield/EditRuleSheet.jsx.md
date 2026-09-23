# `src/components/focus-shield/EditRuleSheet.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import React, { useEffect, useState } from "react";
     | Import for the sheet for editing one rule: `import React, { useEffect, useState } from "react";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   2 | import Sheet from "./Sheet";
     | Import for the sheet for editing one rule: `import Sheet from "./Sheet";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   3 | import Toggle from "./Toggle";
     | Import for the sheet for editing one rule: `import Toggle from "./Toggle";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   4 | import { normalizeDomain, isValidDomain } from "../../utils/focusShield";
     | Import for the sheet for editing one rule: `import { normalizeDomain, isValidDomain } from "../../utils/focusShield";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   5 | 
     | Blank line in `src/components/focus-shield/EditRuleSheet.jsx` (the sheet for editing one rule), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   6 | export default function EditRuleSheet({ open, entry, onClose, onSave, onDelete }) {
     | Defines `EditRuleSheet` in the sheet for editing one rule. Copies the entry into form state when opened. Save re-validates the domain.

   7 |   const [form, setForm] = useState(null);
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): React state `form, setForm`. The value survives re-renders. Calling the setter re-renders this component. `const [form, setForm] = useState(null);`

   8 |   const [error, setError] = useState("");
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): React state `error, setError`. The value survives re-renders. Calling the setter re-renders this component. `const [error, setError] = useState("");`

   9 | 
     | Blank line in `src/components/focus-shield/EditRuleSheet.jsx` (the sheet for editing one rule), inside EditRuleSheet. The parser skips it. It separates the previous statement from the next so the function is readable.

  10 |   useEffect(() => {
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): opens or continues an effect — `useEffect(() => {`. The effect body runs after paint, and its cleanup runs before the next effect and on unmount.

  11 |     if (open && entry) {
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): branch `if (open && entry) {`. Only one side runs.

  12 |       setForm({ ...entry });
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): `setForm({ ...entry });` closes if (open && entry) { (opened on line 11). Names declared inside that block end here.

  13 |       setError("");
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): statement `setError("");`. It runs when EditRuleSheet runs, in order, before the next line of the same function.

  14 |     }
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): `}` closes if (open && entry) { (opened on line 11). Names declared inside that block end here.

  15 |   }, [open, entry]);
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): `}, [open, entry]);` closes effect in EditRuleSheet (opened on line 10). Names declared inside that block end here.

  16 | 
     | Blank line in `src/components/focus-shield/EditRuleSheet.jsx` (the sheet for editing one rule), inside EditRuleSheet. The parser skips it. It separates the previous statement from the next so the function is readable.

  17 |   if (!open || !form) return null;
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): branch `if (!open || !form) return null;`. Only one side runs.

  18 | 
     | Blank line in `src/components/focus-shield/EditRuleSheet.jsx` (the sheet for editing one rule), inside EditRuleSheet. The parser skips it. It separates the previous statement from the next so the function is readable.

  19 |   function handleSave() {
     | Defines `handleSave` in the sheet for editing one rule. normalizeDomain + isValidDomain, then onSave with the cleaned domain.

  20 |     const domain = normalizeDomain(form.value);
     | In `handleSave` (src/components/focus-shield/EditRuleSheet.jsx): `domain` is assigned `normalizeDomain(form.value);`. Later lines in this function read that name.

  21 |     if (!isValidDomain(domain)) {
     | In `handleSave` (src/components/focus-shield/EditRuleSheet.jsx): branch `if (!isValidDomain(domain)) {`. Only one side runs.

  22 |       setError("Enter a valid domain, e.g. example.com");
     | In `handleSave` (src/components/focus-shield/EditRuleSheet.jsx): statement `setError("Enter a valid domain, e.g. example.com");`. It runs when handleSave runs, in order, before the next line of the same function.

  23 |       return;
     | In `handleSave` (src/components/focus-shield/EditRuleSheet.jsx): return `return;`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  24 |     }
     | In `handleSave` (src/components/focus-shield/EditRuleSheet.jsx): `}` closes if (!isValidDomain(domain)) { (opened on line 21). Names declared inside that block end here.

  25 |     onSave({ ...form, value: domain });
     | In `handleSave` (src/components/focus-shield/EditRuleSheet.jsx): `onSave({ ...form, value: domain });` closes handleSave (opened on line 19). Names declared inside that block end here.

  26 |   }
     | In `handleSave` (src/components/focus-shield/EditRuleSheet.jsx): `}` closes handleSave (opened on line 19). Names declared inside that block end here.

  27 | 
     | Blank line in `src/components/focus-shield/EditRuleSheet.jsx` (the sheet for editing one rule), inside EditRuleSheet. The parser skips it. It separates the previous statement from the next so the function is readable.

  28 |   return (
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  29 |     <Sheet open={open} onClose={onClose} title="Edit rule" labelledBy="fs-edit-sheet-title">
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): Opens it. Shared dialog frame. Source: `<Sheet open={open} onClose={onClose} title="Edit rule" labelledBy="fs-edit-sheet-title">`

  30 |       <div className="profile-form" style={{ gap: 14 }}>
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="profile-form" style={{ gap: 14 }}>`

  31 |         <div className="profile-form-field">
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="profile-form-field">`

  32 |           <label className="profile-form-label" htmlFor="fs-edit-label">Rule name (optional)</label>
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): Opens it. The caption for an input. Source: `<label className="profile-form-label" htmlFor="fs-edit-label">Rule name (optional)</label>`

  33 |           <input
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): Opens it. A text or date field. If value and onChange are set, React owns what it shows. Source: `<input`

  34 |             id="fs-edit-label"
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): statement `id="fs-edit-label"`. It runs when EditRuleSheet runs, in order, before the next line of the same function.

  35 |             className="profile-form-input"
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): statement `className="profile-form-input"`. It runs when EditRuleSheet runs, in order, before the next line of the same function.

  36 |             type="text"
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): statement `type="text"`. It runs when EditRuleSheet runs, in order, before the next line of the same function.

  37 |             value={form.label || ""}
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): `value={form.label || ""}` closes EditRuleSheet (opened on line 6). Names declared inside that block end here.

  38 |             onChange={(e) => setForm((f) => ({ ...f, label: e.target.value }))}
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): event prop `onChange={(e) => setForm((f) => ({ ...f, label: e.target.value }))}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

  39 |             placeholder="e.g. Work Twitter"
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): statement `placeholder="e.g. Work Twitter"`. It runs when EditRuleSheet runs, in order, before the next line of the same function.

  40 |             maxLength={100}
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): `maxLength={100}` closes EditRuleSheet (opened on line 6). Names declared inside that block end here.

  41 |           />
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): statement `/>`. It runs when EditRuleSheet runs, in order, before the next line of the same function.

  42 |         </div>
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  43 | 
     | Blank line in `src/components/focus-shield/EditRuleSheet.jsx` (the sheet for editing one rule), inside EditRuleSheet. The parser skips it. It separates the previous statement from the next so the function is readable.

  44 |         <div className="profile-form-field">
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="profile-form-field">`

  45 |           <label className="profile-form-label" htmlFor="fs-edit-domain">Domain</label>
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): Opens it. The caption for an input. Source: `<label className="profile-form-label" htmlFor="fs-edit-domain">Domain</label>`

  46 |           <input
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): Opens it. A text or date field. If value and onChange are set, React owns what it shows. Source: `<input`

  47 |             id="fs-edit-domain"
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): statement `id="fs-edit-domain"`. It runs when EditRuleSheet runs, in order, before the next line of the same function.

  48 |             className="profile-form-input"
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): statement `className="profile-form-input"`. It runs when EditRuleSheet runs, in order, before the next line of the same function.

  49 |             type="text"
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): statement `type="text"`. It runs when EditRuleSheet runs, in order, before the next line of the same function.

  50 |             value={form.value}
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): `value={form.value}` closes EditRuleSheet (opened on line 6). Names declared inside that block end here.

  51 |             onChange={(e) => { setForm((f) => ({ ...f, value: e.target.value })); setError(""); }}
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): event prop `onChange={(e) => { setForm((f) => ({ ...f, value: e.target.value })); setError(""); }}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

  52 |             placeholder="e.g. twitter.com"
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): statement `placeholder="e.g. twitter.com"`. It runs when EditRuleSheet runs, in order, before the next line of the same function.

  53 |             aria-invalid={!!error}
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): `aria-invalid={!!error}` closes EditRuleSheet (opened on line 6). Names declared inside that block end here.

  54 |           />
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): statement `/>`. It runs when EditRuleSheet runs, in order, before the next line of the same function.

  55 |           {error && <p className="text-xs" style={{ color: "var(--red)", marginTop: 4 }}>{error}</p>}
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): `{error && <p className="text-xs" style={{ color: "var(--red)", marginTop: 4 }}>{error}</p>}` closes EditRuleSheet (opened on line 6). Names declared inside that block end here.

  56 |         </div>
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  57 | 
     | Blank line in `src/components/focus-shield/EditRuleSheet.jsx` (the sheet for editing one rule), inside EditRuleSheet. The parser skips it. It separates the previous statement from the next so the function is readable.

  58 |         <div className="profile-form-field">
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="profile-form-field">`

  59 |           <label className="profile-form-label" htmlFor="fs-edit-notes">Notes (optional)</label>
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): Opens it. The caption for an input. Source: `<label className="profile-form-label" htmlFor="fs-edit-notes">Notes (optional)</label>`

  60 |           <textarea
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): Opens it. A multi-line box. Brain dump and rule notes use it. Source: `<textarea`

  61 |             id="fs-edit-notes"
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): statement `id="fs-edit-notes"`. It runs when EditRuleSheet runs, in order, before the next line of the same function.

  62 |             className="textarea profile-form-input"
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): statement `className="textarea profile-form-input"`. It runs when EditRuleSheet runs, in order, before the next line of the same function.

  63 |             value={form.notes || ""}
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): `value={form.notes || ""}` closes EditRuleSheet (opened on line 6). Names declared inside that block end here.

  64 |             onChange={(e) => setForm((f) => ({ ...f, notes: e.target.value }))}
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): event prop `onChange={(e) => setForm((f) => ({ ...f, notes: e.target.value }))}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

  65 |             placeholder="Why is this rule here?"
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): statement `placeholder="Why is this rule here?"`. It runs when EditRuleSheet runs, in order, before the next line of the same function.

  66 |             maxLength={300}
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): `maxLength={300}` closes EditRuleSheet (opened on line 6). Names declared inside that block end here.

  67 |             rows={2}
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): `rows={2}` closes EditRuleSheet (opened on line 6). Names declared inside that block end here.

  68 |           />
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): statement `/>`. It runs when EditRuleSheet runs, in order, before the next line of the same function.

  69 |         </div>
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  70 | 
     | Blank line in `src/components/focus-shield/EditRuleSheet.jsx` (the sheet for editing one rule), inside EditRuleSheet. The parser skips it. It separates the previous statement from the next so the function is readable.

  71 |         <div className="flex items-center justify-between">
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="flex items-center justify-between">`

  72 |           <span className="profile-form-label" style={{ textTransform: "none" }}>Enabled</span>
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): Opens it. An inline box. Source: `<span className="profile-form-label" style={{ textTransform: "none" }}>Enabled</span>`

  73 |           <Toggle
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): Opens it. On/off switch. The parent owns the boolean. Source: `<Toggle`

  74 |             checked={form.enabled !== false}
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): `checked={form.enabled !== false}` closes EditRuleSheet (opened on line 6). Names declared inside that block end here.

  75 |             onChange={(v) => setForm((f) => ({ ...f, enabled: v }))}
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): event prop `onChange={(v) => setForm((f) => ({ ...f, enabled: v }))}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

  76 |             label="Rule enabled"
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): statement `label="Rule enabled"`. It runs when EditRuleSheet runs, in order, before the next line of the same function.

  77 |           />
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): statement `/>`. It runs when EditRuleSheet runs, in order, before the next line of the same function.

  78 |         </div>
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  79 |       </div>
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  80 | 
     | Blank line in `src/components/focus-shield/EditRuleSheet.jsx` (the sheet for editing one rule), inside EditRuleSheet. The parser skips it. It separates the previous statement from the next so the function is readable.

  81 |       <div className="fs-sheet-footer fs-sheet-footer--split">
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="fs-sheet-footer fs-sheet-footer--split">`

  82 |         <button type="button" className="btn btn-danger" onClick={onDelete}>
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button type="button" className="btn btn-danger" onClick={onDelete}>`

  83 |           Delete
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): statement `Delete`. It runs when EditRuleSheet runs, in order, before the next line of the same function.

  84 |         </button>
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

  85 |         <button type="button" className="btn btn-primary" onClick={handleSave}>
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button type="button" className="btn btn-primary" onClick={handleSave}>`

  86 |           Save
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): statement `Save`. It runs when EditRuleSheet runs, in order, before the next line of the same function.

  87 |         </button>
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

  88 |       </div>
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  89 |     </Sheet>
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): Closes it. Shared dialog frame. Source: `</Sheet>`

  90 |   );
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): statement `);`. It runs when EditRuleSheet runs, in order, before the next line of the same function.

  91 | }
     | In `EditRuleSheet` (src/components/focus-shield/EditRuleSheet.jsx): `}` closes EditRuleSheet (opened on line 6). Names declared inside that block end here.

