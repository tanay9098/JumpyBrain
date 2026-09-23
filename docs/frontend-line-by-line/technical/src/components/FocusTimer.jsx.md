# `src/components/FocusTimer.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import React, { useEffect, useRef, useState } from "react";
     | Import for the countdown ring and session saver: `import React, { useEffect, useRef, useState } from "react";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   2 | import api from "../services/api";
     | Import for the countdown ring and session saver: `import api from "../services/api";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   3 | import { setFocusActive, getDistractionCount, resetDistractionCount } from "./FocusOverlay";
     | Import for the countdown ring and session saver: `import { setFocusActive, getDistractionCount, resetDistractionCount } from "./FocusOverlay";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   4 | import Affirmations from "./Affirmations";
     | Import for the countdown ring and session saver: `import Affirmations from "./Affirmations";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   5 | import ShieldStatusCard from "./focus-shield/ShieldStatusCard";
     | Import for the countdown ring and session saver: `import ShieldStatusCard from "./focus-shield/ShieldStatusCard";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   6 | import { useBlockingStore } from "../stores/blockingStore";
     | Import for the countdown ring and session saver: `import { useBlockingStore } from "../stores/blockingStore";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   7 | 
     | Blank line in `src/components/FocusTimer.jsx` (the countdown ring and session saver), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   8 | const CIRCUMFERENCE = 2 * Math.PI * 90;
     | In `the top of the file` (src/components/FocusTimer.jsx): `CIRCUMFERENCE`: Circumference of the timer ring (radius 90). strokeDashoffset uses it so the ring empties as seconds fall. The code is `const CIRCUMFERENCE = 2 * Math.PI * 90;`.

   9 | 
     | Blank line in `src/components/FocusTimer.jsx` (the countdown ring and session saver), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  10 | const MODES = [
     | In `the top of the file` (src/components/FocusTimer.jsx): `MODES`: In FocusTimer, Pomodoro is 25/5 and Deep Work is 50/10. In Mindfulness the live MODES (the third copy, after line 252) are three mp3s. The earlier MODES are inside comments and never run. The code is `const MODES = [`.

  11 |   { id: "pomodoro", label: "Pomodoro", work: 25, brk: 5 },
     | In `the top of the file` (src/components/FocusTimer.jsx): `{ id: "pomodoro", label: "Pomodoro", work: 25, brk: 5 },` closes the nearest open block. Names declared inside that block end here.

  12 |   { id: "deep",     label: "Deep Work", work: 50, brk: 10 },
     | In `the top of the file` (src/components/FocusTimer.jsx): `{ id: "deep",     label: "Deep Work", work: 50, brk: 10 },` closes the nearest open block. Names declared inside that block end here.

  13 | ];
     | In `the top of the file` (src/components/FocusTimer.jsx): statement `];`. It runs when the top of the file runs, in order, before the next line of the same function.

  14 | 
     | Blank line in `src/components/FocusTimer.jsx` (the countdown ring and session saver), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  15 | export default function FocusTimer() {
     | Defines `FocusTimer` in the countdown ring and session saver. Countdown ring. On a finished work phase it POSTs /sessions and tells FocusOverlay the session ended.

  16 |   const { rules: shieldRules, loading: shieldLoading, setRules: setShieldRules, setLoading: setShieldLoading } = useBlockingStore();
     | In `FocusTimer` (src/components/FocusTimer.jsx): `shieldRules`: The blocking rules sitting in useBlockingStore. Home and FocusTimer load them. FocusShieldPage saves them. The code is `const { rules: shieldRules, loading: shieldLoading, setRules: setShieldRules, setLoading: setShieldLoading } = useBlockingStore();`.

  17 |   const [modeIdx, setModeIdx] = useState(0);
     | In `FocusTimer` (src/components/FocusTimer.jsx): React state `modeIdx, setModeIdx`. The value survives re-renders. Calling the setter re-renders this component. `const [modeIdx, setModeIdx] = useState(0);`

  18 |   const [workMins, setWorkMins] = useState(25);
     | In `FocusTimer` (src/components/FocusTimer.jsx): React state `workMins, setWorkMins`. The value survives re-renders. Calling the setter re-renders this component. `const [workMins, setWorkMins] = useState(25);`

  19 |   const [breakMins, setBreakMins] = useState(5);
     | In `FocusTimer` (src/components/FocusTimer.jsx): React state `breakMins, setBreakMins`. The value survives re-renders. Calling the setter re-renders this component. `const [breakMins, setBreakMins] = useState(5);`

  20 |   const [isWork, setIsWork] = useState(true);
     | In `FocusTimer` (src/components/FocusTimer.jsx): React state `isWork, setIsWork`. The value survives re-renders. Calling the setter re-renders this component. `const [isWork, setIsWork] = useState(true);`

  21 |   const [seconds, setSeconds] = useState(25 * 60);
     | In `FocusTimer` (src/components/FocusTimer.jsx): React state `seconds, setSeconds`. The value survives re-renders. Calling the setter re-renders this component. `const [seconds, setSeconds] = useState(25 * 60);`

  22 |   const [active, setActive] = useState(false);
     | In `FocusTimer` (src/components/FocusTimer.jsx): React state `active, setActive`. The value survives re-renders. Calling the setter re-renders this component. `const [active, setActive] = useState(false);`

  23 |   const [sessionCount, setSessionCount] = useState(0);
     | In `FocusTimer` (src/components/FocusTimer.jsx): React state `sessionCount, setSessionCount`. The value survives re-renders. Calling the setter re-renders this component. `const [sessionCount, setSessionCount] = useState(0);`

  24 |   const [reward, setReward] = useState(null);
     | In `FocusTimer` (src/components/FocusTimer.jsx): React state `reward, setReward`. The value survives re-renders. Calling the setter re-renders this component. `const [reward, setReward] = useState(null);`

  25 | 
     | Blank line in `src/components/FocusTimer.jsx` (the countdown ring and session saver), inside FocusTimer. The parser skips it. It separates the previous statement from the next so the function is readable.

  26 |   // Task linking
     | Comment inside FocusTimer. Not executed. It documents the next code: Task linking

  27 |   const [tasks, setTasks] = useState([]);
     | In `FocusTimer` (src/components/FocusTimer.jsx): React state `tasks, setTasks`. The value survives re-renders. Calling the setter re-renders this component. `const [tasks, setTasks] = useState([]);`

  28 |   const [linkedTaskId, setLinkedTaskId] = useState("");
     | In `FocusTimer` (src/components/FocusTimer.jsx): `linkedTaskId`: The task id chosen in the timer dropdown. Sent as taskId on POST /sessions. Empty string means a free session. The code is `const [linkedTaskId, setLinkedTaskId] = useState("");`.

  29 |   const [tasksLoading, setTasksLoading] = useState(false);
     | In `FocusTimer` (src/components/FocusTimer.jsx): React state `tasksLoading, setTasksLoading`. The value survives re-renders. Calling the setter re-renders this component. `const [tasksLoading, setTasksLoading] = useState(false);`

  30 | 
     | Blank line in `src/components/FocusTimer.jsx` (the countdown ring and session saver), inside FocusTimer. The parser skips it. It separates the previous statement from the next so the function is readable.

  31 |   const affirmRef = useRef();
     | In `FocusTimer` (src/components/FocusTimer.jsx): A ref `affirmRef`. `.current` survives re-renders and writing it does not re-render. `const affirmRef = useRef();`

  32 |   const intervalRef = useRef();
     | In `FocusTimer` (src/components/FocusTimer.jsx): A ref `intervalRef`. `.current` survives re-renders and writing it does not re-render. `const intervalRef = useRef();`

  33 | 
     | Blank line in `src/components/FocusTimer.jsx` (the countdown ring and session saver), inside FocusTimer. The parser skips it. It separates the previous statement from the next so the function is readable.

  34 |   const totalSecs = (isWork ? workMins : breakMins) * 60;
     | In `FocusTimer` (src/components/FocusTimer.jsx): `totalSecs` is assigned `(isWork ? workMins : breakMins) * 60;`. Later lines in this function read that name.

  35 |   const progress = totalSecs > 0 ? 1 - seconds / totalSecs : 0;
     | In `FocusTimer` (src/components/FocusTimer.jsx): `progress`: Fraction of the phase already used: 1 - seconds/total. The ring stroke uses this. The code is `const progress = totalSecs > 0 ? 1 - seconds / totalSecs : 0;`.

  36 |   const dashOffset = CIRCUMFERENCE * (1 - progress);
     | In `FocusTimer` (src/components/FocusTimer.jsx): `dashOffset`: How much of the ring to hide. 0 means the ring is full (no time elapsed). CIRCUMFERENCE means the ring is empty. The code is `const dashOffset = CIRCUMFERENCE * (1 - progress);`.

  37 | 
     | Blank line in `src/components/FocusTimer.jsx` (the countdown ring and session saver), inside FocusTimer. The parser skips it. It separates the previous statement from the next so the function is readable.

  38 |   const linkedTask = tasks.find((t) => t._id === linkedTaskId) || null;
     | In `FocusTimer` (src/components/FocusTimer.jsx): `linkedTask` is assigned `tasks.find((t) => t._id === linkedTaskId) || null;`. Later lines in this function read that name.

  39 | 
     | Blank line in `src/components/FocusTimer.jsx` (the countdown ring and session saver), inside FocusTimer. The parser skips it. It separates the previous statement from the next so the function is readable.

  40 |   useEffect(() => { loadTasks(); }, []);
     | In `FocusTimer` (src/components/FocusTimer.jsx): opens or continues an effect — `useEffect(() => { loadTasks(); }, []);`. The effect body runs after paint, and its cleanup runs before the next effect and on unmount.

  41 | 
     | Blank line in `src/components/FocusTimer.jsx` (the countdown ring and session saver), inside FocusTimer. The parser skips it. It separates the previous statement from the next so the function is readable.

  42 |   useEffect(() => {
     | In `FocusTimer` (src/components/FocusTimer.jsx): opens or continues an effect — `useEffect(() => {`. The effect body runs after paint, and its cleanup runs before the next effect and on unmount.

  43 |     setShieldLoading(true);
     | In `FocusTimer` (src/components/FocusTimer.jsx): statement `setShieldLoading(true);`. It runs when FocusTimer runs, in order, before the next line of the same function.

  44 |     api.get("/blocking")
     | In `FocusTimer` (src/components/FocusTimer.jsx): HTTP via the shared Axios instance — `api.get("/blocking")`. The request interceptor adds `Authorization: Bearer <accessToken>`. The response interceptor returns `res.data`, so the awaited value is the JSON body.

  45 |       .then((data) => setShieldRules(data.rules))
     | In `FocusTimer` (src/components/FocusTimer.jsx): statement `.then((data) => setShieldRules(data.rules))`. It runs when FocusTimer runs, in order, before the next line of the same function.

  46 |       .catch(() => {})
     | In `FocusTimer` (src/components/FocusTimer.jsx): statement `.catch(() => {})`. It runs when FocusTimer runs, in order, before the next line of the same function.

  47 |       .finally(() => setShieldLoading(false));
     | In `FocusTimer` (src/components/FocusTimer.jsx): statement `.finally(() => setShieldLoading(false));`. It runs when FocusTimer runs, in order, before the next line of the same function.

  48 |   }, []);
     | In `FocusTimer` (src/components/FocusTimer.jsx): `}, []);` closes effect in FocusTimer (opened on line 42). Names declared inside that block end here.

  49 | 
     | Blank line in `src/components/FocusTimer.jsx` (the countdown ring and session saver), inside FocusTimer. The parser skips it. It separates the previous statement from the next so the function is readable.

  50 |   async function loadTasks() {
     | Defines `loadTasks` in the countdown ring and session saver. GET /tasks and keeps incomplete ones for the dropdown.

  51 |     setTasksLoading(true);
     | In `loadTasks` (src/components/FocusTimer.jsx): statement `setTasksLoading(true);`. It runs when loadTasks runs, in order, before the next line of the same function.

  52 |     try {
     | In `loadTasks` (src/components/FocusTimer.jsx): error path `try {`.

  53 |       const res = await api.get("/tasks");
     | In `loadTasks` (src/components/FocusTimer.jsx): `res` is assigned `await api.get("/tasks");`. Later lines in this function read that name.

  54 |       setTasks((res.tasks || []).filter((t) => !t.completed));
     | In `loadTasks` (src/components/FocusTimer.jsx): iteration `setTasks((res.tasks || []).filter((t) => !t.completed));`.

  55 |     } catch { setTasks([]); }
     | In `loadTasks` (src/components/FocusTimer.jsx): `} catch { setTasks([]); }` closes try { (opened on line 52). Names declared inside that block end here.

  56 |     finally { setTasksLoading(false); }
     | In `loadTasks` (src/components/FocusTimer.jsx): `finally { setTasksLoading(false); }` closes loadTasks (opened on line 50). Names declared inside that block end here.

  57 |   }
     | In `loadTasks` (src/components/FocusTimer.jsx): `}` closes loadTasks (opened on line 50). Names declared inside that block end here.

  58 | 
     | Blank line in `src/components/FocusTimer.jsx` (the countdown ring and session saver), inside FocusTimer. The parser skips it. It separates the previous statement from the next so the function is readable.

  59 |   useEffect(() => {
     | In `FocusTimer` (src/components/FocusTimer.jsx): opens or continues an effect — `useEffect(() => {`. The effect body runs after paint, and its cleanup runs before the next effect and on unmount.

  60 |     const m = MODES[modeIdx];
     | In `FocusTimer` (src/components/FocusTimer.jsx): `m` is assigned `MODES[modeIdx];`. Later lines in this function read that name.

  61 |     if (m.id !== "custom") {
     | In `FocusTimer` (src/components/FocusTimer.jsx): branch `if (m.id !== "custom") {`. Only one side runs.

  62 |       setWorkMins(m.work);
     | In `FocusTimer` (src/components/FocusTimer.jsx): statement `setWorkMins(m.work);`. It runs when FocusTimer runs, in order, before the next line of the same function.

  63 |       setBreakMins(m.brk);
     | In `FocusTimer` (src/components/FocusTimer.jsx): statement `setBreakMins(m.brk);`. It runs when FocusTimer runs, in order, before the next line of the same function.

  64 |       reset(m.work, m.brk);
     | In `FocusTimer` (src/components/FocusTimer.jsx): statement `reset(m.work, m.brk);`. It runs when FocusTimer runs, in order, before the next line of the same function.

  65 |     }
     | In `FocusTimer` (src/components/FocusTimer.jsx): `}` closes if (m.id !== "custom") { (opened on line 61). Names declared inside that block end here.

  66 |   }, [modeIdx]);
     | In `FocusTimer` (src/components/FocusTimer.jsx): `}, [modeIdx]);` closes effect in FocusTimer (opened on line 59). Names declared inside that block end here.

  67 | 
     | Blank line in `src/components/FocusTimer.jsx` (the countdown ring and session saver), inside FocusTimer. The parser skips it. It separates the previous statement from the next so the function is readable.

  68 |   useEffect(() => {
     | In `FocusTimer` (src/components/FocusTimer.jsx): opens or continues an effect — `useEffect(() => {`. The effect body runs after paint, and its cleanup runs before the next effect and on unmount.

  69 |     if (active && seconds > 0) {
     | In `FocusTimer` (src/components/FocusTimer.jsx): branch `if (active && seconds > 0) {`. Only one side runs.

  70 |       intervalRef.current = setInterval(() => setSeconds((s) => s - 1), 1000);
     | In `FocusTimer` (src/components/FocusTimer.jsx): timer — `intervalRef.current = setInterval(() => setSeconds((s) => s - 1), 1000);`. The callback runs later on the event loop, not now.

  71 |     } else if (seconds === 0 && active) {
     | In `FocusTimer` (src/components/FocusTimer.jsx): branch `} else if (seconds === 0 && active) {`. Only one side runs.

  72 |       clearInterval(intervalRef.current);
     | In `FocusTimer` (src/components/FocusTimer.jsx): timer — `clearInterval(intervalRef.current);`. The callback runs later on the event loop, not now.

  73 |       setActive(false);
     | In `FocusTimer` (src/components/FocusTimer.jsx): statement `setActive(false);`. It runs when FocusTimer runs, in order, before the next line of the same function.

  74 |       setFocusActive(false);
     | In `FocusTimer` (src/components/FocusTimer.jsx): Talks to FocusOverlay through the module-level bridge. true starts the focused state; false returns the overlay to idle.

  75 |       handleComplete();
     | In `FocusTimer` (src/components/FocusTimer.jsx): statement `handleComplete();`. It runs when FocusTimer runs, in order, before the next line of the same function.

  76 |     }
     | In `FocusTimer` (src/components/FocusTimer.jsx): `}` closes } else if (seconds === 0 && active) { (opened on line 71). Names declared inside that block end here.

  77 |     return () => clearInterval(intervalRef.current);
     | In `FocusTimer` (src/components/FocusTimer.jsx): return `return () => clearInterval(intervalRef.current);`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  78 |   }, [active, seconds]);
     | In `FocusTimer` (src/components/FocusTimer.jsx): `}, [active, seconds]);` closes effect in FocusTimer (opened on line 68). Names declared inside that block end here.

  79 | 
     | Blank line in `src/components/FocusTimer.jsx` (the countdown ring and session saver), inside FocusTimer. The parser skips it. It separates the previous statement from the next so the function is readable.

  80 |   useEffect(() => {
     | In `FocusTimer` (src/components/FocusTimer.jsx): opens or continues an effect — `useEffect(() => {`. The effect body runs after paint, and its cleanup runs before the next effect and on unmount.

  81 |     if (active) {
     | In `FocusTimer` (src/components/FocusTimer.jsx): branch `if (active) {`. Only one side runs.

  82 |       setFocusActive(true, isWork ? MODES[modeIdx].label : "Break");
     | In `FocusTimer` (src/components/FocusTimer.jsx): Talks to FocusOverlay through the module-level bridge. true starts the focused state; false returns the overlay to idle.

  83 |     } else {
     | In `FocusTimer` (src/components/FocusTimer.jsx): branch `} else {`. Only one side runs.

  84 |       setFocusActive(false);
     | In `FocusTimer` (src/components/FocusTimer.jsx): Talks to FocusOverlay through the module-level bridge. true starts the focused state; false returns the overlay to idle.

  85 |     }
     | In `FocusTimer` (src/components/FocusTimer.jsx): `}` closes } else { (opened on line 83). Names declared inside that block end here.

  86 |     return () => { if (active) setFocusActive(false); };
     | In `FocusTimer` (src/components/FocusTimer.jsx): return `return () => { if (active) setFocusActive(false); };`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  87 |   }, [active, isWork, modeIdx]);
     | In `FocusTimer` (src/components/FocusTimer.jsx): `}, [active, isWork, modeIdx]);` closes effect in FocusTimer (opened on line 80). Names declared inside that block end here.

  88 | 
     | Blank line in `src/components/FocusTimer.jsx` (the countdown ring and session saver), inside FocusTimer. The parser skips it. It separates the previous statement from the next so the function is readable.

  89 |   async function handleComplete() {
     | Defines `handleComplete` in the countdown ring and session saver. Work phase: count the session, read distraction count from the overlay, reset it, POST /sessions with type, minutes, distractions, bb-energy, and optional taskId. Break phase only changes the affirmation.

  90 |     if (isWork) {
     | In `handleComplete` (src/components/FocusTimer.jsx): branch `if (isWork) {`. Only one side runs.

  91 |       setSessionCount((c) => c + 1);
     | In `handleComplete` (src/components/FocusTimer.jsx): statement `setSessionCount((c) => c + 1);`. It runs when handleComplete runs, in order, before the next line of the same function.

  92 |       showReward("🔥");
     | In `handleComplete` (src/components/FocusTimer.jsx): statement `showReward("🔥");`. It runs when handleComplete runs, in order, before the next line of the same function.

  93 |       if (affirmRef.current) affirmRef.current.messageForContext("task-complete");
     | In `handleComplete` (src/components/FocusTimer.jsx): branch `if (affirmRef.current) affirmRef.current.messageForContext("task-complete");`. Only one side runs.

  94 |       const distractionCount = getDistractionCount();
     | In `handleComplete` (src/components/FocusTimer.jsx): `distractionCount`: How many times the 800ms timer fired during this focus session. Posted with the session so the shield page can show 'distractions today'. The code is `const distractionCount = getDistractionCount();`.

  95 |       resetDistractionCount();
     | In `handleComplete` (src/components/FocusTimer.jsx): statement `resetDistractionCount();`. It runs when handleComplete runs, in order, before the next line of the same function.

  96 |       const energyLevel = parseInt(localStorage.getItem("bb-energy") || "3", 10);
     | In `handleComplete` (src/components/FocusTimer.jsx): `energyLevel` is assigned `parseInt(localStorage.getItem("bb-energy") || "3", 10);`. Later lines in this function read that name.

  97 |       try {
     | In `handleComplete` (src/components/FocusTimer.jsx): error path `try {`.

  98 |         await api.post("/sessions", {
     | In `handleComplete` (src/components/FocusTimer.jsx): HTTP via the shared Axios instance — `await api.post("/sessions", {`. The request interceptor adds `Authorization: Bearer <accessToken>`. The response interceptor returns `res.data`, so the awaited value is the JSON body.

  99 |           type: MODES[modeIdx].id,
     | In `handleComplete` (src/components/FocusTimer.jsx): statement `type: MODES[modeIdx].id,`. It runs when handleComplete runs, in order, before the next line of the same function.

 100 |           durationMins: workMins,
     | In `handleComplete` (src/components/FocusTimer.jsx): statement `durationMins: workMins,`. It runs when handleComplete runs, in order, before the next line of the same function.

 101 |           distractionCount,
     | In `handleComplete` (src/components/FocusTimer.jsx): statement `distractionCount,`. It runs when handleComplete runs, in order, before the next line of the same function.

 102 |           energyLevel,
     | In `handleComplete` (src/components/FocusTimer.jsx): statement `energyLevel,`. It runs when handleComplete runs, in order, before the next line of the same function.

 103 |           taskId: linkedTaskId || undefined,
     | In `handleComplete` (src/components/FocusTimer.jsx): statement `taskId: linkedTaskId || undefined,`. It runs when handleComplete runs, in order, before the next line of the same function.

 104 |         });
     | In `handleComplete` (src/components/FocusTimer.jsx): `});` closes await api.post("/sessions", { (opened on line 98). Names declared inside that block end here.

 105 |       } catch {}
     | In `handleComplete` (src/components/FocusTimer.jsx): `} catch {}` closes try { (opened on line 97). Names declared inside that block end here.

 106 |     } else {
     | In `handleComplete` (src/components/FocusTimer.jsx): branch `} else {`. Only one side runs.

 107 |       if (affirmRef.current) affirmRef.current.messageForContext("day-start");
     | In `handleComplete` (src/components/FocusTimer.jsx): branch `if (affirmRef.current) affirmRef.current.messageForContext("day-start");`. Only one side runs.

 108 |     }
     | In `handleComplete` (src/components/FocusTimer.jsx): `}` closes } else { (opened on line 106). Names declared inside that block end here.

 109 |   }
     | In `handleComplete` (src/components/FocusTimer.jsx): `}` closes handleComplete (opened on line 89). Names declared inside that block end here.

 110 | 
     | Blank line in `src/components/FocusTimer.jsx` (the countdown ring and session saver), inside FocusTimer. The parser skips it. It separates the previous statement from the next so the function is readable.

 111 |   function showReward(emoji) {
     | Defines `showReward` in the countdown ring and session saver. Sets an emoji that a CSS burst shows, then clears it after 900ms.

 112 |     setReward(emoji);
     | In `showReward` (src/components/FocusTimer.jsx): statement `setReward(emoji);`. It runs when showReward runs, in order, before the next line of the same function.

 113 |     setTimeout(() => setReward(null), 900);
     | In `showReward` (src/components/FocusTimer.jsx): timer — `setTimeout(() => setReward(null), 900);`. The callback runs later on the event loop, not now.

 114 |   }
     | In `showReward` (src/components/FocusTimer.jsx): `}` closes showReward (opened on line 111). Names declared inside that block end here.

 115 | 
     | Blank line in `src/components/FocusTimer.jsx` (the countdown ring and session saver), inside FocusTimer. The parser skips it. It separates the previous statement from the next so the function is readable.

 116 |   function toggle() {
     | Defines `toggle` in the countdown ring and session saver. Flips active. Pausing also calls setFocusActive(false) so the overlay leaves the focused state.

 117 |     if (!active) {
     | In `toggle` (src/components/FocusTimer.jsx): branch `if (!active) {`. Only one side runs.

 118 |       setActive(true);
     | In `toggle` (src/components/FocusTimer.jsx): statement `setActive(true);`. It runs when toggle runs, in order, before the next line of the same function.

 119 |     } else {
     | In `toggle` (src/components/FocusTimer.jsx): branch `} else {`. Only one side runs.

 120 |       setActive(false);
     | In `toggle` (src/components/FocusTimer.jsx): statement `setActive(false);`. It runs when toggle runs, in order, before the next line of the same function.

 121 |       setFocusActive(false);
     | In `toggle` (src/components/FocusTimer.jsx): Talks to FocusOverlay through the module-level bridge. true starts the focused state; false returns the overlay to idle.

 122 |     }
     | In `toggle` (src/components/FocusTimer.jsx): `}` closes } else { (opened on line 119). Names declared inside that block end here.

 123 |   }
     | In `toggle` (src/components/FocusTimer.jsx): `}` closes toggle (opened on line 116). Names declared inside that block end here.

 124 | 
     | Blank line in `src/components/FocusTimer.jsx` (the countdown ring and session saver), inside FocusTimer. The parser skips it. It separates the previous statement from the next so the function is readable.

 125 |   function reset(w = workMins, b = breakMins) {
     | Defines `reset` in the countdown ring and session saver. Stops the interval, leaves focus, forces the work phase, and restores workMins × 60.

 126 |     clearInterval(intervalRef.current);
     | In `reset` (src/components/FocusTimer.jsx): timer — `clearInterval(intervalRef.current);`. The callback runs later on the event loop, not now.

 127 |     setActive(false);
     | In `reset` (src/components/FocusTimer.jsx): statement `setActive(false);`. It runs when reset runs, in order, before the next line of the same function.

 128 |     setFocusActive(false);
     | In `reset` (src/components/FocusTimer.jsx): Talks to FocusOverlay through the module-level bridge. true starts the focused state; false returns the overlay to idle.

 129 |     setIsWork(true);
     | In `reset` (src/components/FocusTimer.jsx): statement `setIsWork(true);`. It runs when reset runs, in order, before the next line of the same function.

 130 |     setSeconds(w * 60);
     | In `reset` (src/components/FocusTimer.jsx): statement `setSeconds(w * 60);`. It runs when reset runs, in order, before the next line of the same function.

 131 |   }
     | In `reset` (src/components/FocusTimer.jsx): `}` closes reset (opened on line 125). Names declared inside that block end here.

 132 | 
     | Blank line in `src/components/FocusTimer.jsx` (the countdown ring and session saver), inside FocusTimer. The parser skips it. It separates the previous statement from the next so the function is readable.

 133 |   function switchPhase() {
     | Defines `switchPhase` in the countdown ring and session saver. Flips work/break without counting a completed session.

 134 |     clearInterval(intervalRef.current);
     | In `switchPhase` (src/components/FocusTimer.jsx): timer — `clearInterval(intervalRef.current);`. The callback runs later on the event loop, not now.

 135 |     setActive(false);
     | In `switchPhase` (src/components/FocusTimer.jsx): statement `setActive(false);`. It runs when switchPhase runs, in order, before the next line of the same function.

 136 |     setFocusActive(false);
     | In `switchPhase` (src/components/FocusTimer.jsx): Talks to FocusOverlay through the module-level bridge. true starts the focused state; false returns the overlay to idle.

 137 |     const next = !isWork;
     | In `switchPhase` (src/components/FocusTimer.jsx): `next` is assigned `!isWork;`. Later lines in this function read that name.

 138 |     setIsWork(next);
     | In `switchPhase` (src/components/FocusTimer.jsx): statement `setIsWork(next);`. It runs when switchPhase runs, in order, before the next line of the same function.

 139 |     setSeconds((next ? workMins : breakMins) * 60);
     | In `switchPhase` (src/components/FocusTimer.jsx): statement `setSeconds((next ? workMins : breakMins) * 60);`. It runs when switchPhase runs, in order, before the next line of the same function.

 140 |   }
     | In `switchPhase` (src/components/FocusTimer.jsx): `}` closes switchPhase (opened on line 133). Names declared inside that block end here.

 141 | 
     | Blank line in `src/components/FocusTimer.jsx` (the countdown ring and session saver), inside FocusTimer. The parser skips it. It separates the previous statement from the next so the function is readable.

 142 |   function fmt(s) {
     | Defines `fmt` in the countdown ring and session saver. Turns a second count into m:ss.

 143 |     const m = Math.floor(s / 60);
     | In `fmt` (src/components/FocusTimer.jsx): `m` is assigned `Math.floor(s / 60);`. Later lines in this function read that name.

 144 |     const ss = s % 60;
     | In `fmt` (src/components/FocusTimer.jsx): `ss` is assigned `s % 60;`. Later lines in this function read that name.

 145 |     return `${m}:${ss < 10 ? "0" + ss : ss}`;
     | In `fmt` (src/components/FocusTimer.jsx): return `return `${m}:${ss < 10 ? "0" + ss : ss}`;`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

 146 |   }
     | In `fmt` (src/components/FocusTimer.jsx): `}` closes fmt (opened on line 142). Names declared inside that block end here.

 147 | 
     | Blank line in `src/components/FocusTimer.jsx` (the countdown ring and session saver), inside FocusTimer. The parser skips it. It separates the previous statement from the next so the function is readable.

 148 |   const sessionLabels = ["", "Starting out 🙂", "In the zone!", "Focus machine 🔥", "Incredible! 🤯"];
     | In `FocusTimer` (src/components/FocusTimer.jsx): `sessionLabels` is assigned `["", "Starting out 🙂", "In the zone!", "Focus machine 🔥", "Incredible! 🤯"];`. Later lines in this function read that name.

 149 |   const sessionLabel = sessionCount === 0
     | In `FocusTimer` (src/components/FocusTimer.jsx): `sessionLabel` is assigned `sessionCount === 0`. Later lines in this function read that name.

 150 |     ? "Start your first session"
     | In `FocusTimer` (src/components/FocusTimer.jsx): statement `? "Start your first session"`. It runs when FocusTimer runs, in order, before the next line of the same function.

 151 |     : sessionLabels[Math.min(sessionCount, sessionLabels.length - 1)];
     | In `FocusTimer` (src/components/FocusTimer.jsx): statement `: sessionLabels[Math.min(sessionCount, sessionLabels.length - 1)];`. It runs when FocusTimer runs, in order, before the next line of the same function.

 152 | 
     | Blank line in `src/components/FocusTimer.jsx` (the countdown ring and session saver), inside FocusTimer. The parser skips it. It separates the previous statement from the next so the function is readable.

 153 |   return (
     | In `FocusTimer` (src/components/FocusTimer.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

 154 |     <div>
     | In `FocusTimer` (src/components/FocusTimer.jsx): Opens it. A box that groups the elements inside it. Source: `<div>`

 155 |       {reward && <div className="reward-burst">{reward}</div>}
     | In `FocusTimer` (src/components/FocusTimer.jsx): `{reward && <div className="reward-burst">{reward}</div>}` closes FocusTimer (opened on line 15). Names declared inside that block end here.

 156 | 
     | Blank line in `src/components/FocusTimer.jsx` (the countdown ring and session saver), inside FocusTimer. The parser skips it. It separates the previous statement from the next so the function is readable.

 157 |       <h1 className="page-title">Focus Timer</h1>
     | In `FocusTimer` (src/components/FocusTimer.jsx): Opens it. The page title. Source: `<h1 className="page-title">Focus Timer</h1>`

 158 |       <p className="page-subtitle">Pomodoro-style sessions with tab-switch protection</p>
     | In `FocusTimer` (src/components/FocusTimer.jsx): Opens it. A paragraph. Source: `<p className="page-subtitle">Pomodoro-style sessions with tab-switch protection</p>`

 159 | 
     | Blank line in `src/components/FocusTimer.jsx` (the countdown ring and session saver), inside FocusTimer. The parser skips it. It separates the previous statement from the next so the function is readable.

 160 |       <div className="grid-main">
     | In `FocusTimer` (src/components/FocusTimer.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="grid-main">`

 161 |         {/* ── Timer card ────────────────────────────────── */}
     | In `FocusTimer` (src/components/FocusTimer.jsx): `{/* ── Timer card ────────────────────────────────── */}` closes FocusTimer (opened on line 15). Names declared inside that block end here.

 162 |         <div className="card">
     | In `FocusTimer` (src/components/FocusTimer.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="card">`

 163 |           <div className="mode-tabs">
     | In `FocusTimer` (src/components/FocusTimer.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="mode-tabs">`

 164 |             {MODES.map((m, i) => (
     | In `FocusTimer` (src/components/FocusTimer.jsx): iteration `{MODES.map((m, i) => (`.

 165 |               <button
     | In `FocusTimer` (src/components/FocusTimer.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button`

 166 |                 key={m.id}
     | In `FocusTimer` (src/components/FocusTimer.jsx): `key={m.id}` closes FocusTimer (opened on line 15). Names declared inside that block end here.

 167 |                 className={`mode-tab ${modeIdx === i ? "active" : ""}`}
     | In `FocusTimer` (src/components/FocusTimer.jsx): `className={`mode-tab ${modeIdx === i ? "active" : ""}`}` closes FocusTimer (opened on line 15). Names declared inside that block end here.

 168 |                 onClick={() => setModeIdx(i)}
     | In `FocusTimer` (src/components/FocusTimer.jsx): event prop `onClick={() => setModeIdx(i)}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 169 |                 aria-pressed={modeIdx === i}
     | In `FocusTimer` (src/components/FocusTimer.jsx): `aria-pressed={modeIdx === i}` closes FocusTimer (opened on line 15). Names declared inside that block end here.

 170 |               >
     | In `FocusTimer` (src/components/FocusTimer.jsx): statement `>`. It runs when FocusTimer runs, in order, before the next line of the same function.

 171 |                 {m.label}
     | In `FocusTimer` (src/components/FocusTimer.jsx): `{m.label}` closes FocusTimer (opened on line 15). Names declared inside that block end here.

 172 |               </button>
     | In `FocusTimer` (src/components/FocusTimer.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

 173 |             ))}
     | In `FocusTimer` (src/components/FocusTimer.jsx): `))}` closes FocusTimer (opened on line 15). Names declared inside that block end here.

 174 |           </div>
     | In `FocusTimer` (src/components/FocusTimer.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 175 | 
     | Blank line in `src/components/FocusTimer.jsx` (the countdown ring and session saver), inside FocusTimer. The parser skips it. It separates the previous statement from the next so the function is readable.

 176 |           {/* Task picker — links session to a task */}
     | In `FocusTimer` (src/components/FocusTimer.jsx): `{/* Task picker — links session to a task */}` closes FocusTimer (opened on line 15). Names declared inside that block end here.

 177 |           <div className="task-link-picker mb-4">
     | In `FocusTimer` (src/components/FocusTimer.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="task-link-picker mb-4">`

 178 |             <label className="text-xs text-muted" style={{ display: "block", marginBottom: 6 }}>
     | In `FocusTimer` (src/components/FocusTimer.jsx): Opens it. The caption for an input. Source: `<label className="text-xs text-muted" style={{ display: "block", marginBottom: 6 }}>`

 179 |               Working on
     | In `FocusTimer` (src/components/FocusTimer.jsx): statement `Working on`. It runs when FocusTimer runs, in order, before the next line of the same function.

 180 |             </label>
     | In `FocusTimer` (src/components/FocusTimer.jsx): Closes it. The caption for an input. Source: `</label>`

 181 |             {tasksLoading ? (
     | In `FocusTimer` (src/components/FocusTimer.jsx): statement `{tasksLoading ? (`. It runs when FocusTimer runs, in order, before the next line of the same function.

 182 |               <div className="text-sm text-muted">Loading tasks...</div>
     | In `FocusTimer` (src/components/FocusTimer.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="text-sm text-muted">Loading tasks...</div>`

 183 |             ) : tasks.length === 0 ? (
     | In `FocusTimer` (src/components/FocusTimer.jsx): statement `) : tasks.length === 0 ? (`. It runs when FocusTimer runs, in order, before the next line of the same function.

 184 |               <div className="text-sm text-muted">
     | In `FocusTimer` (src/components/FocusTimer.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="text-sm text-muted">`

 185 |                 No tasks yet —{" "}
     | In `FocusTimer` (src/components/FocusTimer.jsx): `No tasks yet —{" "}` closes FocusTimer (opened on line 15). Names declared inside that block end here.

 186 |                 <a href="/todo" className="text-link">add some tasks</a> to link your session.
     | In `FocusTimer` (src/components/FocusTimer.jsx): Opens it. A normal link. If it has target=_blank it leaves the app. Source: `<a href="/todo" className="text-link">add some tasks</a> to link your session.`

 187 |               </div>
     | In `FocusTimer` (src/components/FocusTimer.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 188 |             ) : (
     | In `FocusTimer` (src/components/FocusTimer.jsx): statement `) : (`. It runs when FocusTimer runs, in order, before the next line of the same function.

 189 |               <select
     | In `FocusTimer` (src/components/FocusTimer.jsx): Opens it. A dropdown. onChange writes the chosen value into state. Source: `<select`

 190 |                 className="select"
     | In `FocusTimer` (src/components/FocusTimer.jsx): statement `className="select"`. It runs when FocusTimer runs, in order, before the next line of the same function.

 191 |                 value={linkedTaskId}
     | In `FocusTimer` (src/components/FocusTimer.jsx): `value={linkedTaskId}` closes FocusTimer (opened on line 15). Names declared inside that block end here.

 192 |                 onChange={(e) => setLinkedTaskId(e.target.value)}
     | In `FocusTimer` (src/components/FocusTimer.jsx): event prop `onChange={(e) => setLinkedTaskId(e.target.value)}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 193 |                 aria-label="Select task to focus on"
     | In `FocusTimer` (src/components/FocusTimer.jsx): statement `aria-label="Select task to focus on"`. It runs when FocusTimer runs, in order, before the next line of the same function.

 194 |               >
     | In `FocusTimer` (src/components/FocusTimer.jsx): statement `>`. It runs when FocusTimer runs, in order, before the next line of the same function.

 195 |                 <option value="">Free session (no specific task)</option>
     | In `FocusTimer` (src/components/FocusTimer.jsx): JSX `<option>`. React will create this node when the parent renders.. value is controlled by React state, so the DOM shows that state Source: `<option value="">Free session (no specific task)</option>`

 196 |                 {tasks.map((t) => (
     | In `FocusTimer` (src/components/FocusTimer.jsx): iteration `{tasks.map((t) => (`.

 197 |                   <option key={t._id} value={t._id}>{t.title}</option>
     | In `FocusTimer` (src/components/FocusTimer.jsx): JSX `<option>`. React will create this node when the parent renders.. value is controlled by React state, so the DOM shows that state Source: `<option key={t._id} value={t._id}>{t.title}</option>`

 198 |                 ))}
     | In `FocusTimer` (src/components/FocusTimer.jsx): `))}` closes FocusTimer (opened on line 15). Names declared inside that block end here.

 199 |               </select>
     | In `FocusTimer` (src/components/FocusTimer.jsx): Closes it. A dropdown. onChange writes the chosen value into state. Source: `</select>`

 200 |             )}
     | In `FocusTimer` (src/components/FocusTimer.jsx): `)}` closes FocusTimer (opened on line 15). Names declared inside that block end here.

 201 |             {linkedTask && (
     | In `FocusTimer` (src/components/FocusTimer.jsx): statement `{linkedTask && (`. It runs when FocusTimer runs, in order, before the next line of the same function.

 202 |               <div className="linked-task-badge">
     | In `FocusTimer` (src/components/FocusTimer.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="linked-task-badge">`

 203 |                 <span>🎯</span>
     | In `FocusTimer` (src/components/FocusTimer.jsx): Opens it. An inline box. Source: `<span>🎯</span>`

 204 |                 <span>{linkedTask.title}</span>
     | In `FocusTimer` (src/components/FocusTimer.jsx): Opens it. An inline box. Source: `<span>{linkedTask.title}</span>`

 205 |                 {linkedTask.estimateMins && (
     | In `FocusTimer` (src/components/FocusTimer.jsx): statement `{linkedTask.estimateMins && (`. It runs when FocusTimer runs, in order, before the next line of the same function.

 206 |                   <span className="text-xs text-muted">~{linkedTask.estimateMins}m</span>
     | In `FocusTimer` (src/components/FocusTimer.jsx): Opens it. An inline box. Source: `<span className="text-xs text-muted">~{linkedTask.estimateMins}m</span>`

 207 |                 )}
     | In `FocusTimer` (src/components/FocusTimer.jsx): `)}` closes FocusTimer (opened on line 15). Names declared inside that block end here.

 208 |               </div>
     | In `FocusTimer` (src/components/FocusTimer.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 209 |             )}
     | In `FocusTimer` (src/components/FocusTimer.jsx): `)}` closes FocusTimer (opened on line 15). Names declared inside that block end here.

 210 |           </div>
     | In `FocusTimer` (src/components/FocusTimer.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 211 | 
     | Blank line in `src/components/FocusTimer.jsx` (the countdown ring and session saver), inside FocusTimer. The parser skips it. It separates the previous statement from the next so the function is readable.

 212 |           {/* Ring Timer */}
     | In `FocusTimer` (src/components/FocusTimer.jsx): `{/* Ring Timer */}` closes FocusTimer (opened on line 15). Names declared inside that block end here.

 213 |           <div className="ring-container">
     | In `FocusTimer` (src/components/FocusTimer.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="ring-container">`

 214 |             <svg className="ring-svg" width="220" height="220" viewBox="0 0 220 220" aria-hidden="true">
     | In `FocusTimer` (src/components/FocusTimer.jsx): Opens it. Vector drawing. It does not fetch data. Source: `<svg className="ring-svg" width="220" height="220" viewBox="0 0 220 220" aria-hidden="true">`

 215 |               <circle className="ring-track" cx="110" cy="110" r="90" />
     | In `FocusTimer` (src/components/FocusTimer.jsx): JSX `<circle>`. React will create this node when the parent renders.. className chooses the CSS rules from styles.css Source: `<circle className="ring-track" cx="110" cy="110" r="90" />`

 216 |               <circle
     | In `FocusTimer` (src/components/FocusTimer.jsx): JSX `<circle>`. React will create this node when the parent renders. Source: `<circle`

 217 |                 className={`ring-progress ${isWork ? "work" : "brk"}`}
     | In `FocusTimer` (src/components/FocusTimer.jsx): `className={`ring-progress ${isWork ? "work" : "brk"}`}` closes FocusTimer (opened on line 15). Names declared inside that block end here.

 218 |                 cx="110" cy="110" r="90"
     | In `FocusTimer` (src/components/FocusTimer.jsx): statement `cx="110" cy="110" r="90"`. It runs when FocusTimer runs, in order, before the next line of the same function.

 219 |                 strokeDasharray={CIRCUMFERENCE}
     | In `FocusTimer` (src/components/FocusTimer.jsx): `strokeDasharray={CIRCUMFERENCE}` closes FocusTimer (opened on line 15). Names declared inside that block end here.

 220 |                 strokeDashoffset={dashOffset}
     | In `FocusTimer` (src/components/FocusTimer.jsx): `strokeDashoffset={dashOffset}` closes FocusTimer (opened on line 15). Names declared inside that block end here.

 221 |               />
     | In `FocusTimer` (src/components/FocusTimer.jsx): statement `/>`. It runs when FocusTimer runs, in order, before the next line of the same function.

 222 |             </svg>
     | In `FocusTimer` (src/components/FocusTimer.jsx): Closes it. Vector drawing. It does not fetch data. Source: `</svg>`

 223 |             <div className="ring-text" role="timer" aria-label={`${fmt(seconds)} ${isWork ? "work" : "break"}`}>
     | In `FocusTimer` (src/components/FocusTimer.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="ring-text" role="timer" aria-label={`${fmt(seconds)} ${isWork ? "work" : "break"}`}>`

 224 |               <div className="ring-time">{fmt(seconds)}</div>
     | In `FocusTimer` (src/components/FocusTimer.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="ring-time">{fmt(seconds)}</div>`

 225 |               <div className="ring-label">{isWork ? "Work" : "Break"}</div>
     | In `FocusTimer` (src/components/FocusTimer.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="ring-label">{isWork ? "Work" : "Break"}</div>`

 226 |             </div>
     | In `FocusTimer` (src/components/FocusTimer.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 227 |           </div>
     | In `FocusTimer` (src/components/FocusTimer.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 228 | 
     | Blank line in `src/components/FocusTimer.jsx` (the countdown ring and session saver), inside FocusTimer. The parser skips it. It separates the previous statement from the next so the function is readable.

 229 |           <div style={{ display: "flex", gap: 10, justifyContent: "center", flexWrap: "wrap" }}>
     | In `FocusTimer` (src/components/FocusTimer.jsx): Opens it. A box that groups the elements inside it. Source: `<div style={{ display: "flex", gap: 10, justifyContent: "center", flexWrap: "wrap" }}>`

 230 |             <button
     | In `FocusTimer` (src/components/FocusTimer.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button`

 231 |               className={`btn btn-lg ${active ? "btn-secondary" : "btn-primary"}`}
     | In `FocusTimer` (src/components/FocusTimer.jsx): `className={`btn btn-lg ${active ? "btn-secondary" : "btn-primary"}`}` closes FocusTimer (opened on line 15). Names declared inside that block end here.

 232 |               onClick={toggle}
     | In `FocusTimer` (src/components/FocusTimer.jsx): event prop `onClick={toggle}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 233 |               style={{ minWidth: 130 }}
     | In `FocusTimer` (src/components/FocusTimer.jsx): `style={{ minWidth: 130 }}` closes FocusTimer (opened on line 15). Names declared inside that block end here.

 234 |               aria-label={active ? "Pause timer" : "Start timer"}
     | In `FocusTimer` (src/components/FocusTimer.jsx): `aria-label={active ? "Pause timer" : "Start timer"}` closes FocusTimer (opened on line 15). Names declared inside that block end here.

 235 |             >
     | In `FocusTimer` (src/components/FocusTimer.jsx): statement `>`. It runs when FocusTimer runs, in order, before the next line of the same function.

 236 |               {active ? "⏸ Pause" : "▶ Start"}
     | In `FocusTimer` (src/components/FocusTimer.jsx): `{active ? "⏸ Pause" : "▶ Start"}` closes FocusTimer (opened on line 15). Names declared inside that block end here.

 237 |             </button>
     | In `FocusTimer` (src/components/FocusTimer.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

 238 |             <button className="btn btn-ghost" onClick={() => reset()} aria-label="Reset timer">↺ Reset</button>
     | In `FocusTimer` (src/components/FocusTimer.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button className="btn btn-ghost" onClick={() => reset()} aria-label="Reset timer">↺ Reset</button>`

 239 |             <button className="btn btn-ghost" onClick={switchPhase} aria-label="Switch phase">
     | In `FocusTimer` (src/components/FocusTimer.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button className="btn btn-ghost" onClick={switchPhase} aria-label="Switch phase">`

 240 |               {isWork ? "→ Break" : "→ Work"}
     | In `FocusTimer` (src/components/FocusTimer.jsx): `{isWork ? "→ Break" : "→ Work"}` closes FocusTimer (opened on line 15). Names declared inside that block end here.

 241 |             </button>
     | In `FocusTimer` (src/components/FocusTimer.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

 242 |           </div>
     | In `FocusTimer` (src/components/FocusTimer.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 243 |         </div>
     | In `FocusTimer` (src/components/FocusTimer.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 244 | 
     | Blank line in `src/components/FocusTimer.jsx` (the countdown ring and session saver), inside FocusTimer. The parser skips it. It separates the previous statement from the next so the function is readable.

 245 |         {/* ── Right panel ──────────────────────────────── */}
     | In `FocusTimer` (src/components/FocusTimer.jsx): `{/* ── Right panel ──────────────────────────────── */}` closes FocusTimer (opened on line 15). Names declared inside that block end here.

 246 |         <div className="stack">
     | In `FocusTimer` (src/components/FocusTimer.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="stack">`

 247 |           <div className="card">
     | In `FocusTimer` (src/components/FocusTimer.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="card">`

 248 |             <div className="card-title">Today's Sessions</div>
     | In `FocusTimer` (src/components/FocusTimer.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="card-title">Today's Sessions</div>`

 249 |             <div className="stat-value stat-violet" style={{ fontSize: 42, marginBottom: 4 }}>
     | In `FocusTimer` (src/components/FocusTimer.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="stat-value stat-violet" style={{ fontSize: 42, marginBottom: 4 }}>`

 250 |               {sessionCount}
     | In `FocusTimer` (src/components/FocusTimer.jsx): `{sessionCount}` closes FocusTimer (opened on line 15). Names declared inside that block end here.

 251 |             </div>
     | In `FocusTimer` (src/components/FocusTimer.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 252 |             <div className="text-sm text-muted">{sessionLabel}</div>
     | In `FocusTimer` (src/components/FocusTimer.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="text-sm text-muted">{sessionLabel}</div>`

 253 |             {sessionCount >= 2 && (
     | In `FocusTimer` (src/components/FocusTimer.jsx): statement `{sessionCount >= 2 && (`. It runs when FocusTimer runs, in order, before the next line of the same function.

 254 |               <div className="streak-badge" style={{ marginTop: 10, alignSelf: "flex-start" }}>
     | In `FocusTimer` (src/components/FocusTimer.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="streak-badge" style={{ marginTop: 10, alignSelf: "flex-start" }}>`

 255 |                 🔥 {sessionCount} sessions
     | In `FocusTimer` (src/components/FocusTimer.jsx): `🔥 {sessionCount} sessions` closes FocusTimer (opened on line 15). Names declared inside that block end here.

 256 |               </div>
     | In `FocusTimer` (src/components/FocusTimer.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 257 |             )}
     | In `FocusTimer` (src/components/FocusTimer.jsx): `)}` closes FocusTimer (opened on line 15). Names declared inside that block end here.

 258 |           </div>
     | In `FocusTimer` (src/components/FocusTimer.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 259 | 
     | Blank line in `src/components/FocusTimer.jsx` (the countdown ring and session saver), inside FocusTimer. The parser skips it. It separates the previous statement from the next so the function is readable.

 260 |           <div className="card">
     | In `FocusTimer` (src/components/FocusTimer.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="card">`

 261 |             <div className="card-title">Focus Guard</div>
     | In `FocusTimer` (src/components/FocusTimer.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="card-title">Focus Guard</div>`

 262 |             <div
     | In `FocusTimer` (src/components/FocusTimer.jsx): Opens it. A box that groups the elements inside it. Source: `<div`

 263 |               className="focus-status"
     | In `FocusTimer` (src/components/FocusTimer.jsx): statement `className="focus-status"`. It runs when FocusTimer runs, in order, before the next line of the same function.

 264 |               style={{
     | In `FocusTimer` (src/components/FocusTimer.jsx): statement `style={{`. It runs when FocusTimer runs, in order, before the next line of the same function.

 265 |                 background: active ? "var(--green-dim)" : "var(--border)",
     | In `FocusTimer` (src/components/FocusTimer.jsx): statement `background: active ? "var(--green-dim)" : "var(--border)",`. It runs when FocusTimer runs, in order, before the next line of the same function.

 266 |                 color: active ? "var(--green)" : "var(--muted)",
     | In `FocusTimer` (src/components/FocusTimer.jsx): statement `color: active ? "var(--green)" : "var(--muted)",`. It runs when FocusTimer runs, in order, before the next line of the same function.

 267 |                 marginBottom: 10,
     | In `FocusTimer` (src/components/FocusTimer.jsx): statement `marginBottom: 10,`. It runs when FocusTimer runs, in order, before the next line of the same function.

 268 |               }}
     | In `FocusTimer` (src/components/FocusTimer.jsx): `}}` closes style={{ (opened on line 264). Names declared inside that block end here.

 269 |               role="status"
     | In `FocusTimer` (src/components/FocusTimer.jsx): statement `role="status"`. It runs when FocusTimer runs, in order, before the next line of the same function.

 270 |               aria-live="polite"
     | In `FocusTimer` (src/components/FocusTimer.jsx): statement `aria-live="polite"`. It runs when FocusTimer runs, in order, before the next line of the same function.

 271 |             >
     | In `FocusTimer` (src/components/FocusTimer.jsx): statement `>`. It runs when FocusTimer runs, in order, before the next line of the same function.

 272 |               <span className="focus-status-dot" />
     | In `FocusTimer` (src/components/FocusTimer.jsx): Opens it. An inline box. Source: `<span className="focus-status-dot" />`

 273 |               {active ? "Active — guarding focus" : "Inactive"}
     | In `FocusTimer` (src/components/FocusTimer.jsx): `{active ? "Active — guarding focus" : "Inactive"}` closes FocusTimer (opened on line 15). Names declared inside that block end here.

 274 |             </div>
     | In `FocusTimer` (src/components/FocusTimer.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 275 |             <div className="text-sm text-muted" style={{ lineHeight: 1.7 }}>
     | In `FocusTimer` (src/components/FocusTimer.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="text-sm text-muted" style={{ lineHeight: 1.7 }}>`

 276 |               When you switch tabs during a session, you'll get a gentle nudge.{" "}
     | In `FocusTimer` (src/components/FocusTimer.jsx): `When you switch tabs during a session, you'll get a gentle nudge.{" "}` closes FocusTimer (opened on line 15). Names declared inside that block end here.

 277 |               <span style={{ color: "var(--violet-light)" }}>800ms debounce</span> — quick reference
     | In `FocusTimer` (src/components/FocusTimer.jsx): Opens it. An inline box. Source: `<span style={{ color: "var(--violet-light)" }}>800ms debounce</span> — quick reference`

 278 |               checks won't trigger it.
     | In `FocusTimer` (src/components/FocusTimer.jsx): statement `checks won't trigger it.`. It runs when FocusTimer runs, in order, before the next line of the same function.

 279 |             </div>
     | In `FocusTimer` (src/components/FocusTimer.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 280 |           </div>
     | In `FocusTimer` (src/components/FocusTimer.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 281 | 
     | Blank line in `src/components/FocusTimer.jsx` (the countdown ring and session saver), inside FocusTimer. The parser skips it. It separates the previous statement from the next so the function is readable.

 282 |           <ShieldStatusCard
     | In `FocusTimer` (src/components/FocusTimer.jsx): Opens it. Shared shield status. Home passes variant dashboard. The timer passes variant session and sessionActive. Source: `<ShieldStatusCard`

 283 |             rules={shieldRules}
     | In `FocusTimer` (src/components/FocusTimer.jsx): `rules={shieldRules}` closes FocusTimer (opened on line 15). Names declared inside that block end here.

 284 |             loading={shieldLoading}
     | In `FocusTimer` (src/components/FocusTimer.jsx): `loading={shieldLoading}` closes FocusTimer (opened on line 15). Names declared inside that block end here.

 285 |             sessionActive={active && isWork}
     | In `FocusTimer` (src/components/FocusTimer.jsx): `sessionActive={active && isWork}` closes FocusTimer (opened on line 15). Names declared inside that block end here.

 286 |             variant="session"
     | In `FocusTimer` (src/components/FocusTimer.jsx): statement `variant="session"`. It runs when FocusTimer runs, in order, before the next line of the same function.

 287 |           />
     | In `FocusTimer` (src/components/FocusTimer.jsx): statement `/>`. It runs when FocusTimer runs, in order, before the next line of the same function.

 288 | 
     | Blank line in `src/components/FocusTimer.jsx` (the countdown ring and session saver), inside FocusTimer. The parser skips it. It separates the previous statement from the next so the function is readable.

 289 |           <div className="card">
     | In `FocusTimer` (src/components/FocusTimer.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="card">`

 290 |             <div className="card-title">Affirmation</div>
     | In `FocusTimer` (src/components/FocusTimer.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="card-title">Affirmation</div>`

 291 |             <Affirmations ref={affirmRef} />
     | In `FocusTimer` (src/components/FocusTimer.jsx): Opens it. The sentence box. The parent holds a ref and asks it for a line. Source: `<Affirmations ref={affirmRef} />`

 292 |           </div>
     | In `FocusTimer` (src/components/FocusTimer.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 293 |         </div>
     | In `FocusTimer` (src/components/FocusTimer.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 294 |       </div>
     | In `FocusTimer` (src/components/FocusTimer.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 295 |     </div>
     | In `FocusTimer` (src/components/FocusTimer.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 296 |   );
     | In `FocusTimer` (src/components/FocusTimer.jsx): statement `);`. It runs when FocusTimer runs, in order, before the next line of the same function.

 297 | }
     | In `FocusTimer` (src/components/FocusTimer.jsx): `}` closes FocusTimer (opened on line 15). Names declared inside that block end here.

