# `src/stores/focusStore.ts`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import { create } from 'zustand'
     | Import for Zustand state for the unused focus hook: `import { create } from 'zustand'`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   2 | 
     | Blank line in `src/stores/focusStore.ts` (Zustand state for the unused focus hook), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   3 | interface FocusState {
     | In `the top of the file` (src/stores/focusStore.ts): statement `interface FocusState {`. It runs when the top of the file runs, in order, before the next line of the same function.

   4 |   isFocused: boolean
     | In `the top of the file` (src/stores/focusStore.ts): statement `isFocused: boolean`. It runs when the top of the file runs, in order, before the next line of the same function.

   5 |   focusLostAt: Date | null
     | In `the top of the file` (src/stores/focusStore.ts): statement `focusLostAt: Date | null`. It runs when the top of the file runs, in order, before the next line of the same function.

   6 |   setFocused: (v: boolean) => void
     | In `the top of the file` (src/stores/focusStore.ts): statement `setFocused: (v: boolean) => void`. It runs when the top of the file runs, in order, before the next line of the same function.

   7 | }
     | In `the top of the file` (src/stores/focusStore.ts): `}` closes interface FocusState { (opened on line 3). Names declared inside that block end here.

   8 | 
     | Blank line in `src/stores/focusStore.ts` (Zustand state for the unused focus hook), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   9 | export const useFocusStore = create<FocusState>((set) => ({
     | Named export from Zustand state for the unused focus hook: `export const useFocusStore = create<FocusState>((set) => ({`.

  10 |   isFocused: true,
     | In `the top of the file` (src/stores/focusStore.ts): statement `isFocused: true,`. It runs when the top of the file runs, in order, before the next line of the same function.

  11 |   focusLostAt: null,
     | In `the top of the file` (src/stores/focusStore.ts): statement `focusLostAt: null,`. It runs when the top of the file runs, in order, before the next line of the same function.

  12 |   setFocused: (isFocused) =>
     | In `the top of the file` (src/stores/focusStore.ts): statement `setFocused: (isFocused) =>`. It runs when the top of the file runs, in order, before the next line of the same function.

  13 |     set({ isFocused, focusLostAt: isFocused ? null : new Date() }),
     | In `the top of the file` (src/stores/focusStore.ts): `set({ isFocused, focusLostAt: isFocused ? null : new Date() }),` closes export const useFocusStore = create<FocusState>( (opened on line 9). Names declared inside that block end here.

  14 | }))
     | In `the top of the file` (src/stores/focusStore.ts): `}))` closes export const useFocusStore = create<FocusState>( (opened on line 9). Names declared inside that block end here.

