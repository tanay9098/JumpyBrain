# `src/utils/deadlineScheduler.js`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import { notify } from "./notify";
     | This file borrows a tool another file already made.

   2 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   3 | const scheduled = new Map();
     | Map from task id to the timer id from setTimeout, so a task never has two deadline alarms.

   4 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   5 | /**
     | A note for people. The app skips this line.

   6 |  * Schedule a deadline notification
     | A note for people. The app skips this line.

   7 |  */
     | A note for people. The app skips this line.

   8 | export function scheduleDeadline(task) {
     | This lets another file use this piece by its name.

   9 |   if (!task.dueAt || task.completed) return;
     | This asks a yes-or-no question. The next bit runs only on yes.

  10 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  11 |   const dueTime = new Date(task.dueAt).getTime();
     | This gives a short name to a value so the rest of scheduleDeadline can use it.

  12 |   const now = Date.now();
     | This gives a short name to a value so the rest of scheduleDeadline can use it.

  13 |   const delay = dueTime - now;
     | This gives a short name to a value so the rest of scheduleDeadline can use it.

  14 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  15 |   if (delay <= 0) return;
     | This asks a yes-or-no question. The next bit runs only on yes.

  16 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  17 |   // Avoid duplicate timers
     | A note written for people. The app does not run it.

  18 |   if (scheduled.has(task._id)) {
     | This asks a yes-or-no question. The next bit runs only on yes.

  19 |     clearTimeout(scheduled.get(task._id));
     | Inside scheduleDeadline, this line runs as written: clearTimeout(scheduled.get(task._id));. It happens in order, after the line above it and before the line below it.

  20 |   }
     | This ends if (scheduled.has(task._id)) { (opened on line 18).

  21 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  22 |   const timerId = setTimeout(() => {
     | This gives a short name to a value so the rest of scheduleDeadline can use it.

  23 |     notify(
     | Inside scheduleDeadline, this line runs as written: notify(. It happens in order, after the line above it and before the line below it.

  24 |       "⏰ Task Deadline",
     | Inside scheduleDeadline, this line runs as written: "⏰ Task Deadline",. It happens in order, after the line above it and before the line below it.

  25 |       task.customReminderMessage ||
     | Inside scheduleDeadline, this line runs as written: task.customReminderMessage ||. It happens in order, after the line above it and before the line below it.

  26 |         `"${task.title}" is due now. Start immediately.`
     | This ends const timerId = setTimeout(() => { (opened on line 22).

  27 |     );
     | This closes a box of instructions that opened above.

  28 |     scheduled.delete(task._id);
     | Inside scheduleDeadline, this line runs as written: scheduled.delete(task._id);. It happens in order, after the line above it and before the line below it.

  29 |   }, delay);
     | This ends const timerId = setTimeout(() => { (opened on line 22).

  30 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  31 |   scheduled.set(task._id, timerId);
     | Inside scheduleDeadline, this line runs as written: scheduled.set(task._id, timerId);. It happens in order, after the line above it and before the line below it.

  32 | }
     | This ends scheduleDeadline (opened on line 8).

  33 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  34 | /**
     | A note for people. The app skips this line.

  35 |  * Clear a scheduled deadline (if task is completed/deleted)
     | A note for people. The app skips this line.

  36 |  */
     | A note for people. The app skips this line.

  37 | export function clearDeadline(taskId) {
     | This lets another file use this piece by its name.

  38 |   if (scheduled.has(taskId)) {
     | This asks a yes-or-no question. The next bit runs only on yes.

  39 |     clearTimeout(scheduled.get(taskId));
     | Inside clearDeadline, this line runs as written: clearTimeout(scheduled.get(taskId));. It happens in order, after the line above it and before the line below it.

  40 |     scheduled.delete(taskId);
     | Inside clearDeadline, this line runs as written: scheduled.delete(taskId);. It happens in order, after the line above it and before the line below it.

  41 |   }
     | This ends if (scheduled.has(taskId)) { (opened on line 38).

  42 | }
     | This ends clearDeadline (opened on line 37).

