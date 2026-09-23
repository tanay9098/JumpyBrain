# `src/contexts/EnergyContext.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import React, { createContext, useContext, useState } from "react";
     | Borrows React so this file can remember things and draw the screen.

   2 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   3 | const EnergyContext = createContext();
     | This gives a short name to a value so the rest of the top of the file can use it.

   4 | export const useEnergy = () => useContext(EnergyContext);
     | This lets another file use this piece by its name.

   5 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   6 | export function EnergyProvider({ children }) {
     | This lets another file use this piece by its name.

   7 |   const [energy, setEnergyState] = useState(() => {
     | Integer 1–5 from EnergyContext, persisted as bb-energy. Home refetches 'what next' when it changes. TodoList rescores and refetches suggestions.

   8 |     return parseInt(localStorage.getItem("bb-energy") || "3", 10);
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

   9 |   });
     | This ends const [energy, setEnergyState] = useState(() =>  (opened on line 7).

  10 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  11 |   function setEnergy(level) {
     | This starts setEnergy. Stores the level in React state and in localStorage bb-energy.

  12 |     setEnergyState(level);
     | Inside setEnergy, this line runs as written: setEnergyState(level);. It happens in order, after the line above it and before the line below it.

  13 |     localStorage.setItem("bb-energy", String(level));
     | This looks in the browser's pocket, or puts something there, so it is still around after a refresh.

  14 |   }
     | This ends setEnergy (opened on line 11).

  15 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  16 |   return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  17 |     <EnergyContext.Provider value={{ energy, setEnergy }}>
     | This draws one piece of the page while EnergyProvider is showing.

  18 |       {children}
     | This ends EnergyProvider (opened on line 6).

  19 |     </EnergyContext.Provider>
     | This ends a drawing that EnergyProvider started just above.

  20 |   );
     | This closes a box of instructions that opened above.

  21 | }
     | This ends EnergyProvider (opened on line 6).

