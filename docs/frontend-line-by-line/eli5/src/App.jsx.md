# `src/App.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import React, { useEffect, useState } from "react";
     | Borrows React so this file can remember things and draw the screen.

   2 | import { Routes, Route, Link, NavLink, useLocation } from "react-router-dom";
     | Borrows React so this file can remember things and draw the screen.

   3 | import Logo from "./components/Logo";
     | This file borrows a tool another file already made.

   4 | import api from "./services/api";
     | This file borrows a tool another file already made.

   5 | import Auth from "./components/Auth";
     | This file borrows a tool another file already made.

   6 | import Home from "./components/Home";
     | This file borrows a tool another file already made.

   7 | import Dashboard from "./components/Dashboard";
     | This file borrows a tool another file already made.

   8 | import FocusTimer from "./components/FocusTimer";
     | This file borrows a tool another file already made.

   9 | import TodoList from "./components/TodoList";
     | This file borrows a tool another file already made.

  10 | import Mindfulness from "./components/Mindfulness";
     | This file borrows a tool another file already made.

  11 | import DeadlineTimer from "./components/DeadlineTimer";
     | This file borrows a tool another file already made.

  12 | import Calendar from "./components/Calendar";
     | This file borrows a tool another file already made.

  13 | import ConnectorsPage from "./components/ConnectorsPage";
     | This file borrows a tool another file already made.

  14 | import ProfileSettings from "./components/ProfileSettings";
     | This file borrows a tool another file already made.

  15 | import FocusShieldPage from "./components/focus-shield/FocusShieldPage";
     | This file borrows a tool another file already made.

  16 | import FocusOverlay from "./components/FocusOverlay";
     | This file borrows a tool another file already made.

  17 | import EnergyControl from "./components/EnergyControl";
     | This file borrows a tool another file already made.

  18 | import { useUser } from "./contexts/UserContext";
     | This file borrows a tool another file already made.

  19 | import { EnergyProvider } from "./contexts/EnergyContext";
     | This file borrows a tool another file already made.

  20 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  21 | // ── Icons ────────────────────────────────────────────────────────────────
     | A note written for people. The app does not run it.

  22 | const Icons = {
     | This gives a short name to a value so the rest of the top of the file can use it.

  23 |   Today: () => (
     | Inside the top of the file, this line runs as written: Today: () => (. It happens in order, after the line above it and before the line below it.

  24 |     <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}>
     | This draws one piece of the page while the top of the file is showing.

  25 |       <path d="M3 10L12 3l9 7v10a1 1 0 01-1 1H4a1 1 0 01-1-1V10z" />
     | This draws one piece of the page while the top of the file is showing.

  26 |       <path d="M9 21V12h6v9" />
     | This draws one piece of the page while the top of the file is showing.

  27 |     </svg>
     | This ends a drawing that the top of the file started just above.

  28 |   ),
     | This closes a box of instructions that opened above.

  29 |   Tasks: () => (
     | Inside the top of the file, this line runs as written: Tasks: () => (. It happens in order, after the line above it and before the line below it.

  30 |     <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}>
     | This draws one piece of the page while the top of the file is showing.

  31 |       <path d="M9 11l2 2 4-4" />
     | This draws one piece of the page while the top of the file is showing.

  32 |       <rect x="3" y="3" width="18" height="18" rx="3" />
     | This draws one piece of the page while the top of the file is showing.

  33 |     </svg>
     | This ends a drawing that the top of the file started just above.

  34 |   ),
     | This closes a box of instructions that opened above.

  35 |   Schedule: () => (
     | Inside the top of the file, this line runs as written: Schedule: () => (. It happens in order, after the line above it and before the line below it.

  36 |     <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}>
     | This draws one piece of the page while the top of the file is showing.

  37 |       <rect x="3" y="4" width="18" height="18" rx="2" />
     | This draws one piece of the page while the top of the file is showing.

  38 |       <path d="M16 2v4M8 2v4M3 10h18" />
     | This draws one piece of the page while the top of the file is showing.

  39 |     </svg>
     | This ends a drawing that the top of the file started just above.

  40 |   ),
     | This closes a box of instructions that opened above.

  41 |   Progress: () => (
     | Inside the top of the file, this line runs as written: Progress: () => (. It happens in order, after the line above it and before the line below it.

  42 |     <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}>
     | This draws one piece of the page while the top of the file is showing.

  43 |       <rect x="3" y="3" width="18" height="18" rx="2" />
     | This draws one piece of the page while the top of the file is showing.

  44 |       <path d="M8 17V13M12 17V9M16 17v-3" />
     | This draws one piece of the page while the top of the file is showing.

  45 |     </svg>
     | This ends a drawing that the top of the file started just above.

  46 |   ),
     | This closes a box of instructions that opened above.

  47 |   Sun: () => (
     | Inside the top of the file, this line runs as written: Sun: () => (. It happens in order, after the line above it and before the line below it.

  48 |     <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}>
     | This draws one piece of the page while the top of the file is showing.

  49 |       <circle cx="12" cy="12" r="4" />
     | This draws one piece of the page while the top of the file is showing.

  50 |       <path d="M12 2v2M12 20v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M2 12h2M20 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42" />
     | This draws one piece of the page while the top of the file is showing.

  51 |     </svg>
     | This ends a drawing that the top of the file started just above.

  52 |   ),
     | This closes a box of instructions that opened above.

  53 |   Moon: () => (
     | Inside the top of the file, this line runs as written: Moon: () => (. It happens in order, after the line above it and before the line below it.

  54 |     <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}>
     | This draws one piece of the page while the top of the file is showing.

  55 |       <path d="M21 12.79A9 9 0 1111.21 3 7 7 0 0021 12.79z" />
     | This draws one piece of the page while the top of the file is showing.

  56 |     </svg>
     | This ends a drawing that the top of the file started just above.

  57 |   ),
     | This closes a box of instructions that opened above.

  58 |   Logout: () => (
     | Inside the top of the file, this line runs as written: Logout: () => (. It happens in order, after the line above it and before the line below it.

  59 |     <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}>
     | This draws one piece of the page while the top of the file is showing.

  60 |       <path d="M9 21H5a2 2 0 01-2-2V5a2 2 0 012-2h4M16 17l5-5-5-5M21 12H9" />
     | This draws one piece of the page while the top of the file is showing.

  61 |     </svg>
     | This ends a drawing that the top of the file started just above.

  62 |   ),
     | This closes a box of instructions that opened above.

  63 |   Focus: () => (
     | Inside the top of the file, this line runs as written: Focus: () => (. It happens in order, after the line above it and before the line below it.

  64 |     <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}>
     | This draws one piece of the page while the top of the file is showing.

  65 |       <circle cx="12" cy="12" r="9" />
     | This draws one piece of the page while the top of the file is showing.

  66 |       <circle cx="12" cy="12" r="4" />
     | This draws one piece of the page while the top of the file is showing.

  67 |       <circle cx="12" cy="12" r="1" fill="currentColor" />
     | This draws one piece of the page while the top of the file is showing.

  68 |     </svg>
     | This ends a drawing that the top of the file started just above.

  69 |   ),
     | This closes a box of instructions that opened above.

  70 |   Settings: () => (
     | Inside the top of the file, this line runs as written: Settings: () => (. It happens in order, after the line above it and before the line below it.

  71 |     <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}>
     | This draws one piece of the page while the top of the file is showing.

  72 |       <circle cx="12" cy="12" r="3" />
     | This draws one piece of the page while the top of the file is showing.

  73 |       <path d="M19.07 4.93a10 10 0 010 14.14M4.93 4.93a10 10 0 000 14.14" />
     | This draws one piece of the page while the top of the file is showing.

  74 |     </svg>
     | This ends a drawing that the top of the file started just above.

  75 |   ),
     | This closes a box of instructions that opened above.

  76 |   Shield: () => (
     | Inside the top of the file, this line runs as written: Shield: () => (. It happens in order, after the line above it and before the line below it.

  77 |     <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}>
     | This draws one piece of the page while the top of the file is showing.

  78 |       <path d="M12 3l7 3v6c0 4.5-3 7.5-7 9-4-1.5-7-4.5-7-9V6l7-3z" />
     | This draws one piece of the page while the top of the file is showing.

  79 |       <path d="M9.5 12l1.8 1.8L15 10" />
     | This draws one piece of the page while the top of the file is showing.

  80 |     </svg>
     | This ends a drawing that the top of the file started just above.

  81 |   ),
     | This closes a box of instructions that opened above.

  82 |   Plug: () => (
     | Inside the top of the file, this line runs as written: Plug: () => (. It happens in order, after the line above it and before the line below it.

  83 |     <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}>
     | This draws one piece of the page while the top of the file is showing.

  84 |       <path d="M12 22V12M5 12H19M8 12V7a4 4 0 018 0v5" />
     | This draws one piece of the page while the top of the file is showing.

  85 |     </svg>
     | This ends a drawing that the top of the file started just above.

  86 |   ),
     | This closes a box of instructions that opened above.

  87 |   More: () => (
     | Inside the top of the file, this line runs as written: More: () => (. It happens in order, after the line above it and before the line below it.

  88 |     <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2} strokeLinecap="round">
     | This draws one piece of the page while the top of the file is showing.

  89 |       <circle cx="5" cy="12" r="1.5" fill="currentColor" stroke="none" />
     | This draws one piece of the page while the top of the file is showing.

  90 |       <circle cx="12" cy="12" r="1.5" fill="currentColor" stroke="none" />
     | This draws one piece of the page while the top of the file is showing.

  91 |       <circle cx="19" cy="12" r="1.5" fill="currentColor" stroke="none" />
     | This draws one piece of the page while the top of the file is showing.

  92 |     </svg>
     | This ends a drawing that the top of the file started just above.

  93 |   ),
     | This closes a box of instructions that opened above.

  94 |   Profile: () => (
     | Inside the top of the file, this line runs as written: Profile: () => (. It happens in order, after the line above it and before the line below it.

  95 |     <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}>
     | This draws one piece of the page while the top of the file is showing.

  96 |       <circle cx="12" cy="8" r="4" />
     | This draws one piece of the page while the top of the file is showing.

  97 |       <path d="M4 20c0-4 3.6-7 8-7s8 3 8 7" />
     | This draws one piece of the page while the top of the file is showing.

  98 |     </svg>
     | This ends a drawing that the top of the file started just above.

  99 |   ),
     | This closes a box of instructions that opened above.

 100 |   Coffee: () => (
     | Inside the top of the file, this line runs as written: Coffee: () => (. It happens in order, after the line above it and before the line below it.

 101 |     <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}>
     | This draws one piece of the page while the top of the file is showing.

 102 |       <path d="M18 8h1a3 3 0 010 6h-1" />
     | This draws one piece of the page while the top of the file is showing.

 103 |       <path d="M3 8h15v6a4 4 0 01-4 4H7a4 4 0 01-4-4V8z" />
     | This draws one piece of the page while the top of the file is showing.

 104 |       <path d="M6 2v2M10 2v2M14 2v2" />
     | This draws one piece of the page while the top of the file is showing.

 105 |     </svg>
     | This ends a drawing that the top of the file started just above.

 106 |   ),
     | This closes a box of instructions that opened above.

 107 |   Feedback: () => (
     | Inside the top of the file, this line runs as written: Feedback: () => (. It happens in order, after the line above it and before the line below it.

 108 |     <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}>
     | This draws one piece of the page while the top of the file is showing.

 109 |       <path d="M21 11.5a8.38 8.38 0 01-.9 3.8 8.5 8.5 0 01-7.6 4.7 8.38 8.38 0 01-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 01-.9-3.8 8.5 8.5 0 014.7-7.6 8.38 8.38 0 013.8-.9h.5a8.48 8.48 0 018 8v.5z" />
     | This draws one piece of the page while the top of the file is showing.

 110 |     </svg>
     | This ends a drawing that the top of the file started just above.

 111 |   ),
     | This closes a box of instructions that opened above.

 112 | };
     | This ends const Icons = { (opened on line 22).

 113 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 114 | // Sourced from .github/FUNDING.yml at build time (see vite.config.ts) so
     | A note written for people. The app does not run it.

 115 | // the in-app support link and the GitHub sponsor button never drift apart.
     | A note written for people. The app does not run it.

 116 | const FUNDING_URL = __FUNDING_URL__;
     | The Buy Me a Coffee URL injected at build time from .github/FUNDING.yml by vite.config.ts as __FUNDING_URL__.

 117 | const FEEDBACK_URL = "https://www.jumpybrain.com/#feedback";
     | Hard-coded link to https://www.jumpybrain.com/#feedback. The banner, sidebar, and top bar all open it in a new tab.

 118 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 119 | // Collapsed to 4 primary destinations
     | A note written for people. The app does not run it.

 120 | const NAV_ITEMS = [
     | The four primary routes: / Today, /todo Tasks, /calendar Schedule, /dashboard Progress. Sidebar, TopBar, and BottomNav all map this array.

 121 |   { to: "/",          label: "Today",    icon: Icons.Today },
     | This ends the nearest open block.

 122 |   { to: "/todo",      label: "Tasks",    icon: Icons.Tasks },
     | This ends the nearest open block.

 123 |   { to: "/calendar",  label: "Schedule", icon: Icons.Schedule },
     | This ends the nearest open block.

 124 |   { to: "/dashboard", label: "Progress", icon: Icons.Progress },
     | This ends the nearest open block.

 125 | ];
     | Inside the top of the file, this line runs as written: ];. It happens in order, after the line above it and before the line below it.

 126 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 127 | // Secondary pages accessible from sidebar "More" section
     | A note written for people. The app does not run it.

 128 | const SECONDARY_NAV = [
     | Routes tucked under More: /focus, /blocking, /mindful, /deadline, /settings.

 129 |   { to: "/focus",    label: "Focus Timer",  icon: Icons.Focus },
     | This ends the nearest open block.

 130 |   { to: "/blocking", label: "Focus Shield", icon: Icons.Shield },
     | This ends the nearest open block.

 131 |   { to: "/mindful",  label: "Mindfulness", icon: Icons.Today },
     | This ends the nearest open block.

 132 |   { to: "/deadline", label: "Deadlines",   icon: Icons.Schedule },
     | This ends the nearest open block.

 133 |   { to: "/settings", label: "Profile & Settings", icon: Icons.Profile },
     | This ends the nearest open block.

 134 | ];
     | Inside the top of the file, this line runs as written: ];. It happens in order, after the line above it and before the line below it.

 135 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 136 | const CONNECTORS = [
     | Gmail, Slack, and Google Calendar. Each entry knows the OAuth URL path and the sync path the buttons call.

 137 |   {
     | Inside the top of the file, this line runs as written: {. It happens in order, after the line above it and before the line below it.

 138 |     id: "gmail",
     | Inside the top of the file, this line runs as written: id: "gmail",. It happens in order, after the line above it and before the line below it.

 139 |     label: "Gmail",
     | Inside the top of the file, this line runs as written: label: "Gmail",. It happens in order, after the line above it and before the line below it.

 140 |     color: "#ea4335",
     | Inside the top of the file, this line runs as written: color: "#ea4335",. It happens in order, after the line above it and before the line below it.

 141 |     urlEndpoint: "/integrations/google/url",
     | Inside the top of the file, this line runs as written: urlEndpoint: "/integrations/google/url",. It happens in order, after the line above it and before the line below it.

 142 |     syncEndpoint: "/integrations/gmail/sync",
     | Inside the top of the file, this line runs as written: syncEndpoint: "/integrations/gmail/sync",. It happens in order, after the line above it and before the line below it.

 143 |     icon: () => (
     | Inside the top of the file, this line runs as written: icon: () => (. It happens in order, after the line above it and before the line below it.

 144 |       <svg viewBox="0 0 24 24" fill="currentColor" width="14" height="14">
     | This draws one piece of the page while the top of the file is showing.

 145 |         <path d="M20 4H4C2.9 4 2 4.9 2 6v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 2-8 5-8-5h16zm0 12H4V8l8 5 8-5v10z" />
     | This draws one piece of the page while the top of the file is showing.

 146 |       </svg>
     | This ends a drawing that the top of the file started just above.

 147 |     ),
     | This closes a box of instructions that opened above.

 148 |   },
     | This ends { (opened on line 137).

 149 |   {
     | Inside the top of the file, this line runs as written: {. It happens in order, after the line above it and before the line below it.

 150 |     id: "slack",
     | Inside the top of the file, this line runs as written: id: "slack",. It happens in order, after the line above it and before the line below it.

 151 |     label: "Slack",
     | Inside the top of the file, this line runs as written: label: "Slack",. It happens in order, after the line above it and before the line below it.

 152 |     color: "#4a154b",
     | Inside the top of the file, this line runs as written: color: "#4a154b",. It happens in order, after the line above it and before the line below it.

 153 |     urlEndpoint: "/integrations/slack/url",
     | Inside the top of the file, this line runs as written: urlEndpoint: "/integrations/slack/url",. It happens in order, after the line above it and before the line below it.

 154 |     syncEndpoint: "/integrations/slack/sync",
     | Inside the top of the file, this line runs as written: syncEndpoint: "/integrations/slack/sync",. It happens in order, after the line above it and before the line below it.

 155 |     icon: () => (
     | Inside the top of the file, this line runs as written: icon: () => (. It happens in order, after the line above it and before the line below it.

 156 |       <svg viewBox="0 0 24 24" fill="currentColor" width="14" height="14">
     | This draws one piece of the page while the top of the file is showing.

 157 |         <path d="M5.042 15.165a2.528 2.528 0 01-2.52 2.523A2.528 2.528 0 010 15.165a2.527 2.527 0 012.522-2.52h2.52v2.52zM6.313 15.165a2.527 2.527 0 012.521-2.52 2.527 2.527 0 012.521 2.52v6.313A2.528 2.528 0 018.834 24a2.528 2.528 0 01-2.521-2.522v-6.313zM8.834 5.042a2.528 2.528 0 01-2.521-2.52A2.528 2.528 0 018.834 0a2.528 2.528 0 012.521 2.522v2.52H8.834zM8.834 6.313a2.528 2.528 0 012.521 2.521 2.528 2.528 0 01-2.521 2.521H2.522A2.528 2.528 0 010 8.834a2.528 2.528 0 012.522-2.521h6.312zM18.956 8.834a2.528 2.528 0 012.522-2.521A2.528 2.528 0 0124 8.834a2.528 2.528 0 01-2.522 2.521h-2.522V8.834zM17.688 8.834a2.528 2.528 0 01-2.523 2.521 2.527 2.527 0 01-2.52-2.521V2.522A2.527 2.527 0 0115.165 0a2.528 2.528 0 012.523 2.522v6.312zM15.165 18.956a2.528 2.528 0 012.523 2.522A2.528 2.528 0 0115.165 24a2.527 2.527 0 01-2.52-2.522v-2.522h2.52zM15.165 17.688a2.527 2.527 0 01-2.52-2.523 2.526 2.526 0 012.52-2.52h6.313A2.527 2.527 0 0124 15.165a2.528 2.528 0 01-2.522 2.523h-6.313z" />
     | This draws one piece of the page while the top of the file is showing.

 158 |       </svg>
     | This ends a drawing that the top of the file started just above.

 159 |     ),
     | This closes a box of instructions that opened above.

 160 |   },
     | This ends { (opened on line 149).

 161 |   {
     | Inside the top of the file, this line runs as written: {. It happens in order, after the line above it and before the line below it.

 162 |     id: "gcal",
     | Inside the top of the file, this line runs as written: id: "gcal",. It happens in order, after the line above it and before the line below it.

 163 |     label: "Google Cal",
     | Inside the top of the file, this line runs as written: label: "Google Cal",. It happens in order, after the line above it and before the line below it.

 164 |     color: "#1a73e8",
     | Inside the top of the file, this line runs as written: color: "#1a73e8",. It happens in order, after the line above it and before the line below it.

 165 |     urlEndpoint: "/integrations/google/url",
     | Inside the top of the file, this line runs as written: urlEndpoint: "/integrations/google/url",. It happens in order, after the line above it and before the line below it.

 166 |     syncEndpoint: "/integrations/gcal/sync",
     | Inside the top of the file, this line runs as written: syncEndpoint: "/integrations/gcal/sync",. It happens in order, after the line above it and before the line below it.

 167 |     icon: () => (
     | Inside the top of the file, this line runs as written: icon: () => (. It happens in order, after the line above it and before the line below it.

 168 |       <svg viewBox="0 0 24 24" fill="currentColor" width="14" height="14">
     | This draws one piece of the page while the top of the file is showing.

 169 |         <path d="M19 3h-1V1h-2v2H8V1H6v2H5C3.9 3 3 3.9 3 5v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V8h14v11zM7 10h5v5H7z" />
     | This draws one piece of the page while the top of the file is showing.

 170 |       </svg>
     | This ends a drawing that the top of the file started just above.

 171 |     ),
     | This closes a box of instructions that opened above.

 172 |   },
     | This ends { (opened on line 161).

 173 | ];
     | Inside the top of the file, this line runs as written: ];. It happens in order, after the line above it and before the line below it.

 174 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 175 | function Sidebar({ theme, setTheme, onLogout, open, onClose }) {
     | This starts Sidebar. Left navigation. Renders NAV_ITEMS, SECONDARY_NAV, connector links to /connectors, the compact energy control, coffee, theme, and logout. It does not fetch data.

 176 |   const location = useLocation();
     | This gives a short name to a value so the rest of Sidebar can use it.

 177 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 178 |   return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

 179 |     <>
     | This draws one piece of the page while Sidebar is showing.

 180 |       {open && <div className="sidebar-backdrop" onClick={onClose} />}
     | This decides what happens when you press.

 181 |       <nav className={`sidebar${open ? " open" : ""}`} role="navigation" aria-label="Main navigation">
     | This draws one piece of the page while Sidebar is showing.

 182 |         {/* Brand */}
     | This ends Sidebar (opened on line 175).

 183 |         <div className="sidebar-brand">
     | This draws one piece of the page while Sidebar is showing.

 184 |           <div className="sidebar-logo">
     | This draws one piece of the page while Sidebar is showing.

 185 |             <Logo size={36} variant="icon" />
     | This draws one piece of the page while Sidebar is showing.

 186 |           </div>
     | This ends a drawing that Sidebar started just above.

 187 |           <div>
     | This draws one piece of the page while Sidebar is showing.

 188 |             <div className="sidebar-title">Jumpy<span>Brain</span></div>
     | This draws one piece of the page while Sidebar is showing.

 189 |             <div className="sidebar-subtitle">Focus. Do more.</div>
     | This draws one piece of the page while Sidebar is showing.

 190 |           </div>
     | This ends a drawing that Sidebar started just above.

 191 |         </div>
     | This ends a drawing that Sidebar started just above.

 192 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 193 |         {/* Primary nav — 4 destinations */}
     | This ends Sidebar (opened on line 175).

 194 |         <div className="sidebar-nav-section">
     | This draws one piece of the page while Sidebar is showing.

 195 |           {NAV_ITEMS.map(({ to, label, icon: Icon }) => (
     | This ends Sidebar (opened on line 175).

 196 |             <NavLink
     | This draws one piece of the page while Sidebar is showing.

 197 |               key={to}
     | This ends Sidebar (opened on line 175).

 198 |               to={to}
     | This ends Sidebar (opened on line 175).

 199 |               end={to === "/"}
     | This ends Sidebar (opened on line 175).

 200 |               className={({ isActive }) => `nav-item${isActive ? " active" : ""}`}
     | This ends Sidebar (opened on line 175).

 201 |               onClick={onClose}
     | This decides what happens when you press.

 202 |             >
     | Inside Sidebar, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 203 |               <Icon />
     | This draws one piece of the page while Sidebar is showing.

 204 |               {label}
     | This ends Sidebar (opened on line 175).

 205 |             </NavLink>
     | This ends a drawing that Sidebar started just above.

 206 |           ))}
     | This ends Sidebar (opened on line 175).

 207 |         </div>
     | This ends a drawing that Sidebar started just above.

 208 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 209 |         {/* Secondary nav */}
     | This ends Sidebar (opened on line 175).

 210 |         <div className="sidebar-nav-section" style={{ marginTop: 8 }}>
     | This draws one piece of the page while Sidebar is showing.

 211 |           <div className="sidebar-section-label">More</div>
     | This draws one piece of the page while Sidebar is showing.

 212 |           {SECONDARY_NAV.map(({ to, label, icon: Icon }) => (
     | This ends Sidebar (opened on line 175).

 213 |             <NavLink
     | This draws one piece of the page while Sidebar is showing.

 214 |               key={to}
     | This ends Sidebar (opened on line 175).

 215 |               to={to}
     | This ends Sidebar (opened on line 175).

 216 |               className={({ isActive }) => `nav-item nav-item-sm${isActive ? " active" : ""}`}
     | This ends Sidebar (opened on line 175).

 217 |               onClick={onClose}
     | This decides what happens when you press.

 218 |             >
     | Inside Sidebar, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 219 |               <Icon />
     | This draws one piece of the page while Sidebar is showing.

 220 |               {label}
     | This ends Sidebar (opened on line 175).

 221 |             </NavLink>
     | This ends a drawing that Sidebar started just above.

 222 |           ))}
     | This ends Sidebar (opened on line 175).

 223 |           <a
     | This draws one piece of the page while Sidebar is showing.

 224 |             href={FEEDBACK_URL}
     | This ends Sidebar (opened on line 175).

 225 |             target="_blank"
     | Inside Sidebar, this line runs as written: target="_blank". It happens in order, after the line above it and before the line below it.

 226 |             rel="noopener noreferrer"
     | Inside Sidebar, this line runs as written: rel="noopener noreferrer". It happens in order, after the line above it and before the line below it.

 227 |             className="nav-item nav-item-sm nav-item-feedback"
     | Inside Sidebar, this line runs as written: className="nav-item nav-item-sm nav-item-feedback". It happens in order, after the line above it and before the line below it.

 228 |             onClick={onClose}
     | This decides what happens when you press.

 229 |           >
     | Inside Sidebar, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 230 |             <Icons.Feedback />
     | This draws one piece of the page while Sidebar is showing.

 231 |             Feedback
     | Inside Sidebar, this line runs as written: Feedback. It happens in order, after the line above it and before the line below it.

 232 |           </a>
     | This ends a drawing that Sidebar started just above.

 233 |         </div>
     | This ends a drawing that Sidebar started just above.

 234 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 235 |         {/* Connectors — compact rows */}
     | This ends Sidebar (opened on line 175).

 236 |         <div className="sidebar-nav-section" style={{ marginTop: 8 }}>
     | This draws one piece of the page while Sidebar is showing.

 237 |           <div className="sidebar-section-label">Connectors</div>
     | This draws one piece of the page while Sidebar is showing.

 238 |           {CONNECTORS.map(({ id, label, color, icon: Icon }) => (
     | This ends Sidebar (opened on line 175).

 239 |             <Link
     | This draws one piece of the page while Sidebar is showing.

 240 |               key={id}
     | This ends Sidebar (opened on line 175).

 241 |               to="/connectors"
     | Inside Sidebar, this line runs as written: to="/connectors". It happens in order, after the line above it and before the line below it.

 242 |               className={`connector-row${location.pathname === "/connectors" ? " active" : ""}`}
     | This ends Sidebar (opened on line 175).

 243 |               onClick={onClose}
     | This decides what happens when you press.

 244 |             >
     | Inside Sidebar, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 245 |               <span className="connector-row-icon" style={{ color, background: color + "20" }}>
     | This draws one piece of the page while Sidebar is showing.

 246 |                 <Icon />
     | This draws one piece of the page while Sidebar is showing.

 247 |               </span>
     | This ends a drawing that Sidebar started just above.

 248 |               <span className="connector-row-label">{label}</span>
     | This draws one piece of the page while Sidebar is showing.

 249 |             </Link>
     | This ends a drawing that Sidebar started just above.

 250 |           ))}
     | This ends Sidebar (opened on line 175).

 251 |         </div>
     | This ends a drawing that Sidebar started just above.

 252 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 253 |         {/* Pinned energy control */}
     | This ends Sidebar (opened on line 175).

 254 |         <div className="sidebar-energy">
     | This draws one piece of the page while Sidebar is showing.

 255 |           <div className="sidebar-section-label">Energy level</div>
     | This draws one piece of the page while Sidebar is showing.

 256 |           <EnergyControl compact />
     | This draws one piece of the page while Sidebar is showing.

 257 |         </div>
     | This ends a drawing that Sidebar started just above.

 258 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 259 |         {/* Footer controls */}
     | This ends Sidebar (opened on line 175).

 260 |         <div className="sidebar-footer">
     | This draws one piece of the page while Sidebar is showing.

 261 |           <a
     | This draws one piece of the page while Sidebar is showing.

 262 |             href={FUNDING_URL}
     | This ends Sidebar (opened on line 175).

 263 |             target="_blank"
     | Inside Sidebar, this line runs as written: target="_blank". It happens in order, after the line above it and before the line below it.

 264 |             rel="noopener noreferrer"
     | Inside Sidebar, this line runs as written: rel="noopener noreferrer". It happens in order, after the line above it and before the line below it.

 265 |             className="support-btn"
     | Inside Sidebar, this line runs as written: className="support-btn". It happens in order, after the line above it and before the line below it.

 266 |             aria-label="Buy me a coffee (opens buymeacoffee.com in a new tab)"
     | Inside Sidebar, this line runs as written: aria-label="Buy me a coffee (opens buymeacoffee.com in a new tab)". It happens in order, after the line above it and before the line below it.

 267 |           >
     | Inside Sidebar, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 268 |             <Icons.Coffee />
     | This draws one piece of the page while Sidebar is showing.

 269 |             Buy me a coffee
     | Inside Sidebar, this line runs as written: Buy me a coffee. It happens in order, after the line above it and before the line below it.

 270 |           </a>
     | This ends a drawing that Sidebar started just above.

 271 |           <button
     | This draws one piece of the page while Sidebar is showing.

 272 |             className="theme-toggle"
     | Inside Sidebar, this line runs as written: className="theme-toggle". It happens in order, after the line above it and before the line below it.

 273 |             onClick={() => setTheme((t) => (t === "dark" ? "light" : "dark"))}
     | This decides what happens when you press.

 274 |             aria-label="Toggle theme"
     | Inside Sidebar, this line runs as written: aria-label="Toggle theme". It happens in order, after the line above it and before the line below it.

 275 |           >
     | Inside Sidebar, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 276 |             {theme === "dark" ? <Icons.Sun /> : <Icons.Moon />}
     | This ends Sidebar (opened on line 175).

 277 |             {theme === "dark" ? "Light mode" : "Dark mode"}
     | This ends Sidebar (opened on line 175).

 278 |           </button>
     | This ends a drawing that Sidebar started just above.

 279 |           <button className="logout-btn" onClick={onLogout} aria-label="Logout">
     | This draws one piece of the page while Sidebar is showing.

 280 |             <Icons.Logout />
     | This draws one piece of the page while Sidebar is showing.

 281 |             Logout
     | Inside Sidebar, this line runs as written: Logout. It happens in order, after the line above it and before the line below it.

 282 |           </button>
     | This ends a drawing that Sidebar started just above.

 283 |         </div>
     | This ends a drawing that Sidebar started just above.

 284 |       </nav>
     | This ends a drawing that Sidebar started just above.

 285 |     </>
     | This ends a drawing that Sidebar started just above.

 286 |   );
     | This closes a box of instructions that opened above.

 287 | }
     | This ends Sidebar (opened on line 175).

 288 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 289 | function TopBar({ theme, setTheme, onMenuClick, onMoreClick, onLogout }) {
     | This starts TopBar. The bar above the page. The title is whichever nav item matches the URL. Initials come from the user name. Buttons open the sidebar, the More sheet, connectors, feedback, theme, settings, and logout.

 290 |   const location = useLocation();
     | This gives a short name to a value so the rest of TopBar can use it.

 291 |   const { user } = useUser();
     | The logged-in profile object. Null means ProtectedRoute renders Auth.

 292 |   const currentNav = [...NAV_ITEMS, ...SECONDARY_NAV].find((n) =>
     | This gives a short name to a value so the rest of TopBar can use it.

 293 |     n.to === "/" ? location.pathname === "/" : location.pathname.startsWith(n.to)
     | Inside TopBar, this line runs as written: n.to === "/" ? location.pathname === "/" : location.pathname.startsWith(n.to). It happens in order, after the line above it and before the line below it.

 294 |   );
     | This closes a box of instructions that opened above.

 295 |   const pageTitle = currentNav?.label ?? "JumpyBrain";
     | This gives a short name to a value so the rest of TopBar can use it.

 296 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 297 |   const initials = user?.name
     | This gives a short name to a value so the rest of TopBar can use it.

 298 |     ? user.name.trim().split(/\s+/).slice(0, 2).map((w) => w[0].toUpperCase()).join("")
     | Inside TopBar, this line runs as written: ? user.name.trim().split(/\s+/).slice(0, 2).map((w) => w[0].toUpperCase()).join(""). It happens in order, after the line above it and before the line below it.

 299 |     : (user?.email || "?")[0].toUpperCase();
     | Inside TopBar, this line runs as written: : (user?.email || "?")[0].toUpperCase();. It happens in order, after the line above it and before the line below it.

 300 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 301 |   return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

 302 |     <header className="top-bar" role="banner">
     | This draws one piece of the page while TopBar is showing.

 303 |       <div className="top-bar-left">
     | This draws one piece of the page while TopBar is showing.

 304 |         <button
     | This draws one piece of the page while TopBar is showing.

 305 |           className="top-bar-menu-btn"
     | Inside TopBar, this line runs as written: className="top-bar-menu-btn". It happens in order, after the line above it and before the line below it.

 306 |           onClick={onMenuClick}
     | This decides what happens when you press.

 307 |           aria-label="Open navigation menu"
     | Inside TopBar, this line runs as written: aria-label="Open navigation menu". It happens in order, after the line above it and before the line below it.

 308 |         >
     | Inside TopBar, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 309 |           <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2.2} strokeLinecap="round">
     | This draws one piece of the page while TopBar is showing.

 310 |             <line x1="3" y1="6" x2="21" y2="6" />
     | This draws one piece of the page while TopBar is showing.

 311 |             <line x1="3" y1="12" x2="21" y2="12" />
     | This draws one piece of the page while TopBar is showing.

 312 |             <line x1="3" y1="18" x2="21" y2="18" />
     | This draws one piece of the page while TopBar is showing.

 313 |           </svg>
     | This ends a drawing that TopBar started just above.

 314 |         </button>
     | This ends a drawing that TopBar started just above.

 315 |         <div className="top-bar-brand">
     | This draws one piece of the page while TopBar is showing.

 316 |           <Logo size={28} variant="icon" />
     | This draws one piece of the page while TopBar is showing.

 317 |           <span className="top-bar-page-title">{pageTitle}</span>
     | This draws one piece of the page while TopBar is showing.

 318 |         </div>
     | This ends a drawing that TopBar started just above.

 319 |       </div>
     | This ends a drawing that TopBar started just above.

 320 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 321 |       <div className="top-bar-right">
     | This draws one piece of the page while TopBar is showing.

 322 |         <button
     | This draws one piece of the page while TopBar is showing.

 323 |           className="top-bar-icon-btn top-bar-more-btn"
     | Inside TopBar, this line runs as written: className="top-bar-icon-btn top-bar-more-btn". It happens in order, after the line above it and before the line below it.

 324 |           onClick={onMoreClick}
     | This decides what happens when you press.

 325 |           aria-label="More — Focus Timer, Focus Shield, Mindfulness, Deadlines"
     | Inside TopBar, this line runs as written: aria-label="More — Focus Timer, Focus Shield, Mindfulness, Deadlines". It happens in order, after the line above it and before the line below it.

 326 |           title="More"
     | Inside TopBar, this line runs as written: title="More". It happens in order, after the line above it and before the line below it.

 327 |         >
     | Inside TopBar, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 328 |           <Icons.More />
     | This draws one piece of the page while TopBar is showing.

 329 |         </button>
     | This ends a drawing that TopBar started just above.

 330 |         <Link
     | This draws one piece of the page while TopBar is showing.

 331 |           to="/connectors"
     | Inside TopBar, this line runs as written: to="/connectors". It happens in order, after the line above it and before the line below it.

 332 |           className="top-bar-icon-btn"
     | Inside TopBar, this line runs as written: className="top-bar-icon-btn". It happens in order, after the line above it and before the line below it.

 333 |           title="Connectors"
     | Inside TopBar, this line runs as written: title="Connectors". It happens in order, after the line above it and before the line below it.

 334 |           aria-label="Manage connectors"
     | Inside TopBar, this line runs as written: aria-label="Manage connectors". It happens in order, after the line above it and before the line below it.

 335 |         >
     | Inside TopBar, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 336 |           <Icons.Plug />
     | This draws one piece of the page while TopBar is showing.

 337 |         </Link>
     | This ends a drawing that TopBar started just above.

 338 |         <a
     | This draws one piece of the page while TopBar is showing.

 339 |           href={FEEDBACK_URL}
     | This ends TopBar (opened on line 289).

 340 |           target="_blank"
     | Inside TopBar, this line runs as written: target="_blank". It happens in order, after the line above it and before the line below it.

 341 |           rel="noopener noreferrer"
     | Inside TopBar, this line runs as written: rel="noopener noreferrer". It happens in order, after the line above it and before the line below it.

 342 |           className="top-bar-icon-btn top-bar-feedback-btn"
     | Inside TopBar, this line runs as written: className="top-bar-icon-btn top-bar-feedback-btn". It happens in order, after the line above it and before the line below it.

 343 |           title="Share feedback"
     | Inside TopBar, this line runs as written: title="Share feedback". It happens in order, after the line above it and before the line below it.

 344 |           aria-label="Share feedback"
     | Inside TopBar, this line runs as written: aria-label="Share feedback". It happens in order, after the line above it and before the line below it.

 345 |         >
     | Inside TopBar, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 346 |           <Icons.Feedback />
     | This draws one piece of the page while TopBar is showing.

 347 |         </a>
     | This ends a drawing that TopBar started just above.

 348 |         <button
     | This draws one piece of the page while TopBar is showing.

 349 |           className="top-bar-icon-btn"
     | Inside TopBar, this line runs as written: className="top-bar-icon-btn". It happens in order, after the line above it and before the line below it.

 350 |           onClick={() => setTheme((t) => (t === "dark" ? "light" : "dark"))}
     | This decides what happens when you press.

 351 |           aria-label="Toggle theme"
     | Inside TopBar, this line runs as written: aria-label="Toggle theme". It happens in order, after the line above it and before the line below it.

 352 |         >
     | Inside TopBar, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 353 |           {theme === "dark" ? <Icons.Sun /> : <Icons.Moon />}
     | This ends TopBar (opened on line 289).

 354 |         </button>
     | This ends a drawing that TopBar started just above.

 355 |         <Link
     | This draws one piece of the page while TopBar is showing.

 356 |           to="/settings"
     | Inside TopBar, this line runs as written: to="/settings". It happens in order, after the line above it and before the line below it.

 357 |           className="top-bar-avatar"
     | Inside TopBar, this line runs as written: className="top-bar-avatar". It happens in order, after the line above it and before the line below it.

 358 |           title="Profile & Settings"
     | Inside TopBar, this line runs as written: title="Profile & Settings". It happens in order, after the line above it and before the line below it.

 359 |           aria-label="Profile and settings"
     | Inside TopBar, this line runs as written: aria-label="Profile and settings". It happens in order, after the line above it and before the line below it.

 360 |         >
     | Inside TopBar, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 361 |           {initials}
     | This ends TopBar (opened on line 289).

 362 |         </Link>
     | This ends a drawing that TopBar started just above.

 363 |         <button
     | This draws one piece of the page while TopBar is showing.

 364 |           className="top-bar-icon-btn top-bar-logout-btn"
     | Inside TopBar, this line runs as written: className="top-bar-icon-btn top-bar-logout-btn". It happens in order, after the line above it and before the line below it.

 365 |           onClick={onLogout}
     | This decides what happens when you press.

 366 |           aria-label="Logout"
     | Inside TopBar, this line runs as written: aria-label="Logout". It happens in order, after the line above it and before the line below it.

 367 |           title="Logout"
     | Inside TopBar, this line runs as written: title="Logout". It happens in order, after the line above it and before the line below it.

 368 |         >
     | Inside TopBar, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 369 |           <Icons.Logout />
     | This draws one piece of the page while TopBar is showing.

 370 |         </button>
     | This ends a drawing that TopBar started just above.

 371 |       </div>
     | This ends a drawing that TopBar started just above.

 372 |     </header>
     | This ends a drawing that TopBar started just above.

 373 |   );
     | This closes a box of instructions that opened above.

 374 | }
     | This ends TopBar (opened on line 289).

 375 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 376 | // Bottom nav for mobile (4 primary destinations + Profile & Settings)
     | A note written for people. The app does not run it.

 377 | function BottomNav({ onLogout }) {
     | This starts BottomNav. Phone navigation: the four primary routes plus Profile. CSS hides it on wide screens.

 378 |   return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

 379 |     <nav className="bottom-nav" aria-label="Mobile navigation">
     | This draws one piece of the page while BottomNav is showing.

 380 |       {NAV_ITEMS.map(({ to, label, icon: Icon }) => (
     | This ends BottomNav (opened on line 377).

 381 |         <NavLink
     | This draws one piece of the page while BottomNav is showing.

 382 |           key={to}
     | This ends BottomNav (opened on line 377).

 383 |           to={to}
     | This ends BottomNav (opened on line 377).

 384 |           end={to === "/"}
     | This ends BottomNav (opened on line 377).

 385 |           className={({ isActive }) => `bottom-nav-item${isActive ? " active" : ""}`}
     | This ends BottomNav (opened on line 377).

 386 |         >
     | Inside BottomNav, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 387 |           <Icon />
     | This draws one piece of the page while BottomNav is showing.

 388 |           <span>{label}</span>
     | This draws one piece of the page while BottomNav is showing.

 389 |         </NavLink>
     | This ends a drawing that BottomNav started just above.

 390 |       ))}
     | This ends BottomNav (opened on line 377).

 391 |       <NavLink
     | This draws one piece of the page while BottomNav is showing.

 392 |         to="/settings"
     | Inside BottomNav, this line runs as written: to="/settings". It happens in order, after the line above it and before the line below it.

 393 |         className={({ isActive }) => `bottom-nav-item${isActive ? " active" : ""}`}
     | This ends BottomNav (opened on line 377).

 394 |         aria-label="Profile & Settings"
     | Inside BottomNav, this line runs as written: aria-label="Profile & Settings". It happens in order, after the line above it and before the line below it.

 395 |       >
     | Inside BottomNav, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 396 |         <Icons.Profile />
     | This draws one piece of the page while BottomNav is showing.

 397 |         <span>Profile</span>
     | This draws one piece of the page while BottomNav is showing.

 398 |       </NavLink>
     | This ends a drawing that BottomNav started just above.

 399 |     </nav>
     | This ends a drawing that BottomNav started just above.

 400 |   );
     | This closes a box of instructions that opened above.

 401 | }
     | This ends BottomNav (opened on line 377).

 402 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 403 | function SheetConnectors({ open }) {
     | This starts SheetConnectors. The connector rows inside the More sheet. On open it GET /integrations/status. Connect redirects to the OAuth URL. Sync POSTs. Disconnect DELETEs.

 404 |   const [status, setStatus] = useState(null);
     | This gives a short name to a value so the rest of SheetConnectors can use it.

 405 |   const [syncing, setSyncing] = useState({});
     | This gives a short name to a value so the rest of SheetConnectors can use it.

 406 |   const [connecting, setConnecting] = useState({});
     | This gives a short name to a value so the rest of SheetConnectors can use it.

 407 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 408 |   useEffect(() => {
     | This is an extra job that happens after the picture is drawn.

 409 |     if (!open) return;
     | This asks a yes-or-no question. The next bit runs only on yes.

 410 |     api.get('/integrations/status').then(setStatus).catch(() => {});
     | This asks the server (the office that keeps tasks and accounts) for something, or sends it something.

 411 |   }, [open]);
     | This ends effect in SheetConnectors (opened on line 408).

 412 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 413 |   async function handleConnect(connector) {
     | This starts handleConnect. GET the connector's urlEndpoint and set window.location to that OAuth URL.

 414 |     setConnecting(p => ({ ...p, [connector.id]: true }));
     | This ends handleConnect (opened on line 413).

 415 |     try {
     | Inside handleConnect, this line runs as written: try {. It happens in order, after the line above it and before the line below it.

 416 |       const { url } = await api.get(connector.urlEndpoint);
     | This gives a short name to a value so the rest of handleConnect can use it.

 417 |       window.location.href = url;
     | Inside handleConnect, this line runs as written: window.location.href = url;. It happens in order, after the line above it and before the line below it.

 418 |     } catch {
     | This ends try { (opened on line 415).

 419 |       setConnecting(p => ({ ...p, [connector.id]: false }));
     | This ends } catch { (opened on line 418).

 420 |     }
     | This ends } catch { (opened on line 418).

 421 |   }
     | This ends handleConnect (opened on line 413).

 422 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 423 |   async function handleSync(connector) {
     | This starts handleSync. POST the sync endpoint. The page toast includes result.synced and result.created.

 424 |     setSyncing(p => ({ ...p, [connector.id]: true }));
     | This ends handleSync (opened on line 423).

 425 |     try {
     | Inside handleSync, this line runs as written: try {. It happens in order, after the line above it and before the line below it.

 426 |       await api.post(connector.syncEndpoint);
     | This asks the server (the office that keeps tasks and accounts) for something, or sends it something.

 427 |       const data = await api.get('/integrations/status');
     | This gives a short name to a value so the rest of handleSync can use it.

 428 |       setStatus(data);
     | Inside handleSync, this line runs as written: setStatus(data);. It happens in order, after the line above it and before the line below it.

 429 |     } catch {
     | This ends try { (opened on line 425).

 430 |     } finally {
     | This ends } catch { (opened on line 429).

 431 |       setSyncing(p => ({ ...p, [connector.id]: false }));
     | This ends } finally { (opened on line 430).

 432 |     }
     | This ends } finally { (opened on line 430).

 433 |   }
     | This ends handleSync (opened on line 423).

 434 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 435 |   async function handleDisconnect(connector) {
     | This starts handleDisconnect. DELETE /integrations/:id and refresh status.

 436 |     try {
     | Inside handleDisconnect, this line runs as written: try {. It happens in order, after the line above it and before the line below it.

 437 |       await api.delete(`/integrations/${connector.id}`);
     | This asks the server (the office that keeps tasks and accounts) for something, or sends it something.

 438 |       const data = await api.get('/integrations/status');
     | This gives a short name to a value so the rest of handleDisconnect can use it.

 439 |       setStatus(data);
     | Inside handleDisconnect, this line runs as written: setStatus(data);. It happens in order, after the line above it and before the line below it.

 440 |     } catch {}
     | This ends try { (opened on line 436).

 441 |   }
     | This ends handleDisconnect (opened on line 435).

 442 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 443 |   return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

 444 |     <div className="sheet-connectors">
     | This draws one piece of the page while SheetConnectors is showing.

 445 |       <div className="sidebar-section-label">Connectors</div>
     | This draws one piece of the page while SheetConnectors is showing.

 446 |       {CONNECTORS.map((connector) => {
     | Inside SheetConnectors, this line runs as written: {CONNECTORS.map((connector) => {. It happens in order, after the line above it and before the line below it.

 447 |         const s = status?.[connector.id];
     | This gives a short name to a value so the rest of SheetConnectors can use it.

 448 |         const isConnected = !!s?.connected;
     | This gives a short name to a value so the rest of SheetConnectors can use it.

 449 |         const Icon = connector.icon;
     | This gives a short name to a value so the rest of SheetConnectors can use it.

 450 |         return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

 451 |           <div key={connector.id} className="sheet-connector-row">
     | This draws one piece of the page while SheetConnectors is showing.

 452 |             <span className="sheet-connector-icon" style={{ color: connector.color, background: connector.color + '18' }}>
     | This draws one piece of the page while SheetConnectors is showing.

 453 |               <Icon />
     | This draws one piece of the page while SheetConnectors is showing.

 454 |             </span>
     | This ends a drawing that SheetConnectors started just above.

 455 |             <span className="sheet-connector-label">{connector.label}</span>
     | This draws one piece of the page while SheetConnectors is showing.

 456 |             <span className={`sheet-connector-dot${isConnected ? ' connected' : ''}`} />
     | This draws one piece of the page while SheetConnectors is showing.

 457 |             {isConnected ? (
     | Inside SheetConnectors, this line runs as written: {isConnected ? (. It happens in order, after the line above it and before the line below it.

 458 |               <>
     | This draws one piece of the page while SheetConnectors is showing.

 459 |                 <button
     | This draws one piece of the page while SheetConnectors is showing.

 460 |                   className="sheet-connector-btn"
     | Inside SheetConnectors, this line runs as written: className="sheet-connector-btn". It happens in order, after the line above it and before the line below it.

 461 |                   onClick={() => handleSync(connector)}
     | This decides what happens when you press.

 462 |                   disabled={syncing[connector.id]}
     | This ends {CONNECTORS.map((connector) => { (opened on line 446).

 463 |                 >
     | Inside SheetConnectors, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 464 |                   {syncing[connector.id] ? '…' : 'Sync'}
     | This ends {CONNECTORS.map((connector) => { (opened on line 446).

 465 |                 </button>
     | This ends a drawing that SheetConnectors started just above.

 466 |                 <button
     | This draws one piece of the page while SheetConnectors is showing.

 467 |                   className="sheet-connector-btn sheet-connector-btn--off"
     | Inside SheetConnectors, this line runs as written: className="sheet-connector-btn sheet-connector-btn--off". It happens in order, after the line above it and before the line below it.

 468 |                   onClick={() => handleDisconnect(connector)}
     | This decides what happens when you press.

 469 |                   aria-label={`Disconnect ${connector.label}`}
     | This ends {CONNECTORS.map((connector) => { (opened on line 446).

 470 |                 >
     | Inside SheetConnectors, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 471 |                   ×
     | Inside SheetConnectors, this line runs as written: ×. It happens in order, after the line above it and before the line below it.

 472 |                 </button>
     | This ends a drawing that SheetConnectors started just above.

 473 |               </>
     | This ends a drawing that SheetConnectors started just above.

 474 |             ) : (
     | This closes a box of instructions that opened above.

 475 |               <button
     | This draws one piece of the page while SheetConnectors is showing.

 476 |                 className="sheet-connector-btn sheet-connector-btn--on"
     | Inside SheetConnectors, this line runs as written: className="sheet-connector-btn sheet-connector-btn--on". It happens in order, after the line above it and before the line below it.

 477 |                 onClick={() => handleConnect(connector)}
     | This decides what happens when you press.

 478 |                 disabled={connecting[connector.id]}
     | This ends {CONNECTORS.map((connector) => { (opened on line 446).

 479 |                 style={{ '--c': connector.color }}
     | This ends {CONNECTORS.map((connector) => { (opened on line 446).

 480 |               >
     | Inside SheetConnectors, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 481 |                 {connecting[connector.id] ? '…' : 'Connect'}
     | This ends {CONNECTORS.map((connector) => { (opened on line 446).

 482 |               </button>
     | This ends a drawing that SheetConnectors started just above.

 483 |             )}
     | This ends {CONNECTORS.map((connector) => { (opened on line 446).

 484 |           </div>
     | This ends a drawing that SheetConnectors started just above.

 485 |         );
     | This closes a box of instructions that opened above.

 486 |       })}
     | This ends {CONNECTORS.map((connector) => { (opened on line 446).

 487 |     </div>
     | This ends a drawing that SheetConnectors started just above.

 488 |   );
     | This closes a box of instructions that opened above.

 489 | }
     | This ends SheetConnectors (opened on line 403).

 490 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 491 | // Slide-up sheet for secondary nav on mobile
     | A note written for people. The app does not run it.

 492 | function MoreSheet({ open, onClose, theme, setTheme, onLogout }) {
     | This starts MoreSheet. The slide-up sheet on small screens: secondary links, SheetConnectors, energy, coffee, theme, logout.

 493 |   return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

 494 |     <>
     | This draws one piece of the page while MoreSheet is showing.

 495 |       <div
     | This draws one piece of the page while MoreSheet is showing.

 496 |         className={`bottom-sheet-overlay${open ? " open" : ""}`}
     | This ends MoreSheet (opened on line 492).

 497 |         onClick={onClose}
     | This decides what happens when you press.

 498 |         aria-hidden="true"
     | Inside MoreSheet, this line runs as written: aria-hidden="true". It happens in order, after the line above it and before the line below it.

 499 |       />
     | This closes a box of instructions that opened above.

 500 |       <div
     | This draws one piece of the page while MoreSheet is showing.

 501 |         className={`bottom-sheet${open ? " open" : ""}`}
     | This ends MoreSheet (opened on line 492).

 502 |         role="dialog"
     | Inside MoreSheet, this line runs as written: role="dialog". It happens in order, after the line above it and before the line below it.

 503 |         aria-modal="true"
     | Inside MoreSheet, this line runs as written: aria-modal="true". It happens in order, after the line above it and before the line below it.

 504 |         aria-label="More navigation"
     | Inside MoreSheet, this line runs as written: aria-label="More navigation". It happens in order, after the line above it and before the line below it.

 505 |       >
     | Inside MoreSheet, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 506 |         <div className="bottom-sheet-handle" aria-hidden="true" />
     | This draws one piece of the page while MoreSheet is showing.

 507 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 508 |         <div className="bottom-sheet-section">
     | This draws one piece of the page while MoreSheet is showing.

 509 |           {SECONDARY_NAV.map(({ to, label, icon: Icon }) => (
     | This ends MoreSheet (opened on line 492).

 510 |             <NavLink
     | This draws one piece of the page while MoreSheet is showing.

 511 |               key={to}
     | This ends MoreSheet (opened on line 492).

 512 |               to={to}
     | This ends MoreSheet (opened on line 492).

 513 |               className={({ isActive }) => `nav-item${isActive ? " active" : ""}`}
     | This ends MoreSheet (opened on line 492).

 514 |               onClick={onClose}
     | This decides what happens when you press.

 515 |             >
     | Inside MoreSheet, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 516 |               <Icon />
     | This draws one piece of the page while MoreSheet is showing.

 517 |               {label}
     | This ends MoreSheet (opened on line 492).

 518 |             </NavLink>
     | This ends a drawing that MoreSheet started just above.

 519 |           ))}
     | This ends MoreSheet (opened on line 492).

 520 |         </div>
     | This ends a drawing that MoreSheet started just above.

 521 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 522 |         <div className="bottom-sheet-section">
     | This draws one piece of the page while MoreSheet is showing.

 523 |           <SheetConnectors open={open} />
     | This draws one piece of the page while MoreSheet is showing.

 524 |         </div>
     | This ends a drawing that MoreSheet started just above.

 525 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 526 |         <div className="bottom-sheet-section">
     | This draws one piece of the page while MoreSheet is showing.

 527 |           <div className="sidebar-section-label">Energy level</div>
     | This draws one piece of the page while MoreSheet is showing.

 528 |           <div style={{ padding: "4px 0" }}>
     | This draws one piece of the page while MoreSheet is showing.

 529 |             <EnergyControl compact />
     | This draws one piece of the page while MoreSheet is showing.

 530 |           </div>
     | This ends a drawing that MoreSheet started just above.

 531 |         </div>
     | This ends a drawing that MoreSheet started just above.

 532 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 533 |         <div className="bottom-sheet-footer">
     | This draws one piece of the page while MoreSheet is showing.

 534 |           <a
     | This draws one piece of the page while MoreSheet is showing.

 535 |             href={FUNDING_URL}
     | This ends MoreSheet (opened on line 492).

 536 |             target="_blank"
     | Inside MoreSheet, this line runs as written: target="_blank". It happens in order, after the line above it and before the line below it.

 537 |             rel="noopener noreferrer"
     | Inside MoreSheet, this line runs as written: rel="noopener noreferrer". It happens in order, after the line above it and before the line below it.

 538 |             className="support-btn"
     | Inside MoreSheet, this line runs as written: className="support-btn". It happens in order, after the line above it and before the line below it.

 539 |             onClick={onClose}
     | This decides what happens when you press.

 540 |             aria-label="Buy me a coffee (opens buymeacoffee.com in a new tab)"
     | Inside MoreSheet, this line runs as written: aria-label="Buy me a coffee (opens buymeacoffee.com in a new tab)". It happens in order, after the line above it and before the line below it.

 541 |           >
     | Inside MoreSheet, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 542 |             <Icons.Coffee />
     | This draws one piece of the page while MoreSheet is showing.

 543 |             Buy me a coffee
     | Inside MoreSheet, this line runs as written: Buy me a coffee. It happens in order, after the line above it and before the line below it.

 544 |           </a>
     | This ends a drawing that MoreSheet started just above.

 545 |           <button
     | This draws one piece of the page while MoreSheet is showing.

 546 |             className="theme-toggle"
     | Inside MoreSheet, this line runs as written: className="theme-toggle". It happens in order, after the line above it and before the line below it.

 547 |             onClick={() => setTheme((t) => (t === "dark" ? "light" : "dark"))}
     | This decides what happens when you press.

 548 |           >
     | Inside MoreSheet, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 549 |             {theme === "dark" ? <Icons.Sun /> : <Icons.Moon />}
     | This ends MoreSheet (opened on line 492).

 550 |             {theme === "dark" ? "Light mode" : "Dark mode"}
     | This ends MoreSheet (opened on line 492).

 551 |           </button>
     | This ends a drawing that MoreSheet started just above.

 552 |           <button
     | This draws one piece of the page while MoreSheet is showing.

 553 |             className="logout-btn"
     | Inside MoreSheet, this line runs as written: className="logout-btn". It happens in order, after the line above it and before the line below it.

 554 |             onClick={() => { onLogout(); onClose(); }}
     | This decides what happens when you press.

 555 |           >
     | Inside MoreSheet, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 556 |             <Icons.Logout />
     | This draws one piece of the page while MoreSheet is showing.

 557 |             Logout
     | Inside MoreSheet, this line runs as written: Logout. It happens in order, after the line above it and before the line below it.

 558 |           </button>
     | This ends a drawing that MoreSheet started just above.

 559 |         </div>
     | This ends a drawing that MoreSheet started just above.

 560 |       </div>
     | This ends a drawing that MoreSheet started just above.

 561 |     </>
     | This ends a drawing that MoreSheet started just above.

 562 |   );
     | This closes a box of instructions that opened above.

 563 | }
     | This ends MoreSheet (opened on line 492).

 564 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 565 | function DevNoticeBanner() {
     | This starts DevNoticeBanner. Static 'under development' notice. It does not read state. Two text lengths; CSS picks one.

 566 |   return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

 567 |     <div className="dev-banner">
     | This draws one piece of the page while DevNoticeBanner is showing.

 568 |       <div className="dev-banner-main">
     | This draws one piece of the page while DevNoticeBanner is showing.

 569 |         <span className="dev-banner-icon" aria-hidden="true">i</span>
     | This draws one piece of the page while DevNoticeBanner is showing.

 570 |         <div className="dev-banner-text">
     | This draws one piece of the page while DevNoticeBanner is showing.

 571 |           <span className="dev-banner-text-full">
     | This draws one piece of the page while DevNoticeBanner is showing.

 572 |             <strong>JumpyBrain is currently under development.</strong> Some
     | This draws one piece of the page while DevNoticeBanner is showing.

 573 |             features may not work as expected yet. We're actively improving
     | Inside DevNoticeBanner, this line runs as written: features may not work as expected yet. We're actively improving. It happens in order, after the line above it and before the line below it.

 574 |             the experience, and your feedback helps us make it better.
     | Inside DevNoticeBanner, this line runs as written: the experience, and your feedback helps us make it better.. It happens in order, after the line above it and before the line below it.

 575 |           </span>
     | This ends a drawing that DevNoticeBanner started just above.

 576 |           <span className="dev-banner-text-short">
     | This draws one piece of the page while DevNoticeBanner is showing.

 577 |             <strong>Under development.</strong> Some features may not work
     | This draws one piece of the page while DevNoticeBanner is showing.

 578 |             yet —{" "}
     | This ends DevNoticeBanner (opened on line 565).

 579 |             <a
     | This draws one piece of the page while DevNoticeBanner is showing.

 580 |               href={FEEDBACK_URL}
     | This ends DevNoticeBanner (opened on line 565).

 581 |               target="_blank"
     | Inside DevNoticeBanner, this line runs as written: target="_blank". It happens in order, after the line above it and before the line below it.

 582 |               rel="noopener noreferrer"
     | Inside DevNoticeBanner, this line runs as written: rel="noopener noreferrer". It happens in order, after the line above it and before the line below it.

 583 |               className="dev-banner-inline-link"
     | Inside DevNoticeBanner, this line runs as written: className="dev-banner-inline-link". It happens in order, after the line above it and before the line below it.

 584 |             >
     | Inside DevNoticeBanner, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 585 |               share feedback →
     | Inside DevNoticeBanner, this line runs as written: share feedback →. It happens in order, after the line above it and before the line below it.

 586 |             </a>
     | This ends a drawing that DevNoticeBanner started just above.

 587 |           </span>
     | This ends a drawing that DevNoticeBanner started just above.

 588 |         </div>
     | This ends a drawing that DevNoticeBanner started just above.

 589 |       </div>
     | This ends a drawing that DevNoticeBanner started just above.

 590 |       <a
     | This draws one piece of the page while DevNoticeBanner is showing.

 591 |         href={FEEDBACK_URL}
     | This ends DevNoticeBanner (opened on line 565).

 592 |         target="_blank"
     | Inside DevNoticeBanner, this line runs as written: target="_blank". It happens in order, after the line above it and before the line below it.

 593 |         rel="noopener noreferrer"
     | Inside DevNoticeBanner, this line runs as written: rel="noopener noreferrer". It happens in order, after the line above it and before the line below it.

 594 |         className="dev-banner-cta"
     | Inside DevNoticeBanner, this line runs as written: className="dev-banner-cta". It happens in order, after the line above it and before the line below it.

 595 |       >
     | Inside DevNoticeBanner, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 596 |         Share Feedback →
     | Inside DevNoticeBanner, this line runs as written: Share Feedback →. It happens in order, after the line above it and before the line below it.

 597 |       </a>
     | This ends a drawing that DevNoticeBanner started just above.

 598 |     </div>
     | This ends a drawing that DevNoticeBanner started just above.

 599 |   );
     | This closes a box of instructions that opened above.

 600 | }
     | This ends DevNoticeBanner (opened on line 565).

 601 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 602 | function ProtectedRoute({ children }) {
     | This starts ProtectedRoute. If UserProvider is still loading, render nothing. If there is no user, render Auth. Otherwise render the page.

 603 |   const { user, loading } = useUser();
     | The logged-in profile object. Null means ProtectedRoute renders Auth.

 604 |   if (loading) return null;
     | This asks a yes-or-no question. The next bit runs only on yes.

 605 |   if (!user) return <Auth />;
     | This asks a yes-or-no question. The next bit runs only on yes.

 606 |   return children;
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

 607 | }
     | This ends ProtectedRoute (opened on line 602).

 608 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 609 | export default function App() {
     | This starts App. Owns theme, both menus, and the route table. Wraps everything in EnergyProvider. Sidebar, overlay, top bar, banner, bottom nav, and More sheet render only when user is set.

 610 |   const { user, setUser, setToken } = useUser();
     | The logged-in profile object. Null means ProtectedRoute renders Auth.

 611 |   const [theme, setTheme] = useState(
     | App's dark or light string. Written onto <html data-theme> and localStorage bb-theme. This is not the unused five-palette themeStore.

 612 |     () => localStorage.getItem("bb-theme") || "dark"
     | This looks in the browser's pocket, or puts something there, so it is still around after a refresh.

 613 |   );
     | This closes a box of instructions that opened above.

 614 |   const [sidebarOpen, setSidebarOpen] = useState(false);
     | Whether the desktop sidebar is slid open. The backdrop and the menu button flip it. It is component state, not uiStore.

 615 |   const [moreOpen, setMoreOpen] = useState(false);
     | Whether the mobile More sheet is open.

 616 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 617 |   // Apply theme whenever it changes
     | A note written for people. The app does not run it.

 618 |   useEffect(() => {
     | This is an extra job that happens after the picture is drawn.

 619 |     document.documentElement.setAttribute("data-theme", theme);
     | Inside App, this line runs as written: document.documentElement.setAttribute("data-theme", theme);. It happens in order, after the line above it and before the line below it.

 620 |     localStorage.setItem("bb-theme", theme);
     | This looks in the browser's pocket, or puts something there, so it is still around after a refresh.

 621 |   }, [theme]);
     | This ends effect in App (opened on line 618).

 622 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 623 |   // Sync theme from user's saved preference when they log in
     | A note written for people. The app does not run it.

 624 |   useEffect(() => {
     | This is an extra job that happens after the picture is drawn.

 625 |     if (user?.preferredTheme) {
     | This asks a yes-or-no question. The next bit runs only on yes.

 626 |       setTheme(user.preferredTheme);
     | Inside App, this line runs as written: setTheme(user.preferredTheme);. It happens in order, after the line above it and before the line below it.

 627 |     }
     | This ends if (user?.preferredTheme) { (opened on line 625).

 628 |   }, [user?.preferredTheme]);
     | This ends effect in App (opened on line 624).

 629 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 630 |   useEffect(() => {
     | This is an extra job that happens after the picture is drawn.

 631 |     if ("Notification" in window && Notification.permission !== "granted") {
     | This asks a yes-or-no question. The next bit runs only on yes.

 632 |       Notification.requestPermission();
     | Inside App, this line runs as written: Notification.requestPermission();. It happens in order, after the line above it and before the line below it.

 633 |     }
     | This ends if ("Notification" in window && Notifica (opened on line 631).

 634 |   }, []);
     | This ends effect in App (opened on line 630).

 635 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 636 |   function logout() {
     | This starts logout. Clears user and token through UserProvider (which also clears localStorage and tells the extension). Closes both menus.

 637 |     setUser(null);
     | Inside logout, this line runs as written: setUser(null);. It happens in order, after the line above it and before the line below it.

 638 |     setToken(null);
     | Inside logout, this line runs as written: setToken(null);. It happens in order, after the line above it and before the line below it.

 639 |     setSidebarOpen(false);
     | Inside logout, this line runs as written: setSidebarOpen(false);. It happens in order, after the line above it and before the line below it.

 640 |     setMoreOpen(false);
     | Inside logout, this line runs as written: setMoreOpen(false);. It happens in order, after the line above it and before the line below it.

 641 |   }
     | This ends logout (opened on line 636).

 642 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 643 |   return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

 644 |     <EnergyProvider>
     | This draws one piece of the page while App is showing.

 645 |       <div className="app-shell">
     | This draws one piece of the page while App is showing.

 646 |         {user && (
     | Inside App, this line runs as written: {user && (. It happens in order, after the line above it and before the line below it.

 647 |           <>
     | This draws one piece of the page while App is showing.

 648 |             <Sidebar
     | This draws one piece of the page while App is showing.

 649 |               theme={theme}
     | This ends App (opened on line 609).

 650 |               setTheme={setTheme}
     | This ends App (opened on line 609).

 651 |               onLogout={logout}
     | This ends App (opened on line 609).

 652 |               open={sidebarOpen}
     | This ends App (opened on line 609).

 653 |               onClose={() => setSidebarOpen(false)}
     | This ends App (opened on line 609).

 654 |             />
     | This closes a box of instructions that opened above.

 655 |             <FocusOverlay />
     | This draws one piece of the page while App is showing.

 656 |           </>
     | This ends a drawing that App started just above.

 657 |         )}
     | This ends App (opened on line 609).

 658 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 659 |         <div className="main-wrapper">
     | This draws one piece of the page while App is showing.

 660 |           {user && (
     | Inside App, this line runs as written: {user && (. It happens in order, after the line above it and before the line below it.

 661 |             <TopBar
     | This draws one piece of the page while App is showing.

 662 |               theme={theme}
     | This ends App (opened on line 609).

 663 |               setTheme={setTheme}
     | This ends App (opened on line 609).

 664 |               onMenuClick={() => setSidebarOpen((o) => !o)}
     | This ends App (opened on line 609).

 665 |               onMoreClick={() => setMoreOpen((o) => !o)}
     | This ends App (opened on line 609).

 666 |               onLogout={logout}
     | This ends App (opened on line 609).

 667 |             />
     | This closes a box of instructions that opened above.

 668 |           )}
     | This ends App (opened on line 609).

 669 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 670 |           <main className="main-content" id="main-content">
     | This draws one piece of the page while App is showing.

 671 |             {user && <DevNoticeBanner />}
     | This ends App (opened on line 609).

 672 |             <Routes>
     | This draws one piece of the page while App is showing.

 673 |               <Route path="/auth" element={<Auth />} />
     | This draws one piece of the page while App is showing.

 674 |               <Route path="/" element={<ProtectedRoute><Home /></ProtectedRoute>} />
     | This draws one piece of the page while App is showing.

 675 |               <Route path="/dashboard" element={<ProtectedRoute><Dashboard /></ProtectedRoute>} />
     | This draws one piece of the page while App is showing.

 676 |               <Route path="/focus" element={<ProtectedRoute><FocusTimer /></ProtectedRoute>} />
     | This draws one piece of the page while App is showing.

 677 |               <Route path="/todo" element={<ProtectedRoute><TodoList /></ProtectedRoute>} />
     | This draws one piece of the page while App is showing.

 678 |               <Route path="/mindful" element={<ProtectedRoute><Mindfulness /></ProtectedRoute>} />
     | This draws one piece of the page while App is showing.

 679 |               <Route path="/deadline" element={<ProtectedRoute><DeadlineTimer /></ProtectedRoute>} />
     | This draws one piece of the page while App is showing.

 680 |               <Route path="/calendar" element={<ProtectedRoute><Calendar /></ProtectedRoute>} />
     | This draws one piece of the page while App is showing.

 681 |               <Route path="/connectors" element={<ProtectedRoute><ConnectorsPage /></ProtectedRoute>} />
     | This draws one piece of the page while App is showing.

 682 |               <Route path="/blocking" element={<ProtectedRoute><FocusShieldPage /></ProtectedRoute>} />
     | This draws one piece of the page while App is showing.

 683 |               <Route path="/settings" element={<ProtectedRoute><ProfileSettings onThemeChange={setTheme} /></ProtectedRoute>} />
     | This draws one piece of the page while App is showing.

 684 |             </Routes>
     | This ends a drawing that App started just above.

 685 |           </main>
     | This ends a drawing that App started just above.

 686 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 687 |           {user && <BottomNav onLogout={logout} />}
     | This ends App (opened on line 609).

 688 |         </div>
     | This ends a drawing that App started just above.

 689 |         {user && (
     | Inside App, this line runs as written: {user && (. It happens in order, after the line above it and before the line below it.

 690 |           <MoreSheet
     | This draws one piece of the page while App is showing.

 691 |             open={moreOpen}
     | This ends App (opened on line 609).

 692 |             onClose={() => setMoreOpen(false)}
     | This ends App (opened on line 609).

 693 |             theme={theme}
     | This ends App (opened on line 609).

 694 |             setTheme={setTheme}
     | This ends App (opened on line 609).

 695 |             onLogout={logout}
     | This ends App (opened on line 609).

 696 |           />
     | This closes a box of instructions that opened above.

 697 |         )}
     | This ends App (opened on line 609).

 698 |       </div>
     | This ends a drawing that App started just above.

 699 |     </EnergyProvider>
     | This ends a drawing that App started just above.

 700 |   );
     | This closes a box of instructions that opened above.

 701 | }
     | This ends App (opened on line 609).

