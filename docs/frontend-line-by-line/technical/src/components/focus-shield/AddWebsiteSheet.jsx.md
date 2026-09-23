# `src/components/focus-shield/AddWebsiteSheet.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import React, { useMemo, useState } from "react";
     | Import for the sheet for adding a popular or custom site: `import React, { useMemo, useState } from "react";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   2 | import Sheet from "./Sheet";
     | Import for the sheet for adding a popular or custom site: `import Sheet from "./Sheet";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   3 | import { POPULAR_SITES, normalizeDomain, isValidDomain } from "../../utils/focusShield";
     | Import for the sheet for adding a popular or custom site: `import { POPULAR_SITES, normalizeDomain, isValidDomain } from "../../utils/focusShield";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   4 | 
     | Blank line in `src/components/focus-shield/AddWebsiteSheet.jsx` (the sheet for adding a popular or custom site), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   5 | export default function AddWebsiteSheet({ open, onClose, existingValues, onAdd, target }) {
     | Defines `AddWebsiteSheet` in the sheet for adding a popular or custom site. Searchable popular chips plus a custom domain field. onAdd receives an array of one entry.

   6 |   const [search, setSearch] = useState("");
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): React state `search, setSearch`. The value survives re-renders. Calling the setter re-renders this component. `const [search, setSearch] = useState("");`

   7 |   const [customValue, setCustomValue] = useState("");
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): React state `customValue, setCustomValue`. The value survives re-renders. Calling the setter re-renders this component. `const [customValue, setCustomValue] = useState("");`

   8 |   const [customError, setCustomError] = useState("");
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): React state `customError, setCustomError`. The value survives re-renders. Calling the setter re-renders this component. `const [customError, setCustomError] = useState("");`

   9 | 
     | Blank line in `src/components/focus-shield/AddWebsiteSheet.jsx` (the sheet for adding a popular or custom site), inside AddWebsiteSheet. The parser skips it. It separates the previous statement from the next so the function is readable.

  10 |   const filtered = useMemo(() => {
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): A memoized value `filtered`, recomputed only when its dependency array changes. `const filtered = useMemo(() => {`

  11 |     const q = search.trim().toLowerCase();
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): `q` is assigned `search.trim().toLowerCase();`. Later lines in this function read that name.

  12 |     if (!q) return POPULAR_SITES;
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): branch `if (!q) return POPULAR_SITES;`. Only one side runs.

  13 |     return POPULAR_SITES.filter(
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): return `return POPULAR_SITES.filter(`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  14 |       (s) => s.label.toLowerCase().includes(q) || s.domain.includes(q) || s.category.toLowerCase().includes(q)
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): statement `(s) => s.label.toLowerCase().includes(q) || s.domain.includes(q) || s.category.toLowerCase().includes(q)`. It runs when AddWebsiteSheet runs, in order, before the next line of the same function.

  15 |     );
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): statement `);`. It runs when AddWebsiteSheet runs, in order, before the next line of the same function.

  16 |   }, [search]);
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): `}, [search]);` closes const filtered = useMemo(() => { (opened on line 10). Names declared inside that block end here.

  17 | 
     | Blank line in `src/components/focus-shield/AddWebsiteSheet.jsx` (the sheet for adding a popular or custom site), inside AddWebsiteSheet. The parser skips it. It separates the previous statement from the next so the function is readable.

  18 |   function handleClose() {
     | Defines `handleClose` in the sheet for adding a popular or custom site. Clears the sheet's fields, then calls the parent's onClose.

  19 |     setSearch("");
     | In `handleClose` (src/components/focus-shield/AddWebsiteSheet.jsx): statement `setSearch("");`. It runs when handleClose runs, in order, before the next line of the same function.

  20 |     setCustomValue("");
     | In `handleClose` (src/components/focus-shield/AddWebsiteSheet.jsx): statement `setCustomValue("");`. It runs when handleClose runs, in order, before the next line of the same function.

  21 |     setCustomError("");
     | In `handleClose` (src/components/focus-shield/AddWebsiteSheet.jsx): statement `setCustomError("");`. It runs when handleClose runs, in order, before the next line of the same function.

  22 |     onClose();
     | In `handleClose` (src/components/focus-shield/AddWebsiteSheet.jsx): statement `onClose();`. It runs when handleClose runs, in order, before the next line of the same function.

  23 |   }
     | In `handleClose` (src/components/focus-shield/AddWebsiteSheet.jsx): `}` closes handleClose (opened on line 18). Names declared inside that block end here.

  24 | 
     | Blank line in `src/components/focus-shield/AddWebsiteSheet.jsx` (the sheet for adding a popular or custom site), inside AddWebsiteSheet. The parser skips it. It separates the previous statement from the next so the function is readable.

  25 |   function addPopular(site) {
     | Defines `addPopular` in the sheet for adding a popular or custom site. Adds the chip's domain unless existingValues already has it.

  26 |     if (existingValues.has(site.domain)) return;
     | In `addPopular` (src/components/focus-shield/AddWebsiteSheet.jsx): branch `if (existingValues.has(site.domain)) return;`. Only one side runs.

  27 |     onAdd([{ value: site.domain, label: site.label, enabled: true }]);
     | In `addPopular` (src/components/focus-shield/AddWebsiteSheet.jsx): `onAdd([{ value: site.domain, label: site.label, enabled: true }]);` closes addPopular (opened on line 25). Names declared inside that block end here.

  28 |   }
     | In `addPopular` (src/components/focus-shield/AddWebsiteSheet.jsx): `}` closes addPopular (opened on line 25). Names declared inside that block end here.

  29 | 
     | Blank line in `src/components/focus-shield/AddWebsiteSheet.jsx` (the sheet for adding a popular or custom site), inside AddWebsiteSheet. The parser skips it. It separates the previous statement from the next so the function is readable.

  30 |   function addCustom() {
     | Defines `addCustom` in the sheet for adding a popular or custom site. Normalizes and validates. Sets an error string instead of adding when the domain is bad or duplicate.

  31 |     const domain = normalizeDomain(customValue);
     | In `addCustom` (src/components/focus-shield/AddWebsiteSheet.jsx): `domain` is assigned `normalizeDomain(customValue);`. Later lines in this function read that name.

  32 |     if (!isValidDomain(domain)) {
     | In `addCustom` (src/components/focus-shield/AddWebsiteSheet.jsx): branch `if (!isValidDomain(domain)) {`. Only one side runs.

  33 |       setCustomError("Enter a valid domain, e.g. example.com");
     | In `addCustom` (src/components/focus-shield/AddWebsiteSheet.jsx): statement `setCustomError("Enter a valid domain, e.g. example.com");`. It runs when addCustom runs, in order, before the next line of the same function.

  34 |       return;
     | In `addCustom` (src/components/focus-shield/AddWebsiteSheet.jsx): return `return;`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  35 |     }
     | In `addCustom` (src/components/focus-shield/AddWebsiteSheet.jsx): `}` closes if (!isValidDomain(domain)) { (opened on line 32). Names declared inside that block end here.

  36 |     if (existingValues.has(domain)) {
     | In `addCustom` (src/components/focus-shield/AddWebsiteSheet.jsx): branch `if (existingValues.has(domain)) {`. Only one side runs.

  37 |       setCustomError("That site is already on this list");
     | In `addCustom` (src/components/focus-shield/AddWebsiteSheet.jsx): statement `setCustomError("That site is already on this list");`. It runs when addCustom runs, in order, before the next line of the same function.

  38 |       return;
     | In `addCustom` (src/components/focus-shield/AddWebsiteSheet.jsx): return `return;`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  39 |     }
     | In `addCustom` (src/components/focus-shield/AddWebsiteSheet.jsx): `}` closes if (existingValues.has(domain)) { (opened on line 36). Names declared inside that block end here.

  40 |     onAdd([{ value: domain, label: "", enabled: true }]);
     | In `addCustom` (src/components/focus-shield/AddWebsiteSheet.jsx): `onAdd([{ value: domain, label: "", enabled: true }]);` closes addCustom (opened on line 30). Names declared inside that block end here.

  41 |     setCustomValue("");
     | In `addCustom` (src/components/focus-shield/AddWebsiteSheet.jsx): statement `setCustomValue("");`. It runs when addCustom runs, in order, before the next line of the same function.

  42 |     setCustomError("");
     | In `addCustom` (src/components/focus-shield/AddWebsiteSheet.jsx): statement `setCustomError("");`. It runs when addCustom runs, in order, before the next line of the same function.

  43 |   }
     | In `addCustom` (src/components/focus-shield/AddWebsiteSheet.jsx): `}` closes addCustom (opened on line 30). Names declared inside that block end here.

  44 | 
     | Blank line in `src/components/focus-shield/AddWebsiteSheet.jsx` (the sheet for adding a popular or custom site), inside AddWebsiteSheet. The parser skips it. It separates the previous statement from the next so the function is readable.

  45 |   function handleCustomKey(e) {
     | Defines `handleCustomKey` in the sheet for adding a popular or custom site. Enter in the custom field calls addCustom.

  46 |     if (e.key === "Enter") {
     | In `handleCustomKey` (src/components/focus-shield/AddWebsiteSheet.jsx): branch `if (e.key === "Enter") {`. Only one side runs.

  47 |       e.preventDefault();
     | In `handleCustomKey` (src/components/focus-shield/AddWebsiteSheet.jsx): statement `e.preventDefault();`. It runs when handleCustomKey runs, in order, before the next line of the same function.

  48 |       addCustom();
     | In `handleCustomKey` (src/components/focus-shield/AddWebsiteSheet.jsx): statement `addCustom();`. It runs when handleCustomKey runs, in order, before the next line of the same function.

  49 |     }
     | In `handleCustomKey` (src/components/focus-shield/AddWebsiteSheet.jsx): `}` closes if (e.key === "Enter") { (opened on line 46). Names declared inside that block end here.

  50 |   }
     | In `handleCustomKey` (src/components/focus-shield/AddWebsiteSheet.jsx): `}` closes handleCustomKey (opened on line 45). Names declared inside that block end here.

  51 | 
     | Blank line in `src/components/focus-shield/AddWebsiteSheet.jsx` (the sheet for adding a popular or custom site), inside AddWebsiteSheet. The parser skips it. It separates the previous statement from the next so the function is readable.

  52 |   return (
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  53 |     <Sheet
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): Opens it. Shared dialog frame. Source: `<Sheet`

  54 |       open={open}
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): `open={open}` closes AddWebsiteSheet (opened on line 5). Names declared inside that block end here.

  55 |       onClose={handleClose}
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): `onClose={handleClose}` closes AddWebsiteSheet (opened on line 5). Names declared inside that block end here.

  56 |       title={target === "whitelist" ? "Add to whitelist" : "Add website"}
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): `title={target === "whitelist" ? "Add to whitelist" : "Add website"}` closes AddWebsiteSheet (opened on line 5). Names declared inside that block end here.

  57 |       labelledBy="fs-add-sheet-title"
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): statement `labelledBy="fs-add-sheet-title"`. It runs when AddWebsiteSheet runs, in order, before the next line of the same function.

  58 |     >
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): statement `>`. It runs when AddWebsiteSheet runs, in order, before the next line of the same function.

  59 |       <div className="profile-form-field" style={{ marginBottom: 14 }}>
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="profile-form-field" style={{ marginBottom: 14 }}>`

  60 |         <label className="profile-form-label" htmlFor="fs-add-search">Search</label>
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): Opens it. The caption for an input. Source: `<label className="profile-form-label" htmlFor="fs-add-search">Search</label>`

  61 |         <input
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): Opens it. A text or date field. If value and onChange are set, React owns what it shows. Source: `<input`

  62 |           id="fs-add-search"
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): statement `id="fs-add-search"`. It runs when AddWebsiteSheet runs, in order, before the next line of the same function.

  63 |           className="profile-form-input"
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): statement `className="profile-form-input"`. It runs when AddWebsiteSheet runs, in order, before the next line of the same function.

  64 |           type="search"
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): statement `type="search"`. It runs when AddWebsiteSheet runs, in order, before the next line of the same function.

  65 |           value={search}
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): `value={search}` closes AddWebsiteSheet (opened on line 5). Names declared inside that block end here.

  66 |           onChange={(e) => setSearch(e.target.value)}
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): event prop `onChange={(e) => setSearch(e.target.value)}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

  67 |           placeholder="Search popular sites or categories…"
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): statement `placeholder="Search popular sites or categories…"`. It runs when AddWebsiteSheet runs, in order, before the next line of the same function.

  68 |         />
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): statement `/>`. It runs when AddWebsiteSheet runs, in order, before the next line of the same function.

  69 |       </div>
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  70 | 
     | Blank line in `src/components/focus-shield/AddWebsiteSheet.jsx` (the sheet for adding a popular or custom site), inside AddWebsiteSheet. The parser skips it. It separates the previous statement from the next so the function is readable.

  71 |       <p className="profile-form-label" style={{ marginBottom: 8 }}>Popular websites</p>
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): Opens it. A paragraph. Source: `<p className="profile-form-label" style={{ marginBottom: 8 }}>Popular websites</p>`

  72 |       <div className="fs-popular-grid">
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="fs-popular-grid">`

  73 |         {filtered.map((site) => {
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): iteration `{filtered.map((site) => {`.

  74 |           const added = existingValues.has(site.domain);
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): `added` is assigned `existingValues.has(site.domain);`. Later lines in this function read that name.

  75 |           return (
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  76 |             <button
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button`

  77 |               key={site.id}
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): `key={site.id}` closes {filtered.map((site) => { (opened on line 73). Names declared inside that block end here.

  78 |               type="button"
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): statement `type="button"`. It runs when AddWebsiteSheet runs, in order, before the next line of the same function.

  79 |               className={`fs-popular-chip${added ? " fs-popular-chip--added" : ""}`}
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): `className={`fs-popular-chip${added ? " fs-popular-chip--added" : ""}`}` closes {filtered.map((site) => { (opened on line 73). Names declared inside that block end here.

  80 |               onClick={() => addPopular(site)}
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): event prop `onClick={() => addPopular(site)}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

  81 |               disabled={added}
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): `disabled={added}` closes {filtered.map((site) => { (opened on line 73). Names declared inside that block end here.

  82 |               aria-pressed={added}
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): `aria-pressed={added}` closes {filtered.map((site) => { (opened on line 73). Names declared inside that block end here.

  83 |             >
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): statement `>`. It runs when AddWebsiteSheet runs, in order, before the next line of the same function.

  84 |               <span className="fs-popular-emoji" aria-hidden="true">{site.emoji}</span>
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): Opens it. An inline box. Source: `<span className="fs-popular-emoji" aria-hidden="true">{site.emoji}</span>`

  85 |               <span className="fs-popular-label">{site.label}</span>
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): Opens it. An inline box. Source: `<span className="fs-popular-label">{site.label}</span>`

  86 |               <span className="fs-popular-status">{added ? "✓ Added" : "+ Add"}</span>
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): Opens it. An inline box. Source: `<span className="fs-popular-status">{added ? "✓ Added" : "+ Add"}</span>`

  87 |             </button>
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

  88 |           );
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): statement `);`. It runs when AddWebsiteSheet runs, in order, before the next line of the same function.

  89 |         })}
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): `})}` closes {filtered.map((site) => { (opened on line 73). Names declared inside that block end here.

  90 |         {filtered.length === 0 && (
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): statement `{filtered.length === 0 && (`. It runs when AddWebsiteSheet runs, in order, before the next line of the same function.

  91 |           <p className="text-sm text-muted">No matches — try adding it as a custom domain below.</p>
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): Opens it. A paragraph. Source: `<p className="text-sm text-muted">No matches — try adding it as a custom domain below.</p>`

  92 |         )}
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): `)}` closes AddWebsiteSheet (opened on line 5). Names declared inside that block end here.

  93 |       </div>
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  94 | 
     | Blank line in `src/components/focus-shield/AddWebsiteSheet.jsx` (the sheet for adding a popular or custom site), inside AddWebsiteSheet. The parser skips it. It separates the previous statement from the next so the function is readable.

  95 |       <div className="fs-sheet-divider" />
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="fs-sheet-divider" />`

  96 | 
     | Blank line in `src/components/focus-shield/AddWebsiteSheet.jsx` (the sheet for adding a popular or custom site), inside AddWebsiteSheet. The parser skips it. It separates the previous statement from the next so the function is readable.

  97 |       <p className="profile-form-label" style={{ marginBottom: 8 }}>Custom domain</p>
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): Opens it. A paragraph. Source: `<p className="profile-form-label" style={{ marginBottom: 8 }}>Custom domain</p>`

  98 |       <div className="fs-custom-domain-row">
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="fs-custom-domain-row">`

  99 |         <input
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): Opens it. A text or date field. If value and onChange are set, React owns what it shows. Source: `<input`

 100 |           className="profile-form-input"
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): statement `className="profile-form-input"`. It runs when AddWebsiteSheet runs, in order, before the next line of the same function.

 101 |           type="text"
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): statement `type="text"`. It runs when AddWebsiteSheet runs, in order, before the next line of the same function.

 102 |           value={customValue}
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): `value={customValue}` closes AddWebsiteSheet (opened on line 5). Names declared inside that block end here.

 103 |           onChange={(e) => { setCustomValue(e.target.value); setCustomError(""); }}
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): event prop `onChange={(e) => { setCustomValue(e.target.value); setCustomError(""); }}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 104 |           onKeyDown={handleCustomKey}
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): event prop `onKeyDown={handleCustomKey}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 105 |           placeholder="e.g. news.ycombinator.com"
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): statement `placeholder="e.g. news.ycombinator.com"`. It runs when AddWebsiteSheet runs, in order, before the next line of the same function.

 106 |           aria-label="Custom domain"
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): statement `aria-label="Custom domain"`. It runs when AddWebsiteSheet runs, in order, before the next line of the same function.

 107 |           aria-invalid={!!customError}
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): `aria-invalid={!!customError}` closes AddWebsiteSheet (opened on line 5). Names declared inside that block end here.

 108 |         />
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): statement `/>`. It runs when AddWebsiteSheet runs, in order, before the next line of the same function.

 109 |         <button type="button" className="btn btn-primary btn-sm" onClick={addCustom} disabled={!customValue.trim()}>
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button type="button" className="btn btn-primary btn-sm" onClick={addCustom} disabled={!customValue.trim()}>`

 110 |           Add
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): statement `Add`. It runs when AddWebsiteSheet runs, in order, before the next line of the same function.

 111 |         </button>
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

 112 |       </div>
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 113 |       {customError && <p className="text-xs" style={{ color: "var(--red)", marginTop: 6 }}>{customError}</p>}
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): `{customError && <p className="text-xs" style={{ color: "var(--red)", marginTop: 6 }}>{customError}</p>}` closes AddWebsiteSheet (opened on line 5). Names declared inside that block end here.

 114 | 
     | Blank line in `src/components/focus-shield/AddWebsiteSheet.jsx` (the sheet for adding a popular or custom site), inside AddWebsiteSheet. The parser skips it. It separates the previous statement from the next so the function is readable.

 115 |       <div className="fs-sheet-footer">
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="fs-sheet-footer">`

 116 |         <button type="button" className="btn btn-secondary w-full" onClick={handleClose}>
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button type="button" className="btn btn-secondary w-full" onClick={handleClose}>`

 117 |           Done
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): statement `Done`. It runs when AddWebsiteSheet runs, in order, before the next line of the same function.

 118 |         </button>
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

 119 |       </div>
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 120 |     </Sheet>
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): Closes it. Shared dialog frame. Source: `</Sheet>`

 121 |   );
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): statement `);`. It runs when AddWebsiteSheet runs, in order, before the next line of the same function.

 122 | }
     | In `AddWebsiteSheet` (src/components/focus-shield/AddWebsiteSheet.jsx): `}` closes AddWebsiteSheet (opened on line 5). Names declared inside that block end here.

