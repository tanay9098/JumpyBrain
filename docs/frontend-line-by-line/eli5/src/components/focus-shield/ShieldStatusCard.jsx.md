# `src/components/focus-shield/ShieldStatusCard.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import React from "react";
     | Borrows React so this file can remember things and draw the screen.

   2 | import { Link } from "react-router-dom";
     | Borrows React so this file can remember things and draw the screen.

   3 | import { getShieldStatus } from "../../utils/focusShield";
     | This file borrows a tool another file already made.

   4 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   5 | // Reusable "how is Focus Shield doing right now" card.
     | A note written for people. The app does not run it.

   6 | // variant="dashboard" -> compact card for the Today screen
     | A note written for people. The app does not run it.

   7 | // variant="session"   -> panel shown inside an active Focus Session
     | A note written for people. The app does not run it.

   8 | export default function ShieldStatusCard({ rules, sessionActive = false, variant = "dashboard", loading = false }) {
     | This starts ShieldStatusCard. Dashboard variant shows counts. Session variant lists up to five enabled blocked sites. Both link to /blocking.

   9 |   if (loading || !rules) {
     | This asks a yes-or-no question. The next bit runs only on yes.

  10 |     return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  11 |       <div className="card fs-status-card">
     | This draws one piece of the page while ShieldStatusCard is showing.

  12 |         <div className="card-title">🛡️ Focus Shield</div>
     | This draws one piece of the page while ShieldStatusCard is showing.

  13 |         <p className="text-sm text-muted">Loading shield status…</p>
     | This draws one piece of the page while ShieldStatusCard is showing.

  14 |       </div>
     | This ends a drawing that ShieldStatusCard started just above.

  15 |     );
     | This closes a box of instructions that opened above.

  16 |   }
     | This ends if (loading || !rules) { (opened on line 9).

  17 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  18 |   const status = getShieldStatus(rules, sessionActive);
     | This gives a short name to a value so the rest of ShieldStatusCard can use it.

  19 |   const blockedCount = rules.blockedSites?.length || 0;
     | This gives a short name to a value so the rest of ShieldStatusCard can use it.

  20 |   const whitelistCount = rules.whitelist?.length || 0;
     | This gives a short name to a value so the rest of ShieldStatusCard can use it.

  21 |   const topBlocked = (rules.blockedSites || []).filter((s) => s.enabled !== false).slice(0, 5);
     | This gives a short name to a value so the rest of ShieldStatusCard can use it.

  22 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  23 |   return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  24 |     <div className="card fs-status-card">
     | This draws one piece of the page while ShieldStatusCard is showing.

  25 |       <div className="fs-status-card-header">
     | This draws one piece of the page while ShieldStatusCard is showing.

  26 |         <div className="card-title" style={{ marginBottom: 0 }}>🛡️ Focus Shield</div>
     | This draws one piece of the page while ShieldStatusCard is showing.

  27 |         <span className={`fs-status-pill fs-status-pill--${status.level}`}>
     | This draws one piece of the page while ShieldStatusCard is showing.

  28 |           <span className="fs-status-dot" />
     | This draws one piece of the page while ShieldStatusCard is showing.

  29 |           {status.label}
     | This ends ShieldStatusCard (opened on line 8).

  30 |         </span>
     | This ends a drawing that ShieldStatusCard started just above.

  31 |       </div>
     | This ends a drawing that ShieldStatusCard started just above.

  32 |       <p className="text-sm text-muted" style={{ marginTop: 4, marginBottom: variant === "session" ? 12 : 14 }}>
     | This draws one piece of the page while ShieldStatusCard is showing.

  33 |         {status.description}
     | This ends ShieldStatusCard (opened on line 8).

  34 |       </p>
     | This ends a drawing that ShieldStatusCard started just above.

  35 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  36 |       {variant === "session" ? (
     | Inside ShieldStatusCard, this line runs as written: {variant === "session" ? (. It happens in order, after the line above it and before the line below it.

  37 |         blockedCount > 0 ? (
     | Inside ShieldStatusCard, this line runs as written: blockedCount > 0 ? (. It happens in order, after the line above it and before the line below it.

  38 |           <ul className="fs-session-site-list" aria-label="Blocked websites">
     | This draws one piece of the page while ShieldStatusCard is showing.

  39 |             {topBlocked.map((s) => (
     | Inside ShieldStatusCard, this line runs as written: {topBlocked.map((s) => (. It happens in order, after the line above it and before the line below it.

  40 |               <li key={s.value}>{s.label || s.value}</li>
     | This draws one piece of the page while ShieldStatusCard is showing.

  41 |             ))}
     | This ends ShieldStatusCard (opened on line 8).

  42 |             {blockedCount > topBlocked.length && (
     | Inside ShieldStatusCard, this line runs as written: {blockedCount > topBlocked.length && (. It happens in order, after the line above it and before the line below it.

  43 |               <li className="text-muted">+{blockedCount - topBlocked.length} more</li>
     | This draws one piece of the page while ShieldStatusCard is showing.

  44 |             )}
     | This ends ShieldStatusCard (opened on line 8).

  45 |           </ul>
     | This ends a drawing that ShieldStatusCard started just above.

  46 |         ) : (
     | This closes a box of instructions that opened above.

  47 |           <p className="text-sm text-muted" style={{ marginBottom: 12 }}>
     | This draws one piece of the page while ShieldStatusCard is showing.

  48 |             No sites blocked yet — add some so the shield has something to guard.
     | Inside ShieldStatusCard, this line runs as written: No sites blocked yet — add some so the shield has something to guard.. It happens in order, after the line above it and before the line below it.

  49 |           </p>
     | This ends a drawing that ShieldStatusCard started just above.

  50 |         )
     | This closes a box of instructions that opened above.

  51 |       ) : (
     | This closes a box of instructions that opened above.

  52 |         <div className="fs-dashboard-counts">
     | This draws one piece of the page while ShieldStatusCard is showing.

  53 |           <div>
     | This draws one piece of the page while ShieldStatusCard is showing.

  54 |             <div className="stat-value stat-violet" style={{ fontSize: 22 }}>{blockedCount}</div>
     | This draws one piece of the page while ShieldStatusCard is showing.

  55 |             <div className="stat-label">Blocked</div>
     | This draws one piece of the page while ShieldStatusCard is showing.

  56 |           </div>
     | This ends a drawing that ShieldStatusCard started just above.

  57 |           <div>
     | This draws one piece of the page while ShieldStatusCard is showing.

  58 |             <div className="stat-value stat-green" style={{ fontSize: 22 }}>{whitelistCount}</div>
     | This draws one piece of the page while ShieldStatusCard is showing.

  59 |             <div className="stat-label">Whitelisted</div>
     | This draws one piece of the page while ShieldStatusCard is showing.

  60 |           </div>
     | This ends a drawing that ShieldStatusCard started just above.

  61 |         </div>
     | This ends a drawing that ShieldStatusCard started just above.

  62 |       )}
     | This ends ShieldStatusCard (opened on line 8).

  63 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  64 |       <Link to="/blocking" className="btn btn-secondary btn-sm" style={{ marginTop: 12 }}>
     | This draws one piece of the page while ShieldStatusCard is showing.

  65 |         Manage Rules
     | Inside ShieldStatusCard, this line runs as written: Manage Rules. It happens in order, after the line above it and before the line below it.

  66 |       </Link>
     | This ends a drawing that ShieldStatusCard started just above.

  67 |     </div>
     | This ends a drawing that ShieldStatusCard started just above.

  68 |   );
     | This closes a box of instructions that opened above.

  69 | }
     | This ends ShieldStatusCard (opened on line 8).

