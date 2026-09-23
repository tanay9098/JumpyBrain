# `src/plugins/AppBlockerWeb.ts`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import { WebPlugin } from '@capacitor/core';
     | Import for the web stub that reports blocking as unavailable: `import { WebPlugin } from '@capacitor/core';`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   2 | import type {
     | Import for the web stub that reports blocking as unavailable: `import type {`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   3 |   AppBlockerPlugin,
     | In `the top of the file` (src/plugins/AppBlockerWeb.ts): statement `AppBlockerPlugin,`. It runs when the top of the file runs, in order, before the next line of the same function.

   4 |   AppBlockerPermissions,
     | In `the top of the file` (src/plugins/AppBlockerWeb.ts): statement `AppBlockerPermissions,`. It runs when the top of the file runs, in order, before the next line of the same function.

   5 |   BlockingRules,
     | In `the top of the file` (src/plugins/AppBlockerWeb.ts): statement `BlockingRules,`. It runs when the top of the file runs, in order, before the next line of the same function.

   6 |   BlockingState,
     | In `the top of the file` (src/plugins/AppBlockerWeb.ts): statement `BlockingState,`. It runs when the top of the file runs, in order, before the next line of the same function.

   7 | } from './AppBlocker';
     | In `the top of the file` (src/plugins/AppBlockerWeb.ts): `} from './AppBlocker';` closes import type { (opened on line 2). Names declared inside that block end here.

   8 | 
     | Blank line in `src/plugins/AppBlockerWeb.ts` (the web stub that reports blocking as unavailable), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   9 | export class AppBlockerWeb extends WebPlugin implements AppBlockerPlugin {
     | Named export from the web stub that reports blocking as unavailable: `export class AppBlockerWeb extends WebPlugin implements AppBlockerPlugin {`.

  10 |   async checkPermissions(): Promise<AppBlockerPermissions> {
     | In `the top of the file` (src/plugins/AppBlockerWeb.ts): statement `async checkPermissions(): Promise<AppBlockerPermissions> {`. It runs when the top of the file runs, in order, before the next line of the same function.

  11 |     return { usageStats: 'denied', accessibility: 'denied', familyControls: 'denied' };
     | In `the top of the file` (src/plugins/AppBlockerWeb.ts): return `return { usageStats: 'denied', accessibility: 'denied', familyControls: 'denied' };`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  12 |   }
     | In `the top of the file` (src/plugins/AppBlockerWeb.ts): `}` closes async checkPermissions(): Promise<AppBlockerPerm (opened on line 10). Names declared inside that block end here.

  13 |   async requestPermissions(): Promise<void> {}
     | In `the top of the file` (src/plugins/AppBlockerWeb.ts): `async requestPermissions(): Promise<void> {}` closes export class AppBlockerWeb extends WebPlugin imp (opened on line 9). Names declared inside that block end here.

  14 |   async requestFamilyControlsAuth(): Promise<{ authorized: boolean }> {
     | In `the top of the file` (src/plugins/AppBlockerWeb.ts): `async requestFamilyControlsAuth(): Promise<{ authorized: boolean }> {` closes export class AppBlockerWeb extends WebPlugin imp (opened on line 9). Names declared inside that block end here.

  15 |     return { authorized: false };
     | In `the top of the file` (src/plugins/AppBlockerWeb.ts): return `return { authorized: false };`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  16 |   }
     | In `the top of the file` (src/plugins/AppBlockerWeb.ts): `}` closes async requestFamilyControlsAuth(): Promise<{ aut (opened on line 14). Names declared inside that block end here.

  17 |   async setBlockingRules(_: { rules: BlockingRules }): Promise<{ ok: boolean }> {
     | In `the top of the file` (src/plugins/AppBlockerWeb.ts): `async setBlockingRules(_: { rules: BlockingRules }): Promise<{ ok: boolean }> {` closes export class AppBlockerWeb extends WebPlugin imp (opened on line 9). Names declared inside that block end here.

  18 |     return { ok: false };
     | In `the top of the file` (src/plugins/AppBlockerWeb.ts): return `return { ok: false };`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  19 |   }
     | In `the top of the file` (src/plugins/AppBlockerWeb.ts): `}` closes async setBlockingRules(_: { rules: BlockingRules (opened on line 17). Names declared inside that block end here.

  20 |   async getBlockingState(): Promise<BlockingState> {
     | In `the top of the file` (src/plugins/AppBlockerWeb.ts): statement `async getBlockingState(): Promise<BlockingState> {`. It runs when the top of the file runs, in order, before the next line of the same function.

  21 |     return { active: false, snoozed: false };
     | In `the top of the file` (src/plugins/AppBlockerWeb.ts): return `return { active: false, snoozed: false };`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  22 |   }
     | In `the top of the file` (src/plugins/AppBlockerWeb.ts): `}` closes async getBlockingState(): Promise<BlockingState> (opened on line 20). Names declared inside that block end here.

  23 |   async startBlocking(): Promise<{ ok: boolean }> { return { ok: false }; }
     | In `the top of the file` (src/plugins/AppBlockerWeb.ts): `async startBlocking(): Promise<{ ok: boolean }> { return { ok: false }; }` closes export class AppBlockerWeb extends WebPlugin imp (opened on line 9). Names declared inside that block end here.

  24 |   async stopBlocking(): Promise<{ ok: boolean }> { return { ok: false }; }
     | In `the top of the file` (src/plugins/AppBlockerWeb.ts): `async stopBlocking(): Promise<{ ok: boolean }> { return { ok: false }; }` closes export class AppBlockerWeb extends WebPlugin imp (opened on line 9). Names declared inside that block end here.

  25 |   async snooze(_: { minutes: number }): Promise<{ ok: boolean }> { return { ok: false }; }
     | In `the top of the file` (src/plugins/AppBlockerWeb.ts): `async snooze(_: { minutes: number }): Promise<{ ok: boolean }> { return { ok: false }; }` closes export class AppBlockerWeb extends WebPlugin imp (opened on line 9). Names declared inside that block end here.

  26 | }
     | In `the top of the file` (src/plugins/AppBlockerWeb.ts): `}` closes export class AppBlockerWeb extends WebPlugin imp (opened on line 9). Names declared inside that block end here.

