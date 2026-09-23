# `src/components/DeadlineTimer.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import React, { useEffect, useState } from "react";
     | Borrows React so this file can remember things and draw the screen.

   2 | import { useNavigate } from "react-router-dom";
     | Borrows React so this file can remember things and draw the screen.

   3 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   4 | import api from "../services/api";
     | This file borrows a tool another file already made.

   5 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   6 | export default function DeadlineTimer(){
     | This starts DeadlineTimer. Lists tasks that have dueAt. Reschedule navigates to /calendar. It does not edit the date itself.

   7 |   const navigate = useNavigate();
     | This gives a short name to a value so the rest of DeadlineTimer can use it.

   8 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   9 |   const [tasks, setTasks] = useState([]);
     | This gives a short name to a value so the rest of DeadlineTimer can use it.

  10 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  11 |   useEffect(()=>{ load(); }, []);
     | This is an extra job that happens after the picture is drawn.

  12 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  13 |   async function load(){
     | This starts load. GET /tasks and, on the task page, keeps only tasks that are not completed. Calendar and the deadline page keep a wider set.

  14 |     const res = await api.get("/tasks");
     | This gives a short name to a value so the rest of load can use it.

  15 |     const upcoming = res.tasks.filter(t => t.dueAt);
     | This gives a short name to a value so the rest of load can use it.

  16 |     setTasks(upcoming);
     | Inside load, this line runs as written: setTasks(upcoming);. It happens in order, after the line above it and before the line below it.

  17 |   }
     | This ends load (opened on line 13).

  18 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  19 |   function fmtDue(d) {
     | This starts fmtDue. Overdue, 'due in Nh' under 24 hours, or a calendar date.

  20 |     const dt = new Date(d);
     | This gives a short name to a value so the rest of fmtDue can use it.

  21 |     const h = (dt - new Date()) / 3600000;
     | This gives a short name to a value so the rest of fmtDue can use it.

  22 |     if (h < 0) return { label: "Overdue!", color: "var(--red)" };
     | This asks a yes-or-no question. The next bit runs only on yes.

  23 |     if (h < 24) return { label: `Due in ~${Math.round(h)}h`, color: "var(--amber)" };
     | This asks a yes-or-no question. The next bit runs only on yes.

  24 |     return { label: dt.toLocaleDateString(), color: "var(--muted)" };
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  25 |   }
     | This ends fmtDue (opened on line 19).

  26 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  27 |   return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  28 |     <div>
     | This draws one piece of the page while DeadlineTimer is showing.

  29 |       <h1 className="page-title">Deadlines</h1>
     | This draws one piece of the page while DeadlineTimer is showing.

  30 |       <p className="page-subtitle">Upcoming due dates from your tasks</p>
     | This draws one piece of the page while DeadlineTimer is showing.

  31 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  32 |       <div className="grid-main">
     | This draws one piece of the page while DeadlineTimer is showing.

  33 |         <div className="stack">
     | This draws one piece of the page while DeadlineTimer is showing.

  34 |           {tasks.length === 0 ? (
     | Inside DeadlineTimer, this line runs as written: {tasks.length === 0 ? (. It happens in order, after the line above it and before the line below it.

  35 |             <div className="card" style={{ textAlign: "center", padding: 40, color: "var(--muted)" }}>
     | This draws one piece of the page while DeadlineTimer is showing.

  36 |               <div style={{ fontSize: 28, marginBottom: 8 }}>📭</div>
     | This draws one piece of the page while DeadlineTimer is showing.

  37 |               No deadlines found. Add a due date to a task to see it here.
     | Inside DeadlineTimer, this line runs as written: No deadlines found. Add a due date to a task to see it here.. It happens in order, after the line above it and before the line below it.

  38 |             </div>
     | This ends a drawing that DeadlineTimer started just above.

  39 |           ) : (
     | This closes a box of instructions that opened above.

  40 |             tasks.map((t) => {
     | Inside DeadlineTimer, this line runs as written: tasks.map((t) => {. It happens in order, after the line above it and before the line below it.

  41 |               const due = fmtDue(t.dueAt);
     | This gives a short name to a value so the rest of DeadlineTimer can use it.

  42 |               return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  43 |                 <div className="card" key={t._id}>
     | This draws one piece of the page while DeadlineTimer is showing.

  44 |                   <div className="flex items-center justify-between">
     | This draws one piece of the page while DeadlineTimer is showing.

  45 |                     <div>
     | This draws one piece of the page while DeadlineTimer is showing.

  46 |                       <div className="font-semibold mb-1">{t.title}</div>
     | This draws one piece of the page while DeadlineTimer is showing.

  47 |                       <div className="text-sm" style={{ color: due.color }}>{due.label}</div>
     | This draws one piece of the page while DeadlineTimer is showing.

  48 |                     </div>
     | This ends a drawing that DeadlineTimer started just above.

  49 |                     <button
     | This draws one piece of the page while DeadlineTimer is showing.

  50 |                       className="btn btn-ghost btn-sm"
     | Inside DeadlineTimer, this line runs as written: className="btn btn-ghost btn-sm". It happens in order, after the line above it and before the line below it.

  51 |                       onClick={() => navigate("/calendar")}
     | This decides what happens when you press.

  52 |                     >
     | Inside DeadlineTimer, this line runs as written: >. It happens in order, after the line above it and before the line below it.

  53 |                       📅 Reschedule
     | Inside DeadlineTimer, this line runs as written: 📅 Reschedule. It happens in order, after the line above it and before the line below it.

  54 |                     </button>
     | This ends a drawing that DeadlineTimer started just above.

  55 |                   </div>
     | This ends a drawing that DeadlineTimer started just above.

  56 |                 </div>
     | This ends a drawing that DeadlineTimer started just above.

  57 |               );
     | This closes a box of instructions that opened above.

  58 |             })
     | This ends tasks.map((t) => { (opened on line 40).

  59 |           )}
     | This ends DeadlineTimer (opened on line 6).

  60 |         </div>
     | This ends a drawing that DeadlineTimer started just above.

  61 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  62 |         <aside className="card" style={{ alignSelf: "flex-start" }}>
     | This draws one piece of the page while DeadlineTimer is showing.

  63 |           <div className="card-title">Tip</div>
     | This draws one piece of the page while DeadlineTimer is showing.

  64 |           <div className="text-sm text-muted" style={{ lineHeight: 1.7 }}>
     | This draws one piece of the page while DeadlineTimer is showing.

  65 |             Add due dates to tasks to see them here and on the Calendar.
     | Inside DeadlineTimer, this line runs as written: Add due dates to tasks to see them here and on the Calendar.. It happens in order, after the line above it and before the line below it.

  66 |             <br /><br />
     | This draws one piece of the page while DeadlineTimer is showing.

  67 |             Tasks due within 24 hours show in amber. Overdue tasks show in red.
     | Inside DeadlineTimer, this line runs as written: Tasks due within 24 hours show in amber. Overdue tasks show in red.. It happens in order, after the line above it and before the line below it.

  68 |           </div>
     | This ends a drawing that DeadlineTimer started just above.

  69 |         </aside>
     | This ends a drawing that DeadlineTimer started just above.

  70 |       </div>
     | This ends a drawing that DeadlineTimer started just above.

  71 |     </div>
     | This ends a drawing that DeadlineTimer started just above.

  72 |   );
     | This closes a box of instructions that opened above.

  73 | }
     | This ends DeadlineTimer (opened on line 6).

