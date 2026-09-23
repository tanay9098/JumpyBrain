# `src/components/Calendar.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import React, { useEffect, useState } from 'react';
     | Borrows React so this file can remember things and draw the screen.

   2 | import FullCalendar from '@fullcalendar/react';
     | Borrows React so this file can remember things and draw the screen.

   3 | import dayGridPlugin from '@fullcalendar/daygrid/index.js';
     | This file borrows a tool another file already made.

   4 | import interactionPlugin from '@fullcalendar/interaction/index.js';
     | This file borrows a tool another file already made.

   5 | import timeGridPlugin from '@fullcalendar/timegrid/index.js';
     | This file borrows a tool another file already made.

   6 | import api from '../services/api';
     | This file borrows a tool another file already made.

   7 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   8 | export default function Calendar() {
     | This starts Calendar. FullCalendar month view of tasks. Clicking a day prompts for a title and POSTs a task. Clicking an event prompts for a new due time and PUTs it.

   9 |   const [events, setEvents] = useState([]);
     | This gives a short name to a value so the rest of Calendar can use it.

  10 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  11 |   async function load() {
     | This starts load. GET /tasks and, on the task page, keeps only tasks that are not completed. Calendar and the deadline page keep a wider set.

  12 |     const res = await api.get('/tasks');
     | This gives a short name to a value so the rest of load can use it.

  13 |     const tasks = res.tasks || [];
     | This gives a short name to a value so the rest of load can use it.

  14 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  15 |     setEvents(tasks.map(t => ({
     | Inside load, this line runs as written: setEvents(tasks.map(t => ({. It happens in order, after the line above it and before the line below it.

  16 |       id: t._id,
     | Inside load, this line runs as written: id: t._id,. It happens in order, after the line above it and before the line below it.

  17 |       title: t.title,
     | Inside load, this line runs as written: title: t.title,. It happens in order, after the line above it and before the line below it.

  18 |       date: t.dueAt ? new Date(t.dueAt).toISOString() : null
     | Inside load, this line runs as written: date: t.dueAt ? new Date(t.dueAt).toISOString() : null. It happens in order, after the line above it and before the line below it.

  19 |     })));
     | This ends setEvents(tasks.map(t => ({ (opened on line 15).

  20 |   }
     | This ends load (opened on line 11).

  21 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  22 |   useEffect(() => { load(); }, []);
     | This is an extra job that happens after the picture is drawn.

  23 |   function handleDateClick(info) {
     | This starts handleDateClick. prompt() for a title, POST /tasks with that dueAt, then load() immediately (the reload can race the POST).

  24 |   // open modal for creating a task with that date
     | A note written for people. The app does not run it.

  25 |   const date = info.dateStr;
     | This gives a short name to a value so the rest of handleDateClick can use it.

  26 |   const title = prompt("Task name?");
     | This gives a short name to a value so the rest of handleDateClick can use it.

  27 |   if (!title) return;
     | This asks a yes-or-no question. The next bit runs only on yes.

  28 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  29 |   api.post("/tasks", { title, dueAt: date });
     | This asks the server (the office that keeps tasks and accounts) for something, or sends it something.

  30 |   load();
     | Inside handleDateClick, this line runs as written: load();. It happens in order, after the line above it and before the line below it.

  31 | }
     | This ends handleDateClick (opened on line 23).

  32 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  33 | function handleEventClick(info) {
     | This starts handleEventClick. prompt() for a new datetime, PUT /tasks/:id, then load().

  34 |   const newDate = prompt("Update deadline (YYYY-MM-DD HH:mm)?", info.event.startStr);
     | This gives a short name to a value so the rest of handleEventClick can use it.

  35 |   if (!newDate) return;
     | This asks a yes-or-no question. The next bit runs only on yes.

  36 |   api.put(`/tasks/${info.event.id}`, { dueAt: newDate });
     | This asks the server (the office that keeps tasks and accounts) for something, or sends it something.

  37 |   load();
     | Inside handleEventClick, this line runs as written: load();. It happens in order, after the line above it and before the line below it.

  38 | }
     | This ends handleEventClick (opened on line 33).

  39 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  40 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  41 |   return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  42 |     <div>
     | This draws one piece of the page while Calendar is showing.

  43 |       <h1 className="page-title">Calendar</h1>
     | This draws one piece of the page while Calendar is showing.

  44 |       <p className="page-subtitle">Your tasks in calendar view</p>
     | This draws one piece of the page while Calendar is showing.

  45 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  46 |       <div className="card">
     | This draws one piece of the page while Calendar is showing.

  47 |         <FullCalendar
     | This draws one piece of the page while Calendar is showing.

  48 |           dateClick={handleDateClick}
     | This ends Calendar (opened on line 8).

  49 |   
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  50 |   
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  51 |           eventClick={handleEventClick}
     | This ends Calendar (opened on line 8).

  52 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  53 |           plugins={[dayGridPlugin, timeGridPlugin, interactionPlugin]}
     | This ends Calendar (opened on line 8).

  54 |           initialView="dayGridMonth"
     | Inside Calendar, this line runs as written: initialView="dayGridMonth". It happens in order, after the line above it and before the line below it.

  55 |           events={events}
     | This ends Calendar (opened on line 8).

  56 |           height={"80vh"}
     | This ends Calendar (opened on line 8).

  57 |         />
     | This closes a box of instructions that opened above.

  58 |       </div>
     | This ends a drawing that Calendar started just above.

  59 |     </div>
     | This ends a drawing that Calendar started just above.

  60 |   );
     | This closes a box of instructions that opened above.

  61 | }
     | This ends Calendar (opened on line 8).

  62 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

