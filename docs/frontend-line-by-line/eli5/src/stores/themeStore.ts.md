# `src/stores/themeStore.ts`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import { create } from 'zustand'
     | Borrows a shared notebook that any room can read.

   2 | import { persist } from 'zustand/middleware'
     | Borrows a shared notebook that any room can read.

   3 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   4 | export type ThemeName = 'calm' | 'focus' | 'night' | 'highContrast' | 'minimal'
     | This lets another file use this piece by its name.

   5 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   6 | interface ThemeState {
     | Inside the top of the file, this line runs as written: interface ThemeState {. It happens in order, after the line above it and before the line below it.

   7 |   theme: ThemeName
     | Inside the top of the file, this line runs as written: theme: ThemeName. It happens in order, after the line above it and before the line below it.

   8 |   setTheme: (theme: ThemeName) => void
     | Inside the top of the file, this line runs as written: setTheme: (theme: ThemeName) => void. It happens in order, after the line above it and before the line below it.

   9 | }
     | This ends interface ThemeState { (opened on line 6).

  10 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  11 | export const useThemeStore = create<ThemeState>()(
     | This lets another file use this piece by its name.

  12 |   persist(
     | Inside the top of the file, this line runs as written: persist(. It happens in order, after the line above it and before the line below it.

  13 |     (set) => ({
     | Inside the top of the file, this line runs as written: (set) => ({. It happens in order, after the line above it and before the line below it.

  14 |       theme: 'calm',
     | Inside the top of the file, this line runs as written: theme: 'calm',. It happens in order, after the line above it and before the line below it.

  15 |       setTheme: (theme) => set({ theme }),
     | This ends (set) => ({ (opened on line 13).

  16 |     }),
     | This ends (set) => ({ (opened on line 13).

  17 |     { name: 'bb-theme' }
     | This ends the nearest open block.

  18 |   )
     | This closes a box of instructions that opened above.

  19 | )
     | This closes a box of instructions that opened above.

