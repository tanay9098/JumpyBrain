# `src/plugins/AppBlocker.ts`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import { registerPlugin } from '@capacitor/core';
     | Borrows the bridge to a phone app. The website stub does not block apps.

   2 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   3 | export type PermissionState = 'granted' | 'denied' | 'prompt';
     | This lets another file use this piece by its name.

   4 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   5 | export interface AppBlockerPermissions {
     | This lets another file use this piece by its name.

   6 |   usageStats: PermissionState;     // Android — PACKAGE_USAGE_STATS
     | Inside the top of the file, this line runs as written: usageStats: PermissionState;     // Android — PACKAGE_USAGE_STATS. It happens in order, after the line above it and before the line below it.

   7 |   accessibility: PermissionState;  // Android — AccessibilityService enabled
     | Inside the top of the file, this line runs as written: accessibility: PermissionState;  // Android — AccessibilityService enabled. It happens in order, after the line above it and before the line below it.

   8 |   familyControls: PermissionState; // iOS    — FamilyControls authorization
     | Inside the top of the file, this line runs as written: familyControls: PermissionState; // iOS    — FamilyControls authorization. It happens in order, after the line above it and before the line below it.

   9 | }
     | This ends export interface AppBlockerPermissions { (opened on line 5).

  10 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  11 | export interface BlockEntry {
     | This lets another file use this piece by its name.

  12 |   value: string;
     | Inside the top of the file, this line runs as written: value: string;. It happens in order, after the line above it and before the line below it.

  13 |   label?: string;
     | Inside the top of the file, this line runs as written: label?: string;. It happens in order, after the line above it and before the line below it.

  14 | }
     | This ends export interface BlockEntry { (opened on line 11).

  15 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  16 | export interface BlockingSchedule {
     | This lets another file use this piece by its name.

  17 |   enabled: boolean;
     | Inside the top of the file, this line runs as written: enabled: boolean;. It happens in order, after the line above it and before the line below it.

  18 |   startTime: string; // "HH:MM"
     | Inside the top of the file, this line runs as written: startTime: string; // "HH:MM". It happens in order, after the line above it and before the line below it.

  19 |   endTime: string;   // "HH:MM"
     | Inside the top of the file, this line runs as written: endTime: string;   // "HH:MM". It happens in order, after the line above it and before the line below it.

  20 |   days: number[];    // 0=Sun … 6=Sat
     | Inside the top of the file, this line runs as written: days: number[];    // 0=Sun … 6=Sat. It happens in order, after the line above it and before the line below it.

  21 | }
     | This ends export interface BlockingSchedule { (opened on line 16).

  22 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  23 | export interface BlockingRules {
     | This lets another file use this piece by its name.

  24 |   isEnabled: boolean;
     | Inside the top of the file, this line runs as written: isEnabled: boolean;. It happens in order, after the line above it and before the line below it.

  25 |   blockedApps: BlockEntry[];
     | Inside the top of the file, this line runs as written: blockedApps: BlockEntry[];. It happens in order, after the line above it and before the line below it.

  26 |   blockedSites: BlockEntry[];
     | Inside the top of the file, this line runs as written: blockedSites: BlockEntry[];. It happens in order, after the line above it and before the line below it.

  27 |   whitelist: BlockEntry[];
     | Inside the top of the file, this line runs as written: whitelist: BlockEntry[];. It happens in order, after the line above it and before the line below it.

  28 |   schedule: BlockingSchedule;
     | Inside the top of the file, this line runs as written: schedule: BlockingSchedule;. It happens in order, after the line above it and before the line below it.

  29 | }
     | This ends export interface BlockingRules { (opened on line 23).

  30 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  31 | export interface BlockingState {
     | This lets another file use this piece by its name.

  32 |   active: boolean;
     | Inside the top of the file, this line runs as written: active: boolean;. It happens in order, after the line above it and before the line below it.

  33 |   snoozed: boolean;
     | Inside the top of the file, this line runs as written: snoozed: boolean;. It happens in order, after the line above it and before the line below it.

  34 |   snoozeUntil?: number; // epoch ms
     | Inside the top of the file, this line runs as written: snoozeUntil?: number; // epoch ms. It happens in order, after the line above it and before the line below it.

  35 | }
     | This ends export interface BlockingState { (opened on line 31).

  36 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  37 | export interface AppBlockerPlugin {
     | This lets another file use this piece by its name.

  38 |   checkPermissions(): Promise<AppBlockerPermissions>;
     | Inside the top of the file, this line runs as written: checkPermissions(): Promise<AppBlockerPermissions>;. It happens in order, after the line above it and before the line below it.

  39 |   requestPermissions(): Promise<void>;
     | Inside the top of the file, this line runs as written: requestPermissions(): Promise<void>;. It happens in order, after the line above it and before the line below it.

  40 |   requestFamilyControlsAuth(): Promise<{ authorized: boolean }>;
     | This ends export interface AppBlockerPlugin { (opened on line 37).

  41 |   setBlockingRules(options: { rules: BlockingRules }): Promise<{ ok: boolean }>;
     | This ends export interface AppBlockerPlugin { (opened on line 37).

  42 |   getBlockingState(): Promise<BlockingState>;
     | Inside the top of the file, this line runs as written: getBlockingState(): Promise<BlockingState>;. It happens in order, after the line above it and before the line below it.

  43 |   startBlocking(): Promise<{ ok: boolean }>;
     | This ends export interface AppBlockerPlugin { (opened on line 37).

  44 |   stopBlocking(): Promise<{ ok: boolean }>;
     | This ends export interface AppBlockerPlugin { (opened on line 37).

  45 |   snooze(options: { minutes: number }): Promise<{ ok: boolean }>;
     | This ends export interface AppBlockerPlugin { (opened on line 37).

  46 | }
     | This ends export interface AppBlockerPlugin { (opened on line 37).

  47 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  48 | const AppBlocker = registerPlugin<AppBlockerPlugin>('AppBlocker', {
     | Capacitor plugin named AppBlocker. On the web it loads AppBlockerWeb, which reports every permission denied. No React screen calls it yet.

  49 |   web: () => import('./AppBlockerWeb').then((m) => new m.AppBlockerWeb()),
     | Inside the top of the file, this line runs as written: web: () => import('./AppBlockerWeb').then((m) => new m.AppBlockerWeb()),. It happens in order, after the line above it and before the line below it.

  50 | });
     | This ends const AppBlocker = registerPlugin<AppBlockerPlug (opened on line 48).

  51 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  52 | export { AppBlocker };
     | This lets another file use this piece by its name.

