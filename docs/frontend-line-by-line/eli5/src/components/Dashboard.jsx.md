# `src/components/Dashboard.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import { useEffect, useState } from "react";
     | Borrows React so this file can remember things and draw the screen.

   2 | import api from "../services/api";
     | This file borrows a tool another file already made.

   3 | import {
     | This file borrows a tool another file already made.

   4 |   BarChart, Bar,
     | Inside the top of the file, this line runs as written: BarChart, Bar,. It happens in order, after the line above it and before the line below it.

   5 |   LineChart, Line,
     | Inside the top of the file, this line runs as written: LineChart, Line,. It happens in order, after the line above it and before the line below it.

   6 |   XAxis, YAxis,
     | Inside the top of the file, this line runs as written: XAxis, YAxis,. It happens in order, after the line above it and before the line below it.

   7 |   Tooltip, CartesianGrid,
     | Inside the top of the file, this line runs as written: Tooltip, CartesianGrid,. It happens in order, after the line above it and before the line below it.

   8 |   ResponsiveContainer, ReferenceLine,
     | Inside the top of the file, this line runs as written: ResponsiveContainer, ReferenceLine,. It happens in order, after the line above it and before the line below it.

   9 | } from "recharts";
     | This ends import { (opened on line 3).

  10 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  11 | function ChartLegend({ items }) {
     | This starts ChartLegend. Colored swatches. It does not read chart data.

  12 |   return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  13 |     <div className="chart-legend">
     | This draws one piece of the page while ChartLegend is showing.

  14 |       {items.map(({ label, color }) => (
     | This ends ChartLegend (opened on line 11).

  15 |         <div key={label} className="chart-legend-item">
     | This draws one piece of the page while ChartLegend is showing.

  16 |           <div className="chart-legend-swatch" style={{ background: color }} />
     | This draws one piece of the page while ChartLegend is showing.

  17 |           <span>{label}</span>
     | This draws one piece of the page while ChartLegend is showing.

  18 |         </div>
     | This ends a drawing that ChartLegend started just above.

  19 |       ))}
     | This ends ChartLegend (opened on line 11).

  20 |     </div>
     | This ends a drawing that ChartLegend started just above.

  21 |   );
     | This closes a box of instructions that opened above.

  22 | }
     | This ends ChartLegend (opened on line 11).

  23 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  24 | export default function Dashboard() {
     | This starts Dashboard. Four tiles plus a 7-day bar chart and a 30-day line chart from /stats/daily, /weekly, and /monthly.

  25 |   const [daily, setDaily] = useState({ tasksCompleted: 0, totalSessionMins: 0 });
     | Today's tasksCompleted and totalSessionMins from GET /stats/daily.

  26 |   const [weekly, setWeekly] = useState([]);
     | This gives a short name to a value so the rest of Dashboard can use it.

  27 |   const [monthly, setMonthly] = useState([]);
     | This gives a short name to a value so the rest of Dashboard can use it.

  28 |   const [streak, setStreak] = useState(0);
     | How many days back from today, up to 7, have a completed task. Today may be empty; the count stops at the first gap after today.

  29 |   const [totalCompleted, setTotalCompleted] = useState(0);
     | This gives a short name to a value so the rest of Dashboard can use it.

  30 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  31 |   useEffect(() => { load(); }, []);
     | This is an extra job that happens after the picture is drawn.

  32 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  33 |   async function load() {
     | This starts load. GET /tasks and, on the task page, keeps only tasks that are not completed. Calendar and the deadline page keep a wider set.

  34 |     try {
     | Inside load, this line runs as written: try {. It happens in order, after the line above it and before the line below it.

  35 |       const [d, w, m] = await Promise.all([
     | This gives a short name to a value so the rest of load can use it.

  36 |         api.get("/stats/daily"),
     | This asks the server (the office that keeps tasks and accounts) for something, or sends it something.

  37 |         api.get("/stats/weekly"),
     | This asks the server (the office that keeps tasks and accounts) for something, or sends it something.

  38 |         api.get("/stats/monthly"),
     | This asks the server (the office that keeps tasks and accounts) for something, or sends it something.

  39 |       ]);
     | Inside load, this line runs as written: ]);. It happens in order, after the line above it and before the line below it.

  40 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  41 |       setDaily(d);
     | Inside load, this line runs as written: setDaily(d);. It happens in order, after the line above it and before the line below it.

  42 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  43 |       const weekData = processWeekly(w.tasks || [], w.sessions || []);
     | This gives a short name to a value so the rest of load can use it.

  44 |       setWeekly(weekData);
     | Inside load, this line runs as written: setWeekly(weekData);. It happens in order, after the line above it and before the line below it.

  45 |       setMonthly(processMonthly(m.tasks || [], m.sessions || []));
     | Inside load, this line runs as written: setMonthly(processMonthly(m.tasks || [], m.sessions || []));. It happens in order, after the line above it and before the line below it.

  46 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  47 |       // Streak: consecutive days with at least 1 completed task
     | A note written for people. The app does not run it.

  48 |       const byDay = {};
     | This gives a short name to a value so the rest of load can use it.

  49 |       (w.tasks || []).forEach((t) => {
     | Inside load, this line runs as written: (w.tasks || []).forEach((t) => {. It happens in order, after the line above it and before the line below it.

  50 |         const key = t.completedAt?.split("T")[0];
     | This gives a short name to a value so the rest of load can use it.

  51 |         if (key) byDay[key] = true;
     | This asks a yes-or-no question. The next bit runs only on yes.

  52 |       });
     | This ends (w.tasks || []).forEach((t) => { (opened on line 49).

  53 |       let s = 0;
     | This gives a short name to a value so the rest of load can use it.

  54 |       for (let i = 0; i < 7; i++) {
     | Inside load, this line runs as written: for (let i = 0; i < 7; i++) {. It happens in order, after the line above it and before the line below it.

  55 |         const dt = new Date();
     | This gives a short name to a value so the rest of load can use it.

  56 |         dt.setDate(dt.getDate() - i);
     | Inside load, this line runs as written: dt.setDate(dt.getDate() - i);. It happens in order, after the line above it and before the line below it.

  57 |         const key = dt.toISOString().split("T")[0];
     | This gives a short name to a value so the rest of load can use it.

  58 |         if (byDay[key]) s++;
     | This asks a yes-or-no question. The next bit runs only on yes.

  59 |         else if (i > 0) break;
     | Inside load, this line runs as written: else if (i > 0) break;. It happens in order, after the line above it and before the line below it.

  60 |       }
     | This ends for (let i = 0; i < 7; i++) { (opened on line 54).

  61 |       setStreak(s);
     | Inside load, this line runs as written: setStreak(s);. It happens in order, after the line above it and before the line below it.

  62 |       setTotalCompleted(weekData.reduce((acc, d) => acc + d.tasks, 0));
     | Inside load, this line runs as written: setTotalCompleted(weekData.reduce((acc, d) => acc + d.tasks, 0));. It happens in order, after the line above it and before the line below it.

  63 |     } catch {}
     | This ends try { (opened on line 34).

  64 |   }
     | This ends load (opened on line 33).

  65 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  66 |   function processWeekly(tasks, sessions) {
     | This starts processWeekly. Builds seven day buckets ending today and drops completed tasks and session minutes into them.

  67 |     const map = {};
     | This gives a short name to a value so the rest of processWeekly can use it.

  68 |     for (let i = 6; i >= 0; i--) {
     | Inside processWeekly, this line runs as written: for (let i = 6; i >= 0; i--) {. It happens in order, after the line above it and before the line below it.

  69 |       const d = new Date();
     | This gives a short name to a value so the rest of processWeekly can use it.

  70 |       d.setDate(d.getDate() - i);
     | Inside processWeekly, this line runs as written: d.setDate(d.getDate() - i);. It happens in order, after the line above it and before the line below it.

  71 |       const key = d.toISOString().split("T")[0];
     | This gives a short name to a value so the rest of processWeekly can use it.

  72 |       const label = d.toLocaleDateString("en", { weekday: "short" });
     | This gives a short name to a value so the rest of processWeekly can use it.

  73 |       map[key] = { date: label, tasks: 0, minutes: 0 };
     | This ends for (let i = 6; i >= 0; i--) { (opened on line 68).

  74 |     }
     | This ends for (let i = 6; i >= 0; i--) { (opened on line 68).

  75 |     tasks.forEach((t) => {
     | Inside processWeekly, this line runs as written: tasks.forEach((t) => {. It happens in order, after the line above it and before the line below it.

  76 |       const key = t.completedAt?.split("T")[0];
     | This gives a short name to a value so the rest of processWeekly can use it.

  77 |       if (map[key]) map[key].tasks++;
     | This asks a yes-or-no question. The next bit runs only on yes.

  78 |     });
     | This ends tasks.forEach((t) => { (opened on line 75).

  79 |     sessions.forEach((s) => {
     | Inside processWeekly, this line runs as written: sessions.forEach((s) => {. It happens in order, after the line above it and before the line below it.

  80 |       const key = s.completedAt?.split("T")[0];
     | This gives a short name to a value so the rest of processWeekly can use it.

  81 |       if (map[key]) map[key].minutes += s.durationMins || 0;
     | This asks a yes-or-no question. The next bit runs only on yes.

  82 |     });
     | This ends sessions.forEach((s) => { (opened on line 79).

  83 |     return Object.values(map);
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  84 |   }
     | This ends processWeekly (opened on line 66).

  85 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  86 |   function processMonthly(tasks, sessions) {
     | This starts processMonthly. Same for 30 days. Labels are M/D.

  87 |     const map = {};
     | This gives a short name to a value so the rest of processMonthly can use it.

  88 |     for (let i = 29; i >= 0; i--) {
     | Inside processMonthly, this line runs as written: for (let i = 29; i >= 0; i--) {. It happens in order, after the line above it and before the line below it.

  89 |       const d = new Date();
     | This gives a short name to a value so the rest of processMonthly can use it.

  90 |       d.setDate(d.getDate() - i);
     | Inside processMonthly, this line runs as written: d.setDate(d.getDate() - i);. It happens in order, after the line above it and before the line below it.

  91 |       const key = d.toISOString().split("T")[0];
     | This gives a short name to a value so the rest of processMonthly can use it.

  92 |       const label = `${d.getMonth() + 1}/${d.getDate()}`;
     | This gives a short name to a value so the rest of processMonthly can use it.

  93 |       map[key] = { date: label, tasks: 0, minutes: 0 };
     | This ends for (let i = 29; i >= 0; i--) { (opened on line 88).

  94 |     }
     | This ends for (let i = 29; i >= 0; i--) { (opened on line 88).

  95 |     tasks.forEach((t) => {
     | Inside processMonthly, this line runs as written: tasks.forEach((t) => {. It happens in order, after the line above it and before the line below it.

  96 |       const key = t.completedAt?.split("T")[0];
     | This gives a short name to a value so the rest of processMonthly can use it.

  97 |       if (map[key]) map[key].tasks++;
     | This asks a yes-or-no question. The next bit runs only on yes.

  98 |     });
     | This ends tasks.forEach((t) => { (opened on line 95).

  99 |     sessions.forEach((s) => {
     | Inside processMonthly, this line runs as written: sessions.forEach((s) => {. It happens in order, after the line above it and before the line below it.

 100 |       const key = s.completedAt?.split("T")[0];
     | This gives a short name to a value so the rest of processMonthly can use it.

 101 |       if (map[key]) map[key].minutes += s.durationMins || 0;
     | This asks a yes-or-no question. The next bit runs only on yes.

 102 |     });
     | This ends sessions.forEach((s) => { (opened on line 99).

 103 |     return Object.values(map);
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

 104 |   }
     | This ends processMonthly (opened on line 86).

 105 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 106 |   const tooltipStyle = {
     | This gives a short name to a value so the rest of Dashboard can use it.

 107 |     backgroundColor: "var(--card)",
     | Inside Dashboard, this line runs as written: backgroundColor: "var(--card)",. It happens in order, after the line above it and before the line below it.

 108 |     border: "1px solid var(--border)",
     | Inside Dashboard, this line runs as written: border: "1px solid var(--border)",. It happens in order, after the line above it and before the line below it.

 109 |     borderRadius: 8,
     | Inside Dashboard, this line runs as written: borderRadius: 8,. It happens in order, after the line above it and before the line below it.

 110 |     color: "var(--text)",
     | Inside Dashboard, this line runs as written: color: "var(--text)",. It happens in order, after the line above it and before the line below it.

 111 |     fontSize: 13,
     | Inside Dashboard, this line runs as written: fontSize: 13,. It happens in order, after the line above it and before the line below it.

 112 |   };
     | This ends const tooltipStyle = { (opened on line 106).

 113 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 114 |   const hasWeeklyData = weekly.some((d) => d.tasks > 0 || d.minutes > 0);
     | This gives a short name to a value so the rest of Dashboard can use it.

 115 |   const hasMonthlyData = monthly.some((d) => d.tasks > 0 || d.minutes > 0);
     | This gives a short name to a value so the rest of Dashboard can use it.

 116 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 117 |   return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

 118 |     <div>
     | This draws one piece of the page while Dashboard is showing.

 119 |       <h1 className="page-title">Stats</h1>
     | This draws one piece of the page while Dashboard is showing.

 120 |       <p className="page-subtitle">Track focus, tasks, and streaks over time</p>
     | This draws one piece of the page while Dashboard is showing.

 121 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 122 |       {/* ── Top stat tiles ─────────────────────────────────── */}
     | This ends Dashboard (opened on line 24).

 123 |       <div className="grid-4 mb-4">
     | This draws one piece of the page while Dashboard is showing.

 124 |         <div className="stat-tile">
     | This draws one piece of the page while Dashboard is showing.

 125 |           <div className="stat-value stat-green">{daily.tasksCompleted ?? 0}</div>
     | This draws one piece of the page while Dashboard is showing.

 126 |           <div className="stat-label">Tasks today</div>
     | This draws one piece of the page while Dashboard is showing.

 127 |         </div>
     | This ends a drawing that Dashboard started just above.

 128 |         <div className="stat-tile">
     | This draws one piece of the page while Dashboard is showing.

 129 |           <div className="stat-value stat-violet">{daily.totalSessionMins ?? 0}</div>
     | This draws one piece of the page while Dashboard is showing.

 130 |           <div className="stat-label">Focus mins today</div>
     | This draws one piece of the page while Dashboard is showing.

 131 |         </div>
     | This ends a drawing that Dashboard started just above.

 132 |         <div className="stat-tile">
     | This draws one piece of the page while Dashboard is showing.

 133 |           <div className="stat-value stat-amber">
     | This draws one piece of the page while Dashboard is showing.

 134 |             {streak > 0 ? `${streak}🔥` : "—"}
     | This ends Dashboard (opened on line 24).

 135 |           </div>
     | This ends a drawing that Dashboard started just above.

 136 |           <div className="stat-label">Day streak</div>
     | This draws one piece of the page while Dashboard is showing.

 137 |         </div>
     | This ends a drawing that Dashboard started just above.

 138 |         <div className="stat-tile">
     | This draws one piece of the page while Dashboard is showing.

 139 |           <div className="stat-value" style={{ color: "var(--text)" }}>
     | This draws one piece of the page while Dashboard is showing.

 140 |             {totalCompleted || "—"}
     | This ends Dashboard (opened on line 24).

 141 |           </div>
     | This ends a drawing that Dashboard started just above.

 142 |           <div className="stat-label">Tasks this week</div>
     | This draws one piece of the page while Dashboard is showing.

 143 |         </div>
     | This ends a drawing that Dashboard started just above.

 144 |       </div>
     | This ends a drawing that Dashboard started just above.

 145 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 146 |       {/* ── Weekly bar chart ────────────────────────────────── */}
     | This ends Dashboard (opened on line 24).

 147 |       <div className="card mb-4">
     | This draws one piece of the page while Dashboard is showing.

 148 |         <div className="chart-header">
     | This draws one piece of the page while Dashboard is showing.

 149 |           <div className="card-title" style={{ margin: 0 }}>Tasks Completed — Last 7 Days</div>
     | This draws one piece of the page while Dashboard is showing.

 150 |           <ChartLegend items={[{ label: "Tasks", color: "var(--violet)" }]} />
     | This draws one piece of the page while Dashboard is showing.

 151 |         </div>
     | This ends a drawing that Dashboard started just above.

 152 |         {hasWeeklyData ? (
     | Inside Dashboard, this line runs as written: {hasWeeklyData ? (. It happens in order, after the line above it and before the line below it.

 153 |           <ResponsiveContainer width="100%" height={220}>
     | This draws one piece of the page while Dashboard is showing.

 154 |             <BarChart data={weekly} barSize={28}>
     | This draws one piece of the page while Dashboard is showing.

 155 |               <XAxis
     | This draws one piece of the page while Dashboard is showing.

 156 |                 dataKey="date"
     | Inside Dashboard, this line runs as written: dataKey="date". It happens in order, after the line above it and before the line below it.

 157 |                 tick={{ fill: "var(--muted)", fontSize: 12 }}
     | This ends Dashboard (opened on line 24).

 158 |                 axisLine={false}
     | This ends Dashboard (opened on line 24).

 159 |                 tickLine={false}
     | This ends Dashboard (opened on line 24).

 160 |               />
     | This closes a box of instructions that opened above.

 161 |               <YAxis
     | This draws one piece of the page while Dashboard is showing.

 162 |                 tick={{ fill: "var(--muted)", fontSize: 12 }}
     | This ends Dashboard (opened on line 24).

 163 |                 axisLine={false}
     | This ends Dashboard (opened on line 24).

 164 |                 tickLine={false}
     | This ends Dashboard (opened on line 24).

 165 |                 allowDecimals={false}
     | This ends Dashboard (opened on line 24).

 166 |                 domain={[0, "auto"]}
     | This ends Dashboard (opened on line 24).

 167 |                 width={28}
     | This ends Dashboard (opened on line 24).

 168 |               />
     | This closes a box of instructions that opened above.

 169 |               <Tooltip
     | This draws one piece of the page while Dashboard is showing.

 170 |                 contentStyle={tooltipStyle}
     | This ends Dashboard (opened on line 24).

 171 |                 cursor={{ fill: "var(--violet-dim)" }}
     | This ends Dashboard (opened on line 24).

 172 |               />
     | This closes a box of instructions that opened above.

 173 |               <ReferenceLine y={0} stroke="var(--border)" />
     | This draws one piece of the page while Dashboard is showing.

 174 |               <Bar dataKey="tasks" fill="var(--violet)" radius={[4, 4, 0, 0]} name="Tasks" />
     | This draws one piece of the page while Dashboard is showing.

 175 |             </BarChart>
     | This ends a drawing that Dashboard started just above.

 176 |           </ResponsiveContainer>
     | This ends a drawing that Dashboard started just above.

 177 |         ) : (
     | This closes a box of instructions that opened above.

 178 |           <div className="empty-state" style={{ padding: "32px 20px" }}>
     | This draws one piece of the page while Dashboard is showing.

 179 |             <div className="empty-state-icon">📊</div>
     | This draws one piece of the page while Dashboard is showing.

 180 |             <div className="empty-state-title">No data yet this week</div>
     | This draws one piece of the page while Dashboard is showing.

 181 |             <div className="empty-state-body">
     | This draws one piece of the page while Dashboard is showing.

 182 |               Complete tasks and focus sessions to see your daily progress here.
     | Inside Dashboard, this line runs as written: Complete tasks and focus sessions to see your daily progress here.. It happens in order, after the line above it and before the line below it.

 183 |             </div>
     | This ends a drawing that Dashboard started just above.

 184 |           </div>
     | This ends a drawing that Dashboard started just above.

 185 |         )}
     | This ends Dashboard (opened on line 24).

 186 |       </div>
     | This ends a drawing that Dashboard started just above.

 187 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 188 |       {/* ── Monthly trend ────────────────────────────────────── */}
     | This ends Dashboard (opened on line 24).

 189 |       <div className="card">
     | This draws one piece of the page while Dashboard is showing.

 190 |         <div className="chart-header">
     | This draws one piece of the page while Dashboard is showing.

 191 |           <div className="card-title" style={{ margin: 0 }}>30-Day Trend</div>
     | This draws one piece of the page while Dashboard is showing.

 192 |           <ChartLegend items={[
     | This draws one piece of the page while Dashboard is showing.

 193 |             { label: "Tasks", color: "var(--violet-light)" },
     | This ends Dashboard (opened on line 24).

 194 |             { label: "Focus mins", color: "var(--green)" },
     | This ends Dashboard (opened on line 24).

 195 |           ]} />
     | This ends Dashboard (opened on line 24).

 196 |         </div>
     | This ends a drawing that Dashboard started just above.

 197 |         {hasMonthlyData ? (
     | Inside Dashboard, this line runs as written: {hasMonthlyData ? (. It happens in order, after the line above it and before the line below it.

 198 |           <ResponsiveContainer width="100%" height={220}>
     | This draws one piece of the page while Dashboard is showing.

 199 |             <LineChart data={monthly}>
     | This draws one piece of the page while Dashboard is showing.

 200 |               <XAxis
     | This draws one piece of the page while Dashboard is showing.

 201 |                 dataKey="date"
     | Inside Dashboard, this line runs as written: dataKey="date". It happens in order, after the line above it and before the line below it.

 202 |                 tick={{ fill: "var(--muted)", fontSize: 11 }}
     | This ends Dashboard (opened on line 24).

 203 |                 axisLine={false}
     | This ends Dashboard (opened on line 24).

 204 |                 tickLine={false}
     | This ends Dashboard (opened on line 24).

 205 |                 interval={4}
     | This ends Dashboard (opened on line 24).

 206 |               />
     | This closes a box of instructions that opened above.

 207 |               <YAxis
     | This draws one piece of the page while Dashboard is showing.

 208 |                 tick={{ fill: "var(--muted)", fontSize: 12 }}
     | This ends Dashboard (opened on line 24).

 209 |                 axisLine={false}
     | This ends Dashboard (opened on line 24).

 210 |                 tickLine={false}
     | This ends Dashboard (opened on line 24).

 211 |                 allowDecimals={false}
     | This ends Dashboard (opened on line 24).

 212 |                 domain={[0, "auto"]}
     | This ends Dashboard (opened on line 24).

 213 |                 width={28}
     | This ends Dashboard (opened on line 24).

 214 |               />
     | This closes a box of instructions that opened above.

 215 |               <CartesianGrid stroke="var(--border)" strokeDasharray="4 4" />
     | This draws one piece of the page while Dashboard is showing.

 216 |               <Tooltip contentStyle={tooltipStyle} />
     | This draws one piece of the page while Dashboard is showing.

 217 |               <Line
     | This draws one piece of the page while Dashboard is showing.

 218 |                 type="monotone"
     | Inside Dashboard, this line runs as written: type="monotone". It happens in order, after the line above it and before the line below it.

 219 |                 dataKey="tasks"
     | Inside Dashboard, this line runs as written: dataKey="tasks". It happens in order, after the line above it and before the line below it.

 220 |                 stroke="var(--violet-light)"
     | Inside Dashboard, this line runs as written: stroke="var(--violet-light)". It happens in order, after the line above it and before the line below it.

 221 |                 strokeWidth={2}
     | This ends Dashboard (opened on line 24).

 222 |                 dot={false}
     | This ends Dashboard (opened on line 24).

 223 |                 name="Tasks"
     | Inside Dashboard, this line runs as written: name="Tasks". It happens in order, after the line above it and before the line below it.

 224 |               />
     | This closes a box of instructions that opened above.

 225 |               <Line
     | This draws one piece of the page while Dashboard is showing.

 226 |                 type="monotone"
     | Inside Dashboard, this line runs as written: type="monotone". It happens in order, after the line above it and before the line below it.

 227 |                 dataKey="minutes"
     | Inside Dashboard, this line runs as written: dataKey="minutes". It happens in order, after the line above it and before the line below it.

 228 |                 stroke="var(--green)"
     | Inside Dashboard, this line runs as written: stroke="var(--green)". It happens in order, after the line above it and before the line below it.

 229 |                 strokeWidth={2}
     | This ends Dashboard (opened on line 24).

 230 |                 dot={false}
     | This ends Dashboard (opened on line 24).

 231 |                 name="Focus mins"
     | Inside Dashboard, this line runs as written: name="Focus mins". It happens in order, after the line above it and before the line below it.

 232 |               />
     | This closes a box of instructions that opened above.

 233 |             </LineChart>
     | This ends a drawing that Dashboard started just above.

 234 |           </ResponsiveContainer>
     | This ends a drawing that Dashboard started just above.

 235 |         ) : (
     | This closes a box of instructions that opened above.

 236 |           <div className="empty-state" style={{ padding: "32px 20px" }}>
     | This draws one piece of the page while Dashboard is showing.

 237 |             <div className="empty-state-icon">📈</div>
     | This draws one piece of the page while Dashboard is showing.

 238 |             <div className="empty-state-title">Your trend will appear here</div>
     | This draws one piece of the page while Dashboard is showing.

 239 |             <div className="empty-state-body">
     | This draws one piece of the page while Dashboard is showing.

 240 |               Start completing tasks and running focus sessions — your 30-day trend builds up over time.
     | Inside Dashboard, this line runs as written: Start completing tasks and running focus sessions — your 30-day trend builds up over time.. It happens in order, after the line above it and before the line below it.

 241 |             </div>
     | This ends a drawing that Dashboard started just above.

 242 |           </div>
     | This ends a drawing that Dashboard started just above.

 243 |         )}
     | This ends Dashboard (opened on line 24).

 244 |       </div>
     | This ends a drawing that Dashboard started just above.

 245 |     </div>
     | This ends a drawing that Dashboard started just above.

 246 |   );
     | This closes a box of instructions that opened above.

 247 | }
     | This ends Dashboard (opened on line 24).

