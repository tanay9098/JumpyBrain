# `src/stores/timerStore.ts`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import { create } from 'zustand'
     | Borrows a shared notebook that any room can read.

   2 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   3 | interface TimerState {
     | Inside the top of the file, this line runs as written: interface TimerState {. It happens in order, after the line above it and before the line below it.

   4 |   isRunning: boolean
     | Inside the top of the file, this line runs as written: isRunning: boolean. It happens in order, after the line above it and before the line below it.

   5 |   elapsed: number
     | Inside the top of the file, this line runs as written: elapsed: number. It happens in order, after the line above it and before the line below it.

   6 |   mode: 'pomodoro' | 'deep' | 'deadline'
     | Inside the top of the file, this line runs as written: mode: 'pomodoro' | 'deep' | 'deadline'. It happens in order, after the line above it and before the line below it.

   7 |   sessionId: string | null
     | Inside the top of the file, this line runs as written: sessionId: string | null. It happens in order, after the line above it and before the line below it.

   8 |   start: (mode: TimerState['mode']) => void
     | Inside the top of the file, this line runs as written: start: (mode: TimerState['mode']) => void. It happens in order, after the line above it and before the line below it.

   9 |   pause: () => void
     | Inside the top of the file, this line runs as written: pause: () => void. It happens in order, after the line above it and before the line below it.

  10 |   reset: () => void
     | Inside the top of the file, this line runs as written: reset: () => void. It happens in order, after the line above it and before the line below it.

  11 |   tick: () => void
     | Inside the top of the file, this line runs as written: tick: () => void. It happens in order, after the line above it and before the line below it.

  12 |   setSessionId: (id: string) => void
     | Inside the top of the file, this line runs as written: setSessionId: (id: string) => void. It happens in order, after the line above it and before the line below it.

  13 | }
     | This ends interface TimerState { (opened on line 3).

  14 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  15 | export const useTimerStore = create<TimerState>((set) => ({
     | This lets another file use this piece by its name.

  16 |   isRunning: false,
     | Inside the top of the file, this line runs as written: isRunning: false,. It happens in order, after the line above it and before the line below it.

  17 |   elapsed: 0,
     | Inside the top of the file, this line runs as written: elapsed: 0,. It happens in order, after the line above it and before the line below it.

  18 |   mode: 'pomodoro',
     | Inside the top of the file, this line runs as written: mode: 'pomodoro',. It happens in order, after the line above it and before the line below it.

  19 |   sessionId: null,
     | Inside the top of the file, this line runs as written: sessionId: null,. It happens in order, after the line above it and before the line below it.

  20 |   start: (mode) => set({ isRunning: true, mode }),
     | This ends export const useTimerStore = create<TimerState>( (opened on line 15).

  21 |   pause: () => set({ isRunning: false }),
     | This ends export const useTimerStore = create<TimerState>( (opened on line 15).

  22 |   reset: () => set({ isRunning: false, elapsed: 0, sessionId: null }),
     | This ends export const useTimerStore = create<TimerState>( (opened on line 15).

  23 |   tick: () => set((s) => ({ elapsed: s.elapsed + 1 })),
     | This ends export const useTimerStore = create<TimerState>( (opened on line 15).

  24 |   setSessionId: (id) => set({ sessionId: id }),
     | This ends export const useTimerStore = create<TimerState>( (opened on line 15).

  25 | }))
     | This ends export const useTimerStore = create<TimerState>( (opened on line 15).

