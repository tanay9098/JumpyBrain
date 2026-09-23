# `src/components/Dashboard.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import { useEffect, useState } from "react";
     | Import for the progress charts: `import { useEffect, useState } from "react";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   2 | import api from "../services/api";
     | Import for the progress charts: `import api from "../services/api";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   3 | import {
     | Import for the progress charts: `import {`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   4 |   BarChart, Bar,
     | In `the top of the file` (src/components/Dashboard.jsx): statement `BarChart, Bar,`. It runs when the top of the file runs, in order, before the next line of the same function.

   5 |   LineChart, Line,
     | In `the top of the file` (src/components/Dashboard.jsx): statement `LineChart, Line,`. It runs when the top of the file runs, in order, before the next line of the same function.

   6 |   XAxis, YAxis,
     | In `the top of the file` (src/components/Dashboard.jsx): statement `XAxis, YAxis,`. It runs when the top of the file runs, in order, before the next line of the same function.

   7 |   Tooltip, CartesianGrid,
     | In `the top of the file` (src/components/Dashboard.jsx): statement `Tooltip, CartesianGrid,`. It runs when the top of the file runs, in order, before the next line of the same function.

   8 |   ResponsiveContainer, ReferenceLine,
     | In `the top of the file` (src/components/Dashboard.jsx): statement `ResponsiveContainer, ReferenceLine,`. It runs when the top of the file runs, in order, before the next line of the same function.

   9 | } from "recharts";
     | In `the top of the file` (src/components/Dashboard.jsx): `} from "recharts";` closes import { (opened on line 3). Names declared inside that block end here.

  10 | 
     | Blank line in `src/components/Dashboard.jsx` (the progress charts), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  11 | function ChartLegend({ items }) {
     | Defines `ChartLegend` in the progress charts. Colored swatches. It does not read chart data.

  12 |   return (
     | In `ChartLegend` (src/components/Dashboard.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  13 |     <div className="chart-legend">
     | In `ChartLegend` (src/components/Dashboard.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="chart-legend">`

  14 |       {items.map(({ label, color }) => (
     | In `ChartLegend` (src/components/Dashboard.jsx): iteration `{items.map(({ label, color }) => (`.

  15 |         <div key={label} className="chart-legend-item">
     | In `ChartLegend` (src/components/Dashboard.jsx): Opens it. A box that groups the elements inside it. Source: `<div key={label} className="chart-legend-item">`

  16 |           <div className="chart-legend-swatch" style={{ background: color }} />
     | In `ChartLegend` (src/components/Dashboard.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="chart-legend-swatch" style={{ background: color }} />`

  17 |           <span>{label}</span>
     | In `ChartLegend` (src/components/Dashboard.jsx): Opens it. An inline box. Source: `<span>{label}</span>`

  18 |         </div>
     | In `ChartLegend` (src/components/Dashboard.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  19 |       ))}
     | In `ChartLegend` (src/components/Dashboard.jsx): `))}` closes ChartLegend (opened on line 11). Names declared inside that block end here.

  20 |     </div>
     | In `ChartLegend` (src/components/Dashboard.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  21 |   );
     | In `ChartLegend` (src/components/Dashboard.jsx): statement `);`. It runs when ChartLegend runs, in order, before the next line of the same function.

  22 | }
     | In `ChartLegend` (src/components/Dashboard.jsx): `}` closes ChartLegend (opened on line 11). Names declared inside that block end here.

  23 | 
     | Blank line in `src/components/Dashboard.jsx` (the progress charts), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  24 | export default function Dashboard() {
     | Defines `Dashboard` in the progress charts. Four tiles plus a 7-day bar chart and a 30-day line chart from /stats/daily, /weekly, and /monthly.

  25 |   const [daily, setDaily] = useState({ tasksCompleted: 0, totalSessionMins: 0 });
     | In `Dashboard` (src/components/Dashboard.jsx): `daily`: Today's tasksCompleted and totalSessionMins from GET /stats/daily. The code is `const [daily, setDaily] = useState({ tasksCompleted: 0, totalSessionMins: 0 });`.

  26 |   const [weekly, setWeekly] = useState([]);
     | In `Dashboard` (src/components/Dashboard.jsx): React state `weekly, setWeekly`. The value survives re-renders. Calling the setter re-renders this component. `const [weekly, setWeekly] = useState([]);`

  27 |   const [monthly, setMonthly] = useState([]);
     | In `Dashboard` (src/components/Dashboard.jsx): React state `monthly, setMonthly`. The value survives re-renders. Calling the setter re-renders this component. `const [monthly, setMonthly] = useState([]);`

  28 |   const [streak, setStreak] = useState(0);
     | In `Dashboard` (src/components/Dashboard.jsx): `streak`: How many days back from today, up to 7, have a completed task. Today may be empty; the count stops at the first gap after today. The code is `const [streak, setStreak] = useState(0);`.

  29 |   const [totalCompleted, setTotalCompleted] = useState(0);
     | In `Dashboard` (src/components/Dashboard.jsx): React state `totalCompleted, setTotalCompleted`. The value survives re-renders. Calling the setter re-renders this component. `const [totalCompleted, setTotalCompleted] = useState(0);`

  30 | 
     | Blank line in `src/components/Dashboard.jsx` (the progress charts), inside Dashboard. The parser skips it. It separates the previous statement from the next so the function is readable.

  31 |   useEffect(() => { load(); }, []);
     | In `Dashboard` (src/components/Dashboard.jsx): opens or continues an effect — `useEffect(() => { load(); }, []);`. The effect body runs after paint, and its cleanup runs before the next effect and on unmount.

  32 | 
     | Blank line in `src/components/Dashboard.jsx` (the progress charts), inside Dashboard. The parser skips it. It separates the previous statement from the next so the function is readable.

  33 |   async function load() {
     | Defines `load` in the progress charts. GET /tasks and, on the task page, keeps only tasks that are not completed. Calendar and the deadline page keep a wider set.

  34 |     try {
     | In `load` (src/components/Dashboard.jsx): error path `try {`.

  35 |       const [d, w, m] = await Promise.all([
     | In `load` (src/components/Dashboard.jsx): `d, w, m` is assigned `await Promise.all([`. Later lines in this function read that name.

  36 |         api.get("/stats/daily"),
     | In `load` (src/components/Dashboard.jsx): HTTP via the shared Axios instance — `api.get("/stats/daily"),`. The request interceptor adds `Authorization: Bearer <accessToken>`. The response interceptor returns `res.data`, so the awaited value is the JSON body.

  37 |         api.get("/stats/weekly"),
     | In `load` (src/components/Dashboard.jsx): HTTP via the shared Axios instance — `api.get("/stats/weekly"),`. The request interceptor adds `Authorization: Bearer <accessToken>`. The response interceptor returns `res.data`, so the awaited value is the JSON body.

  38 |         api.get("/stats/monthly"),
     | In `load` (src/components/Dashboard.jsx): HTTP via the shared Axios instance — `api.get("/stats/monthly"),`. The request interceptor adds `Authorization: Bearer <accessToken>`. The response interceptor returns `res.data`, so the awaited value is the JSON body.

  39 |       ]);
     | In `load` (src/components/Dashboard.jsx): statement `]);`. It runs when load runs, in order, before the next line of the same function.

  40 | 
     | Blank line in `src/components/Dashboard.jsx` (the progress charts), inside load. The parser skips it. It separates the previous statement from the next so the function is readable.

  41 |       setDaily(d);
     | In `load` (src/components/Dashboard.jsx): statement `setDaily(d);`. It runs when load runs, in order, before the next line of the same function.

  42 | 
     | Blank line in `src/components/Dashboard.jsx` (the progress charts), inside load. The parser skips it. It separates the previous statement from the next so the function is readable.

  43 |       const weekData = processWeekly(w.tasks || [], w.sessions || []);
     | In `load` (src/components/Dashboard.jsx): `weekData` is assigned `processWeekly(w.tasks || [], w.sessions || []);`. Later lines in this function read that name.

  44 |       setWeekly(weekData);
     | In `load` (src/components/Dashboard.jsx): statement `setWeekly(weekData);`. It runs when load runs, in order, before the next line of the same function.

  45 |       setMonthly(processMonthly(m.tasks || [], m.sessions || []));
     | In `load` (src/components/Dashboard.jsx): statement `setMonthly(processMonthly(m.tasks || [], m.sessions || []));`. It runs when load runs, in order, before the next line of the same function.

  46 | 
     | Blank line in `src/components/Dashboard.jsx` (the progress charts), inside load. The parser skips it. It separates the previous statement from the next so the function is readable.

  47 |       // Streak: consecutive days with at least 1 completed task
     | Comment inside load. Not executed. It documents the next code: Streak: consecutive days with at least 1 completed task

  48 |       const byDay = {};
     | In `load` (src/components/Dashboard.jsx): `byDay` is assigned `{};`. Later lines in this function read that name.

  49 |       (w.tasks || []).forEach((t) => {
     | In `load` (src/components/Dashboard.jsx): iteration `(w.tasks || []).forEach((t) => {`.

  50 |         const key = t.completedAt?.split("T")[0];
     | In `load` (src/components/Dashboard.jsx): `key` is assigned `t.completedAt?.split("T")[0];`. Later lines in this function read that name.

  51 |         if (key) byDay[key] = true;
     | In `load` (src/components/Dashboard.jsx): branch `if (key) byDay[key] = true;`. Only one side runs.

  52 |       });
     | In `load` (src/components/Dashboard.jsx): `});` closes (w.tasks || []).forEach((t) => { (opened on line 49). Names declared inside that block end here.

  53 |       let s = 0;
     | In `load` (src/components/Dashboard.jsx): `s` is assigned `0;`. Later lines in this function read that name.

  54 |       for (let i = 0; i < 7; i++) {
     | In `load` (src/components/Dashboard.jsx): iteration `for (let i = 0; i < 7; i++) {`.

  55 |         const dt = new Date();
     | In `load` (src/components/Dashboard.jsx): `dt` is assigned `new Date();`. Later lines in this function read that name.

  56 |         dt.setDate(dt.getDate() - i);
     | In `load` (src/components/Dashboard.jsx): statement `dt.setDate(dt.getDate() - i);`. It runs when load runs, in order, before the next line of the same function.

  57 |         const key = dt.toISOString().split("T")[0];
     | In `load` (src/components/Dashboard.jsx): `key` is assigned `dt.toISOString().split("T")[0];`. Later lines in this function read that name.

  58 |         if (byDay[key]) s++;
     | In `load` (src/components/Dashboard.jsx): branch `if (byDay[key]) s++;`. Only one side runs.

  59 |         else if (i > 0) break;
     | In `load` (src/components/Dashboard.jsx): statement `else if (i > 0) break;`. It runs when load runs, in order, before the next line of the same function.

  60 |       }
     | In `load` (src/components/Dashboard.jsx): `}` closes for (let i = 0; i < 7; i++) { (opened on line 54). Names declared inside that block end here.

  61 |       setStreak(s);
     | In `load` (src/components/Dashboard.jsx): statement `setStreak(s);`. It runs when load runs, in order, before the next line of the same function.

  62 |       setTotalCompleted(weekData.reduce((acc, d) => acc + d.tasks, 0));
     | In `load` (src/components/Dashboard.jsx): statement `setTotalCompleted(weekData.reduce((acc, d) => acc + d.tasks, 0));`. It runs when load runs, in order, before the next line of the same function.

  63 |     } catch {}
     | In `load` (src/components/Dashboard.jsx): `} catch {}` closes try { (opened on line 34). Names declared inside that block end here.

  64 |   }
     | In `load` (src/components/Dashboard.jsx): `}` closes load (opened on line 33). Names declared inside that block end here.

  65 | 
     | Blank line in `src/components/Dashboard.jsx` (the progress charts), inside Dashboard. The parser skips it. It separates the previous statement from the next so the function is readable.

  66 |   function processWeekly(tasks, sessions) {
     | Defines `processWeekly` in the progress charts. Builds seven day buckets ending today and drops completed tasks and session minutes into them.

  67 |     const map = {};
     | In `processWeekly` (src/components/Dashboard.jsx): `map` is assigned `{};`. Later lines in this function read that name.

  68 |     for (let i = 6; i >= 0; i--) {
     | In `processWeekly` (src/components/Dashboard.jsx): iteration `for (let i = 6; i >= 0; i--) {`.

  69 |       const d = new Date();
     | In `processWeekly` (src/components/Dashboard.jsx): `d` is assigned `new Date();`. Later lines in this function read that name.

  70 |       d.setDate(d.getDate() - i);
     | In `processWeekly` (src/components/Dashboard.jsx): statement `d.setDate(d.getDate() - i);`. It runs when processWeekly runs, in order, before the next line of the same function.

  71 |       const key = d.toISOString().split("T")[0];
     | In `processWeekly` (src/components/Dashboard.jsx): `key` is assigned `d.toISOString().split("T")[0];`. Later lines in this function read that name.

  72 |       const label = d.toLocaleDateString("en", { weekday: "short" });
     | In `processWeekly` (src/components/Dashboard.jsx): `label` is assigned `d.toLocaleDateString("en", { weekday: "short" });`. Later lines in this function read that name.

  73 |       map[key] = { date: label, tasks: 0, minutes: 0 };
     | In `processWeekly` (src/components/Dashboard.jsx): `map[key] = { date: label, tasks: 0, minutes: 0 };` closes for (let i = 6; i >= 0; i--) { (opened on line 68). Names declared inside that block end here.

  74 |     }
     | In `processWeekly` (src/components/Dashboard.jsx): `}` closes for (let i = 6; i >= 0; i--) { (opened on line 68). Names declared inside that block end here.

  75 |     tasks.forEach((t) => {
     | In `processWeekly` (src/components/Dashboard.jsx): iteration `tasks.forEach((t) => {`.

  76 |       const key = t.completedAt?.split("T")[0];
     | In `processWeekly` (src/components/Dashboard.jsx): `key` is assigned `t.completedAt?.split("T")[0];`. Later lines in this function read that name.

  77 |       if (map[key]) map[key].tasks++;
     | In `processWeekly` (src/components/Dashboard.jsx): branch `if (map[key]) map[key].tasks++;`. Only one side runs.

  78 |     });
     | In `processWeekly` (src/components/Dashboard.jsx): `});` closes tasks.forEach((t) => { (opened on line 75). Names declared inside that block end here.

  79 |     sessions.forEach((s) => {
     | In `processWeekly` (src/components/Dashboard.jsx): iteration `sessions.forEach((s) => {`.

  80 |       const key = s.completedAt?.split("T")[0];
     | In `processWeekly` (src/components/Dashboard.jsx): `key` is assigned `s.completedAt?.split("T")[0];`. Later lines in this function read that name.

  81 |       if (map[key]) map[key].minutes += s.durationMins || 0;
     | In `processWeekly` (src/components/Dashboard.jsx): branch `if (map[key]) map[key].minutes += s.durationMins || 0;`. Only one side runs.

  82 |     });
     | In `processWeekly` (src/components/Dashboard.jsx): `});` closes sessions.forEach((s) => { (opened on line 79). Names declared inside that block end here.

  83 |     return Object.values(map);
     | In `processWeekly` (src/components/Dashboard.jsx): return `return Object.values(map);`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  84 |   }
     | In `processWeekly` (src/components/Dashboard.jsx): `}` closes processWeekly (opened on line 66). Names declared inside that block end here.

  85 | 
     | Blank line in `src/components/Dashboard.jsx` (the progress charts), inside Dashboard. The parser skips it. It separates the previous statement from the next so the function is readable.

  86 |   function processMonthly(tasks, sessions) {
     | Defines `processMonthly` in the progress charts. Same for 30 days. Labels are M/D.

  87 |     const map = {};
     | In `processMonthly` (src/components/Dashboard.jsx): `map` is assigned `{};`. Later lines in this function read that name.

  88 |     for (let i = 29; i >= 0; i--) {
     | In `processMonthly` (src/components/Dashboard.jsx): iteration `for (let i = 29; i >= 0; i--) {`.

  89 |       const d = new Date();
     | In `processMonthly` (src/components/Dashboard.jsx): `d` is assigned `new Date();`. Later lines in this function read that name.

  90 |       d.setDate(d.getDate() - i);
     | In `processMonthly` (src/components/Dashboard.jsx): statement `d.setDate(d.getDate() - i);`. It runs when processMonthly runs, in order, before the next line of the same function.

  91 |       const key = d.toISOString().split("T")[0];
     | In `processMonthly` (src/components/Dashboard.jsx): `key` is assigned `d.toISOString().split("T")[0];`. Later lines in this function read that name.

  92 |       const label = `${d.getMonth() + 1}/${d.getDate()}`;
     | In `processMonthly` (src/components/Dashboard.jsx): `label` is assigned ``${d.getMonth() + 1}/${d.getDate()}`;`. Later lines in this function read that name.

  93 |       map[key] = { date: label, tasks: 0, minutes: 0 };
     | In `processMonthly` (src/components/Dashboard.jsx): `map[key] = { date: label, tasks: 0, minutes: 0 };` closes for (let i = 29; i >= 0; i--) { (opened on line 88). Names declared inside that block end here.

  94 |     }
     | In `processMonthly` (src/components/Dashboard.jsx): `}` closes for (let i = 29; i >= 0; i--) { (opened on line 88). Names declared inside that block end here.

  95 |     tasks.forEach((t) => {
     | In `processMonthly` (src/components/Dashboard.jsx): iteration `tasks.forEach((t) => {`.

  96 |       const key = t.completedAt?.split("T")[0];
     | In `processMonthly` (src/components/Dashboard.jsx): `key` is assigned `t.completedAt?.split("T")[0];`. Later lines in this function read that name.

  97 |       if (map[key]) map[key].tasks++;
     | In `processMonthly` (src/components/Dashboard.jsx): branch `if (map[key]) map[key].tasks++;`. Only one side runs.

  98 |     });
     | In `processMonthly` (src/components/Dashboard.jsx): `});` closes tasks.forEach((t) => { (opened on line 95). Names declared inside that block end here.

  99 |     sessions.forEach((s) => {
     | In `processMonthly` (src/components/Dashboard.jsx): iteration `sessions.forEach((s) => {`.

 100 |       const key = s.completedAt?.split("T")[0];
     | In `processMonthly` (src/components/Dashboard.jsx): `key` is assigned `s.completedAt?.split("T")[0];`. Later lines in this function read that name.

 101 |       if (map[key]) map[key].minutes += s.durationMins || 0;
     | In `processMonthly` (src/components/Dashboard.jsx): branch `if (map[key]) map[key].minutes += s.durationMins || 0;`. Only one side runs.

 102 |     });
     | In `processMonthly` (src/components/Dashboard.jsx): `});` closes sessions.forEach((s) => { (opened on line 99). Names declared inside that block end here.

 103 |     return Object.values(map);
     | In `processMonthly` (src/components/Dashboard.jsx): return `return Object.values(map);`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

 104 |   }
     | In `processMonthly` (src/components/Dashboard.jsx): `}` closes processMonthly (opened on line 86). Names declared inside that block end here.

 105 | 
     | Blank line in `src/components/Dashboard.jsx` (the progress charts), inside Dashboard. The parser skips it. It separates the previous statement from the next so the function is readable.

 106 |   const tooltipStyle = {
     | In `Dashboard` (src/components/Dashboard.jsx): `tooltipStyle` is assigned `{`. Later lines in this function read that name.

 107 |     backgroundColor: "var(--card)",
     | In `Dashboard` (src/components/Dashboard.jsx): statement `backgroundColor: "var(--card)",`. It runs when Dashboard runs, in order, before the next line of the same function.

 108 |     border: "1px solid var(--border)",
     | In `Dashboard` (src/components/Dashboard.jsx): statement `border: "1px solid var(--border)",`. It runs when Dashboard runs, in order, before the next line of the same function.

 109 |     borderRadius: 8,
     | In `Dashboard` (src/components/Dashboard.jsx): statement `borderRadius: 8,`. It runs when Dashboard runs, in order, before the next line of the same function.

 110 |     color: "var(--text)",
     | In `Dashboard` (src/components/Dashboard.jsx): statement `color: "var(--text)",`. It runs when Dashboard runs, in order, before the next line of the same function.

 111 |     fontSize: 13,
     | In `Dashboard` (src/components/Dashboard.jsx): statement `fontSize: 13,`. It runs when Dashboard runs, in order, before the next line of the same function.

 112 |   };
     | In `Dashboard` (src/components/Dashboard.jsx): `};` closes const tooltipStyle = { (opened on line 106). Names declared inside that block end here.

 113 | 
     | Blank line in `src/components/Dashboard.jsx` (the progress charts), inside Dashboard. The parser skips it. It separates the previous statement from the next so the function is readable.

 114 |   const hasWeeklyData = weekly.some((d) => d.tasks > 0 || d.minutes > 0);
     | In `Dashboard` (src/components/Dashboard.jsx): `hasWeeklyData` is assigned `weekly.some((d) => d.tasks > 0 || d.minutes > 0);`. Later lines in this function read that name.

 115 |   const hasMonthlyData = monthly.some((d) => d.tasks > 0 || d.minutes > 0);
     | In `Dashboard` (src/components/Dashboard.jsx): `hasMonthlyData` is assigned `monthly.some((d) => d.tasks > 0 || d.minutes > 0);`. Later lines in this function read that name.

 116 | 
     | Blank line in `src/components/Dashboard.jsx` (the progress charts), inside Dashboard. The parser skips it. It separates the previous statement from the next so the function is readable.

 117 |   return (
     | In `Dashboard` (src/components/Dashboard.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

 118 |     <div>
     | In `Dashboard` (src/components/Dashboard.jsx): Opens it. A box that groups the elements inside it. Source: `<div>`

 119 |       <h1 className="page-title">Stats</h1>
     | In `Dashboard` (src/components/Dashboard.jsx): Opens it. The page title. Source: `<h1 className="page-title">Stats</h1>`

 120 |       <p className="page-subtitle">Track focus, tasks, and streaks over time</p>
     | In `Dashboard` (src/components/Dashboard.jsx): Opens it. A paragraph. Source: `<p className="page-subtitle">Track focus, tasks, and streaks over time</p>`

 121 | 
     | Blank line in `src/components/Dashboard.jsx` (the progress charts), inside Dashboard. The parser skips it. It separates the previous statement from the next so the function is readable.

 122 |       {/* ── Top stat tiles ─────────────────────────────────── */}
     | In `Dashboard` (src/components/Dashboard.jsx): `{/* ── Top stat tiles ─────────────────────────────────── */}` closes Dashboard (opened on line 24). Names declared inside that block end here.

 123 |       <div className="grid-4 mb-4">
     | In `Dashboard` (src/components/Dashboard.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="grid-4 mb-4">`

 124 |         <div className="stat-tile">
     | In `Dashboard` (src/components/Dashboard.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="stat-tile">`

 125 |           <div className="stat-value stat-green">{daily.tasksCompleted ?? 0}</div>
     | In `Dashboard` (src/components/Dashboard.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="stat-value stat-green">{daily.tasksCompleted ?? 0}</div>`

 126 |           <div className="stat-label">Tasks today</div>
     | In `Dashboard` (src/components/Dashboard.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="stat-label">Tasks today</div>`

 127 |         </div>
     | In `Dashboard` (src/components/Dashboard.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 128 |         <div className="stat-tile">
     | In `Dashboard` (src/components/Dashboard.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="stat-tile">`

 129 |           <div className="stat-value stat-violet">{daily.totalSessionMins ?? 0}</div>
     | In `Dashboard` (src/components/Dashboard.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="stat-value stat-violet">{daily.totalSessionMins ?? 0}</div>`

 130 |           <div className="stat-label">Focus mins today</div>
     | In `Dashboard` (src/components/Dashboard.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="stat-label">Focus mins today</div>`

 131 |         </div>
     | In `Dashboard` (src/components/Dashboard.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 132 |         <div className="stat-tile">
     | In `Dashboard` (src/components/Dashboard.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="stat-tile">`

 133 |           <div className="stat-value stat-amber">
     | In `Dashboard` (src/components/Dashboard.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="stat-value stat-amber">`

 134 |             {streak > 0 ? `${streak}🔥` : "—"}
     | In `Dashboard` (src/components/Dashboard.jsx): `{streak > 0 ? `${streak}🔥` : "—"}` closes Dashboard (opened on line 24). Names declared inside that block end here.

 135 |           </div>
     | In `Dashboard` (src/components/Dashboard.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 136 |           <div className="stat-label">Day streak</div>
     | In `Dashboard` (src/components/Dashboard.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="stat-label">Day streak</div>`

 137 |         </div>
     | In `Dashboard` (src/components/Dashboard.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 138 |         <div className="stat-tile">
     | In `Dashboard` (src/components/Dashboard.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="stat-tile">`

 139 |           <div className="stat-value" style={{ color: "var(--text)" }}>
     | In `Dashboard` (src/components/Dashboard.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="stat-value" style={{ color: "var(--text)" }}>`

 140 |             {totalCompleted || "—"}
     | In `Dashboard` (src/components/Dashboard.jsx): `{totalCompleted || "—"}` closes Dashboard (opened on line 24). Names declared inside that block end here.

 141 |           </div>
     | In `Dashboard` (src/components/Dashboard.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 142 |           <div className="stat-label">Tasks this week</div>
     | In `Dashboard` (src/components/Dashboard.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="stat-label">Tasks this week</div>`

 143 |         </div>
     | In `Dashboard` (src/components/Dashboard.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 144 |       </div>
     | In `Dashboard` (src/components/Dashboard.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 145 | 
     | Blank line in `src/components/Dashboard.jsx` (the progress charts), inside Dashboard. The parser skips it. It separates the previous statement from the next so the function is readable.

 146 |       {/* ── Weekly bar chart ────────────────────────────────── */}
     | In `Dashboard` (src/components/Dashboard.jsx): `{/* ── Weekly bar chart ────────────────────────────────── */}` closes Dashboard (opened on line 24). Names declared inside that block end here.

 147 |       <div className="card mb-4">
     | In `Dashboard` (src/components/Dashboard.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="card mb-4">`

 148 |         <div className="chart-header">
     | In `Dashboard` (src/components/Dashboard.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="chart-header">`

 149 |           <div className="card-title" style={{ margin: 0 }}>Tasks Completed — Last 7 Days</div>
     | In `Dashboard` (src/components/Dashboard.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="card-title" style={{ margin: 0 }}>Tasks Completed — Last 7 Days</div>`

 150 |           <ChartLegend items={[{ label: "Tasks", color: "var(--violet)" }]} />
     | In `Dashboard` (src/components/Dashboard.jsx): JSX `<ChartLegend>`. React will create this node when the parent renders. Source: `<ChartLegend items={[{ label: "Tasks", color: "var(--violet)" }]} />`

 151 |         </div>
     | In `Dashboard` (src/components/Dashboard.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 152 |         {hasWeeklyData ? (
     | In `Dashboard` (src/components/Dashboard.jsx): statement `{hasWeeklyData ? (`. It runs when Dashboard runs, in order, before the next line of the same function.

 153 |           <ResponsiveContainer width="100%" height={220}>
     | In `Dashboard` (src/components/Dashboard.jsx): JSX `<ResponsiveContainer>`. React will create this node when the parent renders. Source: `<ResponsiveContainer width="100%" height={220}>`

 154 |             <BarChart data={weekly} barSize={28}>
     | In `Dashboard` (src/components/Dashboard.jsx): JSX `<BarChart>`. React will create this node when the parent renders. Source: `<BarChart data={weekly} barSize={28}>`

 155 |               <XAxis
     | In `Dashboard` (src/components/Dashboard.jsx): JSX `<XAxis>`. React will create this node when the parent renders. Source: `<XAxis`

 156 |                 dataKey="date"
     | In `Dashboard` (src/components/Dashboard.jsx): statement `dataKey="date"`. It runs when Dashboard runs, in order, before the next line of the same function.

 157 |                 tick={{ fill: "var(--muted)", fontSize: 12 }}
     | In `Dashboard` (src/components/Dashboard.jsx): `tick={{ fill: "var(--muted)", fontSize: 12 }}` closes Dashboard (opened on line 24). Names declared inside that block end here.

 158 |                 axisLine={false}
     | In `Dashboard` (src/components/Dashboard.jsx): `axisLine={false}` closes Dashboard (opened on line 24). Names declared inside that block end here.

 159 |                 tickLine={false}
     | In `Dashboard` (src/components/Dashboard.jsx): `tickLine={false}` closes Dashboard (opened on line 24). Names declared inside that block end here.

 160 |               />
     | In `Dashboard` (src/components/Dashboard.jsx): statement `/>`. It runs when Dashboard runs, in order, before the next line of the same function.

 161 |               <YAxis
     | In `Dashboard` (src/components/Dashboard.jsx): JSX `<YAxis>`. React will create this node when the parent renders. Source: `<YAxis`

 162 |                 tick={{ fill: "var(--muted)", fontSize: 12 }}
     | In `Dashboard` (src/components/Dashboard.jsx): `tick={{ fill: "var(--muted)", fontSize: 12 }}` closes Dashboard (opened on line 24). Names declared inside that block end here.

 163 |                 axisLine={false}
     | In `Dashboard` (src/components/Dashboard.jsx): `axisLine={false}` closes Dashboard (opened on line 24). Names declared inside that block end here.

 164 |                 tickLine={false}
     | In `Dashboard` (src/components/Dashboard.jsx): `tickLine={false}` closes Dashboard (opened on line 24). Names declared inside that block end here.

 165 |                 allowDecimals={false}
     | In `Dashboard` (src/components/Dashboard.jsx): `allowDecimals={false}` closes Dashboard (opened on line 24). Names declared inside that block end here.

 166 |                 domain={[0, "auto"]}
     | In `Dashboard` (src/components/Dashboard.jsx): `domain={[0, "auto"]}` closes Dashboard (opened on line 24). Names declared inside that block end here.

 167 |                 width={28}
     | In `Dashboard` (src/components/Dashboard.jsx): `width={28}` closes Dashboard (opened on line 24). Names declared inside that block end here.

 168 |               />
     | In `Dashboard` (src/components/Dashboard.jsx): statement `/>`. It runs when Dashboard runs, in order, before the next line of the same function.

 169 |               <Tooltip
     | In `Dashboard` (src/components/Dashboard.jsx): JSX `<Tooltip>`. React will create this node when the parent renders. Source: `<Tooltip`

 170 |                 contentStyle={tooltipStyle}
     | In `Dashboard` (src/components/Dashboard.jsx): `contentStyle={tooltipStyle}` closes Dashboard (opened on line 24). Names declared inside that block end here.

 171 |                 cursor={{ fill: "var(--violet-dim)" }}
     | In `Dashboard` (src/components/Dashboard.jsx): `cursor={{ fill: "var(--violet-dim)" }}` closes Dashboard (opened on line 24). Names declared inside that block end here.

 172 |               />
     | In `Dashboard` (src/components/Dashboard.jsx): statement `/>`. It runs when Dashboard runs, in order, before the next line of the same function.

 173 |               <ReferenceLine y={0} stroke="var(--border)" />
     | In `Dashboard` (src/components/Dashboard.jsx): JSX `<ReferenceLine>`. React will create this node when the parent renders. Source: `<ReferenceLine y={0} stroke="var(--border)" />`

 174 |               <Bar dataKey="tasks" fill="var(--violet)" radius={[4, 4, 0, 0]} name="Tasks" />
     | In `Dashboard` (src/components/Dashboard.jsx): JSX `<Bar>`. React will create this node when the parent renders. Source: `<Bar dataKey="tasks" fill="var(--violet)" radius={[4, 4, 0, 0]} name="Tasks" />`

 175 |             </BarChart>
     | In `Dashboard` (src/components/Dashboard.jsx): JSX `<BarChart>`. This closes that element. Source: `</BarChart>`

 176 |           </ResponsiveContainer>
     | In `Dashboard` (src/components/Dashboard.jsx): JSX `<ResponsiveContainer>`. This closes that element. Source: `</ResponsiveContainer>`

 177 |         ) : (
     | In `Dashboard` (src/components/Dashboard.jsx): statement `) : (`. It runs when Dashboard runs, in order, before the next line of the same function.

 178 |           <div className="empty-state" style={{ padding: "32px 20px" }}>
     | In `Dashboard` (src/components/Dashboard.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="empty-state" style={{ padding: "32px 20px" }}>`

 179 |             <div className="empty-state-icon">📊</div>
     | In `Dashboard` (src/components/Dashboard.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="empty-state-icon">📊</div>`

 180 |             <div className="empty-state-title">No data yet this week</div>
     | In `Dashboard` (src/components/Dashboard.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="empty-state-title">No data yet this week</div>`

 181 |             <div className="empty-state-body">
     | In `Dashboard` (src/components/Dashboard.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="empty-state-body">`

 182 |               Complete tasks and focus sessions to see your daily progress here.
     | In `Dashboard` (src/components/Dashboard.jsx): statement `Complete tasks and focus sessions to see your daily progress here.`. It runs when Dashboard runs, in order, before the next line of the same function.

 183 |             </div>
     | In `Dashboard` (src/components/Dashboard.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 184 |           </div>
     | In `Dashboard` (src/components/Dashboard.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 185 |         )}
     | In `Dashboard` (src/components/Dashboard.jsx): `)}` closes Dashboard (opened on line 24). Names declared inside that block end here.

 186 |       </div>
     | In `Dashboard` (src/components/Dashboard.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 187 | 
     | Blank line in `src/components/Dashboard.jsx` (the progress charts), inside Dashboard. The parser skips it. It separates the previous statement from the next so the function is readable.

 188 |       {/* ── Monthly trend ────────────────────────────────────── */}
     | In `Dashboard` (src/components/Dashboard.jsx): `{/* ── Monthly trend ────────────────────────────────────── */}` closes Dashboard (opened on line 24). Names declared inside that block end here.

 189 |       <div className="card">
     | In `Dashboard` (src/components/Dashboard.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="card">`

 190 |         <div className="chart-header">
     | In `Dashboard` (src/components/Dashboard.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="chart-header">`

 191 |           <div className="card-title" style={{ margin: 0 }}>30-Day Trend</div>
     | In `Dashboard` (src/components/Dashboard.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="card-title" style={{ margin: 0 }}>30-Day Trend</div>`

 192 |           <ChartLegend items={[
     | In `Dashboard` (src/components/Dashboard.jsx): JSX `<ChartLegend>`. React will create this node when the parent renders. Source: `<ChartLegend items={[`

 193 |             { label: "Tasks", color: "var(--violet-light)" },
     | In `Dashboard` (src/components/Dashboard.jsx): `{ label: "Tasks", color: "var(--violet-light)" },` closes Dashboard (opened on line 24). Names declared inside that block end here.

 194 |             { label: "Focus mins", color: "var(--green)" },
     | In `Dashboard` (src/components/Dashboard.jsx): `{ label: "Focus mins", color: "var(--green)" },` closes Dashboard (opened on line 24). Names declared inside that block end here.

 195 |           ]} />
     | In `Dashboard` (src/components/Dashboard.jsx): `]} />` closes Dashboard (opened on line 24). Names declared inside that block end here.

 196 |         </div>
     | In `Dashboard` (src/components/Dashboard.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 197 |         {hasMonthlyData ? (
     | In `Dashboard` (src/components/Dashboard.jsx): statement `{hasMonthlyData ? (`. It runs when Dashboard runs, in order, before the next line of the same function.

 198 |           <ResponsiveContainer width="100%" height={220}>
     | In `Dashboard` (src/components/Dashboard.jsx): JSX `<ResponsiveContainer>`. React will create this node when the parent renders. Source: `<ResponsiveContainer width="100%" height={220}>`

 199 |             <LineChart data={monthly}>
     | In `Dashboard` (src/components/Dashboard.jsx): JSX `<LineChart>`. React will create this node when the parent renders. Source: `<LineChart data={monthly}>`

 200 |               <XAxis
     | In `Dashboard` (src/components/Dashboard.jsx): JSX `<XAxis>`. React will create this node when the parent renders. Source: `<XAxis`

 201 |                 dataKey="date"
     | In `Dashboard` (src/components/Dashboard.jsx): statement `dataKey="date"`. It runs when Dashboard runs, in order, before the next line of the same function.

 202 |                 tick={{ fill: "var(--muted)", fontSize: 11 }}
     | In `Dashboard` (src/components/Dashboard.jsx): `tick={{ fill: "var(--muted)", fontSize: 11 }}` closes Dashboard (opened on line 24). Names declared inside that block end here.

 203 |                 axisLine={false}
     | In `Dashboard` (src/components/Dashboard.jsx): `axisLine={false}` closes Dashboard (opened on line 24). Names declared inside that block end here.

 204 |                 tickLine={false}
     | In `Dashboard` (src/components/Dashboard.jsx): `tickLine={false}` closes Dashboard (opened on line 24). Names declared inside that block end here.

 205 |                 interval={4}
     | In `Dashboard` (src/components/Dashboard.jsx): `interval={4}` closes Dashboard (opened on line 24). Names declared inside that block end here.

 206 |               />
     | In `Dashboard` (src/components/Dashboard.jsx): statement `/>`. It runs when Dashboard runs, in order, before the next line of the same function.

 207 |               <YAxis
     | In `Dashboard` (src/components/Dashboard.jsx): JSX `<YAxis>`. React will create this node when the parent renders. Source: `<YAxis`

 208 |                 tick={{ fill: "var(--muted)", fontSize: 12 }}
     | In `Dashboard` (src/components/Dashboard.jsx): `tick={{ fill: "var(--muted)", fontSize: 12 }}` closes Dashboard (opened on line 24). Names declared inside that block end here.

 209 |                 axisLine={false}
     | In `Dashboard` (src/components/Dashboard.jsx): `axisLine={false}` closes Dashboard (opened on line 24). Names declared inside that block end here.

 210 |                 tickLine={false}
     | In `Dashboard` (src/components/Dashboard.jsx): `tickLine={false}` closes Dashboard (opened on line 24). Names declared inside that block end here.

 211 |                 allowDecimals={false}
     | In `Dashboard` (src/components/Dashboard.jsx): `allowDecimals={false}` closes Dashboard (opened on line 24). Names declared inside that block end here.

 212 |                 domain={[0, "auto"]}
     | In `Dashboard` (src/components/Dashboard.jsx): `domain={[0, "auto"]}` closes Dashboard (opened on line 24). Names declared inside that block end here.

 213 |                 width={28}
     | In `Dashboard` (src/components/Dashboard.jsx): `width={28}` closes Dashboard (opened on line 24). Names declared inside that block end here.

 214 |               />
     | In `Dashboard` (src/components/Dashboard.jsx): statement `/>`. It runs when Dashboard runs, in order, before the next line of the same function.

 215 |               <CartesianGrid stroke="var(--border)" strokeDasharray="4 4" />
     | In `Dashboard` (src/components/Dashboard.jsx): JSX `<CartesianGrid>`. React will create this node when the parent renders. Source: `<CartesianGrid stroke="var(--border)" strokeDasharray="4 4" />`

 216 |               <Tooltip contentStyle={tooltipStyle} />
     | In `Dashboard` (src/components/Dashboard.jsx): JSX `<Tooltip>`. React will create this node when the parent renders. Source: `<Tooltip contentStyle={tooltipStyle} />`

 217 |               <Line
     | In `Dashboard` (src/components/Dashboard.jsx): JSX `<Line>`. React will create this node when the parent renders. Source: `<Line`

 218 |                 type="monotone"
     | In `Dashboard` (src/components/Dashboard.jsx): statement `type="monotone"`. It runs when Dashboard runs, in order, before the next line of the same function.

 219 |                 dataKey="tasks"
     | In `Dashboard` (src/components/Dashboard.jsx): statement `dataKey="tasks"`. It runs when Dashboard runs, in order, before the next line of the same function.

 220 |                 stroke="var(--violet-light)"
     | In `Dashboard` (src/components/Dashboard.jsx): statement `stroke="var(--violet-light)"`. It runs when Dashboard runs, in order, before the next line of the same function.

 221 |                 strokeWidth={2}
     | In `Dashboard` (src/components/Dashboard.jsx): `strokeWidth={2}` closes Dashboard (opened on line 24). Names declared inside that block end here.

 222 |                 dot={false}
     | In `Dashboard` (src/components/Dashboard.jsx): `dot={false}` closes Dashboard (opened on line 24). Names declared inside that block end here.

 223 |                 name="Tasks"
     | In `Dashboard` (src/components/Dashboard.jsx): statement `name="Tasks"`. It runs when Dashboard runs, in order, before the next line of the same function.

 224 |               />
     | In `Dashboard` (src/components/Dashboard.jsx): statement `/>`. It runs when Dashboard runs, in order, before the next line of the same function.

 225 |               <Line
     | In `Dashboard` (src/components/Dashboard.jsx): JSX `<Line>`. React will create this node when the parent renders. Source: `<Line`

 226 |                 type="monotone"
     | In `Dashboard` (src/components/Dashboard.jsx): statement `type="monotone"`. It runs when Dashboard runs, in order, before the next line of the same function.

 227 |                 dataKey="minutes"
     | In `Dashboard` (src/components/Dashboard.jsx): statement `dataKey="minutes"`. It runs when Dashboard runs, in order, before the next line of the same function.

 228 |                 stroke="var(--green)"
     | In `Dashboard` (src/components/Dashboard.jsx): statement `stroke="var(--green)"`. It runs when Dashboard runs, in order, before the next line of the same function.

 229 |                 strokeWidth={2}
     | In `Dashboard` (src/components/Dashboard.jsx): `strokeWidth={2}` closes Dashboard (opened on line 24). Names declared inside that block end here.

 230 |                 dot={false}
     | In `Dashboard` (src/components/Dashboard.jsx): `dot={false}` closes Dashboard (opened on line 24). Names declared inside that block end here.

 231 |                 name="Focus mins"
     | In `Dashboard` (src/components/Dashboard.jsx): statement `name="Focus mins"`. It runs when Dashboard runs, in order, before the next line of the same function.

 232 |               />
     | In `Dashboard` (src/components/Dashboard.jsx): statement `/>`. It runs when Dashboard runs, in order, before the next line of the same function.

 233 |             </LineChart>
     | In `Dashboard` (src/components/Dashboard.jsx): JSX `<LineChart>`. This closes that element. Source: `</LineChart>`

 234 |           </ResponsiveContainer>
     | In `Dashboard` (src/components/Dashboard.jsx): JSX `<ResponsiveContainer>`. This closes that element. Source: `</ResponsiveContainer>`

 235 |         ) : (
     | In `Dashboard` (src/components/Dashboard.jsx): statement `) : (`. It runs when Dashboard runs, in order, before the next line of the same function.

 236 |           <div className="empty-state" style={{ padding: "32px 20px" }}>
     | In `Dashboard` (src/components/Dashboard.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="empty-state" style={{ padding: "32px 20px" }}>`

 237 |             <div className="empty-state-icon">📈</div>
     | In `Dashboard` (src/components/Dashboard.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="empty-state-icon">📈</div>`

 238 |             <div className="empty-state-title">Your trend will appear here</div>
     | In `Dashboard` (src/components/Dashboard.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="empty-state-title">Your trend will appear here</div>`

 239 |             <div className="empty-state-body">
     | In `Dashboard` (src/components/Dashboard.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="empty-state-body">`

 240 |               Start completing tasks and running focus sessions — your 30-day trend builds up over time.
     | In `Dashboard` (src/components/Dashboard.jsx): statement `Start completing tasks and running focus sessions — your 30-day trend builds up over time.`. It runs when Dashboard runs, in order, before the next line of the same function.

 241 |             </div>
     | In `Dashboard` (src/components/Dashboard.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 242 |           </div>
     | In `Dashboard` (src/components/Dashboard.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 243 |         )}
     | In `Dashboard` (src/components/Dashboard.jsx): `)}` closes Dashboard (opened on line 24). Names declared inside that block end here.

 244 |       </div>
     | In `Dashboard` (src/components/Dashboard.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 245 |     </div>
     | In `Dashboard` (src/components/Dashboard.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 246 |   );
     | In `Dashboard` (src/components/Dashboard.jsx): statement `);`. It runs when Dashboard runs, in order, before the next line of the same function.

 247 | }
     | In `Dashboard` (src/components/Dashboard.jsx): `}` closes Dashboard (opened on line 24). Names declared inside that block end here.

