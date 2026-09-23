# `src/components/TodoList.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import { useEffect, useRef, useState } from "react";
     | Import for the task list, brain dump, and AI suggestion cards: `import { useEffect, useRef, useState } from "react";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   2 | import { useSearchParams } from "react-router-dom";
     | Import for the task list, brain dump, and AI suggestion cards: `import { useSearchParams } from "react-router-dom";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   3 | import api from "../services/api";
     | Import for the task list, brain dump, and AI suggestion cards: `import api from "../services/api";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   4 | import { notify } from "../utils/notify";
     | Import for the task list, brain dump, and AI suggestion cards: `import { notify } from "../utils/notify";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   5 | import { scheduleDeadline, clearDeadline } from "../utils/deadlineScheduler";
     | Import for the task list, brain dump, and AI suggestion cards: `import { scheduleDeadline, clearDeadline } from "../utils/deadlineScheduler";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   6 | import { useEnergy } from "../contexts/EnergyContext";
     | Import for the task list, brain dump, and AI suggestion cards: `import { useEnergy } from "../contexts/EnergyContext";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   7 | 
     | Blank line in `src/components/TodoList.jsx` (the task list, brain dump, and AI suggestion cards), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   8 | // ── Dread pip colours ────────────────────────────────────────────────────
     | Comment inside the top of the file. Not executed. It documents the next code: ── Dread pip colours ────────────────────────────────────────────────────

   9 | function DreadMeter({ score, onChange }) {
     | Defines `DreadMeter` in the task list, brain dump, and AI suggestion cards. Five pips. Click or Enter calls onChange with 1–5. Add-task, edit, and each row all use it.

  10 |   return (
     | In `DreadMeter` (src/components/TodoList.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  11 |     <div className="dread-meter" title={`Dread: ${score}/5`} role="group" aria-label={`Dread score ${score} of 5`}>
     | In `DreadMeter` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="dread-meter" title={`Dread: ${score}/5`} role="group" aria-label={`Dread score ${score} of 5`}>`

  12 |       <span className="text-xs text-muted" style={{ marginRight: 4 }}>Dread</span>
     | In `DreadMeter` (src/components/TodoList.jsx): Opens it. An inline box. Source: `<span className="text-xs text-muted" style={{ marginRight: 4 }}>Dread</span>`

  13 |       {[1, 2, 3, 4, 5].map((n) => (
     | In `DreadMeter` (src/components/TodoList.jsx): iteration `{[1, 2, 3, 4, 5].map((n) => (`.

  14 |         <div
     | In `DreadMeter` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div`

  15 |           key={n}
     | In `DreadMeter` (src/components/TodoList.jsx): `key={n}` closes DreadMeter (opened on line 9). Names declared inside that block end here.

  16 |           className={`dread-pip ${n <= score ? `active-${score}` : ""}`}
     | In `DreadMeter` (src/components/TodoList.jsx): `className={`dread-pip ${n <= score ? `active-${score}` : ""}`}` closes DreadMeter (opened on line 9). Names declared inside that block end here.

  17 |           onClick={() => onChange && onChange(n)}
     | In `DreadMeter` (src/components/TodoList.jsx): event prop `onClick={() => onChange && onChange(n)}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

  18 |           role="button"
     | In `DreadMeter` (src/components/TodoList.jsx): statement `role="button"`. It runs when DreadMeter runs, in order, before the next line of the same function.

  19 |           tabIndex={0}
     | In `DreadMeter` (src/components/TodoList.jsx): `tabIndex={0}` closes DreadMeter (opened on line 9). Names declared inside that block end here.

  20 |           aria-label={`Dread level ${n}`}
     | In `DreadMeter` (src/components/TodoList.jsx): `aria-label={`Dread level ${n}`}` closes DreadMeter (opened on line 9). Names declared inside that block end here.

  21 |           onKeyDown={(e) => e.key === "Enter" && onChange && onChange(n)}
     | In `DreadMeter` (src/components/TodoList.jsx): event prop `onKeyDown={(e) => e.key === "Enter" && onChange && onChange(n)}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

  22 |         />
     | In `DreadMeter` (src/components/TodoList.jsx): statement `/>`. It runs when DreadMeter runs, in order, before the next line of the same function.

  23 |       ))}
     | In `DreadMeter` (src/components/TodoList.jsx): `))}` closes DreadMeter (opened on line 9). Names declared inside that block end here.

  24 |     </div>
     | In `DreadMeter` (src/components/TodoList.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  25 |   );
     | In `DreadMeter` (src/components/TodoList.jsx): statement `);`. It runs when DreadMeter runs, in order, before the next line of the same function.

  26 | }
     | In `DreadMeter` (src/components/TodoList.jsx): `}` closes DreadMeter (opened on line 9). Names declared inside that block end here.

  27 | 
     | Blank line in `src/components/TodoList.jsx` (the task list, brain dump, and AI suggestion cards), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  28 | function PriorityBadge({ level }) {
     | Defines `PriorityBadge` in the task list, brain dump, and AI suggestion cards. Shows task.aiPriority as High, Medium, or Low. Renders nothing if the server sent no level.

  29 |   if (!level) return null;
     | In `PriorityBadge` (src/components/TodoList.jsx): branch `if (!level) return null;`. Only one side runs.

  30 |   const cls = level === "High" ? "badge-high" : level === "Medium" ? "badge-medium" : "badge-low";
     | In `PriorityBadge` (src/components/TodoList.jsx): `cls` is assigned `level === "High" ? "badge-high" : level === "Medium" ? "badge-medium" : "badge-low";`. Later lines in this function read that name.

  31 |   return <span className={`badge ${cls}`}>{level}</span>;
     | In `PriorityBadge` (src/components/TodoList.jsx): return `return <span className={`badge ${cls}`}>{level}</span>;`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  32 | }
     | In `PriorityBadge` (src/components/TodoList.jsx): `}` closes PriorityBadge (opened on line 28). Names declared inside that block end here.

  33 | 
     | Blank line in `src/components/TodoList.jsx` (the task list, brain dump, and AI suggestion cards), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  34 | const SUGGESTION_STYLES = {
     | In `the top of the file` (src/components/TodoList.jsx): `SUGGESTION_STYLES`: Left-border colors for AI suggestion types: priority, chunk, deadline, quick-win, nudge. The code is `const SUGGESTION_STYLES = {`.

  35 |   priority:    { borderLeft: "3px solid var(--violet)", background: "var(--violet-dim)" },
     | In `the top of the file` (src/components/TodoList.jsx): `priority:    { borderLeft: "3px solid var(--violet)", background: "var(--violet-dim)" },` closes const SUGGESTION_STYLES = { (opened on line 34). Names declared inside that block end here.

  36 |   chunk:       { borderLeft: "3px solid var(--green)",  background: "var(--green-dim)" },
     | In `the top of the file` (src/components/TodoList.jsx): `chunk:       { borderLeft: "3px solid var(--green)",  background: "var(--green-dim)" },` closes const SUGGESTION_STYLES = { (opened on line 34). Names declared inside that block end here.

  37 |   deadline:    { borderLeft: "3px solid var(--red)",    background: "var(--red-dim)" },
     | In `the top of the file` (src/components/TodoList.jsx): `deadline:    { borderLeft: "3px solid var(--red)",    background: "var(--red-dim)" },` closes const SUGGESTION_STYLES = { (opened on line 34). Names declared inside that block end here.

  38 |   "quick-win": { borderLeft: "3px solid var(--amber)",  background: "var(--amber-dim)" },
     | In `the top of the file` (src/components/TodoList.jsx): `"quick-win": { borderLeft: "3px solid var(--amber)",  background: "var(--amber-dim)" },` closes const SUGGESTION_STYLES = { (opened on line 34). Names declared inside that block end here.

  39 |   nudge:       { borderLeft: "3px solid var(--blue)",   background: "rgba(59,130,246,0.08)" },
     | In `the top of the file` (src/components/TodoList.jsx): `nudge:       { borderLeft: "3px solid var(--blue)",   background: "rgba(59,130,246,0.08)" },` closes const SUGGESTION_STYLES = { (opened on line 34). Names declared inside that block end here.

  40 | };
     | In `the top of the file` (src/components/TodoList.jsx): `};` closes const SUGGESTION_STYLES = { (opened on line 34). Names declared inside that block end here.

  41 | 
     | Blank line in `src/components/TodoList.jsx` (the task list, brain dump, and AI suggestion cards), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  42 | const SUGGESTION_LABELS = {
     | In `the top of the file` (src/components/TodoList.jsx): `SUGGESTION_LABELS`: Human labels for those suggestion types, shown above each card. The code is `const SUGGESTION_LABELS = {`.

  43 |   priority:    "Priority",
     | In `the top of the file` (src/components/TodoList.jsx): statement `priority:    "Priority",`. It runs when the top of the file runs, in order, before the next line of the same function.

  44 |   chunk:       "Break Down",
     | In `the top of the file` (src/components/TodoList.jsx): statement `chunk:       "Break Down",`. It runs when the top of the file runs, in order, before the next line of the same function.

  45 |   deadline:    "Urgent",
     | In `the top of the file` (src/components/TodoList.jsx): statement `deadline:    "Urgent",`. It runs when the top of the file runs, in order, before the next line of the same function.

  46 |   "quick-win": "Quick Win",
     | In `the top of the file` (src/components/TodoList.jsx): statement `"quick-win": "Quick Win",`. It runs when the top of the file runs, in order, before the next line of the same function.

  47 |   nudge:       "Tip",
     | In `the top of the file` (src/components/TodoList.jsx): statement `nudge:       "Tip",`. It runs when the top of the file runs, in order, before the next line of the same function.

  48 | };
     | In `the top of the file` (src/components/TodoList.jsx): `};` closes const SUGGESTION_LABELS = { (opened on line 42). Names declared inside that block end here.

  49 | 
     | Blank line in `src/components/TodoList.jsx` (the task list, brain dump, and AI suggestion cards), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  50 | // ── Simplified add-task row: one field, expand for details ───────────────
     | Comment inside the top of the file. Not executed. It documents the next code: ── Simplified add-task row: one field, expand for details ───────────────

  51 | function AddTaskRow({ onAdd }) {
     | Defines `AddTaskRow` in the task list, brain dump, and AI suggestion cards. One title field. Enter submits. Tab or '+ Details' reveals due date, minutes (default 30), and dread (default 3).

  52 |   const [title, setTitle] = useState("");
     | In `AddTaskRow` (src/components/TodoList.jsx): React state `title, setTitle`. The value survives re-renders. Calling the setter re-renders this component. `const [title, setTitle] = useState("");`

  53 |   const [expanded, setExpanded] = useState(false);
     | In `AddTaskRow` (src/components/TodoList.jsx): React state `expanded, setExpanded`. The value survives re-renders. Calling the setter re-renders this component. `const [expanded, setExpanded] = useState(false);`

  54 |   const [due, setDue] = useState("");
     | In `AddTaskRow` (src/components/TodoList.jsx): React state `due, setDue`. The value survives re-renders. Calling the setter re-renders this component. `const [due, setDue] = useState("");`

  55 |   const [estimate, setEstimate] = useState(30);
     | In `AddTaskRow` (src/components/TodoList.jsx): React state `estimate, setEstimate`. The value survives re-renders. Calling the setter re-renders this component. `const [estimate, setEstimate] = useState(30);`

  56 |   const [dreadScore, setDreadScore] = useState(3);
     | In `AddTaskRow` (src/components/TodoList.jsx): React state `dreadScore, setDreadScore`. The value survives re-renders. Calling the setter re-renders this component. `const [dreadScore, setDreadScore] = useState(3);`

  57 |   const inputRef = useRef();
     | In `AddTaskRow` (src/components/TodoList.jsx): A ref `inputRef`. `.current` survives re-renders and writing it does not re-render. `const inputRef = useRef();`

  58 | 
     | Blank line in `src/components/TodoList.jsx` (the task list, brain dump, and AI suggestion cards), inside AddTaskRow. The parser skips it. It separates the previous statement from the next so the function is readable.

  59 |   async function submit() {
     | Defines `submit` in the task list, brain dump, and AI suggestion cards. Calls the onAdd prop, then clears the form and focuses the title again.

  60 |     if (!title.trim()) return;
     | In `submit` (src/components/TodoList.jsx): branch `if (!title.trim()) return;`. Only one side runs.

  61 |     await onAdd({ title: title.trim(), dueAt: due || null, estimateMins: Number(estimate), dreadScore: Number(dreadScore) });
     | In `submit` (src/components/TodoList.jsx): `await onAdd({ title: title.trim(), dueAt: due || null, estimateMins: Number(estimate), dreadScore: Number(dreadScore) });`. The async function suspends until the promise fulfills, then assigns or continues.

  62 |     setTitle("");
     | In `submit` (src/components/TodoList.jsx): statement `setTitle("");`. It runs when submit runs, in order, before the next line of the same function.

  63 |     setDue("");
     | In `submit` (src/components/TodoList.jsx): statement `setDue("");`. It runs when submit runs, in order, before the next line of the same function.

  64 |     setEstimate(30);
     | In `submit` (src/components/TodoList.jsx): statement `setEstimate(30);`. It runs when submit runs, in order, before the next line of the same function.

  65 |     setDreadScore(3);
     | In `submit` (src/components/TodoList.jsx): statement `setDreadScore(3);`. It runs when submit runs, in order, before the next line of the same function.

  66 |     setExpanded(false);
     | In `submit` (src/components/TodoList.jsx): statement `setExpanded(false);`. It runs when submit runs, in order, before the next line of the same function.

  67 |     inputRef.current?.focus();
     | In `submit` (src/components/TodoList.jsx): statement `inputRef.current?.focus();`. It runs when submit runs, in order, before the next line of the same function.

  68 |   }
     | In `submit` (src/components/TodoList.jsx): `}` closes submit (opened on line 59). Names declared inside that block end here.

  69 | 
     | Blank line in `src/components/TodoList.jsx` (the task list, brain dump, and AI suggestion cards), inside AddTaskRow. The parser skips it. It separates the previous statement from the next so the function is readable.

  70 |   return (
     | In `AddTaskRow` (src/components/TodoList.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  71 |     <div className="card card-sm add-task-row">
     | In `AddTaskRow` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="card card-sm add-task-row">`

  72 |       <div className="flex gap-2">
     | In `AddTaskRow` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="flex gap-2">`

  73 |         <input
     | In `AddTaskRow` (src/components/TodoList.jsx): Opens it. A text or date field. If value and onChange are set, React owns what it shows. Source: `<input`

  74 |           ref={inputRef}
     | In `AddTaskRow` (src/components/TodoList.jsx): `ref={inputRef}` closes AddTaskRow (opened on line 51). Names declared inside that block end here.

  75 |           className="input"
     | In `AddTaskRow` (src/components/TodoList.jsx): statement `className="input"`. It runs when AddTaskRow runs, in order, before the next line of the same function.

  76 |           style={{ flex: 1 }}
     | In `AddTaskRow` (src/components/TodoList.jsx): `style={{ flex: 1 }}` closes AddTaskRow (opened on line 51). Names declared inside that block end here.

  77 |           placeholder="What do you need to do?"
     | In `AddTaskRow` (src/components/TodoList.jsx): statement `placeholder="What do you need to do?"`. It runs when AddTaskRow runs, in order, before the next line of the same function.

  78 |           value={title}
     | In `AddTaskRow` (src/components/TodoList.jsx): `value={title}` closes AddTaskRow (opened on line 51). Names declared inside that block end here.

  79 |           onChange={(e) => {
     | In `AddTaskRow` (src/components/TodoList.jsx): event prop `onChange={(e) => {`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

  80 |             setTitle(e.target.value);
     | In `AddTaskRow` (src/components/TodoList.jsx): statement `setTitle(e.target.value);`. It runs when AddTaskRow runs, in order, before the next line of the same function.

  81 |           }}
     | In `AddTaskRow` (src/components/TodoList.jsx): `}}` closes onChange={(e) => { (opened on line 79). Names declared inside that block end here.

  82 |           onKeyDown={(e) => {
     | In `AddTaskRow` (src/components/TodoList.jsx): event prop `onKeyDown={(e) => {`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

  83 |             if (e.key === "Enter") submit();
     | In `AddTaskRow` (src/components/TodoList.jsx): branch `if (e.key === "Enter") submit();`. Only one side runs.

  84 |             if (e.key === "Tab" && title.trim() && !expanded) { e.preventDefault(); setExpanded(true); }
     | In `AddTaskRow` (src/components/TodoList.jsx): branch `if (e.key === "Tab" && title.trim() && !expanded) { e.preventDefault(); setExpanded(true); }`. Only one side runs.

  85 |           }}
     | In `AddTaskRow` (src/components/TodoList.jsx): `}}` closes onKeyDown={(e) => { (opened on line 82). Names declared inside that block end here.

  86 |           aria-label="New task title"
     | In `AddTaskRow` (src/components/TodoList.jsx): statement `aria-label="New task title"`. It runs when AddTaskRow runs, in order, before the next line of the same function.

  87 |         />
     | In `AddTaskRow` (src/components/TodoList.jsx): statement `/>`. It runs when AddTaskRow runs, in order, before the next line of the same function.

  88 |         {title.trim() && !expanded && (
     | In `AddTaskRow` (src/components/TodoList.jsx): statement `{title.trim() && !expanded && (`. It runs when AddTaskRow runs, in order, before the next line of the same function.

  89 |           <button
     | In `AddTaskRow` (src/components/TodoList.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button`

  90 |             className="btn btn-ghost btn-sm"
     | In `AddTaskRow` (src/components/TodoList.jsx): statement `className="btn btn-ghost btn-sm"`. It runs when AddTaskRow runs, in order, before the next line of the same function.

  91 |             onClick={() => setExpanded(true)}
     | In `AddTaskRow` (src/components/TodoList.jsx): event prop `onClick={() => setExpanded(true)}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

  92 |             aria-label="Show more options"
     | In `AddTaskRow` (src/components/TodoList.jsx): statement `aria-label="Show more options"`. It runs when AddTaskRow runs, in order, before the next line of the same function.

  93 |             title="Add details"
     | In `AddTaskRow` (src/components/TodoList.jsx): statement `title="Add details"`. It runs when AddTaskRow runs, in order, before the next line of the same function.

  94 |           >
     | In `AddTaskRow` (src/components/TodoList.jsx): statement `>`. It runs when AddTaskRow runs, in order, before the next line of the same function.

  95 |             + Details
     | In `AddTaskRow` (src/components/TodoList.jsx): statement `+ Details`. It runs when AddTaskRow runs, in order, before the next line of the same function.

  96 |           </button>
     | In `AddTaskRow` (src/components/TodoList.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

  97 |         )}
     | In `AddTaskRow` (src/components/TodoList.jsx): `)}` closes AddTaskRow (opened on line 51). Names declared inside that block end here.

  98 |         <button
     | In `AddTaskRow` (src/components/TodoList.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button`

  99 |           className="btn btn-primary"
     | In `AddTaskRow` (src/components/TodoList.jsx): statement `className="btn btn-primary"`. It runs when AddTaskRow runs, in order, before the next line of the same function.

 100 |           onClick={submit}
     | In `AddTaskRow` (src/components/TodoList.jsx): event prop `onClick={submit}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 101 |           disabled={!title.trim()}
     | In `AddTaskRow` (src/components/TodoList.jsx): `disabled={!title.trim()}` closes AddTaskRow (opened on line 51). Names declared inside that block end here.

 102 |           aria-label="Add task"
     | In `AddTaskRow` (src/components/TodoList.jsx): statement `aria-label="Add task"`. It runs when AddTaskRow runs, in order, before the next line of the same function.

 103 |           style={{ minWidth: 64 }}
     | In `AddTaskRow` (src/components/TodoList.jsx): `style={{ minWidth: 64 }}` closes AddTaskRow (opened on line 51). Names declared inside that block end here.

 104 |         >
     | In `AddTaskRow` (src/components/TodoList.jsx): statement `>`. It runs when AddTaskRow runs, in order, before the next line of the same function.

 105 |           Add
     | In `AddTaskRow` (src/components/TodoList.jsx): statement `Add`. It runs when AddTaskRow runs, in order, before the next line of the same function.

 106 |         </button>
     | In `AddTaskRow` (src/components/TodoList.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

 107 |       </div>
     | In `AddTaskRow` (src/components/TodoList.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 108 | 
     | Blank line in `src/components/TodoList.jsx` (the task list, brain dump, and AI suggestion cards), inside AddTaskRow. The parser skips it. It separates the previous statement from the next so the function is readable.

 109 |       {expanded && (
     | In `AddTaskRow` (src/components/TodoList.jsx): statement `{expanded && (`. It runs when AddTaskRow runs, in order, before the next line of the same function.

 110 |         <div className="add-task-details">
     | In `AddTaskRow` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="add-task-details">`

 111 |           <div className="flex gap-2" style={{ flexWrap: "wrap" }}>
     | In `AddTaskRow` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="flex gap-2" style={{ flexWrap: "wrap" }}>`

 112 |             <div style={{ flex: 1, minWidth: 160 }}>
     | In `AddTaskRow` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div style={{ flex: 1, minWidth: 160 }}>`

 113 |               <label className="text-xs text-muted" style={{ display: "block", marginBottom: 4 }}>Due date</label>
     | In `AddTaskRow` (src/components/TodoList.jsx): Opens it. The caption for an input. Source: `<label className="text-xs text-muted" style={{ display: "block", marginBottom: 4 }}>Due date</label>`

 114 |               <input
     | In `AddTaskRow` (src/components/TodoList.jsx): Opens it. A text or date field. If value and onChange are set, React owns what it shows. Source: `<input`

 115 |                 className="input"
     | In `AddTaskRow` (src/components/TodoList.jsx): statement `className="input"`. It runs when AddTaskRow runs, in order, before the next line of the same function.

 116 |                 type="datetime-local"
     | In `AddTaskRow` (src/components/TodoList.jsx): statement `type="datetime-local"`. It runs when AddTaskRow runs, in order, before the next line of the same function.

 117 |                 value={due}
     | In `AddTaskRow` (src/components/TodoList.jsx): `value={due}` closes AddTaskRow (opened on line 51). Names declared inside that block end here.

 118 |                 onChange={(e) => setDue(e.target.value)}
     | In `AddTaskRow` (src/components/TodoList.jsx): event prop `onChange={(e) => setDue(e.target.value)}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 119 |                 aria-label="Due date"
     | In `AddTaskRow` (src/components/TodoList.jsx): statement `aria-label="Due date"`. It runs when AddTaskRow runs, in order, before the next line of the same function.

 120 |               />
     | In `AddTaskRow` (src/components/TodoList.jsx): statement `/>`. It runs when AddTaskRow runs, in order, before the next line of the same function.

 121 |             </div>
     | In `AddTaskRow` (src/components/TodoList.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 122 |             <div style={{ width: 100 }}>
     | In `AddTaskRow` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div style={{ width: 100 }}>`

 123 |               <label className="text-xs text-muted" style={{ display: "block", marginBottom: 4 }}>Minutes</label>
     | In `AddTaskRow` (src/components/TodoList.jsx): Opens it. The caption for an input. Source: `<label className="text-xs text-muted" style={{ display: "block", marginBottom: 4 }}>Minutes</label>`

 124 |               <input
     | In `AddTaskRow` (src/components/TodoList.jsx): Opens it. A text or date field. If value and onChange are set, React owns what it shows. Source: `<input`

 125 |                 className="input"
     | In `AddTaskRow` (src/components/TodoList.jsx): statement `className="input"`. It runs when AddTaskRow runs, in order, before the next line of the same function.

 126 |                 type="number"
     | In `AddTaskRow` (src/components/TodoList.jsx): statement `type="number"`. It runs when AddTaskRow runs, in order, before the next line of the same function.

 127 |                 placeholder="30"
     | In `AddTaskRow` (src/components/TodoList.jsx): statement `placeholder="30"`. It runs when AddTaskRow runs, in order, before the next line of the same function.

 128 |                 value={estimate}
     | In `AddTaskRow` (src/components/TodoList.jsx): `value={estimate}` closes AddTaskRow (opened on line 51). Names declared inside that block end here.

 129 |                 onChange={(e) => setEstimate(e.target.value)}
     | In `AddTaskRow` (src/components/TodoList.jsx): event prop `onChange={(e) => setEstimate(e.target.value)}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 130 |                 min={1}
     | In `AddTaskRow` (src/components/TodoList.jsx): `min={1}` closes AddTaskRow (opened on line 51). Names declared inside that block end here.

 131 |                 aria-label="Estimated minutes"
     | In `AddTaskRow` (src/components/TodoList.jsx): statement `aria-label="Estimated minutes"`. It runs when AddTaskRow runs, in order, before the next line of the same function.

 132 |               />
     | In `AddTaskRow` (src/components/TodoList.jsx): statement `/>`. It runs when AddTaskRow runs, in order, before the next line of the same function.

 133 |             </div>
     | In `AddTaskRow` (src/components/TodoList.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 134 |           </div>
     | In `AddTaskRow` (src/components/TodoList.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 135 |           <div style={{ marginTop: 8 }}>
     | In `AddTaskRow` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div style={{ marginTop: 8 }}>`

 136 |             <DreadMeter score={dreadScore} onChange={setDreadScore} />
     | In `AddTaskRow` (src/components/TodoList.jsx): JSX `<DreadMeter>`. React will create this node when the parent renders. Source: `<DreadMeter score={dreadScore} onChange={setDreadScore} />`

 137 |           </div>
     | In `AddTaskRow` (src/components/TodoList.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 138 |         </div>
     | In `AddTaskRow` (src/components/TodoList.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 139 |       )}
     | In `AddTaskRow` (src/components/TodoList.jsx): `)}` closes AddTaskRow (opened on line 51). Names declared inside that block end here.

 140 |     </div>
     | In `AddTaskRow` (src/components/TodoList.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 141 |   );
     | In `AddTaskRow` (src/components/TodoList.jsx): statement `);`. It runs when AddTaskRow runs, in order, before the next line of the same function.

 142 | }
     | In `AddTaskRow` (src/components/TodoList.jsx): `}` closes AddTaskRow (opened on line 51). Names declared inside that block end here.

 143 | 
     | Blank line in `src/components/TodoList.jsx` (the task list, brain dump, and AI suggestion cards), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

 144 | export default function TodoList() {
     | Defines `TodoList` in the task list, brain dump, and AI suggestion cards. Open tasks, brain dump, and suggestion cards. Ranks tasks locally with scoreTask and also asks the server for AI suggestions.

 145 |   const { energy } = useEnergy();
     | In `TodoList` (src/components/TodoList.jsx): `energy`: Integer 1–5 from EnergyContext, persisted as bb-energy. Home refetches 'what next' when it changes. TodoList rescores and refetches suggestions. The code is `const { energy } = useEnergy();`.

 146 |   const [searchParams] = useSearchParams();
     | In `TodoList` (src/components/TodoList.jsx): `searchParams` is assigned `useSearchParams();`. Later lines in this function read that name.

 147 | 
     | Blank line in `src/components/TodoList.jsx` (the task list, brain dump, and AI suggestion cards), inside TodoList. The parser skips it. It separates the previous statement from the next so the function is readable.

 148 |   const [tasks, setTasks] = useState([]);
     | In `TodoList` (src/components/TodoList.jsx): React state `tasks, setTasks`. The value survives re-renders. Calling the setter re-renders this component. `const [tasks, setTasks] = useState([]);`

 149 |   const [completing, setCompleting] = useState(null);
     | In `TodoList` (src/components/TodoList.jsx): React state `completing, setCompleting`. The value survives re-renders. Calling the setter re-renders this component. `const [completing, setCompleting] = useState(null);`

 150 |   const [reward, setReward] = useState(null);
     | In `TodoList` (src/components/TodoList.jsx): React state `reward, setReward`. The value survives re-renders. Calling the setter re-renders this component. `const [reward, setReward] = useState(null);`

 151 | 
     | Blank line in `src/components/TodoList.jsx` (the task list, brain dump, and AI suggestion cards), inside TodoList. The parser skips it. It separates the previous statement from the next so the function is readable.

 152 |   // Edit state
     | Comment inside TodoList. Not executed. It documents the next code: Edit state

 153 |   const [editingId, setEditingId] = useState(null);
     | In `TodoList` (src/components/TodoList.jsx): React state `editingId, setEditingId`. The value survives re-renders. Calling the setter re-renders this component. `const [editingId, setEditingId] = useState(null);`

 154 |   const [editTitle, setEditTitle] = useState("");
     | In `TodoList` (src/components/TodoList.jsx): React state `editTitle, setEditTitle`. The value survives re-renders. Calling the setter re-renders this component. `const [editTitle, setEditTitle] = useState("");`

 155 |   const [editDue, setEditDue] = useState("");
     | In `TodoList` (src/components/TodoList.jsx): React state `editDue, setEditDue`. The value survives re-renders. Calling the setter re-renders this component. `const [editDue, setEditDue] = useState("");`

 156 |   const [editEstimate, setEditEstimate] = useState(30);
     | In `TodoList` (src/components/TodoList.jsx): React state `editEstimate, setEditEstimate`. The value survives re-renders. Calling the setter re-renders this component. `const [editEstimate, setEditEstimate] = useState(30);`

 157 |   const [editDread, setEditDread] = useState(3);
     | In `TodoList` (src/components/TodoList.jsx): React state `editDread, setEditDread`. The value survives re-renders. Calling the setter re-renders this component. `const [editDread, setEditDread] = useState(3);`

 158 | 
     | Blank line in `src/components/TodoList.jsx` (the task list, brain dump, and AI suggestion cards), inside TodoList. The parser skips it. It separates the previous statement from the next so the function is readable.

 159 |   // Brain dump
     | Comment inside TodoList. Not executed. It documents the next code: Brain dump

 160 |   const [dumpText, setDumpText] = useState("");
     | In `TodoList` (src/components/TodoList.jsx): React state `dumpText, setDumpText`. The value survives re-renders. Calling the setter re-renders this component. `const [dumpText, setDumpText] = useState("");`

 161 |   const [dumpLoading, setDumpLoading] = useState(false);
     | In `TodoList` (src/components/TodoList.jsx): React state `dumpLoading, setDumpLoading`. The value survives re-renders. Calling the setter re-renders this component. `const [dumpLoading, setDumpLoading] = useState(false);`

 162 |   const [view, setView] = useState(searchParams.get("tab") === "dump" ? "dump" : "tasks");
     | In `TodoList` (src/components/TodoList.jsx): React state `view, setView`. The value survives re-renders. Calling the setter re-renders this component. `const [view, setView] = useState(searchParams.get("tab") === "dump" ? "dump" : "tasks");`

 163 | 
     | Blank line in `src/components/TodoList.jsx` (the task list, brain dump, and AI suggestion cards), inside TodoList. The parser skips it. It separates the previous statement from the next so the function is readable.

 164 |   // AI suggestions
     | Comment inside TodoList. Not executed. It documents the next code: AI suggestions

 165 |   const [suggestions, setSuggestions] = useState([]);
     | In `TodoList` (src/components/TodoList.jsx): React state `suggestions, setSuggestions`. The value survives re-renders. Calling the setter re-renders this component. `const [suggestions, setSuggestions] = useState([]);`

 166 |   const [suggestionsLoading, setSuggestionsLoading] = useState(false);
     | In `TodoList` (src/components/TodoList.jsx): React state `suggestionsLoading, setSuggestionsLoading`. The value survives re-renders. Calling the setter re-renders this component. `const [suggestionsLoading, setSuggestionsLoading] = useState(false);`

 167 |   const [dismissedIds, setDismissedIds] = useState(new Set());
     | In `TodoList` (src/components/TodoList.jsx): React state `dismissedIds, setDismissedIds`. The value survives re-renders. Calling the setter re-renders this component. `const [dismissedIds, setDismissedIds] = useState(new Set());`

 168 | 
     | Blank line in `src/components/TodoList.jsx` (the task list, brain dump, and AI suggestion cards), inside TodoList. The parser skips it. It separates the previous statement from the next so the function is readable.

 169 |   useEffect(() => { load(); }, []);
     | In `TodoList` (src/components/TodoList.jsx): opens or continues an effect — `useEffect(() => { load(); }, []);`. The effect body runs after paint, and its cleanup runs before the next effect and on unmount.

 170 | 
     | Blank line in `src/components/TodoList.jsx` (the task list, brain dump, and AI suggestion cards), inside TodoList. The parser skips it. It separates the previous statement from the next so the function is readable.

 171 |   useEffect(() => {
     | In `TodoList` (src/components/TodoList.jsx): opens or continues an effect — `useEffect(() => {`. The effect body runs after paint, and its cleanup runs before the next effect and on unmount.

 172 |     tasks.forEach((task) => {
     | In `TodoList` (src/components/TodoList.jsx): iteration `tasks.forEach((task) => {`.

 173 |       if (task.dueAt && !task.completed) scheduleDeadline(task);
     | In `TodoList` (src/components/TodoList.jsx): branch `if (task.dueAt && !task.completed) scheduleDeadline(task);`. Only one side runs.

 174 |     });
     | In `TodoList` (src/components/TodoList.jsx): `});` closes tasks.forEach((task) => { (opened on line 172). Names declared inside that block end here.

 175 |     return () => { tasks.forEach((t) => clearDeadline(t._id)); };
     | In `TodoList` (src/components/TodoList.jsx): return `return () => { tasks.forEach((t) => clearDeadline(t._id)); };`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

 176 |   }, [tasks]);
     | In `TodoList` (src/components/TodoList.jsx): `}, [tasks]);` closes effect in TodoList (opened on line 171). Names declared inside that block end here.

 177 | 
     | Blank line in `src/components/TodoList.jsx` (the task list, brain dump, and AI suggestion cards), inside TodoList. The parser skips it. It separates the previous statement from the next so the function is readable.

 178 |   useEffect(() => {
     | In `TodoList` (src/components/TodoList.jsx): opens or continues an effect — `useEffect(() => {`. The effect body runs after paint, and its cleanup runs before the next effect and on unmount.

 179 |     if (tasks.length > 0) fetchSuggestions();
     | In `TodoList` (src/components/TodoList.jsx): branch `if (tasks.length > 0) fetchSuggestions();`. Only one side runs.

 180 |     else setSuggestions([]);
     | In `TodoList` (src/components/TodoList.jsx): statement `else setSuggestions([]);`. It runs when TodoList runs, in order, before the next line of the same function.

 181 |   }, [tasks.length, energy]);
     | In `TodoList` (src/components/TodoList.jsx): `}, [tasks.length, energy]);` closes effect in TodoList (opened on line 178). Names declared inside that block end here.

 182 | 
     | Blank line in `src/components/TodoList.jsx` (the task list, brain dump, and AI suggestion cards), inside TodoList. The parser skips it. It separates the previous statement from the next so the function is readable.

 183 |   async function load() {
     | Defines `load` in the task list, brain dump, and AI suggestion cards. GET /tasks and, on the task page, keeps only tasks that are not completed. Calendar and the deadline page keep a wider set.

 184 |     try {
     | In `load` (src/components/TodoList.jsx): error path `try {`.

 185 |       const res = await api.get("/tasks");
     | In `load` (src/components/TodoList.jsx): `res` is assigned `await api.get("/tasks");`. Later lines in this function read that name.

 186 |       setTasks((res.tasks || []).filter((t) => !t.completed));
     | In `load` (src/components/TodoList.jsx): iteration `setTasks((res.tasks || []).filter((t) => !t.completed));`.

 187 |     } catch { setTasks([]); }
     | In `load` (src/components/TodoList.jsx): `} catch { setTasks([]); }` closes try { (opened on line 184). Names declared inside that block end here.

 188 |   }
     | In `load` (src/components/TodoList.jsx): `}` closes load (opened on line 183). Names declared inside that block end here.

 189 | 
     | Blank line in `src/components/TodoList.jsx` (the task list, brain dump, and AI suggestion cards), inside TodoList. The parser skips it. It separates the previous statement from the next so the function is readable.

 190 |   async function fetchSuggestions() {
     | Defines `fetchSuggestions` in the task list, brain dump, and AI suggestion cards. GET /tasks/ai/suggestions and GET /recommendations/mindfulness in parallel. A mindfulness hit is inserted as a nudge card. Dismissed ids are filtered out.

 191 |     setSuggestionsLoading(true);
     | In `fetchSuggestions` (src/components/TodoList.jsx): statement `setSuggestionsLoading(true);`. It runs when fetchSuggestions runs, in order, before the next line of the same function.

 192 |     try {
     | In `fetchSuggestions` (src/components/TodoList.jsx): error path `try {`.

 193 |       const [suggestRes, mindRes] = await Promise.allSettled([
     | In `fetchSuggestions` (src/components/TodoList.jsx): `suggestRes, mindRes` is assigned `await Promise.allSettled([`. Later lines in this function read that name.

 194 |         api.get(`/tasks/ai/suggestions?energyLevel=${energy}`),
     | In `fetchSuggestions` (src/components/TodoList.jsx): HTTP via the shared Axios instance — `api.get(`/tasks/ai/suggestions?energyLevel=${energy}`),`. The request interceptor adds `Authorization: Bearer <accessToken>`. The response interceptor returns `res.data`, so the awaited value is the JSON body.

 195 |         api.get(`/recommendations/mindfulness?energyLevel=${energy}`),
     | In `fetchSuggestions` (src/components/TodoList.jsx): HTTP via the shared Axios instance — `api.get(`/recommendations/mindfulness?energyLevel=${energy}`),`. The request interceptor adds `Authorization: Bearer <accessToken>`. The response interceptor returns `res.data`, so the awaited value is the JSON body.

 196 |       ]);
     | In `fetchSuggestions` (src/components/TodoList.jsx): statement `]);`. It runs when fetchSuggestions runs, in order, before the next line of the same function.

 197 | 
     | Blank line in `src/components/TodoList.jsx` (the task list, brain dump, and AI suggestion cards), inside fetchSuggestions. The parser skips it. It separates the previous statement from the next so the function is readable.

 198 |       if (suggestRes.status === "fulfilled") {
     | In `fetchSuggestions` (src/components/TodoList.jsx): branch `if (suggestRes.status === "fulfilled") {`. Only one side runs.

 199 |         const allSuggestions = suggestRes.value.suggestions || [];
     | In `fetchSuggestions` (src/components/TodoList.jsx): `allSuggestions` is assigned `suggestRes.value.suggestions || [];`. Later lines in this function read that name.

 200 |         if (mindRes.status === "fulfilled" && mindRes.value.suggested && mindRes.value.top) {
     | In `fetchSuggestions` (src/components/TodoList.jsx): branch `if (mindRes.status === "fulfilled" && mindRes.value.suggested && mindRes.value.top) {`. Only one side runs.

 201 |           const m = mindRes.value.top;
     | In `fetchSuggestions` (src/components/TodoList.jsx): `m` is assigned `mindRes.value.top;`. Later lines in this function read that name.

 202 |           allSuggestions.unshift({
     | In `fetchSuggestions` (src/components/TodoList.jsx): statement `allSuggestions.unshift({`. It runs when fetchSuggestions runs, in order, before the next line of the same function.

 203 |             id: "mindful_" + Date.now(),
     | In `fetchSuggestions` (src/components/TodoList.jsx): statement `id: "mindful_" + Date.now(),`. It runs when fetchSuggestions runs, in order, before the next line of the same function.

 204 |             type: "nudge",
     | In `fetchSuggestions` (src/components/TodoList.jsx): statement `type: "nudge",`. It runs when fetchSuggestions runs, in order, before the next line of the same function.

 205 |             title: `🧘 ${m.title}`,
     | In `fetchSuggestions` (src/components/TodoList.jsx): `title: `🧘 ${m.title}`,` closes allSuggestions.unshift({ (opened on line 202). Names declared inside that block end here.

 206 |             description: m.description,
     | In `fetchSuggestions` (src/components/TodoList.jsx): statement `description: m.description,`. It runs when fetchSuggestions runs, in order, before the next line of the same function.

 207 |             action: "mindfulness",
     | In `fetchSuggestions` (src/components/TodoList.jsx): statement `action: "mindfulness",`. It runs when fetchSuggestions runs, in order, before the next line of the same function.

 208 |           });
     | In `fetchSuggestions` (src/components/TodoList.jsx): `});` closes allSuggestions.unshift({ (opened on line 202). Names declared inside that block end here.

 209 |         }
     | In `fetchSuggestions` (src/components/TodoList.jsx): `}` closes if (mindRes.status === "fulfilled" && mi (opened on line 200). Names declared inside that block end here.

 210 |         const fresh = allSuggestions.filter((s) => !dismissedIds.has(s.id));
     | In `fetchSuggestions` (src/components/TodoList.jsx): `fresh` is assigned `allSuggestions.filter((s) => !dismissedIds.has(s.id));`. Later lines in this function read that name.

 211 |         setSuggestions(fresh);
     | In `fetchSuggestions` (src/components/TodoList.jsx): statement `setSuggestions(fresh);`. It runs when fetchSuggestions runs, in order, before the next line of the same function.

 212 |       } else {
     | In `fetchSuggestions` (src/components/TodoList.jsx): branch `} else {`. Only one side runs.

 213 |         setSuggestions([]);
     | In `fetchSuggestions` (src/components/TodoList.jsx): statement `setSuggestions([]);`. It runs when fetchSuggestions runs, in order, before the next line of the same function.

 214 |       }
     | In `fetchSuggestions` (src/components/TodoList.jsx): `}` closes } else { (opened on line 212). Names declared inside that block end here.

 215 |     } catch { setSuggestions([]); }
     | In `fetchSuggestions` (src/components/TodoList.jsx): `} catch { setSuggestions([]); }` closes try { (opened on line 192). Names declared inside that block end here.

 216 |     finally { setSuggestionsLoading(false); }
     | In `fetchSuggestions` (src/components/TodoList.jsx): `finally { setSuggestionsLoading(false); }` closes fetchSuggestions (opened on line 190). Names declared inside that block end here.

 217 |   }
     | In `fetchSuggestions` (src/components/TodoList.jsx): `}` closes fetchSuggestions (opened on line 190). Names declared inside that block end here.

 218 | 
     | Blank line in `src/components/TodoList.jsx` (the task list, brain dump, and AI suggestion cards), inside TodoList. The parser skips it. It separates the previous statement from the next so the function is readable.

 219 |   async function add({ title, dueAt, estimateMins, dreadScore }) {
     | Defines `add` in the task list, brain dump, and AI suggestion cards. POST /tasks. If the new task has a due date, schedule a notification and tell the user one was set.

 220 |     try {
     | In `add` (src/components/TodoList.jsx): error path `try {`.

 221 |       const res = await api.post("/tasks", { title, dueAt, estimateMins, dreadScore });
     | In `add` (src/components/TodoList.jsx): `res` is assigned `await api.post("/tasks", { title, dueAt, estimateMins, dreadScore });`. Later lines in this function read that name.

 222 |       const task = res.task;
     | In `add` (src/components/TodoList.jsx): `task` is assigned `res.task;`. Later lines in this function read that name.

 223 |       if (task?.dueAt) {
     | In `add` (src/components/TodoList.jsx): branch `if (task?.dueAt) {`. Only one side runs.

 224 |         scheduleDeadline(task);
     | In `add` (src/components/TodoList.jsx): statement `scheduleDeadline(task);`. It runs when add runs, in order, before the next line of the same function.

 225 |         notify("📅 Deadline set", `You'll be reminded when "${task.title}" is due.`);
     | In `add` (src/components/TodoList.jsx): `notify("📅 Deadline set", `You'll be reminded when "${task.title}" is due.`);` closes if (task?.dueAt) { (opened on line 223). Names declared inside that block end here.

 226 |       }
     | In `add` (src/components/TodoList.jsx): `}` closes if (task?.dueAt) { (opened on line 223). Names declared inside that block end here.

 227 |       load();
     | In `add` (src/components/TodoList.jsx): statement `load();`. It runs when add runs, in order, before the next line of the same function.

 228 |     } catch { alert("Could not add task"); }
     | In `add` (src/components/TodoList.jsx): `} catch { alert("Could not add task"); }` closes try { (opened on line 220). Names declared inside that block end here.

 229 |   }
     | In `add` (src/components/TodoList.jsx): `}` closes add (opened on line 219). Names declared inside that block end here.

 230 | 
     | Blank line in `src/components/TodoList.jsx` (the task list, brain dump, and AI suggestion cards), inside TodoList. The parser skips it. It separates the previous statement from the next so the function is readable.

 231 |   async function complete(id) {
     | Defines `complete` in the task list, brain dump, and AI suggestion cards. Shows the check animation for 450ms, then PUT /tasks/:id/complete, clears the deadline timer, and reloads.

 232 |     setCompleting(id);
     | In `complete` (src/components/TodoList.jsx): statement `setCompleting(id);`. It runs when complete runs, in order, before the next line of the same function.

 233 |     showReward("✅");
     | In `complete` (src/components/TodoList.jsx): statement `showReward("✅");`. It runs when complete runs, in order, before the next line of the same function.

 234 |     setTimeout(async () => {
     | In `complete` (src/components/TodoList.jsx): timer — `setTimeout(async () => {`. The callback runs later on the event loop, not now.

 235 |       try {
     | In `complete` (src/components/TodoList.jsx): error path `try {`.

 236 |         await api.put(`/tasks/${id}/complete`, {});
     | In `complete` (src/components/TodoList.jsx): HTTP via the shared Axios instance — `await api.put(`/tasks/${id}/complete`, {});`. The request interceptor adds `Authorization: Bearer <accessToken>`. The response interceptor returns `res.data`, so the awaited value is the JSON body.

 237 |         clearDeadline(id);
     | In `complete` (src/components/TodoList.jsx): statement `clearDeadline(id);`. It runs when complete runs, in order, before the next line of the same function.

 238 |         notify("✅ Task completed", "Well done. One less thing to worry about.");
     | In `complete` (src/components/TodoList.jsx): statement `notify("✅ Task completed", "Well done. One less thing to worry about.");`. It runs when complete runs, in order, before the next line of the same function.

 239 |         load();
     | In `complete` (src/components/TodoList.jsx): statement `load();`. It runs when complete runs, in order, before the next line of the same function.

 240 |       } catch {}
     | In `complete` (src/components/TodoList.jsx): `} catch {}` closes try { (opened on line 235). Names declared inside that block end here.

 241 |       setCompleting(null);
     | In `complete` (src/components/TodoList.jsx): statement `setCompleting(null);`. It runs when complete runs, in order, before the next line of the same function.

 242 |     }, 450);
     | In `complete` (src/components/TodoList.jsx): `}, 450);` closes setTimeout(async () => { (opened on line 234). Names declared inside that block end here.

 243 |   }
     | In `complete` (src/components/TodoList.jsx): `}` closes complete (opened on line 231). Names declared inside that block end here.

 244 | 
     | Blank line in `src/components/TodoList.jsx` (the task list, brain dump, and AI suggestion cards), inside TodoList. The parser skips it. It separates the previous statement from the next so the function is readable.

 245 |   async function autoChunk(t) {
     | Defines `autoChunk` in the task list, brain dump, and AI suggestion cards. POST /tasks/:id/auto-chunk so the server splits the task into subtasks, then reloads.

 246 |     try {
     | In `autoChunk` (src/components/TodoList.jsx): error path `try {`.

 247 |       await api.post(`/tasks/${t._id}/auto-chunk`, {});
     | In `autoChunk` (src/components/TodoList.jsx): HTTP via the shared Axios instance — `await api.post(`/tasks/${t._id}/auto-chunk`, {});`. The request interceptor adds `Authorization: Bearer <accessToken>`. The response interceptor returns `res.data`, so the awaited value is the JSON body.

 248 |       load();
     | In `autoChunk` (src/components/TodoList.jsx): statement `load();`. It runs when autoChunk runs, in order, before the next line of the same function.

 249 |       notify("🧩 Chunked", `"${t.title}" has been broken into sub-tasks.`);
     | In `autoChunk` (src/components/TodoList.jsx): `notify("🧩 Chunked", `"${t.title}" has been broken into sub-tasks.`);` closes try { (opened on line 246). Names declared inside that block end here.

 250 |     } catch { alert("Chunk failed"); }
     | In `autoChunk` (src/components/TodoList.jsx): `} catch { alert("Chunk failed"); }` closes try { (opened on line 246). Names declared inside that block end here.

 251 |   }
     | In `autoChunk` (src/components/TodoList.jsx): `}` closes autoChunk (opened on line 245). Names declared inside that block end here.

 252 | 
     | Blank line in `src/components/TodoList.jsx` (the task list, brain dump, and AI suggestion cards), inside TodoList. The parser skips it. It separates the previous statement from the next so the function is readable.

 253 |   async function saveEdit(id) {
     | Defines `saveEdit` in the task list, brain dump, and AI suggestion cards. PUT /tasks/:id with the edit fields, closes the editor, reloads.

 254 |     try {
     | In `saveEdit` (src/components/TodoList.jsx): error path `try {`.

 255 |       await api.put(`/tasks/${id}`, {
     | In `saveEdit` (src/components/TodoList.jsx): HTTP via the shared Axios instance — `await api.put(`/tasks/${id}`, {`. The request interceptor adds `Authorization: Bearer <accessToken>`. The response interceptor returns `res.data`, so the awaited value is the JSON body.

 256 |         title: editTitle,
     | In `saveEdit` (src/components/TodoList.jsx): statement `title: editTitle,`. It runs when saveEdit runs, in order, before the next line of the same function.

 257 |         dueAt: editDue || null,
     | In `saveEdit` (src/components/TodoList.jsx): statement `dueAt: editDue || null,`. It runs when saveEdit runs, in order, before the next line of the same function.

 258 |         estimateMins: Number(editEstimate),
     | In `saveEdit` (src/components/TodoList.jsx): statement `estimateMins: Number(editEstimate),`. It runs when saveEdit runs, in order, before the next line of the same function.

 259 |         dreadScore: Number(editDread),
     | In `saveEdit` (src/components/TodoList.jsx): statement `dreadScore: Number(editDread),`. It runs when saveEdit runs, in order, before the next line of the same function.

 260 |       });
     | In `saveEdit` (src/components/TodoList.jsx): `});` closes await api.put(`/tasks/${id}`, { (opened on line 255). Names declared inside that block end here.

 261 |       setEditingId(null);
     | In `saveEdit` (src/components/TodoList.jsx): statement `setEditingId(null);`. It runs when saveEdit runs, in order, before the next line of the same function.

 262 |       load();
     | In `saveEdit` (src/components/TodoList.jsx): statement `load();`. It runs when saveEdit runs, in order, before the next line of the same function.

 263 |     } catch { alert("Failed to update task"); }
     | In `saveEdit` (src/components/TodoList.jsx): `} catch { alert("Failed to update task"); }` closes try { (opened on line 254). Names declared inside that block end here.

 264 |   }
     | In `saveEdit` (src/components/TodoList.jsx): `}` closes saveEdit (opened on line 253). Names declared inside that block end here.

 265 | 
     | Blank line in `src/components/TodoList.jsx` (the task list, brain dump, and AI suggestion cards), inside TodoList. The parser skips it. It separates the previous statement from the next so the function is readable.

 266 |   async function updateDread(id, score) {
     | Defines `updateDread` in the task list, brain dump, and AI suggestion cards. PUT only dreadScore and patches that one task in state so the list does not reload.

 267 |     try {
     | In `updateDread` (src/components/TodoList.jsx): error path `try {`.

 268 |       await api.put(`/tasks/${id}`, { dreadScore: score });
     | In `updateDread` (src/components/TodoList.jsx): HTTP via the shared Axios instance — `await api.put(`/tasks/${id}`, { dreadScore: score });`. The request interceptor adds `Authorization: Bearer <accessToken>`. The response interceptor returns `res.data`, so the awaited value is the JSON body.

 269 |       setTasks((prev) => prev.map((t) => t._id === id ? { ...t, dreadScore: score } : t));
     | In `updateDread` (src/components/TodoList.jsx): iteration `setTasks((prev) => prev.map((t) => t._id === id ? { ...t, dreadScore: score } : t));`.

 270 |     } catch {}
     | In `updateDread` (src/components/TodoList.jsx): `} catch {}` closes try { (opened on line 267). Names declared inside that block end here.

 271 |   }
     | In `updateDread` (src/components/TodoList.jsx): `}` closes updateDread (opened on line 266). Names declared inside that block end here.

 272 | 
     | Blank line in `src/components/TodoList.jsx` (the task list, brain dump, and AI suggestion cards), inside TodoList. The parser skips it. It separates the previous statement from the next so the function is readable.

 273 |   async function submitDump() {
     | Defines `submitDump` in the task list, brain dump, and AI suggestion cards. POST /tasks/brain-dump with the text and current energy. Switches the view back to the list.

 274 |     if (!dumpText.trim()) return;
     | In `submitDump` (src/components/TodoList.jsx): branch `if (!dumpText.trim()) return;`. Only one side runs.

 275 |     setDumpLoading(true);
     | In `submitDump` (src/components/TodoList.jsx): statement `setDumpLoading(true);`. It runs when submitDump runs, in order, before the next line of the same function.

 276 |     try {
     | In `submitDump` (src/components/TodoList.jsx): error path `try {`.

 277 |       const res = await api.post("/tasks/brain-dump", { text: dumpText, energyLevel: energy });
     | In `submitDump` (src/components/TodoList.jsx): `res` is assigned `await api.post("/tasks/brain-dump", { text: dumpText, energyLevel: energy });`. Later lines in this function read that name.

 278 |       const count = res.tasks?.length || 0;
     | In `submitDump` (src/components/TodoList.jsx): `count` is assigned `res.tasks?.length || 0;`. Later lines in this function read that name.

 279 |       notify("🧠 Dumped!", `${count} task${count !== 1 ? "s" : ""} extracted.`);
     | In `submitDump` (src/components/TodoList.jsx): `notify("🧠 Dumped!", `${count} task${count !== 1 ? "s" : ""} extracted.`);` closes try { (opened on line 276). Names declared inside that block end here.

 280 |       setDumpText("");
     | In `submitDump` (src/components/TodoList.jsx): statement `setDumpText("");`. It runs when submitDump runs, in order, before the next line of the same function.

 281 |       setView("tasks");
     | In `submitDump` (src/components/TodoList.jsx): statement `setView("tasks");`. It runs when submitDump runs, in order, before the next line of the same function.

 282 |       load();
     | In `submitDump` (src/components/TodoList.jsx): statement `load();`. It runs when submitDump runs, in order, before the next line of the same function.

 283 |     } catch { alert("Brain dump failed"); }
     | In `submitDump` (src/components/TodoList.jsx): `} catch { alert("Brain dump failed"); }` closes try { (opened on line 276). Names declared inside that block end here.

 284 |     finally { setDumpLoading(false); }
     | In `submitDump` (src/components/TodoList.jsx): `finally { setDumpLoading(false); }` closes submitDump (opened on line 273). Names declared inside that block end here.

 285 |   }
     | In `submitDump` (src/components/TodoList.jsx): `}` closes submitDump (opened on line 273). Names declared inside that block end here.

 286 | 
     | Blank line in `src/components/TodoList.jsx` (the task list, brain dump, and AI suggestion cards), inside TodoList. The parser skips it. It separates the previous statement from the next so the function is readable.

 287 |   function acceptSuggestion(s) {
     | Defines `acceptSuggestion` in the task list, brain dump, and AI suggestion cards. Quick-win completes that task. Mindfulness navigates to /mindful. Prioritize scrolls to the task row. Then the card is removed.

 288 |     if (s.type === "quick-win" && s.taskId) {
     | In `acceptSuggestion` (src/components/TodoList.jsx): branch `if (s.type === "quick-win" && s.taskId) {`. Only one side runs.

 289 |       complete(s.taskId);
     | In `acceptSuggestion` (src/components/TodoList.jsx): statement `complete(s.taskId);`. It runs when acceptSuggestion runs, in order, before the next line of the same function.

 290 |     } else if (s.action === "mindfulness") {
     | In `acceptSuggestion` (src/components/TodoList.jsx): branch `} else if (s.action === "mindfulness") {`. Only one side runs.

 291 |       window.location.href = "/mindful";
     | In `acceptSuggestion` (src/components/TodoList.jsx): statement `window.location.href = "/mindful";`. It runs when acceptSuggestion runs, in order, before the next line of the same function.

 292 |       return;
     | In `acceptSuggestion` (src/components/TodoList.jsx): return `return;`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

 293 |     } else if (s.action === "prioritize" && s.taskId) {
     | In `acceptSuggestion` (src/components/TodoList.jsx): branch `} else if (s.action === "prioritize" && s.taskId) {`. Only one side runs.

 294 |       document.getElementById(`task-${s.taskId}`)?.scrollIntoView({ behavior: "smooth" });
     | In `acceptSuggestion` (src/components/TodoList.jsx): `document.getElementById(`task-${s.taskId}`)?.scrollIntoView({ behavior: "smooth" });` closes } else if (s.action === "prioritize" && s.taskId (opened on line 293). Names declared inside that block end here.

 295 |     }
     | In `acceptSuggestion` (src/components/TodoList.jsx): `}` closes } else if (s.action === "prioritize" && s.taskId (opened on line 293). Names declared inside that block end here.

 296 |     setSuggestions((p) => p.filter((x) => x.id !== s.id));
     | In `acceptSuggestion` (src/components/TodoList.jsx): iteration `setSuggestions((p) => p.filter((x) => x.id !== s.id));`.

 297 |     setDismissedIds((p) => new Set([...p, s.id]));
     | In `acceptSuggestion` (src/components/TodoList.jsx): statement `setDismissedIds((p) => new Set([...p, s.id]));`. It runs when acceptSuggestion runs, in order, before the next line of the same function.

 298 |   }
     | In `acceptSuggestion` (src/components/TodoList.jsx): `}` closes acceptSuggestion (opened on line 287). Names declared inside that block end here.

 299 | 
     | Blank line in `src/components/TodoList.jsx` (the task list, brain dump, and AI suggestion cards), inside TodoList. The parser skips it. It separates the previous statement from the next so the function is readable.

 300 |   function dismissSuggestion(s) {
     | Defines `dismissSuggestion` in the task list, brain dump, and AI suggestion cards. Removes the card and remembers the id so the next fetch does not bring it back.

 301 |     setSuggestions((p) => p.filter((x) => x.id !== s.id));
     | In `dismissSuggestion` (src/components/TodoList.jsx): iteration `setSuggestions((p) => p.filter((x) => x.id !== s.id));`.

 302 |     setDismissedIds((p) => new Set([...p, s.id]));
     | In `dismissSuggestion` (src/components/TodoList.jsx): statement `setDismissedIds((p) => new Set([...p, s.id]));`. It runs when dismissSuggestion runs, in order, before the next line of the same function.

 303 |   }
     | In `dismissSuggestion` (src/components/TodoList.jsx): `}` closes dismissSuggestion (opened on line 300). Names declared inside that block end here.

 304 | 
     | Blank line in `src/components/TodoList.jsx` (the task list, brain dump, and AI suggestion cards), inside TodoList. The parser skips it. It separates the previous statement from the next so the function is readable.

 305 |   function showReward(emoji) {
     | Defines `showReward` in the task list, brain dump, and AI suggestion cards. Sets an emoji that a CSS burst shows, then clears it after 900ms.

 306 |     setReward(emoji);
     | In `showReward` (src/components/TodoList.jsx): statement `setReward(emoji);`. It runs when showReward runs, in order, before the next line of the same function.

 307 |     setTimeout(() => setReward(null), 900);
     | In `showReward` (src/components/TodoList.jsx): timer — `setTimeout(() => setReward(null), 900);`. The callback runs later on the event loop, not now.

 308 |   }
     | In `showReward` (src/components/TodoList.jsx): `}` closes showReward (opened on line 305). Names declared inside that block end here.

 309 | 
     | Blank line in `src/components/TodoList.jsx` (the task list, brain dump, and AI suggestion cards), inside TodoList. The parser skips it. It separates the previous statement from the next so the function is readable.

 310 |   function fmtDue(d) {
     | Defines `fmtDue` in the task list, brain dump, and AI suggestion cards. Overdue, 'due in Nh' under 24 hours, or a calendar date.

 311 |     if (!d) return "No due date";
     | In `fmtDue` (src/components/TodoList.jsx): branch `if (!d) return "No due date";`. Only one side runs.

 312 |     const dt = new Date(d);
     | In `fmtDue` (src/components/TodoList.jsx): `dt` is assigned `new Date(d);`. Later lines in this function read that name.

 313 |     const now = new Date();
     | In `fmtDue` (src/components/TodoList.jsx): `now` is assigned `new Date();`. Later lines in this function read that name.

 314 |     const h = (dt - now) / 3600000;
     | In `fmtDue` (src/components/TodoList.jsx): `h` is assigned `(dt - now) / 3600000;`. Later lines in this function read that name.

 315 |     if (h < 0) return "Overdue!";
     | In `fmtDue` (src/components/TodoList.jsx): branch `if (h < 0) return "Overdue!";`. Only one side runs.

 316 |     if (h < 24) return `Due in ${Math.round(h)}h`;
     | In `fmtDue` (src/components/TodoList.jsx): branch `if (h < 24) return `Due in ${Math.round(h)}h`;`. Only one side runs.

 317 |     return dt.toLocaleDateString();
     | In `fmtDue` (src/components/TodoList.jsx): return `return dt.toLocaleDateString();`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

 318 |   }
     | In `fmtDue` (src/components/TodoList.jsx): `}` closes fmtDue (opened on line 310). Names declared inside that block end here.

 319 | 
     | Blank line in `src/components/TodoList.jsx` (the task list, brain dump, and AI suggestion cards), inside TodoList. The parser skips it. It separates the previous statement from the next so the function is readable.

 320 |   function scoreTask(t) {
     | Defines `scoreTask` in the task list, brain dump, and AI suggestion cards. One number per task. Bigger sorts first. urgency × energyMatch × dreadInverse × timeFit.

 321 |     const now = new Date();
     | In `scoreTask` (src/components/TodoList.jsx): `now` is assigned `new Date();`. Later lines in this function read that name.

 322 |     const hoursLeft = t.dueAt ? (new Date(t.dueAt) - now) / 3600000 : 168;
     | In `scoreTask` (src/components/TodoList.jsx): `hoursLeft`: Hours until due. A task with no due date is treated as 168 hours away so it is not scored as urgent. The code is `const hoursLeft = t.dueAt ? (new Date(t.dueAt) - now) / 3600000 : 168;`.

 323 |     const urgency = t.dueAt ? Math.exp(-Math.max(hoursLeft, 0) / 48) + 0.1 : 0.1;
     | In `scoreTask` (src/components/TodoList.jsx): `urgency`: Near 1 when the deadline is imminent, near 0.1 when it is far or missing. The exponential falls off over about two days (the 48). The code is `const urgency = t.dueAt ? Math.exp(-Math.max(hoursLeft, 0) / 48) + 0.1 : 0.1;`.

 324 |     const taskDiff = Math.min((t.estimateMins || 30) / 120, 1);
     | In `scoreTask` (src/components/TodoList.jsx): `taskDiff`: How big the task is, estimate/120, capped at 1. A 30-minute task is 0.25; two hours or more is 1. The code is `const taskDiff = Math.min((t.estimateMins || 30) / 120, 1);`.

 325 |     const userE = energy / 5;
     | In `scoreTask` (src/components/TodoList.jsx): `userE`: Your energy divided by 5, so level 1 is 0.2 and level 5 is 1. Compared with taskDiff. The code is `const userE = energy / 5;`.

 326 |     const energyMatch = 1 - Math.abs(taskDiff - userE) * 0.5;
     | In `scoreTask` (src/components/TodoList.jsx): `energyMatch`: 1 when the task size matches your energy, lower when they differ. The 0.5 stops a mismatch from zeroing the score. The code is `const energyMatch = 1 - Math.abs(taskDiff - userE) * 0.5;`.

 327 |     const dreadInverse = 1 - ((t.dreadScore || 3) - 1) / 8;
     | In `scoreTask` (src/components/TodoList.jsx): `dreadInverse`: Higher when dread is low, so an easy-feeling task ranks a bit higher. Dread 1 → 1, dread 5 → 0.5. The code is `const dreadInverse = 1 - ((t.dreadScore || 3) - 1) / 8;`.

 328 |     const timeFit = (t.estimateMins || 30) <= 45 ? 1.2 : 0.9;
     | In `scoreTask` (src/components/TodoList.jsx): `timeFit`: 1.2 if the estimate is 45 minutes or less, otherwise 0.9. Short tasks are easier to start. The code is `const timeFit = (t.estimateMins || 30) <= 45 ? 1.2 : 0.9;`.

 329 |     return urgency * energyMatch * dreadInverse * timeFit;
     | In `scoreTask` (src/components/TodoList.jsx): return `return urgency * energyMatch * dreadInverse * timeFit;`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

 330 |   }
     | In `scoreTask` (src/components/TodoList.jsx): `}` closes scoreTask (opened on line 320). Names declared inside that block end here.

 331 | 
     | Blank line in `src/components/TodoList.jsx` (the task list, brain dump, and AI suggestion cards), inside TodoList. The parser skips it. It separates the previous statement from the next so the function is readable.

 332 |   const sortedTasks = [...tasks].sort((a, b) => scoreTask(b) - scoreTask(a));
     | In `TodoList` (src/components/TodoList.jsx): `sortedTasks`: A copy of the open tasks sorted by scoreTask, highest first. Index 0 is the row that gets the Next badge. The code is `const sortedTasks = [...tasks].sort((a, b) => scoreTask(b) - scoreTask(a));`.

 333 | 
     | Blank line in `src/components/TodoList.jsx` (the task list, brain dump, and AI suggestion cards), inside TodoList. The parser skips it. It separates the previous statement from the next so the function is readable.

 334 |   return (
     | In `TodoList` (src/components/TodoList.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

 335 |     <div>
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div>`

 336 |       {reward && <div className="reward-burst">{reward}</div>}
     | In `TodoList` (src/components/TodoList.jsx): `{reward && <div className="reward-burst">{reward}</div>}` closes TodoList (opened on line 144). Names declared inside that block end here.

 337 | 
     | Blank line in `src/components/TodoList.jsx` (the task list, brain dump, and AI suggestion cards), inside TodoList. The parser skips it. It separates the previous statement from the next so the function is readable.

 338 |       <div className="flex items-center justify-between mb-4" style={{ flexWrap: "wrap", gap: 12 }}>
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="flex items-center justify-between mb-4" style={{ flexWrap: "wrap", gap: 12 }}>`

 339 |         <div>
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div>`

 340 |           <h1 className="page-title">Tasks</h1>
     | In `TodoList` (src/components/TodoList.jsx): Opens it. The page title. Source: `<h1 className="page-title">Tasks</h1>`

 341 |           <p className="page-subtitle" style={{ margin: 0 }}>Brain dump, chunk, and conquer</p>
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A paragraph. Source: `<p className="page-subtitle" style={{ margin: 0 }}>Brain dump, chunk, and conquer</p>`

 342 |         </div>
     | In `TodoList` (src/components/TodoList.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 343 |         <div className="mode-tabs" style={{ margin: 0, width: "auto", flexShrink: 0 }}>
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="mode-tabs" style={{ margin: 0, width: "auto", flexShrink: 0 }}>`

 344 |           <button
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button`

 345 |             className={`mode-tab ${view === "tasks" ? "active" : ""}`}
     | In `TodoList` (src/components/TodoList.jsx): `className={`mode-tab ${view === "tasks" ? "active" : ""}`}` closes TodoList (opened on line 144). Names declared inside that block end here.

 346 |             onClick={() => setView("tasks")}
     | In `TodoList` (src/components/TodoList.jsx): event prop `onClick={() => setView("tasks")}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 347 |             aria-pressed={view === "tasks"}
     | In `TodoList` (src/components/TodoList.jsx): `aria-pressed={view === "tasks"}` closes TodoList (opened on line 144). Names declared inside that block end here.

 348 |           >
     | In `TodoList` (src/components/TodoList.jsx): statement `>`. It runs when TodoList runs, in order, before the next line of the same function.

 349 |             📋 Task List
     | In `TodoList` (src/components/TodoList.jsx): statement `📋 Task List`. It runs when TodoList runs, in order, before the next line of the same function.

 350 |           </button>
     | In `TodoList` (src/components/TodoList.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

 351 |           <button
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button`

 352 |             className={`mode-tab ${view === "dump" ? "active" : ""}`}
     | In `TodoList` (src/components/TodoList.jsx): `className={`mode-tab ${view === "dump" ? "active" : ""}`}` closes TodoList (opened on line 144). Names declared inside that block end here.

 353 |             onClick={() => setView("dump")}
     | In `TodoList` (src/components/TodoList.jsx): event prop `onClick={() => setView("dump")}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 354 |             aria-pressed={view === "dump"}
     | In `TodoList` (src/components/TodoList.jsx): `aria-pressed={view === "dump"}` closes TodoList (opened on line 144). Names declared inside that block end here.

 355 |           >
     | In `TodoList` (src/components/TodoList.jsx): statement `>`. It runs when TodoList runs, in order, before the next line of the same function.

 356 |             🧠 Brain Dump
     | In `TodoList` (src/components/TodoList.jsx): statement `🧠 Brain Dump`. It runs when TodoList runs, in order, before the next line of the same function.

 357 |           </button>
     | In `TodoList` (src/components/TodoList.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

 358 |         </div>
     | In `TodoList` (src/components/TodoList.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 359 |       </div>
     | In `TodoList` (src/components/TodoList.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 360 | 
     | Blank line in `src/components/TodoList.jsx` (the task list, brain dump, and AI suggestion cards), inside TodoList. The parser skips it. It separates the previous statement from the next so the function is readable.

 361 |       <div className="grid-main">
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="grid-main">`

 362 |         {/* ── Left Panel ────────────────────────────────── */}
     | In `TodoList` (src/components/TodoList.jsx): `{/* ── Left Panel ────────────────────────────────── */}` closes TodoList (opened on line 144). Names declared inside that block end here.

 363 |         <div className="stack">
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="stack">`

 364 |           {view === "dump" ? (
     | In `TodoList` (src/components/TodoList.jsx): statement `{view === "dump" ? (`. It runs when TodoList runs, in order, before the next line of the same function.

 365 |             <div className="card">
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="card">`

 366 |               <div className="card-title">Brain Dump</div>
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="card-title">Brain Dump</div>`

 367 |               <p className="text-sm text-muted mb-3">
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A paragraph. Source: `<p className="text-sm text-muted mb-3">`

 368 |                 Type anything — thoughts, tasks, worries. AI will parse it into structured tasks.
     | In `TodoList` (src/components/TodoList.jsx): statement `Type anything — thoughts, tasks, worries. AI will parse it into structured tasks.`. It runs when TodoList runs, in order, before the next line of the same function.

 369 |               </p>
     | In `TodoList` (src/components/TodoList.jsx): Closes it. A paragraph. Source: `</p>`

 370 |               <div className="brain-dump-wrap mb-3">
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="brain-dump-wrap mb-3">`

 371 |                 <textarea
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A multi-line box. Brain dump and rule notes use it. Source: `<textarea`

 372 |                   className="textarea"
     | In `TodoList` (src/components/TodoList.jsx): statement `className="textarea"`. It runs when TodoList runs, in order, before the next line of the same function.

 373 |                   style={{ minHeight: 160 }}
     | In `TodoList` (src/components/TodoList.jsx): `style={{ minHeight: 160 }}` closes TodoList (opened on line 144). Names declared inside that block end here.

 374 |                   placeholder="Just type whatever's in your head...&#10;&#10;e.g. Need to finish the report by Friday, call the dentist, study chapter 4 before the exam next week, also reply to Sara's email..."
     | In `TodoList` (src/components/TodoList.jsx): statement `placeholder="Just type whatever's in your head...&#10;&#10;e.g. Need to finish the report by Friday, call the dentist, study chapter 4 before the exam next week, also reply to Sara's email..."`. It runs when TodoList runs, in order, before the next line of the same function.

 375 |                   value={dumpText}
     | In `TodoList` (src/components/TodoList.jsx): `value={dumpText}` closes TodoList (opened on line 144). Names declared inside that block end here.

 376 |                   onChange={(e) => setDumpText(e.target.value)}
     | In `TodoList` (src/components/TodoList.jsx): event prop `onChange={(e) => setDumpText(e.target.value)}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 377 |                   onKeyDown={(e) => { if (e.key === "Enter" && e.ctrlKey) submitDump(); }}
     | In `TodoList` (src/components/TodoList.jsx): event prop `onKeyDown={(e) => { if (e.key === "Enter" && e.ctrlKey) submitDump(); }}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 378 |                   aria-label="Brain dump text"
     | In `TodoList` (src/components/TodoList.jsx): statement `aria-label="Brain dump text"`. It runs when TodoList runs, in order, before the next line of the same function.

 379 |                 />
     | In `TodoList` (src/components/TodoList.jsx): statement `/>`. It runs when TodoList runs, in order, before the next line of the same function.

 380 |                 <div className="brain-dump-hint">Ctrl+Enter to submit</div>
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="brain-dump-hint">Ctrl+Enter to submit</div>`

 381 |               </div>
     | In `TodoList` (src/components/TodoList.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 382 |               <div style={{ display: "flex", gap: 8 }}>
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div style={{ display: "flex", gap: 8 }}>`

 383 |                 <button
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button`

 384 |                   className="btn btn-primary"
     | In `TodoList` (src/components/TodoList.jsx): statement `className="btn btn-primary"`. It runs when TodoList runs, in order, before the next line of the same function.

 385 |                   onClick={submitDump}
     | In `TodoList` (src/components/TodoList.jsx): event prop `onClick={submitDump}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 386 |                   disabled={dumpLoading || !dumpText.trim()}
     | In `TodoList` (src/components/TodoList.jsx): `disabled={dumpLoading || !dumpText.trim()}` closes TodoList (opened on line 144). Names declared inside that block end here.

 387 |                 >
     | In `TodoList` (src/components/TodoList.jsx): statement `>`. It runs when TodoList runs, in order, before the next line of the same function.

 388 |                   {dumpLoading ? "⏳ Parsing..." : "🧠 Chunk with AI"}
     | In `TodoList` (src/components/TodoList.jsx): `{dumpLoading ? "⏳ Parsing..." : "🧠 Chunk with AI"}` closes TodoList (opened on line 144). Names declared inside that block end here.

 389 |                 </button>
     | In `TodoList` (src/components/TodoList.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

 390 |                 <button className="btn btn-ghost" onClick={() => setDumpText("")}>
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button className="btn btn-ghost" onClick={() => setDumpText("")}>`

 391 |                   Clear
     | In `TodoList` (src/components/TodoList.jsx): statement `Clear`. It runs when TodoList runs, in order, before the next line of the same function.

 392 |                 </button>
     | In `TodoList` (src/components/TodoList.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

 393 |               </div>
     | In `TodoList` (src/components/TodoList.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 394 |             </div>
     | In `TodoList` (src/components/TodoList.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 395 |           ) : (
     | In `TodoList` (src/components/TodoList.jsx): statement `) : (`. It runs when TodoList runs, in order, before the next line of the same function.

 396 |             <>
     | In `TodoList` (src/components/TodoList.jsx): JSX `<element>`. React will create this node when the parent renders. Source: `<>`

 397 |               {/* Simplified single-field add task */}
     | In `TodoList` (src/components/TodoList.jsx): `{/* Simplified single-field add task */}` closes TodoList (opened on line 144). Names declared inside that block end here.

 398 |               <AddTaskRow onAdd={add} />
     | In `TodoList` (src/components/TodoList.jsx): JSX `<AddTaskRow>`. React will create this node when the parent renders. Source: `<AddTaskRow onAdd={add} />`

 399 | 
     | Blank line in `src/components/TodoList.jsx` (the task list, brain dump, and AI suggestion cards), inside TodoList. The parser skips it. It separates the previous statement from the next so the function is readable.

 400 |               {/* Task list */}
     | In `TodoList` (src/components/TodoList.jsx): `{/* Task list */}` closes TodoList (opened on line 144). Names declared inside that block end here.

 401 |               <div className="stack-sm">
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="stack-sm">`

 402 |                 {sortedTasks.map((t, idx) => (
     | In `TodoList` (src/components/TodoList.jsx): iteration `{sortedTasks.map((t, idx) => (`.

 403 |                   <div
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div`

 404 |                     key={t._id}
     | In `TodoList` (src/components/TodoList.jsx): `key={t._id}` closes TodoList (opened on line 144). Names declared inside that block end here.

 405 |                     id={`task-${t._id}`}
     | In `TodoList` (src/components/TodoList.jsx): `id={`task-${t._id}`}` closes TodoList (opened on line 144). Names declared inside that block end here.

 406 |                     className={`task-card ${completing === t._id ? "completing" : ""}`}
     | In `TodoList` (src/components/TodoList.jsx): `className={`task-card ${completing === t._id ? "completing" : ""}`}` closes TodoList (opened on line 144). Names declared inside that block end here.

 407 |                   >
     | In `TodoList` (src/components/TodoList.jsx): statement `>`. It runs when TodoList runs, in order, before the next line of the same function.

 408 |                     {editingId === t._id ? (
     | In `TodoList` (src/components/TodoList.jsx): statement `{editingId === t._id ? (`. It runs when TodoList runs, in order, before the next line of the same function.

 409 |                       <div className="stack-sm">
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="stack-sm">`

 410 |                         <div>
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div>`

 411 |                           <label className="text-xs text-muted" style={{ display: "block", marginBottom: 4 }}>Task title</label>
     | In `TodoList` (src/components/TodoList.jsx): Opens it. The caption for an input. Source: `<label className="text-xs text-muted" style={{ display: "block", marginBottom: 4 }}>Task title</label>`

 412 |                           <input
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A text or date field. If value and onChange are set, React owns what it shows. Source: `<input`

 413 |                             className="input"
     | In `TodoList` (src/components/TodoList.jsx): statement `className="input"`. It runs when TodoList runs, in order, before the next line of the same function.

 414 |                             value={editTitle}
     | In `TodoList` (src/components/TodoList.jsx): `value={editTitle}` closes TodoList (opened on line 144). Names declared inside that block end here.

 415 |                             onChange={(e) => setEditTitle(e.target.value)}
     | In `TodoList` (src/components/TodoList.jsx): event prop `onChange={(e) => setEditTitle(e.target.value)}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 416 |                             aria-label="Edit task title"
     | In `TodoList` (src/components/TodoList.jsx): statement `aria-label="Edit task title"`. It runs when TodoList runs, in order, before the next line of the same function.

 417 |                           />
     | In `TodoList` (src/components/TodoList.jsx): statement `/>`. It runs when TodoList runs, in order, before the next line of the same function.

 418 |                         </div>
     | In `TodoList` (src/components/TodoList.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 419 |                         <div>
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div>`

 420 |                           <label className="text-xs text-muted" style={{ display: "block", marginBottom: 4 }}>Due date</label>
     | In `TodoList` (src/components/TodoList.jsx): Opens it. The caption for an input. Source: `<label className="text-xs text-muted" style={{ display: "block", marginBottom: 4 }}>Due date</label>`

 421 |                           <input
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A text or date field. If value and onChange are set, React owns what it shows. Source: `<input`

 422 |                             className="input"
     | In `TodoList` (src/components/TodoList.jsx): statement `className="input"`. It runs when TodoList runs, in order, before the next line of the same function.

 423 |                             type="datetime-local"
     | In `TodoList` (src/components/TodoList.jsx): statement `type="datetime-local"`. It runs when TodoList runs, in order, before the next line of the same function.

 424 |                             value={editDue}
     | In `TodoList` (src/components/TodoList.jsx): `value={editDue}` closes TodoList (opened on line 144). Names declared inside that block end here.

 425 |                             onChange={(e) => setEditDue(e.target.value)}
     | In `TodoList` (src/components/TodoList.jsx): event prop `onChange={(e) => setEditDue(e.target.value)}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 426 |                             aria-label="Edit due date"
     | In `TodoList` (src/components/TodoList.jsx): statement `aria-label="Edit due date"`. It runs when TodoList runs, in order, before the next line of the same function.

 427 |                           />
     | In `TodoList` (src/components/TodoList.jsx): statement `/>`. It runs when TodoList runs, in order, before the next line of the same function.

 428 |                         </div>
     | In `TodoList` (src/components/TodoList.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 429 |                         <div>
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div>`

 430 |                           <label className="text-xs text-muted" style={{ display: "block", marginBottom: 4 }}>Estimated minutes</label>
     | In `TodoList` (src/components/TodoList.jsx): Opens it. The caption for an input. Source: `<label className="text-xs text-muted" style={{ display: "block", marginBottom: 4 }}>Estimated minutes</label>`

 431 |                           <input
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A text or date field. If value and onChange are set, React owns what it shows. Source: `<input`

 432 |                             className="input"
     | In `TodoList` (src/components/TodoList.jsx): statement `className="input"`. It runs when TodoList runs, in order, before the next line of the same function.

 433 |                             type="number"
     | In `TodoList` (src/components/TodoList.jsx): statement `type="number"`. It runs when TodoList runs, in order, before the next line of the same function.

 434 |                             value={editEstimate}
     | In `TodoList` (src/components/TodoList.jsx): `value={editEstimate}` closes TodoList (opened on line 144). Names declared inside that block end here.

 435 |                             onChange={(e) => setEditEstimate(e.target.value)}
     | In `TodoList` (src/components/TodoList.jsx): event prop `onChange={(e) => setEditEstimate(e.target.value)}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 436 |                             min={1}
     | In `TodoList` (src/components/TodoList.jsx): `min={1}` closes TodoList (opened on line 144). Names declared inside that block end here.

 437 |                             aria-label="Edit estimated minutes"
     | In `TodoList` (src/components/TodoList.jsx): statement `aria-label="Edit estimated minutes"`. It runs when TodoList runs, in order, before the next line of the same function.

 438 |                           />
     | In `TodoList` (src/components/TodoList.jsx): statement `/>`. It runs when TodoList runs, in order, before the next line of the same function.

 439 |                         </div>
     | In `TodoList` (src/components/TodoList.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 440 |                         <DreadMeter score={editDread} onChange={setEditDread} />
     | In `TodoList` (src/components/TodoList.jsx): JSX `<DreadMeter>`. React will create this node when the parent renders. Source: `<DreadMeter score={editDread} onChange={setEditDread} />`

 441 |                         <div className="flex gap-2">
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="flex gap-2">`

 442 |                           <button className="btn btn-primary btn-sm" onClick={() => saveEdit(t._id)}>Save</button>
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button className="btn btn-primary btn-sm" onClick={() => saveEdit(t._id)}>Save</button>`

 443 |                           <button className="btn btn-ghost btn-sm" onClick={() => setEditingId(null)}>Cancel</button>
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button className="btn btn-ghost btn-sm" onClick={() => setEditingId(null)}>Cancel</button>`

 444 |                         </div>
     | In `TodoList` (src/components/TodoList.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 445 |                       </div>
     | In `TodoList` (src/components/TodoList.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 446 |                     ) : (
     | In `TodoList` (src/components/TodoList.jsx): statement `) : (`. It runs when TodoList runs, in order, before the next line of the same function.

 447 |                       <>
     | In `TodoList` (src/components/TodoList.jsx): JSX `<element>`. React will create this node when the parent renders. Source: `<>`

 448 |                         <div className="task-header">
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="task-header">`

 449 |                           <button
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button`

 450 |                             className="task-check"
     | In `TodoList` (src/components/TodoList.jsx): statement `className="task-check"`. It runs when TodoList runs, in order, before the next line of the same function.

 451 |                             onClick={() => complete(t._id)}
     | In `TodoList` (src/components/TodoList.jsx): event prop `onClick={() => complete(t._id)}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 452 |                             title="Mark complete"
     | In `TodoList` (src/components/TodoList.jsx): statement `title="Mark complete"`. It runs when TodoList runs, in order, before the next line of the same function.

 453 |                             aria-label={`Complete: ${t.title}`}
     | In `TodoList` (src/components/TodoList.jsx): `aria-label={`Complete: ${t.title}`}` closes TodoList (opened on line 144). Names declared inside that block end here.

 454 |                           >
     | In `TodoList` (src/components/TodoList.jsx): statement `>`. It runs when TodoList runs, in order, before the next line of the same function.

 455 |                             ✓
     | In `TodoList` (src/components/TodoList.jsx): statement `✓`. It runs when TodoList runs, in order, before the next line of the same function.

 456 |                           </button>
     | In `TodoList` (src/components/TodoList.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

 457 |                           <div className="task-title-text">
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="task-title-text">`

 458 |                             {idx === 0 && (
     | In `TodoList` (src/components/TodoList.jsx): statement `{idx === 0 && (`. It runs when TodoList runs, in order, before the next line of the same function.

 459 |                               <span className="badge badge-violet" style={{ marginRight: 6, verticalAlign: "middle" }}>
     | In `TodoList` (src/components/TodoList.jsx): Opens it. An inline box. Source: `<span className="badge badge-violet" style={{ marginRight: 6, verticalAlign: "middle" }}>`

 460 |                                 ⚡ Next
     | In `TodoList` (src/components/TodoList.jsx): statement `⚡ Next`. It runs when TodoList runs, in order, before the next line of the same function.

 461 |                               </span>
     | In `TodoList` (src/components/TodoList.jsx): Closes it. An inline box. Source: `</span>`

 462 |                             )}
     | In `TodoList` (src/components/TodoList.jsx): `)}` closes TodoList (opened on line 144). Names declared inside that block end here.

 463 |                             {t.title}
     | In `TodoList` (src/components/TodoList.jsx): `{t.title}` closes TodoList (opened on line 144). Names declared inside that block end here.

 464 |                           </div>
     | In `TodoList` (src/components/TodoList.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 465 |                           <PriorityBadge level={t.aiPriority} />
     | In `TodoList` (src/components/TodoList.jsx): JSX `<PriorityBadge>`. React will create this node when the parent renders. Source: `<PriorityBadge level={t.aiPriority} />`

 466 |                         </div>
     | In `TodoList` (src/components/TodoList.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 467 | 
     | Blank line in `src/components/TodoList.jsx` (the task list, brain dump, and AI suggestion cards), inside TodoList. The parser skips it. It separates the previous statement from the next so the function is readable.

 468 |                         <div className="task-meta">
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="task-meta">`

 469 |                           {t.dueAt && (
     | In `TodoList` (src/components/TodoList.jsx): statement `{t.dueAt && (`. It runs when TodoList runs, in order, before the next line of the same function.

 470 |                             <span style={{ color: (new Date(t.dueAt) - new Date()) / 3600000 < 24 ? "var(--red)" : "var(--muted)" }}>
     | In `TodoList` (src/components/TodoList.jsx): Opens it. An inline box. Source: `<span style={{ color: (new Date(t.dueAt) - new Date()) / 3600000 < 24 ? "var(--red)" : "var(--muted)" }}>`

 471 |                               📅 {fmtDue(t.dueAt)}
     | In `TodoList` (src/components/TodoList.jsx): `📅 {fmtDue(t.dueAt)}` closes TodoList (opened on line 144). Names declared inside that block end here.

 472 |                             </span>
     | In `TodoList` (src/components/TodoList.jsx): Closes it. An inline box. Source: `</span>`

 473 |                           )}
     | In `TodoList` (src/components/TodoList.jsx): `)}` closes TodoList (opened on line 144). Names declared inside that block end here.

 474 |                           {t.estimateMins && <span>⏱ ~{t.estimateMins}m</span>}
     | In `TodoList` (src/components/TodoList.jsx): `{t.estimateMins && <span>⏱ ~{t.estimateMins}m</span>}` closes TodoList (opened on line 144). Names declared inside that block end here.

 475 |                           <DreadMeter score={t.dreadScore || 3} onChange={(n) => updateDread(t._id, n)} />
     | In `TodoList` (src/components/TodoList.jsx): JSX `<DreadMeter>`. React will create this node when the parent renders. Source: `<DreadMeter score={t.dreadScore || 3} onChange={(n) => updateDread(t._id, n)} />`

 476 |                         </div>
     | In `TodoList` (src/components/TodoList.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 477 | 
     | Blank line in `src/components/TodoList.jsx` (the task list, brain dump, and AI suggestion cards), inside TodoList. The parser skips it. It separates the previous statement from the next so the function is readable.

 478 |                         {t.subtasks?.length > 0 && (
     | In `TodoList` (src/components/TodoList.jsx): statement `{t.subtasks?.length > 0 && (`. It runs when TodoList runs, in order, before the next line of the same function.

 479 |                           <div className="subtask-list">
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="subtask-list">`

 480 |                             {t.subtasks.map((s, i) => (
     | In `TodoList` (src/components/TodoList.jsx): iteration `{t.subtasks.map((s, i) => (`.

 481 |                               <div key={i} className="subtask-item">
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div key={i} className="subtask-item">`

 482 |                                 <div className="subtask-dot" />
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="subtask-dot" />`

 483 |                                 {s.title}
     | In `TodoList` (src/components/TodoList.jsx): `{s.title}` closes TodoList (opened on line 144). Names declared inside that block end here.

 484 |                               </div>
     | In `TodoList` (src/components/TodoList.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 485 |                             ))}
     | In `TodoList` (src/components/TodoList.jsx): `))}` closes TodoList (opened on line 144). Names declared inside that block end here.

 486 |                           </div>
     | In `TodoList` (src/components/TodoList.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 487 |                         )}
     | In `TodoList` (src/components/TodoList.jsx): `)}` closes TodoList (opened on line 144). Names declared inside that block end here.

 488 | 
     | Blank line in `src/components/TodoList.jsx` (the task list, brain dump, and AI suggestion cards), inside TodoList. The parser skips it. It separates the previous statement from the next so the function is readable.

 489 |                         <div className="task-actions">
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="task-actions">`

 490 |                           <button className="btn btn-success btn-sm" onClick={() => complete(t._id)}>✓ Done</button>
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button className="btn btn-success btn-sm" onClick={() => complete(t._id)}>✓ Done</button>`

 491 |                           <button className="btn btn-secondary btn-sm" onClick={() => autoChunk(t)}>✂ Chunk</button>
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button className="btn btn-secondary btn-sm" onClick={() => autoChunk(t)}>✂ Chunk</button>`

 492 |                           <button
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button`

 493 |                             className="btn btn-ghost btn-sm"
     | In `TodoList` (src/components/TodoList.jsx): statement `className="btn btn-ghost btn-sm"`. It runs when TodoList runs, in order, before the next line of the same function.

 494 |                             onClick={() => {
     | In `TodoList` (src/components/TodoList.jsx): event prop `onClick={() => {`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 495 |                               setEditingId(t._id);
     | In `TodoList` (src/components/TodoList.jsx): statement `setEditingId(t._id);`. It runs when TodoList runs, in order, before the next line of the same function.

 496 |                               setEditTitle(t.title);
     | In `TodoList` (src/components/TodoList.jsx): statement `setEditTitle(t.title);`. It runs when TodoList runs, in order, before the next line of the same function.

 497 |                               setEditDue(t.dueAt ? t.dueAt.slice(0, 16) : "");
     | In `TodoList` (src/components/TodoList.jsx): statement `setEditDue(t.dueAt ? t.dueAt.slice(0, 16) : "");`. It runs when TodoList runs, in order, before the next line of the same function.

 498 |                               setEditEstimate(t.estimateMins || 30);
     | In `TodoList` (src/components/TodoList.jsx): statement `setEditEstimate(t.estimateMins || 30);`. It runs when TodoList runs, in order, before the next line of the same function.

 499 |                               setEditDread(t.dreadScore || 3);
     | In `TodoList` (src/components/TodoList.jsx): statement `setEditDread(t.dreadScore || 3);`. It runs when TodoList runs, in order, before the next line of the same function.

 500 |                             }}
     | In `TodoList` (src/components/TodoList.jsx): `}}` closes onClick={() => { (opened on line 494). Names declared inside that block end here.

 501 |                           >
     | In `TodoList` (src/components/TodoList.jsx): statement `>`. It runs when TodoList runs, in order, before the next line of the same function.

 502 |                             ✎ Edit
     | In `TodoList` (src/components/TodoList.jsx): statement `✎ Edit`. It runs when TodoList runs, in order, before the next line of the same function.

 503 |                           </button>
     | In `TodoList` (src/components/TodoList.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

 504 |                         </div>
     | In `TodoList` (src/components/TodoList.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 505 |                       </>
     | In `TodoList` (src/components/TodoList.jsx): JSX `<element>`. This closes that element. Source: `</>`

 506 |                     )}
     | In `TodoList` (src/components/TodoList.jsx): `)}` closes TodoList (opened on line 144). Names declared inside that block end here.

 507 |                   </div>
     | In `TodoList` (src/components/TodoList.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 508 |                 ))}
     | In `TodoList` (src/components/TodoList.jsx): `))}` closes TodoList (opened on line 144). Names declared inside that block end here.

 509 | 
     | Blank line in `src/components/TodoList.jsx` (the task list, brain dump, and AI suggestion cards), inside TodoList. The parser skips it. It separates the previous statement from the next so the function is readable.

 510 |                 {/* Empty state with direct CTA */}
     | In `TodoList` (src/components/TodoList.jsx): `{/* Empty state with direct CTA */}` closes TodoList (opened on line 144). Names declared inside that block end here.

 511 |                 {tasks.length === 0 && (
     | In `TodoList` (src/components/TodoList.jsx): statement `{tasks.length === 0 && (`. It runs when TodoList runs, in order, before the next line of the same function.

 512 |                   <div className="empty-state">
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="empty-state">`

 513 |                     <div className="empty-state-icon">📭</div>
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="empty-state-icon">📭</div>`

 514 |                     <div className="empty-state-title">No tasks yet</div>
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="empty-state-title">No tasks yet</div>`

 515 |                     <div className="empty-state-body">
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="empty-state-body">`

 516 |                       Try the Brain Dump — type everything on your mind and AI will turn it into tasks.
     | In `TodoList` (src/components/TodoList.jsx): statement `Try the Brain Dump — type everything on your mind and AI will turn it into tasks.`. It runs when TodoList runs, in order, before the next line of the same function.

 517 |                     </div>
     | In `TodoList` (src/components/TodoList.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 518 |                     <button className="btn btn-primary" onClick={() => setView("dump")}>
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button className="btn btn-primary" onClick={() => setView("dump")}>`

 519 |                       🧠 Start Brain Dump
     | In `TodoList` (src/components/TodoList.jsx): statement `🧠 Start Brain Dump`. It runs when TodoList runs, in order, before the next line of the same function.

 520 |                     </button>
     | In `TodoList` (src/components/TodoList.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

 521 |                   </div>
     | In `TodoList` (src/components/TodoList.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 522 |                 )}
     | In `TodoList` (src/components/TodoList.jsx): `)}` closes TodoList (opened on line 144). Names declared inside that block end here.

 523 |               </div>
     | In `TodoList` (src/components/TodoList.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 524 |             </>
     | In `TodoList` (src/components/TodoList.jsx): JSX `<element>`. This closes that element. Source: `</>`

 525 |           )}
     | In `TodoList` (src/components/TodoList.jsx): `)}` closes TodoList (opened on line 144). Names declared inside that block end here.

 526 |         </div>
     | In `TodoList` (src/components/TodoList.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 527 | 
     | Blank line in `src/components/TodoList.jsx` (the task list, brain dump, and AI suggestion cards), inside TodoList. The parser skips it. It separates the previous statement from the next so the function is readable.

 528 |         {/* ── Right Panel: AI Suggestions ──────────────── */}
     | In `TodoList` (src/components/TodoList.jsx): `{/* ── Right Panel: AI Suggestions ──────────────── */}` closes TodoList (opened on line 144). Names declared inside that block end here.

 529 |         <aside className="stack">
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A side column. Source: `<aside className="stack">`

 530 |           <div className="card">
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="card">`

 531 |             <div className="flex items-center justify-between mb-3">
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="flex items-center justify-between mb-3">`

 532 |               <div className="card-title" style={{ margin: 0 }}>AI Suggestions</div>
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="card-title" style={{ margin: 0 }}>AI Suggestions</div>`

 533 |               <button
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button`

 534 |                 className="btn btn-ghost btn-sm"
     | In `TodoList` (src/components/TodoList.jsx): statement `className="btn btn-ghost btn-sm"`. It runs when TodoList runs, in order, before the next line of the same function.

 535 |                 onClick={fetchSuggestions}
     | In `TodoList` (src/components/TodoList.jsx): event prop `onClick={fetchSuggestions}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 536 |                 disabled={suggestionsLoading}
     | In `TodoList` (src/components/TodoList.jsx): `disabled={suggestionsLoading}` closes TodoList (opened on line 144). Names declared inside that block end here.

 537 |                 aria-label="Refresh suggestions"
     | In `TodoList` (src/components/TodoList.jsx): statement `aria-label="Refresh suggestions"`. It runs when TodoList runs, in order, before the next line of the same function.

 538 |               >
     | In `TodoList` (src/components/TodoList.jsx): statement `>`. It runs when TodoList runs, in order, before the next line of the same function.

 539 |                 {suggestionsLoading ? "..." : "↺"}
     | In `TodoList` (src/components/TodoList.jsx): `{suggestionsLoading ? "..." : "↺"}` closes TodoList (opened on line 144). Names declared inside that block end here.

 540 |               </button>
     | In `TodoList` (src/components/TodoList.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

 541 |             </div>
     | In `TodoList` (src/components/TodoList.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 542 | 
     | Blank line in `src/components/TodoList.jsx` (the task list, brain dump, and AI suggestion cards), inside TodoList. The parser skips it. It separates the previous statement from the next so the function is readable.

 543 |             {suggestionsLoading && suggestions.length === 0 && (
     | In `TodoList` (src/components/TodoList.jsx): statement `{suggestionsLoading && suggestions.length === 0 && (`. It runs when TodoList runs, in order, before the next line of the same function.

 544 |               <div className="text-sm text-muted" style={{ textAlign: "center", padding: 20 }}>
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="text-sm text-muted" style={{ textAlign: "center", padding: 20 }}>`

 545 |                 Analysing tasks...
     | In `TodoList` (src/components/TodoList.jsx): statement `Analysing tasks...`. It runs when TodoList runs, in order, before the next line of the same function.

 546 |               </div>
     | In `TodoList` (src/components/TodoList.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 547 |             )}
     | In `TodoList` (src/components/TodoList.jsx): `)}` closes TodoList (opened on line 144). Names declared inside that block end here.

 548 | 
     | Blank line in `src/components/TodoList.jsx` (the task list, brain dump, and AI suggestion cards), inside TodoList. The parser skips it. It separates the previous statement from the next so the function is readable.

 549 |             {suggestions.length > 0 ? (
     | In `TodoList` (src/components/TodoList.jsx): statement `{suggestions.length > 0 ? (`. It runs when TodoList runs, in order, before the next line of the same function.

 550 |               <div className="stack-sm">
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="stack-sm">`

 551 |                 {suggestions.map((s) => (
     | In `TodoList` (src/components/TodoList.jsx): iteration `{suggestions.map((s) => (`.

 552 |                   <div
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div`

 553 |                     key={s.id}
     | In `TodoList` (src/components/TodoList.jsx): `key={s.id}` closes TodoList (opened on line 144). Names declared inside that block end here.

 554 |                     style={{ borderRadius: "var(--radius-sm)", padding: "12px 14px", ...SUGGESTION_STYLES[s.type] }}
     | In `TodoList` (src/components/TodoList.jsx): `style={{ borderRadius: "var(--radius-sm)", padding: "12px 14px", ...SUGGESTION_STYLES[s.type] }}` closes TodoList (opened on line 144). Names declared inside that block end here.

 555 |                   >
     | In `TodoList` (src/components/TodoList.jsx): statement `>`. It runs when TodoList runs, in order, before the next line of the same function.

 556 |                     <div className="text-xs font-bold" style={{ textTransform: "uppercase", letterSpacing: "0.5px", color: "var(--muted)", marginBottom: 4 }}>
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="text-xs font-bold" style={{ textTransform: "uppercase", letterSpacing: "0.5px", color: "var(--muted)", marginBottom: 4 }}>`

 557 |                       {SUGGESTION_LABELS[s.type] || "Tip"}
     | In `TodoList` (src/components/TodoList.jsx): `{SUGGESTION_LABELS[s.type] || "Tip"}` closes TodoList (opened on line 144). Names declared inside that block end here.

 558 |                     </div>
     | In `TodoList` (src/components/TodoList.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 559 |                     <div className="font-semibold text-sm mb-1">{s.title}</div>
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="font-semibold text-sm mb-1">{s.title}</div>`

 560 |                     <div className="text-sm text-muted mb-3" style={{ lineHeight: 1.5 }}>{s.description}</div>
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="text-sm text-muted mb-3" style={{ lineHeight: 1.5 }}>{s.description}</div>`

 561 |                     <div className="flex gap-2">
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="flex gap-2">`

 562 |                       <button className="btn btn-primary btn-sm" onClick={() => acceptSuggestion(s)}>Accept</button>
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button className="btn btn-primary btn-sm" onClick={() => acceptSuggestion(s)}>Accept</button>`

 563 |                       <button className="btn btn-ghost btn-sm" onClick={() => dismissSuggestion(s)}>Dismiss</button>
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button className="btn btn-ghost btn-sm" onClick={() => dismissSuggestion(s)}>Dismiss</button>`

 564 |                     </div>
     | In `TodoList` (src/components/TodoList.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 565 |                   </div>
     | In `TodoList` (src/components/TodoList.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 566 |                 ))}
     | In `TodoList` (src/components/TodoList.jsx): `))}` closes TodoList (opened on line 144). Names declared inside that block end here.

 567 |               </div>
     | In `TodoList` (src/components/TodoList.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 568 |             ) : (
     | In `TodoList` (src/components/TodoList.jsx): statement `) : (`. It runs when TodoList runs, in order, before the next line of the same function.

 569 |               !suggestionsLoading && (
     | In `TodoList` (src/components/TodoList.jsx): statement `!suggestionsLoading && (`. It runs when TodoList runs, in order, before the next line of the same function.

 570 |                 /* Empty suggestions state — don't send users elsewhere */
     | Comment inside TodoList. Not executed. Text: /* Empty suggestions state — don't send users elsewhere */

 571 |                 <div className="empty-state" style={{ padding: "16px 0" }}>
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="empty-state" style={{ padding: "16px 0" }}>`

 572 |                   <div style={{ fontSize: 28, marginBottom: 8 }}>✨</div>
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div style={{ fontSize: 28, marginBottom: 8 }}>✨</div>`

 573 |                   <div className="text-sm text-muted" style={{ textAlign: "center", lineHeight: 1.6 }}>
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="text-sm text-muted" style={{ textAlign: "center", lineHeight: 1.6 }}>`

 574 |                     {tasks.length === 0
     | In `TodoList` (src/components/TodoList.jsx): statement `{tasks.length === 0`. It runs when TodoList runs, in order, before the next line of the same function.

 575 |                       ? "Add your first task to get AI-powered suggestions."
     | In `TodoList` (src/components/TodoList.jsx): statement `? "Add your first task to get AI-powered suggestions."`. It runs when TodoList runs, in order, before the next line of the same function.

 576 |                       : "You're all caught up. Keep going!"}
     | In `TodoList` (src/components/TodoList.jsx): `: "You're all caught up. Keep going!"}` closes TodoList (opened on line 144). Names declared inside that block end here.

 577 |                   </div>
     | In `TodoList` (src/components/TodoList.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 578 |                 </div>
     | In `TodoList` (src/components/TodoList.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 579 |               )
     | In `TodoList` (src/components/TodoList.jsx): statement `)`. It runs when TodoList runs, in order, before the next line of the same function.

 580 |             )}
     | In `TodoList` (src/components/TodoList.jsx): `)}` closes TodoList (opened on line 144). Names declared inside that block end here.

 581 |           </div>
     | In `TodoList` (src/components/TodoList.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 582 | 
     | Blank line in `src/components/TodoList.jsx` (the task list, brain dump, and AI suggestion cards), inside TodoList. The parser skips it. It separates the previous statement from the next so the function is readable.

 583 |           <div className="card card-sm">
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="card card-sm">`

 584 |             <div className="card-title">Energy context</div>
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="card-title">Energy context</div>`

 585 |             <div className="text-sm text-muted" style={{ lineHeight: 1.6 }}>
     | In `TodoList` (src/components/TodoList.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="text-sm text-muted" style={{ lineHeight: 1.6 }}>`

 586 |               Tasks are ranked for your current energy.{" "}
     | In `TodoList` (src/components/TodoList.jsx): `Tasks are ranked for your current energy.{" "}` closes TodoList (opened on line 144). Names declared inside that block end here.

 587 |               <span style={{ color: "var(--amber)" }}>⚡ Next</span> shows your best match.
     | In `TodoList` (src/components/TodoList.jsx): Opens it. An inline box. Source: `<span style={{ color: "var(--amber)" }}>⚡ Next</span> shows your best match.`

 588 |             </div>
     | In `TodoList` (src/components/TodoList.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 589 |           </div>
     | In `TodoList` (src/components/TodoList.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 590 |         </aside>
     | In `TodoList` (src/components/TodoList.jsx): Closes it. A side column. Source: `</aside>`

 591 |       </div>
     | In `TodoList` (src/components/TodoList.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 592 |     </div>
     | In `TodoList` (src/components/TodoList.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 593 |   );
     | In `TodoList` (src/components/TodoList.jsx): statement `);`. It runs when TodoList runs, in order, before the next line of the same function.

 594 | }
     | In `TodoList` (src/components/TodoList.jsx): `}` closes TodoList (opened on line 144). Names declared inside that block end here.

