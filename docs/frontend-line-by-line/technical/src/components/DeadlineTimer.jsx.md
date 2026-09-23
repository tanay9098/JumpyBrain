# `src/components/DeadlineTimer.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import React, { useEffect, useState } from "react";
     | Import for the list of tasks that have due dates: `import React, { useEffect, useState } from "react";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   2 | import { useNavigate } from "react-router-dom";
     | Import for the list of tasks that have due dates: `import { useNavigate } from "react-router-dom";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   3 | 
     | Blank line in `src/components/DeadlineTimer.jsx` (the list of tasks that have due dates), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   4 | import api from "../services/api";
     | Import for the list of tasks that have due dates: `import api from "../services/api";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   5 | 
     | Blank line in `src/components/DeadlineTimer.jsx` (the list of tasks that have due dates), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   6 | export default function DeadlineTimer(){
     | Defines `DeadlineTimer` in the list of tasks that have due dates. Lists tasks that have dueAt. Reschedule navigates to /calendar. It does not edit the date itself.

   7 |   const navigate = useNavigate();
     | In `DeadlineTimer` (src/components/DeadlineTimer.jsx): `navigate` is assigned `useNavigate();`. Later lines in this function read that name.

   8 | 
     | Blank line in `src/components/DeadlineTimer.jsx` (the list of tasks that have due dates), inside DeadlineTimer. The parser skips it. It separates the previous statement from the next so the function is readable.

   9 |   const [tasks, setTasks] = useState([]);
     | In `DeadlineTimer` (src/components/DeadlineTimer.jsx): React state `tasks, setTasks`. The value survives re-renders. Calling the setter re-renders this component. `const [tasks, setTasks] = useState([]);`

  10 | 
     | Blank line in `src/components/DeadlineTimer.jsx` (the list of tasks that have due dates), inside DeadlineTimer. The parser skips it. It separates the previous statement from the next so the function is readable.

  11 |   useEffect(()=>{ load(); }, []);
     | In `DeadlineTimer` (src/components/DeadlineTimer.jsx): opens or continues an effect — `useEffect(()=>{ load(); }, []);`. The effect body runs after paint, and its cleanup runs before the next effect and on unmount.

  12 | 
     | Blank line in `src/components/DeadlineTimer.jsx` (the list of tasks that have due dates), inside DeadlineTimer. The parser skips it. It separates the previous statement from the next so the function is readable.

  13 |   async function load(){
     | Defines `load` in the list of tasks that have due dates. GET /tasks and, on the task page, keeps only tasks that are not completed. Calendar and the deadline page keep a wider set.

  14 |     const res = await api.get("/tasks");
     | In `load` (src/components/DeadlineTimer.jsx): `res` is assigned `await api.get("/tasks");`. Later lines in this function read that name.

  15 |     const upcoming = res.tasks.filter(t => t.dueAt);
     | In `load` (src/components/DeadlineTimer.jsx): `upcoming` is assigned `res.tasks.filter(t => t.dueAt);`. Later lines in this function read that name.

  16 |     setTasks(upcoming);
     | In `load` (src/components/DeadlineTimer.jsx): statement `setTasks(upcoming);`. It runs when load runs, in order, before the next line of the same function.

  17 |   }
     | In `load` (src/components/DeadlineTimer.jsx): `}` closes load (opened on line 13). Names declared inside that block end here.

  18 | 
     | Blank line in `src/components/DeadlineTimer.jsx` (the list of tasks that have due dates), inside DeadlineTimer. The parser skips it. It separates the previous statement from the next so the function is readable.

  19 |   function fmtDue(d) {
     | Defines `fmtDue` in the list of tasks that have due dates. Overdue, 'due in Nh' under 24 hours, or a calendar date.

  20 |     const dt = new Date(d);
     | In `fmtDue` (src/components/DeadlineTimer.jsx): `dt` is assigned `new Date(d);`. Later lines in this function read that name.

  21 |     const h = (dt - new Date()) / 3600000;
     | In `fmtDue` (src/components/DeadlineTimer.jsx): `h` is assigned `(dt - new Date()) / 3600000;`. Later lines in this function read that name.

  22 |     if (h < 0) return { label: "Overdue!", color: "var(--red)" };
     | In `fmtDue` (src/components/DeadlineTimer.jsx): branch `if (h < 0) return { label: "Overdue!", color: "var(--red)" };`. Only one side runs.

  23 |     if (h < 24) return { label: `Due in ~${Math.round(h)}h`, color: "var(--amber)" };
     | In `fmtDue` (src/components/DeadlineTimer.jsx): branch `if (h < 24) return { label: `Due in ~${Math.round(h)}h`, color: "var(--amber)" };`. Only one side runs.

  24 |     return { label: dt.toLocaleDateString(), color: "var(--muted)" };
     | In `fmtDue` (src/components/DeadlineTimer.jsx): return `return { label: dt.toLocaleDateString(), color: "var(--muted)" };`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  25 |   }
     | In `fmtDue` (src/components/DeadlineTimer.jsx): `}` closes fmtDue (opened on line 19). Names declared inside that block end here.

  26 | 
     | Blank line in `src/components/DeadlineTimer.jsx` (the list of tasks that have due dates), inside DeadlineTimer. The parser skips it. It separates the previous statement from the next so the function is readable.

  27 |   return (
     | In `DeadlineTimer` (src/components/DeadlineTimer.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  28 |     <div>
     | In `DeadlineTimer` (src/components/DeadlineTimer.jsx): Opens it. A box that groups the elements inside it. Source: `<div>`

  29 |       <h1 className="page-title">Deadlines</h1>
     | In `DeadlineTimer` (src/components/DeadlineTimer.jsx): Opens it. The page title. Source: `<h1 className="page-title">Deadlines</h1>`

  30 |       <p className="page-subtitle">Upcoming due dates from your tasks</p>
     | In `DeadlineTimer` (src/components/DeadlineTimer.jsx): Opens it. A paragraph. Source: `<p className="page-subtitle">Upcoming due dates from your tasks</p>`

  31 | 
     | Blank line in `src/components/DeadlineTimer.jsx` (the list of tasks that have due dates), inside DeadlineTimer. The parser skips it. It separates the previous statement from the next so the function is readable.

  32 |       <div className="grid-main">
     | In `DeadlineTimer` (src/components/DeadlineTimer.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="grid-main">`

  33 |         <div className="stack">
     | In `DeadlineTimer` (src/components/DeadlineTimer.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="stack">`

  34 |           {tasks.length === 0 ? (
     | In `DeadlineTimer` (src/components/DeadlineTimer.jsx): statement `{tasks.length === 0 ? (`. It runs when DeadlineTimer runs, in order, before the next line of the same function.

  35 |             <div className="card" style={{ textAlign: "center", padding: 40, color: "var(--muted)" }}>
     | In `DeadlineTimer` (src/components/DeadlineTimer.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="card" style={{ textAlign: "center", padding: 40, color: "var(--muted)" }}>`

  36 |               <div style={{ fontSize: 28, marginBottom: 8 }}>📭</div>
     | In `DeadlineTimer` (src/components/DeadlineTimer.jsx): Opens it. A box that groups the elements inside it. Source: `<div style={{ fontSize: 28, marginBottom: 8 }}>📭</div>`

  37 |               No deadlines found. Add a due date to a task to see it here.
     | In `DeadlineTimer` (src/components/DeadlineTimer.jsx): statement `No deadlines found. Add a due date to a task to see it here.`. It runs when DeadlineTimer runs, in order, before the next line of the same function.

  38 |             </div>
     | In `DeadlineTimer` (src/components/DeadlineTimer.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  39 |           ) : (
     | In `DeadlineTimer` (src/components/DeadlineTimer.jsx): statement `) : (`. It runs when DeadlineTimer runs, in order, before the next line of the same function.

  40 |             tasks.map((t) => {
     | In `DeadlineTimer` (src/components/DeadlineTimer.jsx): iteration `tasks.map((t) => {`.

  41 |               const due = fmtDue(t.dueAt);
     | In `DeadlineTimer` (src/components/DeadlineTimer.jsx): `due` is assigned `fmtDue(t.dueAt);`. Later lines in this function read that name.

  42 |               return (
     | In `DeadlineTimer` (src/components/DeadlineTimer.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  43 |                 <div className="card" key={t._id}>
     | In `DeadlineTimer` (src/components/DeadlineTimer.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="card" key={t._id}>`

  44 |                   <div className="flex items-center justify-between">
     | In `DeadlineTimer` (src/components/DeadlineTimer.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="flex items-center justify-between">`

  45 |                     <div>
     | In `DeadlineTimer` (src/components/DeadlineTimer.jsx): Opens it. A box that groups the elements inside it. Source: `<div>`

  46 |                       <div className="font-semibold mb-1">{t.title}</div>
     | In `DeadlineTimer` (src/components/DeadlineTimer.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="font-semibold mb-1">{t.title}</div>`

  47 |                       <div className="text-sm" style={{ color: due.color }}>{due.label}</div>
     | In `DeadlineTimer` (src/components/DeadlineTimer.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="text-sm" style={{ color: due.color }}>{due.label}</div>`

  48 |                     </div>
     | In `DeadlineTimer` (src/components/DeadlineTimer.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  49 |                     <button
     | In `DeadlineTimer` (src/components/DeadlineTimer.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button`

  50 |                       className="btn btn-ghost btn-sm"
     | In `DeadlineTimer` (src/components/DeadlineTimer.jsx): statement `className="btn btn-ghost btn-sm"`. It runs when DeadlineTimer runs, in order, before the next line of the same function.

  51 |                       onClick={() => navigate("/calendar")}
     | In `DeadlineTimer` (src/components/DeadlineTimer.jsx): event prop `onClick={() => navigate("/calendar")}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

  52 |                     >
     | In `DeadlineTimer` (src/components/DeadlineTimer.jsx): statement `>`. It runs when DeadlineTimer runs, in order, before the next line of the same function.

  53 |                       📅 Reschedule
     | In `DeadlineTimer` (src/components/DeadlineTimer.jsx): statement `📅 Reschedule`. It runs when DeadlineTimer runs, in order, before the next line of the same function.

  54 |                     </button>
     | In `DeadlineTimer` (src/components/DeadlineTimer.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

  55 |                   </div>
     | In `DeadlineTimer` (src/components/DeadlineTimer.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  56 |                 </div>
     | In `DeadlineTimer` (src/components/DeadlineTimer.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  57 |               );
     | In `DeadlineTimer` (src/components/DeadlineTimer.jsx): statement `);`. It runs when DeadlineTimer runs, in order, before the next line of the same function.

  58 |             })
     | In `DeadlineTimer` (src/components/DeadlineTimer.jsx): `})` closes tasks.map((t) => { (opened on line 40). Names declared inside that block end here.

  59 |           )}
     | In `DeadlineTimer` (src/components/DeadlineTimer.jsx): `)}` closes DeadlineTimer (opened on line 6). Names declared inside that block end here.

  60 |         </div>
     | In `DeadlineTimer` (src/components/DeadlineTimer.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  61 | 
     | Blank line in `src/components/DeadlineTimer.jsx` (the list of tasks that have due dates), inside DeadlineTimer. The parser skips it. It separates the previous statement from the next so the function is readable.

  62 |         <aside className="card" style={{ alignSelf: "flex-start" }}>
     | In `DeadlineTimer` (src/components/DeadlineTimer.jsx): Opens it. A side column. Source: `<aside className="card" style={{ alignSelf: "flex-start" }}>`

  63 |           <div className="card-title">Tip</div>
     | In `DeadlineTimer` (src/components/DeadlineTimer.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="card-title">Tip</div>`

  64 |           <div className="text-sm text-muted" style={{ lineHeight: 1.7 }}>
     | In `DeadlineTimer` (src/components/DeadlineTimer.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="text-sm text-muted" style={{ lineHeight: 1.7 }}>`

  65 |             Add due dates to tasks to see them here and on the Calendar.
     | In `DeadlineTimer` (src/components/DeadlineTimer.jsx): statement `Add due dates to tasks to see them here and on the Calendar.`. It runs when DeadlineTimer runs, in order, before the next line of the same function.

  66 |             <br /><br />
     | In `DeadlineTimer` (src/components/DeadlineTimer.jsx): JSX `<br>`. React will create this node when the parent renders. Source: `<br /><br />`

  67 |             Tasks due within 24 hours show in amber. Overdue tasks show in red.
     | In `DeadlineTimer` (src/components/DeadlineTimer.jsx): statement `Tasks due within 24 hours show in amber. Overdue tasks show in red.`. It runs when DeadlineTimer runs, in order, before the next line of the same function.

  68 |           </div>
     | In `DeadlineTimer` (src/components/DeadlineTimer.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  69 |         </aside>
     | In `DeadlineTimer` (src/components/DeadlineTimer.jsx): Closes it. A side column. Source: `</aside>`

  70 |       </div>
     | In `DeadlineTimer` (src/components/DeadlineTimer.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  71 |     </div>
     | In `DeadlineTimer` (src/components/DeadlineTimer.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  72 |   );
     | In `DeadlineTimer` (src/components/DeadlineTimer.jsx): statement `);`. It runs when DeadlineTimer runs, in order, before the next line of the same function.

  73 | }
     | In `DeadlineTimer` (src/components/DeadlineTimer.jsx): `}` closes DeadlineTimer (opened on line 6). Names declared inside that block end here.

