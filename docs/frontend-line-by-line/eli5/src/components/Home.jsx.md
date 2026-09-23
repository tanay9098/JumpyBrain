# `src/components/Home.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import React, { useEffect, useState } from "react";
     | Borrows React so this file can remember things and draw the screen.

   2 | import { Link } from "react-router-dom";
     | Borrows React so this file can remember things and draw the screen.

   3 | import api from "../services/api";
     | This file borrows a tool another file already made.

   4 | import { useUser } from "../contexts/UserContext";
     | This file borrows a tool another file already made.

   5 | import { useEnergy } from "../contexts/EnergyContext";
     | This file borrows a tool another file already made.

   6 | import EnergyControl from "./EnergyControl";
     | This file borrows a tool another file already made.

   7 | import ShieldStatusCard from "./focus-shield/ShieldStatusCard";
     | This file borrows a tool another file already made.

   8 | import { useBlockingStore } from "../stores/blockingStore";
     | This file borrows a tool another file already made.

   9 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  10 | const FEEDBACK_URL = "https://www.jumpybrain.com/#feedback";
     | Hard-coded link to https://www.jumpybrain.com/#feedback. The banner, sidebar, and top bar all open it in a new tab.

  11 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  12 | function FeedbackCTACard() {
     | This starts FeedbackCTACard. A card with one button that opens the feedback URL.

  13 |   return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  14 |     <div className="card feedback-cta-card">
     | This draws one piece of the page while FeedbackCTACard is showing.

  15 |       <div className="feedback-cta-title">Still improving JumpyBrain</div>
     | This draws one piece of the page while FeedbackCTACard is showing.

  16 |       <div className="text-sm" style={{ color: "var(--text-soft)", lineHeight: 1.6, marginBottom: 12 }}>
     | This draws one piece of the page while FeedbackCTACard is showing.

  17 |         Some features are still under development and may not work exactly as
     | Inside FeedbackCTACard, this line runs as written: Some features are still under development and may not work exactly as. It happens in order, after the line above it and before the line below it.

  18 |         expected. If you hit an issue or have an idea, we'd love to hear from you.
     | Inside FeedbackCTACard, this line runs as written: expected. If you hit an issue or have an idea, we'd love to hear from you.. It happens in order, after the line above it and before the line below it.

  19 |       </div>
     | This ends a drawing that FeedbackCTACard started just above.

  20 |       <a href={FEEDBACK_URL} target="_blank" rel="noopener noreferrer" style={{ textDecoration: "none" }}>
     | This draws one piece of the page while FeedbackCTACard is showing.

  21 |         <button className="btn btn-primary btn-sm">Share Feedback →</button>
     | This draws one piece of the page while FeedbackCTACard is showing.

  22 |       </a>
     | This ends a drawing that FeedbackCTACard started just above.

  23 |     </div>
     | This ends a drawing that FeedbackCTACard started just above.

  24 |   );
     | This closes a box of instructions that opened above.

  25 | }
     | This ends FeedbackCTACard (opened on line 12).

  26 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  27 | export default function Home() {
     | This starts Home. Today page. Greeting, energy, one recommended task, three stats, quick links, shield status, and a tip that depends on energy.

  28 |   const { user } = useUser();
     | The logged-in profile object. Null means ProtectedRoute renders Auth.

  29 |   const { energy } = useEnergy();
     | Integer 1–5 from EnergyContext, persisted as bb-energy. Home refetches 'what next' when it changes. TodoList rescores and refetches suggestions.

  30 |   const { rules: shieldRules, loading: shieldLoading, setRules: setShieldRules, setLoading: setShieldLoading } = useBlockingStore();
     | The blocking rules sitting in useBlockingStore. Home and FocusTimer load them. FocusShieldPage saves them.

  31 |   const [daily, setDaily] = useState({ tasksCompleted: 0, totalSessionMins: 0 });
     | Today's tasksCompleted and totalSessionMins from GET /stats/daily.

  32 |   const [whatNext, setWhatNext] = useState(null);
     | The single task from GET /tasks/what-next?energyLevel=. Null means the list is empty or the request failed.

  33 |   const [loadingNext, setLoadingNext] = useState(false);
     | This gives a short name to a value so the rest of Home can use it.

  34 |   const [streak, setStreak] = useState(0);
     | How many days back from today, up to 7, have a completed task. Today may be empty; the count stops at the first gap after today.

  35 |   const [hasTasks, setHasTasks] = useState(true);
     | This gives a short name to a value so the rest of Home can use it.

  36 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  37 |   const hour = new Date().getHours();
     | This gives a short name to a value so the rest of Home can use it.

  38 |   const greeting =
     | This gives a short name to a value so the rest of Home can use it.

  39 |     hour < 12 ? "Good morning" : hour < 17 ? "Good afternoon" : "Good evening";
     | Inside Home, this line runs as written: hour < 12 ? "Good morning" : hour < 17 ? "Good afternoon" : "Good evening";. It happens in order, after the line above it and before the line below it.

  40 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  41 |   useEffect(() => {
     | This is an extra job that happens after the picture is drawn.

  42 |     loadStats();
     | Inside Home, this line runs as written: loadStats();. It happens in order, after the line above it and before the line below it.

  43 |     loadWhatNext();
     | Inside Home, this line runs as written: loadWhatNext();. It happens in order, after the line above it and before the line below it.

  44 |   }, [energy]);
     | This ends effect in Home (opened on line 41).

  45 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  46 |   useEffect(() => {
     | This is an extra job that happens after the picture is drawn.

  47 |     setShieldLoading(true);
     | Inside Home, this line runs as written: setShieldLoading(true);. It happens in order, after the line above it and before the line below it.

  48 |     api.get("/blocking")
     | This asks the server (the office that keeps tasks and accounts) for something, or sends it something.

  49 |       .then((data) => setShieldRules(data.rules))
     | Inside Home, this line runs as written: .then((data) => setShieldRules(data.rules)). It happens in order, after the line above it and before the line below it.

  50 |       .catch(() => {})
     | This ends effect in Home (opened on line 46).

  51 |       .finally(() => setShieldLoading(false));
     | Inside Home, this line runs as written: .finally(() => setShieldLoading(false));. It happens in order, after the line above it and before the line below it.

  52 |   }, []);
     | This ends effect in Home (opened on line 46).

  53 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  54 |   async function loadStats() {
     | This starts loadStats. GET /stats/daily for the tiles and GET /stats/weekly to count the streak.

  55 |     try {
     | Inside loadStats, this line runs as written: try {. It happens in order, after the line above it and before the line below it.

  56 |       const { data: d } = await api.get("/stats/daily");
     | This gives a short name to a value so the rest of loadStats can use it.

  57 |       setDaily(d ?? { tasksCompleted: 0, totalSessionMins: 0 });
     | This ends try { (opened on line 55).

  58 |       const { data: w } = await api.get("/stats/weekly");
     | This gives a short name to a value so the rest of loadStats can use it.

  59 |       if (w?.tasks) {
     | This asks a yes-or-no question. The next bit runs only on yes.

  60 |         const byDay = {};
     | This gives a short name to a value so the rest of loadStats can use it.

  61 |         w.tasks.forEach((t) => {
     | Inside loadStats, this line runs as written: w.tasks.forEach((t) => {. It happens in order, after the line above it and before the line below it.

  62 |           const key = t.completedAt?.split("T")[0];
     | This gives a short name to a value so the rest of loadStats can use it.

  63 |           if (key) byDay[key] = true;
     | This asks a yes-or-no question. The next bit runs only on yes.

  64 |         });
     | This ends w.tasks.forEach((t) => { (opened on line 61).

  65 |         let s = 0;
     | This gives a short name to a value so the rest of loadStats can use it.

  66 |         for (let i = 0; i < 7; i++) {
     | Inside loadStats, this line runs as written: for (let i = 0; i < 7; i++) {. It happens in order, after the line above it and before the line below it.

  67 |           const d = new Date();
     | This gives a short name to a value so the rest of loadStats can use it.

  68 |           d.setDate(d.getDate() - i);
     | Inside loadStats, this line runs as written: d.setDate(d.getDate() - i);. It happens in order, after the line above it and before the line below it.

  69 |           const key = d.toISOString().split("T")[0];
     | This gives a short name to a value so the rest of loadStats can use it.

  70 |           if (byDay[key]) s++;
     | This asks a yes-or-no question. The next bit runs only on yes.

  71 |           else if (i > 0) break;
     | Inside loadStats, this line runs as written: else if (i > 0) break;. It happens in order, after the line above it and before the line below it.

  72 |         }
     | This ends for (let i = 0; i < 7; i++) { (opened on line 66).

  73 |         setStreak(s);
     | Inside loadStats, this line runs as written: setStreak(s);. It happens in order, after the line above it and before the line below it.

  74 |       }
     | This ends if (w?.tasks) { (opened on line 59).

  75 |     } catch {}
     | This ends try { (opened on line 55).

  76 |   }
     | This ends loadStats (opened on line 54).

  77 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  78 |   async function loadWhatNext() {
     | This starts loadWhatNext. GET /tasks/what-next?energyLevel= plus the current energy. Sets hasTasks from whether a task came back.

  79 |     setLoadingNext(true);
     | Inside loadWhatNext, this line runs as written: setLoadingNext(true);. It happens in order, after the line above it and before the line below it.

  80 |     try {
     | Inside loadWhatNext, this line runs as written: try {. It happens in order, after the line above it and before the line below it.

  81 |       const data = await api.get(`/tasks/what-next?energyLevel=${energy}`);
     | This gives a short name to a value so the rest of loadWhatNext can use it.

  82 |       setWhatNext(data.task || null);
     | Inside loadWhatNext, this line runs as written: setWhatNext(data.task || null);. It happens in order, after the line above it and before the line below it.

  83 |       setHasTasks(!!data.task);
     | Inside loadWhatNext, this line runs as written: setHasTasks(!!data.task);. It happens in order, after the line above it and before the line below it.

  84 |     } catch {
     | This ends try { (opened on line 80).

  85 |       setWhatNext(null);
     | Inside loadWhatNext, this line runs as written: setWhatNext(null);. It happens in order, after the line above it and before the line below it.

  86 |       setHasTasks(false);
     | Inside loadWhatNext, this line runs as written: setHasTasks(false);. It happens in order, after the line above it and before the line below it.

  87 |     } finally {
     | This ends } catch { (opened on line 84).

  88 |       setLoadingNext(false);
     | Inside loadWhatNext, this line runs as written: setLoadingNext(false);. It happens in order, after the line above it and before the line below it.

  89 |     }
     | This ends } finally { (opened on line 87).

  90 |   }
     | This ends loadWhatNext (opened on line 78).

  91 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  92 |   function whatNextReason(task) {
     | This starts whatNextReason. Builds the sentence under the recommended task from due time, estimate, and dread. Does not call the network.

  93 |     if (!task) return "";
     | This asks a yes-or-no question. The next bit runs only on yes.

  94 |     const parts = [];
     | This gives a short name to a value so the rest of whatNextReason can use it.

  95 |     if (task.dueAt) {
     | This asks a yes-or-no question. The next bit runs only on yes.

  96 |       const h = Math.round((new Date(task.dueAt) - new Date()) / 3600000);
     | This gives a short name to a value so the rest of whatNextReason can use it.

  97 |       if (h < 24) parts.push(`Due in ~${h}h`);
     | This asks a yes-or-no question. The next bit runs only on yes.

  98 |       else parts.push(`Due ${new Date(task.dueAt).toLocaleDateString()}`);
     | This ends if (task.dueAt) { (opened on line 95).

  99 |     }
     | This ends if (task.dueAt) { (opened on line 95).

 100 |     if (task.estimateMins) parts.push(`~${task.estimateMins} min`);
     | This asks a yes-or-no question. The next bit runs only on yes.

 101 |     if (task.dreadScore <= 2) parts.push("Low dread — easy to start");
     | This asks a yes-or-no question. The next bit runs only on yes.

 102 |     else if (task.dreadScore >= 4) parts.push("High dread — tackle it now");
     | Inside whatNextReason, this line runs as written: else if (task.dreadScore >= 4) parts.push("High dread — tackle it now");. It happens in order, after the line above it and before the line below it.

 103 |     return parts.join(" · ") || "Good match for your current energy";
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

 104 |   }
     | This ends whatNextReason (opened on line 92).

 105 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 106 |   return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

 107 |     <div>
     | This draws one piece of the page while Home is showing.

 108 |       {/* ── Greeting ──────────────────────────────────── */}
     | This ends Home (opened on line 27).

 109 |       <h1 className="page-title">
     | This draws one piece of the page while Home is showing.

 110 |         {greeting}{user?.name ? `, ${user.name.split(" ")[0]}` : ""}
     | This ends Home (opened on line 27).

 111 |       </h1>
     | This ends a drawing that Home started just above.

 112 |       <p className="page-subtitle">Your ADHD command centre</p>
     | This draws one piece of the page while Home is showing.

 113 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 114 |       {/* ── Energy Check-in (unified component) ───────── */}
     | This ends Home (opened on line 27).

 115 |       <div className="card mb-4">
     | This draws one piece of the page while Home is showing.

 116 |         <div className="card-title">How's your energy right now?</div>
     | This draws one piece of the page while Home is showing.

 117 |         <EnergyControl />
     | This draws one piece of the page while Home is showing.

 118 |       </div>
     | This ends a drawing that Home started just above.

 119 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 120 |       <div className="grid-main">
     | This draws one piece of the page while Home is showing.

 121 |         {/* ── Left column ───────────────────────────────── */}
     | This ends Home (opened on line 27).

 122 |         <div className="stack">
     | This draws one piece of the page while Home is showing.

 123 |           {/* What Next card */}
     | This ends Home (opened on line 27).

 124 |           <div className="what-next-card">
     | This draws one piece of the page while Home is showing.

 125 |             <div className="what-next-label">⚡ What next?</div>
     | This draws one piece of the page while Home is showing.

 126 |             {loadingNext ? (
     | Inside Home, this line runs as written: {loadingNext ? (. It happens in order, after the line above it and before the line below it.

 127 |               <div className="text-sm text-muted">Finding the best task for you...</div>
     | This draws one piece of the page while Home is showing.

 128 |             ) : whatNext ? (
     | This closes a box of instructions that opened above.

 129 |               <>
     | This draws one piece of the page while Home is showing.

 130 |                 <div className="what-next-task">{whatNext.title}</div>
     | This draws one piece of the page while Home is showing.

 131 |                 <div className="what-next-reason">{whatNextReason(whatNext)}</div>
     | This draws one piece of the page while Home is showing.

 132 |                 <div style={{ display: "flex", gap: 8, flexWrap: "wrap" }}>
     | This draws one piece of the page while Home is showing.

 133 |                   <Link to="/focus">
     | This draws one piece of the page while Home is showing.

 134 |                     <button className="btn btn-primary">▶ Start Focus</button>
     | This draws one piece of the page while Home is showing.

 135 |                   </Link>
     | This ends a drawing that Home started just above.

 136 |                   <Link to="/todo">
     | This draws one piece of the page while Home is showing.

 137 |                     <button className="btn btn-ghost btn-sm" style={{ alignSelf: "center" }}>
     | This draws one piece of the page while Home is showing.

 138 |                       View all tasks
     | Inside Home, this line runs as written: View all tasks. It happens in order, after the line above it and before the line below it.

 139 |                     </button>
     | This ends a drawing that Home started just above.

 140 |                   </Link>
     | This ends a drawing that Home started just above.

 141 |                 </div>
     | This ends a drawing that Home started just above.

 142 |               </>
     | This ends a drawing that Home started just above.

 143 |             ) : (
     | This closes a box of instructions that opened above.

 144 |               /* Empty state: CTA to Brain Dump */
     | A note for people. The app skips this line.

 145 |               <>
     | This draws one piece of the page while Home is showing.

 146 |                 <div className="what-next-task" style={{ fontSize: 15 }}>Your task list is empty</div>
     | This draws one piece of the page while Home is showing.

 147 |                 <div className="what-next-reason">
     | This draws one piece of the page while Home is showing.

 148 |                   No tasks, no stress — yet. Do a Brain Dump: type everything
     | Inside Home, this line runs as written: No tasks, no stress — yet. Do a Brain Dump: type everything. It happens in order, after the line above it and before the line below it.

 149 |                   rattling around in your head and AI will turn it into a clear list.
     | Inside Home, this line runs as written: rattling around in your head and AI will turn it into a clear list.. It happens in order, after the line above it and before the line below it.

 150 |                 </div>
     | This ends a drawing that Home started just above.

 151 |                 <div style={{ display: "flex", gap: 8, flexWrap: "wrap" }}>
     | This draws one piece of the page while Home is showing.

 152 |                   <Link to="/todo?tab=dump">
     | This draws one piece of the page while Home is showing.

 153 |                     <button className="btn btn-primary">🧠 Brain Dump</button>
     | This draws one piece of the page while Home is showing.

 154 |                   </Link>
     | This ends a drawing that Home started just above.

 155 |                   <Link to="/todo">
     | This draws one piece of the page while Home is showing.

 156 |                     <button className="btn btn-ghost btn-sm" style={{ alignSelf: "center" }}>
     | This draws one piece of the page while Home is showing.

 157 |                       Add a task
     | Inside Home, this line runs as written: Add a task. It happens in order, after the line above it and before the line below it.

 158 |                     </button>
     | This ends a drawing that Home started just above.

 159 |                   </Link>
     | This ends a drawing that Home started just above.

 160 |                 </div>
     | This ends a drawing that Home started just above.

 161 |               </>
     | This ends a drawing that Home started just above.

 162 |             )}
     | This ends Home (opened on line 27).

 163 |           </div>
     | This ends a drawing that Home started just above.

 164 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 165 |           <div className="feedback-cta-mobile">
     | This draws one piece of the page while Home is showing.

 166 |             <FeedbackCTACard />
     | This draws one piece of the page while Home is showing.

 167 |           </div>
     | This ends a drawing that Home started just above.

 168 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 169 |           {/* Today stats */}
     | This ends Home (opened on line 27).

 170 |           <div className="grid-3">
     | This draws one piece of the page while Home is showing.

 171 |             <div className="stat-tile">
     | This draws one piece of the page while Home is showing.

 172 |               <div className="stat-value stat-green">
     | This draws one piece of the page while Home is showing.

 173 |                 {daily.tasksCompleted > 0 ? daily.tasksCompleted : "—"}
     | This ends Home (opened on line 27).

 174 |               </div>
     | This ends a drawing that Home started just above.

 175 |               <div className="stat-label">Tasks done</div>
     | This draws one piece of the page while Home is showing.

 176 |             </div>
     | This ends a drawing that Home started just above.

 177 |             <div className="stat-tile">
     | This draws one piece of the page while Home is showing.

 178 |               <div className="stat-value stat-violet">
     | This draws one piece of the page while Home is showing.

 179 |                 {daily.totalSessionMins > 0 ? daily.totalSessionMins : "—"}
     | This ends Home (opened on line 27).

 180 |               </div>
     | This ends a drawing that Home started just above.

 181 |               <div className="stat-label">Focus mins</div>
     | This draws one piece of the page while Home is showing.

 182 |             </div>
     | This ends a drawing that Home started just above.

 183 |             <div className="stat-tile">
     | This draws one piece of the page while Home is showing.

 184 |               <div className="stat-value stat-amber">
     | This draws one piece of the page while Home is showing.

 185 |                 {streak > 0 ? `${streak}🔥` : "—"}
     | This ends Home (opened on line 27).

 186 |               </div>
     | This ends a drawing that Home started just above.

 187 |               <div className="stat-label">Day streak</div>
     | This draws one piece of the page while Home is showing.

 188 |             </div>
     | This ends a drawing that Home started just above.

 189 |           </div>
     | This ends a drawing that Home started just above.

 190 |         </div>
     | This ends a drawing that Home started just above.

 191 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 192 |         {/* ── Right column ──────────────────────────────── */}
     | This ends Home (opened on line 27).

 193 |         <div className="stack">
     | This draws one piece of the page while Home is showing.

 194 |           <div className="card">
     | This draws one piece of the page while Home is showing.

 195 |             <div className="card-title">Quick actions</div>
     | This draws one piece of the page while Home is showing.

 196 |             <div className="stack-sm">
     | This draws one piece of the page while Home is showing.

 197 |               <Link to="/focus" style={{ textDecoration: "none" }}>
     | This draws one piece of the page while Home is showing.

 198 |                 <button className="btn btn-primary w-full">
     | This draws one piece of the page while Home is showing.

 199 |                   🎯 Start Focus Session
     | Inside Home, this line runs as written: 🎯 Start Focus Session. It happens in order, after the line above it and before the line below it.

 200 |                 </button>
     | This ends a drawing that Home started just above.

 201 |               </Link>
     | This ends a drawing that Home started just above.

 202 |               <Link to="/todo?tab=dump" style={{ textDecoration: "none" }}>
     | This draws one piece of the page while Home is showing.

 203 |                 <button className="btn btn-secondary w-full">
     | This draws one piece of the page while Home is showing.

 204 |                   🧠 Brain Dump → Tasks
     | Inside Home, this line runs as written: 🧠 Brain Dump → Tasks. It happens in order, after the line above it and before the line below it.

 205 |                 </button>
     | This ends a drawing that Home started just above.

 206 |               </Link>
     | This ends a drawing that Home started just above.

 207 |               <Link to="/blocking" style={{ textDecoration: "none" }}>
     | This draws one piece of the page while Home is showing.

 208 |                 <button className="btn btn-ghost w-full">
     | This draws one piece of the page while Home is showing.

 209 |                   🛡️ Manage Focus Shield
     | Inside Home, this line runs as written: 🛡️ Manage Focus Shield. It happens in order, after the line above it and before the line below it.

 210 |                 </button>
     | This ends a drawing that Home started just above.

 211 |               </Link>
     | This ends a drawing that Home started just above.

 212 |               <Link to="/dashboard" style={{ textDecoration: "none" }}>
     | This draws one piece of the page while Home is showing.

 213 |                 <button className="btn btn-ghost w-full">
     | This draws one piece of the page while Home is showing.

 214 |                   📊 View Progress
     | Inside Home, this line runs as written: 📊 View Progress. It happens in order, after the line above it and before the line below it.

 215 |                 </button>
     | This ends a drawing that Home started just above.

 216 |               </Link>
     | This ends a drawing that Home started just above.

 217 |             </div>
     | This ends a drawing that Home started just above.

 218 |           </div>
     | This ends a drawing that Home started just above.

 219 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 220 |           <ShieldStatusCard rules={shieldRules} loading={shieldLoading} variant="dashboard" />
     | This draws one piece of the page while Home is showing.

 221 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 222 |           <div className="card">
     | This draws one piece of the page while Home is showing.

 223 |             <div className="card-title">Daily tip</div>
     | This draws one piece of the page while Home is showing.

 224 |             <div className="text-sm" style={{ lineHeight: 1.7, color: "var(--text-soft)" }}>
     | This draws one piece of the page while Home is showing.

 225 |               {energy <= 2
     | Inside Home, this line runs as written: {energy <= 2. It happens in order, after the line above it and before the line below it.

 226 |                 ? "Low energy day — pick the easiest task first. Even 10 minutes counts."
     | Inside Home, this line runs as written: ? "Low energy day — pick the easiest task first. Even 10 minutes counts.". It happens in order, after the line above it and before the line below it.

 227 |                 : energy === 3
     | Inside Home, this line runs as written: : energy === 3. It happens in order, after the line above it and before the line below it.

 228 |                 ? "Pick 2 tasks. Start small. Consistency beats intensity."
     | Inside Home, this line runs as written: ? "Pick 2 tasks. Start small. Consistency beats intensity.". It happens in order, after the line above it and before the line below it.

 229 |                 : "Peak energy — tackle your most dreaded task now while you have momentum."}
     | This ends Home (opened on line 27).

 230 |             </div>
     | This ends a drawing that Home started just above.

 231 |           </div>
     | This ends a drawing that Home started just above.

 232 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 233 |           <div className="feedback-cta-desktop">
     | This draws one piece of the page while Home is showing.

 234 |             <FeedbackCTACard />
     | This draws one piece of the page while Home is showing.

 235 |           </div>
     | This ends a drawing that Home started just above.

 236 |         </div>
     | This ends a drawing that Home started just above.

 237 |       </div>
     | This ends a drawing that Home started just above.

 238 |     </div>
     | This ends a drawing that Home started just above.

 239 |   );
     | This closes a box of instructions that opened above.

 240 | }
     | This ends Home (opened on line 27).

