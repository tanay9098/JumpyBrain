# `src/stores/uiStore.ts`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import { create } from 'zustand'
     | Borrows a shared notebook that any room can read.

   2 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   3 | interface UIState {
     | Inside the top of the file, this line runs as written: interface UIState {. It happens in order, after the line above it and before the line below it.

   4 |   sidebarOpen: boolean
     | Inside the top of the file, this line runs as written: sidebarOpen: boolean. It happens in order, after the line above it and before the line below it.

   5 |   activeModal: string | null
     | Inside the top of the file, this line runs as written: activeModal: string | null. It happens in order, after the line above it and before the line below it.

   6 |   toggleSidebar: () => void
     | Inside the top of the file, this line runs as written: toggleSidebar: () => void. It happens in order, after the line above it and before the line below it.

   7 |   openModal: (name: string) => void
     | Inside the top of the file, this line runs as written: openModal: (name: string) => void. It happens in order, after the line above it and before the line below it.

   8 |   closeModal: () => void
     | Inside the top of the file, this line runs as written: closeModal: () => void. It happens in order, after the line above it and before the line below it.

   9 | }
     | This ends interface UIState { (opened on line 3).

  10 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  11 | export const useUIStore = create<UIState>((set) => ({
     | This lets another file use this piece by its name.

  12 |   sidebarOpen: true,
     | Inside the top of the file, this line runs as written: sidebarOpen: true,. It happens in order, after the line above it and before the line below it.

  13 |   activeModal: null,
     | Inside the top of the file, this line runs as written: activeModal: null,. It happens in order, after the line above it and before the line below it.

  14 |   toggleSidebar: () => set((s) => ({ sidebarOpen: !s.sidebarOpen })),
     | This ends export const useUIStore = create<UIState>((set)  (opened on line 11).

  15 |   openModal: (name) => set({ activeModal: name }),
     | This ends export const useUIStore = create<UIState>((set)  (opened on line 11).

  16 |   closeModal: () => set({ activeModal: null }),
     | This ends export const useUIStore = create<UIState>((set)  (opened on line 11).

  17 | }))
     | This ends export const useUIStore = create<UIState>((set)  (opened on line 11).

