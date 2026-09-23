# `src/components/focus-shield/ShieldStatusCard.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import React from "react";
     | Import for the shared status card on Today and the timer: `import React from "react";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   2 | import { Link } from "react-router-dom";
     | Import for the shared status card on Today and the timer: `import { Link } from "react-router-dom";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   3 | import { getShieldStatus } from "../../utils/focusShield";
     | Import for the shared status card on Today and the timer: `import { getShieldStatus } from "../../utils/focusShield";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   4 | 
     | Blank line in `src/components/focus-shield/ShieldStatusCard.jsx` (the shared status card on Today and the timer), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   5 | // Reusable "how is Focus Shield doing right now" card.
     | Comment inside the top of the file. Not executed. It documents the next code: Reusable "how is Focus Shield doing right now" card.

   6 | // variant="dashboard" -> compact card for the Today screen
     | Comment inside the top of the file. Not executed. It documents the next code: variant="dashboard" -> compact card for the Today screen

   7 | // variant="session"   -> panel shown inside an active Focus Session
     | Comment inside the top of the file. Not executed. It documents the next code: variant="session"   -> panel shown inside an active Focus Session

   8 | export default function ShieldStatusCard({ rules, sessionActive = false, variant = "dashboard", loading = false }) {
     | Defines `ShieldStatusCard` in the shared status card on Today and the timer. Dashboard variant shows counts. Session variant lists up to five enabled blocked sites. Both link to /blocking.

   9 |   if (loading || !rules) {
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): branch `if (loading || !rules) {`. Only one side runs.

  10 |     return (
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  11 |       <div className="card fs-status-card">
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="card fs-status-card">`

  12 |         <div className="card-title">🛡️ Focus Shield</div>
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="card-title">🛡️ Focus Shield</div>`

  13 |         <p className="text-sm text-muted">Loading shield status…</p>
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): Opens it. A paragraph. Source: `<p className="text-sm text-muted">Loading shield status…</p>`

  14 |       </div>
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  15 |     );
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): statement `);`. It runs when ShieldStatusCard runs, in order, before the next line of the same function.

  16 |   }
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): `}` closes if (loading || !rules) { (opened on line 9). Names declared inside that block end here.

  17 | 
     | Blank line in `src/components/focus-shield/ShieldStatusCard.jsx` (the shared status card on Today and the timer), inside ShieldStatusCard. The parser skips it. It separates the previous statement from the next so the function is readable.

  18 |   const status = getShieldStatus(rules, sessionActive);
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): `status` is assigned `getShieldStatus(rules, sessionActive);`. Later lines in this function read that name.

  19 |   const blockedCount = rules.blockedSites?.length || 0;
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): `blockedCount` is assigned `rules.blockedSites?.length || 0;`. Later lines in this function read that name.

  20 |   const whitelistCount = rules.whitelist?.length || 0;
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): `whitelistCount` is assigned `rules.whitelist?.length || 0;`. Later lines in this function read that name.

  21 |   const topBlocked = (rules.blockedSites || []).filter((s) => s.enabled !== false).slice(0, 5);
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): `topBlocked` is assigned `(rules.blockedSites || []).filter((s) => s.enabled !== false).slice(0, 5);`. Later lines in this function read that name.

  22 | 
     | Blank line in `src/components/focus-shield/ShieldStatusCard.jsx` (the shared status card on Today and the timer), inside ShieldStatusCard. The parser skips it. It separates the previous statement from the next so the function is readable.

  23 |   return (
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  24 |     <div className="card fs-status-card">
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="card fs-status-card">`

  25 |       <div className="fs-status-card-header">
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="fs-status-card-header">`

  26 |         <div className="card-title" style={{ marginBottom: 0 }}>🛡️ Focus Shield</div>
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="card-title" style={{ marginBottom: 0 }}>🛡️ Focus Shield</div>`

  27 |         <span className={`fs-status-pill fs-status-pill--${status.level}`}>
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): Opens it. An inline box. Source: `<span className={`fs-status-pill fs-status-pill--${status.level}`}>`

  28 |           <span className="fs-status-dot" />
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): Opens it. An inline box. Source: `<span className="fs-status-dot" />`

  29 |           {status.label}
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): `{status.label}` closes ShieldStatusCard (opened on line 8). Names declared inside that block end here.

  30 |         </span>
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): Closes it. An inline box. Source: `</span>`

  31 |       </div>
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  32 |       <p className="text-sm text-muted" style={{ marginTop: 4, marginBottom: variant === "session" ? 12 : 14 }}>
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): Opens it. A paragraph. Source: `<p className="text-sm text-muted" style={{ marginTop: 4, marginBottom: variant === "session" ? 12 : 14 }}>`

  33 |         {status.description}
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): `{status.description}` closes ShieldStatusCard (opened on line 8). Names declared inside that block end here.

  34 |       </p>
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): Closes it. A paragraph. Source: `</p>`

  35 | 
     | Blank line in `src/components/focus-shield/ShieldStatusCard.jsx` (the shared status card on Today and the timer), inside ShieldStatusCard. The parser skips it. It separates the previous statement from the next so the function is readable.

  36 |       {variant === "session" ? (
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): statement `{variant === "session" ? (`. It runs when ShieldStatusCard runs, in order, before the next line of the same function.

  37 |         blockedCount > 0 ? (
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): statement `blockedCount > 0 ? (`. It runs when ShieldStatusCard runs, in order, before the next line of the same function.

  38 |           <ul className="fs-session-site-list" aria-label="Blocked websites">
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): Opens it. A list. Source: `<ul className="fs-session-site-list" aria-label="Blocked websites">`

  39 |             {topBlocked.map((s) => (
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): iteration `{topBlocked.map((s) => (`.

  40 |               <li key={s.value}>{s.label || s.value}</li>
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): Opens it. One list item. Source: `<li key={s.value}>{s.label || s.value}</li>`

  41 |             ))}
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): `))}` closes ShieldStatusCard (opened on line 8). Names declared inside that block end here.

  42 |             {blockedCount > topBlocked.length && (
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): statement `{blockedCount > topBlocked.length && (`. It runs when ShieldStatusCard runs, in order, before the next line of the same function.

  43 |               <li className="text-muted">+{blockedCount - topBlocked.length} more</li>
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): Opens it. One list item. Source: `<li className="text-muted">+{blockedCount - topBlocked.length} more</li>`

  44 |             )}
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): `)}` closes ShieldStatusCard (opened on line 8). Names declared inside that block end here.

  45 |           </ul>
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): Closes it. A list. Source: `</ul>`

  46 |         ) : (
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): statement `) : (`. It runs when ShieldStatusCard runs, in order, before the next line of the same function.

  47 |           <p className="text-sm text-muted" style={{ marginBottom: 12 }}>
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): Opens it. A paragraph. Source: `<p className="text-sm text-muted" style={{ marginBottom: 12 }}>`

  48 |             No sites blocked yet — add some so the shield has something to guard.
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): statement `No sites blocked yet — add some so the shield has something to guard.`. It runs when ShieldStatusCard runs, in order, before the next line of the same function.

  49 |           </p>
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): Closes it. A paragraph. Source: `</p>`

  50 |         )
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): statement `)`. It runs when ShieldStatusCard runs, in order, before the next line of the same function.

  51 |       ) : (
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): statement `) : (`. It runs when ShieldStatusCard runs, in order, before the next line of the same function.

  52 |         <div className="fs-dashboard-counts">
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="fs-dashboard-counts">`

  53 |           <div>
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): Opens it. A box that groups the elements inside it. Source: `<div>`

  54 |             <div className="stat-value stat-violet" style={{ fontSize: 22 }}>{blockedCount}</div>
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="stat-value stat-violet" style={{ fontSize: 22 }}>{blockedCount}</div>`

  55 |             <div className="stat-label">Blocked</div>
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="stat-label">Blocked</div>`

  56 |           </div>
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  57 |           <div>
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): Opens it. A box that groups the elements inside it. Source: `<div>`

  58 |             <div className="stat-value stat-green" style={{ fontSize: 22 }}>{whitelistCount}</div>
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="stat-value stat-green" style={{ fontSize: 22 }}>{whitelistCount}</div>`

  59 |             <div className="stat-label">Whitelisted</div>
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="stat-label">Whitelisted</div>`

  60 |           </div>
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  61 |         </div>
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  62 |       )}
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): `)}` closes ShieldStatusCard (opened on line 8). Names declared inside that block end here.

  63 | 
     | Blank line in `src/components/focus-shield/ShieldStatusCard.jsx` (the shared status card on Today and the timer), inside ShieldStatusCard. The parser skips it. It separates the previous statement from the next so the function is readable.

  64 |       <Link to="/blocking" className="btn btn-secondary btn-sm" style={{ marginTop: 12 }}>
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): Opens it. A react-router link. Clicking it changes the URL without a full page reload. Source: `<Link to="/blocking" className="btn btn-secondary btn-sm" style={{ marginTop: 12 }}>`

  65 |         Manage Rules
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): statement `Manage Rules`. It runs when ShieldStatusCard runs, in order, before the next line of the same function.

  66 |       </Link>
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): Closes it. A react-router link. Clicking it changes the URL without a full page reload. Source: `</Link>`

  67 |     </div>
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  68 |   );
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): statement `);`. It runs when ShieldStatusCard runs, in order, before the next line of the same function.

  69 | }
     | In `ShieldStatusCard` (src/components/focus-shield/ShieldStatusCard.jsx): `}` closes ShieldStatusCard (opened on line 8). Names declared inside that block end here.

