# `src/stores/timerStore.ts`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import { create } from 'zustand'
     | Import for Zustand state for the unused timer hook: `import { create } from 'zustand'`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   2 | 
     | Blank line in `src/stores/timerStore.ts` (Zustand state for the unused timer hook), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   3 | interface TimerState {
     | In `the top of the file` (src/stores/timerStore.ts): statement `interface TimerState {`. It runs when the top of the file runs, in order, before the next line of the same function.

   4 |   isRunning: boolean
     | In `the top of the file` (src/stores/timerStore.ts): statement `isRunning: boolean`. It runs when the top of the file runs, in order, before the next line of the same function.

   5 |   elapsed: number
     | In `the top of the file` (src/stores/timerStore.ts): statement `elapsed: number`. It runs when the top of the file runs, in order, before the next line of the same function.

   6 |   mode: 'pomodoro' | 'deep' | 'deadline'
     | In `the top of the file` (src/stores/timerStore.ts): statement `mode: 'pomodoro' | 'deep' | 'deadline'`. It runs when the top of the file runs, in order, before the next line of the same function.

   7 |   sessionId: string | null
     | In `the top of the file` (src/stores/timerStore.ts): statement `sessionId: string | null`. It runs when the top of the file runs, in order, before the next line of the same function.

   8 |   start: (mode: TimerState['mode']) => void
     | In `the top of the file` (src/stores/timerStore.ts): statement `start: (mode: TimerState['mode']) => void`. It runs when the top of the file runs, in order, before the next line of the same function.

   9 |   pause: () => void
     | In `the top of the file` (src/stores/timerStore.ts): statement `pause: () => void`. It runs when the top of the file runs, in order, before the next line of the same function.

  10 |   reset: () => void
     | In `the top of the file` (src/stores/timerStore.ts): statement `reset: () => void`. It runs when the top of the file runs, in order, before the next line of the same function.

  11 |   tick: () => void
     | In `the top of the file` (src/stores/timerStore.ts): statement `tick: () => void`. It runs when the top of the file runs, in order, before the next line of the same function.

  12 |   setSessionId: (id: string) => void
     | In `the top of the file` (src/stores/timerStore.ts): statement `setSessionId: (id: string) => void`. It runs when the top of the file runs, in order, before the next line of the same function.

  13 | }
     | In `the top of the file` (src/stores/timerStore.ts): `}` closes interface TimerState { (opened on line 3). Names declared inside that block end here.

  14 | 
     | Blank line in `src/stores/timerStore.ts` (Zustand state for the unused timer hook), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  15 | export const useTimerStore = create<TimerState>((set) => ({
     | Named export from Zustand state for the unused timer hook: `export const useTimerStore = create<TimerState>((set) => ({`.

  16 |   isRunning: false,
     | In `the top of the file` (src/stores/timerStore.ts): statement `isRunning: false,`. It runs when the top of the file runs, in order, before the next line of the same function.

  17 |   elapsed: 0,
     | In `the top of the file` (src/stores/timerStore.ts): statement `elapsed: 0,`. It runs when the top of the file runs, in order, before the next line of the same function.

  18 |   mode: 'pomodoro',
     | In `the top of the file` (src/stores/timerStore.ts): statement `mode: 'pomodoro',`. It runs when the top of the file runs, in order, before the next line of the same function.

  19 |   sessionId: null,
     | In `the top of the file` (src/stores/timerStore.ts): statement `sessionId: null,`. It runs when the top of the file runs, in order, before the next line of the same function.

  20 |   start: (mode) => set({ isRunning: true, mode }),
     | In `the top of the file` (src/stores/timerStore.ts): statement `start: (mode) => set({ isRunning: true, mode }),`. It runs when the top of the file runs, in order, before the next line of the same function.

  21 |   pause: () => set({ isRunning: false }),
     | In `the top of the file` (src/stores/timerStore.ts): statement `pause: () => set({ isRunning: false }),`. It runs when the top of the file runs, in order, before the next line of the same function.

  22 |   reset: () => set({ isRunning: false, elapsed: 0, sessionId: null }),
     | In `the top of the file` (src/stores/timerStore.ts): statement `reset: () => set({ isRunning: false, elapsed: 0, sessionId: null }),`. It runs when the top of the file runs, in order, before the next line of the same function.

  23 |   tick: () => set((s) => ({ elapsed: s.elapsed + 1 })),
     | In `the top of the file` (src/stores/timerStore.ts): statement `tick: () => set((s) => ({ elapsed: s.elapsed + 1 })),`. It runs when the top of the file runs, in order, before the next line of the same function.

  24 |   setSessionId: (id) => set({ sessionId: id }),
     | In `the top of the file` (src/stores/timerStore.ts): statement `setSessionId: (id) => set({ sessionId: id }),`. It runs when the top of the file runs, in order, before the next line of the same function.

  25 | }))
     | In `the top of the file` (src/stores/timerStore.ts): `}))` closes export const useTimerStore = create<TimerState>( (opened on line 15). Names declared inside that block end here.

