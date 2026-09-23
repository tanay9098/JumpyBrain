# `src/plugins/AppBlocker.ts`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import { registerPlugin } from '@capacitor/core';
     | Import for the Capacitor bridge to native app blocking: `import { registerPlugin } from '@capacitor/core';`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   2 | 
     | Blank line in `src/plugins/AppBlocker.ts` (the Capacitor bridge to native app blocking), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   3 | export type PermissionState = 'granted' | 'denied' | 'prompt';
     | Named export from the Capacitor bridge to native app blocking: `export type PermissionState = 'granted' | 'denied' | 'prompt';`.

   4 | 
     | Blank line in `src/plugins/AppBlocker.ts` (the Capacitor bridge to native app blocking), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   5 | export interface AppBlockerPermissions {
     | Named export from the Capacitor bridge to native app blocking: `export interface AppBlockerPermissions {`.

   6 |   usageStats: PermissionState;     // Android — PACKAGE_USAGE_STATS
     | In `the top of the file` (src/plugins/AppBlocker.ts): statement `usageStats: PermissionState;     // Android — PACKAGE_USAGE_STATS`. It runs when the top of the file runs, in order, before the next line of the same function.

   7 |   accessibility: PermissionState;  // Android — AccessibilityService enabled
     | In `the top of the file` (src/plugins/AppBlocker.ts): statement `accessibility: PermissionState;  // Android — AccessibilityService enabled`. It runs when the top of the file runs, in order, before the next line of the same function.

   8 |   familyControls: PermissionState; // iOS    — FamilyControls authorization
     | In `the top of the file` (src/plugins/AppBlocker.ts): statement `familyControls: PermissionState; // iOS    — FamilyControls authorization`. It runs when the top of the file runs, in order, before the next line of the same function.

   9 | }
     | In `the top of the file` (src/plugins/AppBlocker.ts): `}` closes export interface AppBlockerPermissions { (opened on line 5). Names declared inside that block end here.

  10 | 
     | Blank line in `src/plugins/AppBlocker.ts` (the Capacitor bridge to native app blocking), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  11 | export interface BlockEntry {
     | Named export from the Capacitor bridge to native app blocking: `export interface BlockEntry {`.

  12 |   value: string;
     | In `the top of the file` (src/plugins/AppBlocker.ts): statement `value: string;`. It runs when the top of the file runs, in order, before the next line of the same function.

  13 |   label?: string;
     | In `the top of the file` (src/plugins/AppBlocker.ts): statement `label?: string;`. It runs when the top of the file runs, in order, before the next line of the same function.

  14 | }
     | In `the top of the file` (src/plugins/AppBlocker.ts): `}` closes export interface BlockEntry { (opened on line 11). Names declared inside that block end here.

  15 | 
     | Blank line in `src/plugins/AppBlocker.ts` (the Capacitor bridge to native app blocking), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  16 | export interface BlockingSchedule {
     | Named export from the Capacitor bridge to native app blocking: `export interface BlockingSchedule {`.

  17 |   enabled: boolean;
     | In `the top of the file` (src/plugins/AppBlocker.ts): statement `enabled: boolean;`. It runs when the top of the file runs, in order, before the next line of the same function.

  18 |   startTime: string; // "HH:MM"
     | In `the top of the file` (src/plugins/AppBlocker.ts): statement `startTime: string; // "HH:MM"`. It runs when the top of the file runs, in order, before the next line of the same function.

  19 |   endTime: string;   // "HH:MM"
     | In `the top of the file` (src/plugins/AppBlocker.ts): statement `endTime: string;   // "HH:MM"`. It runs when the top of the file runs, in order, before the next line of the same function.

  20 |   days: number[];    // 0=Sun … 6=Sat
     | In `the top of the file` (src/plugins/AppBlocker.ts): statement `days: number[];    // 0=Sun … 6=Sat`. It runs when the top of the file runs, in order, before the next line of the same function.

  21 | }
     | In `the top of the file` (src/plugins/AppBlocker.ts): `}` closes export interface BlockingSchedule { (opened on line 16). Names declared inside that block end here.

  22 | 
     | Blank line in `src/plugins/AppBlocker.ts` (the Capacitor bridge to native app blocking), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  23 | export interface BlockingRules {
     | Named export from the Capacitor bridge to native app blocking: `export interface BlockingRules {`.

  24 |   isEnabled: boolean;
     | In `the top of the file` (src/plugins/AppBlocker.ts): statement `isEnabled: boolean;`. It runs when the top of the file runs, in order, before the next line of the same function.

  25 |   blockedApps: BlockEntry[];
     | In `the top of the file` (src/plugins/AppBlocker.ts): statement `blockedApps: BlockEntry[];`. It runs when the top of the file runs, in order, before the next line of the same function.

  26 |   blockedSites: BlockEntry[];
     | In `the top of the file` (src/plugins/AppBlocker.ts): statement `blockedSites: BlockEntry[];`. It runs when the top of the file runs, in order, before the next line of the same function.

  27 |   whitelist: BlockEntry[];
     | In `the top of the file` (src/plugins/AppBlocker.ts): statement `whitelist: BlockEntry[];`. It runs when the top of the file runs, in order, before the next line of the same function.

  28 |   schedule: BlockingSchedule;
     | In `the top of the file` (src/plugins/AppBlocker.ts): statement `schedule: BlockingSchedule;`. It runs when the top of the file runs, in order, before the next line of the same function.

  29 | }
     | In `the top of the file` (src/plugins/AppBlocker.ts): `}` closes export interface BlockingRules { (opened on line 23). Names declared inside that block end here.

  30 | 
     | Blank line in `src/plugins/AppBlocker.ts` (the Capacitor bridge to native app blocking), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  31 | export interface BlockingState {
     | Named export from the Capacitor bridge to native app blocking: `export interface BlockingState {`.

  32 |   active: boolean;
     | In `the top of the file` (src/plugins/AppBlocker.ts): statement `active: boolean;`. It runs when the top of the file runs, in order, before the next line of the same function.

  33 |   snoozed: boolean;
     | In `the top of the file` (src/plugins/AppBlocker.ts): statement `snoozed: boolean;`. It runs when the top of the file runs, in order, before the next line of the same function.

  34 |   snoozeUntil?: number; // epoch ms
     | In `the top of the file` (src/plugins/AppBlocker.ts): statement `snoozeUntil?: number; // epoch ms`. It runs when the top of the file runs, in order, before the next line of the same function.

  35 | }
     | In `the top of the file` (src/plugins/AppBlocker.ts): `}` closes export interface BlockingState { (opened on line 31). Names declared inside that block end here.

  36 | 
     | Blank line in `src/plugins/AppBlocker.ts` (the Capacitor bridge to native app blocking), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  37 | export interface AppBlockerPlugin {
     | Named export from the Capacitor bridge to native app blocking: `export interface AppBlockerPlugin {`.

  38 |   checkPermissions(): Promise<AppBlockerPermissions>;
     | In `the top of the file` (src/plugins/AppBlocker.ts): statement `checkPermissions(): Promise<AppBlockerPermissions>;`. It runs when the top of the file runs, in order, before the next line of the same function.

  39 |   requestPermissions(): Promise<void>;
     | In `the top of the file` (src/plugins/AppBlocker.ts): statement `requestPermissions(): Promise<void>;`. It runs when the top of the file runs, in order, before the next line of the same function.

  40 |   requestFamilyControlsAuth(): Promise<{ authorized: boolean }>;
     | In `the top of the file` (src/plugins/AppBlocker.ts): `requestFamilyControlsAuth(): Promise<{ authorized: boolean }>;` closes export interface AppBlockerPlugin { (opened on line 37). Names declared inside that block end here.

  41 |   setBlockingRules(options: { rules: BlockingRules }): Promise<{ ok: boolean }>;
     | In `the top of the file` (src/plugins/AppBlocker.ts): `setBlockingRules(options: { rules: BlockingRules }): Promise<{ ok: boolean }>;` closes export interface AppBlockerPlugin { (opened on line 37). Names declared inside that block end here.

  42 |   getBlockingState(): Promise<BlockingState>;
     | In `the top of the file` (src/plugins/AppBlocker.ts): statement `getBlockingState(): Promise<BlockingState>;`. It runs when the top of the file runs, in order, before the next line of the same function.

  43 |   startBlocking(): Promise<{ ok: boolean }>;
     | In `the top of the file` (src/plugins/AppBlocker.ts): `startBlocking(): Promise<{ ok: boolean }>;` closes export interface AppBlockerPlugin { (opened on line 37). Names declared inside that block end here.

  44 |   stopBlocking(): Promise<{ ok: boolean }>;
     | In `the top of the file` (src/plugins/AppBlocker.ts): `stopBlocking(): Promise<{ ok: boolean }>;` closes export interface AppBlockerPlugin { (opened on line 37). Names declared inside that block end here.

  45 |   snooze(options: { minutes: number }): Promise<{ ok: boolean }>;
     | In `the top of the file` (src/plugins/AppBlocker.ts): `snooze(options: { minutes: number }): Promise<{ ok: boolean }>;` closes export interface AppBlockerPlugin { (opened on line 37). Names declared inside that block end here.

  46 | }
     | In `the top of the file` (src/plugins/AppBlocker.ts): `}` closes export interface AppBlockerPlugin { (opened on line 37). Names declared inside that block end here.

  47 | 
     | Blank line in `src/plugins/AppBlocker.ts` (the Capacitor bridge to native app blocking), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  48 | const AppBlocker = registerPlugin<AppBlockerPlugin>('AppBlocker', {
     | In `the top of the file` (src/plugins/AppBlocker.ts): `AppBlocker`: Capacitor plugin named AppBlocker. On the web it loads AppBlockerWeb, which reports every permission denied. No React screen calls it yet. The code is `const AppBlocker = registerPlugin<AppBlockerPlugin>('AppBlocker', {`.

  49 |   web: () => import('./AppBlockerWeb').then((m) => new m.AppBlockerWeb()),
     | In `the top of the file` (src/plugins/AppBlocker.ts): statement `web: () => import('./AppBlockerWeb').then((m) => new m.AppBlockerWeb()),`. It runs when the top of the file runs, in order, before the next line of the same function.

  50 | });
     | In `the top of the file` (src/plugins/AppBlocker.ts): `});` closes const AppBlocker = registerPlugin<AppBlockerPlug (opened on line 48). Names declared inside that block end here.

  51 | 
     | Blank line in `src/plugins/AppBlocker.ts` (the Capacitor bridge to native app blocking), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  52 | export { AppBlocker };
     | Named export from the Capacitor bridge to native app blocking: `export { AppBlocker };`.

