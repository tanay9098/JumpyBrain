# `src/contexts/EnergyContext.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import React, { createContext, useContext, useState } from "react";
     | Import for the 1–5 energy level shared by Home, the sidebar, and Tasks: `import React, { createContext, useContext, useState } from "react";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   2 | 
     | Blank line in `src/contexts/EnergyContext.jsx` (the 1–5 energy level shared by Home, the sidebar, and Tasks), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   3 | const EnergyContext = createContext();
     | In `the top of the file` (src/contexts/EnergyContext.jsx): `EnergyContext` is assigned `createContext();`. Later lines in this function read that name.

   4 | export const useEnergy = () => useContext(EnergyContext);
     | Named export from the 1–5 energy level shared by Home, the sidebar, and Tasks: `export const useEnergy = () => useContext(EnergyContext);`.

   5 | 
     | Blank line in `src/contexts/EnergyContext.jsx` (the 1–5 energy level shared by Home, the sidebar, and Tasks), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   6 | export function EnergyProvider({ children }) {
     | Named export from the 1–5 energy level shared by Home, the sidebar, and Tasks: `export function EnergyProvider({ children }) {`.

   7 |   const [energy, setEnergyState] = useState(() => {
     | In `EnergyProvider` (src/contexts/EnergyContext.jsx): `energy`: Integer 1–5 from EnergyContext, persisted as bb-energy. Home refetches 'what next' when it changes. TodoList rescores and refetches suggestions. The code is `const [energy, setEnergyState] = useState(() => {`.

   8 |     return parseInt(localStorage.getItem("bb-energy") || "3", 10);
     | In `EnergyProvider` (src/contexts/EnergyContext.jsx): return `return parseInt(localStorage.getItem("bb-energy") || "3", 10);`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

   9 |   });
     | In `EnergyProvider` (src/contexts/EnergyContext.jsx): `});` closes const [energy, setEnergyState] = useState(() =>  (opened on line 7). Names declared inside that block end here.

  10 | 
     | Blank line in `src/contexts/EnergyContext.jsx` (the 1–5 energy level shared by Home, the sidebar, and Tasks), inside EnergyProvider. The parser skips it. It separates the previous statement from the next so the function is readable.

  11 |   function setEnergy(level) {
     | Defines `setEnergy` in the 1–5 energy level shared by Home, the sidebar, and Tasks. Stores the level in React state and in localStorage bb-energy.

  12 |     setEnergyState(level);
     | In `setEnergy` (src/contexts/EnergyContext.jsx): statement `setEnergyState(level);`. It runs when setEnergy runs, in order, before the next line of the same function.

  13 |     localStorage.setItem("bb-energy", String(level));
     | In `setEnergy` (src/contexts/EnergyContext.jsx): browser storage — `localStorage.setItem("bb-energy", String(level));`. This survives reloads on this origin and is shared by any script that uses the same key.

  14 |   }
     | In `setEnergy` (src/contexts/EnergyContext.jsx): `}` closes setEnergy (opened on line 11). Names declared inside that block end here.

  15 | 
     | Blank line in `src/contexts/EnergyContext.jsx` (the 1–5 energy level shared by Home, the sidebar, and Tasks), inside EnergyProvider. The parser skips it. It separates the previous statement from the next so the function is readable.

  16 |   return (
     | In `EnergyProvider` (src/contexts/EnergyContext.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  17 |     <EnergyContext.Provider value={{ energy, setEnergy }}>
     | In `EnergyProvider` (src/contexts/EnergyContext.jsx): JSX `<EnergyContext.Provider>`. React will create this node when the parent renders.. value is controlled by React state, so the DOM shows that state Source: `<EnergyContext.Provider value={{ energy, setEnergy }}>`

  18 |       {children}
     | In `EnergyProvider` (src/contexts/EnergyContext.jsx): `{children}` closes EnergyProvider (opened on line 6). Names declared inside that block end here.

  19 |     </EnergyContext.Provider>
     | In `EnergyProvider` (src/contexts/EnergyContext.jsx): JSX `<EnergyContext.Provider>`. This closes that element. Source: `</EnergyContext.Provider>`

  20 |   );
     | In `EnergyProvider` (src/contexts/EnergyContext.jsx): statement `);`. It runs when EnergyProvider runs, in order, before the next line of the same function.

  21 | }
     | In `EnergyProvider` (src/contexts/EnergyContext.jsx): `}` closes EnergyProvider (opened on line 6). Names declared inside that block end here.

