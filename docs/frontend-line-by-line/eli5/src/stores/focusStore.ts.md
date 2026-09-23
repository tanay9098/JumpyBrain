# `src/stores/focusStore.ts`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import { create } from 'zustand'
     | Borrows a shared notebook that any room can read.

   2 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   3 | interface FocusState {
     | Inside the top of the file, this line runs as written: interface FocusState {. It happens in order, after the line above it and before the line below it.

   4 |   isFocused: boolean
     | Inside the top of the file, this line runs as written: isFocused: boolean. It happens in order, after the line above it and before the line below it.

   5 |   focusLostAt: Date | null
     | Inside the top of the file, this line runs as written: focusLostAt: Date | null. It happens in order, after the line above it and before the line below it.

   6 |   setFocused: (v: boolean) => void
     | Inside the top of the file, this line runs as written: setFocused: (v: boolean) => void. It happens in order, after the line above it and before the line below it.

   7 | }
     | This ends interface FocusState { (opened on line 3).

   8 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   9 | export const useFocusStore = create<FocusState>((set) => ({
     | This lets another file use this piece by its name.

  10 |   isFocused: true,
     | Inside the top of the file, this line runs as written: isFocused: true,. It happens in order, after the line above it and before the line below it.

  11 |   focusLostAt: null,
     | Inside the top of the file, this line runs as written: focusLostAt: null,. It happens in order, after the line above it and before the line below it.

  12 |   setFocused: (isFocused) =>
     | Inside the top of the file, this line runs as written: setFocused: (isFocused) =>. It happens in order, after the line above it and before the line below it.

  13 |     set({ isFocused, focusLostAt: isFocused ? null : new Date() }),
     | This ends export const useFocusStore = create<FocusState>( (opened on line 9).

  14 | }))
     | This ends export const useFocusStore = create<FocusState>( (opened on line 9).

