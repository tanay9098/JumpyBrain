# `src/components/TodoList.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import { useEffect, useRef, useState } from "react";
     | Borrows React so this file can remember things and draw the screen.

   2 | import { useSearchParams } from "react-router-dom";
     | Borrows React so this file can remember things and draw the screen.

   3 | import api from "../services/api";
     | This file borrows a tool another file already made.

   4 | import { notify } from "../utils/notify";
     | This file borrows a tool another file already made.

   5 | import { scheduleDeadline, clearDeadline } from "../utils/deadlineScheduler";
     | This file borrows a tool another file already made.

   6 | import { useEnergy } from "../contexts/EnergyContext";
     | This file borrows a tool another file already made.

   7 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   8 | // ── Dread pip colours ────────────────────────────────────────────────────
     | A note written for people. The app does not run it.

   9 | function DreadMeter({ score, onChange }) {
     | This starts DreadMeter. Five pips. Click or Enter calls onChange with 1–5. Add-task, edit, and each row all use it.

  10 |   return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  11 |     <div className="dread-meter" title={`Dread: ${score}/5`} role="group" aria-label={`Dread score ${score} of 5`}>
     | This draws one piece of the page while DreadMeter is showing.

  12 |       <span className="text-xs text-muted" style={{ marginRight: 4 }}>Dread</span>
     | This draws one piece of the page while DreadMeter is showing.

  13 |       {[1, 2, 3, 4, 5].map((n) => (
     | Inside DreadMeter, this line runs as written: {[1, 2, 3, 4, 5].map((n) => (. It happens in order, after the line above it and before the line below it.

  14 |         <div
     | This draws one piece of the page while DreadMeter is showing.

  15 |           key={n}
     | This ends DreadMeter (opened on line 9).

  16 |           className={`dread-pip ${n <= score ? `active-${score}` : ""}`}
     | This ends DreadMeter (opened on line 9).

  17 |           onClick={() => onChange && onChange(n)}
     | This decides what happens when you press.

  18 |           role="button"
     | Inside DreadMeter, this line runs as written: role="button". It happens in order, after the line above it and before the line below it.

  19 |           tabIndex={0}
     | This ends DreadMeter (opened on line 9).

  20 |           aria-label={`Dread level ${n}`}
     | This ends DreadMeter (opened on line 9).

  21 |           onKeyDown={(e) => e.key === "Enter" && onChange && onChange(n)}
     | This ends DreadMeter (opened on line 9).

  22 |         />
     | This closes a box of instructions that opened above.

  23 |       ))}
     | This ends DreadMeter (opened on line 9).

  24 |     </div>
     | This ends a drawing that DreadMeter started just above.

  25 |   );
     | This closes a box of instructions that opened above.

  26 | }
     | This ends DreadMeter (opened on line 9).

  27 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  28 | function PriorityBadge({ level }) {
     | This starts PriorityBadge. Shows task.aiPriority as High, Medium, or Low. Renders nothing if the server sent no level.

  29 |   if (!level) return null;
     | This asks a yes-or-no question. The next bit runs only on yes.

  30 |   const cls = level === "High" ? "badge-high" : level === "Medium" ? "badge-medium" : "badge-low";
     | This gives a short name to a value so the rest of PriorityBadge can use it.

  31 |   return <span className={`badge ${cls}`}>{level}</span>;
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  32 | }
     | This ends PriorityBadge (opened on line 28).

  33 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  34 | const SUGGESTION_STYLES = {
     | Left-border colors for AI suggestion types: priority, chunk, deadline, quick-win, nudge.

  35 |   priority:    { borderLeft: "3px solid var(--violet)", background: "var(--violet-dim)" },
     | This ends const SUGGESTION_STYLES = { (opened on line 34).

  36 |   chunk:       { borderLeft: "3px solid var(--green)",  background: "var(--green-dim)" },
     | This ends const SUGGESTION_STYLES = { (opened on line 34).

  37 |   deadline:    { borderLeft: "3px solid var(--red)",    background: "var(--red-dim)" },
     | This ends const SUGGESTION_STYLES = { (opened on line 34).

  38 |   "quick-win": { borderLeft: "3px solid var(--amber)",  background: "var(--amber-dim)" },
     | This ends const SUGGESTION_STYLES = { (opened on line 34).

  39 |   nudge:       { borderLeft: "3px solid var(--blue)",   background: "rgba(59,130,246,0.08)" },
     | This ends const SUGGESTION_STYLES = { (opened on line 34).

  40 | };
     | This ends const SUGGESTION_STYLES = { (opened on line 34).

  41 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  42 | const SUGGESTION_LABELS = {
     | Human labels for those suggestion types, shown above each card.

  43 |   priority:    "Priority",
     | Inside the top of the file, this line runs as written: priority:    "Priority",. It happens in order, after the line above it and before the line below it.

  44 |   chunk:       "Break Down",
     | Inside the top of the file, this line runs as written: chunk:       "Break Down",. It happens in order, after the line above it and before the line below it.

  45 |   deadline:    "Urgent",
     | Inside the top of the file, this line runs as written: deadline:    "Urgent",. It happens in order, after the line above it and before the line below it.

  46 |   "quick-win": "Quick Win",
     | Inside the top of the file, this line runs as written: "quick-win": "Quick Win",. It happens in order, after the line above it and before the line below it.

  47 |   nudge:       "Tip",
     | Inside the top of the file, this line runs as written: nudge:       "Tip",. It happens in order, after the line above it and before the line below it.

  48 | };
     | This ends const SUGGESTION_LABELS = { (opened on line 42).

  49 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  50 | // ── Simplified add-task row: one field, expand for details ───────────────
     | A note written for people. The app does not run it.

  51 | function AddTaskRow({ onAdd }) {
     | This starts AddTaskRow. One title field. Enter submits. Tab or '+ Details' reveals due date, minutes (default 30), and dread (default 3).

  52 |   const [title, setTitle] = useState("");
     | This gives a short name to a value so the rest of AddTaskRow can use it.

  53 |   const [expanded, setExpanded] = useState(false);
     | This gives a short name to a value so the rest of AddTaskRow can use it.

  54 |   const [due, setDue] = useState("");
     | This gives a short name to a value so the rest of AddTaskRow can use it.

  55 |   const [estimate, setEstimate] = useState(30);
     | This gives a short name to a value so the rest of AddTaskRow can use it.

  56 |   const [dreadScore, setDreadScore] = useState(3);
     | This gives a short name to a value so the rest of AddTaskRow can use it.

  57 |   const inputRef = useRef();
     | This gives a short name to a value so the rest of AddTaskRow can use it.

  58 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  59 |   async function submit() {
     | This starts submit. Calls the onAdd prop, then clears the form and focuses the title again.

  60 |     if (!title.trim()) return;
     | This asks a yes-or-no question. The next bit runs only on yes.

  61 |     await onAdd({ title: title.trim(), dueAt: due || null, estimateMins: Number(estimate), dreadScore: Number(dreadScore) });
     | This ends submit (opened on line 59).

  62 |     setTitle("");
     | Inside submit, this line runs as written: setTitle("");. It happens in order, after the line above it and before the line below it.

  63 |     setDue("");
     | Inside submit, this line runs as written: setDue("");. It happens in order, after the line above it and before the line below it.

  64 |     setEstimate(30);
     | Inside submit, this line runs as written: setEstimate(30);. It happens in order, after the line above it and before the line below it.

  65 |     setDreadScore(3);
     | Inside submit, this line runs as written: setDreadScore(3);. It happens in order, after the line above it and before the line below it.

  66 |     setExpanded(false);
     | Inside submit, this line runs as written: setExpanded(false);. It happens in order, after the line above it and before the line below it.

  67 |     inputRef.current?.focus();
     | Inside submit, this line runs as written: inputRef.current?.focus();. It happens in order, after the line above it and before the line below it.

  68 |   }
     | This ends submit (opened on line 59).

  69 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  70 |   return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  71 |     <div className="card card-sm add-task-row">
     | This draws one piece of the page while AddTaskRow is showing.

  72 |       <div className="flex gap-2">
     | This draws one piece of the page while AddTaskRow is showing.

  73 |         <input
     | This draws one piece of the page while AddTaskRow is showing.

  74 |           ref={inputRef}
     | This ends AddTaskRow (opened on line 51).

  75 |           className="input"
     | Inside AddTaskRow, this line runs as written: className="input". It happens in order, after the line above it and before the line below it.

  76 |           style={{ flex: 1 }}
     | This ends AddTaskRow (opened on line 51).

  77 |           placeholder="What do you need to do?"
     | Inside AddTaskRow, this line runs as written: placeholder="What do you need to do?". It happens in order, after the line above it and before the line below it.

  78 |           value={title}
     | This ends AddTaskRow (opened on line 51).

  79 |           onChange={(e) => {
     | Inside AddTaskRow, this line runs as written: onChange={(e) => {. It happens in order, after the line above it and before the line below it.

  80 |             setTitle(e.target.value);
     | Inside AddTaskRow, this line runs as written: setTitle(e.target.value);. It happens in order, after the line above it and before the line below it.

  81 |           }}
     | This ends onChange={(e) => { (opened on line 79).

  82 |           onKeyDown={(e) => {
     | Inside AddTaskRow, this line runs as written: onKeyDown={(e) => {. It happens in order, after the line above it and before the line below it.

  83 |             if (e.key === "Enter") submit();
     | This asks a yes-or-no question. The next bit runs only on yes.

  84 |             if (e.key === "Tab" && title.trim() && !expanded) { e.preventDefault(); setExpanded(true); }
     | This asks a yes-or-no question. The next bit runs only on yes.

  85 |           }}
     | This ends onKeyDown={(e) => { (opened on line 82).

  86 |           aria-label="New task title"
     | Inside AddTaskRow, this line runs as written: aria-label="New task title". It happens in order, after the line above it and before the line below it.

  87 |         />
     | This closes a box of instructions that opened above.

  88 |         {title.trim() && !expanded && (
     | Inside AddTaskRow, this line runs as written: {title.trim() && !expanded && (. It happens in order, after the line above it and before the line below it.

  89 |           <button
     | This draws one piece of the page while AddTaskRow is showing.

  90 |             className="btn btn-ghost btn-sm"
     | Inside AddTaskRow, this line runs as written: className="btn btn-ghost btn-sm". It happens in order, after the line above it and before the line below it.

  91 |             onClick={() => setExpanded(true)}
     | This decides what happens when you press.

  92 |             aria-label="Show more options"
     | Inside AddTaskRow, this line runs as written: aria-label="Show more options". It happens in order, after the line above it and before the line below it.

  93 |             title="Add details"
     | Inside AddTaskRow, this line runs as written: title="Add details". It happens in order, after the line above it and before the line below it.

  94 |           >
     | Inside AddTaskRow, this line runs as written: >. It happens in order, after the line above it and before the line below it.

  95 |             + Details
     | Inside AddTaskRow, this line runs as written: + Details. It happens in order, after the line above it and before the line below it.

  96 |           </button>
     | This ends a drawing that AddTaskRow started just above.

  97 |         )}
     | This ends AddTaskRow (opened on line 51).

  98 |         <button
     | This draws one piece of the page while AddTaskRow is showing.

  99 |           className="btn btn-primary"
     | Inside AddTaskRow, this line runs as written: className="btn btn-primary". It happens in order, after the line above it and before the line below it.

 100 |           onClick={submit}
     | This decides what happens when you press.

 101 |           disabled={!title.trim()}
     | This ends AddTaskRow (opened on line 51).

 102 |           aria-label="Add task"
     | Inside AddTaskRow, this line runs as written: aria-label="Add task". It happens in order, after the line above it and before the line below it.

 103 |           style={{ minWidth: 64 }}
     | This ends AddTaskRow (opened on line 51).

 104 |         >
     | Inside AddTaskRow, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 105 |           Add
     | Inside AddTaskRow, this line runs as written: Add. It happens in order, after the line above it and before the line below it.

 106 |         </button>
     | This ends a drawing that AddTaskRow started just above.

 107 |       </div>
     | This ends a drawing that AddTaskRow started just above.

 108 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 109 |       {expanded && (
     | Inside AddTaskRow, this line runs as written: {expanded && (. It happens in order, after the line above it and before the line below it.

 110 |         <div className="add-task-details">
     | This draws one piece of the page while AddTaskRow is showing.

 111 |           <div className="flex gap-2" style={{ flexWrap: "wrap" }}>
     | This draws one piece of the page while AddTaskRow is showing.

 112 |             <div style={{ flex: 1, minWidth: 160 }}>
     | This draws one piece of the page while AddTaskRow is showing.

 113 |               <label className="text-xs text-muted" style={{ display: "block", marginBottom: 4 }}>Due date</label>
     | This draws one piece of the page while AddTaskRow is showing.

 114 |               <input
     | This draws one piece of the page while AddTaskRow is showing.

 115 |                 className="input"
     | Inside AddTaskRow, this line runs as written: className="input". It happens in order, after the line above it and before the line below it.

 116 |                 type="datetime-local"
     | Inside AddTaskRow, this line runs as written: type="datetime-local". It happens in order, after the line above it and before the line below it.

 117 |                 value={due}
     | This ends AddTaskRow (opened on line 51).

 118 |                 onChange={(e) => setDue(e.target.value)}
     | This ends AddTaskRow (opened on line 51).

 119 |                 aria-label="Due date"
     | Inside AddTaskRow, this line runs as written: aria-label="Due date". It happens in order, after the line above it and before the line below it.

 120 |               />
     | This closes a box of instructions that opened above.

 121 |             </div>
     | This ends a drawing that AddTaskRow started just above.

 122 |             <div style={{ width: 100 }}>
     | This draws one piece of the page while AddTaskRow is showing.

 123 |               <label className="text-xs text-muted" style={{ display: "block", marginBottom: 4 }}>Minutes</label>
     | This draws one piece of the page while AddTaskRow is showing.

 124 |               <input
     | This draws one piece of the page while AddTaskRow is showing.

 125 |                 className="input"
     | Inside AddTaskRow, this line runs as written: className="input". It happens in order, after the line above it and before the line below it.

 126 |                 type="number"
     | Inside AddTaskRow, this line runs as written: type="number". It happens in order, after the line above it and before the line below it.

 127 |                 placeholder="30"
     | Inside AddTaskRow, this line runs as written: placeholder="30". It happens in order, after the line above it and before the line below it.

 128 |                 value={estimate}
     | This ends AddTaskRow (opened on line 51).

 129 |                 onChange={(e) => setEstimate(e.target.value)}
     | This ends AddTaskRow (opened on line 51).

 130 |                 min={1}
     | This ends AddTaskRow (opened on line 51).

 131 |                 aria-label="Estimated minutes"
     | Inside AddTaskRow, this line runs as written: aria-label="Estimated minutes". It happens in order, after the line above it and before the line below it.

 132 |               />
     | This closes a box of instructions that opened above.

 133 |             </div>
     | This ends a drawing that AddTaskRow started just above.

 134 |           </div>
     | This ends a drawing that AddTaskRow started just above.

 135 |           <div style={{ marginTop: 8 }}>
     | This draws one piece of the page while AddTaskRow is showing.

 136 |             <DreadMeter score={dreadScore} onChange={setDreadScore} />
     | This draws one piece of the page while AddTaskRow is showing.

 137 |           </div>
     | This ends a drawing that AddTaskRow started just above.

 138 |         </div>
     | This ends a drawing that AddTaskRow started just above.

 139 |       )}
     | This ends AddTaskRow (opened on line 51).

 140 |     </div>
     | This ends a drawing that AddTaskRow started just above.

 141 |   );
     | This closes a box of instructions that opened above.

 142 | }
     | This ends AddTaskRow (opened on line 51).

 143 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 144 | export default function TodoList() {
     | This starts TodoList. Open tasks, brain dump, and suggestion cards. Ranks tasks locally with scoreTask and also asks the server for AI suggestions.

 145 |   const { energy } = useEnergy();
     | Integer 1–5 from EnergyContext, persisted as bb-energy. Home refetches 'what next' when it changes. TodoList rescores and refetches suggestions.

 146 |   const [searchParams] = useSearchParams();
     | This gives a short name to a value so the rest of TodoList can use it.

 147 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 148 |   const [tasks, setTasks] = useState([]);
     | This gives a short name to a value so the rest of TodoList can use it.

 149 |   const [completing, setCompleting] = useState(null);
     | This gives a short name to a value so the rest of TodoList can use it.

 150 |   const [reward, setReward] = useState(null);
     | This gives a short name to a value so the rest of TodoList can use it.

 151 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 152 |   // Edit state
     | A note written for people. The app does not run it.

 153 |   const [editingId, setEditingId] = useState(null);
     | This gives a short name to a value so the rest of TodoList can use it.

 154 |   const [editTitle, setEditTitle] = useState("");
     | This gives a short name to a value so the rest of TodoList can use it.

 155 |   const [editDue, setEditDue] = useState("");
     | This gives a short name to a value so the rest of TodoList can use it.

 156 |   const [editEstimate, setEditEstimate] = useState(30);
     | This gives a short name to a value so the rest of TodoList can use it.

 157 |   const [editDread, setEditDread] = useState(3);
     | This gives a short name to a value so the rest of TodoList can use it.

 158 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 159 |   // Brain dump
     | A note written for people. The app does not run it.

 160 |   const [dumpText, setDumpText] = useState("");
     | This gives a short name to a value so the rest of TodoList can use it.

 161 |   const [dumpLoading, setDumpLoading] = useState(false);
     | This gives a short name to a value so the rest of TodoList can use it.

 162 |   const [view, setView] = useState(searchParams.get("tab") === "dump" ? "dump" : "tasks");
     | This gives a short name to a value so the rest of TodoList can use it.

 163 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 164 |   // AI suggestions
     | A note written for people. The app does not run it.

 165 |   const [suggestions, setSuggestions] = useState([]);
     | This gives a short name to a value so the rest of TodoList can use it.

 166 |   const [suggestionsLoading, setSuggestionsLoading] = useState(false);
     | This gives a short name to a value so the rest of TodoList can use it.

 167 |   const [dismissedIds, setDismissedIds] = useState(new Set());
     | This gives a short name to a value so the rest of TodoList can use it.

 168 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 169 |   useEffect(() => { load(); }, []);
     | This is an extra job that happens after the picture is drawn.

 170 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 171 |   useEffect(() => {
     | This is an extra job that happens after the picture is drawn.

 172 |     tasks.forEach((task) => {
     | Inside TodoList, this line runs as written: tasks.forEach((task) => {. It happens in order, after the line above it and before the line below it.

 173 |       if (task.dueAt && !task.completed) scheduleDeadline(task);
     | This asks a yes-or-no question. The next bit runs only on yes.

 174 |     });
     | This ends tasks.forEach((task) => { (opened on line 172).

 175 |     return () => { tasks.forEach((t) => clearDeadline(t._id)); };
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

 176 |   }, [tasks]);
     | This ends effect in TodoList (opened on line 171).

 177 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 178 |   useEffect(() => {
     | This is an extra job that happens after the picture is drawn.

 179 |     if (tasks.length > 0) fetchSuggestions();
     | This asks a yes-or-no question. The next bit runs only on yes.

 180 |     else setSuggestions([]);
     | Inside TodoList, this line runs as written: else setSuggestions([]);. It happens in order, after the line above it and before the line below it.

 181 |   }, [tasks.length, energy]);
     | This ends effect in TodoList (opened on line 178).

 182 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 183 |   async function load() {
     | This starts load. GET /tasks and, on the task page, keeps only tasks that are not completed. Calendar and the deadline page keep a wider set.

 184 |     try {
     | Inside load, this line runs as written: try {. It happens in order, after the line above it and before the line below it.

 185 |       const res = await api.get("/tasks");
     | This gives a short name to a value so the rest of load can use it.

 186 |       setTasks((res.tasks || []).filter((t) => !t.completed));
     | Inside load, this line runs as written: setTasks((res.tasks || []).filter((t) => !t.completed));. It happens in order, after the line above it and before the line below it.

 187 |     } catch { setTasks([]); }
     | This ends try { (opened on line 184).

 188 |   }
     | This ends load (opened on line 183).

 189 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 190 |   async function fetchSuggestions() {
     | This starts fetchSuggestions. GET /tasks/ai/suggestions and GET /recommendations/mindfulness in parallel. A mindfulness hit is inserted as a nudge card. Dismissed ids are filtered out.

 191 |     setSuggestionsLoading(true);
     | Inside fetchSuggestions, this line runs as written: setSuggestionsLoading(true);. It happens in order, after the line above it and before the line below it.

 192 |     try {
     | Inside fetchSuggestions, this line runs as written: try {. It happens in order, after the line above it and before the line below it.

 193 |       const [suggestRes, mindRes] = await Promise.allSettled([
     | This gives a short name to a value so the rest of fetchSuggestions can use it.

 194 |         api.get(`/tasks/ai/suggestions?energyLevel=${energy}`),
     | This asks the server (the office that keeps tasks and accounts) for something, or sends it something.

 195 |         api.get(`/recommendations/mindfulness?energyLevel=${energy}`),
     | This asks the server (the office that keeps tasks and accounts) for something, or sends it something.

 196 |       ]);
     | Inside fetchSuggestions, this line runs as written: ]);. It happens in order, after the line above it and before the line below it.

 197 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 198 |       if (suggestRes.status === "fulfilled") {
     | This asks a yes-or-no question. The next bit runs only on yes.

 199 |         const allSuggestions = suggestRes.value.suggestions || [];
     | This gives a short name to a value so the rest of fetchSuggestions can use it.

 200 |         if (mindRes.status === "fulfilled" && mindRes.value.suggested && mindRes.value.top) {
     | This asks a yes-or-no question. The next bit runs only on yes.

 201 |           const m = mindRes.value.top;
     | This gives a short name to a value so the rest of fetchSuggestions can use it.

 202 |           allSuggestions.unshift({
     | Inside fetchSuggestions, this line runs as written: allSuggestions.unshift({. It happens in order, after the line above it and before the line below it.

 203 |             id: "mindful_" + Date.now(),
     | Inside fetchSuggestions, this line runs as written: id: "mindful_" + Date.now(),. It happens in order, after the line above it and before the line below it.

 204 |             type: "nudge",
     | Inside fetchSuggestions, this line runs as written: type: "nudge",. It happens in order, after the line above it and before the line below it.

 205 |             title: `🧘 ${m.title}`,
     | This ends allSuggestions.unshift({ (opened on line 202).

 206 |             description: m.description,
     | Inside fetchSuggestions, this line runs as written: description: m.description,. It happens in order, after the line above it and before the line below it.

 207 |             action: "mindfulness",
     | Inside fetchSuggestions, this line runs as written: action: "mindfulness",. It happens in order, after the line above it and before the line below it.

 208 |           });
     | This ends allSuggestions.unshift({ (opened on line 202).

 209 |         }
     | This ends if (mindRes.status === "fulfilled" && mi (opened on line 200).

 210 |         const fresh = allSuggestions.filter((s) => !dismissedIds.has(s.id));
     | This gives a short name to a value so the rest of fetchSuggestions can use it.

 211 |         setSuggestions(fresh);
     | Inside fetchSuggestions, this line runs as written: setSuggestions(fresh);. It happens in order, after the line above it and before the line below it.

 212 |       } else {
     | This ends if (suggestRes.status === "fulfilled") { (opened on line 198).

 213 |         setSuggestions([]);
     | Inside fetchSuggestions, this line runs as written: setSuggestions([]);. It happens in order, after the line above it and before the line below it.

 214 |       }
     | This ends } else { (opened on line 212).

 215 |     } catch { setSuggestions([]); }
     | This ends try { (opened on line 192).

 216 |     finally { setSuggestionsLoading(false); }
     | This ends fetchSuggestions (opened on line 190).

 217 |   }
     | This ends fetchSuggestions (opened on line 190).

 218 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 219 |   async function add({ title, dueAt, estimateMins, dreadScore }) {
     | This starts add. POST /tasks. If the new task has a due date, schedule a notification and tell the user one was set.

 220 |     try {
     | Inside add, this line runs as written: try {. It happens in order, after the line above it and before the line below it.

 221 |       const res = await api.post("/tasks", { title, dueAt, estimateMins, dreadScore });
     | This gives a short name to a value so the rest of add can use it.

 222 |       const task = res.task;
     | This gives a short name to a value so the rest of add can use it.

 223 |       if (task?.dueAt) {
     | This asks a yes-or-no question. The next bit runs only on yes.

 224 |         scheduleDeadline(task);
     | Inside add, this line runs as written: scheduleDeadline(task);. It happens in order, after the line above it and before the line below it.

 225 |         notify("📅 Deadline set", `You'll be reminded when "${task.title}" is due.`);
     | This ends if (task?.dueAt) { (opened on line 223).

 226 |       }
     | This ends if (task?.dueAt) { (opened on line 223).

 227 |       load();
     | Inside add, this line runs as written: load();. It happens in order, after the line above it and before the line below it.

 228 |     } catch { alert("Could not add task"); }
     | This ends try { (opened on line 220).

 229 |   }
     | This ends add (opened on line 219).

 230 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 231 |   async function complete(id) {
     | This starts complete. Shows the check animation for 450ms, then PUT /tasks/:id/complete, clears the deadline timer, and reloads.

 232 |     setCompleting(id);
     | Inside complete, this line runs as written: setCompleting(id);. It happens in order, after the line above it and before the line below it.

 233 |     showReward("✅");
     | Inside complete, this line runs as written: showReward("✅");. It happens in order, after the line above it and before the line below it.

 234 |     setTimeout(async () => {
     | Inside complete, this line runs as written: setTimeout(async () => {. It happens in order, after the line above it and before the line below it.

 235 |       try {
     | Inside complete, this line runs as written: try {. It happens in order, after the line above it and before the line below it.

 236 |         await api.put(`/tasks/${id}/complete`, {});
     | This asks the server (the office that keeps tasks and accounts) for something, or sends it something.

 237 |         clearDeadline(id);
     | Inside complete, this line runs as written: clearDeadline(id);. It happens in order, after the line above it and before the line below it.

 238 |         notify("✅ Task completed", "Well done. One less thing to worry about.");
     | Inside complete, this line runs as written: notify("✅ Task completed", "Well done. One less thing to worry about.");. It happens in order, after the line above it and before the line below it.

 239 |         load();
     | Inside complete, this line runs as written: load();. It happens in order, after the line above it and before the line below it.

 240 |       } catch {}
     | This ends try { (opened on line 235).

 241 |       setCompleting(null);
     | Inside complete, this line runs as written: setCompleting(null);. It happens in order, after the line above it and before the line below it.

 242 |     }, 450);
     | This ends setTimeout(async () => { (opened on line 234).

 243 |   }
     | This ends complete (opened on line 231).

 244 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 245 |   async function autoChunk(t) {
     | This starts autoChunk. POST /tasks/:id/auto-chunk so the server splits the task into subtasks, then reloads.

 246 |     try {
     | Inside autoChunk, this line runs as written: try {. It happens in order, after the line above it and before the line below it.

 247 |       await api.post(`/tasks/${t._id}/auto-chunk`, {});
     | This asks the server (the office that keeps tasks and accounts) for something, or sends it something.

 248 |       load();
     | Inside autoChunk, this line runs as written: load();. It happens in order, after the line above it and before the line below it.

 249 |       notify("🧩 Chunked", `"${t.title}" has been broken into sub-tasks.`);
     | This ends try { (opened on line 246).

 250 |     } catch { alert("Chunk failed"); }
     | This ends try { (opened on line 246).

 251 |   }
     | This ends autoChunk (opened on line 245).

 252 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 253 |   async function saveEdit(id) {
     | This starts saveEdit. PUT /tasks/:id with the edit fields, closes the editor, reloads.

 254 |     try {
     | Inside saveEdit, this line runs as written: try {. It happens in order, after the line above it and before the line below it.

 255 |       await api.put(`/tasks/${id}`, {
     | This asks the server (the office that keeps tasks and accounts) for something, or sends it something.

 256 |         title: editTitle,
     | Inside saveEdit, this line runs as written: title: editTitle,. It happens in order, after the line above it and before the line below it.

 257 |         dueAt: editDue || null,
     | Inside saveEdit, this line runs as written: dueAt: editDue || null,. It happens in order, after the line above it and before the line below it.

 258 |         estimateMins: Number(editEstimate),
     | Inside saveEdit, this line runs as written: estimateMins: Number(editEstimate),. It happens in order, after the line above it and before the line below it.

 259 |         dreadScore: Number(editDread),
     | Inside saveEdit, this line runs as written: dreadScore: Number(editDread),. It happens in order, after the line above it and before the line below it.

 260 |       });
     | This ends await api.put(`/tasks/${id}`, { (opened on line 255).

 261 |       setEditingId(null);
     | Inside saveEdit, this line runs as written: setEditingId(null);. It happens in order, after the line above it and before the line below it.

 262 |       load();
     | Inside saveEdit, this line runs as written: load();. It happens in order, after the line above it and before the line below it.

 263 |     } catch { alert("Failed to update task"); }
     | This ends try { (opened on line 254).

 264 |   }
     | This ends saveEdit (opened on line 253).

 265 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 266 |   async function updateDread(id, score) {
     | This starts updateDread. PUT only dreadScore and patches that one task in state so the list does not reload.

 267 |     try {
     | Inside updateDread, this line runs as written: try {. It happens in order, after the line above it and before the line below it.

 268 |       await api.put(`/tasks/${id}`, { dreadScore: score });
     | This asks the server (the office that keeps tasks and accounts) for something, or sends it something.

 269 |       setTasks((prev) => prev.map((t) => t._id === id ? { ...t, dreadScore: score } : t));
     | This ends try { (opened on line 267).

 270 |     } catch {}
     | This ends try { (opened on line 267).

 271 |   }
     | This ends updateDread (opened on line 266).

 272 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 273 |   async function submitDump() {
     | This starts submitDump. POST /tasks/brain-dump with the text and current energy. Switches the view back to the list.

 274 |     if (!dumpText.trim()) return;
     | This asks a yes-or-no question. The next bit runs only on yes.

 275 |     setDumpLoading(true);
     | Inside submitDump, this line runs as written: setDumpLoading(true);. It happens in order, after the line above it and before the line below it.

 276 |     try {
     | Inside submitDump, this line runs as written: try {. It happens in order, after the line above it and before the line below it.

 277 |       const res = await api.post("/tasks/brain-dump", { text: dumpText, energyLevel: energy });
     | This gives a short name to a value so the rest of submitDump can use it.

 278 |       const count = res.tasks?.length || 0;
     | This gives a short name to a value so the rest of submitDump can use it.

 279 |       notify("🧠 Dumped!", `${count} task${count !== 1 ? "s" : ""} extracted.`);
     | This ends try { (opened on line 276).

 280 |       setDumpText("");
     | Inside submitDump, this line runs as written: setDumpText("");. It happens in order, after the line above it and before the line below it.

 281 |       setView("tasks");
     | Inside submitDump, this line runs as written: setView("tasks");. It happens in order, after the line above it and before the line below it.

 282 |       load();
     | Inside submitDump, this line runs as written: load();. It happens in order, after the line above it and before the line below it.

 283 |     } catch { alert("Brain dump failed"); }
     | This ends try { (opened on line 276).

 284 |     finally { setDumpLoading(false); }
     | This ends submitDump (opened on line 273).

 285 |   }
     | This ends submitDump (opened on line 273).

 286 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 287 |   function acceptSuggestion(s) {
     | This starts acceptSuggestion. Quick-win completes that task. Mindfulness navigates to /mindful. Prioritize scrolls to the task row. Then the card is removed.

 288 |     if (s.type === "quick-win" && s.taskId) {
     | This asks a yes-or-no question. The next bit runs only on yes.

 289 |       complete(s.taskId);
     | Inside acceptSuggestion, this line runs as written: complete(s.taskId);. It happens in order, after the line above it and before the line below it.

 290 |     } else if (s.action === "mindfulness") {
     | This ends if (s.type === "quick-win" && s.taskId)  (opened on line 288).

 291 |       window.location.href = "/mindful";
     | Inside acceptSuggestion, this line runs as written: window.location.href = "/mindful";. It happens in order, after the line above it and before the line below it.

 292 |       return;
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

 293 |     } else if (s.action === "prioritize" && s.taskId) {
     | This ends } else if (s.action === "mindfulness") { (opened on line 290).

 294 |       document.getElementById(`task-${s.taskId}`)?.scrollIntoView({ behavior: "smooth" });
     | This ends } else if (s.action === "prioritize" && s.taskId (opened on line 293).

 295 |     }
     | This ends } else if (s.action === "prioritize" && s.taskId (opened on line 293).

 296 |     setSuggestions((p) => p.filter((x) => x.id !== s.id));
     | Inside acceptSuggestion, this line runs as written: setSuggestions((p) => p.filter((x) => x.id !== s.id));. It happens in order, after the line above it and before the line below it.

 297 |     setDismissedIds((p) => new Set([...p, s.id]));
     | Inside acceptSuggestion, this line runs as written: setDismissedIds((p) => new Set([...p, s.id]));. It happens in order, after the line above it and before the line below it.

 298 |   }
     | This ends acceptSuggestion (opened on line 287).

 299 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 300 |   function dismissSuggestion(s) {
     | This starts dismissSuggestion. Removes the card and remembers the id so the next fetch does not bring it back.

 301 |     setSuggestions((p) => p.filter((x) => x.id !== s.id));
     | Inside dismissSuggestion, this line runs as written: setSuggestions((p) => p.filter((x) => x.id !== s.id));. It happens in order, after the line above it and before the line below it.

 302 |     setDismissedIds((p) => new Set([...p, s.id]));
     | Inside dismissSuggestion, this line runs as written: setDismissedIds((p) => new Set([...p, s.id]));. It happens in order, after the line above it and before the line below it.

 303 |   }
     | This ends dismissSuggestion (opened on line 300).

 304 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 305 |   function showReward(emoji) {
     | This starts showReward. Sets an emoji that a CSS burst shows, then clears it after 900ms.

 306 |     setReward(emoji);
     | Inside showReward, this line runs as written: setReward(emoji);. It happens in order, after the line above it and before the line below it.

 307 |     setTimeout(() => setReward(null), 900);
     | Inside showReward, this line runs as written: setTimeout(() => setReward(null), 900);. It happens in order, after the line above it and before the line below it.

 308 |   }
     | This ends showReward (opened on line 305).

 309 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 310 |   function fmtDue(d) {
     | This starts fmtDue. Overdue, 'due in Nh' under 24 hours, or a calendar date.

 311 |     if (!d) return "No due date";
     | This asks a yes-or-no question. The next bit runs only on yes.

 312 |     const dt = new Date(d);
     | This gives a short name to a value so the rest of fmtDue can use it.

 313 |     const now = new Date();
     | This gives a short name to a value so the rest of fmtDue can use it.

 314 |     const h = (dt - now) / 3600000;
     | This gives a short name to a value so the rest of fmtDue can use it.

 315 |     if (h < 0) return "Overdue!";
     | This asks a yes-or-no question. The next bit runs only on yes.

 316 |     if (h < 24) return `Due in ${Math.round(h)}h`;
     | This asks a yes-or-no question. The next bit runs only on yes.

 317 |     return dt.toLocaleDateString();
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

 318 |   }
     | This ends fmtDue (opened on line 310).

 319 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 320 |   function scoreTask(t) {
     | This starts scoreTask. One number per task. Bigger sorts first. urgency × energyMatch × dreadInverse × timeFit.

 321 |     const now = new Date();
     | This gives a short name to a value so the rest of scoreTask can use it.

 322 |     const hoursLeft = t.dueAt ? (new Date(t.dueAt) - now) / 3600000 : 168;
     | Hours until due. A task with no due date is treated as 168 hours away so it is not scored as urgent.

 323 |     const urgency = t.dueAt ? Math.exp(-Math.max(hoursLeft, 0) / 48) + 0.1 : 0.1;
     | Near 1 when the deadline is imminent, near 0.1 when it is far or missing. The exponential falls off over about two days (the 48).

 324 |     const taskDiff = Math.min((t.estimateMins || 30) / 120, 1);
     | How big the task is, estimate/120, capped at 1. A 30-minute task is 0.25; two hours or more is 1.

 325 |     const userE = energy / 5;
     | Your energy divided by 5, so level 1 is 0.2 and level 5 is 1. Compared with taskDiff.

 326 |     const energyMatch = 1 - Math.abs(taskDiff - userE) * 0.5;
     | 1 when the task size matches your energy, lower when they differ. The 0.5 stops a mismatch from zeroing the score.

 327 |     const dreadInverse = 1 - ((t.dreadScore || 3) - 1) / 8;
     | Higher when dread is low, so an easy-feeling task ranks a bit higher. Dread 1 → 1, dread 5 → 0.5.

 328 |     const timeFit = (t.estimateMins || 30) <= 45 ? 1.2 : 0.9;
     | 1.2 if the estimate is 45 minutes or less, otherwise 0.9. Short tasks are easier to start.

 329 |     return urgency * energyMatch * dreadInverse * timeFit;
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

 330 |   }
     | This ends scoreTask (opened on line 320).

 331 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 332 |   const sortedTasks = [...tasks].sort((a, b) => scoreTask(b) - scoreTask(a));
     | A copy of the open tasks sorted by scoreTask, highest first. Index 0 is the row that gets the Next badge.

 333 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 334 |   return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

 335 |     <div>
     | This draws one piece of the page while TodoList is showing.

 336 |       {reward && <div className="reward-burst">{reward}</div>}
     | This ends TodoList (opened on line 144).

 337 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 338 |       <div className="flex items-center justify-between mb-4" style={{ flexWrap: "wrap", gap: 12 }}>
     | This draws one piece of the page while TodoList is showing.

 339 |         <div>
     | This draws one piece of the page while TodoList is showing.

 340 |           <h1 className="page-title">Tasks</h1>
     | This draws one piece of the page while TodoList is showing.

 341 |           <p className="page-subtitle" style={{ margin: 0 }}>Brain dump, chunk, and conquer</p>
     | This draws one piece of the page while TodoList is showing.

 342 |         </div>
     | This ends a drawing that TodoList started just above.

 343 |         <div className="mode-tabs" style={{ margin: 0, width: "auto", flexShrink: 0 }}>
     | This draws one piece of the page while TodoList is showing.

 344 |           <button
     | This draws one piece of the page while TodoList is showing.

 345 |             className={`mode-tab ${view === "tasks" ? "active" : ""}`}
     | This ends TodoList (opened on line 144).

 346 |             onClick={() => setView("tasks")}
     | This decides what happens when you press.

 347 |             aria-pressed={view === "tasks"}
     | This ends TodoList (opened on line 144).

 348 |           >
     | Inside TodoList, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 349 |             📋 Task List
     | Inside TodoList, this line runs as written: 📋 Task List. It happens in order, after the line above it and before the line below it.

 350 |           </button>
     | This ends a drawing that TodoList started just above.

 351 |           <button
     | This draws one piece of the page while TodoList is showing.

 352 |             className={`mode-tab ${view === "dump" ? "active" : ""}`}
     | This ends TodoList (opened on line 144).

 353 |             onClick={() => setView("dump")}
     | This decides what happens when you press.

 354 |             aria-pressed={view === "dump"}
     | This ends TodoList (opened on line 144).

 355 |           >
     | Inside TodoList, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 356 |             🧠 Brain Dump
     | Inside TodoList, this line runs as written: 🧠 Brain Dump. It happens in order, after the line above it and before the line below it.

 357 |           </button>
     | This ends a drawing that TodoList started just above.

 358 |         </div>
     | This ends a drawing that TodoList started just above.

 359 |       </div>
     | This ends a drawing that TodoList started just above.

 360 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 361 |       <div className="grid-main">
     | This draws one piece of the page while TodoList is showing.

 362 |         {/* ── Left Panel ────────────────────────────────── */}
     | This ends TodoList (opened on line 144).

 363 |         <div className="stack">
     | This draws one piece of the page while TodoList is showing.

 364 |           {view === "dump" ? (
     | Inside TodoList, this line runs as written: {view === "dump" ? (. It happens in order, after the line above it and before the line below it.

 365 |             <div className="card">
     | This draws one piece of the page while TodoList is showing.

 366 |               <div className="card-title">Brain Dump</div>
     | This draws one piece of the page while TodoList is showing.

 367 |               <p className="text-sm text-muted mb-3">
     | This draws one piece of the page while TodoList is showing.

 368 |                 Type anything — thoughts, tasks, worries. AI will parse it into structured tasks.
     | Inside TodoList, this line runs as written: Type anything — thoughts, tasks, worries. AI will parse it into structured tasks.. It happens in order, after the line above it and before the line below it.

 369 |               </p>
     | This ends a drawing that TodoList started just above.

 370 |               <div className="brain-dump-wrap mb-3">
     | This draws one piece of the page while TodoList is showing.

 371 |                 <textarea
     | This draws one piece of the page while TodoList is showing.

 372 |                   className="textarea"
     | Inside TodoList, this line runs as written: className="textarea". It happens in order, after the line above it and before the line below it.

 373 |                   style={{ minHeight: 160 }}
     | This ends TodoList (opened on line 144).

 374 |                   placeholder="Just type whatever's in your head...&#10;&#10;e.g. Need to finish the report by Friday, call the dentist, study chapter 4 before the exam next week, also reply to Sara's email..."
     | Inside TodoList, this line runs as written: placeholder="Just type whatever's in your head...&#10;&#10;e.g. Need to finish the report by Friday, call the dentist, study chapter 4 befor. It happens in order, after the line above it and before the line below it.

 375 |                   value={dumpText}
     | This ends TodoList (opened on line 144).

 376 |                   onChange={(e) => setDumpText(e.target.value)}
     | This ends TodoList (opened on line 144).

 377 |                   onKeyDown={(e) => { if (e.key === "Enter" && e.ctrlKey) submitDump(); }}
     | This ends TodoList (opened on line 144).

 378 |                   aria-label="Brain dump text"
     | Inside TodoList, this line runs as written: aria-label="Brain dump text". It happens in order, after the line above it and before the line below it.

 379 |                 />
     | This closes a box of instructions that opened above.

 380 |                 <div className="brain-dump-hint">Ctrl+Enter to submit</div>
     | This draws one piece of the page while TodoList is showing.

 381 |               </div>
     | This ends a drawing that TodoList started just above.

 382 |               <div style={{ display: "flex", gap: 8 }}>
     | This draws one piece of the page while TodoList is showing.

 383 |                 <button
     | This draws one piece of the page while TodoList is showing.

 384 |                   className="btn btn-primary"
     | Inside TodoList, this line runs as written: className="btn btn-primary". It happens in order, after the line above it and before the line below it.

 385 |                   onClick={submitDump}
     | This decides what happens when you press.

 386 |                   disabled={dumpLoading || !dumpText.trim()}
     | This ends TodoList (opened on line 144).

 387 |                 >
     | Inside TodoList, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 388 |                   {dumpLoading ? "⏳ Parsing..." : "🧠 Chunk with AI"}
     | This ends TodoList (opened on line 144).

 389 |                 </button>
     | This ends a drawing that TodoList started just above.

 390 |                 <button className="btn btn-ghost" onClick={() => setDumpText("")}>
     | This draws one piece of the page while TodoList is showing.

 391 |                   Clear
     | Inside TodoList, this line runs as written: Clear. It happens in order, after the line above it and before the line below it.

 392 |                 </button>
     | This ends a drawing that TodoList started just above.

 393 |               </div>
     | This ends a drawing that TodoList started just above.

 394 |             </div>
     | This ends a drawing that TodoList started just above.

 395 |           ) : (
     | This closes a box of instructions that opened above.

 396 |             <>
     | This draws one piece of the page while TodoList is showing.

 397 |               {/* Simplified single-field add task */}
     | This ends TodoList (opened on line 144).

 398 |               <AddTaskRow onAdd={add} />
     | This draws one piece of the page while TodoList is showing.

 399 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 400 |               {/* Task list */}
     | This ends TodoList (opened on line 144).

 401 |               <div className="stack-sm">
     | This draws one piece of the page while TodoList is showing.

 402 |                 {sortedTasks.map((t, idx) => (
     | Inside TodoList, this line runs as written: {sortedTasks.map((t, idx) => (. It happens in order, after the line above it and before the line below it.

 403 |                   <div
     | This draws one piece of the page while TodoList is showing.

 404 |                     key={t._id}
     | This ends TodoList (opened on line 144).

 405 |                     id={`task-${t._id}`}
     | This ends TodoList (opened on line 144).

 406 |                     className={`task-card ${completing === t._id ? "completing" : ""}`}
     | This ends TodoList (opened on line 144).

 407 |                   >
     | Inside TodoList, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 408 |                     {editingId === t._id ? (
     | Inside TodoList, this line runs as written: {editingId === t._id ? (. It happens in order, after the line above it and before the line below it.

 409 |                       <div className="stack-sm">
     | This draws one piece of the page while TodoList is showing.

 410 |                         <div>
     | This draws one piece of the page while TodoList is showing.

 411 |                           <label className="text-xs text-muted" style={{ display: "block", marginBottom: 4 }}>Task title</label>
     | This draws one piece of the page while TodoList is showing.

 412 |                           <input
     | This draws one piece of the page while TodoList is showing.

 413 |                             className="input"
     | Inside TodoList, this line runs as written: className="input". It happens in order, after the line above it and before the line below it.

 414 |                             value={editTitle}
     | This ends TodoList (opened on line 144).

 415 |                             onChange={(e) => setEditTitle(e.target.value)}
     | This ends TodoList (opened on line 144).

 416 |                             aria-label="Edit task title"
     | Inside TodoList, this line runs as written: aria-label="Edit task title". It happens in order, after the line above it and before the line below it.

 417 |                           />
     | This closes a box of instructions that opened above.

 418 |                         </div>
     | This ends a drawing that TodoList started just above.

 419 |                         <div>
     | This draws one piece of the page while TodoList is showing.

 420 |                           <label className="text-xs text-muted" style={{ display: "block", marginBottom: 4 }}>Due date</label>
     | This draws one piece of the page while TodoList is showing.

 421 |                           <input
     | This draws one piece of the page while TodoList is showing.

 422 |                             className="input"
     | Inside TodoList, this line runs as written: className="input". It happens in order, after the line above it and before the line below it.

 423 |                             type="datetime-local"
     | Inside TodoList, this line runs as written: type="datetime-local". It happens in order, after the line above it and before the line below it.

 424 |                             value={editDue}
     | This ends TodoList (opened on line 144).

 425 |                             onChange={(e) => setEditDue(e.target.value)}
     | This ends TodoList (opened on line 144).

 426 |                             aria-label="Edit due date"
     | Inside TodoList, this line runs as written: aria-label="Edit due date". It happens in order, after the line above it and before the line below it.

 427 |                           />
     | This closes a box of instructions that opened above.

 428 |                         </div>
     | This ends a drawing that TodoList started just above.

 429 |                         <div>
     | This draws one piece of the page while TodoList is showing.

 430 |                           <label className="text-xs text-muted" style={{ display: "block", marginBottom: 4 }}>Estimated minutes</label>
     | This draws one piece of the page while TodoList is showing.

 431 |                           <input
     | This draws one piece of the page while TodoList is showing.

 432 |                             className="input"
     | Inside TodoList, this line runs as written: className="input". It happens in order, after the line above it and before the line below it.

 433 |                             type="number"
     | Inside TodoList, this line runs as written: type="number". It happens in order, after the line above it and before the line below it.

 434 |                             value={editEstimate}
     | This ends TodoList (opened on line 144).

 435 |                             onChange={(e) => setEditEstimate(e.target.value)}
     | This ends TodoList (opened on line 144).

 436 |                             min={1}
     | This ends TodoList (opened on line 144).

 437 |                             aria-label="Edit estimated minutes"
     | Inside TodoList, this line runs as written: aria-label="Edit estimated minutes". It happens in order, after the line above it and before the line below it.

 438 |                           />
     | This closes a box of instructions that opened above.

 439 |                         </div>
     | This ends a drawing that TodoList started just above.

 440 |                         <DreadMeter score={editDread} onChange={setEditDread} />
     | This draws one piece of the page while TodoList is showing.

 441 |                         <div className="flex gap-2">
     | This draws one piece of the page while TodoList is showing.

 442 |                           <button className="btn btn-primary btn-sm" onClick={() => saveEdit(t._id)}>Save</button>
     | This draws one piece of the page while TodoList is showing.

 443 |                           <button className="btn btn-ghost btn-sm" onClick={() => setEditingId(null)}>Cancel</button>
     | This draws one piece of the page while TodoList is showing.

 444 |                         </div>
     | This ends a drawing that TodoList started just above.

 445 |                       </div>
     | This ends a drawing that TodoList started just above.

 446 |                     ) : (
     | This closes a box of instructions that opened above.

 447 |                       <>
     | This draws one piece of the page while TodoList is showing.

 448 |                         <div className="task-header">
     | This draws one piece of the page while TodoList is showing.

 449 |                           <button
     | This draws one piece of the page while TodoList is showing.

 450 |                             className="task-check"
     | Inside TodoList, this line runs as written: className="task-check". It happens in order, after the line above it and before the line below it.

 451 |                             onClick={() => complete(t._id)}
     | This decides what happens when you press.

 452 |                             title="Mark complete"
     | Inside TodoList, this line runs as written: title="Mark complete". It happens in order, after the line above it and before the line below it.

 453 |                             aria-label={`Complete: ${t.title}`}
     | This ends TodoList (opened on line 144).

 454 |                           >
     | Inside TodoList, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 455 |                             ✓
     | Inside TodoList, this line runs as written: ✓. It happens in order, after the line above it and before the line below it.

 456 |                           </button>
     | This ends a drawing that TodoList started just above.

 457 |                           <div className="task-title-text">
     | This draws one piece of the page while TodoList is showing.

 458 |                             {idx === 0 && (
     | Inside TodoList, this line runs as written: {idx === 0 && (. It happens in order, after the line above it and before the line below it.

 459 |                               <span className="badge badge-violet" style={{ marginRight: 6, verticalAlign: "middle" }}>
     | This draws one piece of the page while TodoList is showing.

 460 |                                 ⚡ Next
     | Inside TodoList, this line runs as written: ⚡ Next. It happens in order, after the line above it and before the line below it.

 461 |                               </span>
     | This ends a drawing that TodoList started just above.

 462 |                             )}
     | This ends TodoList (opened on line 144).

 463 |                             {t.title}
     | This ends TodoList (opened on line 144).

 464 |                           </div>
     | This ends a drawing that TodoList started just above.

 465 |                           <PriorityBadge level={t.aiPriority} />
     | This draws one piece of the page while TodoList is showing.

 466 |                         </div>
     | This ends a drawing that TodoList started just above.

 467 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 468 |                         <div className="task-meta">
     | This draws one piece of the page while TodoList is showing.

 469 |                           {t.dueAt && (
     | Inside TodoList, this line runs as written: {t.dueAt && (. It happens in order, after the line above it and before the line below it.

 470 |                             <span style={{ color: (new Date(t.dueAt) - new Date()) / 3600000 < 24 ? "var(--red)" : "var(--muted)" }}>
     | This draws one piece of the page while TodoList is showing.

 471 |                               📅 {fmtDue(t.dueAt)}
     | This ends TodoList (opened on line 144).

 472 |                             </span>
     | This ends a drawing that TodoList started just above.

 473 |                           )}
     | This ends TodoList (opened on line 144).

 474 |                           {t.estimateMins && <span>⏱ ~{t.estimateMins}m</span>}
     | This ends TodoList (opened on line 144).

 475 |                           <DreadMeter score={t.dreadScore || 3} onChange={(n) => updateDread(t._id, n)} />
     | This draws one piece of the page while TodoList is showing.

 476 |                         </div>
     | This ends a drawing that TodoList started just above.

 477 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 478 |                         {t.subtasks?.length > 0 && (
     | Inside TodoList, this line runs as written: {t.subtasks?.length > 0 && (. It happens in order, after the line above it and before the line below it.

 479 |                           <div className="subtask-list">
     | This draws one piece of the page while TodoList is showing.

 480 |                             {t.subtasks.map((s, i) => (
     | Inside TodoList, this line runs as written: {t.subtasks.map((s, i) => (. It happens in order, after the line above it and before the line below it.

 481 |                               <div key={i} className="subtask-item">
     | This draws one piece of the page while TodoList is showing.

 482 |                                 <div className="subtask-dot" />
     | This draws one piece of the page while TodoList is showing.

 483 |                                 {s.title}
     | This ends TodoList (opened on line 144).

 484 |                               </div>
     | This ends a drawing that TodoList started just above.

 485 |                             ))}
     | This ends TodoList (opened on line 144).

 486 |                           </div>
     | This ends a drawing that TodoList started just above.

 487 |                         )}
     | This ends TodoList (opened on line 144).

 488 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 489 |                         <div className="task-actions">
     | This draws one piece of the page while TodoList is showing.

 490 |                           <button className="btn btn-success btn-sm" onClick={() => complete(t._id)}>✓ Done</button>
     | This draws one piece of the page while TodoList is showing.

 491 |                           <button className="btn btn-secondary btn-sm" onClick={() => autoChunk(t)}>✂ Chunk</button>
     | This draws one piece of the page while TodoList is showing.

 492 |                           <button
     | This draws one piece of the page while TodoList is showing.

 493 |                             className="btn btn-ghost btn-sm"
     | Inside TodoList, this line runs as written: className="btn btn-ghost btn-sm". It happens in order, after the line above it and before the line below it.

 494 |                             onClick={() => {
     | This decides what happens when you press.

 495 |                               setEditingId(t._id);
     | Inside TodoList, this line runs as written: setEditingId(t._id);. It happens in order, after the line above it and before the line below it.

 496 |                               setEditTitle(t.title);
     | Inside TodoList, this line runs as written: setEditTitle(t.title);. It happens in order, after the line above it and before the line below it.

 497 |                               setEditDue(t.dueAt ? t.dueAt.slice(0, 16) : "");
     | Inside TodoList, this line runs as written: setEditDue(t.dueAt ? t.dueAt.slice(0, 16) : "");. It happens in order, after the line above it and before the line below it.

 498 |                               setEditEstimate(t.estimateMins || 30);
     | Inside TodoList, this line runs as written: setEditEstimate(t.estimateMins || 30);. It happens in order, after the line above it and before the line below it.

 499 |                               setEditDread(t.dreadScore || 3);
     | Inside TodoList, this line runs as written: setEditDread(t.dreadScore || 3);. It happens in order, after the line above it and before the line below it.

 500 |                             }}
     | This ends onClick={() => { (opened on line 494).

 501 |                           >
     | Inside TodoList, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 502 |                             ✎ Edit
     | Inside TodoList, this line runs as written: ✎ Edit. It happens in order, after the line above it and before the line below it.

 503 |                           </button>
     | This ends a drawing that TodoList started just above.

 504 |                         </div>
     | This ends a drawing that TodoList started just above.

 505 |                       </>
     | This ends a drawing that TodoList started just above.

 506 |                     )}
     | This ends TodoList (opened on line 144).

 507 |                   </div>
     | This ends a drawing that TodoList started just above.

 508 |                 ))}
     | This ends TodoList (opened on line 144).

 509 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 510 |                 {/* Empty state with direct CTA */}
     | This ends TodoList (opened on line 144).

 511 |                 {tasks.length === 0 && (
     | Inside TodoList, this line runs as written: {tasks.length === 0 && (. It happens in order, after the line above it and before the line below it.

 512 |                   <div className="empty-state">
     | This draws one piece of the page while TodoList is showing.

 513 |                     <div className="empty-state-icon">📭</div>
     | This draws one piece of the page while TodoList is showing.

 514 |                     <div className="empty-state-title">No tasks yet</div>
     | This draws one piece of the page while TodoList is showing.

 515 |                     <div className="empty-state-body">
     | This draws one piece of the page while TodoList is showing.

 516 |                       Try the Brain Dump — type everything on your mind and AI will turn it into tasks.
     | Inside TodoList, this line runs as written: Try the Brain Dump — type everything on your mind and AI will turn it into tasks.. It happens in order, after the line above it and before the line below it.

 517 |                     </div>
     | This ends a drawing that TodoList started just above.

 518 |                     <button className="btn btn-primary" onClick={() => setView("dump")}>
     | This draws one piece of the page while TodoList is showing.

 519 |                       🧠 Start Brain Dump
     | Inside TodoList, this line runs as written: 🧠 Start Brain Dump. It happens in order, after the line above it and before the line below it.

 520 |                     </button>
     | This ends a drawing that TodoList started just above.

 521 |                   </div>
     | This ends a drawing that TodoList started just above.

 522 |                 )}
     | This ends TodoList (opened on line 144).

 523 |               </div>
     | This ends a drawing that TodoList started just above.

 524 |             </>
     | This ends a drawing that TodoList started just above.

 525 |           )}
     | This ends TodoList (opened on line 144).

 526 |         </div>
     | This ends a drawing that TodoList started just above.

 527 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 528 |         {/* ── Right Panel: AI Suggestions ──────────────── */}
     | This ends TodoList (opened on line 144).

 529 |         <aside className="stack">
     | This draws one piece of the page while TodoList is showing.

 530 |           <div className="card">
     | This draws one piece of the page while TodoList is showing.

 531 |             <div className="flex items-center justify-between mb-3">
     | This draws one piece of the page while TodoList is showing.

 532 |               <div className="card-title" style={{ margin: 0 }}>AI Suggestions</div>
     | This draws one piece of the page while TodoList is showing.

 533 |               <button
     | This draws one piece of the page while TodoList is showing.

 534 |                 className="btn btn-ghost btn-sm"
     | Inside TodoList, this line runs as written: className="btn btn-ghost btn-sm". It happens in order, after the line above it and before the line below it.

 535 |                 onClick={fetchSuggestions}
     | This decides what happens when you press.

 536 |                 disabled={suggestionsLoading}
     | This ends TodoList (opened on line 144).

 537 |                 aria-label="Refresh suggestions"
     | Inside TodoList, this line runs as written: aria-label="Refresh suggestions". It happens in order, after the line above it and before the line below it.

 538 |               >
     | Inside TodoList, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 539 |                 {suggestionsLoading ? "..." : "↺"}
     | This ends TodoList (opened on line 144).

 540 |               </button>
     | This ends a drawing that TodoList started just above.

 541 |             </div>
     | This ends a drawing that TodoList started just above.

 542 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 543 |             {suggestionsLoading && suggestions.length === 0 && (
     | Inside TodoList, this line runs as written: {suggestionsLoading && suggestions.length === 0 && (. It happens in order, after the line above it and before the line below it.

 544 |               <div className="text-sm text-muted" style={{ textAlign: "center", padding: 20 }}>
     | This draws one piece of the page while TodoList is showing.

 545 |                 Analysing tasks...
     | Inside TodoList, this line runs as written: Analysing tasks.... It happens in order, after the line above it and before the line below it.

 546 |               </div>
     | This ends a drawing that TodoList started just above.

 547 |             )}
     | This ends TodoList (opened on line 144).

 548 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 549 |             {suggestions.length > 0 ? (
     | Inside TodoList, this line runs as written: {suggestions.length > 0 ? (. It happens in order, after the line above it and before the line below it.

 550 |               <div className="stack-sm">
     | This draws one piece of the page while TodoList is showing.

 551 |                 {suggestions.map((s) => (
     | Inside TodoList, this line runs as written: {suggestions.map((s) => (. It happens in order, after the line above it and before the line below it.

 552 |                   <div
     | This draws one piece of the page while TodoList is showing.

 553 |                     key={s.id}
     | This ends TodoList (opened on line 144).

 554 |                     style={{ borderRadius: "var(--radius-sm)", padding: "12px 14px", ...SUGGESTION_STYLES[s.type] }}
     | This ends TodoList (opened on line 144).

 555 |                   >
     | Inside TodoList, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 556 |                     <div className="text-xs font-bold" style={{ textTransform: "uppercase", letterSpacing: "0.5px", color: "var(--muted)", marginBottom: 4 }}>
     | This draws one piece of the page while TodoList is showing.

 557 |                       {SUGGESTION_LABELS[s.type] || "Tip"}
     | This ends TodoList (opened on line 144).

 558 |                     </div>
     | This ends a drawing that TodoList started just above.

 559 |                     <div className="font-semibold text-sm mb-1">{s.title}</div>
     | This draws one piece of the page while TodoList is showing.

 560 |                     <div className="text-sm text-muted mb-3" style={{ lineHeight: 1.5 }}>{s.description}</div>
     | This draws one piece of the page while TodoList is showing.

 561 |                     <div className="flex gap-2">
     | This draws one piece of the page while TodoList is showing.

 562 |                       <button className="btn btn-primary btn-sm" onClick={() => acceptSuggestion(s)}>Accept</button>
     | This draws one piece of the page while TodoList is showing.

 563 |                       <button className="btn btn-ghost btn-sm" onClick={() => dismissSuggestion(s)}>Dismiss</button>
     | This draws one piece of the page while TodoList is showing.

 564 |                     </div>
     | This ends a drawing that TodoList started just above.

 565 |                   </div>
     | This ends a drawing that TodoList started just above.

 566 |                 ))}
     | This ends TodoList (opened on line 144).

 567 |               </div>
     | This ends a drawing that TodoList started just above.

 568 |             ) : (
     | This closes a box of instructions that opened above.

 569 |               !suggestionsLoading && (
     | Inside TodoList, this line runs as written: !suggestionsLoading && (. It happens in order, after the line above it and before the line below it.

 570 |                 /* Empty suggestions state — don't send users elsewhere */
     | A note for people. The app skips this line.

 571 |                 <div className="empty-state" style={{ padding: "16px 0" }}>
     | This draws one piece of the page while TodoList is showing.

 572 |                   <div style={{ fontSize: 28, marginBottom: 8 }}>✨</div>
     | This draws one piece of the page while TodoList is showing.

 573 |                   <div className="text-sm text-muted" style={{ textAlign: "center", lineHeight: 1.6 }}>
     | This draws one piece of the page while TodoList is showing.

 574 |                     {tasks.length === 0
     | Inside TodoList, this line runs as written: {tasks.length === 0. It happens in order, after the line above it and before the line below it.

 575 |                       ? "Add your first task to get AI-powered suggestions."
     | Inside TodoList, this line runs as written: ? "Add your first task to get AI-powered suggestions.". It happens in order, after the line above it and before the line below it.

 576 |                       : "You're all caught up. Keep going!"}
     | This ends TodoList (opened on line 144).

 577 |                   </div>
     | This ends a drawing that TodoList started just above.

 578 |                 </div>
     | This ends a drawing that TodoList started just above.

 579 |               )
     | This closes a box of instructions that opened above.

 580 |             )}
     | This ends TodoList (opened on line 144).

 581 |           </div>
     | This ends a drawing that TodoList started just above.

 582 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 583 |           <div className="card card-sm">
     | This draws one piece of the page while TodoList is showing.

 584 |             <div className="card-title">Energy context</div>
     | This draws one piece of the page while TodoList is showing.

 585 |             <div className="text-sm text-muted" style={{ lineHeight: 1.6 }}>
     | This draws one piece of the page while TodoList is showing.

 586 |               Tasks are ranked for your current energy.{" "}
     | This ends TodoList (opened on line 144).

 587 |               <span style={{ color: "var(--amber)" }}>⚡ Next</span> shows your best match.
     | This draws one piece of the page while TodoList is showing.

 588 |             </div>
     | This ends a drawing that TodoList started just above.

 589 |           </div>
     | This ends a drawing that TodoList started just above.

 590 |         </aside>
     | This ends a drawing that TodoList started just above.

 591 |       </div>
     | This ends a drawing that TodoList started just above.

 592 |     </div>
     | This ends a drawing that TodoList started just above.

 593 |   );
     | This closes a box of instructions that opened above.

 594 | }
     | This ends TodoList (opened on line 144).

