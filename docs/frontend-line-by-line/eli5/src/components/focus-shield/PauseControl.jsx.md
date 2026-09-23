# `src/components/focus-shield/PauseControl.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import React, { useState } from "react";
     | Borrows React so this file can remember things and draw the screen.

   2 | import { PAUSE_PRESETS, computePauseUntil, formatClockTime, isPaused } from "../../utils/focusShield";
     | This file borrows a tool another file already made.

   3 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   4 | // Temporary-disable control: quick presets (15m/30m/1h/tomorrow) plus a custom-minutes option.
     | A note written for people. The app does not run it.

   5 | // Pausing writes `pausedUntil` back through the normal PUT /blocking save path, so it
     | A note written for people. The app does not run it.

   6 | // propagates to the Chrome extension on its next sync — no separate endpoint needed.
     | A note written for people. The app does not run it.

   7 | export default function PauseControl({ rules, saving, onPause, onResume }) {
     | This starts PauseControl. Hidden when the shield is off. If paused, shows the resume time. Otherwise preset buttons and a custom minute field.

   8 |   const [customOpen, setCustomOpen] = useState(false);
     | This gives a short name to a value so the rest of PauseControl can use it.

   9 |   const [customMinutes, setCustomMinutes] = useState(45);
     | This gives a short name to a value so the rest of PauseControl can use it.

  10 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  11 |   if (!rules?.isEnabled) return null;
     | This asks a yes-or-no question. The next bit runs only on yes.

  12 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  13 |   if (isPaused(rules)) {
     | This asks a yes-or-no question. The next bit runs only on yes.

  14 |     return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  15 |       <div className="fs-pause-banner" role="status" aria-live="polite">
     | This draws one piece of the page while PauseControl is showing.

  16 |         <span>⏸ Paused — resumes at {formatClockTime(rules.pausedUntil)}</span>
     | This draws one piece of the page while PauseControl is showing.

  17 |         <button type="button" className="btn btn-primary btn-sm" onClick={onResume} disabled={saving}>
     | This draws one piece of the page while PauseControl is showing.

  18 |           Resume now
     | Inside PauseControl, this line runs as written: Resume now. It happens in order, after the line above it and before the line below it.

  19 |         </button>
     | This ends a drawing that PauseControl started just above.

  20 |       </div>
     | This ends a drawing that PauseControl started just above.

  21 |     );
     | This closes a box of instructions that opened above.

  22 |   }
     | This ends if (isPaused(rules)) { (opened on line 13).

  23 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  24 |   return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  25 |     <div>
     | This draws one piece of the page while PauseControl is showing.

  26 |       <p className="profile-form-label" style={{ marginBottom: 8 }}>Pause blocking</p>
     | This draws one piece of the page while PauseControl is showing.

  27 |       <div className="fs-pause-row">
     | This draws one piece of the page while PauseControl is showing.

  28 |         {PAUSE_PRESETS.map((p) => (
     | Inside PauseControl, this line runs as written: {PAUSE_PRESETS.map((p) => (. It happens in order, after the line above it and before the line below it.

  29 |           <button
     | This draws one piece of the page while PauseControl is showing.

  30 |             key={p.id}
     | This ends PauseControl (opened on line 7).

  31 |             type="button"
     | Inside PauseControl, this line runs as written: type="button". It happens in order, after the line above it and before the line below it.

  32 |             className="btn btn-ghost btn-sm"
     | Inside PauseControl, this line runs as written: className="btn btn-ghost btn-sm". It happens in order, after the line above it and before the line below it.

  33 |             disabled={saving}
     | This ends PauseControl (opened on line 7).

  34 |             onClick={() => onPause(computePauseUntil(p.id))}
     | This decides what happens when you press.

  35 |           >
     | Inside PauseControl, this line runs as written: >. It happens in order, after the line above it and before the line below it.

  36 |             {p.label}
     | This ends PauseControl (opened on line 7).

  37 |           </button>
     | This ends a drawing that PauseControl started just above.

  38 |         ))}
     | This ends PauseControl (opened on line 7).

  39 |         <button
     | This draws one piece of the page while PauseControl is showing.

  40 |           type="button"
     | Inside PauseControl, this line runs as written: type="button". It happens in order, after the line above it and before the line below it.

  41 |           className="btn btn-ghost btn-sm"
     | Inside PauseControl, this line runs as written: className="btn btn-ghost btn-sm". It happens in order, after the line above it and before the line below it.

  42 |           disabled={saving}
     | This ends PauseControl (opened on line 7).

  43 |           onClick={() => setCustomOpen((o) => !o)}
     | This decides what happens when you press.

  44 |           aria-expanded={customOpen}
     | This ends PauseControl (opened on line 7).

  45 |         >
     | Inside PauseControl, this line runs as written: >. It happens in order, after the line above it and before the line below it.

  46 |           Custom…
     | Inside PauseControl, this line runs as written: Custom…. It happens in order, after the line above it and before the line below it.

  47 |         </button>
     | This ends a drawing that PauseControl started just above.

  48 |       </div>
     | This ends a drawing that PauseControl started just above.

  49 |       {customOpen && (
     | Inside PauseControl, this line runs as written: {customOpen && (. It happens in order, after the line above it and before the line below it.

  50 |         <div className="fs-pause-custom">
     | This draws one piece of the page while PauseControl is showing.

  51 |           <input
     | This draws one piece of the page while PauseControl is showing.

  52 |             type="number"
     | Inside PauseControl, this line runs as written: type="number". It happens in order, after the line above it and before the line below it.

  53 |             min={1}
     | This ends PauseControl (opened on line 7).

  54 |             max={1440}
     | This ends PauseControl (opened on line 7).

  55 |             className="profile-form-input"
     | Inside PauseControl, this line runs as written: className="profile-form-input". It happens in order, after the line above it and before the line below it.

  56 |             style={{ width: 90 }}
     | This ends PauseControl (opened on line 7).

  57 |             value={customMinutes}
     | This ends PauseControl (opened on line 7).

  58 |             onChange={(e) => setCustomMinutes(Number(e.target.value))}
     | This ends PauseControl (opened on line 7).

  59 |             aria-label="Custom pause duration in minutes"
     | Inside PauseControl, this line runs as written: aria-label="Custom pause duration in minutes". It happens in order, after the line above it and before the line below it.

  60 |           />
     | This closes a box of instructions that opened above.

  61 |           <span className="text-sm text-muted">minutes</span>
     | This draws one piece of the page while PauseControl is showing.

  62 |           <button
     | This draws one piece of the page while PauseControl is showing.

  63 |             type="button"
     | Inside PauseControl, this line runs as written: type="button". It happens in order, after the line above it and before the line below it.

  64 |             className="btn btn-primary btn-sm"
     | Inside PauseControl, this line runs as written: className="btn btn-primary btn-sm". It happens in order, after the line above it and before the line below it.

  65 |             disabled={saving || !customMinutes || customMinutes < 1}
     | This ends PauseControl (opened on line 7).

  66 |             onClick={() => onPause(computePauseUntil("custom", customMinutes))}
     | This decides what happens when you press.

  67 |           >
     | Inside PauseControl, this line runs as written: >. It happens in order, after the line above it and before the line below it.

  68 |             Pause
     | Inside PauseControl, this line runs as written: Pause. It happens in order, after the line above it and before the line below it.

  69 |           </button>
     | This ends a drawing that PauseControl started just above.

  70 |         </div>
     | This ends a drawing that PauseControl started just above.

  71 |       )}
     | This ends PauseControl (opened on line 7).

  72 |     </div>
     | This ends a drawing that PauseControl started just above.

  73 |   );
     | This closes a box of instructions that opened above.

  74 | }
     | This ends PauseControl (opened on line 7).

