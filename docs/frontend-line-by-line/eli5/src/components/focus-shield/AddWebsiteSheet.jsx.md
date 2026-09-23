# `src/components/focus-shield/AddWebsiteSheet.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import React, { useMemo, useState } from "react";
     | Borrows React so this file can remember things and draw the screen.

   2 | import Sheet from "./Sheet";
     | This file borrows a tool another file already made.

   3 | import { POPULAR_SITES, normalizeDomain, isValidDomain } from "../../utils/focusShield";
     | This file borrows a tool another file already made.

   4 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   5 | export default function AddWebsiteSheet({ open, onClose, existingValues, onAdd, target }) {
     | This starts AddWebsiteSheet. Searchable popular chips plus a custom domain field. onAdd receives an array of one entry.

   6 |   const [search, setSearch] = useState("");
     | This gives a short name to a value so the rest of AddWebsiteSheet can use it.

   7 |   const [customValue, setCustomValue] = useState("");
     | This gives a short name to a value so the rest of AddWebsiteSheet can use it.

   8 |   const [customError, setCustomError] = useState("");
     | This gives a short name to a value so the rest of AddWebsiteSheet can use it.

   9 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  10 |   const filtered = useMemo(() => {
     | This gives a short name to a value so the rest of AddWebsiteSheet can use it.

  11 |     const q = search.trim().toLowerCase();
     | This gives a short name to a value so the rest of AddWebsiteSheet can use it.

  12 |     if (!q) return POPULAR_SITES;
     | This asks a yes-or-no question. The next bit runs only on yes.

  13 |     return POPULAR_SITES.filter(
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  14 |       (s) => s.label.toLowerCase().includes(q) || s.domain.includes(q) || s.category.toLowerCase().includes(q)
     | Inside AddWebsiteSheet, this line runs as written: (s) => s.label.toLowerCase().includes(q) || s.domain.includes(q) || s.category.toLowerCase().includes(q). It happens in order, after the line above it and before the line below it.

  15 |     );
     | This closes a box of instructions that opened above.

  16 |   }, [search]);
     | This ends const filtered = useMemo(() => { (opened on line 10).

  17 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  18 |   function handleClose() {
     | This starts handleClose. Clears the sheet's fields, then calls the parent's onClose.

  19 |     setSearch("");
     | Inside handleClose, this line runs as written: setSearch("");. It happens in order, after the line above it and before the line below it.

  20 |     setCustomValue("");
     | Inside handleClose, this line runs as written: setCustomValue("");. It happens in order, after the line above it and before the line below it.

  21 |     setCustomError("");
     | Inside handleClose, this line runs as written: setCustomError("");. It happens in order, after the line above it and before the line below it.

  22 |     onClose();
     | Inside handleClose, this line runs as written: onClose();. It happens in order, after the line above it and before the line below it.

  23 |   }
     | This ends handleClose (opened on line 18).

  24 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  25 |   function addPopular(site) {
     | This starts addPopular. Adds the chip's domain unless existingValues already has it.

  26 |     if (existingValues.has(site.domain)) return;
     | This asks a yes-or-no question. The next bit runs only on yes.

  27 |     onAdd([{ value: site.domain, label: site.label, enabled: true }]);
     | This ends addPopular (opened on line 25).

  28 |   }
     | This ends addPopular (opened on line 25).

  29 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  30 |   function addCustom() {
     | This starts addCustom. Normalizes and validates. Sets an error string instead of adding when the domain is bad or duplicate.

  31 |     const domain = normalizeDomain(customValue);
     | This gives a short name to a value so the rest of addCustom can use it.

  32 |     if (!isValidDomain(domain)) {
     | This asks a yes-or-no question. The next bit runs only on yes.

  33 |       setCustomError("Enter a valid domain, e.g. example.com");
     | Inside addCustom, this line runs as written: setCustomError("Enter a valid domain, e.g. example.com");. It happens in order, after the line above it and before the line below it.

  34 |       return;
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  35 |     }
     | This ends if (!isValidDomain(domain)) { (opened on line 32).

  36 |     if (existingValues.has(domain)) {
     | This asks a yes-or-no question. The next bit runs only on yes.

  37 |       setCustomError("That site is already on this list");
     | Inside addCustom, this line runs as written: setCustomError("That site is already on this list");. It happens in order, after the line above it and before the line below it.

  38 |       return;
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  39 |     }
     | This ends if (existingValues.has(domain)) { (opened on line 36).

  40 |     onAdd([{ value: domain, label: "", enabled: true }]);
     | This ends addCustom (opened on line 30).

  41 |     setCustomValue("");
     | Inside addCustom, this line runs as written: setCustomValue("");. It happens in order, after the line above it and before the line below it.

  42 |     setCustomError("");
     | Inside addCustom, this line runs as written: setCustomError("");. It happens in order, after the line above it and before the line below it.

  43 |   }
     | This ends addCustom (opened on line 30).

  44 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  45 |   function handleCustomKey(e) {
     | This starts handleCustomKey. Enter in the custom field calls addCustom.

  46 |     if (e.key === "Enter") {
     | This asks a yes-or-no question. The next bit runs only on yes.

  47 |       e.preventDefault();
     | Inside handleCustomKey, this line runs as written: e.preventDefault();. It happens in order, after the line above it and before the line below it.

  48 |       addCustom();
     | Inside handleCustomKey, this line runs as written: addCustom();. It happens in order, after the line above it and before the line below it.

  49 |     }
     | This ends if (e.key === "Enter") { (opened on line 46).

  50 |   }
     | This ends handleCustomKey (opened on line 45).

  51 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  52 |   return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  53 |     <Sheet
     | This draws one piece of the page while AddWebsiteSheet is showing.

  54 |       open={open}
     | This ends AddWebsiteSheet (opened on line 5).

  55 |       onClose={handleClose}
     | This ends AddWebsiteSheet (opened on line 5).

  56 |       title={target === "whitelist" ? "Add to whitelist" : "Add website"}
     | This ends AddWebsiteSheet (opened on line 5).

  57 |       labelledBy="fs-add-sheet-title"
     | Inside AddWebsiteSheet, this line runs as written: labelledBy="fs-add-sheet-title". It happens in order, after the line above it and before the line below it.

  58 |     >
     | Inside AddWebsiteSheet, this line runs as written: >. It happens in order, after the line above it and before the line below it.

  59 |       <div className="profile-form-field" style={{ marginBottom: 14 }}>
     | This draws one piece of the page while AddWebsiteSheet is showing.

  60 |         <label className="profile-form-label" htmlFor="fs-add-search">Search</label>
     | This draws one piece of the page while AddWebsiteSheet is showing.

  61 |         <input
     | This draws one piece of the page while AddWebsiteSheet is showing.

  62 |           id="fs-add-search"
     | Inside AddWebsiteSheet, this line runs as written: id="fs-add-search". It happens in order, after the line above it and before the line below it.

  63 |           className="profile-form-input"
     | Inside AddWebsiteSheet, this line runs as written: className="profile-form-input". It happens in order, after the line above it and before the line below it.

  64 |           type="search"
     | Inside AddWebsiteSheet, this line runs as written: type="search". It happens in order, after the line above it and before the line below it.

  65 |           value={search}
     | This ends AddWebsiteSheet (opened on line 5).

  66 |           onChange={(e) => setSearch(e.target.value)}
     | This ends AddWebsiteSheet (opened on line 5).

  67 |           placeholder="Search popular sites or categories…"
     | Inside AddWebsiteSheet, this line runs as written: placeholder="Search popular sites or categories…". It happens in order, after the line above it and before the line below it.

  68 |         />
     | This closes a box of instructions that opened above.

  69 |       </div>
     | This ends a drawing that AddWebsiteSheet started just above.

  70 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  71 |       <p className="profile-form-label" style={{ marginBottom: 8 }}>Popular websites</p>
     | This draws one piece of the page while AddWebsiteSheet is showing.

  72 |       <div className="fs-popular-grid">
     | This draws one piece of the page while AddWebsiteSheet is showing.

  73 |         {filtered.map((site) => {
     | Inside AddWebsiteSheet, this line runs as written: {filtered.map((site) => {. It happens in order, after the line above it and before the line below it.

  74 |           const added = existingValues.has(site.domain);
     | This gives a short name to a value so the rest of AddWebsiteSheet can use it.

  75 |           return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  76 |             <button
     | This draws one piece of the page while AddWebsiteSheet is showing.

  77 |               key={site.id}
     | This ends {filtered.map((site) => { (opened on line 73).

  78 |               type="button"
     | Inside AddWebsiteSheet, this line runs as written: type="button". It happens in order, after the line above it and before the line below it.

  79 |               className={`fs-popular-chip${added ? " fs-popular-chip--added" : ""}`}
     | This ends {filtered.map((site) => { (opened on line 73).

  80 |               onClick={() => addPopular(site)}
     | This decides what happens when you press.

  81 |               disabled={added}
     | This ends {filtered.map((site) => { (opened on line 73).

  82 |               aria-pressed={added}
     | This ends {filtered.map((site) => { (opened on line 73).

  83 |             >
     | Inside AddWebsiteSheet, this line runs as written: >. It happens in order, after the line above it and before the line below it.

  84 |               <span className="fs-popular-emoji" aria-hidden="true">{site.emoji}</span>
     | This draws one piece of the page while AddWebsiteSheet is showing.

  85 |               <span className="fs-popular-label">{site.label}</span>
     | This draws one piece of the page while AddWebsiteSheet is showing.

  86 |               <span className="fs-popular-status">{added ? "✓ Added" : "+ Add"}</span>
     | This draws one piece of the page while AddWebsiteSheet is showing.

  87 |             </button>
     | This ends a drawing that AddWebsiteSheet started just above.

  88 |           );
     | This closes a box of instructions that opened above.

  89 |         })}
     | This ends {filtered.map((site) => { (opened on line 73).

  90 |         {filtered.length === 0 && (
     | Inside AddWebsiteSheet, this line runs as written: {filtered.length === 0 && (. It happens in order, after the line above it and before the line below it.

  91 |           <p className="text-sm text-muted">No matches — try adding it as a custom domain below.</p>
     | This draws one piece of the page while AddWebsiteSheet is showing.

  92 |         )}
     | This ends AddWebsiteSheet (opened on line 5).

  93 |       </div>
     | This ends a drawing that AddWebsiteSheet started just above.

  94 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  95 |       <div className="fs-sheet-divider" />
     | This draws one piece of the page while AddWebsiteSheet is showing.

  96 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  97 |       <p className="profile-form-label" style={{ marginBottom: 8 }}>Custom domain</p>
     | This draws one piece of the page while AddWebsiteSheet is showing.

  98 |       <div className="fs-custom-domain-row">
     | This draws one piece of the page while AddWebsiteSheet is showing.

  99 |         <input
     | This draws one piece of the page while AddWebsiteSheet is showing.

 100 |           className="profile-form-input"
     | Inside AddWebsiteSheet, this line runs as written: className="profile-form-input". It happens in order, after the line above it and before the line below it.

 101 |           type="text"
     | Inside AddWebsiteSheet, this line runs as written: type="text". It happens in order, after the line above it and before the line below it.

 102 |           value={customValue}
     | This ends AddWebsiteSheet (opened on line 5).

 103 |           onChange={(e) => { setCustomValue(e.target.value); setCustomError(""); }}
     | This ends AddWebsiteSheet (opened on line 5).

 104 |           onKeyDown={handleCustomKey}
     | This ends AddWebsiteSheet (opened on line 5).

 105 |           placeholder="e.g. news.ycombinator.com"
     | Inside AddWebsiteSheet, this line runs as written: placeholder="e.g. news.ycombinator.com". It happens in order, after the line above it and before the line below it.

 106 |           aria-label="Custom domain"
     | Inside AddWebsiteSheet, this line runs as written: aria-label="Custom domain". It happens in order, after the line above it and before the line below it.

 107 |           aria-invalid={!!customError}
     | This ends AddWebsiteSheet (opened on line 5).

 108 |         />
     | This closes a box of instructions that opened above.

 109 |         <button type="button" className="btn btn-primary btn-sm" onClick={addCustom} disabled={!customValue.trim()}>
     | This draws one piece of the page while AddWebsiteSheet is showing.

 110 |           Add
     | Inside AddWebsiteSheet, this line runs as written: Add. It happens in order, after the line above it and before the line below it.

 111 |         </button>
     | This ends a drawing that AddWebsiteSheet started just above.

 112 |       </div>
     | This ends a drawing that AddWebsiteSheet started just above.

 113 |       {customError && <p className="text-xs" style={{ color: "var(--red)", marginTop: 6 }}>{customError}</p>}
     | This ends AddWebsiteSheet (opened on line 5).

 114 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 115 |       <div className="fs-sheet-footer">
     | This draws one piece of the page while AddWebsiteSheet is showing.

 116 |         <button type="button" className="btn btn-secondary w-full" onClick={handleClose}>
     | This draws one piece of the page while AddWebsiteSheet is showing.

 117 |           Done
     | Inside AddWebsiteSheet, this line runs as written: Done. It happens in order, after the line above it and before the line below it.

 118 |         </button>
     | This ends a drawing that AddWebsiteSheet started just above.

 119 |       </div>
     | This ends a drawing that AddWebsiteSheet started just above.

 120 |     </Sheet>
     | This ends a drawing that AddWebsiteSheet started just above.

 121 |   );
     | This closes a box of instructions that opened above.

 122 | }
     | This ends AddWebsiteSheet (opened on line 5).

