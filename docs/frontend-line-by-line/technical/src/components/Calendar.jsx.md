# `src/components/Calendar.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import React, { useEffect, useState } from 'react';
     | Import for the month view of tasks: `import React, { useEffect, useState } from 'react';`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   2 | import FullCalendar from '@fullcalendar/react';
     | Import for the month view of tasks: `import FullCalendar from '@fullcalendar/react';`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   3 | import dayGridPlugin from '@fullcalendar/daygrid/index.js';
     | Import for the month view of tasks: `import dayGridPlugin from '@fullcalendar/daygrid/index.js';`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   4 | import interactionPlugin from '@fullcalendar/interaction/index.js';
     | Import for the month view of tasks: `import interactionPlugin from '@fullcalendar/interaction/index.js';`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   5 | import timeGridPlugin from '@fullcalendar/timegrid/index.js';
     | Import for the month view of tasks: `import timeGridPlugin from '@fullcalendar/timegrid/index.js';`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   6 | import api from '../services/api';
     | Import for the month view of tasks: `import api from '../services/api';`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   7 | 
     | Blank line in `src/components/Calendar.jsx` (the month view of tasks), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   8 | export default function Calendar() {
     | Defines `Calendar` in the month view of tasks. FullCalendar month view of tasks. Clicking a day prompts for a title and POSTs a task. Clicking an event prompts for a new due time and PUTs it.

   9 |   const [events, setEvents] = useState([]);
     | In `Calendar` (src/components/Calendar.jsx): React state `events, setEvents`. The value survives re-renders. Calling the setter re-renders this component. `const [events, setEvents] = useState([]);`

  10 | 
     | Blank line in `src/components/Calendar.jsx` (the month view of tasks), inside Calendar. The parser skips it. It separates the previous statement from the next so the function is readable.

  11 |   async function load() {
     | Defines `load` in the month view of tasks. GET /tasks and, on the task page, keeps only tasks that are not completed. Calendar and the deadline page keep a wider set.

  12 |     const res = await api.get('/tasks');
     | In `load` (src/components/Calendar.jsx): `res` is assigned `await api.get('/tasks');`. Later lines in this function read that name.

  13 |     const tasks = res.tasks || [];
     | In `load` (src/components/Calendar.jsx): `tasks` is assigned `res.tasks || [];`. Later lines in this function read that name.

  14 | 
     | Blank line in `src/components/Calendar.jsx` (the month view of tasks), inside load. The parser skips it. It separates the previous statement from the next so the function is readable.

  15 |     setEvents(tasks.map(t => ({
     | In `load` (src/components/Calendar.jsx): iteration `setEvents(tasks.map(t => ({`.

  16 |       id: t._id,
     | In `load` (src/components/Calendar.jsx): statement `id: t._id,`. It runs when load runs, in order, before the next line of the same function.

  17 |       title: t.title,
     | In `load` (src/components/Calendar.jsx): statement `title: t.title,`. It runs when load runs, in order, before the next line of the same function.

  18 |       date: t.dueAt ? new Date(t.dueAt).toISOString() : null
     | In `load` (src/components/Calendar.jsx): statement `date: t.dueAt ? new Date(t.dueAt).toISOString() : null`. It runs when load runs, in order, before the next line of the same function.

  19 |     })));
     | In `load` (src/components/Calendar.jsx): `})));` closes setEvents(tasks.map(t => ({ (opened on line 15). Names declared inside that block end here.

  20 |   }
     | In `load` (src/components/Calendar.jsx): `}` closes load (opened on line 11). Names declared inside that block end here.

  21 | 
     | Blank line in `src/components/Calendar.jsx` (the month view of tasks), inside Calendar. The parser skips it. It separates the previous statement from the next so the function is readable.

  22 |   useEffect(() => { load(); }, []);
     | In `Calendar` (src/components/Calendar.jsx): opens or continues an effect — `useEffect(() => { load(); }, []);`. The effect body runs after paint, and its cleanup runs before the next effect and on unmount.

  23 |   function handleDateClick(info) {
     | Defines `handleDateClick` in the month view of tasks. prompt() for a title, POST /tasks with that dueAt, then load() immediately (the reload can race the POST).

  24 |   // open modal for creating a task with that date
     | Comment inside handleDateClick. Not executed. It documents the next code: open modal for creating a task with that date

  25 |   const date = info.dateStr;
     | In `handleDateClick` (src/components/Calendar.jsx): `date` is assigned `info.dateStr;`. Later lines in this function read that name.

  26 |   const title = prompt("Task name?");
     | In `handleDateClick` (src/components/Calendar.jsx): `title` is assigned `prompt("Task name?");`. Later lines in this function read that name.

  27 |   if (!title) return;
     | In `handleDateClick` (src/components/Calendar.jsx): branch `if (!title) return;`. Only one side runs.

  28 | 
     | Blank line in `src/components/Calendar.jsx` (the month view of tasks), inside handleDateClick. The parser skips it. It separates the previous statement from the next so the function is readable.

  29 |   api.post("/tasks", { title, dueAt: date });
     | In `handleDateClick` (src/components/Calendar.jsx): HTTP via the shared Axios instance — `api.post("/tasks", { title, dueAt: date });`. The request interceptor adds `Authorization: Bearer <accessToken>`. The response interceptor returns `res.data`, so the awaited value is the JSON body.

  30 |   load();
     | In `handleDateClick` (src/components/Calendar.jsx): statement `load();`. It runs when handleDateClick runs, in order, before the next line of the same function.

  31 | }
     | In `handleDateClick` (src/components/Calendar.jsx): `}` closes handleDateClick (opened on line 23). Names declared inside that block end here.

  32 | 
     | Blank line in `src/components/Calendar.jsx` (the month view of tasks), inside Calendar. The parser skips it. It separates the previous statement from the next so the function is readable.

  33 | function handleEventClick(info) {
     | Defines `handleEventClick` in the month view of tasks. prompt() for a new datetime, PUT /tasks/:id, then load().

  34 |   const newDate = prompt("Update deadline (YYYY-MM-DD HH:mm)?", info.event.startStr);
     | In `handleEventClick` (src/components/Calendar.jsx): `newDate` is assigned `prompt("Update deadline (YYYY-MM-DD HH:mm)?", info.event.startStr);`. Later lines in this function read that name.

  35 |   if (!newDate) return;
     | In `handleEventClick` (src/components/Calendar.jsx): branch `if (!newDate) return;`. Only one side runs.

  36 |   api.put(`/tasks/${info.event.id}`, { dueAt: newDate });
     | In `handleEventClick` (src/components/Calendar.jsx): HTTP via the shared Axios instance — `api.put(`/tasks/${info.event.id}`, { dueAt: newDate });`. The request interceptor adds `Authorization: Bearer <accessToken>`. The response interceptor returns `res.data`, so the awaited value is the JSON body.

  37 |   load();
     | In `handleEventClick` (src/components/Calendar.jsx): statement `load();`. It runs when handleEventClick runs, in order, before the next line of the same function.

  38 | }
     | In `handleEventClick` (src/components/Calendar.jsx): `}` closes handleEventClick (opened on line 33). Names declared inside that block end here.

  39 | 
     | Blank line in `src/components/Calendar.jsx` (the month view of tasks), inside Calendar. The parser skips it. It separates the previous statement from the next so the function is readable.

  40 | 
     | Blank line in `src/components/Calendar.jsx` (the month view of tasks), inside Calendar. The parser skips it. It separates the previous statement from the next so the function is readable.

  41 |   return (
     | In `Calendar` (src/components/Calendar.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  42 |     <div>
     | In `Calendar` (src/components/Calendar.jsx): Opens it. A box that groups the elements inside it. Source: `<div>`

  43 |       <h1 className="page-title">Calendar</h1>
     | In `Calendar` (src/components/Calendar.jsx): Opens it. The page title. Source: `<h1 className="page-title">Calendar</h1>`

  44 |       <p className="page-subtitle">Your tasks in calendar view</p>
     | In `Calendar` (src/components/Calendar.jsx): Opens it. A paragraph. Source: `<p className="page-subtitle">Your tasks in calendar view</p>`

  45 | 
     | Blank line in `src/components/Calendar.jsx` (the month view of tasks), inside Calendar. The parser skips it. It separates the previous statement from the next so the function is readable.

  46 |       <div className="card">
     | In `Calendar` (src/components/Calendar.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="card">`

  47 |         <FullCalendar
     | In `Calendar` (src/components/Calendar.jsx): Opens it. The month grid. events come from GET /tasks. Source: `<FullCalendar`

  48 |           dateClick={handleDateClick}
     | In `Calendar` (src/components/Calendar.jsx): `dateClick={handleDateClick}` closes Calendar (opened on line 8). Names declared inside that block end here.

  49 |   
     | Blank line in `src/components/Calendar.jsx` (the month view of tasks), inside Calendar. The parser skips it. It separates the previous statement from the next so the function is readable.

  50 |   
     | Blank line in `src/components/Calendar.jsx` (the month view of tasks), inside Calendar. The parser skips it. It separates the previous statement from the next so the function is readable.

  51 |           eventClick={handleEventClick}
     | In `Calendar` (src/components/Calendar.jsx): `eventClick={handleEventClick}` closes Calendar (opened on line 8). Names declared inside that block end here.

  52 | 
     | Blank line in `src/components/Calendar.jsx` (the month view of tasks), inside Calendar. The parser skips it. It separates the previous statement from the next so the function is readable.

  53 |           plugins={[dayGridPlugin, timeGridPlugin, interactionPlugin]}
     | In `Calendar` (src/components/Calendar.jsx): `plugins={[dayGridPlugin, timeGridPlugin, interactionPlugin]}` closes Calendar (opened on line 8). Names declared inside that block end here.

  54 |           initialView="dayGridMonth"
     | In `Calendar` (src/components/Calendar.jsx): statement `initialView="dayGridMonth"`. It runs when Calendar runs, in order, before the next line of the same function.

  55 |           events={events}
     | In `Calendar` (src/components/Calendar.jsx): `events={events}` closes Calendar (opened on line 8). Names declared inside that block end here.

  56 |           height={"80vh"}
     | In `Calendar` (src/components/Calendar.jsx): `height={"80vh"}` closes Calendar (opened on line 8). Names declared inside that block end here.

  57 |         />
     | In `Calendar` (src/components/Calendar.jsx): statement `/>`. It runs when Calendar runs, in order, before the next line of the same function.

  58 |       </div>
     | In `Calendar` (src/components/Calendar.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  59 |     </div>
     | In `Calendar` (src/components/Calendar.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  60 |   );
     | In `Calendar` (src/components/Calendar.jsx): statement `);`. It runs when Calendar runs, in order, before the next line of the same function.

  61 | }
     | In `Calendar` (src/components/Calendar.jsx): `}` closes Calendar (opened on line 8). Names declared inside that block end here.

  62 | 
     | Blank line in `src/components/Calendar.jsx` (the month view of tasks), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

