# `src/App.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import React, { useEffect, useState } from "react";
     | Import for the shell: theme, menus, and which page is visible: `import React, { useEffect, useState } from "react";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   2 | import { Routes, Route, Link, NavLink, useLocation } from "react-router-dom";
     | Import for the shell: theme, menus, and which page is visible: `import { Routes, Route, Link, NavLink, useLocation } from "react-router-dom";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   3 | import Logo from "./components/Logo";
     | Import for the shell: theme, menus, and which page is visible: `import Logo from "./components/Logo";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   4 | import api from "./services/api";
     | Import for the shell: theme, menus, and which page is visible: `import api from "./services/api";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   5 | import Auth from "./components/Auth";
     | Import for the shell: theme, menus, and which page is visible: `import Auth from "./components/Auth";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   6 | import Home from "./components/Home";
     | Import for the shell: theme, menus, and which page is visible: `import Home from "./components/Home";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   7 | import Dashboard from "./components/Dashboard";
     | Import for the shell: theme, menus, and which page is visible: `import Dashboard from "./components/Dashboard";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   8 | import FocusTimer from "./components/FocusTimer";
     | Import for the shell: theme, menus, and which page is visible: `import FocusTimer from "./components/FocusTimer";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   9 | import TodoList from "./components/TodoList";
     | Import for the shell: theme, menus, and which page is visible: `import TodoList from "./components/TodoList";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

  10 | import Mindfulness from "./components/Mindfulness";
     | Import for the shell: theme, menus, and which page is visible: `import Mindfulness from "./components/Mindfulness";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

  11 | import DeadlineTimer from "./components/DeadlineTimer";
     | Import for the shell: theme, menus, and which page is visible: `import DeadlineTimer from "./components/DeadlineTimer";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

  12 | import Calendar from "./components/Calendar";
     | Import for the shell: theme, menus, and which page is visible: `import Calendar from "./components/Calendar";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

  13 | import ConnectorsPage from "./components/ConnectorsPage";
     | Import for the shell: theme, menus, and which page is visible: `import ConnectorsPage from "./components/ConnectorsPage";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

  14 | import ProfileSettings from "./components/ProfileSettings";
     | Import for the shell: theme, menus, and which page is visible: `import ProfileSettings from "./components/ProfileSettings";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

  15 | import FocusShieldPage from "./components/focus-shield/FocusShieldPage";
     | Import for the shell: theme, menus, and which page is visible: `import FocusShieldPage from "./components/focus-shield/FocusShieldPage";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

  16 | import FocusOverlay from "./components/FocusOverlay";
     | Import for the shell: theme, menus, and which page is visible: `import FocusOverlay from "./components/FocusOverlay";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

  17 | import EnergyControl from "./components/EnergyControl";
     | Import for the shell: theme, menus, and which page is visible: `import EnergyControl from "./components/EnergyControl";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

  18 | import { useUser } from "./contexts/UserContext";
     | Import for the shell: theme, menus, and which page is visible: `import { useUser } from "./contexts/UserContext";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

  19 | import { EnergyProvider } from "./contexts/EnergyContext";
     | Import for the shell: theme, menus, and which page is visible: `import { EnergyProvider } from "./contexts/EnergyContext";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

  20 | 
     | Blank line in `src/App.jsx` (the shell: theme, menus, and which page is visible), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  21 | // ── Icons ────────────────────────────────────────────────────────────────
     | Comment inside the top of the file. Not executed. It documents the next code: ── Icons ────────────────────────────────────────────────────────────────

  22 | const Icons = {
     | In `the top of the file` (src/App.jsx): `Icons` is assigned `{`. Later lines in this function read that name.

  23 |   Today: () => (
     | In `the top of the file` (src/App.jsx): statement `Today: () => (`. It runs when the top of the file runs, in order, before the next line of the same function.

  24 |     <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}>
     | In `the top of the file` (src/App.jsx): Opens it. Vector drawing. It does not fetch data. Source: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}>`

  25 |       <path d="M3 10L12 3l9 7v10a1 1 0 01-1 1H4a1 1 0 01-1-1V10z" />
     | In `the top of the file` (src/App.jsx): JSX `<path>`. React will create this node when the parent renders. Source: `<path d="M3 10L12 3l9 7v10a1 1 0 01-1 1H4a1 1 0 01-1-1V10z" />`

  26 |       <path d="M9 21V12h6v9" />
     | In `the top of the file` (src/App.jsx): JSX `<path>`. React will create this node when the parent renders. Source: `<path d="M9 21V12h6v9" />`

  27 |     </svg>
     | In `the top of the file` (src/App.jsx): Closes it. Vector drawing. It does not fetch data. Source: `</svg>`

  28 |   ),
     | In `the top of the file` (src/App.jsx): statement `),`. It runs when the top of the file runs, in order, before the next line of the same function.

  29 |   Tasks: () => (
     | In `the top of the file` (src/App.jsx): statement `Tasks: () => (`. It runs when the top of the file runs, in order, before the next line of the same function.

  30 |     <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}>
     | In `the top of the file` (src/App.jsx): Opens it. Vector drawing. It does not fetch data. Source: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}>`

  31 |       <path d="M9 11l2 2 4-4" />
     | In `the top of the file` (src/App.jsx): JSX `<path>`. React will create this node when the parent renders. Source: `<path d="M9 11l2 2 4-4" />`

  32 |       <rect x="3" y="3" width="18" height="18" rx="3" />
     | In `the top of the file` (src/App.jsx): JSX `<rect>`. React will create this node when the parent renders. Source: `<rect x="3" y="3" width="18" height="18" rx="3" />`

  33 |     </svg>
     | In `the top of the file` (src/App.jsx): Closes it. Vector drawing. It does not fetch data. Source: `</svg>`

  34 |   ),
     | In `the top of the file` (src/App.jsx): statement `),`. It runs when the top of the file runs, in order, before the next line of the same function.

  35 |   Schedule: () => (
     | In `the top of the file` (src/App.jsx): statement `Schedule: () => (`. It runs when the top of the file runs, in order, before the next line of the same function.

  36 |     <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}>
     | In `the top of the file` (src/App.jsx): Opens it. Vector drawing. It does not fetch data. Source: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}>`

  37 |       <rect x="3" y="4" width="18" height="18" rx="2" />
     | In `the top of the file` (src/App.jsx): JSX `<rect>`. React will create this node when the parent renders. Source: `<rect x="3" y="4" width="18" height="18" rx="2" />`

  38 |       <path d="M16 2v4M8 2v4M3 10h18" />
     | In `the top of the file` (src/App.jsx): JSX `<path>`. React will create this node when the parent renders. Source: `<path d="M16 2v4M8 2v4M3 10h18" />`

  39 |     </svg>
     | In `the top of the file` (src/App.jsx): Closes it. Vector drawing. It does not fetch data. Source: `</svg>`

  40 |   ),
     | In `the top of the file` (src/App.jsx): statement `),`. It runs when the top of the file runs, in order, before the next line of the same function.

  41 |   Progress: () => (
     | In `the top of the file` (src/App.jsx): statement `Progress: () => (`. It runs when the top of the file runs, in order, before the next line of the same function.

  42 |     <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}>
     | In `the top of the file` (src/App.jsx): Opens it. Vector drawing. It does not fetch data. Source: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}>`

  43 |       <rect x="3" y="3" width="18" height="18" rx="2" />
     | In `the top of the file` (src/App.jsx): JSX `<rect>`. React will create this node when the parent renders. Source: `<rect x="3" y="3" width="18" height="18" rx="2" />`

  44 |       <path d="M8 17V13M12 17V9M16 17v-3" />
     | In `the top of the file` (src/App.jsx): JSX `<path>`. React will create this node when the parent renders. Source: `<path d="M8 17V13M12 17V9M16 17v-3" />`

  45 |     </svg>
     | In `the top of the file` (src/App.jsx): Closes it. Vector drawing. It does not fetch data. Source: `</svg>`

  46 |   ),
     | In `the top of the file` (src/App.jsx): statement `),`. It runs when the top of the file runs, in order, before the next line of the same function.

  47 |   Sun: () => (
     | In `the top of the file` (src/App.jsx): statement `Sun: () => (`. It runs when the top of the file runs, in order, before the next line of the same function.

  48 |     <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}>
     | In `the top of the file` (src/App.jsx): Opens it. Vector drawing. It does not fetch data. Source: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}>`

  49 |       <circle cx="12" cy="12" r="4" />
     | In `the top of the file` (src/App.jsx): JSX `<circle>`. React will create this node when the parent renders. Source: `<circle cx="12" cy="12" r="4" />`

  50 |       <path d="M12 2v2M12 20v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M2 12h2M20 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42" />
     | In `the top of the file` (src/App.jsx): JSX `<path>`. React will create this node when the parent renders. Source: `<path d="M12 2v2M12 20v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M2 12h2M20 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42" />`

  51 |     </svg>
     | In `the top of the file` (src/App.jsx): Closes it. Vector drawing. It does not fetch data. Source: `</svg>`

  52 |   ),
     | In `the top of the file` (src/App.jsx): statement `),`. It runs when the top of the file runs, in order, before the next line of the same function.

  53 |   Moon: () => (
     | In `the top of the file` (src/App.jsx): statement `Moon: () => (`. It runs when the top of the file runs, in order, before the next line of the same function.

  54 |     <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}>
     | In `the top of the file` (src/App.jsx): Opens it. Vector drawing. It does not fetch data. Source: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}>`

  55 |       <path d="M21 12.79A9 9 0 1111.21 3 7 7 0 0021 12.79z" />
     | In `the top of the file` (src/App.jsx): JSX `<path>`. React will create this node when the parent renders. Source: `<path d="M21 12.79A9 9 0 1111.21 3 7 7 0 0021 12.79z" />`

  56 |     </svg>
     | In `the top of the file` (src/App.jsx): Closes it. Vector drawing. It does not fetch data. Source: `</svg>`

  57 |   ),
     | In `the top of the file` (src/App.jsx): statement `),`. It runs when the top of the file runs, in order, before the next line of the same function.

  58 |   Logout: () => (
     | In `the top of the file` (src/App.jsx): statement `Logout: () => (`. It runs when the top of the file runs, in order, before the next line of the same function.

  59 |     <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}>
     | In `the top of the file` (src/App.jsx): Opens it. Vector drawing. It does not fetch data. Source: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}>`

  60 |       <path d="M9 21H5a2 2 0 01-2-2V5a2 2 0 012-2h4M16 17l5-5-5-5M21 12H9" />
     | In `the top of the file` (src/App.jsx): JSX `<path>`. React will create this node when the parent renders. Source: `<path d="M9 21H5a2 2 0 01-2-2V5a2 2 0 012-2h4M16 17l5-5-5-5M21 12H9" />`

  61 |     </svg>
     | In `the top of the file` (src/App.jsx): Closes it. Vector drawing. It does not fetch data. Source: `</svg>`

  62 |   ),
     | In `the top of the file` (src/App.jsx): statement `),`. It runs when the top of the file runs, in order, before the next line of the same function.

  63 |   Focus: () => (
     | In `the top of the file` (src/App.jsx): statement `Focus: () => (`. It runs when the top of the file runs, in order, before the next line of the same function.

  64 |     <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}>
     | In `the top of the file` (src/App.jsx): Opens it. Vector drawing. It does not fetch data. Source: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}>`

  65 |       <circle cx="12" cy="12" r="9" />
     | In `the top of the file` (src/App.jsx): JSX `<circle>`. React will create this node when the parent renders. Source: `<circle cx="12" cy="12" r="9" />`

  66 |       <circle cx="12" cy="12" r="4" />
     | In `the top of the file` (src/App.jsx): JSX `<circle>`. React will create this node when the parent renders. Source: `<circle cx="12" cy="12" r="4" />`

  67 |       <circle cx="12" cy="12" r="1" fill="currentColor" />
     | In `the top of the file` (src/App.jsx): JSX `<circle>`. React will create this node when the parent renders. Source: `<circle cx="12" cy="12" r="1" fill="currentColor" />`

  68 |     </svg>
     | In `the top of the file` (src/App.jsx): Closes it. Vector drawing. It does not fetch data. Source: `</svg>`

  69 |   ),
     | In `the top of the file` (src/App.jsx): statement `),`. It runs when the top of the file runs, in order, before the next line of the same function.

  70 |   Settings: () => (
     | In `the top of the file` (src/App.jsx): statement `Settings: () => (`. It runs when the top of the file runs, in order, before the next line of the same function.

  71 |     <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}>
     | In `the top of the file` (src/App.jsx): Opens it. Vector drawing. It does not fetch data. Source: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}>`

  72 |       <circle cx="12" cy="12" r="3" />
     | In `the top of the file` (src/App.jsx): JSX `<circle>`. React will create this node when the parent renders. Source: `<circle cx="12" cy="12" r="3" />`

  73 |       <path d="M19.07 4.93a10 10 0 010 14.14M4.93 4.93a10 10 0 000 14.14" />
     | In `the top of the file` (src/App.jsx): JSX `<path>`. React will create this node when the parent renders. Source: `<path d="M19.07 4.93a10 10 0 010 14.14M4.93 4.93a10 10 0 000 14.14" />`

  74 |     </svg>
     | In `the top of the file` (src/App.jsx): Closes it. Vector drawing. It does not fetch data. Source: `</svg>`

  75 |   ),
     | In `the top of the file` (src/App.jsx): statement `),`. It runs when the top of the file runs, in order, before the next line of the same function.

  76 |   Shield: () => (
     | In `the top of the file` (src/App.jsx): statement `Shield: () => (`. It runs when the top of the file runs, in order, before the next line of the same function.

  77 |     <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}>
     | In `the top of the file` (src/App.jsx): Opens it. Vector drawing. It does not fetch data. Source: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}>`

  78 |       <path d="M12 3l7 3v6c0 4.5-3 7.5-7 9-4-1.5-7-4.5-7-9V6l7-3z" />
     | In `the top of the file` (src/App.jsx): JSX `<path>`. React will create this node when the parent renders. Source: `<path d="M12 3l7 3v6c0 4.5-3 7.5-7 9-4-1.5-7-4.5-7-9V6l7-3z" />`

  79 |       <path d="M9.5 12l1.8 1.8L15 10" />
     | In `the top of the file` (src/App.jsx): JSX `<path>`. React will create this node when the parent renders. Source: `<path d="M9.5 12l1.8 1.8L15 10" />`

  80 |     </svg>
     | In `the top of the file` (src/App.jsx): Closes it. Vector drawing. It does not fetch data. Source: `</svg>`

  81 |   ),
     | In `the top of the file` (src/App.jsx): statement `),`. It runs when the top of the file runs, in order, before the next line of the same function.

  82 |   Plug: () => (
     | In `the top of the file` (src/App.jsx): statement `Plug: () => (`. It runs when the top of the file runs, in order, before the next line of the same function.

  83 |     <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}>
     | In `the top of the file` (src/App.jsx): Opens it. Vector drawing. It does not fetch data. Source: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}>`

  84 |       <path d="M12 22V12M5 12H19M8 12V7a4 4 0 018 0v5" />
     | In `the top of the file` (src/App.jsx): JSX `<path>`. React will create this node when the parent renders. Source: `<path d="M12 22V12M5 12H19M8 12V7a4 4 0 018 0v5" />`

  85 |     </svg>
     | In `the top of the file` (src/App.jsx): Closes it. Vector drawing. It does not fetch data. Source: `</svg>`

  86 |   ),
     | In `the top of the file` (src/App.jsx): statement `),`. It runs when the top of the file runs, in order, before the next line of the same function.

  87 |   More: () => (
     | In `the top of the file` (src/App.jsx): statement `More: () => (`. It runs when the top of the file runs, in order, before the next line of the same function.

  88 |     <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2} strokeLinecap="round">
     | In `the top of the file` (src/App.jsx): Opens it. Vector drawing. It does not fetch data. Source: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2} strokeLinecap="round">`

  89 |       <circle cx="5" cy="12" r="1.5" fill="currentColor" stroke="none" />
     | In `the top of the file` (src/App.jsx): JSX `<circle>`. React will create this node when the parent renders. Source: `<circle cx="5" cy="12" r="1.5" fill="currentColor" stroke="none" />`

  90 |       <circle cx="12" cy="12" r="1.5" fill="currentColor" stroke="none" />
     | In `the top of the file` (src/App.jsx): JSX `<circle>`. React will create this node when the parent renders. Source: `<circle cx="12" cy="12" r="1.5" fill="currentColor" stroke="none" />`

  91 |       <circle cx="19" cy="12" r="1.5" fill="currentColor" stroke="none" />
     | In `the top of the file` (src/App.jsx): JSX `<circle>`. React will create this node when the parent renders. Source: `<circle cx="19" cy="12" r="1.5" fill="currentColor" stroke="none" />`

  92 |     </svg>
     | In `the top of the file` (src/App.jsx): Closes it. Vector drawing. It does not fetch data. Source: `</svg>`

  93 |   ),
     | In `the top of the file` (src/App.jsx): statement `),`. It runs when the top of the file runs, in order, before the next line of the same function.

  94 |   Profile: () => (
     | In `the top of the file` (src/App.jsx): statement `Profile: () => (`. It runs when the top of the file runs, in order, before the next line of the same function.

  95 |     <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}>
     | In `the top of the file` (src/App.jsx): Opens it. Vector drawing. It does not fetch data. Source: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}>`

  96 |       <circle cx="12" cy="8" r="4" />
     | In `the top of the file` (src/App.jsx): JSX `<circle>`. React will create this node when the parent renders. Source: `<circle cx="12" cy="8" r="4" />`

  97 |       <path d="M4 20c0-4 3.6-7 8-7s8 3 8 7" />
     | In `the top of the file` (src/App.jsx): JSX `<path>`. React will create this node when the parent renders. Source: `<path d="M4 20c0-4 3.6-7 8-7s8 3 8 7" />`

  98 |     </svg>
     | In `the top of the file` (src/App.jsx): Closes it. Vector drawing. It does not fetch data. Source: `</svg>`

  99 |   ),
     | In `the top of the file` (src/App.jsx): statement `),`. It runs when the top of the file runs, in order, before the next line of the same function.

 100 |   Coffee: () => (
     | In `the top of the file` (src/App.jsx): statement `Coffee: () => (`. It runs when the top of the file runs, in order, before the next line of the same function.

 101 |     <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}>
     | In `the top of the file` (src/App.jsx): Opens it. Vector drawing. It does not fetch data. Source: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}>`

 102 |       <path d="M18 8h1a3 3 0 010 6h-1" />
     | In `the top of the file` (src/App.jsx): JSX `<path>`. React will create this node when the parent renders. Source: `<path d="M18 8h1a3 3 0 010 6h-1" />`

 103 |       <path d="M3 8h15v6a4 4 0 01-4 4H7a4 4 0 01-4-4V8z" />
     | In `the top of the file` (src/App.jsx): JSX `<path>`. React will create this node when the parent renders. Source: `<path d="M3 8h15v6a4 4 0 01-4 4H7a4 4 0 01-4-4V8z" />`

 104 |       <path d="M6 2v2M10 2v2M14 2v2" />
     | In `the top of the file` (src/App.jsx): JSX `<path>`. React will create this node when the parent renders. Source: `<path d="M6 2v2M10 2v2M14 2v2" />`

 105 |     </svg>
     | In `the top of the file` (src/App.jsx): Closes it. Vector drawing. It does not fetch data. Source: `</svg>`

 106 |   ),
     | In `the top of the file` (src/App.jsx): statement `),`. It runs when the top of the file runs, in order, before the next line of the same function.

 107 |   Feedback: () => (
     | In `the top of the file` (src/App.jsx): statement `Feedback: () => (`. It runs when the top of the file runs, in order, before the next line of the same function.

 108 |     <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}>
     | In `the top of the file` (src/App.jsx): Opens it. Vector drawing. It does not fetch data. Source: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}>`

 109 |       <path d="M21 11.5a8.38 8.38 0 01-.9 3.8 8.5 8.5 0 01-7.6 4.7 8.38 8.38 0 01-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 01-.9-3.8 8.5 8.5 0 014.7-7.6 8.38 8.38 0 013.8-.9h.5a8.48 8.48 0 018 8v.5z" />
     | In `the top of the file` (src/App.jsx): JSX `<path>`. React will create this node when the parent renders. Source: `<path d="M21 11.5a8.38 8.38 0 01-.9 3.8 8.5 8.5 0 01-7.6 4.7 8.38 8.38 0 01-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 01-.9-3.8 8.5 8.5 0 014.7-7.6 8.38 8.38 0 013.8-.9h.5a8.48 8.48 0 018 8v.5z" />`

 110 |     </svg>
     | In `the top of the file` (src/App.jsx): Closes it. Vector drawing. It does not fetch data. Source: `</svg>`

 111 |   ),
     | In `the top of the file` (src/App.jsx): statement `),`. It runs when the top of the file runs, in order, before the next line of the same function.

 112 | };
     | In `the top of the file` (src/App.jsx): `};` closes const Icons = { (opened on line 22). Names declared inside that block end here.

 113 | 
     | Blank line in `src/App.jsx` (the shell: theme, menus, and which page is visible), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

 114 | // Sourced from .github/FUNDING.yml at build time (see vite.config.ts) so
     | Comment inside the top of the file. Not executed. It documents the next code: Sourced from .github/FUNDING.yml at build time (see vite.config.ts) so

 115 | // the in-app support link and the GitHub sponsor button never drift apart.
     | Comment inside the top of the file. Not executed. It documents the next code: the in-app support link and the GitHub sponsor button never drift apart.

 116 | const FUNDING_URL = __FUNDING_URL__;
     | In `the top of the file` (src/App.jsx): `FUNDING_URL`: The Buy Me a Coffee URL injected at build time from .github/FUNDING.yml by vite.config.ts as __FUNDING_URL__. The code is `const FUNDING_URL = __FUNDING_URL__;`.

 117 | const FEEDBACK_URL = "https://www.jumpybrain.com/#feedback";
     | In `the top of the file` (src/App.jsx): `FEEDBACK_URL`: Hard-coded link to https://www.jumpybrain.com/#feedback. The banner, sidebar, and top bar all open it in a new tab. The code is `const FEEDBACK_URL = "https://www.jumpybrain.com/#feedback";`.

 118 | 
     | Blank line in `src/App.jsx` (the shell: theme, menus, and which page is visible), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

 119 | // Collapsed to 4 primary destinations
     | Comment inside the top of the file. Not executed. It documents the next code: Collapsed to 4 primary destinations

 120 | const NAV_ITEMS = [
     | In `the top of the file` (src/App.jsx): `NAV_ITEMS`: The four primary routes: / Today, /todo Tasks, /calendar Schedule, /dashboard Progress. Sidebar, TopBar, and BottomNav all map this array. The code is `const NAV_ITEMS = [`.

 121 |   { to: "/",          label: "Today",    icon: Icons.Today },
     | In `the top of the file` (src/App.jsx): `{ to: "/",          label: "Today",    icon: Icons.Today },` closes the nearest open block. Names declared inside that block end here.

 122 |   { to: "/todo",      label: "Tasks",    icon: Icons.Tasks },
     | In `the top of the file` (src/App.jsx): `{ to: "/todo",      label: "Tasks",    icon: Icons.Tasks },` closes the nearest open block. Names declared inside that block end here.

 123 |   { to: "/calendar",  label: "Schedule", icon: Icons.Schedule },
     | In `the top of the file` (src/App.jsx): `{ to: "/calendar",  label: "Schedule", icon: Icons.Schedule },` closes the nearest open block. Names declared inside that block end here.

 124 |   { to: "/dashboard", label: "Progress", icon: Icons.Progress },
     | In `the top of the file` (src/App.jsx): `{ to: "/dashboard", label: "Progress", icon: Icons.Progress },` closes the nearest open block. Names declared inside that block end here.

 125 | ];
     | In `the top of the file` (src/App.jsx): statement `];`. It runs when the top of the file runs, in order, before the next line of the same function.

 126 | 
     | Blank line in `src/App.jsx` (the shell: theme, menus, and which page is visible), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

 127 | // Secondary pages accessible from sidebar "More" section
     | Comment inside the top of the file. Not executed. It documents the next code: Secondary pages accessible from sidebar "More" section

 128 | const SECONDARY_NAV = [
     | In `the top of the file` (src/App.jsx): `SECONDARY_NAV`: Routes tucked under More: /focus, /blocking, /mindful, /deadline, /settings. The code is `const SECONDARY_NAV = [`.

 129 |   { to: "/focus",    label: "Focus Timer",  icon: Icons.Focus },
     | In `the top of the file` (src/App.jsx): `{ to: "/focus",    label: "Focus Timer",  icon: Icons.Focus },` closes the nearest open block. Names declared inside that block end here.

 130 |   { to: "/blocking", label: "Focus Shield", icon: Icons.Shield },
     | In `the top of the file` (src/App.jsx): `{ to: "/blocking", label: "Focus Shield", icon: Icons.Shield },` closes the nearest open block. Names declared inside that block end here.

 131 |   { to: "/mindful",  label: "Mindfulness", icon: Icons.Today },
     | In `the top of the file` (src/App.jsx): `{ to: "/mindful",  label: "Mindfulness", icon: Icons.Today },` closes the nearest open block. Names declared inside that block end here.

 132 |   { to: "/deadline", label: "Deadlines",   icon: Icons.Schedule },
     | In `the top of the file` (src/App.jsx): `{ to: "/deadline", label: "Deadlines",   icon: Icons.Schedule },` closes the nearest open block. Names declared inside that block end here.

 133 |   { to: "/settings", label: "Profile & Settings", icon: Icons.Profile },
     | In `the top of the file` (src/App.jsx): `{ to: "/settings", label: "Profile & Settings", icon: Icons.Profile },` closes the nearest open block. Names declared inside that block end here.

 134 | ];
     | In `the top of the file` (src/App.jsx): statement `];`. It runs when the top of the file runs, in order, before the next line of the same function.

 135 | 
     | Blank line in `src/App.jsx` (the shell: theme, menus, and which page is visible), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

 136 | const CONNECTORS = [
     | In `the top of the file` (src/App.jsx): `CONNECTORS`: Gmail, Slack, and Google Calendar. Each entry knows the OAuth URL path and the sync path the buttons call. The code is `const CONNECTORS = [`.

 137 |   {
     | In `the top of the file` (src/App.jsx): statement `{`. It runs when the top of the file runs, in order, before the next line of the same function.

 138 |     id: "gmail",
     | In `the top of the file` (src/App.jsx): statement `id: "gmail",`. It runs when the top of the file runs, in order, before the next line of the same function.

 139 |     label: "Gmail",
     | In `the top of the file` (src/App.jsx): statement `label: "Gmail",`. It runs when the top of the file runs, in order, before the next line of the same function.

 140 |     color: "#ea4335",
     | In `the top of the file` (src/App.jsx): statement `color: "#ea4335",`. It runs when the top of the file runs, in order, before the next line of the same function.

 141 |     urlEndpoint: "/integrations/google/url",
     | In `the top of the file` (src/App.jsx): statement `urlEndpoint: "/integrations/google/url",`. It runs when the top of the file runs, in order, before the next line of the same function.

 142 |     syncEndpoint: "/integrations/gmail/sync",
     | In `the top of the file` (src/App.jsx): statement `syncEndpoint: "/integrations/gmail/sync",`. It runs when the top of the file runs, in order, before the next line of the same function.

 143 |     icon: () => (
     | In `the top of the file` (src/App.jsx): statement `icon: () => (`. It runs when the top of the file runs, in order, before the next line of the same function.

 144 |       <svg viewBox="0 0 24 24" fill="currentColor" width="14" height="14">
     | In `the top of the file` (src/App.jsx): Opens it. Vector drawing. It does not fetch data. Source: `<svg viewBox="0 0 24 24" fill="currentColor" width="14" height="14">`

 145 |         <path d="M20 4H4C2.9 4 2 4.9 2 6v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 2-8 5-8-5h16zm0 12H4V8l8 5 8-5v10z" />
     | In `the top of the file` (src/App.jsx): JSX `<path>`. React will create this node when the parent renders. Source: `<path d="M20 4H4C2.9 4 2 4.9 2 6v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 2-8 5-8-5h16zm0 12H4V8l8 5 8-5v10z" />`

 146 |       </svg>
     | In `the top of the file` (src/App.jsx): Closes it. Vector drawing. It does not fetch data. Source: `</svg>`

 147 |     ),
     | In `the top of the file` (src/App.jsx): statement `),`. It runs when the top of the file runs, in order, before the next line of the same function.

 148 |   },
     | In `the top of the file` (src/App.jsx): `},` closes { (opened on line 137). Names declared inside that block end here.

 149 |   {
     | In `the top of the file` (src/App.jsx): statement `{`. It runs when the top of the file runs, in order, before the next line of the same function.

 150 |     id: "slack",
     | In `the top of the file` (src/App.jsx): statement `id: "slack",`. It runs when the top of the file runs, in order, before the next line of the same function.

 151 |     label: "Slack",
     | In `the top of the file` (src/App.jsx): statement `label: "Slack",`. It runs when the top of the file runs, in order, before the next line of the same function.

 152 |     color: "#4a154b",
     | In `the top of the file` (src/App.jsx): statement `color: "#4a154b",`. It runs when the top of the file runs, in order, before the next line of the same function.

 153 |     urlEndpoint: "/integrations/slack/url",
     | In `the top of the file` (src/App.jsx): statement `urlEndpoint: "/integrations/slack/url",`. It runs when the top of the file runs, in order, before the next line of the same function.

 154 |     syncEndpoint: "/integrations/slack/sync",
     | In `the top of the file` (src/App.jsx): statement `syncEndpoint: "/integrations/slack/sync",`. It runs when the top of the file runs, in order, before the next line of the same function.

 155 |     icon: () => (
     | In `the top of the file` (src/App.jsx): statement `icon: () => (`. It runs when the top of the file runs, in order, before the next line of the same function.

 156 |       <svg viewBox="0 0 24 24" fill="currentColor" width="14" height="14">
     | In `the top of the file` (src/App.jsx): Opens it. Vector drawing. It does not fetch data. Source: `<svg viewBox="0 0 24 24" fill="currentColor" width="14" height="14">`

 157 |         <path d="M5.042 15.165a2.528 2.528 0 01-2.52 2.523A2.528 2.528 0 010 15.165a2.527 2.527 0 012.522-2.52h2.52v2.52zM6.313 15.165a2.527 2.527 0 012.521-2.52 2.527 2.527 0 012.521 2.52v6.313A2.528 2.528 0 018.834 24a2.528 2.528 0 01-2.521-2.522v-6.313zM8.834 5.042a2.528 2.528 0 01-2.521-2.52A2.528 2.528 0 018.834 0a2.528 2.528 0 012.521 2.522v2.52H8.834zM8.834 6.313a2.528 2.528 0 012.521 2.521 2.528 2.528 0 01-2.521 2.521H2.522A2.528 2.528 0 010 8.834a2.528 2.528 0 012.522-2.521h6.312zM18.956 8.834a2.528 2.528 0 012.522-2.521A2.528 2.528 0 0124 8.834a2.528 2.528 0 01-2.522 2.521h-2.522V8.834zM17.688 8.834a2.528 2.528 0 01-2.523 2.521 2.527 2.527 0 01-2.52-2.521V2.522A2.527 2.527 0 0115.165 0a2.528 2.528 0 012.523 2.522v6.312zM15.165 18.956a2.528 2.528 0 012.523 2.522A2.528 2.528 0 0115.165 24a2.527 2.527 0 01-2.52-2.522v-2.522h2.52zM15.165 17.688a2.527 2.527 0 01-2.52-2.523 2.526 2.526 0 012.52-2.52h6.313A2.527 2.527 0 0124 15.165a2.528 2.528 0 01-2.522 2.523h-6.313z" />
     | In `the top of the file` (src/App.jsx): JSX `<path>`. React will create this node when the parent renders. Source: `<path d="M5.042 15.165a2.528 2.528 0 01-2.52 2.523A2.528 2.528 0 010 15.165a2.527 2.527 0 012.522-2.52h2.52v2.52zM6.313 15.165a2.527 2.527 0 012.521-2.52 2.527 2.527 0 012.521 2.52v6.313A2.528 2.528 0`

 158 |       </svg>
     | In `the top of the file` (src/App.jsx): Closes it. Vector drawing. It does not fetch data. Source: `</svg>`

 159 |     ),
     | In `the top of the file` (src/App.jsx): statement `),`. It runs when the top of the file runs, in order, before the next line of the same function.

 160 |   },
     | In `the top of the file` (src/App.jsx): `},` closes { (opened on line 149). Names declared inside that block end here.

 161 |   {
     | In `the top of the file` (src/App.jsx): statement `{`. It runs when the top of the file runs, in order, before the next line of the same function.

 162 |     id: "gcal",
     | In `the top of the file` (src/App.jsx): statement `id: "gcal",`. It runs when the top of the file runs, in order, before the next line of the same function.

 163 |     label: "Google Cal",
     | In `the top of the file` (src/App.jsx): statement `label: "Google Cal",`. It runs when the top of the file runs, in order, before the next line of the same function.

 164 |     color: "#1a73e8",
     | In `the top of the file` (src/App.jsx): statement `color: "#1a73e8",`. It runs when the top of the file runs, in order, before the next line of the same function.

 165 |     urlEndpoint: "/integrations/google/url",
     | In `the top of the file` (src/App.jsx): statement `urlEndpoint: "/integrations/google/url",`. It runs when the top of the file runs, in order, before the next line of the same function.

 166 |     syncEndpoint: "/integrations/gcal/sync",
     | In `the top of the file` (src/App.jsx): statement `syncEndpoint: "/integrations/gcal/sync",`. It runs when the top of the file runs, in order, before the next line of the same function.

 167 |     icon: () => (
     | In `the top of the file` (src/App.jsx): statement `icon: () => (`. It runs when the top of the file runs, in order, before the next line of the same function.

 168 |       <svg viewBox="0 0 24 24" fill="currentColor" width="14" height="14">
     | In `the top of the file` (src/App.jsx): Opens it. Vector drawing. It does not fetch data. Source: `<svg viewBox="0 0 24 24" fill="currentColor" width="14" height="14">`

 169 |         <path d="M19 3h-1V1h-2v2H8V1H6v2H5C3.9 3 3 3.9 3 5v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V8h14v11zM7 10h5v5H7z" />
     | In `the top of the file` (src/App.jsx): JSX `<path>`. React will create this node when the parent renders. Source: `<path d="M19 3h-1V1h-2v2H8V1H6v2H5C3.9 3 3 3.9 3 5v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V8h14v11zM7 10h5v5H7z" />`

 170 |       </svg>
     | In `the top of the file` (src/App.jsx): Closes it. Vector drawing. It does not fetch data. Source: `</svg>`

 171 |     ),
     | In `the top of the file` (src/App.jsx): statement `),`. It runs when the top of the file runs, in order, before the next line of the same function.

 172 |   },
     | In `the top of the file` (src/App.jsx): `},` closes { (opened on line 161). Names declared inside that block end here.

 173 | ];
     | In `the top of the file` (src/App.jsx): statement `];`. It runs when the top of the file runs, in order, before the next line of the same function.

 174 | 
     | Blank line in `src/App.jsx` (the shell: theme, menus, and which page is visible), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

 175 | function Sidebar({ theme, setTheme, onLogout, open, onClose }) {
     | Defines `Sidebar` in the shell: theme, menus, and which page is visible. Left navigation. Renders NAV_ITEMS, SECONDARY_NAV, connector links to /connectors, the compact energy control, coffee, theme, and logout. It does not fetch data.

 176 |   const location = useLocation();
     | In `Sidebar` (src/App.jsx): `location` is assigned `useLocation();`. Later lines in this function read that name.

 177 | 
     | Blank line in `src/App.jsx` (the shell: theme, menus, and which page is visible), inside Sidebar. The parser skips it. It separates the previous statement from the next so the function is readable.

 178 |   return (
     | In `Sidebar` (src/App.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

 179 |     <>
     | In `Sidebar` (src/App.jsx): JSX `<element>`. React will create this node when the parent renders. Source: `<>`

 180 |       {open && <div className="sidebar-backdrop" onClick={onClose} />}
     | In `Sidebar` (src/App.jsx): event prop `{open && <div className="sidebar-backdrop" onClick={onClose} />}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 181 |       <nav className={`sidebar${open ? " open" : ""}`} role="navigation" aria-label="Main navigation">
     | In `Sidebar` (src/App.jsx): Opens it. A navigation landmark. Source: `<nav className={`sidebar${open ? " open" : ""}`} role="navigation" aria-label="Main navigation">`

 182 |         {/* Brand */}
     | In `Sidebar` (src/App.jsx): `{/* Brand */}` closes Sidebar (opened on line 175). Names declared inside that block end here.

 183 |         <div className="sidebar-brand">
     | In `Sidebar` (src/App.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="sidebar-brand">`

 184 |           <div className="sidebar-logo">
     | In `Sidebar` (src/App.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="sidebar-logo">`

 185 |             <Logo size={36} variant="icon" />
     | In `Sidebar` (src/App.jsx): Opens it. The JB mark. Source: `<Logo size={36} variant="icon" />`

 186 |           </div>
     | In `Sidebar` (src/App.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 187 |           <div>
     | In `Sidebar` (src/App.jsx): Opens it. A box that groups the elements inside it. Source: `<div>`

 188 |             <div className="sidebar-title">Jumpy<span>Brain</span></div>
     | In `Sidebar` (src/App.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="sidebar-title">Jumpy<span>Brain</span></div>`

 189 |             <div className="sidebar-subtitle">Focus. Do more.</div>
     | In `Sidebar` (src/App.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="sidebar-subtitle">Focus. Do more.</div>`

 190 |           </div>
     | In `Sidebar` (src/App.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 191 |         </div>
     | In `Sidebar` (src/App.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 192 | 
     | Blank line in `src/App.jsx` (the shell: theme, menus, and which page is visible), inside Sidebar. The parser skips it. It separates the previous statement from the next so the function is readable.

 193 |         {/* Primary nav — 4 destinations */}
     | In `Sidebar` (src/App.jsx): `{/* Primary nav — 4 destinations */}` closes Sidebar (opened on line 175). Names declared inside that block end here.

 194 |         <div className="sidebar-nav-section">
     | In `Sidebar` (src/App.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="sidebar-nav-section">`

 195 |           {NAV_ITEMS.map(({ to, label, icon: Icon }) => (
     | In `Sidebar` (src/App.jsx): iteration `{NAV_ITEMS.map(({ to, label, icon: Icon }) => (`.

 196 |             <NavLink
     | In `Sidebar` (src/App.jsx): Opens it. A link that knows whether its route is active, so the CSS class 'active' can highlight it. Source: `<NavLink`

 197 |               key={to}
     | In `Sidebar` (src/App.jsx): `key={to}` closes Sidebar (opened on line 175). Names declared inside that block end here.

 198 |               to={to}
     | In `Sidebar` (src/App.jsx): `to={to}` closes Sidebar (opened on line 175). Names declared inside that block end here.

 199 |               end={to === "/"}
     | In `Sidebar` (src/App.jsx): `end={to === "/"}` closes Sidebar (opened on line 175). Names declared inside that block end here.

 200 |               className={({ isActive }) => `nav-item${isActive ? " active" : ""}`}
     | In `Sidebar` (src/App.jsx): statement `className={({ isActive }) => `nav-item${isActive ? " active" : ""}`}`. It runs when Sidebar runs, in order, before the next line of the same function.

 201 |               onClick={onClose}
     | In `Sidebar` (src/App.jsx): event prop `onClick={onClose}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 202 |             >
     | In `Sidebar` (src/App.jsx): statement `>`. It runs when Sidebar runs, in order, before the next line of the same function.

 203 |               <Icon />
     | In `Sidebar` (src/App.jsx): JSX `<Icon>`. React will create this node when the parent renders. Source: `<Icon />`

 204 |               {label}
     | In `Sidebar` (src/App.jsx): `{label}` closes Sidebar (opened on line 175). Names declared inside that block end here.

 205 |             </NavLink>
     | In `Sidebar` (src/App.jsx): Closes it. A link that knows whether its route is active, so the CSS class 'active' can highlight it. Source: `</NavLink>`

 206 |           ))}
     | In `Sidebar` (src/App.jsx): `))}` closes Sidebar (opened on line 175). Names declared inside that block end here.

 207 |         </div>
     | In `Sidebar` (src/App.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 208 | 
     | Blank line in `src/App.jsx` (the shell: theme, menus, and which page is visible), inside Sidebar. The parser skips it. It separates the previous statement from the next so the function is readable.

 209 |         {/* Secondary nav */}
     | In `Sidebar` (src/App.jsx): `{/* Secondary nav */}` closes Sidebar (opened on line 175). Names declared inside that block end here.

 210 |         <div className="sidebar-nav-section" style={{ marginTop: 8 }}>
     | In `Sidebar` (src/App.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="sidebar-nav-section" style={{ marginTop: 8 }}>`

 211 |           <div className="sidebar-section-label">More</div>
     | In `Sidebar` (src/App.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="sidebar-section-label">More</div>`

 212 |           {SECONDARY_NAV.map(({ to, label, icon: Icon }) => (
     | In `Sidebar` (src/App.jsx): iteration `{SECONDARY_NAV.map(({ to, label, icon: Icon }) => (`.

 213 |             <NavLink
     | In `Sidebar` (src/App.jsx): Opens it. A link that knows whether its route is active, so the CSS class 'active' can highlight it. Source: `<NavLink`

 214 |               key={to}
     | In `Sidebar` (src/App.jsx): `key={to}` closes Sidebar (opened on line 175). Names declared inside that block end here.

 215 |               to={to}
     | In `Sidebar` (src/App.jsx): `to={to}` closes Sidebar (opened on line 175). Names declared inside that block end here.

 216 |               className={({ isActive }) => `nav-item nav-item-sm${isActive ? " active" : ""}`}
     | In `Sidebar` (src/App.jsx): statement `className={({ isActive }) => `nav-item nav-item-sm${isActive ? " active" : ""}`}`. It runs when Sidebar runs, in order, before the next line of the same function.

 217 |               onClick={onClose}
     | In `Sidebar` (src/App.jsx): event prop `onClick={onClose}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 218 |             >
     | In `Sidebar` (src/App.jsx): statement `>`. It runs when Sidebar runs, in order, before the next line of the same function.

 219 |               <Icon />
     | In `Sidebar` (src/App.jsx): JSX `<Icon>`. React will create this node when the parent renders. Source: `<Icon />`

 220 |               {label}
     | In `Sidebar` (src/App.jsx): `{label}` closes Sidebar (opened on line 175). Names declared inside that block end here.

 221 |             </NavLink>
     | In `Sidebar` (src/App.jsx): Closes it. A link that knows whether its route is active, so the CSS class 'active' can highlight it. Source: `</NavLink>`

 222 |           ))}
     | In `Sidebar` (src/App.jsx): `))}` closes Sidebar (opened on line 175). Names declared inside that block end here.

 223 |           <a
     | In `Sidebar` (src/App.jsx): Opens it. A normal link. If it has target=_blank it leaves the app. Source: `<a`

 224 |             href={FEEDBACK_URL}
     | In `Sidebar` (src/App.jsx): `href={FEEDBACK_URL}` closes Sidebar (opened on line 175). Names declared inside that block end here.

 225 |             target="_blank"
     | In `Sidebar` (src/App.jsx): statement `target="_blank"`. It runs when Sidebar runs, in order, before the next line of the same function.

 226 |             rel="noopener noreferrer"
     | In `Sidebar` (src/App.jsx): statement `rel="noopener noreferrer"`. It runs when Sidebar runs, in order, before the next line of the same function.

 227 |             className="nav-item nav-item-sm nav-item-feedback"
     | In `Sidebar` (src/App.jsx): statement `className="nav-item nav-item-sm nav-item-feedback"`. It runs when Sidebar runs, in order, before the next line of the same function.

 228 |             onClick={onClose}
     | In `Sidebar` (src/App.jsx): event prop `onClick={onClose}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 229 |           >
     | In `Sidebar` (src/App.jsx): statement `>`. It runs when Sidebar runs, in order, before the next line of the same function.

 230 |             <Icons.Feedback />
     | In `Sidebar` (src/App.jsx): JSX `<Icons.Feedback>`. React will create this node when the parent renders. Source: `<Icons.Feedback />`

 231 |             Feedback
     | In `Sidebar` (src/App.jsx): statement `Feedback`. It runs when Sidebar runs, in order, before the next line of the same function.

 232 |           </a>
     | In `Sidebar` (src/App.jsx): Closes it. A normal link. If it has target=_blank it leaves the app. Source: `</a>`

 233 |         </div>
     | In `Sidebar` (src/App.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 234 | 
     | Blank line in `src/App.jsx` (the shell: theme, menus, and which page is visible), inside Sidebar. The parser skips it. It separates the previous statement from the next so the function is readable.

 235 |         {/* Connectors — compact rows */}
     | In `Sidebar` (src/App.jsx): `{/* Connectors — compact rows */}` closes Sidebar (opened on line 175). Names declared inside that block end here.

 236 |         <div className="sidebar-nav-section" style={{ marginTop: 8 }}>
     | In `Sidebar` (src/App.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="sidebar-nav-section" style={{ marginTop: 8 }}>`

 237 |           <div className="sidebar-section-label">Connectors</div>
     | In `Sidebar` (src/App.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="sidebar-section-label">Connectors</div>`

 238 |           {CONNECTORS.map(({ id, label, color, icon: Icon }) => (
     | In `Sidebar` (src/App.jsx): iteration `{CONNECTORS.map(({ id, label, color, icon: Icon }) => (`.

 239 |             <Link
     | In `Sidebar` (src/App.jsx): Opens it. A react-router link. Clicking it changes the URL without a full page reload. Source: `<Link`

 240 |               key={id}
     | In `Sidebar` (src/App.jsx): `key={id}` closes Sidebar (opened on line 175). Names declared inside that block end here.

 241 |               to="/connectors"
     | In `Sidebar` (src/App.jsx): statement `to="/connectors"`. It runs when Sidebar runs, in order, before the next line of the same function.

 242 |               className={`connector-row${location.pathname === "/connectors" ? " active" : ""}`}
     | In `Sidebar` (src/App.jsx): `className={`connector-row${location.pathname === "/connectors" ? " active" : ""}`}` closes Sidebar (opened on line 175). Names declared inside that block end here.

 243 |               onClick={onClose}
     | In `Sidebar` (src/App.jsx): event prop `onClick={onClose}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 244 |             >
     | In `Sidebar` (src/App.jsx): statement `>`. It runs when Sidebar runs, in order, before the next line of the same function.

 245 |               <span className="connector-row-icon" style={{ color, background: color + "20" }}>
     | In `Sidebar` (src/App.jsx): Opens it. An inline box. Source: `<span className="connector-row-icon" style={{ color, background: color + "20" }}>`

 246 |                 <Icon />
     | In `Sidebar` (src/App.jsx): JSX `<Icon>`. React will create this node when the parent renders. Source: `<Icon />`

 247 |               </span>
     | In `Sidebar` (src/App.jsx): Closes it. An inline box. Source: `</span>`

 248 |               <span className="connector-row-label">{label}</span>
     | In `Sidebar` (src/App.jsx): Opens it. An inline box. Source: `<span className="connector-row-label">{label}</span>`

 249 |             </Link>
     | In `Sidebar` (src/App.jsx): Closes it. A react-router link. Clicking it changes the URL without a full page reload. Source: `</Link>`

 250 |           ))}
     | In `Sidebar` (src/App.jsx): `))}` closes Sidebar (opened on line 175). Names declared inside that block end here.

 251 |         </div>
     | In `Sidebar` (src/App.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 252 | 
     | Blank line in `src/App.jsx` (the shell: theme, menus, and which page is visible), inside Sidebar. The parser skips it. It separates the previous statement from the next so the function is readable.

 253 |         {/* Pinned energy control */}
     | In `Sidebar` (src/App.jsx): `{/* Pinned energy control */}` closes Sidebar (opened on line 175). Names declared inside that block end here.

 254 |         <div className="sidebar-energy">
     | In `Sidebar` (src/App.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="sidebar-energy">`

 255 |           <div className="sidebar-section-label">Energy level</div>
     | In `Sidebar` (src/App.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="sidebar-section-label">Energy level</div>`

 256 |           <EnergyControl compact />
     | In `Sidebar` (src/App.jsx): Opens it. The energy faces. compact is the sidebar dots; without it, the big buttons on Today. Source: `<EnergyControl compact />`

 257 |         </div>
     | In `Sidebar` (src/App.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 258 | 
     | Blank line in `src/App.jsx` (the shell: theme, menus, and which page is visible), inside Sidebar. The parser skips it. It separates the previous statement from the next so the function is readable.

 259 |         {/* Footer controls */}
     | In `Sidebar` (src/App.jsx): `{/* Footer controls */}` closes Sidebar (opened on line 175). Names declared inside that block end here.

 260 |         <div className="sidebar-footer">
     | In `Sidebar` (src/App.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="sidebar-footer">`

 261 |           <a
     | In `Sidebar` (src/App.jsx): Opens it. A normal link. If it has target=_blank it leaves the app. Source: `<a`

 262 |             href={FUNDING_URL}
     | In `Sidebar` (src/App.jsx): `href={FUNDING_URL}` closes Sidebar (opened on line 175). Names declared inside that block end here.

 263 |             target="_blank"
     | In `Sidebar` (src/App.jsx): statement `target="_blank"`. It runs when Sidebar runs, in order, before the next line of the same function.

 264 |             rel="noopener noreferrer"
     | In `Sidebar` (src/App.jsx): statement `rel="noopener noreferrer"`. It runs when Sidebar runs, in order, before the next line of the same function.

 265 |             className="support-btn"
     | In `Sidebar` (src/App.jsx): statement `className="support-btn"`. It runs when Sidebar runs, in order, before the next line of the same function.

 266 |             aria-label="Buy me a coffee (opens buymeacoffee.com in a new tab)"
     | In `Sidebar` (src/App.jsx): statement `aria-label="Buy me a coffee (opens buymeacoffee.com in a new tab)"`. It runs when Sidebar runs, in order, before the next line of the same function.

 267 |           >
     | In `Sidebar` (src/App.jsx): statement `>`. It runs when Sidebar runs, in order, before the next line of the same function.

 268 |             <Icons.Coffee />
     | In `Sidebar` (src/App.jsx): JSX `<Icons.Coffee>`. React will create this node when the parent renders. Source: `<Icons.Coffee />`

 269 |             Buy me a coffee
     | In `Sidebar` (src/App.jsx): statement `Buy me a coffee`. It runs when Sidebar runs, in order, before the next line of the same function.

 270 |           </a>
     | In `Sidebar` (src/App.jsx): Closes it. A normal link. If it has target=_blank it leaves the app. Source: `</a>`

 271 |           <button
     | In `Sidebar` (src/App.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button`

 272 |             className="theme-toggle"
     | In `Sidebar` (src/App.jsx): statement `className="theme-toggle"`. It runs when Sidebar runs, in order, before the next line of the same function.

 273 |             onClick={() => setTheme((t) => (t === "dark" ? "light" : "dark"))}
     | In `Sidebar` (src/App.jsx): event prop `onClick={() => setTheme((t) => (t === "dark" ? "light" : "dark"))}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 274 |             aria-label="Toggle theme"
     | In `Sidebar` (src/App.jsx): statement `aria-label="Toggle theme"`. It runs when Sidebar runs, in order, before the next line of the same function.

 275 |           >
     | In `Sidebar` (src/App.jsx): statement `>`. It runs when Sidebar runs, in order, before the next line of the same function.

 276 |             {theme === "dark" ? <Icons.Sun /> : <Icons.Moon />}
     | In `Sidebar` (src/App.jsx): `{theme === "dark" ? <Icons.Sun /> : <Icons.Moon />}` closes Sidebar (opened on line 175). Names declared inside that block end here.

 277 |             {theme === "dark" ? "Light mode" : "Dark mode"}
     | In `Sidebar` (src/App.jsx): `{theme === "dark" ? "Light mode" : "Dark mode"}` closes Sidebar (opened on line 175). Names declared inside that block end here.

 278 |           </button>
     | In `Sidebar` (src/App.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

 279 |           <button className="logout-btn" onClick={onLogout} aria-label="Logout">
     | In `Sidebar` (src/App.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button className="logout-btn" onClick={onLogout} aria-label="Logout">`

 280 |             <Icons.Logout />
     | In `Sidebar` (src/App.jsx): JSX `<Icons.Logout>`. React will create this node when the parent renders. Source: `<Icons.Logout />`

 281 |             Logout
     | In `Sidebar` (src/App.jsx): statement `Logout`. It runs when Sidebar runs, in order, before the next line of the same function.

 282 |           </button>
     | In `Sidebar` (src/App.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

 283 |         </div>
     | In `Sidebar` (src/App.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 284 |       </nav>
     | In `Sidebar` (src/App.jsx): Closes it. A navigation landmark. Source: `</nav>`

 285 |     </>
     | In `Sidebar` (src/App.jsx): JSX `<element>`. This closes that element. Source: `</>`

 286 |   );
     | In `Sidebar` (src/App.jsx): statement `);`. It runs when Sidebar runs, in order, before the next line of the same function.

 287 | }
     | In `Sidebar` (src/App.jsx): `}` closes Sidebar (opened on line 175). Names declared inside that block end here.

 288 | 
     | Blank line in `src/App.jsx` (the shell: theme, menus, and which page is visible), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

 289 | function TopBar({ theme, setTheme, onMenuClick, onMoreClick, onLogout }) {
     | Defines `TopBar` in the shell: theme, menus, and which page is visible. The bar above the page. The title is whichever nav item matches the URL. Initials come from the user name. Buttons open the sidebar, the More sheet, connectors, feedback, theme, settings, and logout.

 290 |   const location = useLocation();
     | In `TopBar` (src/App.jsx): `location` is assigned `useLocation();`. Later lines in this function read that name.

 291 |   const { user } = useUser();
     | In `TopBar` (src/App.jsx): `user`: The logged-in profile object. Null means ProtectedRoute renders Auth. The code is `const { user } = useUser();`.

 292 |   const currentNav = [...NAV_ITEMS, ...SECONDARY_NAV].find((n) =>
     | In `TopBar` (src/App.jsx): `currentNav` is assigned `[...NAV_ITEMS, ...SECONDARY_NAV].find((n) =>`. Later lines in this function read that name.

 293 |     n.to === "/" ? location.pathname === "/" : location.pathname.startsWith(n.to)
     | In `TopBar` (src/App.jsx): statement `n.to === "/" ? location.pathname === "/" : location.pathname.startsWith(n.to)`. It runs when TopBar runs, in order, before the next line of the same function.

 294 |   );
     | In `TopBar` (src/App.jsx): statement `);`. It runs when TopBar runs, in order, before the next line of the same function.

 295 |   const pageTitle = currentNav?.label ?? "JumpyBrain";
     | In `TopBar` (src/App.jsx): `pageTitle` is assigned `currentNav?.label ?? "JumpyBrain";`. Later lines in this function read that name.

 296 | 
     | Blank line in `src/App.jsx` (the shell: theme, menus, and which page is visible), inside TopBar. The parser skips it. It separates the previous statement from the next so the function is readable.

 297 |   const initials = user?.name
     | In `TopBar` (src/App.jsx): `initials` is assigned `user?.name`. Later lines in this function read that name.

 298 |     ? user.name.trim().split(/\s+/).slice(0, 2).map((w) => w[0].toUpperCase()).join("")
     | In `TopBar` (src/App.jsx): iteration `? user.name.trim().split(/\s+/).slice(0, 2).map((w) => w[0].toUpperCase()).join("")`.

 299 |     : (user?.email || "?")[0].toUpperCase();
     | In `TopBar` (src/App.jsx): statement `: (user?.email || "?")[0].toUpperCase();`. It runs when TopBar runs, in order, before the next line of the same function.

 300 | 
     | Blank line in `src/App.jsx` (the shell: theme, menus, and which page is visible), inside TopBar. The parser skips it. It separates the previous statement from the next so the function is readable.

 301 |   return (
     | In `TopBar` (src/App.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

 302 |     <header className="top-bar" role="banner">
     | In `TopBar` (src/App.jsx): Opens it. The top bar landmark. Source: `<header className="top-bar" role="banner">`

 303 |       <div className="top-bar-left">
     | In `TopBar` (src/App.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="top-bar-left">`

 304 |         <button
     | In `TopBar` (src/App.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button`

 305 |           className="top-bar-menu-btn"
     | In `TopBar` (src/App.jsx): statement `className="top-bar-menu-btn"`. It runs when TopBar runs, in order, before the next line of the same function.

 306 |           onClick={onMenuClick}
     | In `TopBar` (src/App.jsx): event prop `onClick={onMenuClick}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 307 |           aria-label="Open navigation menu"
     | In `TopBar` (src/App.jsx): statement `aria-label="Open navigation menu"`. It runs when TopBar runs, in order, before the next line of the same function.

 308 |         >
     | In `TopBar` (src/App.jsx): statement `>`. It runs when TopBar runs, in order, before the next line of the same function.

 309 |           <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2.2} strokeLinecap="round">
     | In `TopBar` (src/App.jsx): Opens it. Vector drawing. It does not fetch data. Source: `<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2.2} strokeLinecap="round">`

 310 |             <line x1="3" y1="6" x2="21" y2="6" />
     | In `TopBar` (src/App.jsx): JSX `<line>`. React will create this node when the parent renders. Source: `<line x1="3" y1="6" x2="21" y2="6" />`

 311 |             <line x1="3" y1="12" x2="21" y2="12" />
     | In `TopBar` (src/App.jsx): JSX `<line>`. React will create this node when the parent renders. Source: `<line x1="3" y1="12" x2="21" y2="12" />`

 312 |             <line x1="3" y1="18" x2="21" y2="18" />
     | In `TopBar` (src/App.jsx): JSX `<line>`. React will create this node when the parent renders. Source: `<line x1="3" y1="18" x2="21" y2="18" />`

 313 |           </svg>
     | In `TopBar` (src/App.jsx): Closes it. Vector drawing. It does not fetch data. Source: `</svg>`

 314 |         </button>
     | In `TopBar` (src/App.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

 315 |         <div className="top-bar-brand">
     | In `TopBar` (src/App.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="top-bar-brand">`

 316 |           <Logo size={28} variant="icon" />
     | In `TopBar` (src/App.jsx): Opens it. The JB mark. Source: `<Logo size={28} variant="icon" />`

 317 |           <span className="top-bar-page-title">{pageTitle}</span>
     | In `TopBar` (src/App.jsx): Opens it. An inline box. Source: `<span className="top-bar-page-title">{pageTitle}</span>`

 318 |         </div>
     | In `TopBar` (src/App.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 319 |       </div>
     | In `TopBar` (src/App.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 320 | 
     | Blank line in `src/App.jsx` (the shell: theme, menus, and which page is visible), inside TopBar. The parser skips it. It separates the previous statement from the next so the function is readable.

 321 |       <div className="top-bar-right">
     | In `TopBar` (src/App.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="top-bar-right">`

 322 |         <button
     | In `TopBar` (src/App.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button`

 323 |           className="top-bar-icon-btn top-bar-more-btn"
     | In `TopBar` (src/App.jsx): statement `className="top-bar-icon-btn top-bar-more-btn"`. It runs when TopBar runs, in order, before the next line of the same function.

 324 |           onClick={onMoreClick}
     | In `TopBar` (src/App.jsx): event prop `onClick={onMoreClick}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 325 |           aria-label="More — Focus Timer, Focus Shield, Mindfulness, Deadlines"
     | In `TopBar` (src/App.jsx): statement `aria-label="More — Focus Timer, Focus Shield, Mindfulness, Deadlines"`. It runs when TopBar runs, in order, before the next line of the same function.

 326 |           title="More"
     | In `TopBar` (src/App.jsx): statement `title="More"`. It runs when TopBar runs, in order, before the next line of the same function.

 327 |         >
     | In `TopBar` (src/App.jsx): statement `>`. It runs when TopBar runs, in order, before the next line of the same function.

 328 |           <Icons.More />
     | In `TopBar` (src/App.jsx): JSX `<Icons.More>`. React will create this node when the parent renders. Source: `<Icons.More />`

 329 |         </button>
     | In `TopBar` (src/App.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

 330 |         <Link
     | In `TopBar` (src/App.jsx): Opens it. A react-router link. Clicking it changes the URL without a full page reload. Source: `<Link`

 331 |           to="/connectors"
     | In `TopBar` (src/App.jsx): statement `to="/connectors"`. It runs when TopBar runs, in order, before the next line of the same function.

 332 |           className="top-bar-icon-btn"
     | In `TopBar` (src/App.jsx): statement `className="top-bar-icon-btn"`. It runs when TopBar runs, in order, before the next line of the same function.

 333 |           title="Connectors"
     | In `TopBar` (src/App.jsx): statement `title="Connectors"`. It runs when TopBar runs, in order, before the next line of the same function.

 334 |           aria-label="Manage connectors"
     | In `TopBar` (src/App.jsx): statement `aria-label="Manage connectors"`. It runs when TopBar runs, in order, before the next line of the same function.

 335 |         >
     | In `TopBar` (src/App.jsx): statement `>`. It runs when TopBar runs, in order, before the next line of the same function.

 336 |           <Icons.Plug />
     | In `TopBar` (src/App.jsx): JSX `<Icons.Plug>`. React will create this node when the parent renders. Source: `<Icons.Plug />`

 337 |         </Link>
     | In `TopBar` (src/App.jsx): Closes it. A react-router link. Clicking it changes the URL without a full page reload. Source: `</Link>`

 338 |         <a
     | In `TopBar` (src/App.jsx): Opens it. A normal link. If it has target=_blank it leaves the app. Source: `<a`

 339 |           href={FEEDBACK_URL}
     | In `TopBar` (src/App.jsx): `href={FEEDBACK_URL}` closes TopBar (opened on line 289). Names declared inside that block end here.

 340 |           target="_blank"
     | In `TopBar` (src/App.jsx): statement `target="_blank"`. It runs when TopBar runs, in order, before the next line of the same function.

 341 |           rel="noopener noreferrer"
     | In `TopBar` (src/App.jsx): statement `rel="noopener noreferrer"`. It runs when TopBar runs, in order, before the next line of the same function.

 342 |           className="top-bar-icon-btn top-bar-feedback-btn"
     | In `TopBar` (src/App.jsx): statement `className="top-bar-icon-btn top-bar-feedback-btn"`. It runs when TopBar runs, in order, before the next line of the same function.

 343 |           title="Share feedback"
     | In `TopBar` (src/App.jsx): statement `title="Share feedback"`. It runs when TopBar runs, in order, before the next line of the same function.

 344 |           aria-label="Share feedback"
     | In `TopBar` (src/App.jsx): statement `aria-label="Share feedback"`. It runs when TopBar runs, in order, before the next line of the same function.

 345 |         >
     | In `TopBar` (src/App.jsx): statement `>`. It runs when TopBar runs, in order, before the next line of the same function.

 346 |           <Icons.Feedback />
     | In `TopBar` (src/App.jsx): JSX `<Icons.Feedback>`. React will create this node when the parent renders. Source: `<Icons.Feedback />`

 347 |         </a>
     | In `TopBar` (src/App.jsx): Closes it. A normal link. If it has target=_blank it leaves the app. Source: `</a>`

 348 |         <button
     | In `TopBar` (src/App.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button`

 349 |           className="top-bar-icon-btn"
     | In `TopBar` (src/App.jsx): statement `className="top-bar-icon-btn"`. It runs when TopBar runs, in order, before the next line of the same function.

 350 |           onClick={() => setTheme((t) => (t === "dark" ? "light" : "dark"))}
     | In `TopBar` (src/App.jsx): event prop `onClick={() => setTheme((t) => (t === "dark" ? "light" : "dark"))}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 351 |           aria-label="Toggle theme"
     | In `TopBar` (src/App.jsx): statement `aria-label="Toggle theme"`. It runs when TopBar runs, in order, before the next line of the same function.

 352 |         >
     | In `TopBar` (src/App.jsx): statement `>`. It runs when TopBar runs, in order, before the next line of the same function.

 353 |           {theme === "dark" ? <Icons.Sun /> : <Icons.Moon />}
     | In `TopBar` (src/App.jsx): `{theme === "dark" ? <Icons.Sun /> : <Icons.Moon />}` closes TopBar (opened on line 289). Names declared inside that block end here.

 354 |         </button>
     | In `TopBar` (src/App.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

 355 |         <Link
     | In `TopBar` (src/App.jsx): Opens it. A react-router link. Clicking it changes the URL without a full page reload. Source: `<Link`

 356 |           to="/settings"
     | In `TopBar` (src/App.jsx): statement `to="/settings"`. It runs when TopBar runs, in order, before the next line of the same function.

 357 |           className="top-bar-avatar"
     | In `TopBar` (src/App.jsx): statement `className="top-bar-avatar"`. It runs when TopBar runs, in order, before the next line of the same function.

 358 |           title="Profile & Settings"
     | In `TopBar` (src/App.jsx): statement `title="Profile & Settings"`. It runs when TopBar runs, in order, before the next line of the same function.

 359 |           aria-label="Profile and settings"
     | In `TopBar` (src/App.jsx): statement `aria-label="Profile and settings"`. It runs when TopBar runs, in order, before the next line of the same function.

 360 |         >
     | In `TopBar` (src/App.jsx): statement `>`. It runs when TopBar runs, in order, before the next line of the same function.

 361 |           {initials}
     | In `TopBar` (src/App.jsx): `{initials}` closes TopBar (opened on line 289). Names declared inside that block end here.

 362 |         </Link>
     | In `TopBar` (src/App.jsx): Closes it. A react-router link. Clicking it changes the URL without a full page reload. Source: `</Link>`

 363 |         <button
     | In `TopBar` (src/App.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button`

 364 |           className="top-bar-icon-btn top-bar-logout-btn"
     | In `TopBar` (src/App.jsx): statement `className="top-bar-icon-btn top-bar-logout-btn"`. It runs when TopBar runs, in order, before the next line of the same function.

 365 |           onClick={onLogout}
     | In `TopBar` (src/App.jsx): event prop `onClick={onLogout}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 366 |           aria-label="Logout"
     | In `TopBar` (src/App.jsx): statement `aria-label="Logout"`. It runs when TopBar runs, in order, before the next line of the same function.

 367 |           title="Logout"
     | In `TopBar` (src/App.jsx): statement `title="Logout"`. It runs when TopBar runs, in order, before the next line of the same function.

 368 |         >
     | In `TopBar` (src/App.jsx): statement `>`. It runs when TopBar runs, in order, before the next line of the same function.

 369 |           <Icons.Logout />
     | In `TopBar` (src/App.jsx): JSX `<Icons.Logout>`. React will create this node when the parent renders. Source: `<Icons.Logout />`

 370 |         </button>
     | In `TopBar` (src/App.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

 371 |       </div>
     | In `TopBar` (src/App.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 372 |     </header>
     | In `TopBar` (src/App.jsx): Closes it. The top bar landmark. Source: `</header>`

 373 |   );
     | In `TopBar` (src/App.jsx): statement `);`. It runs when TopBar runs, in order, before the next line of the same function.

 374 | }
     | In `TopBar` (src/App.jsx): `}` closes TopBar (opened on line 289). Names declared inside that block end here.

 375 | 
     | Blank line in `src/App.jsx` (the shell: theme, menus, and which page is visible), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

 376 | // Bottom nav for mobile (4 primary destinations + Profile & Settings)
     | Comment inside the top of the file. Not executed. It documents the next code: Bottom nav for mobile (4 primary destinations + Profile & Settings)

 377 | function BottomNav({ onLogout }) {
     | Defines `BottomNav` in the shell: theme, menus, and which page is visible. Phone navigation: the four primary routes plus Profile. CSS hides it on wide screens.

 378 |   return (
     | In `BottomNav` (src/App.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

 379 |     <nav className="bottom-nav" aria-label="Mobile navigation">
     | In `BottomNav` (src/App.jsx): Opens it. A navigation landmark. Source: `<nav className="bottom-nav" aria-label="Mobile navigation">`

 380 |       {NAV_ITEMS.map(({ to, label, icon: Icon }) => (
     | In `BottomNav` (src/App.jsx): iteration `{NAV_ITEMS.map(({ to, label, icon: Icon }) => (`.

 381 |         <NavLink
     | In `BottomNav` (src/App.jsx): Opens it. A link that knows whether its route is active, so the CSS class 'active' can highlight it. Source: `<NavLink`

 382 |           key={to}
     | In `BottomNav` (src/App.jsx): `key={to}` closes BottomNav (opened on line 377). Names declared inside that block end here.

 383 |           to={to}
     | In `BottomNav` (src/App.jsx): `to={to}` closes BottomNav (opened on line 377). Names declared inside that block end here.

 384 |           end={to === "/"}
     | In `BottomNav` (src/App.jsx): `end={to === "/"}` closes BottomNav (opened on line 377). Names declared inside that block end here.

 385 |           className={({ isActive }) => `bottom-nav-item${isActive ? " active" : ""}`}
     | In `BottomNav` (src/App.jsx): statement `className={({ isActive }) => `bottom-nav-item${isActive ? " active" : ""}`}`. It runs when BottomNav runs, in order, before the next line of the same function.

 386 |         >
     | In `BottomNav` (src/App.jsx): statement `>`. It runs when BottomNav runs, in order, before the next line of the same function.

 387 |           <Icon />
     | In `BottomNav` (src/App.jsx): JSX `<Icon>`. React will create this node when the parent renders. Source: `<Icon />`

 388 |           <span>{label}</span>
     | In `BottomNav` (src/App.jsx): Opens it. An inline box. Source: `<span>{label}</span>`

 389 |         </NavLink>
     | In `BottomNav` (src/App.jsx): Closes it. A link that knows whether its route is active, so the CSS class 'active' can highlight it. Source: `</NavLink>`

 390 |       ))}
     | In `BottomNav` (src/App.jsx): `))}` closes BottomNav (opened on line 377). Names declared inside that block end here.

 391 |       <NavLink
     | In `BottomNav` (src/App.jsx): Opens it. A link that knows whether its route is active, so the CSS class 'active' can highlight it. Source: `<NavLink`

 392 |         to="/settings"
     | In `BottomNav` (src/App.jsx): statement `to="/settings"`. It runs when BottomNav runs, in order, before the next line of the same function.

 393 |         className={({ isActive }) => `bottom-nav-item${isActive ? " active" : ""}`}
     | In `BottomNav` (src/App.jsx): statement `className={({ isActive }) => `bottom-nav-item${isActive ? " active" : ""}`}`. It runs when BottomNav runs, in order, before the next line of the same function.

 394 |         aria-label="Profile & Settings"
     | In `BottomNav` (src/App.jsx): statement `aria-label="Profile & Settings"`. It runs when BottomNav runs, in order, before the next line of the same function.

 395 |       >
     | In `BottomNav` (src/App.jsx): statement `>`. It runs when BottomNav runs, in order, before the next line of the same function.

 396 |         <Icons.Profile />
     | In `BottomNav` (src/App.jsx): JSX `<Icons.Profile>`. React will create this node when the parent renders. Source: `<Icons.Profile />`

 397 |         <span>Profile</span>
     | In `BottomNav` (src/App.jsx): Opens it. An inline box. Source: `<span>Profile</span>`

 398 |       </NavLink>
     | In `BottomNav` (src/App.jsx): Closes it. A link that knows whether its route is active, so the CSS class 'active' can highlight it. Source: `</NavLink>`

 399 |     </nav>
     | In `BottomNav` (src/App.jsx): Closes it. A navigation landmark. Source: `</nav>`

 400 |   );
     | In `BottomNav` (src/App.jsx): statement `);`. It runs when BottomNav runs, in order, before the next line of the same function.

 401 | }
     | In `BottomNav` (src/App.jsx): `}` closes BottomNav (opened on line 377). Names declared inside that block end here.

 402 | 
     | Blank line in `src/App.jsx` (the shell: theme, menus, and which page is visible), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

 403 | function SheetConnectors({ open }) {
     | Defines `SheetConnectors` in the shell: theme, menus, and which page is visible. The connector rows inside the More sheet. On open it GET /integrations/status. Connect redirects to the OAuth URL. Sync POSTs. Disconnect DELETEs.

 404 |   const [status, setStatus] = useState(null);
     | In `SheetConnectors` (src/App.jsx): React state `status, setStatus`. The value survives re-renders. Calling the setter re-renders this component. `const [status, setStatus] = useState(null);`

 405 |   const [syncing, setSyncing] = useState({});
     | In `SheetConnectors` (src/App.jsx): React state `syncing, setSyncing`. The value survives re-renders. Calling the setter re-renders this component. `const [syncing, setSyncing] = useState({});`

 406 |   const [connecting, setConnecting] = useState({});
     | In `SheetConnectors` (src/App.jsx): React state `connecting, setConnecting`. The value survives re-renders. Calling the setter re-renders this component. `const [connecting, setConnecting] = useState({});`

 407 | 
     | Blank line in `src/App.jsx` (the shell: theme, menus, and which page is visible), inside SheetConnectors. The parser skips it. It separates the previous statement from the next so the function is readable.

 408 |   useEffect(() => {
     | In `SheetConnectors` (src/App.jsx): opens or continues an effect — `useEffect(() => {`. The effect body runs after paint, and its cleanup runs before the next effect and on unmount.

 409 |     if (!open) return;
     | In `SheetConnectors` (src/App.jsx): branch `if (!open) return;`. Only one side runs.

 410 |     api.get('/integrations/status').then(setStatus).catch(() => {});
     | In `SheetConnectors` (src/App.jsx): HTTP via the shared Axios instance — `api.get('/integrations/status').then(setStatus).catch(() => {});`. The request interceptor adds `Authorization: Bearer <accessToken>`. The response interceptor returns `res.data`, so the awaited value is the JSON body.

 411 |   }, [open]);
     | In `SheetConnectors` (src/App.jsx): `}, [open]);` closes effect in SheetConnectors (opened on line 408). Names declared inside that block end here.

 412 | 
     | Blank line in `src/App.jsx` (the shell: theme, menus, and which page is visible), inside SheetConnectors. The parser skips it. It separates the previous statement from the next so the function is readable.

 413 |   async function handleConnect(connector) {
     | Defines `handleConnect` in the shell: theme, menus, and which page is visible. GET the connector's urlEndpoint and set window.location to that OAuth URL.

 414 |     setConnecting(p => ({ ...p, [connector.id]: true }));
     | In `handleConnect` (src/App.jsx): statement `setConnecting(p => ({ ...p, [connector.id]: true }));`. It runs when handleConnect runs, in order, before the next line of the same function.

 415 |     try {
     | In `handleConnect` (src/App.jsx): error path `try {`.

 416 |       const { url } = await api.get(connector.urlEndpoint);
     | In `handleConnect` (src/App.jsx): `url` is assigned `await api.get(connector.urlEndpoint);`. Later lines in this function read that name.

 417 |       window.location.href = url;
     | In `handleConnect` (src/App.jsx): statement `window.location.href = url;`. It runs when handleConnect runs, in order, before the next line of the same function.

 418 |     } catch {
     | In `handleConnect` (src/App.jsx): `} catch {` closes try { (opened on line 415). Names declared inside that block end here.

 419 |       setConnecting(p => ({ ...p, [connector.id]: false }));
     | In `handleConnect` (src/App.jsx): statement `setConnecting(p => ({ ...p, [connector.id]: false }));`. It runs when handleConnect runs, in order, before the next line of the same function.

 420 |     }
     | In `handleConnect` (src/App.jsx): `}` closes } catch { (opened on line 418). Names declared inside that block end here.

 421 |   }
     | In `handleConnect` (src/App.jsx): `}` closes handleConnect (opened on line 413). Names declared inside that block end here.

 422 | 
     | Blank line in `src/App.jsx` (the shell: theme, menus, and which page is visible), inside SheetConnectors. The parser skips it. It separates the previous statement from the next so the function is readable.

 423 |   async function handleSync(connector) {
     | Defines `handleSync` in the shell: theme, menus, and which page is visible. POST the sync endpoint. The page toast includes result.synced and result.created.

 424 |     setSyncing(p => ({ ...p, [connector.id]: true }));
     | In `handleSync` (src/App.jsx): statement `setSyncing(p => ({ ...p, [connector.id]: true }));`. It runs when handleSync runs, in order, before the next line of the same function.

 425 |     try {
     | In `handleSync` (src/App.jsx): error path `try {`.

 426 |       await api.post(connector.syncEndpoint);
     | In `handleSync` (src/App.jsx): HTTP via the shared Axios instance — `await api.post(connector.syncEndpoint);`. The request interceptor adds `Authorization: Bearer <accessToken>`. The response interceptor returns `res.data`, so the awaited value is the JSON body.

 427 |       const data = await api.get('/integrations/status');
     | In `handleSync` (src/App.jsx): `data` is assigned `await api.get('/integrations/status');`. Later lines in this function read that name.

 428 |       setStatus(data);
     | In `handleSync` (src/App.jsx): statement `setStatus(data);`. It runs when handleSync runs, in order, before the next line of the same function.

 429 |     } catch {
     | In `handleSync` (src/App.jsx): `} catch {` closes try { (opened on line 425). Names declared inside that block end here.

 430 |     } finally {
     | In `handleSync` (src/App.jsx): `} finally {` closes } catch { (opened on line 429). Names declared inside that block end here.

 431 |       setSyncing(p => ({ ...p, [connector.id]: false }));
     | In `handleSync` (src/App.jsx): statement `setSyncing(p => ({ ...p, [connector.id]: false }));`. It runs when handleSync runs, in order, before the next line of the same function.

 432 |     }
     | In `handleSync` (src/App.jsx): `}` closes } finally { (opened on line 430). Names declared inside that block end here.

 433 |   }
     | In `handleSync` (src/App.jsx): `}` closes handleSync (opened on line 423). Names declared inside that block end here.

 434 | 
     | Blank line in `src/App.jsx` (the shell: theme, menus, and which page is visible), inside SheetConnectors. The parser skips it. It separates the previous statement from the next so the function is readable.

 435 |   async function handleDisconnect(connector) {
     | Defines `handleDisconnect` in the shell: theme, menus, and which page is visible. DELETE /integrations/:id and refresh status.

 436 |     try {
     | In `handleDisconnect` (src/App.jsx): error path `try {`.

 437 |       await api.delete(`/integrations/${connector.id}`);
     | In `handleDisconnect` (src/App.jsx): HTTP via the shared Axios instance — `await api.delete(`/integrations/${connector.id}`);`. The request interceptor adds `Authorization: Bearer <accessToken>`. The response interceptor returns `res.data`, so the awaited value is the JSON body.

 438 |       const data = await api.get('/integrations/status');
     | In `handleDisconnect` (src/App.jsx): `data` is assigned `await api.get('/integrations/status');`. Later lines in this function read that name.

 439 |       setStatus(data);
     | In `handleDisconnect` (src/App.jsx): statement `setStatus(data);`. It runs when handleDisconnect runs, in order, before the next line of the same function.

 440 |     } catch {}
     | In `handleDisconnect` (src/App.jsx): `} catch {}` closes try { (opened on line 436). Names declared inside that block end here.

 441 |   }
     | In `handleDisconnect` (src/App.jsx): `}` closes handleDisconnect (opened on line 435). Names declared inside that block end here.

 442 | 
     | Blank line in `src/App.jsx` (the shell: theme, menus, and which page is visible), inside SheetConnectors. The parser skips it. It separates the previous statement from the next so the function is readable.

 443 |   return (
     | In `SheetConnectors` (src/App.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

 444 |     <div className="sheet-connectors">
     | In `SheetConnectors` (src/App.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="sheet-connectors">`

 445 |       <div className="sidebar-section-label">Connectors</div>
     | In `SheetConnectors` (src/App.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="sidebar-section-label">Connectors</div>`

 446 |       {CONNECTORS.map((connector) => {
     | In `SheetConnectors` (src/App.jsx): iteration `{CONNECTORS.map((connector) => {`.

 447 |         const s = status?.[connector.id];
     | In `SheetConnectors` (src/App.jsx): `s` is assigned `status?.[connector.id];`. Later lines in this function read that name.

 448 |         const isConnected = !!s?.connected;
     | In `SheetConnectors` (src/App.jsx): `isConnected` is assigned `!!s?.connected;`. Later lines in this function read that name.

 449 |         const Icon = connector.icon;
     | In `SheetConnectors` (src/App.jsx): `Icon` is assigned `connector.icon;`. Later lines in this function read that name.

 450 |         return (
     | In `SheetConnectors` (src/App.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

 451 |           <div key={connector.id} className="sheet-connector-row">
     | In `SheetConnectors` (src/App.jsx): Opens it. A box that groups the elements inside it. Source: `<div key={connector.id} className="sheet-connector-row">`

 452 |             <span className="sheet-connector-icon" style={{ color: connector.color, background: connector.color + '18' }}>
     | In `SheetConnectors` (src/App.jsx): Opens it. An inline box. Source: `<span className="sheet-connector-icon" style={{ color: connector.color, background: connector.color + '18' }}>`

 453 |               <Icon />
     | In `SheetConnectors` (src/App.jsx): JSX `<Icon>`. React will create this node when the parent renders. Source: `<Icon />`

 454 |             </span>
     | In `SheetConnectors` (src/App.jsx): Closes it. An inline box. Source: `</span>`

 455 |             <span className="sheet-connector-label">{connector.label}</span>
     | In `SheetConnectors` (src/App.jsx): Opens it. An inline box. Source: `<span className="sheet-connector-label">{connector.label}</span>`

 456 |             <span className={`sheet-connector-dot${isConnected ? ' connected' : ''}`} />
     | In `SheetConnectors` (src/App.jsx): Opens it. An inline box. Source: `<span className={`sheet-connector-dot${isConnected ? ' connected' : ''}`} />`

 457 |             {isConnected ? (
     | In `SheetConnectors` (src/App.jsx): statement `{isConnected ? (`. It runs when SheetConnectors runs, in order, before the next line of the same function.

 458 |               <>
     | In `SheetConnectors` (src/App.jsx): JSX `<element>`. React will create this node when the parent renders. Source: `<>`

 459 |                 <button
     | In `SheetConnectors` (src/App.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button`

 460 |                   className="sheet-connector-btn"
     | In `SheetConnectors` (src/App.jsx): statement `className="sheet-connector-btn"`. It runs when SheetConnectors runs, in order, before the next line of the same function.

 461 |                   onClick={() => handleSync(connector)}
     | In `SheetConnectors` (src/App.jsx): event prop `onClick={() => handleSync(connector)}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 462 |                   disabled={syncing[connector.id]}
     | In `SheetConnectors` (src/App.jsx): `disabled={syncing[connector.id]}` closes {CONNECTORS.map((connector) => { (opened on line 446). Names declared inside that block end here.

 463 |                 >
     | In `SheetConnectors` (src/App.jsx): statement `>`. It runs when SheetConnectors runs, in order, before the next line of the same function.

 464 |                   {syncing[connector.id] ? '…' : 'Sync'}
     | In `SheetConnectors` (src/App.jsx): `{syncing[connector.id] ? '…' : 'Sync'}` closes {CONNECTORS.map((connector) => { (opened on line 446). Names declared inside that block end here.

 465 |                 </button>
     | In `SheetConnectors` (src/App.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

 466 |                 <button
     | In `SheetConnectors` (src/App.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button`

 467 |                   className="sheet-connector-btn sheet-connector-btn--off"
     | In `SheetConnectors` (src/App.jsx): statement `className="sheet-connector-btn sheet-connector-btn--off"`. It runs when SheetConnectors runs, in order, before the next line of the same function.

 468 |                   onClick={() => handleDisconnect(connector)}
     | In `SheetConnectors` (src/App.jsx): event prop `onClick={() => handleDisconnect(connector)}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 469 |                   aria-label={`Disconnect ${connector.label}`}
     | In `SheetConnectors` (src/App.jsx): `aria-label={`Disconnect ${connector.label}`}` closes {CONNECTORS.map((connector) => { (opened on line 446). Names declared inside that block end here.

 470 |                 >
     | In `SheetConnectors` (src/App.jsx): statement `>`. It runs when SheetConnectors runs, in order, before the next line of the same function.

 471 |                   ×
     | In `SheetConnectors` (src/App.jsx): statement `×`. It runs when SheetConnectors runs, in order, before the next line of the same function.

 472 |                 </button>
     | In `SheetConnectors` (src/App.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

 473 |               </>
     | In `SheetConnectors` (src/App.jsx): JSX `<element>`. This closes that element. Source: `</>`

 474 |             ) : (
     | In `SheetConnectors` (src/App.jsx): statement `) : (`. It runs when SheetConnectors runs, in order, before the next line of the same function.

 475 |               <button
     | In `SheetConnectors` (src/App.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button`

 476 |                 className="sheet-connector-btn sheet-connector-btn--on"
     | In `SheetConnectors` (src/App.jsx): statement `className="sheet-connector-btn sheet-connector-btn--on"`. It runs when SheetConnectors runs, in order, before the next line of the same function.

 477 |                 onClick={() => handleConnect(connector)}
     | In `SheetConnectors` (src/App.jsx): event prop `onClick={() => handleConnect(connector)}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 478 |                 disabled={connecting[connector.id]}
     | In `SheetConnectors` (src/App.jsx): `disabled={connecting[connector.id]}` closes {CONNECTORS.map((connector) => { (opened on line 446). Names declared inside that block end here.

 479 |                 style={{ '--c': connector.color }}
     | In `SheetConnectors` (src/App.jsx): `style={{ '--c': connector.color }}` closes {CONNECTORS.map((connector) => { (opened on line 446). Names declared inside that block end here.

 480 |               >
     | In `SheetConnectors` (src/App.jsx): statement `>`. It runs when SheetConnectors runs, in order, before the next line of the same function.

 481 |                 {connecting[connector.id] ? '…' : 'Connect'}
     | In `SheetConnectors` (src/App.jsx): `{connecting[connector.id] ? '…' : 'Connect'}` closes {CONNECTORS.map((connector) => { (opened on line 446). Names declared inside that block end here.

 482 |               </button>
     | In `SheetConnectors` (src/App.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

 483 |             )}
     | In `SheetConnectors` (src/App.jsx): `)}` closes {CONNECTORS.map((connector) => { (opened on line 446). Names declared inside that block end here.

 484 |           </div>
     | In `SheetConnectors` (src/App.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 485 |         );
     | In `SheetConnectors` (src/App.jsx): statement `);`. It runs when SheetConnectors runs, in order, before the next line of the same function.

 486 |       })}
     | In `SheetConnectors` (src/App.jsx): `})}` closes {CONNECTORS.map((connector) => { (opened on line 446). Names declared inside that block end here.

 487 |     </div>
     | In `SheetConnectors` (src/App.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 488 |   );
     | In `SheetConnectors` (src/App.jsx): statement `);`. It runs when SheetConnectors runs, in order, before the next line of the same function.

 489 | }
     | In `SheetConnectors` (src/App.jsx): `}` closes SheetConnectors (opened on line 403). Names declared inside that block end here.

 490 | 
     | Blank line in `src/App.jsx` (the shell: theme, menus, and which page is visible), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

 491 | // Slide-up sheet for secondary nav on mobile
     | Comment inside the top of the file. Not executed. It documents the next code: Slide-up sheet for secondary nav on mobile

 492 | function MoreSheet({ open, onClose, theme, setTheme, onLogout }) {
     | Defines `MoreSheet` in the shell: theme, menus, and which page is visible. The slide-up sheet on small screens: secondary links, SheetConnectors, energy, coffee, theme, logout.

 493 |   return (
     | In `MoreSheet` (src/App.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

 494 |     <>
     | In `MoreSheet` (src/App.jsx): JSX `<element>`. React will create this node when the parent renders. Source: `<>`

 495 |       <div
     | In `MoreSheet` (src/App.jsx): Opens it. A box that groups the elements inside it. Source: `<div`

 496 |         className={`bottom-sheet-overlay${open ? " open" : ""}`}
     | In `MoreSheet` (src/App.jsx): `className={`bottom-sheet-overlay${open ? " open" : ""}`}` closes MoreSheet (opened on line 492). Names declared inside that block end here.

 497 |         onClick={onClose}
     | In `MoreSheet` (src/App.jsx): event prop `onClick={onClose}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 498 |         aria-hidden="true"
     | In `MoreSheet` (src/App.jsx): statement `aria-hidden="true"`. It runs when MoreSheet runs, in order, before the next line of the same function.

 499 |       />
     | In `MoreSheet` (src/App.jsx): statement `/>`. It runs when MoreSheet runs, in order, before the next line of the same function.

 500 |       <div
     | In `MoreSheet` (src/App.jsx): Opens it. A box that groups the elements inside it. Source: `<div`

 501 |         className={`bottom-sheet${open ? " open" : ""}`}
     | In `MoreSheet` (src/App.jsx): `className={`bottom-sheet${open ? " open" : ""}`}` closes MoreSheet (opened on line 492). Names declared inside that block end here.

 502 |         role="dialog"
     | In `MoreSheet` (src/App.jsx): statement `role="dialog"`. It runs when MoreSheet runs, in order, before the next line of the same function.

 503 |         aria-modal="true"
     | In `MoreSheet` (src/App.jsx): statement `aria-modal="true"`. It runs when MoreSheet runs, in order, before the next line of the same function.

 504 |         aria-label="More navigation"
     | In `MoreSheet` (src/App.jsx): statement `aria-label="More navigation"`. It runs when MoreSheet runs, in order, before the next line of the same function.

 505 |       >
     | In `MoreSheet` (src/App.jsx): statement `>`. It runs when MoreSheet runs, in order, before the next line of the same function.

 506 |         <div className="bottom-sheet-handle" aria-hidden="true" />
     | In `MoreSheet` (src/App.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="bottom-sheet-handle" aria-hidden="true" />`

 507 | 
     | Blank line in `src/App.jsx` (the shell: theme, menus, and which page is visible), inside MoreSheet. The parser skips it. It separates the previous statement from the next so the function is readable.

 508 |         <div className="bottom-sheet-section">
     | In `MoreSheet` (src/App.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="bottom-sheet-section">`

 509 |           {SECONDARY_NAV.map(({ to, label, icon: Icon }) => (
     | In `MoreSheet` (src/App.jsx): iteration `{SECONDARY_NAV.map(({ to, label, icon: Icon }) => (`.

 510 |             <NavLink
     | In `MoreSheet` (src/App.jsx): Opens it. A link that knows whether its route is active, so the CSS class 'active' can highlight it. Source: `<NavLink`

 511 |               key={to}
     | In `MoreSheet` (src/App.jsx): `key={to}` closes MoreSheet (opened on line 492). Names declared inside that block end here.

 512 |               to={to}
     | In `MoreSheet` (src/App.jsx): `to={to}` closes MoreSheet (opened on line 492). Names declared inside that block end here.

 513 |               className={({ isActive }) => `nav-item${isActive ? " active" : ""}`}
     | In `MoreSheet` (src/App.jsx): statement `className={({ isActive }) => `nav-item${isActive ? " active" : ""}`}`. It runs when MoreSheet runs, in order, before the next line of the same function.

 514 |               onClick={onClose}
     | In `MoreSheet` (src/App.jsx): event prop `onClick={onClose}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 515 |             >
     | In `MoreSheet` (src/App.jsx): statement `>`. It runs when MoreSheet runs, in order, before the next line of the same function.

 516 |               <Icon />
     | In `MoreSheet` (src/App.jsx): JSX `<Icon>`. React will create this node when the parent renders. Source: `<Icon />`

 517 |               {label}
     | In `MoreSheet` (src/App.jsx): `{label}` closes MoreSheet (opened on line 492). Names declared inside that block end here.

 518 |             </NavLink>
     | In `MoreSheet` (src/App.jsx): Closes it. A link that knows whether its route is active, so the CSS class 'active' can highlight it. Source: `</NavLink>`

 519 |           ))}
     | In `MoreSheet` (src/App.jsx): `))}` closes MoreSheet (opened on line 492). Names declared inside that block end here.

 520 |         </div>
     | In `MoreSheet` (src/App.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 521 | 
     | Blank line in `src/App.jsx` (the shell: theme, menus, and which page is visible), inside MoreSheet. The parser skips it. It separates the previous statement from the next so the function is readable.

 522 |         <div className="bottom-sheet-section">
     | In `MoreSheet` (src/App.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="bottom-sheet-section">`

 523 |           <SheetConnectors open={open} />
     | In `MoreSheet` (src/App.jsx): JSX `<SheetConnectors>`. React will create this node when the parent renders. Source: `<SheetConnectors open={open} />`

 524 |         </div>
     | In `MoreSheet` (src/App.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 525 | 
     | Blank line in `src/App.jsx` (the shell: theme, menus, and which page is visible), inside MoreSheet. The parser skips it. It separates the previous statement from the next so the function is readable.

 526 |         <div className="bottom-sheet-section">
     | In `MoreSheet` (src/App.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="bottom-sheet-section">`

 527 |           <div className="sidebar-section-label">Energy level</div>
     | In `MoreSheet` (src/App.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="sidebar-section-label">Energy level</div>`

 528 |           <div style={{ padding: "4px 0" }}>
     | In `MoreSheet` (src/App.jsx): Opens it. A box that groups the elements inside it. Source: `<div style={{ padding: "4px 0" }}>`

 529 |             <EnergyControl compact />
     | In `MoreSheet` (src/App.jsx): Opens it. The energy faces. compact is the sidebar dots; without it, the big buttons on Today. Source: `<EnergyControl compact />`

 530 |           </div>
     | In `MoreSheet` (src/App.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 531 |         </div>
     | In `MoreSheet` (src/App.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 532 | 
     | Blank line in `src/App.jsx` (the shell: theme, menus, and which page is visible), inside MoreSheet. The parser skips it. It separates the previous statement from the next so the function is readable.

 533 |         <div className="bottom-sheet-footer">
     | In `MoreSheet` (src/App.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="bottom-sheet-footer">`

 534 |           <a
     | In `MoreSheet` (src/App.jsx): Opens it. A normal link. If it has target=_blank it leaves the app. Source: `<a`

 535 |             href={FUNDING_URL}
     | In `MoreSheet` (src/App.jsx): `href={FUNDING_URL}` closes MoreSheet (opened on line 492). Names declared inside that block end here.

 536 |             target="_blank"
     | In `MoreSheet` (src/App.jsx): statement `target="_blank"`. It runs when MoreSheet runs, in order, before the next line of the same function.

 537 |             rel="noopener noreferrer"
     | In `MoreSheet` (src/App.jsx): statement `rel="noopener noreferrer"`. It runs when MoreSheet runs, in order, before the next line of the same function.

 538 |             className="support-btn"
     | In `MoreSheet` (src/App.jsx): statement `className="support-btn"`. It runs when MoreSheet runs, in order, before the next line of the same function.

 539 |             onClick={onClose}
     | In `MoreSheet` (src/App.jsx): event prop `onClick={onClose}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 540 |             aria-label="Buy me a coffee (opens buymeacoffee.com in a new tab)"
     | In `MoreSheet` (src/App.jsx): statement `aria-label="Buy me a coffee (opens buymeacoffee.com in a new tab)"`. It runs when MoreSheet runs, in order, before the next line of the same function.

 541 |           >
     | In `MoreSheet` (src/App.jsx): statement `>`. It runs when MoreSheet runs, in order, before the next line of the same function.

 542 |             <Icons.Coffee />
     | In `MoreSheet` (src/App.jsx): JSX `<Icons.Coffee>`. React will create this node when the parent renders. Source: `<Icons.Coffee />`

 543 |             Buy me a coffee
     | In `MoreSheet` (src/App.jsx): statement `Buy me a coffee`. It runs when MoreSheet runs, in order, before the next line of the same function.

 544 |           </a>
     | In `MoreSheet` (src/App.jsx): Closes it. A normal link. If it has target=_blank it leaves the app. Source: `</a>`

 545 |           <button
     | In `MoreSheet` (src/App.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button`

 546 |             className="theme-toggle"
     | In `MoreSheet` (src/App.jsx): statement `className="theme-toggle"`. It runs when MoreSheet runs, in order, before the next line of the same function.

 547 |             onClick={() => setTheme((t) => (t === "dark" ? "light" : "dark"))}
     | In `MoreSheet` (src/App.jsx): event prop `onClick={() => setTheme((t) => (t === "dark" ? "light" : "dark"))}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 548 |           >
     | In `MoreSheet` (src/App.jsx): statement `>`. It runs when MoreSheet runs, in order, before the next line of the same function.

 549 |             {theme === "dark" ? <Icons.Sun /> : <Icons.Moon />}
     | In `MoreSheet` (src/App.jsx): `{theme === "dark" ? <Icons.Sun /> : <Icons.Moon />}` closes MoreSheet (opened on line 492). Names declared inside that block end here.

 550 |             {theme === "dark" ? "Light mode" : "Dark mode"}
     | In `MoreSheet` (src/App.jsx): `{theme === "dark" ? "Light mode" : "Dark mode"}` closes MoreSheet (opened on line 492). Names declared inside that block end here.

 551 |           </button>
     | In `MoreSheet` (src/App.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

 552 |           <button
     | In `MoreSheet` (src/App.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button`

 553 |             className="logout-btn"
     | In `MoreSheet` (src/App.jsx): statement `className="logout-btn"`. It runs when MoreSheet runs, in order, before the next line of the same function.

 554 |             onClick={() => { onLogout(); onClose(); }}
     | In `MoreSheet` (src/App.jsx): event prop `onClick={() => { onLogout(); onClose(); }}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 555 |           >
     | In `MoreSheet` (src/App.jsx): statement `>`. It runs when MoreSheet runs, in order, before the next line of the same function.

 556 |             <Icons.Logout />
     | In `MoreSheet` (src/App.jsx): JSX `<Icons.Logout>`. React will create this node when the parent renders. Source: `<Icons.Logout />`

 557 |             Logout
     | In `MoreSheet` (src/App.jsx): statement `Logout`. It runs when MoreSheet runs, in order, before the next line of the same function.

 558 |           </button>
     | In `MoreSheet` (src/App.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

 559 |         </div>
     | In `MoreSheet` (src/App.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 560 |       </div>
     | In `MoreSheet` (src/App.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 561 |     </>
     | In `MoreSheet` (src/App.jsx): JSX `<element>`. This closes that element. Source: `</>`

 562 |   );
     | In `MoreSheet` (src/App.jsx): statement `);`. It runs when MoreSheet runs, in order, before the next line of the same function.

 563 | }
     | In `MoreSheet` (src/App.jsx): `}` closes MoreSheet (opened on line 492). Names declared inside that block end here.

 564 | 
     | Blank line in `src/App.jsx` (the shell: theme, menus, and which page is visible), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

 565 | function DevNoticeBanner() {
     | Defines `DevNoticeBanner` in the shell: theme, menus, and which page is visible. Static 'under development' notice. It does not read state. Two text lengths; CSS picks one.

 566 |   return (
     | In `DevNoticeBanner` (src/App.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

 567 |     <div className="dev-banner">
     | In `DevNoticeBanner` (src/App.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="dev-banner">`

 568 |       <div className="dev-banner-main">
     | In `DevNoticeBanner` (src/App.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="dev-banner-main">`

 569 |         <span className="dev-banner-icon" aria-hidden="true">i</span>
     | In `DevNoticeBanner` (src/App.jsx): Opens it. An inline box. Source: `<span className="dev-banner-icon" aria-hidden="true">i</span>`

 570 |         <div className="dev-banner-text">
     | In `DevNoticeBanner` (src/App.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="dev-banner-text">`

 571 |           <span className="dev-banner-text-full">
     | In `DevNoticeBanner` (src/App.jsx): Opens it. An inline box. Source: `<span className="dev-banner-text-full">`

 572 |             <strong>JumpyBrain is currently under development.</strong> Some
     | In `DevNoticeBanner` (src/App.jsx): JSX `<strong>`. React will create this node when the parent renders. Source: `<strong>JumpyBrain is currently under development.</strong> Some`

 573 |             features may not work as expected yet. We're actively improving
     | In `DevNoticeBanner` (src/App.jsx): statement `features may not work as expected yet. We're actively improving`. It runs when DevNoticeBanner runs, in order, before the next line of the same function.

 574 |             the experience, and your feedback helps us make it better.
     | In `DevNoticeBanner` (src/App.jsx): statement `the experience, and your feedback helps us make it better.`. It runs when DevNoticeBanner runs, in order, before the next line of the same function.

 575 |           </span>
     | In `DevNoticeBanner` (src/App.jsx): Closes it. An inline box. Source: `</span>`

 576 |           <span className="dev-banner-text-short">
     | In `DevNoticeBanner` (src/App.jsx): Opens it. An inline box. Source: `<span className="dev-banner-text-short">`

 577 |             <strong>Under development.</strong> Some features may not work
     | In `DevNoticeBanner` (src/App.jsx): JSX `<strong>`. React will create this node when the parent renders. Source: `<strong>Under development.</strong> Some features may not work`

 578 |             yet —{" "}
     | In `DevNoticeBanner` (src/App.jsx): `yet —{" "}` closes DevNoticeBanner (opened on line 565). Names declared inside that block end here.

 579 |             <a
     | In `DevNoticeBanner` (src/App.jsx): Opens it. A normal link. If it has target=_blank it leaves the app. Source: `<a`

 580 |               href={FEEDBACK_URL}
     | In `DevNoticeBanner` (src/App.jsx): `href={FEEDBACK_URL}` closes DevNoticeBanner (opened on line 565). Names declared inside that block end here.

 581 |               target="_blank"
     | In `DevNoticeBanner` (src/App.jsx): statement `target="_blank"`. It runs when DevNoticeBanner runs, in order, before the next line of the same function.

 582 |               rel="noopener noreferrer"
     | In `DevNoticeBanner` (src/App.jsx): statement `rel="noopener noreferrer"`. It runs when DevNoticeBanner runs, in order, before the next line of the same function.

 583 |               className="dev-banner-inline-link"
     | In `DevNoticeBanner` (src/App.jsx): statement `className="dev-banner-inline-link"`. It runs when DevNoticeBanner runs, in order, before the next line of the same function.

 584 |             >
     | In `DevNoticeBanner` (src/App.jsx): statement `>`. It runs when DevNoticeBanner runs, in order, before the next line of the same function.

 585 |               share feedback →
     | In `DevNoticeBanner` (src/App.jsx): statement `share feedback →`. It runs when DevNoticeBanner runs, in order, before the next line of the same function.

 586 |             </a>
     | In `DevNoticeBanner` (src/App.jsx): Closes it. A normal link. If it has target=_blank it leaves the app. Source: `</a>`

 587 |           </span>
     | In `DevNoticeBanner` (src/App.jsx): Closes it. An inline box. Source: `</span>`

 588 |         </div>
     | In `DevNoticeBanner` (src/App.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 589 |       </div>
     | In `DevNoticeBanner` (src/App.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 590 |       <a
     | In `DevNoticeBanner` (src/App.jsx): Opens it. A normal link. If it has target=_blank it leaves the app. Source: `<a`

 591 |         href={FEEDBACK_URL}
     | In `DevNoticeBanner` (src/App.jsx): `href={FEEDBACK_URL}` closes DevNoticeBanner (opened on line 565). Names declared inside that block end here.

 592 |         target="_blank"
     | In `DevNoticeBanner` (src/App.jsx): statement `target="_blank"`. It runs when DevNoticeBanner runs, in order, before the next line of the same function.

 593 |         rel="noopener noreferrer"
     | In `DevNoticeBanner` (src/App.jsx): statement `rel="noopener noreferrer"`. It runs when DevNoticeBanner runs, in order, before the next line of the same function.

 594 |         className="dev-banner-cta"
     | In `DevNoticeBanner` (src/App.jsx): statement `className="dev-banner-cta"`. It runs when DevNoticeBanner runs, in order, before the next line of the same function.

 595 |       >
     | In `DevNoticeBanner` (src/App.jsx): statement `>`. It runs when DevNoticeBanner runs, in order, before the next line of the same function.

 596 |         Share Feedback →
     | In `DevNoticeBanner` (src/App.jsx): statement `Share Feedback →`. It runs when DevNoticeBanner runs, in order, before the next line of the same function.

 597 |       </a>
     | In `DevNoticeBanner` (src/App.jsx): Closes it. A normal link. If it has target=_blank it leaves the app. Source: `</a>`

 598 |     </div>
     | In `DevNoticeBanner` (src/App.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 599 |   );
     | In `DevNoticeBanner` (src/App.jsx): statement `);`. It runs when DevNoticeBanner runs, in order, before the next line of the same function.

 600 | }
     | In `DevNoticeBanner` (src/App.jsx): `}` closes DevNoticeBanner (opened on line 565). Names declared inside that block end here.

 601 | 
     | Blank line in `src/App.jsx` (the shell: theme, menus, and which page is visible), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

 602 | function ProtectedRoute({ children }) {
     | Defines `ProtectedRoute` in the shell: theme, menus, and which page is visible. If UserProvider is still loading, render nothing. If there is no user, render Auth. Otherwise render the page.

 603 |   const { user, loading } = useUser();
     | In `ProtectedRoute` (src/App.jsx): `user`: The logged-in profile object. Null means ProtectedRoute renders Auth. `loading`: True until UserProvider finishes the first localStorage read. ProtectedRoute renders nothing during that moment so Auth does not flash. The code is `const { user, loading } = useUser();`.

 604 |   if (loading) return null;
     | In `ProtectedRoute` (src/App.jsx): branch `if (loading) return null;`. Only one side runs.

 605 |   if (!user) return <Auth />;
     | In `ProtectedRoute` (src/App.jsx): branch `if (!user) return <Auth />;`. Only one side runs.

 606 |   return children;
     | In `ProtectedRoute` (src/App.jsx): return `return children;`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

 607 | }
     | In `ProtectedRoute` (src/App.jsx): `}` closes ProtectedRoute (opened on line 602). Names declared inside that block end here.

 608 | 
     | Blank line in `src/App.jsx` (the shell: theme, menus, and which page is visible), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

 609 | export default function App() {
     | Defines `App` in the shell: theme, menus, and which page is visible. Owns theme, both menus, and the route table. Wraps everything in EnergyProvider. Sidebar, overlay, top bar, banner, bottom nav, and More sheet render only when user is set.

 610 |   const { user, setUser, setToken } = useUser();
     | In `App` (src/App.jsx): `user`: The logged-in profile object. Null means ProtectedRoute renders Auth. The code is `const { user, setUser, setToken } = useUser();`.

 611 |   const [theme, setTheme] = useState(
     | In `App` (src/App.jsx): `theme`: App's dark or light string. Written onto <html data-theme> and localStorage bb-theme. This is not the unused five-palette themeStore. The code is `const [theme, setTheme] = useState(`.

 612 |     () => localStorage.getItem("bb-theme") || "dark"
     | In `App` (src/App.jsx): browser storage — `() => localStorage.getItem("bb-theme") || "dark"`. This survives reloads on this origin and is shared by any script that uses the same key.

 613 |   );
     | In `App` (src/App.jsx): statement `);`. It runs when App runs, in order, before the next line of the same function.

 614 |   const [sidebarOpen, setSidebarOpen] = useState(false);
     | In `App` (src/App.jsx): `sidebarOpen`: Whether the desktop sidebar is slid open. The backdrop and the menu button flip it. It is component state, not uiStore. The code is `const [sidebarOpen, setSidebarOpen] = useState(false);`.

 615 |   const [moreOpen, setMoreOpen] = useState(false);
     | In `App` (src/App.jsx): `moreOpen`: Whether the mobile More sheet is open. The code is `const [moreOpen, setMoreOpen] = useState(false);`.

 616 | 
     | Blank line in `src/App.jsx` (the shell: theme, menus, and which page is visible), inside App. The parser skips it. It separates the previous statement from the next so the function is readable.

 617 |   // Apply theme whenever it changes
     | Comment inside App. Not executed. It documents the next code: Apply theme whenever it changes

 618 |   useEffect(() => {
     | In `App` (src/App.jsx): opens or continues an effect — `useEffect(() => {`. The effect body runs after paint, and its cleanup runs before the next effect and on unmount.

 619 |     document.documentElement.setAttribute("data-theme", theme);
     | In `App` (src/App.jsx): Writes data-theme on <html>. styles.css uses :root[data-theme=light] to swap the color tokens. Dark is the default :root.

 620 |     localStorage.setItem("bb-theme", theme);
     | In `App` (src/App.jsx): browser storage — `localStorage.setItem("bb-theme", theme);`. This survives reloads on this origin and is shared by any script that uses the same key.

 621 |   }, [theme]);
     | In `App` (src/App.jsx): `}, [theme]);` closes effect in App (opened on line 618). Names declared inside that block end here.

 622 | 
     | Blank line in `src/App.jsx` (the shell: theme, menus, and which page is visible), inside App. The parser skips it. It separates the previous statement from the next so the function is readable.

 623 |   // Sync theme from user's saved preference when they log in
     | Comment inside App. Not executed. It documents the next code: Sync theme from user's saved preference when they log in

 624 |   useEffect(() => {
     | In `App` (src/App.jsx): opens or continues an effect — `useEffect(() => {`. The effect body runs after paint, and its cleanup runs before the next effect and on unmount.

 625 |     if (user?.preferredTheme) {
     | In `App` (src/App.jsx): branch `if (user?.preferredTheme) {`. Only one side runs.

 626 |       setTheme(user.preferredTheme);
     | In `App` (src/App.jsx): statement `setTheme(user.preferredTheme);`. It runs when App runs, in order, before the next line of the same function.

 627 |     }
     | In `App` (src/App.jsx): `}` closes if (user?.preferredTheme) { (opened on line 625). Names declared inside that block end here.

 628 |   }, [user?.preferredTheme]);
     | In `App` (src/App.jsx): `}, [user?.preferredTheme]);` closes effect in App (opened on line 624). Names declared inside that block end here.

 629 | 
     | Blank line in `src/App.jsx` (the shell: theme, menus, and which page is visible), inside App. The parser skips it. It separates the previous statement from the next so the function is readable.

 630 |   useEffect(() => {
     | In `App` (src/App.jsx): opens or continues an effect — `useEffect(() => {`. The effect body runs after paint, and its cleanup runs before the next effect and on unmount.

 631 |     if ("Notification" in window && Notification.permission !== "granted") {
     | In `App` (src/App.jsx): branch `if ("Notification" in window && Notification.permission !== "granted") {`. Only one side runs.

 632 |       Notification.requestPermission();
     | In `App` (src/App.jsx): Asks the browser once, on startup, for notification permission. notify() later only works if this was granted.

 633 |     }
     | In `App` (src/App.jsx): `}` closes if ("Notification" in window && Notifica (opened on line 631). Names declared inside that block end here.

 634 |   }, []);
     | In `App` (src/App.jsx): `}, []);` closes effect in App (opened on line 630). Names declared inside that block end here.

 635 | 
     | Blank line in `src/App.jsx` (the shell: theme, menus, and which page is visible), inside App. The parser skips it. It separates the previous statement from the next so the function is readable.

 636 |   function logout() {
     | Defines `logout` in the shell: theme, menus, and which page is visible. Clears user and token through UserProvider (which also clears localStorage and tells the extension). Closes both menus.

 637 |     setUser(null);
     | In `logout` (src/App.jsx): statement `setUser(null);`. It runs when logout runs, in order, before the next line of the same function.

 638 |     setToken(null);
     | In `logout` (src/App.jsx): statement `setToken(null);`. It runs when logout runs, in order, before the next line of the same function.

 639 |     setSidebarOpen(false);
     | In `logout` (src/App.jsx): statement `setSidebarOpen(false);`. It runs when logout runs, in order, before the next line of the same function.

 640 |     setMoreOpen(false);
     | In `logout` (src/App.jsx): statement `setMoreOpen(false);`. It runs when logout runs, in order, before the next line of the same function.

 641 |   }
     | In `logout` (src/App.jsx): `}` closes logout (opened on line 636). Names declared inside that block end here.

 642 | 
     | Blank line in `src/App.jsx` (the shell: theme, menus, and which page is visible), inside App. The parser skips it. It separates the previous statement from the next so the function is readable.

 643 |   return (
     | In `App` (src/App.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

 644 |     <EnergyProvider>
     | In `App` (src/App.jsx): Opens it. Provides useEnergy() to the shell and every page. Source: `<EnergyProvider>`

 645 |       <div className="app-shell">
     | In `App` (src/App.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="app-shell">`

 646 |         {user && (
     | In `App` (src/App.jsx): statement `{user && (`. It runs when App runs, in order, before the next line of the same function.

 647 |           <>
     | In `App` (src/App.jsx): JSX `<element>`. React will create this node when the parent renders. Source: `<>`

 648 |             <Sidebar
     | In `App` (src/App.jsx): Opens it. Left nav. Rendered only when user is set. Source: `<Sidebar`

 649 |               theme={theme}
     | In `App` (src/App.jsx): `theme={theme}` closes App (opened on line 609). Names declared inside that block end here.

 650 |               setTheme={setTheme}
     | In `App` (src/App.jsx): `setTheme={setTheme}` closes App (opened on line 609). Names declared inside that block end here.

 651 |               onLogout={logout}
     | In `App` (src/App.jsx): `onLogout={logout}` closes App (opened on line 609). Names declared inside that block end here.

 652 |               open={sidebarOpen}
     | In `App` (src/App.jsx): `open={sidebarOpen}` closes App (opened on line 609). Names declared inside that block end here.

 653 |               onClose={() => setSidebarOpen(false)}
     | In `App` (src/App.jsx): statement `onClose={() => setSidebarOpen(false)}`. It runs when App runs, in order, before the next line of the same function.

 654 |             />
     | In `App` (src/App.jsx): statement `/>`. It runs when App runs, in order, before the next line of the same function.

 655 |             <FocusOverlay />
     | In `App` (src/App.jsx): Opens it. The tab-leave nudge. Mounted next to the routes, not inside a page, so it stays alive while you move between pages. Source: `<FocusOverlay />`

 656 |           </>
     | In `App` (src/App.jsx): JSX `<element>`. This closes that element. Source: `</>`

 657 |         )}
     | In `App` (src/App.jsx): `)}` closes App (opened on line 609). Names declared inside that block end here.

 658 | 
     | Blank line in `src/App.jsx` (the shell: theme, menus, and which page is visible), inside App. The parser skips it. It separates the previous statement from the next so the function is readable.

 659 |         <div className="main-wrapper">
     | In `App` (src/App.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="main-wrapper">`

 660 |           {user && (
     | In `App` (src/App.jsx): statement `{user && (`. It runs when App runs, in order, before the next line of the same function.

 661 |             <TopBar
     | In `App` (src/App.jsx): Opens it. Header. Rendered only when user is set. Source: `<TopBar`

 662 |               theme={theme}
     | In `App` (src/App.jsx): `theme={theme}` closes App (opened on line 609). Names declared inside that block end here.

 663 |               setTheme={setTheme}
     | In `App` (src/App.jsx): `setTheme={setTheme}` closes App (opened on line 609). Names declared inside that block end here.

 664 |               onMenuClick={() => setSidebarOpen((o) => !o)}
     | In `App` (src/App.jsx): statement `onMenuClick={() => setSidebarOpen((o) => !o)}`. It runs when App runs, in order, before the next line of the same function.

 665 |               onMoreClick={() => setMoreOpen((o) => !o)}
     | In `App` (src/App.jsx): statement `onMoreClick={() => setMoreOpen((o) => !o)}`. It runs when App runs, in order, before the next line of the same function.

 666 |               onLogout={logout}
     | In `App` (src/App.jsx): `onLogout={logout}` closes App (opened on line 609). Names declared inside that block end here.

 667 |             />
     | In `App` (src/App.jsx): statement `/>`. It runs when App runs, in order, before the next line of the same function.

 668 |           )}
     | In `App` (src/App.jsx): `)}` closes App (opened on line 609). Names declared inside that block end here.

 669 | 
     | Blank line in `src/App.jsx` (the shell: theme, menus, and which page is visible), inside App. The parser skips it. It separates the previous statement from the next so the function is readable.

 670 |           <main className="main-content" id="main-content">
     | In `App` (src/App.jsx): Opens it. The page body landmark. Source: `<main className="main-content" id="main-content">`

 671 |             {user && <DevNoticeBanner />}
     | In `App` (src/App.jsx): `{user && <DevNoticeBanner />}` closes App (opened on line 609). Names declared inside that block end here.

 672 |             <Routes>
     | In `App` (src/App.jsx): Opens it. The table of URL to page. Only one Route matches. Source: `<Routes>`

 673 |               <Route path="/auth" element={<Auth />} />
     | In `App` (src/App.jsx): Opens it. One URL. element is what React renders when the path matches. Source: `<Route path="/auth" element={<Auth />} />`

 674 |               <Route path="/" element={<ProtectedRoute><Home /></ProtectedRoute>} />
     | In `App` (src/App.jsx): Opens it. One URL. element is what React renders when the path matches. Source: `<Route path="/" element={<ProtectedRoute><Home /></ProtectedRoute>} />`

 675 |               <Route path="/dashboard" element={<ProtectedRoute><Dashboard /></ProtectedRoute>} />
     | In `App` (src/App.jsx): Opens it. One URL. element is what React renders when the path matches. Source: `<Route path="/dashboard" element={<ProtectedRoute><Dashboard /></ProtectedRoute>} />`

 676 |               <Route path="/focus" element={<ProtectedRoute><FocusTimer /></ProtectedRoute>} />
     | In `App` (src/App.jsx): Opens it. One URL. element is what React renders when the path matches. Source: `<Route path="/focus" element={<ProtectedRoute><FocusTimer /></ProtectedRoute>} />`

 677 |               <Route path="/todo" element={<ProtectedRoute><TodoList /></ProtectedRoute>} />
     | In `App` (src/App.jsx): Opens it. One URL. element is what React renders when the path matches. Source: `<Route path="/todo" element={<ProtectedRoute><TodoList /></ProtectedRoute>} />`

 678 |               <Route path="/mindful" element={<ProtectedRoute><Mindfulness /></ProtectedRoute>} />
     | In `App` (src/App.jsx): Opens it. One URL. element is what React renders when the path matches. Source: `<Route path="/mindful" element={<ProtectedRoute><Mindfulness /></ProtectedRoute>} />`

 679 |               <Route path="/deadline" element={<ProtectedRoute><DeadlineTimer /></ProtectedRoute>} />
     | In `App` (src/App.jsx): Opens it. One URL. element is what React renders when the path matches. Source: `<Route path="/deadline" element={<ProtectedRoute><DeadlineTimer /></ProtectedRoute>} />`

 680 |               <Route path="/calendar" element={<ProtectedRoute><Calendar /></ProtectedRoute>} />
     | In `App` (src/App.jsx): Opens it. One URL. element is what React renders when the path matches. Source: `<Route path="/calendar" element={<ProtectedRoute><Calendar /></ProtectedRoute>} />`

 681 |               <Route path="/connectors" element={<ProtectedRoute><ConnectorsPage /></ProtectedRoute>} />
     | In `App` (src/App.jsx): Opens it. One URL. element is what React renders when the path matches. Source: `<Route path="/connectors" element={<ProtectedRoute><ConnectorsPage /></ProtectedRoute>} />`

 682 |               <Route path="/blocking" element={<ProtectedRoute><FocusShieldPage /></ProtectedRoute>} />
     | In `App` (src/App.jsx): Opens it. One URL. element is what React renders when the path matches. Source: `<Route path="/blocking" element={<ProtectedRoute><FocusShieldPage /></ProtectedRoute>} />`

 683 |               <Route path="/settings" element={<ProtectedRoute><ProfileSettings onThemeChange={setTheme} /></ProtectedRoute>} />
     | In `App` (src/App.jsx): Opens it. One URL. element is what React renders when the path matches. Source: `<Route path="/settings" element={<ProtectedRoute><ProfileSettings onThemeChange={setTheme} /></ProtectedRoute>} />`

 684 |             </Routes>
     | In `App` (src/App.jsx): Closes it. The table of URL to page. Only one Route matches. Source: `</Routes>`

 685 |           </main>
     | In `App` (src/App.jsx): Closes it. The page body landmark. Source: `</main>`

 686 | 
     | Blank line in `src/App.jsx` (the shell: theme, menus, and which page is visible), inside App. The parser skips it. It separates the previous statement from the next so the function is readable.

 687 |           {user && <BottomNav onLogout={logout} />}
     | In `App` (src/App.jsx): `{user && <BottomNav onLogout={logout} />}` closes App (opened on line 609). Names declared inside that block end here.

 688 |         </div>
     | In `App` (src/App.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 689 |         {user && (
     | In `App` (src/App.jsx): statement `{user && (`. It runs when App runs, in order, before the next line of the same function.

 690 |           <MoreSheet
     | In `App` (src/App.jsx): Opens it. Phone 'more' sheet. Rendered only when user is set. Source: `<MoreSheet`

 691 |             open={moreOpen}
     | In `App` (src/App.jsx): `open={moreOpen}` closes App (opened on line 609). Names declared inside that block end here.

 692 |             onClose={() => setMoreOpen(false)}
     | In `App` (src/App.jsx): statement `onClose={() => setMoreOpen(false)}`. It runs when App runs, in order, before the next line of the same function.

 693 |             theme={theme}
     | In `App` (src/App.jsx): `theme={theme}` closes App (opened on line 609). Names declared inside that block end here.

 694 |             setTheme={setTheme}
     | In `App` (src/App.jsx): `setTheme={setTheme}` closes App (opened on line 609). Names declared inside that block end here.

 695 |             onLogout={logout}
     | In `App` (src/App.jsx): `onLogout={logout}` closes App (opened on line 609). Names declared inside that block end here.

 696 |           />
     | In `App` (src/App.jsx): statement `/>`. It runs when App runs, in order, before the next line of the same function.

 697 |         )}
     | In `App` (src/App.jsx): `)}` closes App (opened on line 609). Names declared inside that block end here.

 698 |       </div>
     | In `App` (src/App.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 699 |     </EnergyProvider>
     | In `App` (src/App.jsx): Closes it. Provides useEnergy() to the shell and every page. Source: `</EnergyProvider>`

 700 |   );
     | In `App` (src/App.jsx): statement `);`. It runs when App runs, in order, before the next line of the same function.

 701 | }
     | In `App` (src/App.jsx): `}` closes App (opened on line 609). Names declared inside that block end here.

