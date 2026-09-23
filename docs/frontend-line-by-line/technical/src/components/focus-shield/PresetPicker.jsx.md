# `src/components/focus-shield/PresetPicker.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import React, { useState } from "react";
     | Import for one-click blocklists: `import React, { useState } from "react";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   2 | import { PRESETS, mergeDomains } from "../../utils/focusShield";
     | Import for one-click blocklists: `import { PRESETS, mergeDomains } from "../../utils/focusShield";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   3 | 
     | Blank line in `src/components/focus-shield/PresetPicker.jsx` (one-click blocklists), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   4 | // One-click presets — populate blockedSites with a recommended set of domains for a role.
     | Comment inside the top of the file. Not executed. It documents the next code: One-click presets — populate blockedSites with a recommended set of domains for a role.

   5 | // Non-destructive: merges in new domains, never removes what the user already added.
     | Comment inside the top of the file. Not executed. It documents the next code: Non-destructive: merges in new domains, never removes what the user already added.

   6 | export default function PresetPicker({ blockedSites, onApply }) {
     | Defines `PresetPicker` in one-click blocklists. Applies one preset by merging its domains into the current block list.

   7 |   const [appliedId, setAppliedId] = useState(null);
     | In `PresetPicker` (src/components/focus-shield/PresetPicker.jsx): React state `appliedId, setAppliedId`. The value survives re-renders. Calling the setter re-renders this component. `const [appliedId, setAppliedId] = useState(null);`

   8 | 
     | Blank line in `src/components/focus-shield/PresetPicker.jsx` (one-click blocklists), inside PresetPicker. The parser skips it. It separates the previous statement from the next so the function is readable.

   9 |   function apply(preset) {
     | Defines `apply` in one-click blocklists. mergeDomains then onApply. Shows 'Applied' for 2 seconds.

  10 |     const merged = mergeDomains(
     | In `apply` (src/components/focus-shield/PresetPicker.jsx): `merged` is assigned `mergeDomains(`. Later lines in this function read that name.

  11 |       blockedSites,
     | In `apply` (src/components/focus-shield/PresetPicker.jsx): statement `blockedSites,`. It runs when apply runs, in order, before the next line of the same function.

  12 |       preset.domains.map((d) => ({ value: d, label: "" }))
     | In `apply` (src/components/focus-shield/PresetPicker.jsx): iteration `preset.domains.map((d) => ({ value: d, label: "" }))`.

  13 |     );
     | In `apply` (src/components/focus-shield/PresetPicker.jsx): statement `);`. It runs when apply runs, in order, before the next line of the same function.

  14 |     onApply(merged);
     | In `apply` (src/components/focus-shield/PresetPicker.jsx): statement `onApply(merged);`. It runs when apply runs, in order, before the next line of the same function.

  15 |     setAppliedId(preset.id);
     | In `apply` (src/components/focus-shield/PresetPicker.jsx): statement `setAppliedId(preset.id);`. It runs when apply runs, in order, before the next line of the same function.

  16 |     setTimeout(() => setAppliedId(null), 2000);
     | In `apply` (src/components/focus-shield/PresetPicker.jsx): timer — `setTimeout(() => setAppliedId(null), 2000);`. The callback runs later on the event loop, not now.

  17 |   }
     | In `apply` (src/components/focus-shield/PresetPicker.jsx): `}` closes apply (opened on line 9). Names declared inside that block end here.

  18 | 
     | Blank line in `src/components/focus-shield/PresetPicker.jsx` (one-click blocklists), inside PresetPicker. The parser skips it. It separates the previous statement from the next so the function is readable.

  19 |   return (
     | In `PresetPicker` (src/components/focus-shield/PresetPicker.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  20 |     <section className="profile-settings-card">
     | In `PresetPicker` (src/components/focus-shield/PresetPicker.jsx): Opens it. A grouped block on the settings-style pages. Source: `<section className="profile-settings-card">`

  21 |       <div className="profile-settings-card-header">
     | In `PresetPicker` (src/components/focus-shield/PresetPicker.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="profile-settings-card-header">`

  22 |         <h2 className="profile-settings-card-title">Smart presets</h2>
     | In `PresetPicker` (src/components/focus-shield/PresetPicker.jsx): JSX `<h2>`. React will create this node when the parent renders.. className chooses the CSS rules from styles.css Source: `<h2 className="profile-settings-card-title">Smart presets</h2>`

  23 |         <p className="profile-settings-card-desc">
     | In `PresetPicker` (src/components/focus-shield/PresetPicker.jsx): Opens it. A paragraph. Source: `<p className="profile-settings-card-desc">`

  24 |           One click adds a recommended blocklist for your situation. You can still edit anything after.
     | In `PresetPicker` (src/components/focus-shield/PresetPicker.jsx): statement `One click adds a recommended blocklist for your situation. You can still edit anything after.`. It runs when PresetPicker runs, in order, before the next line of the same function.

  25 |         </p>
     | In `PresetPicker` (src/components/focus-shield/PresetPicker.jsx): Closes it. A paragraph. Source: `</p>`

  26 |       </div>
     | In `PresetPicker` (src/components/focus-shield/PresetPicker.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  27 |       <div className="fs-preset-grid">
     | In `PresetPicker` (src/components/focus-shield/PresetPicker.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="fs-preset-grid">`

  28 |         {PRESETS.map((preset) => (
     | In `PresetPicker` (src/components/focus-shield/PresetPicker.jsx): iteration `{PRESETS.map((preset) => (`.

  29 |           <button
     | In `PresetPicker` (src/components/focus-shield/PresetPicker.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button`

  30 |             key={preset.id}
     | In `PresetPicker` (src/components/focus-shield/PresetPicker.jsx): `key={preset.id}` closes PresetPicker (opened on line 6). Names declared inside that block end here.

  31 |             type="button"
     | In `PresetPicker` (src/components/focus-shield/PresetPicker.jsx): statement `type="button"`. It runs when PresetPicker runs, in order, before the next line of the same function.

  32 |             className="fs-preset-card"
     | In `PresetPicker` (src/components/focus-shield/PresetPicker.jsx): statement `className="fs-preset-card"`. It runs when PresetPicker runs, in order, before the next line of the same function.

  33 |             onClick={() => apply(preset)}
     | In `PresetPicker` (src/components/focus-shield/PresetPicker.jsx): event prop `onClick={() => apply(preset)}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

  34 |           >
     | In `PresetPicker` (src/components/focus-shield/PresetPicker.jsx): statement `>`. It runs when PresetPicker runs, in order, before the next line of the same function.

  35 |             <span className="fs-preset-emoji" aria-hidden="true">{preset.emoji}</span>
     | In `PresetPicker` (src/components/focus-shield/PresetPicker.jsx): Opens it. An inline box. Source: `<span className="fs-preset-emoji" aria-hidden="true">{preset.emoji}</span>`

  36 |             <span className="fs-preset-label">{preset.label}</span>
     | In `PresetPicker` (src/components/focus-shield/PresetPicker.jsx): Opens it. An inline box. Source: `<span className="fs-preset-label">{preset.label}</span>`

  37 |             <span className="fs-preset-desc">{preset.description}</span>
     | In `PresetPicker` (src/components/focus-shield/PresetPicker.jsx): Opens it. An inline box. Source: `<span className="fs-preset-desc">{preset.description}</span>`

  38 |             <span className="fs-preset-status">
     | In `PresetPicker` (src/components/focus-shield/PresetPicker.jsx): Opens it. An inline box. Source: `<span className="fs-preset-status">`

  39 |               {appliedId === preset.id ? "✓ Applied" : `${preset.domains.length} sites`}
     | In `PresetPicker` (src/components/focus-shield/PresetPicker.jsx): `{appliedId === preset.id ? "✓ Applied" : `${preset.domains.length} sites`}` closes PresetPicker (opened on line 6). Names declared inside that block end here.

  40 |             </span>
     | In `PresetPicker` (src/components/focus-shield/PresetPicker.jsx): Closes it. An inline box. Source: `</span>`

  41 |           </button>
     | In `PresetPicker` (src/components/focus-shield/PresetPicker.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

  42 |         ))}
     | In `PresetPicker` (src/components/focus-shield/PresetPicker.jsx): `))}` closes PresetPicker (opened on line 6). Names declared inside that block end here.

  43 |       </div>
     | In `PresetPicker` (src/components/focus-shield/PresetPicker.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  44 |     </section>
     | In `PresetPicker` (src/components/focus-shield/PresetPicker.jsx): Closes it. A grouped block on the settings-style pages. Source: `</section>`

  45 |   );
     | In `PresetPicker` (src/components/focus-shield/PresetPicker.jsx): statement `);`. It runs when PresetPicker runs, in order, before the next line of the same function.

  46 | }
     | In `PresetPicker` (src/components/focus-shield/PresetPicker.jsx): `}` closes PresetPicker (opened on line 6). Names declared inside that block end here.

