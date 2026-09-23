# `src/components/FocusTimer.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import React, { useEffect, useRef, useState } from "react";
     | Borrows React so this file can remember things and draw the screen.

   2 | import api from "../services/api";
     | This file borrows a tool another file already made.

   3 | import { setFocusActive, getDistractionCount, resetDistractionCount } from "./FocusOverlay";
     | This file borrows a tool another file already made.

   4 | import Affirmations from "./Affirmations";
     | This file borrows a tool another file already made.

   5 | import ShieldStatusCard from "./focus-shield/ShieldStatusCard";
     | This file borrows a tool another file already made.

   6 | import { useBlockingStore } from "../stores/blockingStore";
     | This file borrows a tool another file already made.

   7 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   8 | const CIRCUMFERENCE = 2 * Math.PI * 90;
     | Circumference of the timer ring (radius 90). strokeDashoffset uses it so the ring empties as seconds fall.

   9 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  10 | const MODES = [
     | In FocusTimer, Pomodoro is 25/5 and Deep Work is 50/10. In Mindfulness the live MODES (the third copy, after line 252) are three mp3s. The earlier MODES are inside comments and never run.

  11 |   { id: "pomodoro", label: "Pomodoro", work: 25, brk: 5 },
     | This ends the nearest open block.

  12 |   { id: "deep",     label: "Deep Work", work: 50, brk: 10 },
     | This ends the nearest open block.

  13 | ];
     | Inside the top of the file, this line runs as written: ];. It happens in order, after the line above it and before the line below it.

  14 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  15 | export default function FocusTimer() {
     | This starts FocusTimer. Countdown ring. On a finished work phase it POSTs /sessions and tells FocusOverlay the session ended.

  16 |   const { rules: shieldRules, loading: shieldLoading, setRules: setShieldRules, setLoading: setShieldLoading } = useBlockingStore();
     | The blocking rules sitting in useBlockingStore. Home and FocusTimer load them. FocusShieldPage saves them.

  17 |   const [modeIdx, setModeIdx] = useState(0);
     | This gives a short name to a value so the rest of FocusTimer can use it.

  18 |   const [workMins, setWorkMins] = useState(25);
     | This gives a short name to a value so the rest of FocusTimer can use it.

  19 |   const [breakMins, setBreakMins] = useState(5);
     | This gives a short name to a value so the rest of FocusTimer can use it.

  20 |   const [isWork, setIsWork] = useState(true);
     | This gives a short name to a value so the rest of FocusTimer can use it.

  21 |   const [seconds, setSeconds] = useState(25 * 60);
     | This gives a short name to a value so the rest of FocusTimer can use it.

  22 |   const [active, setActive] = useState(false);
     | This gives a short name to a value so the rest of FocusTimer can use it.

  23 |   const [sessionCount, setSessionCount] = useState(0);
     | This gives a short name to a value so the rest of FocusTimer can use it.

  24 |   const [reward, setReward] = useState(null);
     | This gives a short name to a value so the rest of FocusTimer can use it.

  25 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  26 |   // Task linking
     | A note written for people. The app does not run it.

  27 |   const [tasks, setTasks] = useState([]);
     | This gives a short name to a value so the rest of FocusTimer can use it.

  28 |   const [linkedTaskId, setLinkedTaskId] = useState("");
     | The task id chosen in the timer dropdown. Sent as taskId on POST /sessions. Empty string means a free session.

  29 |   const [tasksLoading, setTasksLoading] = useState(false);
     | This gives a short name to a value so the rest of FocusTimer can use it.

  30 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  31 |   const affirmRef = useRef();
     | This gives a short name to a value so the rest of FocusTimer can use it.

  32 |   const intervalRef = useRef();
     | This gives a short name to a value so the rest of FocusTimer can use it.

  33 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  34 |   const totalSecs = (isWork ? workMins : breakMins) * 60;
     | This gives a short name to a value so the rest of FocusTimer can use it.

  35 |   const progress = totalSecs > 0 ? 1 - seconds / totalSecs : 0;
     | Fraction of the phase already used: 1 - seconds/total. The ring stroke uses this.

  36 |   const dashOffset = CIRCUMFERENCE * (1 - progress);
     | How much of the ring to hide. 0 means the ring is full (no time elapsed). CIRCUMFERENCE means the ring is empty.

  37 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  38 |   const linkedTask = tasks.find((t) => t._id === linkedTaskId) || null;
     | This gives a short name to a value so the rest of FocusTimer can use it.

  39 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  40 |   useEffect(() => { loadTasks(); }, []);
     | This is an extra job that happens after the picture is drawn.

  41 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  42 |   useEffect(() => {
     | This is an extra job that happens after the picture is drawn.

  43 |     setShieldLoading(true);
     | Inside FocusTimer, this line runs as written: setShieldLoading(true);. It happens in order, after the line above it and before the line below it.

  44 |     api.get("/blocking")
     | This asks the server (the office that keeps tasks and accounts) for something, or sends it something.

  45 |       .then((data) => setShieldRules(data.rules))
     | Inside FocusTimer, this line runs as written: .then((data) => setShieldRules(data.rules)). It happens in order, after the line above it and before the line below it.

  46 |       .catch(() => {})
     | This ends effect in FocusTimer (opened on line 42).

  47 |       .finally(() => setShieldLoading(false));
     | Inside FocusTimer, this line runs as written: .finally(() => setShieldLoading(false));. It happens in order, after the line above it and before the line below it.

  48 |   }, []);
     | This ends effect in FocusTimer (opened on line 42).

  49 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  50 |   async function loadTasks() {
     | This starts loadTasks. GET /tasks and keeps incomplete ones for the dropdown.

  51 |     setTasksLoading(true);
     | Inside loadTasks, this line runs as written: setTasksLoading(true);. It happens in order, after the line above it and before the line below it.

  52 |     try {
     | Inside loadTasks, this line runs as written: try {. It happens in order, after the line above it and before the line below it.

  53 |       const res = await api.get("/tasks");
     | This gives a short name to a value so the rest of loadTasks can use it.

  54 |       setTasks((res.tasks || []).filter((t) => !t.completed));
     | Inside loadTasks, this line runs as written: setTasks((res.tasks || []).filter((t) => !t.completed));. It happens in order, after the line above it and before the line below it.

  55 |     } catch { setTasks([]); }
     | This ends try { (opened on line 52).

  56 |     finally { setTasksLoading(false); }
     | This ends loadTasks (opened on line 50).

  57 |   }
     | This ends loadTasks (opened on line 50).

  58 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  59 |   useEffect(() => {
     | This is an extra job that happens after the picture is drawn.

  60 |     const m = MODES[modeIdx];
     | This gives a short name to a value so the rest of FocusTimer can use it.

  61 |     if (m.id !== "custom") {
     | This asks a yes-or-no question. The next bit runs only on yes.

  62 |       setWorkMins(m.work);
     | Inside FocusTimer, this line runs as written: setWorkMins(m.work);. It happens in order, after the line above it and before the line below it.

  63 |       setBreakMins(m.brk);
     | Inside FocusTimer, this line runs as written: setBreakMins(m.brk);. It happens in order, after the line above it and before the line below it.

  64 |       reset(m.work, m.brk);
     | Inside FocusTimer, this line runs as written: reset(m.work, m.brk);. It happens in order, after the line above it and before the line below it.

  65 |     }
     | This ends if (m.id !== "custom") { (opened on line 61).

  66 |   }, [modeIdx]);
     | This ends effect in FocusTimer (opened on line 59).

  67 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  68 |   useEffect(() => {
     | This is an extra job that happens after the picture is drawn.

  69 |     if (active && seconds > 0) {
     | This asks a yes-or-no question. The next bit runs only on yes.

  70 |       intervalRef.current = setInterval(() => setSeconds((s) => s - 1), 1000);
     | Inside FocusTimer, this line runs as written: intervalRef.current = setInterval(() => setSeconds((s) => s - 1), 1000);. It happens in order, after the line above it and before the line below it.

  71 |     } else if (seconds === 0 && active) {
     | This ends if (active && seconds > 0) { (opened on line 69).

  72 |       clearInterval(intervalRef.current);
     | Inside FocusTimer, this line runs as written: clearInterval(intervalRef.current);. It happens in order, after the line above it and before the line below it.

  73 |       setActive(false);
     | Inside FocusTimer, this line runs as written: setActive(false);. It happens in order, after the line above it and before the line below it.

  74 |       setFocusActive(false);
     | Inside FocusTimer, this line runs as written: setFocusActive(false);. It happens in order, after the line above it and before the line below it.

  75 |       handleComplete();
     | Inside FocusTimer, this line runs as written: handleComplete();. It happens in order, after the line above it and before the line below it.

  76 |     }
     | This ends } else if (seconds === 0 && active) { (opened on line 71).

  77 |     return () => clearInterval(intervalRef.current);
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  78 |   }, [active, seconds]);
     | This ends effect in FocusTimer (opened on line 68).

  79 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  80 |   useEffect(() => {
     | This is an extra job that happens after the picture is drawn.

  81 |     if (active) {
     | This asks a yes-or-no question. The next bit runs only on yes.

  82 |       setFocusActive(true, isWork ? MODES[modeIdx].label : "Break");
     | Inside FocusTimer, this line runs as written: setFocusActive(true, isWork ? MODES[modeIdx].label : "Break");. It happens in order, after the line above it and before the line below it.

  83 |     } else {
     | This ends if (active) { (opened on line 81).

  84 |       setFocusActive(false);
     | Inside FocusTimer, this line runs as written: setFocusActive(false);. It happens in order, after the line above it and before the line below it.

  85 |     }
     | This ends } else { (opened on line 83).

  86 |     return () => { if (active) setFocusActive(false); };
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  87 |   }, [active, isWork, modeIdx]);
     | This ends effect in FocusTimer (opened on line 80).

  88 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  89 |   async function handleComplete() {
     | This starts handleComplete. Work phase: count the session, read distraction count from the overlay, reset it, POST /sessions with type, minutes, distractions, bb-energy, and optional taskId. Break phase only changes the affirmation.

  90 |     if (isWork) {
     | This asks a yes-or-no question. The next bit runs only on yes.

  91 |       setSessionCount((c) => c + 1);
     | Inside handleComplete, this line runs as written: setSessionCount((c) => c + 1);. It happens in order, after the line above it and before the line below it.

  92 |       showReward("🔥");
     | Inside handleComplete, this line runs as written: showReward("🔥");. It happens in order, after the line above it and before the line below it.

  93 |       if (affirmRef.current) affirmRef.current.messageForContext("task-complete");
     | This asks a yes-or-no question. The next bit runs only on yes.

  94 |       const distractionCount = getDistractionCount();
     | How many times the 800ms timer fired during this focus session. Posted with the session so the shield page can show 'distractions today'.

  95 |       resetDistractionCount();
     | Inside handleComplete, this line runs as written: resetDistractionCount();. It happens in order, after the line above it and before the line below it.

  96 |       const energyLevel = parseInt(localStorage.getItem("bb-energy") || "3", 10);
     | This gives a short name to a value so the rest of handleComplete can use it.

  97 |       try {
     | Inside handleComplete, this line runs as written: try {. It happens in order, after the line above it and before the line below it.

  98 |         await api.post("/sessions", {
     | This asks the server (the office that keeps tasks and accounts) for something, or sends it something.

  99 |           type: MODES[modeIdx].id,
     | Inside handleComplete, this line runs as written: type: MODES[modeIdx].id,. It happens in order, after the line above it and before the line below it.

 100 |           durationMins: workMins,
     | Inside handleComplete, this line runs as written: durationMins: workMins,. It happens in order, after the line above it and before the line below it.

 101 |           distractionCount,
     | Inside handleComplete, this line runs as written: distractionCount,. It happens in order, after the line above it and before the line below it.

 102 |           energyLevel,
     | Inside handleComplete, this line runs as written: energyLevel,. It happens in order, after the line above it and before the line below it.

 103 |           taskId: linkedTaskId || undefined,
     | Inside handleComplete, this line runs as written: taskId: linkedTaskId || undefined,. It happens in order, after the line above it and before the line below it.

 104 |         });
     | This ends await api.post("/sessions", { (opened on line 98).

 105 |       } catch {}
     | This ends try { (opened on line 97).

 106 |     } else {
     | This ends if (isWork) { (opened on line 90).

 107 |       if (affirmRef.current) affirmRef.current.messageForContext("day-start");
     | This asks a yes-or-no question. The next bit runs only on yes.

 108 |     }
     | This ends } else { (opened on line 106).

 109 |   }
     | This ends handleComplete (opened on line 89).

 110 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 111 |   function showReward(emoji) {
     | This starts showReward. Sets an emoji that a CSS burst shows, then clears it after 900ms.

 112 |     setReward(emoji);
     | Inside showReward, this line runs as written: setReward(emoji);. It happens in order, after the line above it and before the line below it.

 113 |     setTimeout(() => setReward(null), 900);
     | Inside showReward, this line runs as written: setTimeout(() => setReward(null), 900);. It happens in order, after the line above it and before the line below it.

 114 |   }
     | This ends showReward (opened on line 111).

 115 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 116 |   function toggle() {
     | This starts toggle. Flips active. Pausing also calls setFocusActive(false) so the overlay leaves the focused state.

 117 |     if (!active) {
     | This asks a yes-or-no question. The next bit runs only on yes.

 118 |       setActive(true);
     | Inside toggle, this line runs as written: setActive(true);. It happens in order, after the line above it and before the line below it.

 119 |     } else {
     | This ends if (!active) { (opened on line 117).

 120 |       setActive(false);
     | Inside toggle, this line runs as written: setActive(false);. It happens in order, after the line above it and before the line below it.

 121 |       setFocusActive(false);
     | Inside toggle, this line runs as written: setFocusActive(false);. It happens in order, after the line above it and before the line below it.

 122 |     }
     | This ends } else { (opened on line 119).

 123 |   }
     | This ends toggle (opened on line 116).

 124 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 125 |   function reset(w = workMins, b = breakMins) {
     | This starts reset. Stops the interval, leaves focus, forces the work phase, and restores workMins × 60.

 126 |     clearInterval(intervalRef.current);
     | Inside reset, this line runs as written: clearInterval(intervalRef.current);. It happens in order, after the line above it and before the line below it.

 127 |     setActive(false);
     | Inside reset, this line runs as written: setActive(false);. It happens in order, after the line above it and before the line below it.

 128 |     setFocusActive(false);
     | Inside reset, this line runs as written: setFocusActive(false);. It happens in order, after the line above it and before the line below it.

 129 |     setIsWork(true);
     | Inside reset, this line runs as written: setIsWork(true);. It happens in order, after the line above it and before the line below it.

 130 |     setSeconds(w * 60);
     | Inside reset, this line runs as written: setSeconds(w * 60);. It happens in order, after the line above it and before the line below it.

 131 |   }
     | This ends reset (opened on line 125).

 132 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 133 |   function switchPhase() {
     | This starts switchPhase. Flips work/break without counting a completed session.

 134 |     clearInterval(intervalRef.current);
     | Inside switchPhase, this line runs as written: clearInterval(intervalRef.current);. It happens in order, after the line above it and before the line below it.

 135 |     setActive(false);
     | Inside switchPhase, this line runs as written: setActive(false);. It happens in order, after the line above it and before the line below it.

 136 |     setFocusActive(false);
     | Inside switchPhase, this line runs as written: setFocusActive(false);. It happens in order, after the line above it and before the line below it.

 137 |     const next = !isWork;
     | This gives a short name to a value so the rest of switchPhase can use it.

 138 |     setIsWork(next);
     | Inside switchPhase, this line runs as written: setIsWork(next);. It happens in order, after the line above it and before the line below it.

 139 |     setSeconds((next ? workMins : breakMins) * 60);
     | Inside switchPhase, this line runs as written: setSeconds((next ? workMins : breakMins) * 60);. It happens in order, after the line above it and before the line below it.

 140 |   }
     | This ends switchPhase (opened on line 133).

 141 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 142 |   function fmt(s) {
     | This starts fmt. Turns a second count into m:ss.

 143 |     const m = Math.floor(s / 60);
     | This gives a short name to a value so the rest of fmt can use it.

 144 |     const ss = s % 60;
     | This gives a short name to a value so the rest of fmt can use it.

 145 |     return `${m}:${ss < 10 ? "0" + ss : ss}`;
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

 146 |   }
     | This ends fmt (opened on line 142).

 147 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 148 |   const sessionLabels = ["", "Starting out 🙂", "In the zone!", "Focus machine 🔥", "Incredible! 🤯"];
     | This gives a short name to a value so the rest of FocusTimer can use it.

 149 |   const sessionLabel = sessionCount === 0
     | This gives a short name to a value so the rest of FocusTimer can use it.

 150 |     ? "Start your first session"
     | Inside FocusTimer, this line runs as written: ? "Start your first session". It happens in order, after the line above it and before the line below it.

 151 |     : sessionLabels[Math.min(sessionCount, sessionLabels.length - 1)];
     | Inside FocusTimer, this line runs as written: : sessionLabels[Math.min(sessionCount, sessionLabels.length - 1)];. It happens in order, after the line above it and before the line below it.

 152 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 153 |   return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

 154 |     <div>
     | This draws one piece of the page while FocusTimer is showing.

 155 |       {reward && <div className="reward-burst">{reward}</div>}
     | This ends FocusTimer (opened on line 15).

 156 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 157 |       <h1 className="page-title">Focus Timer</h1>
     | This draws one piece of the page while FocusTimer is showing.

 158 |       <p className="page-subtitle">Pomodoro-style sessions with tab-switch protection</p>
     | This draws one piece of the page while FocusTimer is showing.

 159 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 160 |       <div className="grid-main">
     | This draws one piece of the page while FocusTimer is showing.

 161 |         {/* ── Timer card ────────────────────────────────── */}
     | This ends FocusTimer (opened on line 15).

 162 |         <div className="card">
     | This draws one piece of the page while FocusTimer is showing.

 163 |           <div className="mode-tabs">
     | This draws one piece of the page while FocusTimer is showing.

 164 |             {MODES.map((m, i) => (
     | Inside FocusTimer, this line runs as written: {MODES.map((m, i) => (. It happens in order, after the line above it and before the line below it.

 165 |               <button
     | This draws one piece of the page while FocusTimer is showing.

 166 |                 key={m.id}
     | This ends FocusTimer (opened on line 15).

 167 |                 className={`mode-tab ${modeIdx === i ? "active" : ""}`}
     | This ends FocusTimer (opened on line 15).

 168 |                 onClick={() => setModeIdx(i)}
     | This decides what happens when you press.

 169 |                 aria-pressed={modeIdx === i}
     | This ends FocusTimer (opened on line 15).

 170 |               >
     | Inside FocusTimer, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 171 |                 {m.label}
     | This ends FocusTimer (opened on line 15).

 172 |               </button>
     | This ends a drawing that FocusTimer started just above.

 173 |             ))}
     | This ends FocusTimer (opened on line 15).

 174 |           </div>
     | This ends a drawing that FocusTimer started just above.

 175 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 176 |           {/* Task picker — links session to a task */}
     | This ends FocusTimer (opened on line 15).

 177 |           <div className="task-link-picker mb-4">
     | This draws one piece of the page while FocusTimer is showing.

 178 |             <label className="text-xs text-muted" style={{ display: "block", marginBottom: 6 }}>
     | This draws one piece of the page while FocusTimer is showing.

 179 |               Working on
     | Inside FocusTimer, this line runs as written: Working on. It happens in order, after the line above it and before the line below it.

 180 |             </label>
     | This ends a drawing that FocusTimer started just above.

 181 |             {tasksLoading ? (
     | Inside FocusTimer, this line runs as written: {tasksLoading ? (. It happens in order, after the line above it and before the line below it.

 182 |               <div className="text-sm text-muted">Loading tasks...</div>
     | This draws one piece of the page while FocusTimer is showing.

 183 |             ) : tasks.length === 0 ? (
     | This closes a box of instructions that opened above.

 184 |               <div className="text-sm text-muted">
     | This draws one piece of the page while FocusTimer is showing.

 185 |                 No tasks yet —{" "}
     | This ends FocusTimer (opened on line 15).

 186 |                 <a href="/todo" className="text-link">add some tasks</a> to link your session.
     | This draws one piece of the page while FocusTimer is showing.

 187 |               </div>
     | This ends a drawing that FocusTimer started just above.

 188 |             ) : (
     | This closes a box of instructions that opened above.

 189 |               <select
     | This draws one piece of the page while FocusTimer is showing.

 190 |                 className="select"
     | Inside FocusTimer, this line runs as written: className="select". It happens in order, after the line above it and before the line below it.

 191 |                 value={linkedTaskId}
     | This ends FocusTimer (opened on line 15).

 192 |                 onChange={(e) => setLinkedTaskId(e.target.value)}
     | This ends FocusTimer (opened on line 15).

 193 |                 aria-label="Select task to focus on"
     | Inside FocusTimer, this line runs as written: aria-label="Select task to focus on". It happens in order, after the line above it and before the line below it.

 194 |               >
     | Inside FocusTimer, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 195 |                 <option value="">Free session (no specific task)</option>
     | This draws one piece of the page while FocusTimer is showing.

 196 |                 {tasks.map((t) => (
     | Inside FocusTimer, this line runs as written: {tasks.map((t) => (. It happens in order, after the line above it and before the line below it.

 197 |                   <option key={t._id} value={t._id}>{t.title}</option>
     | This draws one piece of the page while FocusTimer is showing.

 198 |                 ))}
     | This ends FocusTimer (opened on line 15).

 199 |               </select>
     | This ends a drawing that FocusTimer started just above.

 200 |             )}
     | This ends FocusTimer (opened on line 15).

 201 |             {linkedTask && (
     | Inside FocusTimer, this line runs as written: {linkedTask && (. It happens in order, after the line above it and before the line below it.

 202 |               <div className="linked-task-badge">
     | This draws one piece of the page while FocusTimer is showing.

 203 |                 <span>🎯</span>
     | This draws one piece of the page while FocusTimer is showing.

 204 |                 <span>{linkedTask.title}</span>
     | This draws one piece of the page while FocusTimer is showing.

 205 |                 {linkedTask.estimateMins && (
     | Inside FocusTimer, this line runs as written: {linkedTask.estimateMins && (. It happens in order, after the line above it and before the line below it.

 206 |                   <span className="text-xs text-muted">~{linkedTask.estimateMins}m</span>
     | This draws one piece of the page while FocusTimer is showing.

 207 |                 )}
     | This ends FocusTimer (opened on line 15).

 208 |               </div>
     | This ends a drawing that FocusTimer started just above.

 209 |             )}
     | This ends FocusTimer (opened on line 15).

 210 |           </div>
     | This ends a drawing that FocusTimer started just above.

 211 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 212 |           {/* Ring Timer */}
     | This ends FocusTimer (opened on line 15).

 213 |           <div className="ring-container">
     | This draws one piece of the page while FocusTimer is showing.

 214 |             <svg className="ring-svg" width="220" height="220" viewBox="0 0 220 220" aria-hidden="true">
     | This draws one piece of the page while FocusTimer is showing.

 215 |               <circle className="ring-track" cx="110" cy="110" r="90" />
     | This draws one piece of the page while FocusTimer is showing.

 216 |               <circle
     | This draws one piece of the page while FocusTimer is showing.

 217 |                 className={`ring-progress ${isWork ? "work" : "brk"}`}
     | This ends FocusTimer (opened on line 15).

 218 |                 cx="110" cy="110" r="90"
     | Inside FocusTimer, this line runs as written: cx="110" cy="110" r="90". It happens in order, after the line above it and before the line below it.

 219 |                 strokeDasharray={CIRCUMFERENCE}
     | This ends FocusTimer (opened on line 15).

 220 |                 strokeDashoffset={dashOffset}
     | This ends FocusTimer (opened on line 15).

 221 |               />
     | This closes a box of instructions that opened above.

 222 |             </svg>
     | This ends a drawing that FocusTimer started just above.

 223 |             <div className="ring-text" role="timer" aria-label={`${fmt(seconds)} ${isWork ? "work" : "break"}`}>
     | This draws one piece of the page while FocusTimer is showing.

 224 |               <div className="ring-time">{fmt(seconds)}</div>
     | This draws one piece of the page while FocusTimer is showing.

 225 |               <div className="ring-label">{isWork ? "Work" : "Break"}</div>
     | This draws one piece of the page while FocusTimer is showing.

 226 |             </div>
     | This ends a drawing that FocusTimer started just above.

 227 |           </div>
     | This ends a drawing that FocusTimer started just above.

 228 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 229 |           <div style={{ display: "flex", gap: 10, justifyContent: "center", flexWrap: "wrap" }}>
     | This draws one piece of the page while FocusTimer is showing.

 230 |             <button
     | This draws one piece of the page while FocusTimer is showing.

 231 |               className={`btn btn-lg ${active ? "btn-secondary" : "btn-primary"}`}
     | This ends FocusTimer (opened on line 15).

 232 |               onClick={toggle}
     | This decides what happens when you press.

 233 |               style={{ minWidth: 130 }}
     | This ends FocusTimer (opened on line 15).

 234 |               aria-label={active ? "Pause timer" : "Start timer"}
     | This ends FocusTimer (opened on line 15).

 235 |             >
     | Inside FocusTimer, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 236 |               {active ? "⏸ Pause" : "▶ Start"}
     | This ends FocusTimer (opened on line 15).

 237 |             </button>
     | This ends a drawing that FocusTimer started just above.

 238 |             <button className="btn btn-ghost" onClick={() => reset()} aria-label="Reset timer">↺ Reset</button>
     | This draws one piece of the page while FocusTimer is showing.

 239 |             <button className="btn btn-ghost" onClick={switchPhase} aria-label="Switch phase">
     | This draws one piece of the page while FocusTimer is showing.

 240 |               {isWork ? "→ Break" : "→ Work"}
     | This ends FocusTimer (opened on line 15).

 241 |             </button>
     | This ends a drawing that FocusTimer started just above.

 242 |           </div>
     | This ends a drawing that FocusTimer started just above.

 243 |         </div>
     | This ends a drawing that FocusTimer started just above.

 244 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 245 |         {/* ── Right panel ──────────────────────────────── */}
     | This ends FocusTimer (opened on line 15).

 246 |         <div className="stack">
     | This draws one piece of the page while FocusTimer is showing.

 247 |           <div className="card">
     | This draws one piece of the page while FocusTimer is showing.

 248 |             <div className="card-title">Today's Sessions</div>
     | This draws one piece of the page while FocusTimer is showing.

 249 |             <div className="stat-value stat-violet" style={{ fontSize: 42, marginBottom: 4 }}>
     | This draws one piece of the page while FocusTimer is showing.

 250 |               {sessionCount}
     | This ends FocusTimer (opened on line 15).

 251 |             </div>
     | This ends a drawing that FocusTimer started just above.

 252 |             <div className="text-sm text-muted">{sessionLabel}</div>
     | This draws one piece of the page while FocusTimer is showing.

 253 |             {sessionCount >= 2 && (
     | Inside FocusTimer, this line runs as written: {sessionCount >= 2 && (. It happens in order, after the line above it and before the line below it.

 254 |               <div className="streak-badge" style={{ marginTop: 10, alignSelf: "flex-start" }}>
     | This draws one piece of the page while FocusTimer is showing.

 255 |                 🔥 {sessionCount} sessions
     | This ends FocusTimer (opened on line 15).

 256 |               </div>
     | This ends a drawing that FocusTimer started just above.

 257 |             )}
     | This ends FocusTimer (opened on line 15).

 258 |           </div>
     | This ends a drawing that FocusTimer started just above.

 259 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 260 |           <div className="card">
     | This draws one piece of the page while FocusTimer is showing.

 261 |             <div className="card-title">Focus Guard</div>
     | This draws one piece of the page while FocusTimer is showing.

 262 |             <div
     | This draws one piece of the page while FocusTimer is showing.

 263 |               className="focus-status"
     | Inside FocusTimer, this line runs as written: className="focus-status". It happens in order, after the line above it and before the line below it.

 264 |               style={{
     | Inside FocusTimer, this line runs as written: style={{. It happens in order, after the line above it and before the line below it.

 265 |                 background: active ? "var(--green-dim)" : "var(--border)",
     | Inside FocusTimer, this line runs as written: background: active ? "var(--green-dim)" : "var(--border)",. It happens in order, after the line above it and before the line below it.

 266 |                 color: active ? "var(--green)" : "var(--muted)",
     | Inside FocusTimer, this line runs as written: color: active ? "var(--green)" : "var(--muted)",. It happens in order, after the line above it and before the line below it.

 267 |                 marginBottom: 10,
     | Inside FocusTimer, this line runs as written: marginBottom: 10,. It happens in order, after the line above it and before the line below it.

 268 |               }}
     | This ends style={{ (opened on line 264).

 269 |               role="status"
     | Inside FocusTimer, this line runs as written: role="status". It happens in order, after the line above it and before the line below it.

 270 |               aria-live="polite"
     | Inside FocusTimer, this line runs as written: aria-live="polite". It happens in order, after the line above it and before the line below it.

 271 |             >
     | Inside FocusTimer, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 272 |               <span className="focus-status-dot" />
     | This draws one piece of the page while FocusTimer is showing.

 273 |               {active ? "Active — guarding focus" : "Inactive"}
     | This ends FocusTimer (opened on line 15).

 274 |             </div>
     | This ends a drawing that FocusTimer started just above.

 275 |             <div className="text-sm text-muted" style={{ lineHeight: 1.7 }}>
     | This draws one piece of the page while FocusTimer is showing.

 276 |               When you switch tabs during a session, you'll get a gentle nudge.{" "}
     | This ends FocusTimer (opened on line 15).

 277 |               <span style={{ color: "var(--violet-light)" }}>800ms debounce</span> — quick reference
     | This draws one piece of the page while FocusTimer is showing.

 278 |               checks won't trigger it.
     | Inside FocusTimer, this line runs as written: checks won't trigger it.. It happens in order, after the line above it and before the line below it.

 279 |             </div>
     | This ends a drawing that FocusTimer started just above.

 280 |           </div>
     | This ends a drawing that FocusTimer started just above.

 281 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 282 |           <ShieldStatusCard
     | This draws one piece of the page while FocusTimer is showing.

 283 |             rules={shieldRules}
     | This ends FocusTimer (opened on line 15).

 284 |             loading={shieldLoading}
     | This ends FocusTimer (opened on line 15).

 285 |             sessionActive={active && isWork}
     | This ends FocusTimer (opened on line 15).

 286 |             variant="session"
     | Inside FocusTimer, this line runs as written: variant="session". It happens in order, after the line above it and before the line below it.

 287 |           />
     | This closes a box of instructions that opened above.

 288 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 289 |           <div className="card">
     | This draws one piece of the page while FocusTimer is showing.

 290 |             <div className="card-title">Affirmation</div>
     | This draws one piece of the page while FocusTimer is showing.

 291 |             <Affirmations ref={affirmRef} />
     | This draws one piece of the page while FocusTimer is showing.

 292 |           </div>
     | This ends a drawing that FocusTimer started just above.

 293 |         </div>
     | This ends a drawing that FocusTimer started just above.

 294 |       </div>
     | This ends a drawing that FocusTimer started just above.

 295 |     </div>
     | This ends a drawing that FocusTimer started just above.

 296 |   );
     | This closes a box of instructions that opened above.

 297 | }
     | This ends FocusTimer (opened on line 15).

