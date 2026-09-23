# `src/components/EnergyControl.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import React from "react";
     | Borrows React so this file can remember things and draw the screen.

   2 | import { useEnergy } from "../contexts/EnergyContext";
     | This file borrows a tool another file already made.

   3 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   4 | const ENERGY_LEVELS = [
     | Five faces indexed 0–4, stored as levels 1–5: Exhausted, Low, Okay, Good, Peak. EnergyControl is the only writer; EnergyContext holds the number.

   5 |   { emoji: "💀", label: "Exhausted", color: "var(--muted)" },
     | This ends the nearest open block.

   6 |   { emoji: "😔", label: "Low",       color: "var(--blue)" },
     | This ends the nearest open block.

   7 |   { emoji: "😐", label: "Okay",      color: "var(--amber)" },
     | This ends the nearest open block.

   8 |   { emoji: "⚡", label: "Good",      color: "var(--green)" },
     | This ends the nearest open block.

   9 |   { emoji: "🔥", label: "Peak",      color: "var(--violet-light)" },
     | This ends the nearest open block.

  10 | ];
     | Inside the top of the file, this line runs as written: ];. It happens in order, after the line above it and before the line below it.

  11 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  12 | export default function EnergyControl({ compact = false }) {
     | This starts EnergyControl. Reads and writes EnergyContext. compact=true is the five dots in the sidebar. Otherwise the big emoji buttons on Today.

  13 |   const { energy, setEnergy } = useEnergy();
     | Integer 1–5 from EnergyContext, persisted as bb-energy. Home refetches 'what next' when it changes. TodoList rescores and refetches suggestions.

  14 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  15 |   if (compact) {
     | This asks a yes-or-no question. The next bit runs only on yes.

  16 |     return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  17 |       <div className="energy-control-compact">
     | This draws one piece of the page while EnergyControl is showing.

  18 |         {ENERGY_LEVELS.map((lvl, i) => {
     | Inside EnergyControl, this line runs as written: {ENERGY_LEVELS.map((lvl, i) => {. It happens in order, after the line above it and before the line below it.

  19 |           const n = i + 1;
     | This gives a short name to a value so the rest of EnergyControl can use it.

  20 |           return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  21 |             <button
     | This draws one piece of the page while EnergyControl is showing.

  22 |               key={n}
     | This ends {ENERGY_LEVELS.map((lvl, i) => { (opened on line 18).

  23 |               className={`energy-dot ${n <= energy ? "filled" : ""}`}
     | This ends {ENERGY_LEVELS.map((lvl, i) => { (opened on line 18).

  24 |               onClick={() => setEnergy(n)}
     | This decides what happens when you press.

  25 |               title={`${lvl.emoji} ${lvl.label}`}
     | This ends {ENERGY_LEVELS.map((lvl, i) => { (opened on line 18).

  26 |               aria-label={`Set energy to ${lvl.label}`}
     | This ends {ENERGY_LEVELS.map((lvl, i) => { (opened on line 18).

  27 |               aria-pressed={n === energy}
     | This ends {ENERGY_LEVELS.map((lvl, i) => { (opened on line 18).

  28 |               style={n <= energy ? { borderColor: ENERGY_LEVELS[energy - 1].color, background: ENERGY_LEVELS[energy - 1].color + "25" } : {}}
     | This ends {ENERGY_LEVELS.map((lvl, i) => { (opened on line 18).

  29 |             >
     | Inside EnergyControl, this line runs as written: >. It happens in order, after the line above it and before the line below it.

  30 |               {n <= energy ? lvl.emoji : ""}
     | This ends {ENERGY_LEVELS.map((lvl, i) => { (opened on line 18).

  31 |             </button>
     | This ends a drawing that EnergyControl started just above.

  32 |           );
     | This closes a box of instructions that opened above.

  33 |         })}
     | This ends {ENERGY_LEVELS.map((lvl, i) => { (opened on line 18).

  34 |       </div>
     | This ends a drawing that EnergyControl started just above.

  35 |     );
     | This closes a box of instructions that opened above.

  36 |   }
     | This ends if (compact) { (opened on line 15).

  37 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  38 |   return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  39 |     <div className="energy-control">
     | This draws one piece of the page while EnergyControl is showing.

  40 |       <div className="energy-control-row">
     | This draws one piece of the page while EnergyControl is showing.

  41 |         {ENERGY_LEVELS.map((lvl, i) => {
     | Inside EnergyControl, this line runs as written: {ENERGY_LEVELS.map((lvl, i) => {. It happens in order, after the line above it and before the line below it.

  42 |           const n = i + 1;
     | This gives a short name to a value so the rest of EnergyControl can use it.

  43 |           const isSelected = energy === n;
     | This gives a short name to a value so the rest of EnergyControl can use it.

  44 |           return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  45 |             <button
     | This draws one piece of the page while EnergyControl is showing.

  46 |               key={n}
     | This ends {ENERGY_LEVELS.map((lvl, i) => { (opened on line 41).

  47 |               className={`energy-btn ${isSelected ? "selected" : ""}`}
     | This ends {ENERGY_LEVELS.map((lvl, i) => { (opened on line 41).

  48 |               onClick={() => setEnergy(n)}
     | This decides what happens when you press.

  49 |               title={`${lvl.emoji} ${lvl.label}`}
     | This ends {ENERGY_LEVELS.map((lvl, i) => { (opened on line 41).

  50 |               aria-label={`Set energy to ${lvl.label}`}
     | This ends {ENERGY_LEVELS.map((lvl, i) => { (opened on line 41).

  51 |               aria-pressed={isSelected}
     | This ends {ENERGY_LEVELS.map((lvl, i) => { (opened on line 41).

  52 |             >
     | Inside EnergyControl, this line runs as written: >. It happens in order, after the line above it and before the line below it.

  53 |               {lvl.emoji}
     | This ends {ENERGY_LEVELS.map((lvl, i) => { (opened on line 41).

  54 |             </button>
     | This ends a drawing that EnergyControl started just above.

  55 |           );
     | This closes a box of instructions that opened above.

  56 |         })}
     | This ends {ENERGY_LEVELS.map((lvl, i) => { (opened on line 41).

  57 |         <span className="energy-current-label">
     | This draws one piece of the page while EnergyControl is showing.

  58 |           {ENERGY_LEVELS[energy - 1].label}
     | This ends EnergyControl (opened on line 12).

  59 |         </span>
     | This ends a drawing that EnergyControl started just above.

  60 |       </div>
     | This ends a drawing that EnergyControl started just above.

  61 |     </div>
     | This ends a drawing that EnergyControl started just above.

  62 |   );
     | This closes a box of instructions that opened above.

  63 | }
     | This ends EnergyControl (opened on line 12).

