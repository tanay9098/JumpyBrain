# `src/stores/uiStore.ts`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import { create } from 'zustand'
     | Import for Zustand sidebar/modal state that App.jsx does not read: `import { create } from 'zustand'`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   2 | 
     | Blank line in `src/stores/uiStore.ts` (Zustand sidebar/modal state that App.jsx does not read), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   3 | interface UIState {
     | In `the top of the file` (src/stores/uiStore.ts): statement `interface UIState {`. It runs when the top of the file runs, in order, before the next line of the same function.

   4 |   sidebarOpen: boolean
     | In `the top of the file` (src/stores/uiStore.ts): statement `sidebarOpen: boolean`. It runs when the top of the file runs, in order, before the next line of the same function.

   5 |   activeModal: string | null
     | In `the top of the file` (src/stores/uiStore.ts): statement `activeModal: string | null`. It runs when the top of the file runs, in order, before the next line of the same function.

   6 |   toggleSidebar: () => void
     | In `the top of the file` (src/stores/uiStore.ts): statement `toggleSidebar: () => void`. It runs when the top of the file runs, in order, before the next line of the same function.

   7 |   openModal: (name: string) => void
     | In `the top of the file` (src/stores/uiStore.ts): statement `openModal: (name: string) => void`. It runs when the top of the file runs, in order, before the next line of the same function.

   8 |   closeModal: () => void
     | In `the top of the file` (src/stores/uiStore.ts): statement `closeModal: () => void`. It runs when the top of the file runs, in order, before the next line of the same function.

   9 | }
     | In `the top of the file` (src/stores/uiStore.ts): `}` closes interface UIState { (opened on line 3). Names declared inside that block end here.

  10 | 
     | Blank line in `src/stores/uiStore.ts` (Zustand sidebar/modal state that App.jsx does not read), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  11 | export const useUIStore = create<UIState>((set) => ({
     | Named export from Zustand sidebar/modal state that App.jsx does not read: `export const useUIStore = create<UIState>((set) => ({`.

  12 |   sidebarOpen: true,
     | In `the top of the file` (src/stores/uiStore.ts): statement `sidebarOpen: true,`. It runs when the top of the file runs, in order, before the next line of the same function.

  13 |   activeModal: null,
     | In `the top of the file` (src/stores/uiStore.ts): statement `activeModal: null,`. It runs when the top of the file runs, in order, before the next line of the same function.

  14 |   toggleSidebar: () => set((s) => ({ sidebarOpen: !s.sidebarOpen })),
     | In `the top of the file` (src/stores/uiStore.ts): statement `toggleSidebar: () => set((s) => ({ sidebarOpen: !s.sidebarOpen })),`. It runs when the top of the file runs, in order, before the next line of the same function.

  15 |   openModal: (name) => set({ activeModal: name }),
     | In `the top of the file` (src/stores/uiStore.ts): statement `openModal: (name) => set({ activeModal: name }),`. It runs when the top of the file runs, in order, before the next line of the same function.

  16 |   closeModal: () => set({ activeModal: null }),
     | In `the top of the file` (src/stores/uiStore.ts): statement `closeModal: () => set({ activeModal: null }),`. It runs when the top of the file runs, in order, before the next line of the same function.

  17 | }))
     | In `the top of the file` (src/stores/uiStore.ts): `}))` closes export const useUIStore = create<UIState>((set)  (opened on line 11). Names declared inside that block end here.

