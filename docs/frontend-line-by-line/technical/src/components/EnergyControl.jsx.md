# `src/components/EnergyControl.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import React from "react";
     | Import for the five energy buttons: `import React from "react";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   2 | import { useEnergy } from "../contexts/EnergyContext";
     | Import for the five energy buttons: `import { useEnergy } from "../contexts/EnergyContext";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   3 | 
     | Blank line in `src/components/EnergyControl.jsx` (the five energy buttons), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   4 | const ENERGY_LEVELS = [
     | In `the top of the file` (src/components/EnergyControl.jsx): `ENERGY_LEVELS`: Five faces indexed 0–4, stored as levels 1–5: Exhausted, Low, Okay, Good, Peak. EnergyControl is the only writer; EnergyContext holds the number. The code is `const ENERGY_LEVELS = [`.

   5 |   { emoji: "💀", label: "Exhausted", color: "var(--muted)" },
     | In `the top of the file` (src/components/EnergyControl.jsx): `{ emoji: "💀", label: "Exhausted", color: "var(--muted)" },` closes the nearest open block. Names declared inside that block end here.

   6 |   { emoji: "😔", label: "Low",       color: "var(--blue)" },
     | In `the top of the file` (src/components/EnergyControl.jsx): `{ emoji: "😔", label: "Low",       color: "var(--blue)" },` closes the nearest open block. Names declared inside that block end here.

   7 |   { emoji: "😐", label: "Okay",      color: "var(--amber)" },
     | In `the top of the file` (src/components/EnergyControl.jsx): `{ emoji: "😐", label: "Okay",      color: "var(--amber)" },` closes the nearest open block. Names declared inside that block end here.

   8 |   { emoji: "⚡", label: "Good",      color: "var(--green)" },
     | In `the top of the file` (src/components/EnergyControl.jsx): `{ emoji: "⚡", label: "Good",      color: "var(--green)" },` closes the nearest open block. Names declared inside that block end here.

   9 |   { emoji: "🔥", label: "Peak",      color: "var(--violet-light)" },
     | In `the top of the file` (src/components/EnergyControl.jsx): `{ emoji: "🔥", label: "Peak",      color: "var(--violet-light)" },` closes the nearest open block. Names declared inside that block end here.

  10 | ];
     | In `the top of the file` (src/components/EnergyControl.jsx): statement `];`. It runs when the top of the file runs, in order, before the next line of the same function.

  11 | 
     | Blank line in `src/components/EnergyControl.jsx` (the five energy buttons), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  12 | export default function EnergyControl({ compact = false }) {
     | Defines `EnergyControl` in the five energy buttons. Reads and writes EnergyContext. compact=true is the five dots in the sidebar. Otherwise the big emoji buttons on Today.

  13 |   const { energy, setEnergy } = useEnergy();
     | In `EnergyControl` (src/components/EnergyControl.jsx): `energy`: Integer 1–5 from EnergyContext, persisted as bb-energy. Home refetches 'what next' when it changes. TodoList rescores and refetches suggestions. The code is `const { energy, setEnergy } = useEnergy();`.

  14 | 
     | Blank line in `src/components/EnergyControl.jsx` (the five energy buttons), inside EnergyControl. The parser skips it. It separates the previous statement from the next so the function is readable.

  15 |   if (compact) {
     | In `EnergyControl` (src/components/EnergyControl.jsx): branch `if (compact) {`. Only one side runs.

  16 |     return (
     | In `EnergyControl` (src/components/EnergyControl.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  17 |       <div className="energy-control-compact">
     | In `EnergyControl` (src/components/EnergyControl.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="energy-control-compact">`

  18 |         {ENERGY_LEVELS.map((lvl, i) => {
     | In `EnergyControl` (src/components/EnergyControl.jsx): iteration `{ENERGY_LEVELS.map((lvl, i) => {`.

  19 |           const n = i + 1;
     | In `EnergyControl` (src/components/EnergyControl.jsx): `n` is assigned `i + 1;`. Later lines in this function read that name.

  20 |           return (
     | In `EnergyControl` (src/components/EnergyControl.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  21 |             <button
     | In `EnergyControl` (src/components/EnergyControl.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button`

  22 |               key={n}
     | In `EnergyControl` (src/components/EnergyControl.jsx): `key={n}` closes {ENERGY_LEVELS.map((lvl, i) => { (opened on line 18). Names declared inside that block end here.

  23 |               className={`energy-dot ${n <= energy ? "filled" : ""}`}
     | In `EnergyControl` (src/components/EnergyControl.jsx): `className={`energy-dot ${n <= energy ? "filled" : ""}`}` closes {ENERGY_LEVELS.map((lvl, i) => { (opened on line 18). Names declared inside that block end here.

  24 |               onClick={() => setEnergy(n)}
     | In `EnergyControl` (src/components/EnergyControl.jsx): event prop `onClick={() => setEnergy(n)}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

  25 |               title={`${lvl.emoji} ${lvl.label}`}
     | In `EnergyControl` (src/components/EnergyControl.jsx): `title={`${lvl.emoji} ${lvl.label}`}` closes {ENERGY_LEVELS.map((lvl, i) => { (opened on line 18). Names declared inside that block end here.

  26 |               aria-label={`Set energy to ${lvl.label}`}
     | In `EnergyControl` (src/components/EnergyControl.jsx): `aria-label={`Set energy to ${lvl.label}`}` closes {ENERGY_LEVELS.map((lvl, i) => { (opened on line 18). Names declared inside that block end here.

  27 |               aria-pressed={n === energy}
     | In `EnergyControl` (src/components/EnergyControl.jsx): `aria-pressed={n === energy}` closes {ENERGY_LEVELS.map((lvl, i) => { (opened on line 18). Names declared inside that block end here.

  28 |               style={n <= energy ? { borderColor: ENERGY_LEVELS[energy - 1].color, background: ENERGY_LEVELS[energy - 1].color + "25" } : {}}
     | In `EnergyControl` (src/components/EnergyControl.jsx): `style={n <= energy ? { borderColor: ENERGY_LEVELS[energy - 1].color, background: ENERGY_LEVELS[energy - 1].color + "25" } : {}}` closes {ENERGY_LEVELS.map((lvl, i) => { (opened on line 18). Names declared inside that block end here.

  29 |             >
     | In `EnergyControl` (src/components/EnergyControl.jsx): statement `>`. It runs when EnergyControl runs, in order, before the next line of the same function.

  30 |               {n <= energy ? lvl.emoji : ""}
     | In `EnergyControl` (src/components/EnergyControl.jsx): `{n <= energy ? lvl.emoji : ""}` closes {ENERGY_LEVELS.map((lvl, i) => { (opened on line 18). Names declared inside that block end here.

  31 |             </button>
     | In `EnergyControl` (src/components/EnergyControl.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

  32 |           );
     | In `EnergyControl` (src/components/EnergyControl.jsx): statement `);`. It runs when EnergyControl runs, in order, before the next line of the same function.

  33 |         })}
     | In `EnergyControl` (src/components/EnergyControl.jsx): `})}` closes {ENERGY_LEVELS.map((lvl, i) => { (opened on line 18). Names declared inside that block end here.

  34 |       </div>
     | In `EnergyControl` (src/components/EnergyControl.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  35 |     );
     | In `EnergyControl` (src/components/EnergyControl.jsx): statement `);`. It runs when EnergyControl runs, in order, before the next line of the same function.

  36 |   }
     | In `EnergyControl` (src/components/EnergyControl.jsx): `}` closes if (compact) { (opened on line 15). Names declared inside that block end here.

  37 | 
     | Blank line in `src/components/EnergyControl.jsx` (the five energy buttons), inside EnergyControl. The parser skips it. It separates the previous statement from the next so the function is readable.

  38 |   return (
     | In `EnergyControl` (src/components/EnergyControl.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  39 |     <div className="energy-control">
     | In `EnergyControl` (src/components/EnergyControl.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="energy-control">`

  40 |       <div className="energy-control-row">
     | In `EnergyControl` (src/components/EnergyControl.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="energy-control-row">`

  41 |         {ENERGY_LEVELS.map((lvl, i) => {
     | In `EnergyControl` (src/components/EnergyControl.jsx): iteration `{ENERGY_LEVELS.map((lvl, i) => {`.

  42 |           const n = i + 1;
     | In `EnergyControl` (src/components/EnergyControl.jsx): `n` is assigned `i + 1;`. Later lines in this function read that name.

  43 |           const isSelected = energy === n;
     | In `EnergyControl` (src/components/EnergyControl.jsx): `isSelected` is assigned `energy === n;`. Later lines in this function read that name.

  44 |           return (
     | In `EnergyControl` (src/components/EnergyControl.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  45 |             <button
     | In `EnergyControl` (src/components/EnergyControl.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button`

  46 |               key={n}
     | In `EnergyControl` (src/components/EnergyControl.jsx): `key={n}` closes {ENERGY_LEVELS.map((lvl, i) => { (opened on line 41). Names declared inside that block end here.

  47 |               className={`energy-btn ${isSelected ? "selected" : ""}`}
     | In `EnergyControl` (src/components/EnergyControl.jsx): `className={`energy-btn ${isSelected ? "selected" : ""}`}` closes {ENERGY_LEVELS.map((lvl, i) => { (opened on line 41). Names declared inside that block end here.

  48 |               onClick={() => setEnergy(n)}
     | In `EnergyControl` (src/components/EnergyControl.jsx): event prop `onClick={() => setEnergy(n)}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

  49 |               title={`${lvl.emoji} ${lvl.label}`}
     | In `EnergyControl` (src/components/EnergyControl.jsx): `title={`${lvl.emoji} ${lvl.label}`}` closes {ENERGY_LEVELS.map((lvl, i) => { (opened on line 41). Names declared inside that block end here.

  50 |               aria-label={`Set energy to ${lvl.label}`}
     | In `EnergyControl` (src/components/EnergyControl.jsx): `aria-label={`Set energy to ${lvl.label}`}` closes {ENERGY_LEVELS.map((lvl, i) => { (opened on line 41). Names declared inside that block end here.

  51 |               aria-pressed={isSelected}
     | In `EnergyControl` (src/components/EnergyControl.jsx): `aria-pressed={isSelected}` closes {ENERGY_LEVELS.map((lvl, i) => { (opened on line 41). Names declared inside that block end here.

  52 |             >
     | In `EnergyControl` (src/components/EnergyControl.jsx): statement `>`. It runs when EnergyControl runs, in order, before the next line of the same function.

  53 |               {lvl.emoji}
     | In `EnergyControl` (src/components/EnergyControl.jsx): `{lvl.emoji}` closes {ENERGY_LEVELS.map((lvl, i) => { (opened on line 41). Names declared inside that block end here.

  54 |             </button>
     | In `EnergyControl` (src/components/EnergyControl.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

  55 |           );
     | In `EnergyControl` (src/components/EnergyControl.jsx): statement `);`. It runs when EnergyControl runs, in order, before the next line of the same function.

  56 |         })}
     | In `EnergyControl` (src/components/EnergyControl.jsx): `})}` closes {ENERGY_LEVELS.map((lvl, i) => { (opened on line 41). Names declared inside that block end here.

  57 |         <span className="energy-current-label">
     | In `EnergyControl` (src/components/EnergyControl.jsx): Opens it. An inline box. Source: `<span className="energy-current-label">`

  58 |           {ENERGY_LEVELS[energy - 1].label}
     | In `EnergyControl` (src/components/EnergyControl.jsx): `{ENERGY_LEVELS[energy - 1].label}` closes EnergyControl (opened on line 12). Names declared inside that block end here.

  59 |         </span>
     | In `EnergyControl` (src/components/EnergyControl.jsx): Closes it. An inline box. Source: `</span>`

  60 |       </div>
     | In `EnergyControl` (src/components/EnergyControl.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  61 |     </div>
     | In `EnergyControl` (src/components/EnergyControl.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  62 |   );
     | In `EnergyControl` (src/components/EnergyControl.jsx): statement `);`. It runs when EnergyControl runs, in order, before the next line of the same function.

  63 | }
     | In `EnergyControl` (src/components/EnergyControl.jsx): `}` closes EnergyControl (opened on line 12). Names declared inside that block end here.

