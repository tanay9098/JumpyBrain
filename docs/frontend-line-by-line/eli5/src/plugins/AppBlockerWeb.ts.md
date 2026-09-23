# `src/plugins/AppBlockerWeb.ts`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import { WebPlugin } from '@capacitor/core';
     | Borrows the bridge to a phone app. The website stub does not block apps.

   2 | import type {
     | This file borrows a tool another file already made.

   3 |   AppBlockerPlugin,
     | Inside the top of the file, this line runs as written: AppBlockerPlugin,. It happens in order, after the line above it and before the line below it.

   4 |   AppBlockerPermissions,
     | Inside the top of the file, this line runs as written: AppBlockerPermissions,. It happens in order, after the line above it and before the line below it.

   5 |   BlockingRules,
     | Inside the top of the file, this line runs as written: BlockingRules,. It happens in order, after the line above it and before the line below it.

   6 |   BlockingState,
     | Inside the top of the file, this line runs as written: BlockingState,. It happens in order, after the line above it and before the line below it.

   7 | } from './AppBlocker';
     | This ends import type { (opened on line 2).

   8 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   9 | export class AppBlockerWeb extends WebPlugin implements AppBlockerPlugin {
     | This lets another file use this piece by its name.

  10 |   async checkPermissions(): Promise<AppBlockerPermissions> {
     | Inside the top of the file, this line runs as written: async checkPermissions(): Promise<AppBlockerPermissions> {. It happens in order, after the line above it and before the line below it.

  11 |     return { usageStats: 'denied', accessibility: 'denied', familyControls: 'denied' };
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  12 |   }
     | This ends async checkPermissions(): Promise<AppBlockerPerm (opened on line 10).

  13 |   async requestPermissions(): Promise<void> {}
     | This ends export class AppBlockerWeb extends WebPlugin imp (opened on line 9).

  14 |   async requestFamilyControlsAuth(): Promise<{ authorized: boolean }> {
     | This ends export class AppBlockerWeb extends WebPlugin imp (opened on line 9).

  15 |     return { authorized: false };
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  16 |   }
     | This ends async requestFamilyControlsAuth(): Promise<{ aut (opened on line 14).

  17 |   async setBlockingRules(_: { rules: BlockingRules }): Promise<{ ok: boolean }> {
     | This ends export class AppBlockerWeb extends WebPlugin imp (opened on line 9).

  18 |     return { ok: false };
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  19 |   }
     | This ends async setBlockingRules(_: { rules: BlockingRules (opened on line 17).

  20 |   async getBlockingState(): Promise<BlockingState> {
     | Inside the top of the file, this line runs as written: async getBlockingState(): Promise<BlockingState> {. It happens in order, after the line above it and before the line below it.

  21 |     return { active: false, snoozed: false };
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  22 |   }
     | This ends async getBlockingState(): Promise<BlockingState> (opened on line 20).

  23 |   async startBlocking(): Promise<{ ok: boolean }> { return { ok: false }; }
     | This ends export class AppBlockerWeb extends WebPlugin imp (opened on line 9).

  24 |   async stopBlocking(): Promise<{ ok: boolean }> { return { ok: false }; }
     | This ends export class AppBlockerWeb extends WebPlugin imp (opened on line 9).

  25 |   async snooze(_: { minutes: number }): Promise<{ ok: boolean }> { return { ok: false }; }
     | This ends export class AppBlockerWeb extends WebPlugin imp (opened on line 9).

  26 | }
     | This ends export class AppBlockerWeb extends WebPlugin imp (opened on line 9).

