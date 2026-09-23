# `src/components/focus-shield/EditRuleSheet.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import React, { useEffect, useState } from "react";
     | Borrows React so this file can remember things and draw the screen.

   2 | import Sheet from "./Sheet";
     | This file borrows a tool another file already made.

   3 | import Toggle from "./Toggle";
     | This file borrows a tool another file already made.

   4 | import { normalizeDomain, isValidDomain } from "../../utils/focusShield";
     | This file borrows a tool another file already made.

   5 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   6 | export default function EditRuleSheet({ open, entry, onClose, onSave, onDelete }) {
     | This starts EditRuleSheet. Copies the entry into form state when opened. Save re-validates the domain.

   7 |   const [form, setForm] = useState(null);
     | This gives a short name to a value so the rest of EditRuleSheet can use it.

   8 |   const [error, setError] = useState("");
     | This gives a short name to a value so the rest of EditRuleSheet can use it.

   9 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  10 |   useEffect(() => {
     | This is an extra job that happens after the picture is drawn.

  11 |     if (open && entry) {
     | This asks a yes-or-no question. The next bit runs only on yes.

  12 |       setForm({ ...entry });
     | This ends if (open && entry) { (opened on line 11).

  13 |       setError("");
     | Inside EditRuleSheet, this line runs as written: setError("");. It happens in order, after the line above it and before the line below it.

  14 |     }
     | This ends if (open && entry) { (opened on line 11).

  15 |   }, [open, entry]);
     | This ends effect in EditRuleSheet (opened on line 10).

  16 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  17 |   if (!open || !form) return null;
     | This asks a yes-or-no question. The next bit runs only on yes.

  18 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  19 |   function handleSave() {
     | This starts handleSave. normalizeDomain + isValidDomain, then onSave with the cleaned domain.

  20 |     const domain = normalizeDomain(form.value);
     | This gives a short name to a value so the rest of handleSave can use it.

  21 |     if (!isValidDomain(domain)) {
     | This asks a yes-or-no question. The next bit runs only on yes.

  22 |       setError("Enter a valid domain, e.g. example.com");
     | Inside handleSave, this line runs as written: setError("Enter a valid domain, e.g. example.com");. It happens in order, after the line above it and before the line below it.

  23 |       return;
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  24 |     }
     | This ends if (!isValidDomain(domain)) { (opened on line 21).

  25 |     onSave({ ...form, value: domain });
     | This ends handleSave (opened on line 19).

  26 |   }
     | This ends handleSave (opened on line 19).

  27 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  28 |   return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  29 |     <Sheet open={open} onClose={onClose} title="Edit rule" labelledBy="fs-edit-sheet-title">
     | This draws one piece of the page while EditRuleSheet is showing.

  30 |       <div className="profile-form" style={{ gap: 14 }}>
     | This draws one piece of the page while EditRuleSheet is showing.

  31 |         <div className="profile-form-field">
     | This draws one piece of the page while EditRuleSheet is showing.

  32 |           <label className="profile-form-label" htmlFor="fs-edit-label">Rule name (optional)</label>
     | This draws one piece of the page while EditRuleSheet is showing.

  33 |           <input
     | This draws one piece of the page while EditRuleSheet is showing.

  34 |             id="fs-edit-label"
     | Inside EditRuleSheet, this line runs as written: id="fs-edit-label". It happens in order, after the line above it and before the line below it.

  35 |             className="profile-form-input"
     | Inside EditRuleSheet, this line runs as written: className="profile-form-input". It happens in order, after the line above it and before the line below it.

  36 |             type="text"
     | Inside EditRuleSheet, this line runs as written: type="text". It happens in order, after the line above it and before the line below it.

  37 |             value={form.label || ""}
     | This ends EditRuleSheet (opened on line 6).

  38 |             onChange={(e) => setForm((f) => ({ ...f, label: e.target.value }))}
     | This ends EditRuleSheet (opened on line 6).

  39 |             placeholder="e.g. Work Twitter"
     | Inside EditRuleSheet, this line runs as written: placeholder="e.g. Work Twitter". It happens in order, after the line above it and before the line below it.

  40 |             maxLength={100}
     | This ends EditRuleSheet (opened on line 6).

  41 |           />
     | This closes a box of instructions that opened above.

  42 |         </div>
     | This ends a drawing that EditRuleSheet started just above.

  43 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  44 |         <div className="profile-form-field">
     | This draws one piece of the page while EditRuleSheet is showing.

  45 |           <label className="profile-form-label" htmlFor="fs-edit-domain">Domain</label>
     | This draws one piece of the page while EditRuleSheet is showing.

  46 |           <input
     | This draws one piece of the page while EditRuleSheet is showing.

  47 |             id="fs-edit-domain"
     | Inside EditRuleSheet, this line runs as written: id="fs-edit-domain". It happens in order, after the line above it and before the line below it.

  48 |             className="profile-form-input"
     | Inside EditRuleSheet, this line runs as written: className="profile-form-input". It happens in order, after the line above it and before the line below it.

  49 |             type="text"
     | Inside EditRuleSheet, this line runs as written: type="text". It happens in order, after the line above it and before the line below it.

  50 |             value={form.value}
     | This ends EditRuleSheet (opened on line 6).

  51 |             onChange={(e) => { setForm((f) => ({ ...f, value: e.target.value })); setError(""); }}
     | This ends EditRuleSheet (opened on line 6).

  52 |             placeholder="e.g. twitter.com"
     | Inside EditRuleSheet, this line runs as written: placeholder="e.g. twitter.com". It happens in order, after the line above it and before the line below it.

  53 |             aria-invalid={!!error}
     | This ends EditRuleSheet (opened on line 6).

  54 |           />
     | This closes a box of instructions that opened above.

  55 |           {error && <p className="text-xs" style={{ color: "var(--red)", marginTop: 4 }}>{error}</p>}
     | This ends EditRuleSheet (opened on line 6).

  56 |         </div>
     | This ends a drawing that EditRuleSheet started just above.

  57 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  58 |         <div className="profile-form-field">
     | This draws one piece of the page while EditRuleSheet is showing.

  59 |           <label className="profile-form-label" htmlFor="fs-edit-notes">Notes (optional)</label>
     | This draws one piece of the page while EditRuleSheet is showing.

  60 |           <textarea
     | This draws one piece of the page while EditRuleSheet is showing.

  61 |             id="fs-edit-notes"
     | Inside EditRuleSheet, this line runs as written: id="fs-edit-notes". It happens in order, after the line above it and before the line below it.

  62 |             className="textarea profile-form-input"
     | Inside EditRuleSheet, this line runs as written: className="textarea profile-form-input". It happens in order, after the line above it and before the line below it.

  63 |             value={form.notes || ""}
     | This ends EditRuleSheet (opened on line 6).

  64 |             onChange={(e) => setForm((f) => ({ ...f, notes: e.target.value }))}
     | This ends EditRuleSheet (opened on line 6).

  65 |             placeholder="Why is this rule here?"
     | Inside EditRuleSheet, this line runs as written: placeholder="Why is this rule here?". It happens in order, after the line above it and before the line below it.

  66 |             maxLength={300}
     | This ends EditRuleSheet (opened on line 6).

  67 |             rows={2}
     | This ends EditRuleSheet (opened on line 6).

  68 |           />
     | This closes a box of instructions that opened above.

  69 |         </div>
     | This ends a drawing that EditRuleSheet started just above.

  70 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  71 |         <div className="flex items-center justify-between">
     | This draws one piece of the page while EditRuleSheet is showing.

  72 |           <span className="profile-form-label" style={{ textTransform: "none" }}>Enabled</span>
     | This draws one piece of the page while EditRuleSheet is showing.

  73 |           <Toggle
     | This draws one piece of the page while EditRuleSheet is showing.

  74 |             checked={form.enabled !== false}
     | This ends EditRuleSheet (opened on line 6).

  75 |             onChange={(v) => setForm((f) => ({ ...f, enabled: v }))}
     | This ends EditRuleSheet (opened on line 6).

  76 |             label="Rule enabled"
     | Inside EditRuleSheet, this line runs as written: label="Rule enabled". It happens in order, after the line above it and before the line below it.

  77 |           />
     | This closes a box of instructions that opened above.

  78 |         </div>
     | This ends a drawing that EditRuleSheet started just above.

  79 |       </div>
     | This ends a drawing that EditRuleSheet started just above.

  80 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  81 |       <div className="fs-sheet-footer fs-sheet-footer--split">
     | This draws one piece of the page while EditRuleSheet is showing.

  82 |         <button type="button" className="btn btn-danger" onClick={onDelete}>
     | This draws one piece of the page while EditRuleSheet is showing.

  83 |           Delete
     | Inside EditRuleSheet, this line runs as written: Delete. It happens in order, after the line above it and before the line below it.

  84 |         </button>
     | This ends a drawing that EditRuleSheet started just above.

  85 |         <button type="button" className="btn btn-primary" onClick={handleSave}>
     | This draws one piece of the page while EditRuleSheet is showing.

  86 |           Save
     | Inside EditRuleSheet, this line runs as written: Save. It happens in order, after the line above it and before the line below it.

  87 |         </button>
     | This ends a drawing that EditRuleSheet started just above.

  88 |       </div>
     | This ends a drawing that EditRuleSheet started just above.

  89 |     </Sheet>
     | This ends a drawing that EditRuleSheet started just above.

  90 |   );
     | This closes a box of instructions that opened above.

  91 | }
     | This ends EditRuleSheet (opened on line 6).

