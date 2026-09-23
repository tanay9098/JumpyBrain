# `src/components/focus-shield/FocusShieldPage.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import React, { useEffect, useRef, useState } from "react";
     | Import for the page that edits and autosaves blocking rules: `import React, { useEffect, useRef, useState } from "react";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   2 | import api from "../../services/api";
     | Import for the page that edits and autosaves blocking rules: `import api from "../../services/api";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   3 | import { useBlockingStore } from "../../stores/blockingStore";
     | Import for the page that edits and autosaves blocking rules: `import { useBlockingStore } from "../../stores/blockingStore";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   4 | import Toggle from "./Toggle";
     | Import for the page that edits and autosaves blocking rules: `import Toggle from "./Toggle";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   5 | import PauseControl from "./PauseControl";
     | Import for the page that edits and autosaves blocking rules: `import PauseControl from "./PauseControl";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   6 | import PresetPicker from "./PresetPicker";
     | Import for the page that edits and autosaves blocking rules: `import PresetPicker from "./PresetPicker";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   7 | import WebsiteListManager from "./WebsiteListManager";
     | Import for the page that edits and autosaves blocking rules: `import WebsiteListManager from "./WebsiteListManager";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   8 | import { getShieldStatus } from "../../utils/focusShield";
     | Import for the page that edits and autosaves blocking rules: `import { getShieldStatus } from "../../utils/focusShield";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   9 | 
     | Blank line in `src/components/focus-shield/FocusShieldPage.jsx` (the page that edits and autosaves blocking rules), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  10 | const DAY_LABELS = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
     | In `the top of the file` (src/components/focus-shield/FocusShieldPage.jsx): `DAY_LABELS`: Sunday-first labels. Index matches Date.getDay and the schedule.days numbers. The code is `const DAY_LABELS = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];`.

  11 | 
     | Blank line in `src/components/focus-shield/FocusShieldPage.jsx` (the page that edits and autosaves blocking rules), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  12 | function AppEntryList({ items, onRemove, placeholder }) {
     | Defines `AppEntryList` in the page that edits and autosaves blocking rules. Renders blocked apps with a remove button.

  13 |   return (
     | In `AppEntryList` (src/components/focus-shield/FocusShieldPage.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  14 |     <div style={{ display: "flex", flexDirection: "column", gap: 6 }}>
     | In `AppEntryList` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A box that groups the elements inside it. Source: `<div style={{ display: "flex", flexDirection: "column", gap: 6 }}>`

  15 |       {items.length === 0 && (
     | In `AppEntryList` (src/components/focus-shield/FocusShieldPage.jsx): statement `{items.length === 0 && (`. It runs when AppEntryList runs, in order, before the next line of the same function.

  16 |         <p className="text-xs text-muted" style={{ margin: 0 }}>{placeholder}</p>
     | In `AppEntryList` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A paragraph. Source: `<p className="text-xs text-muted" style={{ margin: 0 }}>{placeholder}</p>`

  17 |       )}
     | In `AppEntryList` (src/components/focus-shield/FocusShieldPage.jsx): `)}` closes AppEntryList (opened on line 12). Names declared inside that block end here.

  18 |       {items.map((item, idx) => (
     | In `AppEntryList` (src/components/focus-shield/FocusShieldPage.jsx): iteration `{items.map((item, idx) => (`.

  19 |         <div key={item._id || idx} className="fs-app-row">
     | In `AppEntryList` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A box that groups the elements inside it. Source: `<div key={item._id || idx} className="fs-app-row">`

  20 |           <span className="fs-row-domain">
     | In `AppEntryList` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. An inline box. Source: `<span className="fs-row-domain">`

  21 |             {item.value}
     | In `AppEntryList` (src/components/focus-shield/FocusShieldPage.jsx): `{item.value}` closes AppEntryList (opened on line 12). Names declared inside that block end here.

  22 |             {item.label && <span className="fs-row-domain-sub"> {item.label}</span>}
     | In `AppEntryList` (src/components/focus-shield/FocusShieldPage.jsx): `{item.label && <span className="fs-row-domain-sub"> {item.label}</span>}` closes AppEntryList (opened on line 12). Names declared inside that block end here.

  23 |           </span>
     | In `AppEntryList` (src/components/focus-shield/FocusShieldPage.jsx): Closes it. An inline box. Source: `</span>`

  24 |           <button type="button" onClick={() => onRemove(idx)} className="fs-app-remove" aria-label={`Remove ${item.value}`}>
     | In `AppEntryList` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button type="button" onClick={() => onRemove(idx)} className="fs-app-remove" aria-label={`Remove ${item.value}`}>`

  25 |             ×
     | In `AppEntryList` (src/components/focus-shield/FocusShieldPage.jsx): statement `×`. It runs when AppEntryList runs, in order, before the next line of the same function.

  26 |           </button>
     | In `AppEntryList` (src/components/focus-shield/FocusShieldPage.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

  27 |         </div>
     | In `AppEntryList` (src/components/focus-shield/FocusShieldPage.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  28 |       ))}
     | In `AppEntryList` (src/components/focus-shield/FocusShieldPage.jsx): `))}` closes AppEntryList (opened on line 12). Names declared inside that block end here.

  29 |     </div>
     | In `AppEntryList` (src/components/focus-shield/FocusShieldPage.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  30 |   );
     | In `AppEntryList` (src/components/focus-shield/FocusShieldPage.jsx): statement `);`. It runs when AppEntryList runs, in order, before the next line of the same function.

  31 | }
     | In `AppEntryList` (src/components/focus-shield/FocusShieldPage.jsx): `}` closes AppEntryList (opened on line 12). Names declared inside that block end here.

  32 | 
     | Blank line in `src/components/focus-shield/FocusShieldPage.jsx` (the page that edits and autosaves blocking rules), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  33 | function AppAddRow({ onAdd }) {
     | Defines `AppAddRow` in the page that edits and autosaves blocking rules. Two inputs: display name and optional package name.

  34 |   const [value, setValue] = useState("");
     | In `AppAddRow` (src/components/focus-shield/FocusShieldPage.jsx): React state `value, setValue`. The value survives re-renders. Calling the setter re-renders this component. `const [value, setValue] = useState("");`

  35 |   const [label, setLabel] = useState("");
     | In `AppAddRow` (src/components/focus-shield/FocusShieldPage.jsx): React state `label, setLabel`. The value survives re-renders. Calling the setter re-renders this component. `const [label, setLabel] = useState("");`

  36 | 
     | Blank line in `src/components/focus-shield/FocusShieldPage.jsx` (the page that edits and autosaves blocking rules), inside AppAddRow. The parser skips it. It separates the previous statement from the next so the function is readable.

  37 |   function handleAdd() {
     | Defines `handleAdd` in the page that edits and autosaves blocking rules. Trims the name and calls onAdd, then clears the inputs.

  38 |     const trimmed = value.trim();
     | In `handleAdd` (src/components/focus-shield/FocusShieldPage.jsx): `trimmed` is assigned `value.trim();`. Later lines in this function read that name.

  39 |     if (!trimmed) return;
     | In `handleAdd` (src/components/focus-shield/FocusShieldPage.jsx): branch `if (!trimmed) return;`. Only one side runs.

  40 |     onAdd({ value: trimmed, label: label.trim(), enabled: true });
     | In `handleAdd` (src/components/focus-shield/FocusShieldPage.jsx): `onAdd({ value: trimmed, label: label.trim(), enabled: true });` closes handleAdd (opened on line 37). Names declared inside that block end here.

  41 |     setValue("");
     | In `handleAdd` (src/components/focus-shield/FocusShieldPage.jsx): statement `setValue("");`. It runs when handleAdd runs, in order, before the next line of the same function.

  42 |     setLabel("");
     | In `handleAdd` (src/components/focus-shield/FocusShieldPage.jsx): statement `setLabel("");`. It runs when handleAdd runs, in order, before the next line of the same function.

  43 |   }
     | In `handleAdd` (src/components/focus-shield/FocusShieldPage.jsx): `}` closes handleAdd (opened on line 37). Names declared inside that block end here.

  44 | 
     | Blank line in `src/components/focus-shield/FocusShieldPage.jsx` (the page that edits and autosaves blocking rules), inside AppAddRow. The parser skips it. It separates the previous statement from the next so the function is readable.

  45 |   return (
     | In `AppAddRow` (src/components/focus-shield/FocusShieldPage.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  46 |     <div style={{ display: "flex", gap: 8, flexWrap: "wrap", marginTop: 10 }}>
     | In `AppAddRow` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A box that groups the elements inside it. Source: `<div style={{ display: "flex", gap: 8, flexWrap: "wrap", marginTop: 10 }}>`

  47 |       <input
     | In `AppAddRow` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A text or date field. If value and onChange are set, React owns what it shows. Source: `<input`

  48 |         className="profile-form-input"
     | In `AppAddRow` (src/components/focus-shield/FocusShieldPage.jsx): statement `className="profile-form-input"`. It runs when AppAddRow runs, in order, before the next line of the same function.

  49 |         style={{ flex: "2 1 160px", minWidth: 0 }}
     | In `AppAddRow` (src/components/focus-shield/FocusShieldPage.jsx): `style={{ flex: "2 1 160px", minWidth: 0 }}` closes AppAddRow (opened on line 33). Names declared inside that block end here.

  50 |         value={value}
     | In `AppAddRow` (src/components/focus-shield/FocusShieldPage.jsx): `value={value}` closes AppAddRow (opened on line 33). Names declared inside that block end here.

  51 |         onChange={(e) => setValue(e.target.value)}
     | In `AppAddRow` (src/components/focus-shield/FocusShieldPage.jsx): event prop `onChange={(e) => setValue(e.target.value)}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

  52 |         onKeyDown={(e) => e.key === "Enter" && (e.preventDefault(), handleAdd())}
     | In `AppAddRow` (src/components/focus-shield/FocusShieldPage.jsx): event prop `onKeyDown={(e) => e.key === "Enter" && (e.preventDefault(), handleAdd())}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

  53 |         placeholder="e.g. Instagram"
     | In `AppAddRow` (src/components/focus-shield/FocusShieldPage.jsx): statement `placeholder="e.g. Instagram"`. It runs when AppAddRow runs, in order, before the next line of the same function.

  54 |         maxLength={100}
     | In `AppAddRow` (src/components/focus-shield/FocusShieldPage.jsx): `maxLength={100}` closes AppAddRow (opened on line 33). Names declared inside that block end here.

  55 |       />
     | In `AppAddRow` (src/components/focus-shield/FocusShieldPage.jsx): statement `/>`. It runs when AppAddRow runs, in order, before the next line of the same function.

  56 |       <input
     | In `AppAddRow` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A text or date field. If value and onChange are set, React owns what it shows. Source: `<input`

  57 |         className="profile-form-input"
     | In `AppAddRow` (src/components/focus-shield/FocusShieldPage.jsx): statement `className="profile-form-input"`. It runs when AppAddRow runs, in order, before the next line of the same function.

  58 |         style={{ flex: "1 1 100px", minWidth: 0 }}
     | In `AppAddRow` (src/components/focus-shield/FocusShieldPage.jsx): `style={{ flex: "1 1 100px", minWidth: 0 }}` closes AppAddRow (opened on line 33). Names declared inside that block end here.

  59 |         value={label}
     | In `AppAddRow` (src/components/focus-shield/FocusShieldPage.jsx): `value={label}` closes AppAddRow (opened on line 33). Names declared inside that block end here.

  60 |         onChange={(e) => setLabel(e.target.value)}
     | In `AppAddRow` (src/components/focus-shield/FocusShieldPage.jsx): event prop `onChange={(e) => setLabel(e.target.value)}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

  61 |         onKeyDown={(e) => e.key === "Enter" && (e.preventDefault(), handleAdd())}
     | In `AppAddRow` (src/components/focus-shield/FocusShieldPage.jsx): event prop `onKeyDown={(e) => e.key === "Enter" && (e.preventDefault(), handleAdd())}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

  62 |         placeholder="Package name (optional)"
     | In `AppAddRow` (src/components/focus-shield/FocusShieldPage.jsx): statement `placeholder="Package name (optional)"`. It runs when AppAddRow runs, in order, before the next line of the same function.

  63 |         maxLength={100}
     | In `AppAddRow` (src/components/focus-shield/FocusShieldPage.jsx): `maxLength={100}` closes AppAddRow (opened on line 33). Names declared inside that block end here.

  64 |       />
     | In `AppAddRow` (src/components/focus-shield/FocusShieldPage.jsx): statement `/>`. It runs when AppAddRow runs, in order, before the next line of the same function.

  65 |       <button type="button" className="profile-save-btn" style={{ flexShrink: 0, padding: "0 16px" }} onClick={handleAdd} disabled={!value.trim()}>
     | In `AppAddRow` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button type="button" className="profile-save-btn" style={{ flexShrink: 0, padding: "0 16px" }} onClick={handleAdd} disabled={!value.trim()}>`

  66 |         Add
     | In `AppAddRow` (src/components/focus-shield/FocusShieldPage.jsx): statement `Add`. It runs when AppAddRow runs, in order, before the next line of the same function.

  67 |       </button>
     | In `AppAddRow` (src/components/focus-shield/FocusShieldPage.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

  68 |     </div>
     | In `AppAddRow` (src/components/focus-shield/FocusShieldPage.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  69 |   );
     | In `AppAddRow` (src/components/focus-shield/FocusShieldPage.jsx): statement `);`. It runs when AppAddRow runs, in order, before the next line of the same function.

  70 | }
     | In `AppAddRow` (src/components/focus-shield/FocusShieldPage.jsx): `}` closes AppAddRow (opened on line 33). Names declared inside that block end here.

  71 | 
     | Blank line in `src/components/focus-shield/FocusShieldPage.jsx` (the page that edits and autosaves blocking rules), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  72 | export default function FocusShieldPage() {
     | Defines `FocusShieldPage` in the page that edits and autosaves blocking rules. Loads GET /blocking into local state and the Zustand store, then PUTs local 600ms after each change.

  73 |   const { loading, setRules, setLoading } = useBlockingStore();
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): `loading`: True until UserProvider finishes the first localStorage read. ProtectedRoute renders nothing during that moment so Auth does not flash. The code is `const { loading, setRules, setLoading } = useBlockingStore();`.

  74 |   const [local, setLocal] = useState(null);
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): `local`: The editable copy of blocking rules on the Focus Shield page. Every toggle writes here. The effect on local autosaves. The code is `const [local, setLocal] = useState(null);`.

  75 |   const [saveState, setSaveState] = useState("idle"); // idle | saving | saved | error
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): `saveState`: idle, saving, saved, or error. The Focus Shield page shows this next to the title. There is no Save button; local changes debounce into PUT /blocking. The code is `const [saveState, setSaveState] = useState("idle"); // idle | saving | saved | error`.

  76 |   const [statsSessions, setStatsSessions] = useState([]);
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): React state `statsSessions, setStatsSessions`. The value survives re-renders. Calling the setter re-renders this component. `const [statsSessions, setStatsSessions] = useState([]);`

  77 |   const fileInputRef = useRef(null);
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): A ref `fileInputRef`. `.current` survives re-renders and writing it does not re-render. `const fileInputRef = useRef(null);`

  78 |   const skipNextSave = useRef(true);
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): `skipNextSave`: Starts true so the first GET /blocking does not immediately PUT the same rules back. The code is `const skipNextSave = useRef(true);`.

  79 | 
     | Blank line in `src/components/focus-shield/FocusShieldPage.jsx` (the page that edits and autosaves blocking rules), inside FocusShieldPage. The parser skips it. It separates the previous statement from the next so the function is readable.

  80 |   useEffect(() => {
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): opens or continues an effect — `useEffect(() => {`. The effect body runs after paint, and its cleanup runs before the next effect and on unmount.

  81 |     setLoading(true);
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): statement `setLoading(true);`. It runs when FocusShieldPage runs, in order, before the next line of the same function.

  82 |     api.get("/blocking")
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): HTTP via the shared Axios instance — `api.get("/blocking")`. The request interceptor adds `Authorization: Bearer <accessToken>`. The response interceptor returns `res.data`, so the awaited value is the JSON body.

  83 |       .then((data) => {
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): statement `.then((data) => {`. It runs when FocusShieldPage runs, in order, before the next line of the same function.

  84 |         skipNextSave.current = true;
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): statement `skipNextSave.current = true;`. It runs when FocusShieldPage runs, in order, before the next line of the same function.

  85 |         setRules(data.rules);
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): statement `setRules(data.rules);`. It runs when FocusShieldPage runs, in order, before the next line of the same function.

  86 |         setLocal(data.rules);
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): statement `setLocal(data.rules);`. It runs when FocusShieldPage runs, in order, before the next line of the same function.

  87 |       })
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): `})` closes .then((data) => { (opened on line 83). Names declared inside that block end here.

  88 |       .catch(() => setSaveState("error"))
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): statement `.catch(() => setSaveState("error"))`. It runs when FocusShieldPage runs, in order, before the next line of the same function.

  89 |       .finally(() => setLoading(false));
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): statement `.finally(() => setLoading(false));`. It runs when FocusShieldPage runs, in order, before the next line of the same function.

  90 | 
     | Blank line in `src/components/focus-shield/FocusShieldPage.jsx` (the page that edits and autosaves blocking rules), inside FocusShieldPage. The parser skips it. It separates the previous statement from the next so the function is readable.

  91 |     api.get("/stats/weekly").then((d) => setStatsSessions(d?.sessions || [])).catch(() => {});
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): HTTP via the shared Axios instance — `api.get("/stats/weekly").then((d) => setStatsSessions(d?.sessions || [])).catch(() => {});`. The request interceptor adds `Authorization: Bearer <accessToken>`. The response interceptor returns `res.data`, so the awaited value is the JSON body.

  92 |   }, []);
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): `}, []);` closes effect in FocusShieldPage (opened on line 80). Names declared inside that block end here.

  93 | 
     | Blank line in `src/components/focus-shield/FocusShieldPage.jsx` (the page that edits and autosaves blocking rules), inside FocusShieldPage. The parser skips it. It separates the previous statement from the next so the function is readable.

  94 |   // Autosave — every mutation (toggle, add, delete, pause, preset, schedule edit) flows
     | Comment inside FocusShieldPage. Not executed. It documents the next code: Autosave — every mutation (toggle, add, delete, pause, preset, schedule edit) flows

  95 |   // through `local` and lands here debounced, so the page never needs an explicit Save button.
     | Comment inside FocusShieldPage. Not executed. It documents the next code: through `local` and lands here debounced, so the page never needs an explicit Save button.

  96 |   useEffect(() => {
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): opens or continues an effect — `useEffect(() => {`. The effect body runs after paint, and its cleanup runs before the next effect and on unmount.

  97 |     if (!local) return;
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): branch `if (!local) return;`. Only one side runs.

  98 |     if (skipNextSave.current) { skipNextSave.current = false; return; }
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): branch `if (skipNextSave.current) { skipNextSave.current = false; return; }`. Only one side runs.

  99 |     setSaveState("saving");
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): statement `setSaveState("saving");`. It runs when FocusShieldPage runs, in order, before the next line of the same function.

 100 |     const t = setTimeout(async () => {
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): `t` is assigned `setTimeout(async () => {`. Later lines in this function read that name.

 101 |       try {
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): error path `try {`.

 102 |         const data = await api.put("/blocking", local);
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): `data` is assigned `await api.put("/blocking", local);`. Later lines in this function read that name.

 103 |         setRules(data.rules);
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): statement `setRules(data.rules);`. It runs when FocusShieldPage runs, in order, before the next line of the same function.

 104 |         setSaveState("saved");
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): statement `setSaveState("saved");`. It runs when FocusShieldPage runs, in order, before the next line of the same function.

 105 |         setTimeout(() => setSaveState((s) => (s === "saved" ? "idle" : s)), 1800);
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): timer — `setTimeout(() => setSaveState((s) => (s === "saved" ? "idle" : s)), 1800);`. The callback runs later on the event loop, not now.

 106 |       } catch {
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): `} catch {` closes try { (opened on line 101). Names declared inside that block end here.

 107 |         setSaveState("error");
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): statement `setSaveState("error");`. It runs when FocusShieldPage runs, in order, before the next line of the same function.

 108 |       }
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): `}` closes } catch { (opened on line 106). Names declared inside that block end here.

 109 |     }, 600);
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): `}, 600);` closes const t = setTimeout(async () => { (opened on line 100). Names declared inside that block end here.

 110 |     return () => clearTimeout(t);
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): return `return () => clearTimeout(t);`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

 111 |   }, [local]);
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): `}, [local]);` closes effect in FocusShieldPage (opened on line 96). Names declared inside that block end here.

 112 | 
     | Blank line in `src/components/focus-shield/FocusShieldPage.jsx` (the page that edits and autosaves blocking rules), inside FocusShieldPage. The parser skips it. It separates the previous statement from the next so the function is readable.

 113 |   if (loading || !local) {
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): branch `if (loading || !local) {`. Only one side runs.

 114 |     return (
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

 115 |       <div className="profile-settings-page">
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="profile-settings-page">`

 116 |         <div className="profile-settings-container">
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="profile-settings-container">`

 117 |           <p className="text-sm text-muted">Loading Focus Shield…</p>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A paragraph. Source: `<p className="text-sm text-muted">Loading Focus Shield…</p>`

 118 |         </div>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 119 |       </div>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 120 |     );
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): statement `);`. It runs when FocusShieldPage runs, in order, before the next line of the same function.

 121 |   }
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): `}` closes if (loading || !local) { (opened on line 113). Names declared inside that block end here.

 122 | 
     | Blank line in `src/components/focus-shield/FocusShieldPage.jsx` (the page that edits and autosaves blocking rules), inside FocusShieldPage. The parser skips it. It separates the previous statement from the next so the function is readable.

 123 |   function update(patch) {
     | Defines `update` in the page that edits and autosaves blocking rules. Shallow-merges a patch into local, which schedules the autosave.

 124 |     setLocal((prev) => ({ ...prev, ...patch }));
     | In `update` (src/components/focus-shield/FocusShieldPage.jsx): statement `setLocal((prev) => ({ ...prev, ...patch }));`. It runs when update runs, in order, before the next line of the same function.

 125 |   }
     | In `update` (src/components/focus-shield/FocusShieldPage.jsx): `}` closes update (opened on line 123). Names declared inside that block end here.

 126 | 
     | Blank line in `src/components/focus-shield/FocusShieldPage.jsx` (the page that edits and autosaves blocking rules), inside FocusShieldPage. The parser skips it. It separates the previous statement from the next so the function is readable.

 127 |   function updateSchedule(patch) {
     | Defines `updateSchedule` in the page that edits and autosaves blocking rules. Same, but the patch is applied to local.schedule.

 128 |     setLocal((prev) => ({ ...prev, schedule: { ...prev.schedule, ...patch } }));
     | In `updateSchedule` (src/components/focus-shield/FocusShieldPage.jsx): statement `setLocal((prev) => ({ ...prev, schedule: { ...prev.schedule, ...patch } }));`. It runs when updateSchedule runs, in order, before the next line of the same function.

 129 |   }
     | In `updateSchedule` (src/components/focus-shield/FocusShieldPage.jsx): `}` closes updateSchedule (opened on line 127). Names declared inside that block end here.

 130 | 
     | Blank line in `src/components/focus-shield/FocusShieldPage.jsx` (the page that edits and autosaves blocking rules), inside FocusShieldPage. The parser skips it. It separates the previous statement from the next so the function is readable.

 131 |   function toggleDay(day) {
     | Defines `toggleDay` in the page that edits and autosaves blocking rules. Adds or removes a weekday number and keeps the array sorted.

 132 |     const days = local.schedule.days.includes(day)
     | In `toggleDay` (src/components/focus-shield/FocusShieldPage.jsx): `days` is assigned `local.schedule.days.includes(day)`. Later lines in this function read that name.

 133 |       ? local.schedule.days.filter((d) => d !== day)
     | In `toggleDay` (src/components/focus-shield/FocusShieldPage.jsx): iteration `? local.schedule.days.filter((d) => d !== day)`.

 134 |       : [...local.schedule.days, day].sort((a, b) => a - b);
     | In `toggleDay` (src/components/focus-shield/FocusShieldPage.jsx): statement `: [...local.schedule.days, day].sort((a, b) => a - b);`. It runs when toggleDay runs, in order, before the next line of the same function.

 135 |     updateSchedule({ days });
     | In `toggleDay` (src/components/focus-shield/FocusShieldPage.jsx): `updateSchedule({ days });` closes toggleDay (opened on line 131). Names declared inside that block end here.

 136 |   }
     | In `toggleDay` (src/components/focus-shield/FocusShieldPage.jsx): `}` closes toggleDay (opened on line 131). Names declared inside that block end here.

 137 | 
     | Blank line in `src/components/focus-shield/FocusShieldPage.jsx` (the page that edits and autosaves blocking rules), inside FocusShieldPage. The parser skips it. It separates the previous statement from the next so the function is readable.

 138 |   function addApp(entry) {
     | Defines `addApp` in the page that edits and autosaves blocking rules. Appends a blocked-app entry. Enforcement is native; this page only stores the name.

 139 |     update({ blockedApps: [...local.blockedApps, entry] });
     | In `addApp` (src/components/focus-shield/FocusShieldPage.jsx): `update({ blockedApps: [...local.blockedApps, entry] });` closes addApp (opened on line 138). Names declared inside that block end here.

 140 |   }
     | In `addApp` (src/components/focus-shield/FocusShieldPage.jsx): `}` closes addApp (opened on line 138). Names declared inside that block end here.

 141 | 
     | Blank line in `src/components/focus-shield/FocusShieldPage.jsx` (the page that edits and autosaves blocking rules), inside FocusShieldPage. The parser skips it. It separates the previous statement from the next so the function is readable.

 142 |   function removeApp(idx) {
     | Defines `removeApp` in the page that edits and autosaves blocking rules. Drops one blocked app by index.

 143 |     update({ blockedApps: local.blockedApps.filter((_, i) => i !== idx) });
     | In `removeApp` (src/components/focus-shield/FocusShieldPage.jsx): iteration `update({ blockedApps: local.blockedApps.filter((_, i) => i !== idx) });`.

 144 |   }
     | In `removeApp` (src/components/focus-shield/FocusShieldPage.jsx): `}` closes removeApp (opened on line 142). Names declared inside that block end here.

 145 | 
     | Blank line in `src/components/focus-shield/FocusShieldPage.jsx` (the page that edits and autosaves blocking rules), inside FocusShieldPage. The parser skips it. It separates the previous statement from the next so the function is readable.

 146 |   function handleExport() {
     | Defines `handleExport` in the page that edits and autosaves blocking rules. Downloads jumpybrain-focus-shield-rules.json containing blocked sites and the whitelist.

 147 |     const payload = {
     | In `handleExport` (src/components/focus-shield/FocusShieldPage.jsx): `payload` is assigned `{`. Later lines in this function read that name.

 148 |       exportedAt: new Date().toISOString(),
     | In `handleExport` (src/components/focus-shield/FocusShieldPage.jsx): statement `exportedAt: new Date().toISOString(),`. It runs when handleExport runs, in order, before the next line of the same function.

 149 |       blockedSites: local.blockedSites,
     | In `handleExport` (src/components/focus-shield/FocusShieldPage.jsx): statement `blockedSites: local.blockedSites,`. It runs when handleExport runs, in order, before the next line of the same function.

 150 |       whitelist: local.whitelist,
     | In `handleExport` (src/components/focus-shield/FocusShieldPage.jsx): statement `whitelist: local.whitelist,`. It runs when handleExport runs, in order, before the next line of the same function.

 151 |     };
     | In `handleExport` (src/components/focus-shield/FocusShieldPage.jsx): `};` closes const payload = { (opened on line 147). Names declared inside that block end here.

 152 |     const blob = new Blob([JSON.stringify(payload, null, 2)], { type: "application/json" });
     | In `handleExport` (src/components/focus-shield/FocusShieldPage.jsx): `blob` is assigned `new Blob([JSON.stringify(payload, null, 2)], { type: "application/json" });`. Later lines in this function read that name.

 153 |     const url = URL.createObjectURL(blob);
     | In `handleExport` (src/components/focus-shield/FocusShieldPage.jsx): `url` is assigned `URL.createObjectURL(blob);`. Later lines in this function read that name.

 154 |     const a = document.createElement("a");
     | In `handleExport` (src/components/focus-shield/FocusShieldPage.jsx): `a` is assigned `document.createElement("a");`. Later lines in this function read that name.

 155 |     a.href = url;
     | In `handleExport` (src/components/focus-shield/FocusShieldPage.jsx): statement `a.href = url;`. It runs when handleExport runs, in order, before the next line of the same function.

 156 |     a.download = "jumpybrain-focus-shield-rules.json";
     | In `handleExport` (src/components/focus-shield/FocusShieldPage.jsx): statement `a.download = "jumpybrain-focus-shield-rules.json";`. It runs when handleExport runs, in order, before the next line of the same function.

 157 |     a.click();
     | In `handleExport` (src/components/focus-shield/FocusShieldPage.jsx): statement `a.click();`. It runs when handleExport runs, in order, before the next line of the same function.

 158 |     URL.revokeObjectURL(url);
     | In `handleExport` (src/components/focus-shield/FocusShieldPage.jsx): statement `URL.revokeObjectURL(url);`. It runs when handleExport runs, in order, before the next line of the same function.

 159 |   }
     | In `handleExport` (src/components/focus-shield/FocusShieldPage.jsx): `}` closes handleExport (opened on line 146). Names declared inside that block end here.

 160 | 
     | Blank line in `src/components/focus-shield/FocusShieldPage.jsx` (the page that edits and autosaves blocking rules), inside FocusShieldPage. The parser skips it. It separates the previous statement from the next so the function is readable.

 161 |   function handleImportFile(e) {
     | Defines `handleImportFile` in the page that edits and autosaves blocking rules. Reads a JSON file and appends domains that are not already present.

 162 |     const file = e.target.files?.[0];
     | In `handleImportFile` (src/components/focus-shield/FocusShieldPage.jsx): `file` is assigned `e.target.files?.[0];`. Later lines in this function read that name.

 163 |     e.target.value = "";
     | In `handleImportFile` (src/components/focus-shield/FocusShieldPage.jsx): statement `e.target.value = "";`. It runs when handleImportFile runs, in order, before the next line of the same function.

 164 |     if (!file) return;
     | In `handleImportFile` (src/components/focus-shield/FocusShieldPage.jsx): branch `if (!file) return;`. Only one side runs.

 165 |     const reader = new FileReader();
     | In `handleImportFile` (src/components/focus-shield/FocusShieldPage.jsx): `reader` is assigned `new FileReader();`. Later lines in this function read that name.

 166 |     reader.onload = () => {
     | In `handleImportFile` (src/components/focus-shield/FocusShieldPage.jsx): statement `reader.onload = () => {`. It runs when handleImportFile runs, in order, before the next line of the same function.

 167 |       try {
     | In `handleImportFile` (src/components/focus-shield/FocusShieldPage.jsx): error path `try {`.

 168 |         const parsed = JSON.parse(String(reader.result));
     | In `handleImportFile` (src/components/focus-shield/FocusShieldPage.jsx): `parsed` is assigned `JSON.parse(String(reader.result));`. Later lines in this function read that name.

 169 |         const importedBlocked = Array.isArray(parsed.blockedSites) ? parsed.blockedSites : [];
     | In `handleImportFile` (src/components/focus-shield/FocusShieldPage.jsx): `importedBlocked` is assigned `Array.isArray(parsed.blockedSites) ? parsed.blockedSites : [];`. Later lines in this function read that name.

 170 |         const importedWhitelist = Array.isArray(parsed.whitelist) ? parsed.whitelist : [];
     | In `handleImportFile` (src/components/focus-shield/FocusShieldPage.jsx): `importedWhitelist` is assigned `Array.isArray(parsed.whitelist) ? parsed.whitelist : [];`. Later lines in this function read that name.

 171 |         const haveBlocked = new Set(local.blockedSites.map((s) => s.value));
     | In `handleImportFile` (src/components/focus-shield/FocusShieldPage.jsx): `haveBlocked` is assigned `new Set(local.blockedSites.map((s) => s.value));`. Later lines in this function read that name.

 172 |         const haveWhite = new Set(local.whitelist.map((s) => s.value));
     | In `handleImportFile` (src/components/focus-shield/FocusShieldPage.jsx): `haveWhite` is assigned `new Set(local.whitelist.map((s) => s.value));`. Later lines in this function read that name.

 173 |         const newBlocked = importedBlocked.filter((s) => s?.value && !haveBlocked.has(s.value));
     | In `handleImportFile` (src/components/focus-shield/FocusShieldPage.jsx): `newBlocked` is assigned `importedBlocked.filter((s) => s?.value && !haveBlocked.has(s.value));`. Later lines in this function read that name.

 174 |         const newWhite = importedWhitelist.filter((s) => s?.value && !haveWhite.has(s.value));
     | In `handleImportFile` (src/components/focus-shield/FocusShieldPage.jsx): `newWhite` is assigned `importedWhitelist.filter((s) => s?.value && !haveWhite.has(s.value));`. Later lines in this function read that name.

 175 |         update({
     | In `handleImportFile` (src/components/focus-shield/FocusShieldPage.jsx): statement `update({`. It runs when handleImportFile runs, in order, before the next line of the same function.

 176 |           blockedSites: [...local.blockedSites, ...newBlocked],
     | In `handleImportFile` (src/components/focus-shield/FocusShieldPage.jsx): statement `blockedSites: [...local.blockedSites, ...newBlocked],`. It runs when handleImportFile runs, in order, before the next line of the same function.

 177 |           whitelist: [...local.whitelist, ...newWhite],
     | In `handleImportFile` (src/components/focus-shield/FocusShieldPage.jsx): statement `whitelist: [...local.whitelist, ...newWhite],`. It runs when handleImportFile runs, in order, before the next line of the same function.

 178 |         });
     | In `handleImportFile` (src/components/focus-shield/FocusShieldPage.jsx): `});` closes update({ (opened on line 175). Names declared inside that block end here.

 179 |       } catch {
     | In `handleImportFile` (src/components/focus-shield/FocusShieldPage.jsx): `} catch {` closes try { (opened on line 167). Names declared inside that block end here.

 180 |         setSaveState("error");
     | In `handleImportFile` (src/components/focus-shield/FocusShieldPage.jsx): statement `setSaveState("error");`. It runs when handleImportFile runs, in order, before the next line of the same function.

 181 |       }
     | In `handleImportFile` (src/components/focus-shield/FocusShieldPage.jsx): `}` closes } catch { (opened on line 179). Names declared inside that block end here.

 182 |     };
     | In `handleImportFile` (src/components/focus-shield/FocusShieldPage.jsx): `};` closes reader.onload = () => { (opened on line 166). Names declared inside that block end here.

 183 |     reader.readAsText(file);
     | In `handleImportFile` (src/components/focus-shield/FocusShieldPage.jsx): statement `reader.readAsText(file);`. It runs when handleImportFile runs, in order, before the next line of the same function.

 184 |   }
     | In `handleImportFile` (src/components/focus-shield/FocusShieldPage.jsx): `}` closes handleImportFile (opened on line 161). Names declared inside that block end here.

 185 | 
     | Blank line in `src/components/focus-shield/FocusShieldPage.jsx` (the page that edits and autosaves blocking rules), inside FocusShieldPage. The parser skips it. It separates the previous statement from the next so the function is readable.

 186 |   const status = getShieldStatus(local);
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): `status` is assigned `getShieldStatus(local);`. Later lines in this function read that name.

 187 |   const todaySessions = statsSessions.filter((s) => {
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): `todaySessions` is assigned `statsSessions.filter((s) => {`. Later lines in this function read that name.

 188 |     const d = s.completedAt ? new Date(s.completedAt) : null;
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): `d` is assigned `s.completedAt ? new Date(s.completedAt) : null;`. Later lines in this function read that name.

 189 |     if (!d) return false;
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): branch `if (!d) return false;`. Only one side runs.

 190 |     const now = new Date();
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): `now` is assigned `new Date();`. Later lines in this function read that name.

 191 |     return d.toDateString() === now.toDateString();
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): return `return d.toDateString() === now.toDateString();`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

 192 |   });
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): `});` closes const todaySessions = statsSessions.filter((s) = (opened on line 187). Names declared inside that block end here.

 193 |   const distractionsToday = todaySessions.reduce((a, s) => a + (s.distractionCount || 0), 0);
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): `distractionsToday` is assigned `todaySessions.reduce((a, s) => a + (s.distractionCount || 0), 0);`. Later lines in this function read that name.

 194 |   const distractionsWeek = statsSessions.reduce((a, s) => a + (s.distractionCount || 0), 0);
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): `distractionsWeek` is assigned `statsSessions.reduce((a, s) => a + (s.distractionCount || 0), 0);`. Later lines in this function read that name.

 195 | 
     | Blank line in `src/components/focus-shield/FocusShieldPage.jsx` (the page that edits and autosaves blocking rules), inside FocusShieldPage. The parser skips it. It separates the previous statement from the next so the function is readable.

 196 |   return (
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

 197 |     <div className="profile-settings-page">
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="profile-settings-page">`

 198 |       <div className="profile-settings-container">
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="profile-settings-container">`

 199 |         <div className="profile-settings-header fs-page-header">
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="profile-settings-header fs-page-header">`

 200 |           <div>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A box that groups the elements inside it. Source: `<div>`

 201 |             <h1 className="profile-settings-title">🛡️ Focus Shield</h1>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. The page title. Source: `<h1 className="profile-settings-title">🛡️ Focus Shield</h1>`

 202 |             <p className="profile-settings-subtitle">
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A paragraph. Source: `<p className="profile-settings-subtitle">`

 203 |               Block distracting sites during focus sessions, always allow the ones you need.
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): statement `Block distracting sites during focus sessions, always allow the ones you need.`. It runs when FocusShieldPage runs, in order, before the next line of the same function.

 204 |             </p>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Closes it. A paragraph. Source: `</p>`

 205 |           </div>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 206 |           <span className="fs-save-indicator" aria-live="polite">
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. An inline box. Source: `<span className="fs-save-indicator" aria-live="polite">`

 207 |             {saveState === "saving" && "Saving…"}
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): `{saveState === "saving" && "Saving…"}` closes FocusShieldPage (opened on line 72). Names declared inside that block end here.

 208 |             {saveState === "saved" && "✓ Saved"}
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): `{saveState === "saved" && "✓ Saved"}` closes FocusShieldPage (opened on line 72). Names declared inside that block end here.

 209 |             {saveState === "error" && "⚠ Couldn't save"}
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): `{saveState === "error" && "⚠ Couldn't save"}` closes FocusShieldPage (opened on line 72). Names declared inside that block end here.

 210 |           </span>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Closes it. An inline box. Source: `</span>`

 211 |         </div>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 212 | 
     | Blank line in `src/components/focus-shield/FocusShieldPage.jsx` (the page that edits and autosaves blocking rules), inside FocusShieldPage. The parser skips it. It separates the previous statement from the next so the function is readable.

 213 |         {/* Master toggle + status + pause */}
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): `{/* Master toggle + status + pause */}` closes FocusShieldPage (opened on line 72). Names declared inside that block end here.

 214 |         <section className="profile-settings-card">
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A grouped block on the settings-style pages. Source: `<section className="profile-settings-card">`

 215 |           <div className="flex items-center justify-between gap-3">
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="flex items-center justify-between gap-3">`

 216 |             <div>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A box that groups the elements inside it. Source: `<div>`

 217 |               <div className="profile-settings-card-title" style={{ marginBottom: 2 }}>Focus Shield</div>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="profile-settings-card-title" style={{ marginBottom: 2 }}>Focus Shield</div>`

 218 |               <p className="text-xs text-muted" style={{ margin: 0 }}>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A paragraph. Source: `<p className="text-xs text-muted" style={{ margin: 0 }}>`

 219 |                 Enforcement runs in the Chrome extension (desktop) or native app (mobile).
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): statement `Enforcement runs in the Chrome extension (desktop) or native app (mobile).`. It runs when FocusShieldPage runs, in order, before the next line of the same function.

 220 |               </p>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Closes it. A paragraph. Source: `</p>`

 221 |             </div>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 222 |             <Toggle checked={local.isEnabled} onChange={(v) => update({ isEnabled: v })} label="Focus Shield enabled" />
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. On/off switch. The parent owns the boolean. Source: `<Toggle checked={local.isEnabled} onChange={(v) => update({ isEnabled: v })} label="Focus Shield enabled" />`

 223 |           </div>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 224 | 
     | Blank line in `src/components/focus-shield/FocusShieldPage.jsx` (the page that edits and autosaves blocking rules), inside FocusShieldPage. The parser skips it. It separates the previous statement from the next so the function is readable.

 225 |           <div className={`fs-status-pill fs-status-pill--${status.level}`} style={{ marginTop: 14 }}>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A box that groups the elements inside it. Source: `<div className={`fs-status-pill fs-status-pill--${status.level}`} style={{ marginTop: 14 }}>`

 226 |             <span className="fs-status-dot" />
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. An inline box. Source: `<span className="fs-status-dot" />`

 227 |             {status.label} — {status.description}
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): `{status.label} — {status.description}` closes FocusShieldPage (opened on line 72). Names declared inside that block end here.

 228 |           </div>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 229 | 
     | Blank line in `src/components/focus-shield/FocusShieldPage.jsx` (the page that edits and autosaves blocking rules), inside FocusShieldPage. The parser skips it. It separates the previous statement from the next so the function is readable.

 230 |           <div style={{ marginTop: 16 }}>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A box that groups the elements inside it. Source: `<div style={{ marginTop: 16 }}>`

 231 |             <PauseControl
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. Pause buttons. Writes pausedUntil through the parent's update, which autosaves. Source: `<PauseControl`

 232 |               rules={local}
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): `rules={local}` closes FocusShieldPage (opened on line 72). Names declared inside that block end here.

 233 |               saving={saveState === "saving"}
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): `saving={saveState === "saving"}` closes FocusShieldPage (opened on line 72). Names declared inside that block end here.

 234 |               onPause={(date) => update({ pausedUntil: date.toISOString() })}
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): statement `onPause={(date) => update({ pausedUntil: date.toISOString() })}`. It runs when FocusShieldPage runs, in order, before the next line of the same function.

 235 |               onResume={() => update({ pausedUntil: null })}
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): statement `onResume={() => update({ pausedUntil: null })}`. It runs when FocusShieldPage runs, in order, before the next line of the same function.

 236 |             />
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): statement `/>`. It runs when FocusShieldPage runs, in order, before the next line of the same function.

 237 |           </div>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 238 |         </section>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Closes it. A grouped block on the settings-style pages. Source: `</section>`

 239 | 
     | Blank line in `src/components/focus-shield/FocusShieldPage.jsx` (the page that edits and autosaves blocking rules), inside FocusShieldPage. The parser skips it. It separates the previous statement from the next so the function is readable.

 240 |         {/* Stats */}
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): `{/* Stats */}` closes FocusShieldPage (opened on line 72). Names declared inside that block end here.

 241 |         <div className="grid-3">
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="grid-3">`

 242 |           <div className="stat-tile">
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="stat-tile">`

 243 |             <div className="stat-value stat-violet">{local.blockedSites.length || "—"}</div>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="stat-value stat-violet">{local.blockedSites.length || "—"}</div>`

 244 |             <div className="stat-label">Blocked sites</div>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="stat-label">Blocked sites</div>`

 245 |           </div>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 246 |           <div className="stat-tile">
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="stat-tile">`

 247 |             <div className="stat-value stat-green">{local.whitelist.length || "—"}</div>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="stat-value stat-green">{local.whitelist.length || "—"}</div>`

 248 |             <div className="stat-label">Whitelisted</div>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="stat-label">Whitelisted</div>`

 249 |           </div>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 250 |           <div className="stat-tile">
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="stat-tile">`

 251 |             <div className="stat-value stat-amber">{distractionsToday > 0 ? distractionsToday : "—"}</div>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="stat-value stat-amber">{distractionsToday > 0 ? distractionsToday : "—"}</div>`

 252 |             <div className="stat-label">Distractions today</div>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="stat-label">Distractions today</div>`

 253 |           </div>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 254 |         </div>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 255 |         {distractionsWeek > 0 && (
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): statement `{distractionsWeek > 0 && (`. It runs when FocusShieldPage runs, in order, before the next line of the same function.

 256 |           <p className="text-xs text-muted" style={{ margin: "-8px 2px 0" }}>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A paragraph. Source: `<p className="text-xs text-muted" style={{ margin: "-8px 2px 0" }}>`

 257 |             {distractionsWeek} tab-switch distractions logged during focus sessions this week.
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): `{distractionsWeek} tab-switch distractions logged during focus sessions this week.` closes FocusShieldPage (opened on line 72). Names declared inside that block end here.

 258 |           </p>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Closes it. A paragraph. Source: `</p>`

 259 |         )}
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): `)}` closes FocusShieldPage (opened on line 72). Names declared inside that block end here.

 260 | 
     | Blank line in `src/components/focus-shield/FocusShieldPage.jsx` (the page that edits and autosaves blocking rules), inside FocusShieldPage. The parser skips it. It separates the previous statement from the next so the function is readable.

 261 |         <PresetPicker blockedSites={local.blockedSites} onApply={(merged) => update({ blockedSites: merged })} />
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. Preset buttons. Merges domains into the block list. Source: `<PresetPicker blockedSites={local.blockedSites} onApply={(merged) => update({ blockedSites: merged })} />`

 262 | 
     | Blank line in `src/components/focus-shield/FocusShieldPage.jsx` (the page that edits and autosaves blocking rules), inside FocusShieldPage. The parser skips it. It separates the previous statement from the next so the function is readable.

 263 |         <WebsiteListManager
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. One domain list. The page renders two of these. Source: `<WebsiteListManager`

 264 |           title="Blocked Websites"
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): statement `title="Blocked Websites"`. It runs when FocusShieldPage runs, in order, before the next line of the same function.

 265 |           description="Blocked during active focus sessions and any scheduled block window."
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): statement `description="Blocked during active focus sessions and any scheduled block window."`. It runs when FocusShieldPage runs, in order, before the next line of the same function.

 266 |           items={local.blockedSites}
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): `items={local.blockedSites}` closes FocusShieldPage (opened on line 72). Names declared inside that block end here.

 267 |           onChange={(items) => update({ blockedSites: items })}
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): event prop `onChange={(items) => update({ blockedSites: items })}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 268 |           target="blocked"
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): statement `target="blocked"`. It runs when FocusShieldPage runs, in order, before the next line of the same function.

 269 |           emptyIcon="🚫"
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): statement `emptyIcon="🚫"`. It runs when FocusShieldPage runs, in order, before the next line of the same function.

 270 |           emptyTitle="No blocked websites yet"
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): statement `emptyTitle="No blocked websites yet"`. It runs when FocusShieldPage runs, in order, before the next line of the same function.

 271 |           emptyBody="Protect your focus by blocking distracting websites — pick a popular one or add your own."
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): statement `emptyBody="Protect your focus by blocking distracting websites — pick a popular one or add your own."`. It runs when FocusShieldPage runs, in order, before the next line of the same function.

 272 |         />
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): statement `/>`. It runs when FocusShieldPage runs, in order, before the next line of the same function.

 273 | 
     | Blank line in `src/components/focus-shield/FocusShieldPage.jsx` (the page that edits and autosaves blocking rules), inside FocusShieldPage. The parser skips it. It separates the previous statement from the next so the function is readable.

 274 |         <WebsiteListManager
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. One domain list. The page renders two of these. Source: `<WebsiteListManager`

 275 |           title="Whitelisted Websites"
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): statement `title="Whitelisted Websites"`. It runs when FocusShieldPage runs, in order, before the next line of the same function.

 276 |           description="Always allowed, even while the shield is blocking."
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): statement `description="Always allowed, even while the shield is blocking."`. It runs when FocusShieldPage runs, in order, before the next line of the same function.

 277 |           items={local.whitelist}
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): `items={local.whitelist}` closes FocusShieldPage (opened on line 72). Names declared inside that block end here.

 278 |           onChange={(items) => update({ whitelist: items })}
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): event prop `onChange={(items) => update({ whitelist: items })}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 279 |           target="whitelist"
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): statement `target="whitelist"`. It runs when FocusShieldPage runs, in order, before the next line of the same function.

 280 |           emptyIcon="✅"
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): statement `emptyIcon="✅"`. It runs when FocusShieldPage runs, in order, before the next line of the same function.

 281 |           emptyTitle="No whitelisted websites yet"
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): statement `emptyTitle="No whitelisted websites yet"`. It runs when FocusShieldPage runs, in order, before the next line of the same function.

 282 |           emptyBody="Add sites you always need — like docs or your work tools — so they're never blocked by mistake."
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): statement `emptyBody="Add sites you always need — like docs or your work tools — so they're never blocked by mistake."`. It runs when FocusShieldPage runs, in order, before the next line of the same function.

 283 |         />
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): statement `/>`. It runs when FocusShieldPage runs, in order, before the next line of the same function.

 284 | 
     | Blank line in `src/components/focus-shield/FocusShieldPage.jsx` (the page that edits and autosaves blocking rules), inside FocusShieldPage. The parser skips it. It separates the previous statement from the next so the function is readable.

 285 |         {/* Blocked apps (mobile) */}
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): `{/* Blocked apps (mobile) */}` closes FocusShieldPage (opened on line 72). Names declared inside that block end here.

 286 |         <section className="profile-settings-card">
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A grouped block on the settings-style pages. Source: `<section className="profile-settings-card">`

 287 |           <div className="profile-settings-card-header">
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="profile-settings-card-header">`

 288 |             <h2 className="profile-settings-card-title">Blocked Apps</h2>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): JSX `<h2>`. React will create this node when the parent renders.. className chooses the CSS rules from styles.css Source: `<h2 className="profile-settings-card-title">Blocked Apps</h2>`

 289 |             <p className="profile-settings-card-desc">
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A paragraph. Source: `<p className="profile-settings-card-desc">`

 290 |               Add app names to block on mobile. Enforcement requires the native app.
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): statement `Add app names to block on mobile. Enforcement requires the native app.`. It runs when FocusShieldPage runs, in order, before the next line of the same function.

 291 |             </p>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Closes it. A paragraph. Source: `</p>`

 292 |           </div>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 293 |           <div className="fs-notice">
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="fs-notice">`

 294 |             <span aria-hidden="true">⚠️</span>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. An inline box. Source: `<span aria-hidden="true">⚠️</span>`

 295 |             <p className="text-xs text-soft" style={{ margin: 0 }}>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A paragraph. Source: `<p className="text-xs text-soft" style={{ margin: 0 }}>`

 296 |               App blocking on Android requires <strong>Accessibility Service</strong> permissions. iOS requires{" "}
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): `App blocking on Android requires <strong>Accessibility Service</strong> permissions. iOS requires{" "}` closes FocusShieldPage (opened on line 72). Names declared inside that block end here.

 297 |               <strong>FamilyControls</strong>. Rules saved here will be used once the native app is available.
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): JSX `<strong>`. React will create this node when the parent renders. Source: `<strong>FamilyControls</strong>. Rules saved here will be used once the native app is available.`

 298 |             </p>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Closes it. A paragraph. Source: `</p>`

 299 |           </div>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 300 |           <AppEntryList items={local.blockedApps} onRemove={removeApp} placeholder="No blocked apps yet — add one below" />
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): JSX `<AppEntryList>`. React will create this node when the parent renders. Source: `<AppEntryList items={local.blockedApps} onRemove={removeApp} placeholder="No blocked apps yet — add one below" />`

 301 |           <AppAddRow onAdd={addApp} />
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): JSX `<AppAddRow>`. React will create this node when the parent renders. Source: `<AppAddRow onAdd={addApp} />`

 302 |         </section>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Closes it. A grouped block on the settings-style pages. Source: `</section>`

 303 | 
     | Blank line in `src/components/focus-shield/FocusShieldPage.jsx` (the page that edits and autosaves blocking rules), inside FocusShieldPage. The parser skips it. It separates the previous statement from the next so the function is readable.

 304 |         {/* Schedule */}
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): `{/* Schedule */}` closes FocusShieldPage (opened on line 72). Names declared inside that block end here.

 305 |         <section className="profile-settings-card">
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A grouped block on the settings-style pages. Source: `<section className="profile-settings-card">`

 306 |           <div className="flex items-center justify-between gap-3" style={{ marginBottom: local.schedule.enabled ? 16 : 0 }}>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="flex items-center justify-between gap-3" style={{ marginBottom: local.schedule.enabled ? 16 : 0 }}>`

 307 |             <div>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A box that groups the elements inside it. Source: `<div>`

 308 |               <div className="profile-settings-card-title" style={{ marginBottom: 2 }}>Scheduled blocking</div>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="profile-settings-card-title" style={{ marginBottom: 2 }}>Scheduled blocking</div>`

 309 |               <p className="text-xs text-muted" style={{ margin: 0 }}>Block during specific hours and days, even without a focus session running.</p>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A paragraph. Source: `<p className="text-xs text-muted" style={{ margin: 0 }}>Block during specific hours and days, even without a focus session running.</p>`

 310 |             </div>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 311 |             <Toggle checked={local.schedule.enabled} onChange={(v) => updateSchedule({ enabled: v })} label="Scheduled blocking enabled" />
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. On/off switch. The parent owns the boolean. Source: `<Toggle checked={local.schedule.enabled} onChange={(v) => updateSchedule({ enabled: v })} label="Scheduled blocking enabled" />`

 312 |           </div>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 313 | 
     | Blank line in `src/components/focus-shield/FocusShieldPage.jsx` (the page that edits and autosaves blocking rules), inside FocusShieldPage. The parser skips it. It separates the previous statement from the next so the function is readable.

 314 |           {local.schedule.enabled && (
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): statement `{local.schedule.enabled && (`. It runs when FocusShieldPage runs, in order, before the next line of the same function.

 315 |             <>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): JSX `<element>`. React will create this node when the parent renders. Source: `<>`

 316 |               <div style={{ display: "flex", gap: 12, flexWrap: "wrap", marginBottom: 14 }}>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A box that groups the elements inside it. Source: `<div style={{ display: "flex", gap: 12, flexWrap: "wrap", marginBottom: 14 }}>`

 317 |                 <div className="profile-form-field" style={{ flex: "1 1 120px" }}>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="profile-form-field" style={{ flex: "1 1 120px" }}>`

 318 |                   <label className="profile-form-label">Start time</label>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. The caption for an input. Source: `<label className="profile-form-label">Start time</label>`

 319 |                   <input className="profile-form-input" type="time" value={local.schedule.startTime} onChange={(e) => updateSchedule({ startTime: e.target.value })} />
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A text or date field. If value and onChange are set, React owns what it shows. Source: `<input className="profile-form-input" type="time" value={local.schedule.startTime} onChange={(e) => updateSchedule({ startTime: e.target.value })} />`

 320 |                 </div>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 321 |                 <div className="profile-form-field" style={{ flex: "1 1 120px" }}>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="profile-form-field" style={{ flex: "1 1 120px" }}>`

 322 |                   <label className="profile-form-label">End time</label>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. The caption for an input. Source: `<label className="profile-form-label">End time</label>`

 323 |                   <input className="profile-form-input" type="time" value={local.schedule.endTime} onChange={(e) => updateSchedule({ endTime: e.target.value })} />
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A text or date field. If value and onChange are set, React owns what it shows. Source: `<input className="profile-form-input" type="time" value={local.schedule.endTime} onChange={(e) => updateSchedule({ endTime: e.target.value })} />`

 324 |                 </div>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 325 |               </div>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 326 |               <div>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A box that groups the elements inside it. Source: `<div>`

 327 |                 <p className="profile-form-label" style={{ marginBottom: 8 }}>Active days</p>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A paragraph. Source: `<p className="profile-form-label" style={{ marginBottom: 8 }}>Active days</p>`

 328 |                 <div style={{ display: "flex", gap: 6, flexWrap: "wrap" }}>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A box that groups the elements inside it. Source: `<div style={{ display: "flex", gap: 6, flexWrap: "wrap" }}>`

 329 |                   {DAY_LABELS.map((d, i) => {
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): iteration `{DAY_LABELS.map((d, i) => {`.

 330 |                     const active = local.schedule.days.includes(i);
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): `active` is assigned `local.schedule.days.includes(i);`. Later lines in this function read that name.

 331 |                     return (
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

 332 |                       <button
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button`

 333 |                         key={i}
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): `key={i}` closes {DAY_LABELS.map((d, i) => { (opened on line 329). Names declared inside that block end here.

 334 |                         type="button"
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): statement `type="button"`. It runs when FocusShieldPage runs, in order, before the next line of the same function.

 335 |                         onClick={() => toggleDay(i)}
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): event prop `onClick={() => toggleDay(i)}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 336 |                         className={`fs-day-pill${active ? " fs-day-pill--active" : ""}`}
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): `className={`fs-day-pill${active ? " fs-day-pill--active" : ""}`}` closes {DAY_LABELS.map((d, i) => { (opened on line 329). Names declared inside that block end here.

 337 |                         aria-pressed={active}
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): `aria-pressed={active}` closes {DAY_LABELS.map((d, i) => { (opened on line 329). Names declared inside that block end here.

 338 |                       >
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): statement `>`. It runs when FocusShieldPage runs, in order, before the next line of the same function.

 339 |                         {d}
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): `{d}` closes {DAY_LABELS.map((d, i) => { (opened on line 329). Names declared inside that block end here.

 340 |                       </button>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

 341 |                     );
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): statement `);`. It runs when FocusShieldPage runs, in order, before the next line of the same function.

 342 |                   })}
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): `})}` closes {DAY_LABELS.map((d, i) => { (opened on line 329). Names declared inside that block end here.

 343 |                 </div>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 344 |               </div>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 345 |             </>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): JSX `<element>`. This closes that element. Source: `</>`

 346 |           )}
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): `)}` closes FocusShieldPage (opened on line 72). Names declared inside that block end here.

 347 |         </section>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Closes it. A grouped block on the settings-style pages. Source: `</section>`

 348 | 
     | Blank line in `src/components/focus-shield/FocusShieldPage.jsx` (the page that edits and autosaves blocking rules), inside FocusShieldPage. The parser skips it. It separates the previous statement from the next so the function is readable.

 349 |         {/* Import / Export */}
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): `{/* Import / Export */}` closes FocusShieldPage (opened on line 72). Names declared inside that block end here.

 350 |         <section className="profile-settings-card">
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A grouped block on the settings-style pages. Source: `<section className="profile-settings-card">`

 351 |           <div className="profile-settings-card-header">
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="profile-settings-card-header">`

 352 |             <h2 className="profile-settings-card-title">Import / Export</h2>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): JSX `<h2>`. React will create this node when the parent renders.. className chooses the CSS rules from styles.css Source: `<h2 className="profile-settings-card-title">Import / Export</h2>`

 353 |             <p className="profile-settings-card-desc">Back up your rules or move them to another device.</p>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A paragraph. Source: `<p className="profile-settings-card-desc">Back up your rules or move them to another device.</p>`

 354 |           </div>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 355 |           <div style={{ display: "flex", gap: 10, flexWrap: "wrap" }}>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A box that groups the elements inside it. Source: `<div style={{ display: "flex", gap: 10, flexWrap: "wrap" }}>`

 356 |             <button type="button" className="btn btn-secondary btn-sm" onClick={handleExport}>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button type="button" className="btn btn-secondary btn-sm" onClick={handleExport}>`

 357 |               ⭳ Export rules
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): statement `⭳ Export rules`. It runs when FocusShieldPage runs, in order, before the next line of the same function.

 358 |             </button>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

 359 |             <button type="button" className="btn btn-ghost btn-sm" onClick={() => fileInputRef.current?.click()}>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button type="button" className="btn btn-ghost btn-sm" onClick={() => fileInputRef.current?.click()}>`

 360 |               ⭱ Import rules
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): statement `⭱ Import rules`. It runs when FocusShieldPage runs, in order, before the next line of the same function.

 361 |             </button>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

 362 |             <input ref={fileInputRef} type="file" accept="application/json" hidden onChange={handleImportFile} />
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Opens it. A text or date field. If value and onChange are set, React owns what it shows. Source: `<input ref={fileInputRef} type="file" accept="application/json" hidden onChange={handleImportFile} />`

 363 |           </div>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 364 |         </section>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Closes it. A grouped block on the settings-style pages. Source: `</section>`

 365 |       </div>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 366 |     </div>
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 367 |   );
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): statement `);`. It runs when FocusShieldPage runs, in order, before the next line of the same function.

 368 | }
     | In `FocusShieldPage` (src/components/focus-shield/FocusShieldPage.jsx): `}` closes FocusShieldPage (opened on line 72). Names declared inside that block end here.

