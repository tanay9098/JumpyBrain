# `src/components/focus-shield/FocusShieldPage.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import React, { useEffect, useRef, useState } from "react";
     | Borrows React so this file can remember things and draw the screen.

   2 | import api from "../../services/api";
     | This file borrows a tool another file already made.

   3 | import { useBlockingStore } from "../../stores/blockingStore";
     | This file borrows a tool another file already made.

   4 | import Toggle from "./Toggle";
     | This file borrows a tool another file already made.

   5 | import PauseControl from "./PauseControl";
     | This file borrows a tool another file already made.

   6 | import PresetPicker from "./PresetPicker";
     | This file borrows a tool another file already made.

   7 | import WebsiteListManager from "./WebsiteListManager";
     | This file borrows a tool another file already made.

   8 | import { getShieldStatus } from "../../utils/focusShield";
     | This file borrows a tool another file already made.

   9 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  10 | const DAY_LABELS = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
     | Sunday-first labels. Index matches Date.getDay and the schedule.days numbers.

  11 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  12 | function AppEntryList({ items, onRemove, placeholder }) {
     | This starts AppEntryList. Renders blocked apps with a remove button.

  13 |   return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  14 |     <div style={{ display: "flex", flexDirection: "column", gap: 6 }}>
     | This draws one piece of the page while AppEntryList is showing.

  15 |       {items.length === 0 && (
     | Inside AppEntryList, this line runs as written: {items.length === 0 && (. It happens in order, after the line above it and before the line below it.

  16 |         <p className="text-xs text-muted" style={{ margin: 0 }}>{placeholder}</p>
     | This draws one piece of the page while AppEntryList is showing.

  17 |       )}
     | This ends AppEntryList (opened on line 12).

  18 |       {items.map((item, idx) => (
     | Inside AppEntryList, this line runs as written: {items.map((item, idx) => (. It happens in order, after the line above it and before the line below it.

  19 |         <div key={item._id || idx} className="fs-app-row">
     | This draws one piece of the page while AppEntryList is showing.

  20 |           <span className="fs-row-domain">
     | This draws one piece of the page while AppEntryList is showing.

  21 |             {item.value}
     | This ends AppEntryList (opened on line 12).

  22 |             {item.label && <span className="fs-row-domain-sub"> {item.label}</span>}
     | This ends AppEntryList (opened on line 12).

  23 |           </span>
     | This ends a drawing that AppEntryList started just above.

  24 |           <button type="button" onClick={() => onRemove(idx)} className="fs-app-remove" aria-label={`Remove ${item.value}`}>
     | This draws one piece of the page while AppEntryList is showing.

  25 |             ×
     | Inside AppEntryList, this line runs as written: ×. It happens in order, after the line above it and before the line below it.

  26 |           </button>
     | This ends a drawing that AppEntryList started just above.

  27 |         </div>
     | This ends a drawing that AppEntryList started just above.

  28 |       ))}
     | This ends AppEntryList (opened on line 12).

  29 |     </div>
     | This ends a drawing that AppEntryList started just above.

  30 |   );
     | This closes a box of instructions that opened above.

  31 | }
     | This ends AppEntryList (opened on line 12).

  32 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  33 | function AppAddRow({ onAdd }) {
     | This starts AppAddRow. Two inputs: display name and optional package name.

  34 |   const [value, setValue] = useState("");
     | This gives a short name to a value so the rest of AppAddRow can use it.

  35 |   const [label, setLabel] = useState("");
     | This gives a short name to a value so the rest of AppAddRow can use it.

  36 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  37 |   function handleAdd() {
     | This starts handleAdd. Trims the name and calls onAdd, then clears the inputs.

  38 |     const trimmed = value.trim();
     | This gives a short name to a value so the rest of handleAdd can use it.

  39 |     if (!trimmed) return;
     | This asks a yes-or-no question. The next bit runs only on yes.

  40 |     onAdd({ value: trimmed, label: label.trim(), enabled: true });
     | This ends handleAdd (opened on line 37).

  41 |     setValue("");
     | Inside handleAdd, this line runs as written: setValue("");. It happens in order, after the line above it and before the line below it.

  42 |     setLabel("");
     | Inside handleAdd, this line runs as written: setLabel("");. It happens in order, after the line above it and before the line below it.

  43 |   }
     | This ends handleAdd (opened on line 37).

  44 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  45 |   return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  46 |     <div style={{ display: "flex", gap: 8, flexWrap: "wrap", marginTop: 10 }}>
     | This draws one piece of the page while AppAddRow is showing.

  47 |       <input
     | This draws one piece of the page while AppAddRow is showing.

  48 |         className="profile-form-input"
     | Inside AppAddRow, this line runs as written: className="profile-form-input". It happens in order, after the line above it and before the line below it.

  49 |         style={{ flex: "2 1 160px", minWidth: 0 }}
     | This ends AppAddRow (opened on line 33).

  50 |         value={value}
     | This ends AppAddRow (opened on line 33).

  51 |         onChange={(e) => setValue(e.target.value)}
     | This ends AppAddRow (opened on line 33).

  52 |         onKeyDown={(e) => e.key === "Enter" && (e.preventDefault(), handleAdd())}
     | This ends AppAddRow (opened on line 33).

  53 |         placeholder="e.g. Instagram"
     | Inside AppAddRow, this line runs as written: placeholder="e.g. Instagram". It happens in order, after the line above it and before the line below it.

  54 |         maxLength={100}
     | This ends AppAddRow (opened on line 33).

  55 |       />
     | This closes a box of instructions that opened above.

  56 |       <input
     | This draws one piece of the page while AppAddRow is showing.

  57 |         className="profile-form-input"
     | Inside AppAddRow, this line runs as written: className="profile-form-input". It happens in order, after the line above it and before the line below it.

  58 |         style={{ flex: "1 1 100px", minWidth: 0 }}
     | This ends AppAddRow (opened on line 33).

  59 |         value={label}
     | This ends AppAddRow (opened on line 33).

  60 |         onChange={(e) => setLabel(e.target.value)}
     | This ends AppAddRow (opened on line 33).

  61 |         onKeyDown={(e) => e.key === "Enter" && (e.preventDefault(), handleAdd())}
     | This ends AppAddRow (opened on line 33).

  62 |         placeholder="Package name (optional)"
     | Inside AppAddRow, this line runs as written: placeholder="Package name (optional)". It happens in order, after the line above it and before the line below it.

  63 |         maxLength={100}
     | This ends AppAddRow (opened on line 33).

  64 |       />
     | This closes a box of instructions that opened above.

  65 |       <button type="button" className="profile-save-btn" style={{ flexShrink: 0, padding: "0 16px" }} onClick={handleAdd} disabled={!value.trim()}>
     | This draws one piece of the page while AppAddRow is showing.

  66 |         Add
     | Inside AppAddRow, this line runs as written: Add. It happens in order, after the line above it and before the line below it.

  67 |       </button>
     | This ends a drawing that AppAddRow started just above.

  68 |     </div>
     | This ends a drawing that AppAddRow started just above.

  69 |   );
     | This closes a box of instructions that opened above.

  70 | }
     | This ends AppAddRow (opened on line 33).

  71 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  72 | export default function FocusShieldPage() {
     | This starts FocusShieldPage. Loads GET /blocking into local state and the Zustand store, then PUTs local 600ms after each change.

  73 |   const { loading, setRules, setLoading } = useBlockingStore();
     | True until UserProvider finishes the first localStorage read. ProtectedRoute renders nothing during that moment so Auth does not flash.

  74 |   const [local, setLocal] = useState(null);
     | The editable copy of blocking rules on the Focus Shield page. Every toggle writes here. The effect on local autosaves.

  75 |   const [saveState, setSaveState] = useState("idle"); // idle | saving | saved | error
     | idle, saving, saved, or error. The Focus Shield page shows this next to the title. There is no Save button; local changes debounce into PUT /blocking.

  76 |   const [statsSessions, setStatsSessions] = useState([]);
     | This gives a short name to a value so the rest of FocusShieldPage can use it.

  77 |   const fileInputRef = useRef(null);
     | This gives a short name to a value so the rest of FocusShieldPage can use it.

  78 |   const skipNextSave = useRef(true);
     | Starts true so the first GET /blocking does not immediately PUT the same rules back.

  79 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  80 |   useEffect(() => {
     | This is an extra job that happens after the picture is drawn.

  81 |     setLoading(true);
     | Inside FocusShieldPage, this line runs as written: setLoading(true);. It happens in order, after the line above it and before the line below it.

  82 |     api.get("/blocking")
     | This asks the server (the office that keeps tasks and accounts) for something, or sends it something.

  83 |       .then((data) => {
     | Inside FocusShieldPage, this line runs as written: .then((data) => {. It happens in order, after the line above it and before the line below it.

  84 |         skipNextSave.current = true;
     | Inside FocusShieldPage, this line runs as written: skipNextSave.current = true;. It happens in order, after the line above it and before the line below it.

  85 |         setRules(data.rules);
     | Inside FocusShieldPage, this line runs as written: setRules(data.rules);. It happens in order, after the line above it and before the line below it.

  86 |         setLocal(data.rules);
     | Inside FocusShieldPage, this line runs as written: setLocal(data.rules);. It happens in order, after the line above it and before the line below it.

  87 |       })
     | This ends .then((data) => { (opened on line 83).

  88 |       .catch(() => setSaveState("error"))
     | Inside FocusShieldPage, this line runs as written: .catch(() => setSaveState("error")). It happens in order, after the line above it and before the line below it.

  89 |       .finally(() => setLoading(false));
     | Inside FocusShieldPage, this line runs as written: .finally(() => setLoading(false));. It happens in order, after the line above it and before the line below it.

  90 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  91 |     api.get("/stats/weekly").then((d) => setStatsSessions(d?.sessions || [])).catch(() => {});
     | This asks the server (the office that keeps tasks and accounts) for something, or sends it something.

  92 |   }, []);
     | This ends effect in FocusShieldPage (opened on line 80).

  93 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  94 |   // Autosave — every mutation (toggle, add, delete, pause, preset, schedule edit) flows
     | A note written for people. The app does not run it.

  95 |   // through `local` and lands here debounced, so the page never needs an explicit Save button.
     | A note written for people. The app does not run it.

  96 |   useEffect(() => {
     | This is an extra job that happens after the picture is drawn.

  97 |     if (!local) return;
     | This asks a yes-or-no question. The next bit runs only on yes.

  98 |     if (skipNextSave.current) { skipNextSave.current = false; return; }
     | This asks a yes-or-no question. The next bit runs only on yes.

  99 |     setSaveState("saving");
     | Inside FocusShieldPage, this line runs as written: setSaveState("saving");. It happens in order, after the line above it and before the line below it.

 100 |     const t = setTimeout(async () => {
     | This gives a short name to a value so the rest of FocusShieldPage can use it.

 101 |       try {
     | Inside FocusShieldPage, this line runs as written: try {. It happens in order, after the line above it and before the line below it.

 102 |         const data = await api.put("/blocking", local);
     | This gives a short name to a value so the rest of FocusShieldPage can use it.

 103 |         setRules(data.rules);
     | Inside FocusShieldPage, this line runs as written: setRules(data.rules);. It happens in order, after the line above it and before the line below it.

 104 |         setSaveState("saved");
     | Inside FocusShieldPage, this line runs as written: setSaveState("saved");. It happens in order, after the line above it and before the line below it.

 105 |         setTimeout(() => setSaveState((s) => (s === "saved" ? "idle" : s)), 1800);
     | Inside FocusShieldPage, this line runs as written: setTimeout(() => setSaveState((s) => (s === "saved" ? "idle" : s)), 1800);. It happens in order, after the line above it and before the line below it.

 106 |       } catch {
     | This ends try { (opened on line 101).

 107 |         setSaveState("error");
     | Inside FocusShieldPage, this line runs as written: setSaveState("error");. It happens in order, after the line above it and before the line below it.

 108 |       }
     | This ends } catch { (opened on line 106).

 109 |     }, 600);
     | This ends const t = setTimeout(async () => { (opened on line 100).

 110 |     return () => clearTimeout(t);
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

 111 |   }, [local]);
     | This ends effect in FocusShieldPage (opened on line 96).

 112 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 113 |   if (loading || !local) {
     | This asks a yes-or-no question. The next bit runs only on yes.

 114 |     return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

 115 |       <div className="profile-settings-page">
     | This draws one piece of the page while FocusShieldPage is showing.

 116 |         <div className="profile-settings-container">
     | This draws one piece of the page while FocusShieldPage is showing.

 117 |           <p className="text-sm text-muted">Loading Focus Shield…</p>
     | This draws one piece of the page while FocusShieldPage is showing.

 118 |         </div>
     | This ends a drawing that FocusShieldPage started just above.

 119 |       </div>
     | This ends a drawing that FocusShieldPage started just above.

 120 |     );
     | This closes a box of instructions that opened above.

 121 |   }
     | This ends if (loading || !local) { (opened on line 113).

 122 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 123 |   function update(patch) {
     | This starts update. Shallow-merges a patch into local, which schedules the autosave.

 124 |     setLocal((prev) => ({ ...prev, ...patch }));
     | This ends update (opened on line 123).

 125 |   }
     | This ends update (opened on line 123).

 126 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 127 |   function updateSchedule(patch) {
     | This starts updateSchedule. Same, but the patch is applied to local.schedule.

 128 |     setLocal((prev) => ({ ...prev, schedule: { ...prev.schedule, ...patch } }));
     | This ends updateSchedule (opened on line 127).

 129 |   }
     | This ends updateSchedule (opened on line 127).

 130 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 131 |   function toggleDay(day) {
     | This starts toggleDay. Adds or removes a weekday number and keeps the array sorted.

 132 |     const days = local.schedule.days.includes(day)
     | This gives a short name to a value so the rest of toggleDay can use it.

 133 |       ? local.schedule.days.filter((d) => d !== day)
     | Inside toggleDay, this line runs as written: ? local.schedule.days.filter((d) => d !== day). It happens in order, after the line above it and before the line below it.

 134 |       : [...local.schedule.days, day].sort((a, b) => a - b);
     | Inside toggleDay, this line runs as written: : [...local.schedule.days, day].sort((a, b) => a - b);. It happens in order, after the line above it and before the line below it.

 135 |     updateSchedule({ days });
     | This ends toggleDay (opened on line 131).

 136 |   }
     | This ends toggleDay (opened on line 131).

 137 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 138 |   function addApp(entry) {
     | This starts addApp. Appends a blocked-app entry. Enforcement is native; this page only stores the name.

 139 |     update({ blockedApps: [...local.blockedApps, entry] });
     | This ends addApp (opened on line 138).

 140 |   }
     | This ends addApp (opened on line 138).

 141 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 142 |   function removeApp(idx) {
     | This starts removeApp. Drops one blocked app by index.

 143 |     update({ blockedApps: local.blockedApps.filter((_, i) => i !== idx) });
     | This ends removeApp (opened on line 142).

 144 |   }
     | This ends removeApp (opened on line 142).

 145 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 146 |   function handleExport() {
     | This starts handleExport. Downloads jumpybrain-focus-shield-rules.json containing blocked sites and the whitelist.

 147 |     const payload = {
     | This gives a short name to a value so the rest of handleExport can use it.

 148 |       exportedAt: new Date().toISOString(),
     | Inside handleExport, this line runs as written: exportedAt: new Date().toISOString(),. It happens in order, after the line above it and before the line below it.

 149 |       blockedSites: local.blockedSites,
     | Inside handleExport, this line runs as written: blockedSites: local.blockedSites,. It happens in order, after the line above it and before the line below it.

 150 |       whitelist: local.whitelist,
     | Inside handleExport, this line runs as written: whitelist: local.whitelist,. It happens in order, after the line above it and before the line below it.

 151 |     };
     | This ends const payload = { (opened on line 147).

 152 |     const blob = new Blob([JSON.stringify(payload, null, 2)], { type: "application/json" });
     | This gives a short name to a value so the rest of handleExport can use it.

 153 |     const url = URL.createObjectURL(blob);
     | This gives a short name to a value so the rest of handleExport can use it.

 154 |     const a = document.createElement("a");
     | This gives a short name to a value so the rest of handleExport can use it.

 155 |     a.href = url;
     | Inside handleExport, this line runs as written: a.href = url;. It happens in order, after the line above it and before the line below it.

 156 |     a.download = "jumpybrain-focus-shield-rules.json";
     | Inside handleExport, this line runs as written: a.download = "jumpybrain-focus-shield-rules.json";. It happens in order, after the line above it and before the line below it.

 157 |     a.click();
     | Inside handleExport, this line runs as written: a.click();. It happens in order, after the line above it and before the line below it.

 158 |     URL.revokeObjectURL(url);
     | Inside handleExport, this line runs as written: URL.revokeObjectURL(url);. It happens in order, after the line above it and before the line below it.

 159 |   }
     | This ends handleExport (opened on line 146).

 160 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 161 |   function handleImportFile(e) {
     | This starts handleImportFile. Reads a JSON file and appends domains that are not already present.

 162 |     const file = e.target.files?.[0];
     | This gives a short name to a value so the rest of handleImportFile can use it.

 163 |     e.target.value = "";
     | Inside handleImportFile, this line runs as written: e.target.value = "";. It happens in order, after the line above it and before the line below it.

 164 |     if (!file) return;
     | This asks a yes-or-no question. The next bit runs only on yes.

 165 |     const reader = new FileReader();
     | This gives a short name to a value so the rest of handleImportFile can use it.

 166 |     reader.onload = () => {
     | Inside handleImportFile, this line runs as written: reader.onload = () => {. It happens in order, after the line above it and before the line below it.

 167 |       try {
     | Inside handleImportFile, this line runs as written: try {. It happens in order, after the line above it and before the line below it.

 168 |         const parsed = JSON.parse(String(reader.result));
     | This gives a short name to a value so the rest of handleImportFile can use it.

 169 |         const importedBlocked = Array.isArray(parsed.blockedSites) ? parsed.blockedSites : [];
     | This gives a short name to a value so the rest of handleImportFile can use it.

 170 |         const importedWhitelist = Array.isArray(parsed.whitelist) ? parsed.whitelist : [];
     | This gives a short name to a value so the rest of handleImportFile can use it.

 171 |         const haveBlocked = new Set(local.blockedSites.map((s) => s.value));
     | This gives a short name to a value so the rest of handleImportFile can use it.

 172 |         const haveWhite = new Set(local.whitelist.map((s) => s.value));
     | This gives a short name to a value so the rest of handleImportFile can use it.

 173 |         const newBlocked = importedBlocked.filter((s) => s?.value && !haveBlocked.has(s.value));
     | This gives a short name to a value so the rest of handleImportFile can use it.

 174 |         const newWhite = importedWhitelist.filter((s) => s?.value && !haveWhite.has(s.value));
     | This gives a short name to a value so the rest of handleImportFile can use it.

 175 |         update({
     | Inside handleImportFile, this line runs as written: update({. It happens in order, after the line above it and before the line below it.

 176 |           blockedSites: [...local.blockedSites, ...newBlocked],
     | Inside handleImportFile, this line runs as written: blockedSites: [...local.blockedSites, ...newBlocked],. It happens in order, after the line above it and before the line below it.

 177 |           whitelist: [...local.whitelist, ...newWhite],
     | Inside handleImportFile, this line runs as written: whitelist: [...local.whitelist, ...newWhite],. It happens in order, after the line above it and before the line below it.

 178 |         });
     | This ends update({ (opened on line 175).

 179 |       } catch {
     | This ends try { (opened on line 167).

 180 |         setSaveState("error");
     | Inside handleImportFile, this line runs as written: setSaveState("error");. It happens in order, after the line above it and before the line below it.

 181 |       }
     | This ends } catch { (opened on line 179).

 182 |     };
     | This ends reader.onload = () => { (opened on line 166).

 183 |     reader.readAsText(file);
     | Inside handleImportFile, this line runs as written: reader.readAsText(file);. It happens in order, after the line above it and before the line below it.

 184 |   }
     | This ends handleImportFile (opened on line 161).

 185 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 186 |   const status = getShieldStatus(local);
     | This gives a short name to a value so the rest of FocusShieldPage can use it.

 187 |   const todaySessions = statsSessions.filter((s) => {
     | This gives a short name to a value so the rest of FocusShieldPage can use it.

 188 |     const d = s.completedAt ? new Date(s.completedAt) : null;
     | This gives a short name to a value so the rest of FocusShieldPage can use it.

 189 |     if (!d) return false;
     | This asks a yes-or-no question. The next bit runs only on yes.

 190 |     const now = new Date();
     | This gives a short name to a value so the rest of FocusShieldPage can use it.

 191 |     return d.toDateString() === now.toDateString();
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

 192 |   });
     | This ends const todaySessions = statsSessions.filter((s) = (opened on line 187).

 193 |   const distractionsToday = todaySessions.reduce((a, s) => a + (s.distractionCount || 0), 0);
     | This gives a short name to a value so the rest of FocusShieldPage can use it.

 194 |   const distractionsWeek = statsSessions.reduce((a, s) => a + (s.distractionCount || 0), 0);
     | This gives a short name to a value so the rest of FocusShieldPage can use it.

 195 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 196 |   return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

 197 |     <div className="profile-settings-page">
     | This draws one piece of the page while FocusShieldPage is showing.

 198 |       <div className="profile-settings-container">
     | This draws one piece of the page while FocusShieldPage is showing.

 199 |         <div className="profile-settings-header fs-page-header">
     | This draws one piece of the page while FocusShieldPage is showing.

 200 |           <div>
     | This draws one piece of the page while FocusShieldPage is showing.

 201 |             <h1 className="profile-settings-title">🛡️ Focus Shield</h1>
     | This draws one piece of the page while FocusShieldPage is showing.

 202 |             <p className="profile-settings-subtitle">
     | This draws one piece of the page while FocusShieldPage is showing.

 203 |               Block distracting sites during focus sessions, always allow the ones you need.
     | Inside FocusShieldPage, this line runs as written: Block distracting sites during focus sessions, always allow the ones you need.. It happens in order, after the line above it and before the line below it.

 204 |             </p>
     | This ends a drawing that FocusShieldPage started just above.

 205 |           </div>
     | This ends a drawing that FocusShieldPage started just above.

 206 |           <span className="fs-save-indicator" aria-live="polite">
     | This draws one piece of the page while FocusShieldPage is showing.

 207 |             {saveState === "saving" && "Saving…"}
     | This ends FocusShieldPage (opened on line 72).

 208 |             {saveState === "saved" && "✓ Saved"}
     | This ends FocusShieldPage (opened on line 72).

 209 |             {saveState === "error" && "⚠ Couldn't save"}
     | This ends FocusShieldPage (opened on line 72).

 210 |           </span>
     | This ends a drawing that FocusShieldPage started just above.

 211 |         </div>
     | This ends a drawing that FocusShieldPage started just above.

 212 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 213 |         {/* Master toggle + status + pause */}
     | This ends FocusShieldPage (opened on line 72).

 214 |         <section className="profile-settings-card">
     | This draws one piece of the page while FocusShieldPage is showing.

 215 |           <div className="flex items-center justify-between gap-3">
     | This draws one piece of the page while FocusShieldPage is showing.

 216 |             <div>
     | This draws one piece of the page while FocusShieldPage is showing.

 217 |               <div className="profile-settings-card-title" style={{ marginBottom: 2 }}>Focus Shield</div>
     | This draws one piece of the page while FocusShieldPage is showing.

 218 |               <p className="text-xs text-muted" style={{ margin: 0 }}>
     | This draws one piece of the page while FocusShieldPage is showing.

 219 |                 Enforcement runs in the Chrome extension (desktop) or native app (mobile).
     | Inside FocusShieldPage, this line runs as written: Enforcement runs in the Chrome extension (desktop) or native app (mobile).. It happens in order, after the line above it and before the line below it.

 220 |               </p>
     | This ends a drawing that FocusShieldPage started just above.

 221 |             </div>
     | This ends a drawing that FocusShieldPage started just above.

 222 |             <Toggle checked={local.isEnabled} onChange={(v) => update({ isEnabled: v })} label="Focus Shield enabled" />
     | This draws one piece of the page while FocusShieldPage is showing.

 223 |           </div>
     | This ends a drawing that FocusShieldPage started just above.

 224 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 225 |           <div className={`fs-status-pill fs-status-pill--${status.level}`} style={{ marginTop: 14 }}>
     | This draws one piece of the page while FocusShieldPage is showing.

 226 |             <span className="fs-status-dot" />
     | This draws one piece of the page while FocusShieldPage is showing.

 227 |             {status.label} — {status.description}
     | This ends FocusShieldPage (opened on line 72).

 228 |           </div>
     | This ends a drawing that FocusShieldPage started just above.

 229 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 230 |           <div style={{ marginTop: 16 }}>
     | This draws one piece of the page while FocusShieldPage is showing.

 231 |             <PauseControl
     | This draws one piece of the page while FocusShieldPage is showing.

 232 |               rules={local}
     | This ends FocusShieldPage (opened on line 72).

 233 |               saving={saveState === "saving"}
     | This ends FocusShieldPage (opened on line 72).

 234 |               onPause={(date) => update({ pausedUntil: date.toISOString() })}
     | This ends FocusShieldPage (opened on line 72).

 235 |               onResume={() => update({ pausedUntil: null })}
     | This ends FocusShieldPage (opened on line 72).

 236 |             />
     | This closes a box of instructions that opened above.

 237 |           </div>
     | This ends a drawing that FocusShieldPage started just above.

 238 |         </section>
     | This ends a drawing that FocusShieldPage started just above.

 239 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 240 |         {/* Stats */}
     | This ends FocusShieldPage (opened on line 72).

 241 |         <div className="grid-3">
     | This draws one piece of the page while FocusShieldPage is showing.

 242 |           <div className="stat-tile">
     | This draws one piece of the page while FocusShieldPage is showing.

 243 |             <div className="stat-value stat-violet">{local.blockedSites.length || "—"}</div>
     | This draws one piece of the page while FocusShieldPage is showing.

 244 |             <div className="stat-label">Blocked sites</div>
     | This draws one piece of the page while FocusShieldPage is showing.

 245 |           </div>
     | This ends a drawing that FocusShieldPage started just above.

 246 |           <div className="stat-tile">
     | This draws one piece of the page while FocusShieldPage is showing.

 247 |             <div className="stat-value stat-green">{local.whitelist.length || "—"}</div>
     | This draws one piece of the page while FocusShieldPage is showing.

 248 |             <div className="stat-label">Whitelisted</div>
     | This draws one piece of the page while FocusShieldPage is showing.

 249 |           </div>
     | This ends a drawing that FocusShieldPage started just above.

 250 |           <div className="stat-tile">
     | This draws one piece of the page while FocusShieldPage is showing.

 251 |             <div className="stat-value stat-amber">{distractionsToday > 0 ? distractionsToday : "—"}</div>
     | This draws one piece of the page while FocusShieldPage is showing.

 252 |             <div className="stat-label">Distractions today</div>
     | This draws one piece of the page while FocusShieldPage is showing.

 253 |           </div>
     | This ends a drawing that FocusShieldPage started just above.

 254 |         </div>
     | This ends a drawing that FocusShieldPage started just above.

 255 |         {distractionsWeek > 0 && (
     | Inside FocusShieldPage, this line runs as written: {distractionsWeek > 0 && (. It happens in order, after the line above it and before the line below it.

 256 |           <p className="text-xs text-muted" style={{ margin: "-8px 2px 0" }}>
     | This draws one piece of the page while FocusShieldPage is showing.

 257 |             {distractionsWeek} tab-switch distractions logged during focus sessions this week.
     | This ends FocusShieldPage (opened on line 72).

 258 |           </p>
     | This ends a drawing that FocusShieldPage started just above.

 259 |         )}
     | This ends FocusShieldPage (opened on line 72).

 260 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 261 |         <PresetPicker blockedSites={local.blockedSites} onApply={(merged) => update({ blockedSites: merged })} />
     | This draws one piece of the page while FocusShieldPage is showing.

 262 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 263 |         <WebsiteListManager
     | This draws one piece of the page while FocusShieldPage is showing.

 264 |           title="Blocked Websites"
     | Inside FocusShieldPage, this line runs as written: title="Blocked Websites". It happens in order, after the line above it and before the line below it.

 265 |           description="Blocked during active focus sessions and any scheduled block window."
     | Inside FocusShieldPage, this line runs as written: description="Blocked during active focus sessions and any scheduled block window.". It happens in order, after the line above it and before the line below it.

 266 |           items={local.blockedSites}
     | This ends FocusShieldPage (opened on line 72).

 267 |           onChange={(items) => update({ blockedSites: items })}
     | This ends FocusShieldPage (opened on line 72).

 268 |           target="blocked"
     | Inside FocusShieldPage, this line runs as written: target="blocked". It happens in order, after the line above it and before the line below it.

 269 |           emptyIcon="🚫"
     | Inside FocusShieldPage, this line runs as written: emptyIcon="🚫". It happens in order, after the line above it and before the line below it.

 270 |           emptyTitle="No blocked websites yet"
     | Inside FocusShieldPage, this line runs as written: emptyTitle="No blocked websites yet". It happens in order, after the line above it and before the line below it.

 271 |           emptyBody="Protect your focus by blocking distracting websites — pick a popular one or add your own."
     | Inside FocusShieldPage, this line runs as written: emptyBody="Protect your focus by blocking distracting websites — pick a popular one or add your own.". It happens in order, after the line above it and before the line below it.

 272 |         />
     | This closes a box of instructions that opened above.

 273 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 274 |         <WebsiteListManager
     | This draws one piece of the page while FocusShieldPage is showing.

 275 |           title="Whitelisted Websites"
     | Inside FocusShieldPage, this line runs as written: title="Whitelisted Websites". It happens in order, after the line above it and before the line below it.

 276 |           description="Always allowed, even while the shield is blocking."
     | Inside FocusShieldPage, this line runs as written: description="Always allowed, even while the shield is blocking.". It happens in order, after the line above it and before the line below it.

 277 |           items={local.whitelist}
     | This ends FocusShieldPage (opened on line 72).

 278 |           onChange={(items) => update({ whitelist: items })}
     | This ends FocusShieldPage (opened on line 72).

 279 |           target="whitelist"
     | Inside FocusShieldPage, this line runs as written: target="whitelist". It happens in order, after the line above it and before the line below it.

 280 |           emptyIcon="✅"
     | Inside FocusShieldPage, this line runs as written: emptyIcon="✅". It happens in order, after the line above it and before the line below it.

 281 |           emptyTitle="No whitelisted websites yet"
     | Inside FocusShieldPage, this line runs as written: emptyTitle="No whitelisted websites yet". It happens in order, after the line above it and before the line below it.

 282 |           emptyBody="Add sites you always need — like docs or your work tools — so they're never blocked by mistake."
     | Inside FocusShieldPage, this line runs as written: emptyBody="Add sites you always need — like docs or your work tools — so they're never blocked by mistake.". It happens in order, after the line above it and before the line below it.

 283 |         />
     | This closes a box of instructions that opened above.

 284 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 285 |         {/* Blocked apps (mobile) */}
     | This ends FocusShieldPage (opened on line 72).

 286 |         <section className="profile-settings-card">
     | This draws one piece of the page while FocusShieldPage is showing.

 287 |           <div className="profile-settings-card-header">
     | This draws one piece of the page while FocusShieldPage is showing.

 288 |             <h2 className="profile-settings-card-title">Blocked Apps</h2>
     | This draws one piece of the page while FocusShieldPage is showing.

 289 |             <p className="profile-settings-card-desc">
     | This draws one piece of the page while FocusShieldPage is showing.

 290 |               Add app names to block on mobile. Enforcement requires the native app.
     | Inside FocusShieldPage, this line runs as written: Add app names to block on mobile. Enforcement requires the native app.. It happens in order, after the line above it and before the line below it.

 291 |             </p>
     | This ends a drawing that FocusShieldPage started just above.

 292 |           </div>
     | This ends a drawing that FocusShieldPage started just above.

 293 |           <div className="fs-notice">
     | This draws one piece of the page while FocusShieldPage is showing.

 294 |             <span aria-hidden="true">⚠️</span>
     | This draws one piece of the page while FocusShieldPage is showing.

 295 |             <p className="text-xs text-soft" style={{ margin: 0 }}>
     | This draws one piece of the page while FocusShieldPage is showing.

 296 |               App blocking on Android requires <strong>Accessibility Service</strong> permissions. iOS requires{" "}
     | This ends FocusShieldPage (opened on line 72).

 297 |               <strong>FamilyControls</strong>. Rules saved here will be used once the native app is available.
     | This draws one piece of the page while FocusShieldPage is showing.

 298 |             </p>
     | This ends a drawing that FocusShieldPage started just above.

 299 |           </div>
     | This ends a drawing that FocusShieldPage started just above.

 300 |           <AppEntryList items={local.blockedApps} onRemove={removeApp} placeholder="No blocked apps yet — add one below" />
     | This draws one piece of the page while FocusShieldPage is showing.

 301 |           <AppAddRow onAdd={addApp} />
     | This draws one piece of the page while FocusShieldPage is showing.

 302 |         </section>
     | This ends a drawing that FocusShieldPage started just above.

 303 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 304 |         {/* Schedule */}
     | This ends FocusShieldPage (opened on line 72).

 305 |         <section className="profile-settings-card">
     | This draws one piece of the page while FocusShieldPage is showing.

 306 |           <div className="flex items-center justify-between gap-3" style={{ marginBottom: local.schedule.enabled ? 16 : 0 }}>
     | This draws one piece of the page while FocusShieldPage is showing.

 307 |             <div>
     | This draws one piece of the page while FocusShieldPage is showing.

 308 |               <div className="profile-settings-card-title" style={{ marginBottom: 2 }}>Scheduled blocking</div>
     | This draws one piece of the page while FocusShieldPage is showing.

 309 |               <p className="text-xs text-muted" style={{ margin: 0 }}>Block during specific hours and days, even without a focus session running.</p>
     | This draws one piece of the page while FocusShieldPage is showing.

 310 |             </div>
     | This ends a drawing that FocusShieldPage started just above.

 311 |             <Toggle checked={local.schedule.enabled} onChange={(v) => updateSchedule({ enabled: v })} label="Scheduled blocking enabled" />
     | This draws one piece of the page while FocusShieldPage is showing.

 312 |           </div>
     | This ends a drawing that FocusShieldPage started just above.

 313 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 314 |           {local.schedule.enabled && (
     | Inside FocusShieldPage, this line runs as written: {local.schedule.enabled && (. It happens in order, after the line above it and before the line below it.

 315 |             <>
     | This draws one piece of the page while FocusShieldPage is showing.

 316 |               <div style={{ display: "flex", gap: 12, flexWrap: "wrap", marginBottom: 14 }}>
     | This draws one piece of the page while FocusShieldPage is showing.

 317 |                 <div className="profile-form-field" style={{ flex: "1 1 120px" }}>
     | This draws one piece of the page while FocusShieldPage is showing.

 318 |                   <label className="profile-form-label">Start time</label>
     | This draws one piece of the page while FocusShieldPage is showing.

 319 |                   <input className="profile-form-input" type="time" value={local.schedule.startTime} onChange={(e) => updateSchedule({ startTime: e.target.value })} />
     | This draws one piece of the page while FocusShieldPage is showing.

 320 |                 </div>
     | This ends a drawing that FocusShieldPage started just above.

 321 |                 <div className="profile-form-field" style={{ flex: "1 1 120px" }}>
     | This draws one piece of the page while FocusShieldPage is showing.

 322 |                   <label className="profile-form-label">End time</label>
     | This draws one piece of the page while FocusShieldPage is showing.

 323 |                   <input className="profile-form-input" type="time" value={local.schedule.endTime} onChange={(e) => updateSchedule({ endTime: e.target.value })} />
     | This draws one piece of the page while FocusShieldPage is showing.

 324 |                 </div>
     | This ends a drawing that FocusShieldPage started just above.

 325 |               </div>
     | This ends a drawing that FocusShieldPage started just above.

 326 |               <div>
     | This draws one piece of the page while FocusShieldPage is showing.

 327 |                 <p className="profile-form-label" style={{ marginBottom: 8 }}>Active days</p>
     | This draws one piece of the page while FocusShieldPage is showing.

 328 |                 <div style={{ display: "flex", gap: 6, flexWrap: "wrap" }}>
     | This draws one piece of the page while FocusShieldPage is showing.

 329 |                   {DAY_LABELS.map((d, i) => {
     | Inside FocusShieldPage, this line runs as written: {DAY_LABELS.map((d, i) => {. It happens in order, after the line above it and before the line below it.

 330 |                     const active = local.schedule.days.includes(i);
     | This gives a short name to a value so the rest of FocusShieldPage can use it.

 331 |                     return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

 332 |                       <button
     | This draws one piece of the page while FocusShieldPage is showing.

 333 |                         key={i}
     | This ends {DAY_LABELS.map((d, i) => { (opened on line 329).

 334 |                         type="button"
     | Inside FocusShieldPage, this line runs as written: type="button". It happens in order, after the line above it and before the line below it.

 335 |                         onClick={() => toggleDay(i)}
     | This decides what happens when you press.

 336 |                         className={`fs-day-pill${active ? " fs-day-pill--active" : ""}`}
     | This ends {DAY_LABELS.map((d, i) => { (opened on line 329).

 337 |                         aria-pressed={active}
     | This ends {DAY_LABELS.map((d, i) => { (opened on line 329).

 338 |                       >
     | Inside FocusShieldPage, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 339 |                         {d}
     | This ends {DAY_LABELS.map((d, i) => { (opened on line 329).

 340 |                       </button>
     | This ends a drawing that FocusShieldPage started just above.

 341 |                     );
     | This closes a box of instructions that opened above.

 342 |                   })}
     | This ends {DAY_LABELS.map((d, i) => { (opened on line 329).

 343 |                 </div>
     | This ends a drawing that FocusShieldPage started just above.

 344 |               </div>
     | This ends a drawing that FocusShieldPage started just above.

 345 |             </>
     | This ends a drawing that FocusShieldPage started just above.

 346 |           )}
     | This ends FocusShieldPage (opened on line 72).

 347 |         </section>
     | This ends a drawing that FocusShieldPage started just above.

 348 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 349 |         {/* Import / Export */}
     | This ends FocusShieldPage (opened on line 72).

 350 |         <section className="profile-settings-card">
     | This draws one piece of the page while FocusShieldPage is showing.

 351 |           <div className="profile-settings-card-header">
     | This draws one piece of the page while FocusShieldPage is showing.

 352 |             <h2 className="profile-settings-card-title">Import / Export</h2>
     | This draws one piece of the page while FocusShieldPage is showing.

 353 |             <p className="profile-settings-card-desc">Back up your rules or move them to another device.</p>
     | This draws one piece of the page while FocusShieldPage is showing.

 354 |           </div>
     | This ends a drawing that FocusShieldPage started just above.

 355 |           <div style={{ display: "flex", gap: 10, flexWrap: "wrap" }}>
     | This draws one piece of the page while FocusShieldPage is showing.

 356 |             <button type="button" className="btn btn-secondary btn-sm" onClick={handleExport}>
     | This draws one piece of the page while FocusShieldPage is showing.

 357 |               ⭳ Export rules
     | Inside FocusShieldPage, this line runs as written: ⭳ Export rules. It happens in order, after the line above it and before the line below it.

 358 |             </button>
     | This ends a drawing that FocusShieldPage started just above.

 359 |             <button type="button" className="btn btn-ghost btn-sm" onClick={() => fileInputRef.current?.click()}>
     | This draws one piece of the page while FocusShieldPage is showing.

 360 |               ⭱ Import rules
     | Inside FocusShieldPage, this line runs as written: ⭱ Import rules. It happens in order, after the line above it and before the line below it.

 361 |             </button>
     | This ends a drawing that FocusShieldPage started just above.

 362 |             <input ref={fileInputRef} type="file" accept="application/json" hidden onChange={handleImportFile} />
     | This draws one piece of the page while FocusShieldPage is showing.

 363 |           </div>
     | This ends a drawing that FocusShieldPage started just above.

 364 |         </section>
     | This ends a drawing that FocusShieldPage started just above.

 365 |       </div>
     | This ends a drawing that FocusShieldPage started just above.

 366 |     </div>
     | This ends a drawing that FocusShieldPage started just above.

 367 |   );
     | This closes a box of instructions that opened above.

 368 | }
     | This ends FocusShieldPage (opened on line 72).

