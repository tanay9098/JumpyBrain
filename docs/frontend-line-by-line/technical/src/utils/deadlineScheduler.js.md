# `src/utils/deadlineScheduler.js`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import { notify } from "./notify";
     | Import for browser timers that fire when a task is due: `import { notify } from "./notify";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   2 | 
     | Blank line in `src/utils/deadlineScheduler.js` (browser timers that fire when a task is due), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   3 | const scheduled = new Map();
     | In `the top of the file` (src/utils/deadlineScheduler.js): `scheduled`: Map from task id to the timer id from setTimeout, so a task never has two deadline alarms. The code is `const scheduled = new Map();`.

   4 | 
     | Blank line in `src/utils/deadlineScheduler.js` (browser timers that fire when a task is due), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   5 | /**
     | Comment inside the top of the file. Not executed. Text: /**

   6 |  * Schedule a deadline notification
     | Comment inside the top of the file. Not executed. Text: * Schedule a deadline notification

   7 |  */
     | Comment inside the top of the file. Not executed. Text: */

   8 | export function scheduleDeadline(task) {
     | Named export from browser timers that fire when a task is due: `export function scheduleDeadline(task) {`.

   9 |   if (!task.dueAt || task.completed) return;
     | In `scheduleDeadline` (src/utils/deadlineScheduler.js): branch `if (!task.dueAt || task.completed) return;`. Only one side runs.

  10 | 
     | Blank line in `src/utils/deadlineScheduler.js` (browser timers that fire when a task is due), inside scheduleDeadline. The parser skips it. It separates the previous statement from the next so the function is readable.

  11 |   const dueTime = new Date(task.dueAt).getTime();
     | In `scheduleDeadline` (src/utils/deadlineScheduler.js): `dueTime` is assigned `new Date(task.dueAt).getTime();`. Later lines in this function read that name.

  12 |   const now = Date.now();
     | In `scheduleDeadline` (src/utils/deadlineScheduler.js): `now` is assigned `Date.now();`. Later lines in this function read that name.

  13 |   const delay = dueTime - now;
     | In `scheduleDeadline` (src/utils/deadlineScheduler.js): `delay` is assigned `dueTime - now;`. Later lines in this function read that name.

  14 | 
     | Blank line in `src/utils/deadlineScheduler.js` (browser timers that fire when a task is due), inside scheduleDeadline. The parser skips it. It separates the previous statement from the next so the function is readable.

  15 |   if (delay <= 0) return;
     | In `scheduleDeadline` (src/utils/deadlineScheduler.js): branch `if (delay <= 0) return;`. Only one side runs.

  16 | 
     | Blank line in `src/utils/deadlineScheduler.js` (browser timers that fire when a task is due), inside scheduleDeadline. The parser skips it. It separates the previous statement from the next so the function is readable.

  17 |   // Avoid duplicate timers
     | Comment inside scheduleDeadline. Not executed. It documents the next code: Avoid duplicate timers

  18 |   if (scheduled.has(task._id)) {
     | In `scheduleDeadline` (src/utils/deadlineScheduler.js): branch `if (scheduled.has(task._id)) {`. Only one side runs.

  19 |     clearTimeout(scheduled.get(task._id));
     | In `scheduleDeadline` (src/utils/deadlineScheduler.js): timer — `clearTimeout(scheduled.get(task._id));`. The callback runs later on the event loop, not now.

  20 |   }
     | In `scheduleDeadline` (src/utils/deadlineScheduler.js): `}` closes if (scheduled.has(task._id)) { (opened on line 18). Names declared inside that block end here.

  21 | 
     | Blank line in `src/utils/deadlineScheduler.js` (browser timers that fire when a task is due), inside scheduleDeadline. The parser skips it. It separates the previous statement from the next so the function is readable.

  22 |   const timerId = setTimeout(() => {
     | In `scheduleDeadline` (src/utils/deadlineScheduler.js): `timerId` is assigned `setTimeout(() => {`. Later lines in this function read that name.

  23 |     notify(
     | In `scheduleDeadline` (src/utils/deadlineScheduler.js): statement `notify(`. It runs when scheduleDeadline runs, in order, before the next line of the same function.

  24 |       "⏰ Task Deadline",
     | In `scheduleDeadline` (src/utils/deadlineScheduler.js): statement `"⏰ Task Deadline",`. It runs when scheduleDeadline runs, in order, before the next line of the same function.

  25 |       task.customReminderMessage ||
     | In `scheduleDeadline` (src/utils/deadlineScheduler.js): statement `task.customReminderMessage ||`. It runs when scheduleDeadline runs, in order, before the next line of the same function.

  26 |         `"${task.title}" is due now. Start immediately.`
     | In `scheduleDeadline` (src/utils/deadlineScheduler.js): ``"${task.title}" is due now. Start immediately.`` closes const timerId = setTimeout(() => { (opened on line 22). Names declared inside that block end here.

  27 |     );
     | In `scheduleDeadline` (src/utils/deadlineScheduler.js): statement `);`. It runs when scheduleDeadline runs, in order, before the next line of the same function.

  28 |     scheduled.delete(task._id);
     | In `scheduleDeadline` (src/utils/deadlineScheduler.js): statement `scheduled.delete(task._id);`. It runs when scheduleDeadline runs, in order, before the next line of the same function.

  29 |   }, delay);
     | In `scheduleDeadline` (src/utils/deadlineScheduler.js): `}, delay);` closes const timerId = setTimeout(() => { (opened on line 22). Names declared inside that block end here.

  30 | 
     | Blank line in `src/utils/deadlineScheduler.js` (browser timers that fire when a task is due), inside scheduleDeadline. The parser skips it. It separates the previous statement from the next so the function is readable.

  31 |   scheduled.set(task._id, timerId);
     | In `scheduleDeadline` (src/utils/deadlineScheduler.js): statement `scheduled.set(task._id, timerId);`. It runs when scheduleDeadline runs, in order, before the next line of the same function.

  32 | }
     | In `scheduleDeadline` (src/utils/deadlineScheduler.js): `}` closes scheduleDeadline (opened on line 8). Names declared inside that block end here.

  33 | 
     | Blank line in `src/utils/deadlineScheduler.js` (browser timers that fire when a task is due), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  34 | /**
     | Comment inside the top of the file. Not executed. Text: /**

  35 |  * Clear a scheduled deadline (if task is completed/deleted)
     | Comment inside the top of the file. Not executed. Text: * Clear a scheduled deadline (if task is completed/deleted)

  36 |  */
     | Comment inside the top of the file. Not executed. Text: */

  37 | export function clearDeadline(taskId) {
     | Named export from browser timers that fire when a task is due: `export function clearDeadline(taskId) {`.

  38 |   if (scheduled.has(taskId)) {
     | In `clearDeadline` (src/utils/deadlineScheduler.js): branch `if (scheduled.has(taskId)) {`. Only one side runs.

  39 |     clearTimeout(scheduled.get(taskId));
     | In `clearDeadline` (src/utils/deadlineScheduler.js): timer — `clearTimeout(scheduled.get(taskId));`. The callback runs later on the event loop, not now.

  40 |     scheduled.delete(taskId);
     | In `clearDeadline` (src/utils/deadlineScheduler.js): statement `scheduled.delete(taskId);`. It runs when clearDeadline runs, in order, before the next line of the same function.

  41 |   }
     | In `clearDeadline` (src/utils/deadlineScheduler.js): `}` closes if (scheduled.has(taskId)) { (opened on line 38). Names declared inside that block end here.

  42 | }
     | In `clearDeadline` (src/utils/deadlineScheduler.js): `}` closes clearDeadline (opened on line 37). Names declared inside that block end here.

