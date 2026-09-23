# `src/components/focus-shield/PauseControl.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import React, { useState } from "react";
     | Import for pause blocking for a few minutes or until tomorrow: `import React, { useState } from "react";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   2 | import { PAUSE_PRESETS, computePauseUntil, formatClockTime, isPaused } from "../../utils/focusShield";
     | Import for pause blocking for a few minutes or until tomorrow: `import { PAUSE_PRESETS, computePauseUntil, formatClockTime, isPaused } from "../../utils/focusShield";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   3 | 
     | Blank line in `src/components/focus-shield/PauseControl.jsx` (pause blocking for a few minutes or until tomorrow), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   4 | // Temporary-disable control: quick presets (15m/30m/1h/tomorrow) plus a custom-minutes option.
     | Comment inside the top of the file. Not executed. It documents the next code: Temporary-disable control: quick presets (15m/30m/1h/tomorrow) plus a custom-minutes option.

   5 | // Pausing writes `pausedUntil` back through the normal PUT /blocking save path, so it
     | Comment inside the top of the file. Not executed. It documents the next code: Pausing writes `pausedUntil` back through the normal PUT /blocking save path, so it

   6 | // propagates to the Chrome extension on its next sync — no separate endpoint needed.
     | Comment inside the top of the file. Not executed. It documents the next code: propagates to the Chrome extension on its next sync — no separate endpoint needed.

   7 | export default function PauseControl({ rules, saving, onPause, onResume }) {
     | Defines `PauseControl` in pause blocking for a few minutes or until tomorrow. Hidden when the shield is off. If paused, shows the resume time. Otherwise preset buttons and a custom minute field.

   8 |   const [customOpen, setCustomOpen] = useState(false);
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): React state `customOpen, setCustomOpen`. The value survives re-renders. Calling the setter re-renders this component. `const [customOpen, setCustomOpen] = useState(false);`

   9 |   const [customMinutes, setCustomMinutes] = useState(45);
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): React state `customMinutes, setCustomMinutes`. The value survives re-renders. Calling the setter re-renders this component. `const [customMinutes, setCustomMinutes] = useState(45);`

  10 | 
     | Blank line in `src/components/focus-shield/PauseControl.jsx` (pause blocking for a few minutes or until tomorrow), inside PauseControl. The parser skips it. It separates the previous statement from the next so the function is readable.

  11 |   if (!rules?.isEnabled) return null;
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): branch `if (!rules?.isEnabled) return null;`. Only one side runs.

  12 | 
     | Blank line in `src/components/focus-shield/PauseControl.jsx` (pause blocking for a few minutes or until tomorrow), inside PauseControl. The parser skips it. It separates the previous statement from the next so the function is readable.

  13 |   if (isPaused(rules)) {
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): branch `if (isPaused(rules)) {`. Only one side runs.

  14 |     return (
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  15 |       <div className="fs-pause-banner" role="status" aria-live="polite">
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="fs-pause-banner" role="status" aria-live="polite">`

  16 |         <span>⏸ Paused — resumes at {formatClockTime(rules.pausedUntil)}</span>
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): Opens it. An inline box. Source: `<span>⏸ Paused — resumes at {formatClockTime(rules.pausedUntil)}</span>`

  17 |         <button type="button" className="btn btn-primary btn-sm" onClick={onResume} disabled={saving}>
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button type="button" className="btn btn-primary btn-sm" onClick={onResume} disabled={saving}>`

  18 |           Resume now
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): statement `Resume now`. It runs when PauseControl runs, in order, before the next line of the same function.

  19 |         </button>
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

  20 |       </div>
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  21 |     );
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): statement `);`. It runs when PauseControl runs, in order, before the next line of the same function.

  22 |   }
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): `}` closes if (isPaused(rules)) { (opened on line 13). Names declared inside that block end here.

  23 | 
     | Blank line in `src/components/focus-shield/PauseControl.jsx` (pause blocking for a few minutes or until tomorrow), inside PauseControl. The parser skips it. It separates the previous statement from the next so the function is readable.

  24 |   return (
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  25 |     <div>
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): Opens it. A box that groups the elements inside it. Source: `<div>`

  26 |       <p className="profile-form-label" style={{ marginBottom: 8 }}>Pause blocking</p>
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): Opens it. A paragraph. Source: `<p className="profile-form-label" style={{ marginBottom: 8 }}>Pause blocking</p>`

  27 |       <div className="fs-pause-row">
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="fs-pause-row">`

  28 |         {PAUSE_PRESETS.map((p) => (
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): iteration `{PAUSE_PRESETS.map((p) => (`.

  29 |           <button
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button`

  30 |             key={p.id}
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): `key={p.id}` closes PauseControl (opened on line 7). Names declared inside that block end here.

  31 |             type="button"
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): statement `type="button"`. It runs when PauseControl runs, in order, before the next line of the same function.

  32 |             className="btn btn-ghost btn-sm"
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): statement `className="btn btn-ghost btn-sm"`. It runs when PauseControl runs, in order, before the next line of the same function.

  33 |             disabled={saving}
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): `disabled={saving}` closes PauseControl (opened on line 7). Names declared inside that block end here.

  34 |             onClick={() => onPause(computePauseUntil(p.id))}
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): event prop `onClick={() => onPause(computePauseUntil(p.id))}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

  35 |           >
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): statement `>`. It runs when PauseControl runs, in order, before the next line of the same function.

  36 |             {p.label}
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): `{p.label}` closes PauseControl (opened on line 7). Names declared inside that block end here.

  37 |           </button>
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

  38 |         ))}
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): `))}` closes PauseControl (opened on line 7). Names declared inside that block end here.

  39 |         <button
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button`

  40 |           type="button"
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): statement `type="button"`. It runs when PauseControl runs, in order, before the next line of the same function.

  41 |           className="btn btn-ghost btn-sm"
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): statement `className="btn btn-ghost btn-sm"`. It runs when PauseControl runs, in order, before the next line of the same function.

  42 |           disabled={saving}
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): `disabled={saving}` closes PauseControl (opened on line 7). Names declared inside that block end here.

  43 |           onClick={() => setCustomOpen((o) => !o)}
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): event prop `onClick={() => setCustomOpen((o) => !o)}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

  44 |           aria-expanded={customOpen}
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): `aria-expanded={customOpen}` closes PauseControl (opened on line 7). Names declared inside that block end here.

  45 |         >
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): statement `>`. It runs when PauseControl runs, in order, before the next line of the same function.

  46 |           Custom…
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): statement `Custom…`. It runs when PauseControl runs, in order, before the next line of the same function.

  47 |         </button>
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

  48 |       </div>
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  49 |       {customOpen && (
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): statement `{customOpen && (`. It runs when PauseControl runs, in order, before the next line of the same function.

  50 |         <div className="fs-pause-custom">
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="fs-pause-custom">`

  51 |           <input
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): Opens it. A text or date field. If value and onChange are set, React owns what it shows. Source: `<input`

  52 |             type="number"
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): statement `type="number"`. It runs when PauseControl runs, in order, before the next line of the same function.

  53 |             min={1}
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): `min={1}` closes PauseControl (opened on line 7). Names declared inside that block end here.

  54 |             max={1440}
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): `max={1440}` closes PauseControl (opened on line 7). Names declared inside that block end here.

  55 |             className="profile-form-input"
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): statement `className="profile-form-input"`. It runs when PauseControl runs, in order, before the next line of the same function.

  56 |             style={{ width: 90 }}
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): `style={{ width: 90 }}` closes PauseControl (opened on line 7). Names declared inside that block end here.

  57 |             value={customMinutes}
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): `value={customMinutes}` closes PauseControl (opened on line 7). Names declared inside that block end here.

  58 |             onChange={(e) => setCustomMinutes(Number(e.target.value))}
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): event prop `onChange={(e) => setCustomMinutes(Number(e.target.value))}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

  59 |             aria-label="Custom pause duration in minutes"
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): statement `aria-label="Custom pause duration in minutes"`. It runs when PauseControl runs, in order, before the next line of the same function.

  60 |           />
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): statement `/>`. It runs when PauseControl runs, in order, before the next line of the same function.

  61 |           <span className="text-sm text-muted">minutes</span>
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): Opens it. An inline box. Source: `<span className="text-sm text-muted">minutes</span>`

  62 |           <button
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button`

  63 |             type="button"
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): statement `type="button"`. It runs when PauseControl runs, in order, before the next line of the same function.

  64 |             className="btn btn-primary btn-sm"
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): statement `className="btn btn-primary btn-sm"`. It runs when PauseControl runs, in order, before the next line of the same function.

  65 |             disabled={saving || !customMinutes || customMinutes < 1}
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): `disabled={saving || !customMinutes || customMinutes < 1}` closes PauseControl (opened on line 7). Names declared inside that block end here.

  66 |             onClick={() => onPause(computePauseUntil("custom", customMinutes))}
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): event prop `onClick={() => onPause(computePauseUntil("custom", customMinutes))}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

  67 |           >
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): statement `>`. It runs when PauseControl runs, in order, before the next line of the same function.

  68 |             Pause
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): statement `Pause`. It runs when PauseControl runs, in order, before the next line of the same function.

  69 |           </button>
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

  70 |         </div>
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  71 |       )}
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): `)}` closes PauseControl (opened on line 7). Names declared inside that block end here.

  72 |     </div>
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  73 |   );
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): statement `);`. It runs when PauseControl runs, in order, before the next line of the same function.

  74 | }
     | In `PauseControl` (src/components/focus-shield/PauseControl.jsx): `}` closes PauseControl (opened on line 7). Names declared inside that block end here.

