# `src/components/Home.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import React, { useEffect, useState } from "react";
     | Import for the Today page: `import React, { useEffect, useState } from "react";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   2 | import { Link } from "react-router-dom";
     | Import for the Today page: `import { Link } from "react-router-dom";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   3 | import api from "../services/api";
     | Import for the Today page: `import api from "../services/api";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   4 | import { useUser } from "../contexts/UserContext";
     | Import for the Today page: `import { useUser } from "../contexts/UserContext";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   5 | import { useEnergy } from "../contexts/EnergyContext";
     | Import for the Today page: `import { useEnergy } from "../contexts/EnergyContext";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   6 | import EnergyControl from "./EnergyControl";
     | Import for the Today page: `import EnergyControl from "./EnergyControl";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   7 | import ShieldStatusCard from "./focus-shield/ShieldStatusCard";
     | Import for the Today page: `import ShieldStatusCard from "./focus-shield/ShieldStatusCard";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   8 | import { useBlockingStore } from "../stores/blockingStore";
     | Import for the Today page: `import { useBlockingStore } from "../stores/blockingStore";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   9 | 
     | Blank line in `src/components/Home.jsx` (the Today page), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  10 | const FEEDBACK_URL = "https://www.jumpybrain.com/#feedback";
     | In `the top of the file` (src/components/Home.jsx): `FEEDBACK_URL`: Hard-coded link to https://www.jumpybrain.com/#feedback. The banner, sidebar, and top bar all open it in a new tab. The code is `const FEEDBACK_URL = "https://www.jumpybrain.com/#feedback";`.

  11 | 
     | Blank line in `src/components/Home.jsx` (the Today page), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  12 | function FeedbackCTACard() {
     | Defines `FeedbackCTACard` in the Today page. A card with one button that opens the feedback URL.

  13 |   return (
     | In `FeedbackCTACard` (src/components/Home.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  14 |     <div className="card feedback-cta-card">
     | In `FeedbackCTACard` (src/components/Home.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="card feedback-cta-card">`

  15 |       <div className="feedback-cta-title">Still improving JumpyBrain</div>
     | In `FeedbackCTACard` (src/components/Home.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="feedback-cta-title">Still improving JumpyBrain</div>`

  16 |       <div className="text-sm" style={{ color: "var(--text-soft)", lineHeight: 1.6, marginBottom: 12 }}>
     | In `FeedbackCTACard` (src/components/Home.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="text-sm" style={{ color: "var(--text-soft)", lineHeight: 1.6, marginBottom: 12 }}>`

  17 |         Some features are still under development and may not work exactly as
     | In `FeedbackCTACard` (src/components/Home.jsx): statement `Some features are still under development and may not work exactly as`. It runs when FeedbackCTACard runs, in order, before the next line of the same function.

  18 |         expected. If you hit an issue or have an idea, we'd love to hear from you.
     | In `FeedbackCTACard` (src/components/Home.jsx): statement `expected. If you hit an issue or have an idea, we'd love to hear from you.`. It runs when FeedbackCTACard runs, in order, before the next line of the same function.

  19 |       </div>
     | In `FeedbackCTACard` (src/components/Home.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  20 |       <a href={FEEDBACK_URL} target="_blank" rel="noopener noreferrer" style={{ textDecoration: "none" }}>
     | In `FeedbackCTACard` (src/components/Home.jsx): Opens it. A normal link. If it has target=_blank it leaves the app. Source: `<a href={FEEDBACK_URL} target="_blank" rel="noopener noreferrer" style={{ textDecoration: "none" }}>`

  21 |         <button className="btn btn-primary btn-sm">Share Feedback →</button>
     | In `FeedbackCTACard` (src/components/Home.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button className="btn btn-primary btn-sm">Share Feedback →</button>`

  22 |       </a>
     | In `FeedbackCTACard` (src/components/Home.jsx): Closes it. A normal link. If it has target=_blank it leaves the app. Source: `</a>`

  23 |     </div>
     | In `FeedbackCTACard` (src/components/Home.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  24 |   );
     | In `FeedbackCTACard` (src/components/Home.jsx): statement `);`. It runs when FeedbackCTACard runs, in order, before the next line of the same function.

  25 | }
     | In `FeedbackCTACard` (src/components/Home.jsx): `}` closes FeedbackCTACard (opened on line 12). Names declared inside that block end here.

  26 | 
     | Blank line in `src/components/Home.jsx` (the Today page), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  27 | export default function Home() {
     | Defines `Home` in the Today page. Today page. Greeting, energy, one recommended task, three stats, quick links, shield status, and a tip that depends on energy.

  28 |   const { user } = useUser();
     | In `Home` (src/components/Home.jsx): `user`: The logged-in profile object. Null means ProtectedRoute renders Auth. The code is `const { user } = useUser();`.

  29 |   const { energy } = useEnergy();
     | In `Home` (src/components/Home.jsx): `energy`: Integer 1–5 from EnergyContext, persisted as bb-energy. Home refetches 'what next' when it changes. TodoList rescores and refetches suggestions. The code is `const { energy } = useEnergy();`.

  30 |   const { rules: shieldRules, loading: shieldLoading, setRules: setShieldRules, setLoading: setShieldLoading } = useBlockingStore();
     | In `Home` (src/components/Home.jsx): `shieldRules`: The blocking rules sitting in useBlockingStore. Home and FocusTimer load them. FocusShieldPage saves them. The code is `const { rules: shieldRules, loading: shieldLoading, setRules: setShieldRules, setLoading: setShieldLoading } = useBlockingStore();`.

  31 |   const [daily, setDaily] = useState({ tasksCompleted: 0, totalSessionMins: 0 });
     | In `Home` (src/components/Home.jsx): `daily`: Today's tasksCompleted and totalSessionMins from GET /stats/daily. The code is `const [daily, setDaily] = useState({ tasksCompleted: 0, totalSessionMins: 0 });`.

  32 |   const [whatNext, setWhatNext] = useState(null);
     | In `Home` (src/components/Home.jsx): `whatNext`: The single task from GET /tasks/what-next?energyLevel=. Null means the list is empty or the request failed. The code is `const [whatNext, setWhatNext] = useState(null);`.

  33 |   const [loadingNext, setLoadingNext] = useState(false);
     | In `Home` (src/components/Home.jsx): React state `loadingNext, setLoadingNext`. The value survives re-renders. Calling the setter re-renders this component. `const [loadingNext, setLoadingNext] = useState(false);`

  34 |   const [streak, setStreak] = useState(0);
     | In `Home` (src/components/Home.jsx): `streak`: How many days back from today, up to 7, have a completed task. Today may be empty; the count stops at the first gap after today. The code is `const [streak, setStreak] = useState(0);`.

  35 |   const [hasTasks, setHasTasks] = useState(true);
     | In `Home` (src/components/Home.jsx): React state `hasTasks, setHasTasks`. The value survives re-renders. Calling the setter re-renders this component. `const [hasTasks, setHasTasks] = useState(true);`

  36 | 
     | Blank line in `src/components/Home.jsx` (the Today page), inside Home. The parser skips it. It separates the previous statement from the next so the function is readable.

  37 |   const hour = new Date().getHours();
     | In `Home` (src/components/Home.jsx): `hour` is assigned `new Date().getHours();`. Later lines in this function read that name.

  38 |   const greeting =
     | In `Home` (src/components/Home.jsx): `greeting` is assigned ``. Later lines in this function read that name.

  39 |     hour < 12 ? "Good morning" : hour < 17 ? "Good afternoon" : "Good evening";
     | In `Home` (src/components/Home.jsx): statement `hour < 12 ? "Good morning" : hour < 17 ? "Good afternoon" : "Good evening";`. It runs when Home runs, in order, before the next line of the same function.

  40 | 
     | Blank line in `src/components/Home.jsx` (the Today page), inside Home. The parser skips it. It separates the previous statement from the next so the function is readable.

  41 |   useEffect(() => {
     | In `Home` (src/components/Home.jsx): opens or continues an effect — `useEffect(() => {`. The effect body runs after paint, and its cleanup runs before the next effect and on unmount.

  42 |     loadStats();
     | In `Home` (src/components/Home.jsx): statement `loadStats();`. It runs when Home runs, in order, before the next line of the same function.

  43 |     loadWhatNext();
     | In `Home` (src/components/Home.jsx): statement `loadWhatNext();`. It runs when Home runs, in order, before the next line of the same function.

  44 |   }, [energy]);
     | In `Home` (src/components/Home.jsx): `}, [energy]);` closes effect in Home (opened on line 41). Names declared inside that block end here.

  45 | 
     | Blank line in `src/components/Home.jsx` (the Today page), inside Home. The parser skips it. It separates the previous statement from the next so the function is readable.

  46 |   useEffect(() => {
     | In `Home` (src/components/Home.jsx): opens or continues an effect — `useEffect(() => {`. The effect body runs after paint, and its cleanup runs before the next effect and on unmount.

  47 |     setShieldLoading(true);
     | In `Home` (src/components/Home.jsx): statement `setShieldLoading(true);`. It runs when Home runs, in order, before the next line of the same function.

  48 |     api.get("/blocking")
     | In `Home` (src/components/Home.jsx): HTTP via the shared Axios instance — `api.get("/blocking")`. The request interceptor adds `Authorization: Bearer <accessToken>`. The response interceptor returns `res.data`, so the awaited value is the JSON body.

  49 |       .then((data) => setShieldRules(data.rules))
     | In `Home` (src/components/Home.jsx): statement `.then((data) => setShieldRules(data.rules))`. It runs when Home runs, in order, before the next line of the same function.

  50 |       .catch(() => {})
     | In `Home` (src/components/Home.jsx): statement `.catch(() => {})`. It runs when Home runs, in order, before the next line of the same function.

  51 |       .finally(() => setShieldLoading(false));
     | In `Home` (src/components/Home.jsx): statement `.finally(() => setShieldLoading(false));`. It runs when Home runs, in order, before the next line of the same function.

  52 |   }, []);
     | In `Home` (src/components/Home.jsx): `}, []);` closes effect in Home (opened on line 46). Names declared inside that block end here.

  53 | 
     | Blank line in `src/components/Home.jsx` (the Today page), inside Home. The parser skips it. It separates the previous statement from the next so the function is readable.

  54 |   async function loadStats() {
     | Defines `loadStats` in the Today page. GET /stats/daily for the tiles and GET /stats/weekly to count the streak.

  55 |     try {
     | In `loadStats` (src/components/Home.jsx): error path `try {`.

  56 |       const { data: d } = await api.get("/stats/daily");
     | In `loadStats` (src/components/Home.jsx): `data:, d` is assigned `await api.get("/stats/daily");`. Later lines in this function read that name.

  57 |       setDaily(d ?? { tasksCompleted: 0, totalSessionMins: 0 });
     | In `loadStats` (src/components/Home.jsx): `setDaily(d ?? { tasksCompleted: 0, totalSessionMins: 0 });` closes try { (opened on line 55). Names declared inside that block end here.

  58 |       const { data: w } = await api.get("/stats/weekly");
     | In `loadStats` (src/components/Home.jsx): `data:, w` is assigned `await api.get("/stats/weekly");`. Later lines in this function read that name.

  59 |       if (w?.tasks) {
     | In `loadStats` (src/components/Home.jsx): branch `if (w?.tasks) {`. Only one side runs.

  60 |         const byDay = {};
     | In `loadStats` (src/components/Home.jsx): `byDay` is assigned `{};`. Later lines in this function read that name.

  61 |         w.tasks.forEach((t) => {
     | In `loadStats` (src/components/Home.jsx): iteration `w.tasks.forEach((t) => {`.

  62 |           const key = t.completedAt?.split("T")[0];
     | In `loadStats` (src/components/Home.jsx): `key` is assigned `t.completedAt?.split("T")[0];`. Later lines in this function read that name.

  63 |           if (key) byDay[key] = true;
     | In `loadStats` (src/components/Home.jsx): branch `if (key) byDay[key] = true;`. Only one side runs.

  64 |         });
     | In `loadStats` (src/components/Home.jsx): `});` closes w.tasks.forEach((t) => { (opened on line 61). Names declared inside that block end here.

  65 |         let s = 0;
     | In `loadStats` (src/components/Home.jsx): `s` is assigned `0;`. Later lines in this function read that name.

  66 |         for (let i = 0; i < 7; i++) {
     | In `loadStats` (src/components/Home.jsx): iteration `for (let i = 0; i < 7; i++) {`.

  67 |           const d = new Date();
     | In `loadStats` (src/components/Home.jsx): `d` is assigned `new Date();`. Later lines in this function read that name.

  68 |           d.setDate(d.getDate() - i);
     | In `loadStats` (src/components/Home.jsx): statement `d.setDate(d.getDate() - i);`. It runs when loadStats runs, in order, before the next line of the same function.

  69 |           const key = d.toISOString().split("T")[0];
     | In `loadStats` (src/components/Home.jsx): `key` is assigned `d.toISOString().split("T")[0];`. Later lines in this function read that name.

  70 |           if (byDay[key]) s++;
     | In `loadStats` (src/components/Home.jsx): branch `if (byDay[key]) s++;`. Only one side runs.

  71 |           else if (i > 0) break;
     | In `loadStats` (src/components/Home.jsx): statement `else if (i > 0) break;`. It runs when loadStats runs, in order, before the next line of the same function.

  72 |         }
     | In `loadStats` (src/components/Home.jsx): `}` closes for (let i = 0; i < 7; i++) { (opened on line 66). Names declared inside that block end here.

  73 |         setStreak(s);
     | In `loadStats` (src/components/Home.jsx): statement `setStreak(s);`. It runs when loadStats runs, in order, before the next line of the same function.

  74 |       }
     | In `loadStats` (src/components/Home.jsx): `}` closes if (w?.tasks) { (opened on line 59). Names declared inside that block end here.

  75 |     } catch {}
     | In `loadStats` (src/components/Home.jsx): `} catch {}` closes try { (opened on line 55). Names declared inside that block end here.

  76 |   }
     | In `loadStats` (src/components/Home.jsx): `}` closes loadStats (opened on line 54). Names declared inside that block end here.

  77 | 
     | Blank line in `src/components/Home.jsx` (the Today page), inside Home. The parser skips it. It separates the previous statement from the next so the function is readable.

  78 |   async function loadWhatNext() {
     | Defines `loadWhatNext` in the Today page. GET /tasks/what-next?energyLevel= plus the current energy. Sets hasTasks from whether a task came back.

  79 |     setLoadingNext(true);
     | In `loadWhatNext` (src/components/Home.jsx): statement `setLoadingNext(true);`. It runs when loadWhatNext runs, in order, before the next line of the same function.

  80 |     try {
     | In `loadWhatNext` (src/components/Home.jsx): error path `try {`.

  81 |       const data = await api.get(`/tasks/what-next?energyLevel=${energy}`);
     | In `loadWhatNext` (src/components/Home.jsx): `data` is assigned `await api.get(`/tasks/what-next?energyLevel=${energy}`);`. Later lines in this function read that name.

  82 |       setWhatNext(data.task || null);
     | In `loadWhatNext` (src/components/Home.jsx): statement `setWhatNext(data.task || null);`. It runs when loadWhatNext runs, in order, before the next line of the same function.

  83 |       setHasTasks(!!data.task);
     | In `loadWhatNext` (src/components/Home.jsx): statement `setHasTasks(!!data.task);`. It runs when loadWhatNext runs, in order, before the next line of the same function.

  84 |     } catch {
     | In `loadWhatNext` (src/components/Home.jsx): `} catch {` closes try { (opened on line 80). Names declared inside that block end here.

  85 |       setWhatNext(null);
     | In `loadWhatNext` (src/components/Home.jsx): statement `setWhatNext(null);`. It runs when loadWhatNext runs, in order, before the next line of the same function.

  86 |       setHasTasks(false);
     | In `loadWhatNext` (src/components/Home.jsx): statement `setHasTasks(false);`. It runs when loadWhatNext runs, in order, before the next line of the same function.

  87 |     } finally {
     | In `loadWhatNext` (src/components/Home.jsx): `} finally {` closes } catch { (opened on line 84). Names declared inside that block end here.

  88 |       setLoadingNext(false);
     | In `loadWhatNext` (src/components/Home.jsx): statement `setLoadingNext(false);`. It runs when loadWhatNext runs, in order, before the next line of the same function.

  89 |     }
     | In `loadWhatNext` (src/components/Home.jsx): `}` closes } finally { (opened on line 87). Names declared inside that block end here.

  90 |   }
     | In `loadWhatNext` (src/components/Home.jsx): `}` closes loadWhatNext (opened on line 78). Names declared inside that block end here.

  91 | 
     | Blank line in `src/components/Home.jsx` (the Today page), inside Home. The parser skips it. It separates the previous statement from the next so the function is readable.

  92 |   function whatNextReason(task) {
     | Defines `whatNextReason` in the Today page. Builds the sentence under the recommended task from due time, estimate, and dread. Does not call the network.

  93 |     if (!task) return "";
     | In `whatNextReason` (src/components/Home.jsx): branch `if (!task) return "";`. Only one side runs.

  94 |     const parts = [];
     | In `whatNextReason` (src/components/Home.jsx): `parts` is assigned `[];`. Later lines in this function read that name.

  95 |     if (task.dueAt) {
     | In `whatNextReason` (src/components/Home.jsx): branch `if (task.dueAt) {`. Only one side runs.

  96 |       const h = Math.round((new Date(task.dueAt) - new Date()) / 3600000);
     | In `whatNextReason` (src/components/Home.jsx): `h` is assigned `Math.round((new Date(task.dueAt) - new Date()) / 3600000);`. Later lines in this function read that name.

  97 |       if (h < 24) parts.push(`Due in ~${h}h`);
     | In `whatNextReason` (src/components/Home.jsx): branch `if (h < 24) parts.push(`Due in ~${h}h`);`. Only one side runs.

  98 |       else parts.push(`Due ${new Date(task.dueAt).toLocaleDateString()}`);
     | In `whatNextReason` (src/components/Home.jsx): `else parts.push(`Due ${new Date(task.dueAt).toLocaleDateString()}`);` closes if (task.dueAt) { (opened on line 95). Names declared inside that block end here.

  99 |     }
     | In `whatNextReason` (src/components/Home.jsx): `}` closes if (task.dueAt) { (opened on line 95). Names declared inside that block end here.

 100 |     if (task.estimateMins) parts.push(`~${task.estimateMins} min`);
     | In `whatNextReason` (src/components/Home.jsx): branch `if (task.estimateMins) parts.push(`~${task.estimateMins} min`);`. Only one side runs.

 101 |     if (task.dreadScore <= 2) parts.push("Low dread — easy to start");
     | In `whatNextReason` (src/components/Home.jsx): branch `if (task.dreadScore <= 2) parts.push("Low dread — easy to start");`. Only one side runs.

 102 |     else if (task.dreadScore >= 4) parts.push("High dread — tackle it now");
     | In `whatNextReason` (src/components/Home.jsx): statement `else if (task.dreadScore >= 4) parts.push("High dread — tackle it now");`. It runs when whatNextReason runs, in order, before the next line of the same function.

 103 |     return parts.join(" · ") || "Good match for your current energy";
     | In `whatNextReason` (src/components/Home.jsx): return `return parts.join(" · ") || "Good match for your current energy";`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

 104 |   }
     | In `whatNextReason` (src/components/Home.jsx): `}` closes whatNextReason (opened on line 92). Names declared inside that block end here.

 105 | 
     | Blank line in `src/components/Home.jsx` (the Today page), inside Home. The parser skips it. It separates the previous statement from the next so the function is readable.

 106 |   return (
     | In `Home` (src/components/Home.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

 107 |     <div>
     | In `Home` (src/components/Home.jsx): Opens it. A box that groups the elements inside it. Source: `<div>`

 108 |       {/* ── Greeting ──────────────────────────────────── */}
     | In `Home` (src/components/Home.jsx): `{/* ── Greeting ──────────────────────────────────── */}` closes Home (opened on line 27). Names declared inside that block end here.

 109 |       <h1 className="page-title">
     | In `Home` (src/components/Home.jsx): Opens it. The page title. Source: `<h1 className="page-title">`

 110 |         {greeting}{user?.name ? `, ${user.name.split(" ")[0]}` : ""}
     | In `Home` (src/components/Home.jsx): `{greeting}{user?.name ? `, ${user.name.split(" ")[0]}` : ""}` closes Home (opened on line 27). Names declared inside that block end here.

 111 |       </h1>
     | In `Home` (src/components/Home.jsx): Closes it. The page title. Source: `</h1>`

 112 |       <p className="page-subtitle">Your ADHD command centre</p>
     | In `Home` (src/components/Home.jsx): Opens it. A paragraph. Source: `<p className="page-subtitle">Your ADHD command centre</p>`

 113 | 
     | Blank line in `src/components/Home.jsx` (the Today page), inside Home. The parser skips it. It separates the previous statement from the next so the function is readable.

 114 |       {/* ── Energy Check-in (unified component) ───────── */}
     | In `Home` (src/components/Home.jsx): `{/* ── Energy Check-in (unified component) ───────── */}` closes Home (opened on line 27). Names declared inside that block end here.

 115 |       <div className="card mb-4">
     | In `Home` (src/components/Home.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="card mb-4">`

 116 |         <div className="card-title">How's your energy right now?</div>
     | In `Home` (src/components/Home.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="card-title">How's your energy right now?</div>`

 117 |         <EnergyControl />
     | In `Home` (src/components/Home.jsx): Opens it. The energy faces. compact is the sidebar dots; without it, the big buttons on Today. Source: `<EnergyControl />`

 118 |       </div>
     | In `Home` (src/components/Home.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 119 | 
     | Blank line in `src/components/Home.jsx` (the Today page), inside Home. The parser skips it. It separates the previous statement from the next so the function is readable.

 120 |       <div className="grid-main">
     | In `Home` (src/components/Home.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="grid-main">`

 121 |         {/* ── Left column ───────────────────────────────── */}
     | In `Home` (src/components/Home.jsx): `{/* ── Left column ───────────────────────────────── */}` closes Home (opened on line 27). Names declared inside that block end here.

 122 |         <div className="stack">
     | In `Home` (src/components/Home.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="stack">`

 123 |           {/* What Next card */}
     | In `Home` (src/components/Home.jsx): `{/* What Next card */}` closes Home (opened on line 27). Names declared inside that block end here.

 124 |           <div className="what-next-card">
     | In `Home` (src/components/Home.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="what-next-card">`

 125 |             <div className="what-next-label">⚡ What next?</div>
     | In `Home` (src/components/Home.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="what-next-label">⚡ What next?</div>`

 126 |             {loadingNext ? (
     | In `Home` (src/components/Home.jsx): statement `{loadingNext ? (`. It runs when Home runs, in order, before the next line of the same function.

 127 |               <div className="text-sm text-muted">Finding the best task for you...</div>
     | In `Home` (src/components/Home.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="text-sm text-muted">Finding the best task for you...</div>`

 128 |             ) : whatNext ? (
     | In `Home` (src/components/Home.jsx): statement `) : whatNext ? (`. It runs when Home runs, in order, before the next line of the same function.

 129 |               <>
     | In `Home` (src/components/Home.jsx): JSX `<element>`. React will create this node when the parent renders. Source: `<>`

 130 |                 <div className="what-next-task">{whatNext.title}</div>
     | In `Home` (src/components/Home.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="what-next-task">{whatNext.title}</div>`

 131 |                 <div className="what-next-reason">{whatNextReason(whatNext)}</div>
     | In `Home` (src/components/Home.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="what-next-reason">{whatNextReason(whatNext)}</div>`

 132 |                 <div style={{ display: "flex", gap: 8, flexWrap: "wrap" }}>
     | In `Home` (src/components/Home.jsx): Opens it. A box that groups the elements inside it. Source: `<div style={{ display: "flex", gap: 8, flexWrap: "wrap" }}>`

 133 |                   <Link to="/focus">
     | In `Home` (src/components/Home.jsx): Opens it. A react-router link. Clicking it changes the URL without a full page reload. Source: `<Link to="/focus">`

 134 |                     <button className="btn btn-primary">▶ Start Focus</button>
     | In `Home` (src/components/Home.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button className="btn btn-primary">▶ Start Focus</button>`

 135 |                   </Link>
     | In `Home` (src/components/Home.jsx): Closes it. A react-router link. Clicking it changes the URL without a full page reload. Source: `</Link>`

 136 |                   <Link to="/todo">
     | In `Home` (src/components/Home.jsx): Opens it. A react-router link. Clicking it changes the URL without a full page reload. Source: `<Link to="/todo">`

 137 |                     <button className="btn btn-ghost btn-sm" style={{ alignSelf: "center" }}>
     | In `Home` (src/components/Home.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button className="btn btn-ghost btn-sm" style={{ alignSelf: "center" }}>`

 138 |                       View all tasks
     | In `Home` (src/components/Home.jsx): statement `View all tasks`. It runs when Home runs, in order, before the next line of the same function.

 139 |                     </button>
     | In `Home` (src/components/Home.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

 140 |                   </Link>
     | In `Home` (src/components/Home.jsx): Closes it. A react-router link. Clicking it changes the URL without a full page reload. Source: `</Link>`

 141 |                 </div>
     | In `Home` (src/components/Home.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 142 |               </>
     | In `Home` (src/components/Home.jsx): JSX `<element>`. This closes that element. Source: `</>`

 143 |             ) : (
     | In `Home` (src/components/Home.jsx): statement `) : (`. It runs when Home runs, in order, before the next line of the same function.

 144 |               /* Empty state: CTA to Brain Dump */
     | Comment inside Home. Not executed. Text: /* Empty state: CTA to Brain Dump */

 145 |               <>
     | In `Home` (src/components/Home.jsx): JSX `<element>`. React will create this node when the parent renders. Source: `<>`

 146 |                 <div className="what-next-task" style={{ fontSize: 15 }}>Your task list is empty</div>
     | In `Home` (src/components/Home.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="what-next-task" style={{ fontSize: 15 }}>Your task list is empty</div>`

 147 |                 <div className="what-next-reason">
     | In `Home` (src/components/Home.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="what-next-reason">`

 148 |                   No tasks, no stress — yet. Do a Brain Dump: type everything
     | In `Home` (src/components/Home.jsx): statement `No tasks, no stress — yet. Do a Brain Dump: type everything`. It runs when Home runs, in order, before the next line of the same function.

 149 |                   rattling around in your head and AI will turn it into a clear list.
     | In `Home` (src/components/Home.jsx): statement `rattling around in your head and AI will turn it into a clear list.`. It runs when Home runs, in order, before the next line of the same function.

 150 |                 </div>
     | In `Home` (src/components/Home.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 151 |                 <div style={{ display: "flex", gap: 8, flexWrap: "wrap" }}>
     | In `Home` (src/components/Home.jsx): Opens it. A box that groups the elements inside it. Source: `<div style={{ display: "flex", gap: 8, flexWrap: "wrap" }}>`

 152 |                   <Link to="/todo?tab=dump">
     | In `Home` (src/components/Home.jsx): Opens it. A react-router link. Clicking it changes the URL without a full page reload. Source: `<Link to="/todo?tab=dump">`

 153 |                     <button className="btn btn-primary">🧠 Brain Dump</button>
     | In `Home` (src/components/Home.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button className="btn btn-primary">🧠 Brain Dump</button>`

 154 |                   </Link>
     | In `Home` (src/components/Home.jsx): Closes it. A react-router link. Clicking it changes the URL without a full page reload. Source: `</Link>`

 155 |                   <Link to="/todo">
     | In `Home` (src/components/Home.jsx): Opens it. A react-router link. Clicking it changes the URL without a full page reload. Source: `<Link to="/todo">`

 156 |                     <button className="btn btn-ghost btn-sm" style={{ alignSelf: "center" }}>
     | In `Home` (src/components/Home.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button className="btn btn-ghost btn-sm" style={{ alignSelf: "center" }}>`

 157 |                       Add a task
     | In `Home` (src/components/Home.jsx): statement `Add a task`. It runs when Home runs, in order, before the next line of the same function.

 158 |                     </button>
     | In `Home` (src/components/Home.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

 159 |                   </Link>
     | In `Home` (src/components/Home.jsx): Closes it. A react-router link. Clicking it changes the URL without a full page reload. Source: `</Link>`

 160 |                 </div>
     | In `Home` (src/components/Home.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 161 |               </>
     | In `Home` (src/components/Home.jsx): JSX `<element>`. This closes that element. Source: `</>`

 162 |             )}
     | In `Home` (src/components/Home.jsx): `)}` closes Home (opened on line 27). Names declared inside that block end here.

 163 |           </div>
     | In `Home` (src/components/Home.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 164 | 
     | Blank line in `src/components/Home.jsx` (the Today page), inside Home. The parser skips it. It separates the previous statement from the next so the function is readable.

 165 |           <div className="feedback-cta-mobile">
     | In `Home` (src/components/Home.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="feedback-cta-mobile">`

 166 |             <FeedbackCTACard />
     | In `Home` (src/components/Home.jsx): JSX `<FeedbackCTACard>`. React will create this node when the parent renders. Source: `<FeedbackCTACard />`

 167 |           </div>
     | In `Home` (src/components/Home.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 168 | 
     | Blank line in `src/components/Home.jsx` (the Today page), inside Home. The parser skips it. It separates the previous statement from the next so the function is readable.

 169 |           {/* Today stats */}
     | In `Home` (src/components/Home.jsx): `{/* Today stats */}` closes Home (opened on line 27). Names declared inside that block end here.

 170 |           <div className="grid-3">
     | In `Home` (src/components/Home.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="grid-3">`

 171 |             <div className="stat-tile">
     | In `Home` (src/components/Home.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="stat-tile">`

 172 |               <div className="stat-value stat-green">
     | In `Home` (src/components/Home.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="stat-value stat-green">`

 173 |                 {daily.tasksCompleted > 0 ? daily.tasksCompleted : "—"}
     | In `Home` (src/components/Home.jsx): `{daily.tasksCompleted > 0 ? daily.tasksCompleted : "—"}` closes Home (opened on line 27). Names declared inside that block end here.

 174 |               </div>
     | In `Home` (src/components/Home.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 175 |               <div className="stat-label">Tasks done</div>
     | In `Home` (src/components/Home.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="stat-label">Tasks done</div>`

 176 |             </div>
     | In `Home` (src/components/Home.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 177 |             <div className="stat-tile">
     | In `Home` (src/components/Home.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="stat-tile">`

 178 |               <div className="stat-value stat-violet">
     | In `Home` (src/components/Home.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="stat-value stat-violet">`

 179 |                 {daily.totalSessionMins > 0 ? daily.totalSessionMins : "—"}
     | In `Home` (src/components/Home.jsx): `{daily.totalSessionMins > 0 ? daily.totalSessionMins : "—"}` closes Home (opened on line 27). Names declared inside that block end here.

 180 |               </div>
     | In `Home` (src/components/Home.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 181 |               <div className="stat-label">Focus mins</div>
     | In `Home` (src/components/Home.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="stat-label">Focus mins</div>`

 182 |             </div>
     | In `Home` (src/components/Home.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 183 |             <div className="stat-tile">
     | In `Home` (src/components/Home.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="stat-tile">`

 184 |               <div className="stat-value stat-amber">
     | In `Home` (src/components/Home.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="stat-value stat-amber">`

 185 |                 {streak > 0 ? `${streak}🔥` : "—"}
     | In `Home` (src/components/Home.jsx): `{streak > 0 ? `${streak}🔥` : "—"}` closes Home (opened on line 27). Names declared inside that block end here.

 186 |               </div>
     | In `Home` (src/components/Home.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 187 |               <div className="stat-label">Day streak</div>
     | In `Home` (src/components/Home.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="stat-label">Day streak</div>`

 188 |             </div>
     | In `Home` (src/components/Home.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 189 |           </div>
     | In `Home` (src/components/Home.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 190 |         </div>
     | In `Home` (src/components/Home.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 191 | 
     | Blank line in `src/components/Home.jsx` (the Today page), inside Home. The parser skips it. It separates the previous statement from the next so the function is readable.

 192 |         {/* ── Right column ──────────────────────────────── */}
     | In `Home` (src/components/Home.jsx): `{/* ── Right column ──────────────────────────────── */}` closes Home (opened on line 27). Names declared inside that block end here.

 193 |         <div className="stack">
     | In `Home` (src/components/Home.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="stack">`

 194 |           <div className="card">
     | In `Home` (src/components/Home.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="card">`

 195 |             <div className="card-title">Quick actions</div>
     | In `Home` (src/components/Home.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="card-title">Quick actions</div>`

 196 |             <div className="stack-sm">
     | In `Home` (src/components/Home.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="stack-sm">`

 197 |               <Link to="/focus" style={{ textDecoration: "none" }}>
     | In `Home` (src/components/Home.jsx): Opens it. A react-router link. Clicking it changes the URL without a full page reload. Source: `<Link to="/focus" style={{ textDecoration: "none" }}>`

 198 |                 <button className="btn btn-primary w-full">
     | In `Home` (src/components/Home.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button className="btn btn-primary w-full">`

 199 |                   🎯 Start Focus Session
     | In `Home` (src/components/Home.jsx): statement `🎯 Start Focus Session`. It runs when Home runs, in order, before the next line of the same function.

 200 |                 </button>
     | In `Home` (src/components/Home.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

 201 |               </Link>
     | In `Home` (src/components/Home.jsx): Closes it. A react-router link. Clicking it changes the URL without a full page reload. Source: `</Link>`

 202 |               <Link to="/todo?tab=dump" style={{ textDecoration: "none" }}>
     | In `Home` (src/components/Home.jsx): Opens it. A react-router link. Clicking it changes the URL without a full page reload. Source: `<Link to="/todo?tab=dump" style={{ textDecoration: "none" }}>`

 203 |                 <button className="btn btn-secondary w-full">
     | In `Home` (src/components/Home.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button className="btn btn-secondary w-full">`

 204 |                   🧠 Brain Dump → Tasks
     | In `Home` (src/components/Home.jsx): statement `🧠 Brain Dump → Tasks`. It runs when Home runs, in order, before the next line of the same function.

 205 |                 </button>
     | In `Home` (src/components/Home.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

 206 |               </Link>
     | In `Home` (src/components/Home.jsx): Closes it. A react-router link. Clicking it changes the URL without a full page reload. Source: `</Link>`

 207 |               <Link to="/blocking" style={{ textDecoration: "none" }}>
     | In `Home` (src/components/Home.jsx): Opens it. A react-router link. Clicking it changes the URL without a full page reload. Source: `<Link to="/blocking" style={{ textDecoration: "none" }}>`

 208 |                 <button className="btn btn-ghost w-full">
     | In `Home` (src/components/Home.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button className="btn btn-ghost w-full">`

 209 |                   🛡️ Manage Focus Shield
     | In `Home` (src/components/Home.jsx): statement `🛡️ Manage Focus Shield`. It runs when Home runs, in order, before the next line of the same function.

 210 |                 </button>
     | In `Home` (src/components/Home.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

 211 |               </Link>
     | In `Home` (src/components/Home.jsx): Closes it. A react-router link. Clicking it changes the URL without a full page reload. Source: `</Link>`

 212 |               <Link to="/dashboard" style={{ textDecoration: "none" }}>
     | In `Home` (src/components/Home.jsx): Opens it. A react-router link. Clicking it changes the URL without a full page reload. Source: `<Link to="/dashboard" style={{ textDecoration: "none" }}>`

 213 |                 <button className="btn btn-ghost w-full">
     | In `Home` (src/components/Home.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button className="btn btn-ghost w-full">`

 214 |                   📊 View Progress
     | In `Home` (src/components/Home.jsx): statement `📊 View Progress`. It runs when Home runs, in order, before the next line of the same function.

 215 |                 </button>
     | In `Home` (src/components/Home.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

 216 |               </Link>
     | In `Home` (src/components/Home.jsx): Closes it. A react-router link. Clicking it changes the URL without a full page reload. Source: `</Link>`

 217 |             </div>
     | In `Home` (src/components/Home.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 218 |           </div>
     | In `Home` (src/components/Home.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 219 | 
     | Blank line in `src/components/Home.jsx` (the Today page), inside Home. The parser skips it. It separates the previous statement from the next so the function is readable.

 220 |           <ShieldStatusCard rules={shieldRules} loading={shieldLoading} variant="dashboard" />
     | In `Home` (src/components/Home.jsx): Opens it. Shared shield status. Home passes variant dashboard. The timer passes variant session and sessionActive. Source: `<ShieldStatusCard rules={shieldRules} loading={shieldLoading} variant="dashboard" />`

 221 | 
     | Blank line in `src/components/Home.jsx` (the Today page), inside Home. The parser skips it. It separates the previous statement from the next so the function is readable.

 222 |           <div className="card">
     | In `Home` (src/components/Home.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="card">`

 223 |             <div className="card-title">Daily tip</div>
     | In `Home` (src/components/Home.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="card-title">Daily tip</div>`

 224 |             <div className="text-sm" style={{ lineHeight: 1.7, color: "var(--text-soft)" }}>
     | In `Home` (src/components/Home.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="text-sm" style={{ lineHeight: 1.7, color: "var(--text-soft)" }}>`

 225 |               {energy <= 2
     | In `Home` (src/components/Home.jsx): statement `{energy <= 2`. It runs when Home runs, in order, before the next line of the same function.

 226 |                 ? "Low energy day — pick the easiest task first. Even 10 minutes counts."
     | In `Home` (src/components/Home.jsx): statement `? "Low energy day — pick the easiest task first. Even 10 minutes counts."`. It runs when Home runs, in order, before the next line of the same function.

 227 |                 : energy === 3
     | In `Home` (src/components/Home.jsx): statement `: energy === 3`. It runs when Home runs, in order, before the next line of the same function.

 228 |                 ? "Pick 2 tasks. Start small. Consistency beats intensity."
     | In `Home` (src/components/Home.jsx): statement `? "Pick 2 tasks. Start small. Consistency beats intensity."`. It runs when Home runs, in order, before the next line of the same function.

 229 |                 : "Peak energy — tackle your most dreaded task now while you have momentum."}
     | In `Home` (src/components/Home.jsx): `: "Peak energy — tackle your most dreaded task now while you have momentum."}` closes Home (opened on line 27). Names declared inside that block end here.

 230 |             </div>
     | In `Home` (src/components/Home.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 231 |           </div>
     | In `Home` (src/components/Home.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 232 | 
     | Blank line in `src/components/Home.jsx` (the Today page), inside Home. The parser skips it. It separates the previous statement from the next so the function is readable.

 233 |           <div className="feedback-cta-desktop">
     | In `Home` (src/components/Home.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="feedback-cta-desktop">`

 234 |             <FeedbackCTACard />
     | In `Home` (src/components/Home.jsx): JSX `<FeedbackCTACard>`. React will create this node when the parent renders. Source: `<FeedbackCTACard />`

 235 |           </div>
     | In `Home` (src/components/Home.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 236 |         </div>
     | In `Home` (src/components/Home.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 237 |       </div>
     | In `Home` (src/components/Home.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 238 |     </div>
     | In `Home` (src/components/Home.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 239 |   );
     | In `Home` (src/components/Home.jsx): statement `);`. It runs when Home runs, in order, before the next line of the same function.

 240 | }
     | In `Home` (src/components/Home.jsx): `}` closes Home (opened on line 27). Names declared inside that block end here.

