# `src/stores/blockingStore.ts`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import { create } from 'zustand'
     | Borrows a shared notebook that any room can read.

   2 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   3 | export interface BlockEntry {
     | This lets another file use this piece by its name.

   4 |   _id?: string
     | Inside the top of the file, this line runs as written: _id?: string. It happens in order, after the line above it and before the line below it.

   5 |   value: string
     | Inside the top of the file, this line runs as written: value: string. It happens in order, after the line above it and before the line below it.

   6 |   label: string
     | Inside the top of the file, this line runs as written: label: string. It happens in order, after the line above it and before the line below it.

   7 |   enabled?: boolean
     | Inside the top of the file, this line runs as written: enabled?: boolean. It happens in order, after the line above it and before the line below it.

   8 |   notes?: string
     | Inside the top of the file, this line runs as written: notes?: string. It happens in order, after the line above it and before the line below it.

   9 | }
     | This ends export interface BlockEntry { (opened on line 3).

  10 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  11 | export interface BlockingSchedule {
     | This lets another file use this piece by its name.

  12 |   enabled: boolean
     | Inside the top of the file, this line runs as written: enabled: boolean. It happens in order, after the line above it and before the line below it.

  13 |   startTime: string
     | Inside the top of the file, this line runs as written: startTime: string. It happens in order, after the line above it and before the line below it.

  14 |   endTime: string
     | Inside the top of the file, this line runs as written: endTime: string. It happens in order, after the line above it and before the line below it.

  15 |   days: number[]
     | Inside the top of the file, this line runs as written: days: number[]. It happens in order, after the line above it and before the line below it.

  16 | }
     | This ends export interface BlockingSchedule { (opened on line 11).

  17 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  18 | export interface BlockingRules {
     | This lets another file use this piece by its name.

  19 |   isEnabled: boolean
     | Inside the top of the file, this line runs as written: isEnabled: boolean. It happens in order, after the line above it and before the line below it.

  20 |   blockedSites: BlockEntry[]
     | Inside the top of the file, this line runs as written: blockedSites: BlockEntry[]. It happens in order, after the line above it and before the line below it.

  21 |   blockedApps: BlockEntry[]
     | Inside the top of the file, this line runs as written: blockedApps: BlockEntry[]. It happens in order, after the line above it and before the line below it.

  22 |   whitelist: BlockEntry[]
     | Inside the top of the file, this line runs as written: whitelist: BlockEntry[]. It happens in order, after the line above it and before the line below it.

  23 |   schedule: BlockingSchedule
     | Inside the top of the file, this line runs as written: schedule: BlockingSchedule. It happens in order, after the line above it and before the line below it.

  24 |   pausedUntil?: string | null
     | Inside the top of the file, this line runs as written: pausedUntil?: string | null. It happens in order, after the line above it and before the line below it.

  25 | }
     | This ends export interface BlockingRules { (opened on line 18).

  26 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  27 | interface BlockingState {
     | Inside the top of the file, this line runs as written: interface BlockingState {. It happens in order, after the line above it and before the line below it.

  28 |   rules: BlockingRules
     | Inside the top of the file, this line runs as written: rules: BlockingRules. It happens in order, after the line above it and before the line below it.

  29 |   loading: boolean
     | Inside the top of the file, this line runs as written: loading: boolean. It happens in order, after the line above it and before the line below it.

  30 |   saving: boolean
     | Inside the top of the file, this line runs as written: saving: boolean. It happens in order, after the line above it and before the line below it.

  31 |   setRules: (rules: BlockingRules) => void
     | Inside the top of the file, this line runs as written: setRules: (rules: BlockingRules) => void. It happens in order, after the line above it and before the line below it.

  32 |   setLoading: (v: boolean) => void
     | Inside the top of the file, this line runs as written: setLoading: (v: boolean) => void. It happens in order, after the line above it and before the line below it.

  33 |   setSaving: (v: boolean) => void
     | Inside the top of the file, this line runs as written: setSaving: (v: boolean) => void. It happens in order, after the line above it and before the line below it.

  34 | }
     | This ends interface BlockingState { (opened on line 27).

  35 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  36 | const DEFAULT_RULES: BlockingRules = {
     | Shield off, empty lists, weekdays 09:00–17:00, not paused. blockingStore starts here until GET /blocking returns.

  37 |   isEnabled: false,
     | Inside the top of the file, this line runs as written: isEnabled: false,. It happens in order, after the line above it and before the line below it.

  38 |   blockedSites: [],
     | Inside the top of the file, this line runs as written: blockedSites: [],. It happens in order, after the line above it and before the line below it.

  39 |   blockedApps: [],
     | Inside the top of the file, this line runs as written: blockedApps: [],. It happens in order, after the line above it and before the line below it.

  40 |   whitelist: [],
     | Inside the top of the file, this line runs as written: whitelist: [],. It happens in order, after the line above it and before the line below it.

  41 |   schedule: {
     | Inside the top of the file, this line runs as written: schedule: {. It happens in order, after the line above it and before the line below it.

  42 |     enabled: false,
     | Inside the top of the file, this line runs as written: enabled: false,. It happens in order, after the line above it and before the line below it.

  43 |     startTime: '09:00',
     | Inside the top of the file, this line runs as written: startTime: '09:00',. It happens in order, after the line above it and before the line below it.

  44 |     endTime: '17:00',
     | Inside the top of the file, this line runs as written: endTime: '17:00',. It happens in order, after the line above it and before the line below it.

  45 |     days: [1, 2, 3, 4, 5],
     | Inside the top of the file, this line runs as written: days: [1, 2, 3, 4, 5],. It happens in order, after the line above it and before the line below it.

  46 |   },
     | This ends schedule: { (opened on line 41).

  47 |   pausedUntil: null,
     | Inside the top of the file, this line runs as written: pausedUntil: null,. It happens in order, after the line above it and before the line below it.

  48 | }
     | This ends const DEFAULT_RULES: BlockingRules = { (opened on line 36).

  49 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  50 | export const useBlockingStore = create<BlockingState>((set) => ({
     | This lets another file use this piece by its name.

  51 |   rules: DEFAULT_RULES,
     | Inside the top of the file, this line runs as written: rules: DEFAULT_RULES,. It happens in order, after the line above it and before the line below it.

  52 |   loading: false,
     | Inside the top of the file, this line runs as written: loading: false,. It happens in order, after the line above it and before the line below it.

  53 |   saving: false,
     | Inside the top of the file, this line runs as written: saving: false,. It happens in order, after the line above it and before the line below it.

  54 |   setRules: (rules) => set({ rules }),
     | This ends export const useBlockingStore = create<BlockingS (opened on line 50).

  55 |   setLoading: (loading) => set({ loading }),
     | This ends export const useBlockingStore = create<BlockingS (opened on line 50).

  56 |   setSaving: (saving) => set({ saving }),
     | This ends export const useBlockingStore = create<BlockingS (opened on line 50).

  57 | }))
     | This ends export const useBlockingStore = create<BlockingS (opened on line 50).

