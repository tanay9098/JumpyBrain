# `src/components/focus-shield/PresetPicker.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import React, { useState } from "react";
     | Borrows React so this file can remember things and draw the screen.

   2 | import { PRESETS, mergeDomains } from "../../utils/focusShield";
     | This file borrows a tool another file already made.

   3 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   4 | // One-click presets — populate blockedSites with a recommended set of domains for a role.
     | A note written for people. The app does not run it.

   5 | // Non-destructive: merges in new domains, never removes what the user already added.
     | A note written for people. The app does not run it.

   6 | export default function PresetPicker({ blockedSites, onApply }) {
     | This starts PresetPicker. Applies one preset by merging its domains into the current block list.

   7 |   const [appliedId, setAppliedId] = useState(null);
     | This gives a short name to a value so the rest of PresetPicker can use it.

   8 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   9 |   function apply(preset) {
     | This starts apply. mergeDomains then onApply. Shows 'Applied' for 2 seconds.

  10 |     const merged = mergeDomains(
     | This gives a short name to a value so the rest of apply can use it.

  11 |       blockedSites,
     | Inside apply, this line runs as written: blockedSites,. It happens in order, after the line above it and before the line below it.

  12 |       preset.domains.map((d) => ({ value: d, label: "" }))
     | This ends apply (opened on line 9).

  13 |     );
     | This closes a box of instructions that opened above.

  14 |     onApply(merged);
     | Inside apply, this line runs as written: onApply(merged);. It happens in order, after the line above it and before the line below it.

  15 |     setAppliedId(preset.id);
     | Inside apply, this line runs as written: setAppliedId(preset.id);. It happens in order, after the line above it and before the line below it.

  16 |     setTimeout(() => setAppliedId(null), 2000);
     | Inside apply, this line runs as written: setTimeout(() => setAppliedId(null), 2000);. It happens in order, after the line above it and before the line below it.

  17 |   }
     | This ends apply (opened on line 9).

  18 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  19 |   return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  20 |     <section className="profile-settings-card">
     | This draws one piece of the page while PresetPicker is showing.

  21 |       <div className="profile-settings-card-header">
     | This draws one piece of the page while PresetPicker is showing.

  22 |         <h2 className="profile-settings-card-title">Smart presets</h2>
     | This draws one piece of the page while PresetPicker is showing.

  23 |         <p className="profile-settings-card-desc">
     | This draws one piece of the page while PresetPicker is showing.

  24 |           One click adds a recommended blocklist for your situation. You can still edit anything after.
     | Inside PresetPicker, this line runs as written: One click adds a recommended blocklist for your situation. You can still edit anything after.. It happens in order, after the line above it and before the line below it.

  25 |         </p>
     | This ends a drawing that PresetPicker started just above.

  26 |       </div>
     | This ends a drawing that PresetPicker started just above.

  27 |       <div className="fs-preset-grid">
     | This draws one piece of the page while PresetPicker is showing.

  28 |         {PRESETS.map((preset) => (
     | Inside PresetPicker, this line runs as written: {PRESETS.map((preset) => (. It happens in order, after the line above it and before the line below it.

  29 |           <button
     | This draws one piece of the page while PresetPicker is showing.

  30 |             key={preset.id}
     | This ends PresetPicker (opened on line 6).

  31 |             type="button"
     | Inside PresetPicker, this line runs as written: type="button". It happens in order, after the line above it and before the line below it.

  32 |             className="fs-preset-card"
     | Inside PresetPicker, this line runs as written: className="fs-preset-card". It happens in order, after the line above it and before the line below it.

  33 |             onClick={() => apply(preset)}
     | This decides what happens when you press.

  34 |           >
     | Inside PresetPicker, this line runs as written: >. It happens in order, after the line above it and before the line below it.

  35 |             <span className="fs-preset-emoji" aria-hidden="true">{preset.emoji}</span>
     | This draws one piece of the page while PresetPicker is showing.

  36 |             <span className="fs-preset-label">{preset.label}</span>
     | This draws one piece of the page while PresetPicker is showing.

  37 |             <span className="fs-preset-desc">{preset.description}</span>
     | This draws one piece of the page while PresetPicker is showing.

  38 |             <span className="fs-preset-status">
     | This draws one piece of the page while PresetPicker is showing.

  39 |               {appliedId === preset.id ? "✓ Applied" : `${preset.domains.length} sites`}
     | This ends PresetPicker (opened on line 6).

  40 |             </span>
     | This ends a drawing that PresetPicker started just above.

  41 |           </button>
     | This ends a drawing that PresetPicker started just above.

  42 |         ))}
     | This ends PresetPicker (opened on line 6).

  43 |       </div>
     | This ends a drawing that PresetPicker started just above.

  44 |     </section>
     | This ends a drawing that PresetPicker started just above.

  45 |   );
     | This closes a box of instructions that opened above.

  46 | }
     | This ends PresetPicker (opened on line 6).

