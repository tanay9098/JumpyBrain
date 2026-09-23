# `src/stores/blockingStore.ts`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import { create } from 'zustand'
     | Import for the shared Focus Shield rules object: `import { create } from 'zustand'`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   2 | 
     | Blank line in `src/stores/blockingStore.ts` (the shared Focus Shield rules object), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   3 | export interface BlockEntry {
     | Named export from the shared Focus Shield rules object: `export interface BlockEntry {`.

   4 |   _id?: string
     | In `the top of the file` (src/stores/blockingStore.ts): statement `_id?: string`. It runs when the top of the file runs, in order, before the next line of the same function.

   5 |   value: string
     | In `the top of the file` (src/stores/blockingStore.ts): statement `value: string`. It runs when the top of the file runs, in order, before the next line of the same function.

   6 |   label: string
     | In `the top of the file` (src/stores/blockingStore.ts): statement `label: string`. It runs when the top of the file runs, in order, before the next line of the same function.

   7 |   enabled?: boolean
     | In `the top of the file` (src/stores/blockingStore.ts): statement `enabled?: boolean`. It runs when the top of the file runs, in order, before the next line of the same function.

   8 |   notes?: string
     | In `the top of the file` (src/stores/blockingStore.ts): statement `notes?: string`. It runs when the top of the file runs, in order, before the next line of the same function.

   9 | }
     | In `the top of the file` (src/stores/blockingStore.ts): `}` closes export interface BlockEntry { (opened on line 3). Names declared inside that block end here.

  10 | 
     | Blank line in `src/stores/blockingStore.ts` (the shared Focus Shield rules object), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  11 | export interface BlockingSchedule {
     | Named export from the shared Focus Shield rules object: `export interface BlockingSchedule {`.

  12 |   enabled: boolean
     | In `the top of the file` (src/stores/blockingStore.ts): statement `enabled: boolean`. It runs when the top of the file runs, in order, before the next line of the same function.

  13 |   startTime: string
     | In `the top of the file` (src/stores/blockingStore.ts): statement `startTime: string`. It runs when the top of the file runs, in order, before the next line of the same function.

  14 |   endTime: string
     | In `the top of the file` (src/stores/blockingStore.ts): statement `endTime: string`. It runs when the top of the file runs, in order, before the next line of the same function.

  15 |   days: number[]
     | In `the top of the file` (src/stores/blockingStore.ts): statement `days: number[]`. It runs when the top of the file runs, in order, before the next line of the same function.

  16 | }
     | In `the top of the file` (src/stores/blockingStore.ts): `}` closes export interface BlockingSchedule { (opened on line 11). Names declared inside that block end here.

  17 | 
     | Blank line in `src/stores/blockingStore.ts` (the shared Focus Shield rules object), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  18 | export interface BlockingRules {
     | Named export from the shared Focus Shield rules object: `export interface BlockingRules {`.

  19 |   isEnabled: boolean
     | In `the top of the file` (src/stores/blockingStore.ts): statement `isEnabled: boolean`. It runs when the top of the file runs, in order, before the next line of the same function.

  20 |   blockedSites: BlockEntry[]
     | In `the top of the file` (src/stores/blockingStore.ts): statement `blockedSites: BlockEntry[]`. It runs when the top of the file runs, in order, before the next line of the same function.

  21 |   blockedApps: BlockEntry[]
     | In `the top of the file` (src/stores/blockingStore.ts): statement `blockedApps: BlockEntry[]`. It runs when the top of the file runs, in order, before the next line of the same function.

  22 |   whitelist: BlockEntry[]
     | In `the top of the file` (src/stores/blockingStore.ts): statement `whitelist: BlockEntry[]`. It runs when the top of the file runs, in order, before the next line of the same function.

  23 |   schedule: BlockingSchedule
     | In `the top of the file` (src/stores/blockingStore.ts): statement `schedule: BlockingSchedule`. It runs when the top of the file runs, in order, before the next line of the same function.

  24 |   pausedUntil?: string | null
     | In `the top of the file` (src/stores/blockingStore.ts): statement `pausedUntil?: string | null`. It runs when the top of the file runs, in order, before the next line of the same function.

  25 | }
     | In `the top of the file` (src/stores/blockingStore.ts): `}` closes export interface BlockingRules { (opened on line 18). Names declared inside that block end here.

  26 | 
     | Blank line in `src/stores/blockingStore.ts` (the shared Focus Shield rules object), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  27 | interface BlockingState {
     | In `the top of the file` (src/stores/blockingStore.ts): statement `interface BlockingState {`. It runs when the top of the file runs, in order, before the next line of the same function.

  28 |   rules: BlockingRules
     | In `the top of the file` (src/stores/blockingStore.ts): statement `rules: BlockingRules`. It runs when the top of the file runs, in order, before the next line of the same function.

  29 |   loading: boolean
     | In `the top of the file` (src/stores/blockingStore.ts): statement `loading: boolean`. It runs when the top of the file runs, in order, before the next line of the same function.

  30 |   saving: boolean
     | In `the top of the file` (src/stores/blockingStore.ts): statement `saving: boolean`. It runs when the top of the file runs, in order, before the next line of the same function.

  31 |   setRules: (rules: BlockingRules) => void
     | In `the top of the file` (src/stores/blockingStore.ts): statement `setRules: (rules: BlockingRules) => void`. It runs when the top of the file runs, in order, before the next line of the same function.

  32 |   setLoading: (v: boolean) => void
     | In `the top of the file` (src/stores/blockingStore.ts): statement `setLoading: (v: boolean) => void`. It runs when the top of the file runs, in order, before the next line of the same function.

  33 |   setSaving: (v: boolean) => void
     | In `the top of the file` (src/stores/blockingStore.ts): statement `setSaving: (v: boolean) => void`. It runs when the top of the file runs, in order, before the next line of the same function.

  34 | }
     | In `the top of the file` (src/stores/blockingStore.ts): `}` closes interface BlockingState { (opened on line 27). Names declared inside that block end here.

  35 | 
     | Blank line in `src/stores/blockingStore.ts` (the shared Focus Shield rules object), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  36 | const DEFAULT_RULES: BlockingRules = {
     | In `the top of the file` (src/stores/blockingStore.ts): declaration `const DEFAULT_RULES: BlockingRules = {`.

  37 |   isEnabled: false,
     | In `the top of the file` (src/stores/blockingStore.ts): statement `isEnabled: false,`. It runs when the top of the file runs, in order, before the next line of the same function.

  38 |   blockedSites: [],
     | In `the top of the file` (src/stores/blockingStore.ts): statement `blockedSites: [],`. It runs when the top of the file runs, in order, before the next line of the same function.

  39 |   blockedApps: [],
     | In `the top of the file` (src/stores/blockingStore.ts): statement `blockedApps: [],`. It runs when the top of the file runs, in order, before the next line of the same function.

  40 |   whitelist: [],
     | In `the top of the file` (src/stores/blockingStore.ts): statement `whitelist: [],`. It runs when the top of the file runs, in order, before the next line of the same function.

  41 |   schedule: {
     | In `the top of the file` (src/stores/blockingStore.ts): statement `schedule: {`. It runs when the top of the file runs, in order, before the next line of the same function.

  42 |     enabled: false,
     | In `the top of the file` (src/stores/blockingStore.ts): statement `enabled: false,`. It runs when the top of the file runs, in order, before the next line of the same function.

  43 |     startTime: '09:00',
     | In `the top of the file` (src/stores/blockingStore.ts): statement `startTime: '09:00',`. It runs when the top of the file runs, in order, before the next line of the same function.

  44 |     endTime: '17:00',
     | In `the top of the file` (src/stores/blockingStore.ts): statement `endTime: '17:00',`. It runs when the top of the file runs, in order, before the next line of the same function.

  45 |     days: [1, 2, 3, 4, 5],
     | In `the top of the file` (src/stores/blockingStore.ts): statement `days: [1, 2, 3, 4, 5],`. It runs when the top of the file runs, in order, before the next line of the same function.

  46 |   },
     | In `the top of the file` (src/stores/blockingStore.ts): `},` closes schedule: { (opened on line 41). Names declared inside that block end here.

  47 |   pausedUntil: null,
     | In `the top of the file` (src/stores/blockingStore.ts): statement `pausedUntil: null,`. It runs when the top of the file runs, in order, before the next line of the same function.

  48 | }
     | In `the top of the file` (src/stores/blockingStore.ts): `}` closes const DEFAULT_RULES: BlockingRules = { (opened on line 36). Names declared inside that block end here.

  49 | 
     | Blank line in `src/stores/blockingStore.ts` (the shared Focus Shield rules object), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  50 | export const useBlockingStore = create<BlockingState>((set) => ({
     | Named export from the shared Focus Shield rules object: `export const useBlockingStore = create<BlockingState>((set) => ({`.

  51 |   rules: DEFAULT_RULES,
     | In `the top of the file` (src/stores/blockingStore.ts): statement `rules: DEFAULT_RULES,`. It runs when the top of the file runs, in order, before the next line of the same function.

  52 |   loading: false,
     | In `the top of the file` (src/stores/blockingStore.ts): statement `loading: false,`. It runs when the top of the file runs, in order, before the next line of the same function.

  53 |   saving: false,
     | In `the top of the file` (src/stores/blockingStore.ts): statement `saving: false,`. It runs when the top of the file runs, in order, before the next line of the same function.

  54 |   setRules: (rules) => set({ rules }),
     | In `the top of the file` (src/stores/blockingStore.ts): statement `setRules: (rules) => set({ rules }),`. It runs when the top of the file runs, in order, before the next line of the same function.

  55 |   setLoading: (loading) => set({ loading }),
     | In `the top of the file` (src/stores/blockingStore.ts): statement `setLoading: (loading) => set({ loading }),`. It runs when the top of the file runs, in order, before the next line of the same function.

  56 |   setSaving: (saving) => set({ saving }),
     | In `the top of the file` (src/stores/blockingStore.ts): statement `setSaving: (saving) => set({ saving }),`. It runs when the top of the file runs, in order, before the next line of the same function.

  57 | }))
     | In `the top of the file` (src/stores/blockingStore.ts): `}))` closes export const useBlockingStore = create<BlockingS (opened on line 50). Names declared inside that block end here.

