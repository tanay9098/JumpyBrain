# `src/components/ConnectorsPage.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import React, { useEffect, useState, useCallback } from 'react';
     | Import for Gmail, Calendar, and Slack connect/sync/disconnect: `import React, { useEffect, useState, useCallback } from 'react';`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   2 | import { useSearchParams } from 'react-router-dom';
     | Import for Gmail, Calendar, and Slack connect/sync/disconnect: `import { useSearchParams } from 'react-router-dom';`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   3 | import api from '../services/api';
     | Import for Gmail, Calendar, and Slack connect/sync/disconnect: `import api from '../services/api';`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   4 | 
     | Blank line in `src/components/ConnectorsPage.jsx` (Gmail, Calendar, and Slack connect/sync/disconnect), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   5 | const CONNECTORS = [
     | In `the top of the file` (src/components/ConnectorsPage.jsx): `CONNECTORS`: Gmail, Slack, and Google Calendar. Each entry knows the OAuth URL path and the sync path the buttons call. The code is `const CONNECTORS = [`.

   6 |   {
     | In `the top of the file` (src/components/ConnectorsPage.jsx): statement `{`. It runs when the top of the file runs, in order, before the next line of the same function.

   7 |     id: 'gmail',
     | In `the top of the file` (src/components/ConnectorsPage.jsx): statement `id: 'gmail',`. It runs when the top of the file runs, in order, before the next line of the same function.

   8 |     label: 'Gmail',
     | In `the top of the file` (src/components/ConnectorsPage.jsx): statement `label: 'Gmail',`. It runs when the top of the file runs, in order, before the next line of the same function.

   9 |     description: 'Import unread emails as tasks automatically',
     | In `the top of the file` (src/components/ConnectorsPage.jsx): statement `description: 'Import unread emails as tasks automatically',`. It runs when the top of the file runs, in order, before the next line of the same function.

  10 |     color: '#ea4335',
     | In `the top of the file` (src/components/ConnectorsPage.jsx): statement `color: '#ea4335',`. It runs when the top of the file runs, in order, before the next line of the same function.

  11 |     urlEndpoint: '/integrations/google/url',
     | In `the top of the file` (src/components/ConnectorsPage.jsx): statement `urlEndpoint: '/integrations/google/url',`. It runs when the top of the file runs, in order, before the next line of the same function.

  12 |     syncEndpoint: '/integrations/gmail/sync',
     | In `the top of the file` (src/components/ConnectorsPage.jsx): statement `syncEndpoint: '/integrations/gmail/sync',`. It runs when the top of the file runs, in order, before the next line of the same function.

  13 |     icon: (
     | In `the top of the file` (src/components/ConnectorsPage.jsx): statement `icon: (`. It runs when the top of the file runs, in order, before the next line of the same function.

  14 |       <svg viewBox="0 0 24 24" fill="currentColor" width="22" height="22">
     | In `the top of the file` (src/components/ConnectorsPage.jsx): Opens it. Vector drawing. It does not fetch data. Source: `<svg viewBox="0 0 24 24" fill="currentColor" width="22" height="22">`

  15 |         <path d="M20 4H4C2.9 4 2 4.9 2 6v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 2-8 5-8-5h16zm0 12H4V8l8 5 8-5v10z" />
     | In `the top of the file` (src/components/ConnectorsPage.jsx): JSX `<path>`. React will create this node when the parent renders. Source: `<path d="M20 4H4C2.9 4 2 4.9 2 6v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 2-8 5-8-5h16zm0 12H4V8l8 5 8-5v10z" />`

  16 |       </svg>
     | In `the top of the file` (src/components/ConnectorsPage.jsx): Closes it. Vector drawing. It does not fetch data. Source: `</svg>`

  17 |     ),
     | In `the top of the file` (src/components/ConnectorsPage.jsx): statement `),`. It runs when the top of the file runs, in order, before the next line of the same function.

  18 |   },
     | In `the top of the file` (src/components/ConnectorsPage.jsx): `},` closes { (opened on line 6). Names declared inside that block end here.

  19 |   {
     | In `the top of the file` (src/components/ConnectorsPage.jsx): statement `{`. It runs when the top of the file runs, in order, before the next line of the same function.

  20 |     id: 'gcal',
     | In `the top of the file` (src/components/ConnectorsPage.jsx): statement `id: 'gcal',`. It runs when the top of the file runs, in order, before the next line of the same function.

  21 |     label: 'Google Calendar',
     | In `the top of the file` (src/components/ConnectorsPage.jsx): statement `label: 'Google Calendar',`. It runs when the top of the file runs, in order, before the next line of the same function.

  22 |     description: 'Sync upcoming events as deadlines',
     | In `the top of the file` (src/components/ConnectorsPage.jsx): statement `description: 'Sync upcoming events as deadlines',`. It runs when the top of the file runs, in order, before the next line of the same function.

  23 |     color: '#1a73e8',
     | In `the top of the file` (src/components/ConnectorsPage.jsx): statement `color: '#1a73e8',`. It runs when the top of the file runs, in order, before the next line of the same function.

  24 |     urlEndpoint: '/integrations/google/url',
     | In `the top of the file` (src/components/ConnectorsPage.jsx): statement `urlEndpoint: '/integrations/google/url',`. It runs when the top of the file runs, in order, before the next line of the same function.

  25 |     syncEndpoint: '/integrations/gcal/sync',
     | In `the top of the file` (src/components/ConnectorsPage.jsx): statement `syncEndpoint: '/integrations/gcal/sync',`. It runs when the top of the file runs, in order, before the next line of the same function.

  26 |     icon: (
     | In `the top of the file` (src/components/ConnectorsPage.jsx): statement `icon: (`. It runs when the top of the file runs, in order, before the next line of the same function.

  27 |       <svg viewBox="0 0 24 24" fill="currentColor" width="22" height="22">
     | In `the top of the file` (src/components/ConnectorsPage.jsx): Opens it. Vector drawing. It does not fetch data. Source: `<svg viewBox="0 0 24 24" fill="currentColor" width="22" height="22">`

  28 |         <path d="M19 3h-1V1h-2v2H8V1H6v2H5C3.9 3 3 3.9 3 5v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V8h14v11zM7 10h5v5H7z" />
     | In `the top of the file` (src/components/ConnectorsPage.jsx): JSX `<path>`. React will create this node when the parent renders. Source: `<path d="M19 3h-1V1h-2v2H8V1H6v2H5C3.9 3 3 3.9 3 5v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V8h14v11zM7 10h5v5H7z" />`

  29 |       </svg>
     | In `the top of the file` (src/components/ConnectorsPage.jsx): Closes it. Vector drawing. It does not fetch data. Source: `</svg>`

  30 |     ),
     | In `the top of the file` (src/components/ConnectorsPage.jsx): statement `),`. It runs when the top of the file runs, in order, before the next line of the same function.

  31 |   },
     | In `the top of the file` (src/components/ConnectorsPage.jsx): `},` closes { (opened on line 19). Names declared inside that block end here.

  32 |   {
     | In `the top of the file` (src/components/ConnectorsPage.jsx): statement `{`. It runs when the top of the file runs, in order, before the next line of the same function.

  33 |     id: 'slack',
     | In `the top of the file` (src/components/ConnectorsPage.jsx): statement `id: 'slack',`. It runs when the top of the file runs, in order, before the next line of the same function.

  34 |     label: 'Slack',
     | In `the top of the file` (src/components/ConnectorsPage.jsx): statement `label: 'Slack',`. It runs when the top of the file runs, in order, before the next line of the same function.

  35 |     description: 'Turn starred Slack messages into tasks',
     | In `the top of the file` (src/components/ConnectorsPage.jsx): statement `description: 'Turn starred Slack messages into tasks',`. It runs when the top of the file runs, in order, before the next line of the same function.

  36 |     color: '#611f69',
     | In `the top of the file` (src/components/ConnectorsPage.jsx): statement `color: '#611f69',`. It runs when the top of the file runs, in order, before the next line of the same function.

  37 |     urlEndpoint: '/integrations/slack/url',
     | In `the top of the file` (src/components/ConnectorsPage.jsx): statement `urlEndpoint: '/integrations/slack/url',`. It runs when the top of the file runs, in order, before the next line of the same function.

  38 |     syncEndpoint: '/integrations/slack/sync',
     | In `the top of the file` (src/components/ConnectorsPage.jsx): statement `syncEndpoint: '/integrations/slack/sync',`. It runs when the top of the file runs, in order, before the next line of the same function.

  39 |     icon: (
     | In `the top of the file` (src/components/ConnectorsPage.jsx): statement `icon: (`. It runs when the top of the file runs, in order, before the next line of the same function.

  40 |       <svg viewBox="0 0 24 24" fill="currentColor" width="22" height="22">
     | In `the top of the file` (src/components/ConnectorsPage.jsx): Opens it. Vector drawing. It does not fetch data. Source: `<svg viewBox="0 0 24 24" fill="currentColor" width="22" height="22">`

  41 |         <path d="M5.042 15.165a2.528 2.528 0 01-2.52 2.523A2.528 2.528 0 010 15.165a2.527 2.527 0 012.522-2.52h2.52v2.52zM6.313 15.165a2.527 2.527 0 012.521-2.52 2.527 2.527 0 012.521 2.52v6.313A2.528 2.528 0 018.834 24a2.528 2.528 0 01-2.521-2.522v-6.313zM8.834 5.042a2.528 2.528 0 01-2.521-2.52A2.528 2.528 0 018.834 0a2.528 2.528 0 012.521 2.522v2.52H8.834zM8.834 6.313a2.528 2.528 0 012.521 2.521 2.528 2.528 0 01-2.521 2.521H2.522A2.528 2.528 0 010 8.834a2.528 2.528 0 012.522-2.521h6.312zM18.956 8.834a2.528 2.528 0 012.522-2.521A2.528 2.528 0 0124 8.834a2.528 2.528 0 01-2.522 2.521h-2.522V8.834zM17.688 8.834a2.528 2.528 0 01-2.523 2.521 2.527 2.527 0 01-2.52-2.521V2.522A2.527 2.527 0 0115.165 0a2.528 2.528 0 012.523 2.522v6.312zM15.165 18.956a2.528 2.528 0 012.523 2.522A2.528 2.528 0 0115.165 24a2.527 2.527 0 01-2.52-2.522v-2.522h2.52zM15.165 17.688a2.527 2.527 0 01-2.52-2.523 2.526 2.526 0 012.52-2.52h6.313A2.527 2.527 0 0124 15.165a2.528 2.528 0 01-2.522 2.523h-6.313z" />
     | In `the top of the file` (src/components/ConnectorsPage.jsx): JSX `<path>`. React will create this node when the parent renders. Source: `<path d="M5.042 15.165a2.528 2.528 0 01-2.52 2.523A2.528 2.528 0 010 15.165a2.527 2.527 0 012.522-2.52h2.52v2.52zM6.313 15.165a2.527 2.527 0 012.521-2.52 2.527 2.527 0 012.521 2.52v6.313A2.528 2.528 0`

  42 |       </svg>
     | In `the top of the file` (src/components/ConnectorsPage.jsx): Closes it. Vector drawing. It does not fetch data. Source: `</svg>`

  43 |     ),
     | In `the top of the file` (src/components/ConnectorsPage.jsx): statement `),`. It runs when the top of the file runs, in order, before the next line of the same function.

  44 |   },
     | In `the top of the file` (src/components/ConnectorsPage.jsx): `},` closes { (opened on line 32). Names declared inside that block end here.

  45 | ];
     | In `the top of the file` (src/components/ConnectorsPage.jsx): statement `];`. It runs when the top of the file runs, in order, before the next line of the same function.

  46 | 
     | Blank line in `src/components/ConnectorsPage.jsx` (Gmail, Calendar, and Slack connect/sync/disconnect), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  47 | function fmtDate(iso) {
     | Defines `fmtDate` in Gmail, Calendar, and Slack connect/sync/disconnect. Short local date-time for 'last synced'.

  48 |   if (!iso) return null;
     | In `fmtDate` (src/components/ConnectorsPage.jsx): branch `if (!iso) return null;`. Only one side runs.

  49 |   return new Date(iso).toLocaleDateString(undefined, { month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' });
     | In `fmtDate` (src/components/ConnectorsPage.jsx): return `return new Date(iso).toLocaleDateString(undefined, { month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' });`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  50 | }
     | In `fmtDate` (src/components/ConnectorsPage.jsx): `}` closes fmtDate (opened on line 47). Names declared inside that block end here.

  51 | 
     | Blank line in `src/components/ConnectorsPage.jsx` (Gmail, Calendar, and Slack connect/sync/disconnect), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  52 | export default function ConnectorsPage() {
     | Defines `ConnectorsPage` in Gmail, Calendar, and Slack connect/sync/disconnect. Full-page version of the three connectors, plus toasts and the OAuth return query string.

  53 |   const [status, setStatus] = useState(null);
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): React state `status, setStatus`. The value survives re-renders. Calling the setter re-renders this component. `const [status, setStatus] = useState(null);`

  54 |   const [syncing, setSyncing] = useState({});
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): React state `syncing, setSyncing`. The value survives re-renders. Calling the setter re-renders this component. `const [syncing, setSyncing] = useState({});`

  55 |   const [connecting, setConnecting] = useState({});
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): React state `connecting, setConnecting`. The value survives re-renders. Calling the setter re-renders this component. `const [connecting, setConnecting] = useState({});`

  56 |   const [toast, setToast] = useState(null);
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): React state `toast, setToast`. The value survives re-renders. Calling the setter re-renders this component. `const [toast, setToast] = useState(null);`

  57 |   const [searchParams, setSearchParams] = useSearchParams();
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): `searchParams, setSearchParams` is assigned `useSearchParams();`. Later lines in this function read that name.

  58 | 
     | Blank line in `src/components/ConnectorsPage.jsx` (Gmail, Calendar, and Slack connect/sync/disconnect), inside ConnectorsPage. The parser skips it. It separates the previous statement from the next so the function is readable.

  59 |   const loadStatus = useCallback(async () => {
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): A memoized function `loadStatus`. `const loadStatus = useCallback(async () => {`

  60 |     try {
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): error path `try {`.

  61 |       const data = await api.get('/integrations/status');
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): `data` is assigned `await api.get('/integrations/status');`. Later lines in this function read that name.

  62 |       setStatus(data);
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): statement `setStatus(data);`. It runs when ConnectorsPage runs, in order, before the next line of the same function.

  63 |     } catch {
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): `} catch {` closes try { (opened on line 60). Names declared inside that block end here.

  64 |       // ignore
     | Comment inside ConnectorsPage. Not executed. It documents the next code: ignore

  65 |     }
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): `}` closes } catch { (opened on line 63). Names declared inside that block end here.

  66 |   }, []);
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): `}, []);` closes const loadStatus = useCallback(async () => { (opened on line 59). Names declared inside that block end here.

  67 | 
     | Blank line in `src/components/ConnectorsPage.jsx` (Gmail, Calendar, and Slack connect/sync/disconnect), inside ConnectorsPage. The parser skips it. It separates the previous statement from the next so the function is readable.

  68 |   useEffect(() => {
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): opens or continues an effect — `useEffect(() => {`. The effect body runs after paint, and its cleanup runs before the next effect and on unmount.

  69 |     loadStatus();
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): statement `loadStatus();`. It runs when ConnectorsPage runs, in order, before the next line of the same function.

  70 |   }, [loadStatus]);
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): `}, [loadStatus]);` closes effect in ConnectorsPage (opened on line 68). Names declared inside that block end here.

  71 | 
     | Blank line in `src/components/ConnectorsPage.jsx` (Gmail, Calendar, and Slack connect/sync/disconnect), inside ConnectorsPage. The parser skips it. It separates the previous statement from the next so the function is readable.

  72 |   // Handle redirect back from OAuth
     | Comment inside ConnectorsPage. Not executed. It documents the next code: Handle redirect back from OAuth

  73 |   useEffect(() => {
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): opens or continues an effect — `useEffect(() => {`. The effect body runs after paint, and its cleanup runs before the next effect and on unmount.

  74 |     const connected = searchParams.get('connected');
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): `connected` is assigned `searchParams.get('connected');`. Later lines in this function read that name.

  75 |     const error = searchParams.get('error');
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): `error` is assigned `searchParams.get('error');`. Later lines in this function read that name.

  76 | 
     | Blank line in `src/components/ConnectorsPage.jsx` (Gmail, Calendar, and Slack connect/sync/disconnect), inside ConnectorsPage. The parser skips it. It separates the previous statement from the next so the function is readable.

  77 |     if (connected) {
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): branch `if (connected) {`. Only one side runs.

  78 |       showToast(`${connected === 'google' ? 'Gmail & Google Calendar' : 'Slack'} connected!`, 'success');
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): `showToast(`${connected === 'google' ? 'Gmail & Google Calendar' : 'Slack'} connected!`, 'success');` closes if (connected) { (opened on line 77). Names declared inside that block end here.

  79 |       setSearchParams({});
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): `setSearchParams({});` closes if (connected) { (opened on line 77). Names declared inside that block end here.

  80 |       loadStatus();
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): statement `loadStatus();`. It runs when ConnectorsPage runs, in order, before the next line of the same function.

  81 |     } else if (error) {
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): branch `} else if (error) {`. Only one side runs.

  82 |       showToast('Connection failed. Please try again.', 'error');
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): statement `showToast('Connection failed. Please try again.', 'error');`. It runs when ConnectorsPage runs, in order, before the next line of the same function.

  83 |       setSearchParams({});
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): `setSearchParams({});` closes } else if (error) { (opened on line 81). Names declared inside that block end here.

  84 |     }
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): `}` closes } else if (error) { (opened on line 81). Names declared inside that block end here.

  85 |   }, [searchParams, setSearchParams, loadStatus]);
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): `}, [searchParams, setSearchParams, loadStatus]);` closes effect in ConnectorsPage (opened on line 73). Names declared inside that block end here.

  86 | 
     | Blank line in `src/components/ConnectorsPage.jsx` (Gmail, Calendar, and Slack connect/sync/disconnect), inside ConnectorsPage. The parser skips it. It separates the previous statement from the next so the function is readable.

  87 |   function showToast(message, type = 'success') {
     | Defines `showToast` in Gmail, Calendar, and Slack connect/sync/disconnect. Sets toast state and clears it after 4 seconds.

  88 |     setToast({ message, type });
     | In `showToast` (src/components/ConnectorsPage.jsx): `setToast({ message, type });` closes showToast (opened on line 87). Names declared inside that block end here.

  89 |     setTimeout(() => setToast(null), 4000);
     | In `showToast` (src/components/ConnectorsPage.jsx): timer — `setTimeout(() => setToast(null), 4000);`. The callback runs later on the event loop, not now.

  90 |   }
     | In `showToast` (src/components/ConnectorsPage.jsx): `}` closes showToast (opened on line 87). Names declared inside that block end here.

  91 | 
     | Blank line in `src/components/ConnectorsPage.jsx` (Gmail, Calendar, and Slack connect/sync/disconnect), inside ConnectorsPage. The parser skips it. It separates the previous statement from the next so the function is readable.

  92 |   async function handleConnect(connector) {
     | Defines `handleConnect` in Gmail, Calendar, and Slack connect/sync/disconnect. GET the connector's urlEndpoint and set window.location to that OAuth URL.

  93 |     setConnecting(p => ({ ...p, [connector.id]: true }));
     | In `handleConnect` (src/components/ConnectorsPage.jsx): statement `setConnecting(p => ({ ...p, [connector.id]: true }));`. It runs when handleConnect runs, in order, before the next line of the same function.

  94 |     try {
     | In `handleConnect` (src/components/ConnectorsPage.jsx): error path `try {`.

  95 |       const { url } = await api.get(connector.urlEndpoint);
     | In `handleConnect` (src/components/ConnectorsPage.jsx): `url` is assigned `await api.get(connector.urlEndpoint);`. Later lines in this function read that name.

  96 |       window.location.href = url;
     | In `handleConnect` (src/components/ConnectorsPage.jsx): statement `window.location.href = url;`. It runs when handleConnect runs, in order, before the next line of the same function.

  97 |     } catch {
     | In `handleConnect` (src/components/ConnectorsPage.jsx): `} catch {` closes try { (opened on line 94). Names declared inside that block end here.

  98 |       showToast('Connection unavailable. Please try again later.', 'error');
     | In `handleConnect` (src/components/ConnectorsPage.jsx): statement `showToast('Connection unavailable. Please try again later.', 'error');`. It runs when handleConnect runs, in order, before the next line of the same function.

  99 |       setConnecting(p => ({ ...p, [connector.id]: false }));
     | In `handleConnect` (src/components/ConnectorsPage.jsx): statement `setConnecting(p => ({ ...p, [connector.id]: false }));`. It runs when handleConnect runs, in order, before the next line of the same function.

 100 |     }
     | In `handleConnect` (src/components/ConnectorsPage.jsx): `}` closes } catch { (opened on line 97). Names declared inside that block end here.

 101 |   }
     | In `handleConnect` (src/components/ConnectorsPage.jsx): `}` closes handleConnect (opened on line 92). Names declared inside that block end here.

 102 | 
     | Blank line in `src/components/ConnectorsPage.jsx` (Gmail, Calendar, and Slack connect/sync/disconnect), inside ConnectorsPage. The parser skips it. It separates the previous statement from the next so the function is readable.

 103 |   async function handleSync(connector) {
     | Defines `handleSync` in Gmail, Calendar, and Slack connect/sync/disconnect. POST the sync endpoint. The page toast includes result.synced and result.created.

 104 |     setSyncing(p => ({ ...p, [connector.id]: true }));
     | In `handleSync` (src/components/ConnectorsPage.jsx): statement `setSyncing(p => ({ ...p, [connector.id]: true }));`. It runs when handleSync runs, in order, before the next line of the same function.

 105 |     try {
     | In `handleSync` (src/components/ConnectorsPage.jsx): error path `try {`.

 106 |       const result = await api.post(connector.syncEndpoint);
     | In `handleSync` (src/components/ConnectorsPage.jsx): `result` is assigned `await api.post(connector.syncEndpoint);`. Later lines in this function read that name.

 107 |       showToast(`Synced ${result.synced} items, created ${result.created} new tasks.`, 'success');
     | In `handleSync` (src/components/ConnectorsPage.jsx): `showToast(`Synced ${result.synced} items, created ${result.created} new tasks.`, 'success');` closes try { (opened on line 105). Names declared inside that block end here.

 108 |       loadStatus();
     | In `handleSync` (src/components/ConnectorsPage.jsx): statement `loadStatus();`. It runs when handleSync runs, in order, before the next line of the same function.

 109 |     } catch (err) {
     | In `handleSync` (src/components/ConnectorsPage.jsx): `} catch (err) {` closes try { (opened on line 105). Names declared inside that block end here.

 110 |       const msg = err.response?.data?.error || 'Sync failed.';
     | In `handleSync` (src/components/ConnectorsPage.jsx): `msg` is assigned `err.response?.data?.error || 'Sync failed.';`. Later lines in this function read that name.

 111 |       showToast(msg, 'error');
     | In `handleSync` (src/components/ConnectorsPage.jsx): statement `showToast(msg, 'error');`. It runs when handleSync runs, in order, before the next line of the same function.

 112 |     } finally {
     | In `handleSync` (src/components/ConnectorsPage.jsx): `} finally {` closes } catch (err) { (opened on line 109). Names declared inside that block end here.

 113 |       setSyncing(p => ({ ...p, [connector.id]: false }));
     | In `handleSync` (src/components/ConnectorsPage.jsx): statement `setSyncing(p => ({ ...p, [connector.id]: false }));`. It runs when handleSync runs, in order, before the next line of the same function.

 114 |     }
     | In `handleSync` (src/components/ConnectorsPage.jsx): `}` closes } finally { (opened on line 112). Names declared inside that block end here.

 115 |   }
     | In `handleSync` (src/components/ConnectorsPage.jsx): `}` closes handleSync (opened on line 103). Names declared inside that block end here.

 116 | 
     | Blank line in `src/components/ConnectorsPage.jsx` (Gmail, Calendar, and Slack connect/sync/disconnect), inside ConnectorsPage. The parser skips it. It separates the previous statement from the next so the function is readable.

 117 |   async function handleDisconnect(connector) {
     | Defines `handleDisconnect` in Gmail, Calendar, and Slack connect/sync/disconnect. DELETE /integrations/:id and refresh status.

 118 |     try {
     | In `handleDisconnect` (src/components/ConnectorsPage.jsx): error path `try {`.

 119 |       await api.delete(`/integrations/${connector.id}`);
     | In `handleDisconnect` (src/components/ConnectorsPage.jsx): HTTP via the shared Axios instance — `await api.delete(`/integrations/${connector.id}`);`. The request interceptor adds `Authorization: Bearer <accessToken>`. The response interceptor returns `res.data`, so the awaited value is the JSON body.

 120 |       showToast(`${connector.label} disconnected.`, 'success');
     | In `handleDisconnect` (src/components/ConnectorsPage.jsx): `showToast(`${connector.label} disconnected.`, 'success');` closes try { (opened on line 118). Names declared inside that block end here.

 121 |       loadStatus();
     | In `handleDisconnect` (src/components/ConnectorsPage.jsx): statement `loadStatus();`. It runs when handleDisconnect runs, in order, before the next line of the same function.

 122 |     } catch {
     | In `handleDisconnect` (src/components/ConnectorsPage.jsx): `} catch {` closes try { (opened on line 118). Names declared inside that block end here.

 123 |       showToast('Failed to disconnect.', 'error');
     | In `handleDisconnect` (src/components/ConnectorsPage.jsx): statement `showToast('Failed to disconnect.', 'error');`. It runs when handleDisconnect runs, in order, before the next line of the same function.

 124 |     }
     | In `handleDisconnect` (src/components/ConnectorsPage.jsx): `}` closes } catch { (opened on line 122). Names declared inside that block end here.

 125 |   }
     | In `handleDisconnect` (src/components/ConnectorsPage.jsx): `}` closes handleDisconnect (opened on line 117). Names declared inside that block end here.

 126 | 
     | Blank line in `src/components/ConnectorsPage.jsx` (Gmail, Calendar, and Slack connect/sync/disconnect), inside ConnectorsPage. The parser skips it. It separates the previous statement from the next so the function is readable.

 127 |   return (
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

 128 |     <div className="connectors-page">
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="connectors-page">`

 129 |       {toast && (
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): statement `{toast && (`. It runs when ConnectorsPage runs, in order, before the next line of the same function.

 130 |         <div className={`connectors-toast connectors-toast--${toast.type}`}>
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): Opens it. A box that groups the elements inside it. Source: `<div className={`connectors-toast connectors-toast--${toast.type}`}>`

 131 |           {toast.message}
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): `{toast.message}` closes ConnectorsPage (opened on line 52). Names declared inside that block end here.

 132 |         </div>
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 133 |       )}
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): `)}` closes ConnectorsPage (opened on line 52). Names declared inside that block end here.

 134 | 
     | Blank line in `src/components/ConnectorsPage.jsx` (Gmail, Calendar, and Slack connect/sync/disconnect), inside ConnectorsPage. The parser skips it. It separates the previous statement from the next so the function is readable.

 135 |       <div className="page-header">
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="page-header">`

 136 |         <h1 className="page-title">Connectors</h1>
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): Opens it. The page title. Source: `<h1 className="page-title">Connectors</h1>`

 137 |         <p className="page-subtitle">
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): Opens it. A paragraph. Source: `<p className="page-subtitle">`

 138 |           Link your tools to automatically pull emails, events, and messages as tasks.
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): statement `Link your tools to automatically pull emails, events, and messages as tasks.`. It runs when ConnectorsPage runs, in order, before the next line of the same function.

 139 |         </p>
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): Closes it. A paragraph. Source: `</p>`

 140 |       </div>
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 141 | 
     | Blank line in `src/components/ConnectorsPage.jsx` (Gmail, Calendar, and Slack connect/sync/disconnect), inside ConnectorsPage. The parser skips it. It separates the previous statement from the next so the function is readable.

 142 |       <div className="connectors-list">
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="connectors-list">`

 143 |         {CONNECTORS.map((connector) => {
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): iteration `{CONNECTORS.map((connector) => {`.

 144 |           const s = status?.[connector.id];
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): `s` is assigned `status?.[connector.id];`. Later lines in this function read that name.

 145 |           const isConnected = !!s?.connected;
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): `isConnected` is assigned `!!s?.connected;`. Later lines in this function read that name.

 146 | 
     | Blank line in `src/components/ConnectorsPage.jsx` (Gmail, Calendar, and Slack connect/sync/disconnect), inside ConnectorsPage. The parser skips it. It separates the previous statement from the next so the function is readable.

 147 |           return (
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

 148 |             <div key={connector.id} className="connector-card">
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): Opens it. A box that groups the elements inside it. Source: `<div key={connector.id} className="connector-card">`

 149 |               <div className="connector-card-icon" style={{ color: connector.color, background: connector.color + '18' }}>
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="connector-card-icon" style={{ color: connector.color, background: connector.color + '18' }}>`

 150 |                 {connector.icon}
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): `{connector.icon}` closes {CONNECTORS.map((connector) => { (opened on line 143). Names declared inside that block end here.

 151 |               </div>
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 152 | 
     | Blank line in `src/components/ConnectorsPage.jsx` (Gmail, Calendar, and Slack connect/sync/disconnect), inside ConnectorsPage. The parser skips it. It separates the previous statement from the next so the function is readable.

 153 |               <div className="connector-card-body">
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="connector-card-body">`

 154 |                 <div className="connector-card-title">{connector.label}</div>
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="connector-card-title">{connector.label}</div>`

 155 |                 <div className="connector-card-desc">{connector.description}</div>
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="connector-card-desc">{connector.description}</div>`

 156 |                 {isConnected && s.lastSyncedAt && (
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): statement `{isConnected && s.lastSyncedAt && (`. It runs when ConnectorsPage runs, in order, before the next line of the same function.

 157 |                   <div className="connector-card-meta">Last synced {fmtDate(s.lastSyncedAt)}</div>
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="connector-card-meta">Last synced {fmtDate(s.lastSyncedAt)}</div>`

 158 |                 )}
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): `)}` closes {CONNECTORS.map((connector) => { (opened on line 143). Names declared inside that block end here.

 159 |                 {isConnected && !s.lastSyncedAt && (
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): statement `{isConnected && !s.lastSyncedAt && (`. It runs when ConnectorsPage runs, in order, before the next line of the same function.

 160 |                   <div className="connector-card-meta">Connected {fmtDate(s.connectedAt)} · Never synced</div>
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="connector-card-meta">Connected {fmtDate(s.connectedAt)} · Never synced</div>`

 161 |                 )}
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): `)}` closes {CONNECTORS.map((connector) => { (opened on line 143). Names declared inside that block end here.

 162 |               </div>
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 163 | 
     | Blank line in `src/components/ConnectorsPage.jsx` (Gmail, Calendar, and Slack connect/sync/disconnect), inside ConnectorsPage. The parser skips it. It separates the previous statement from the next so the function is readable.

 164 |               <div className="connector-card-actions">
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="connector-card-actions">`

 165 |                 {isConnected ? (
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): statement `{isConnected ? (`. It runs when ConnectorsPage runs, in order, before the next line of the same function.

 166 |                   <>
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): JSX `<element>`. React will create this node when the parent renders. Source: `<>`

 167 |                     <button
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button`

 168 |                       className="btn-connector btn-connector-sync"
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): statement `className="btn-connector btn-connector-sync"`. It runs when ConnectorsPage runs, in order, before the next line of the same function.

 169 |                       onClick={() => handleSync(connector)}
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): event prop `onClick={() => handleSync(connector)}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 170 |                       disabled={syncing[connector.id]}
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): `disabled={syncing[connector.id]}` closes {CONNECTORS.map((connector) => { (opened on line 143). Names declared inside that block end here.

 171 |                     >
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): statement `>`. It runs when ConnectorsPage runs, in order, before the next line of the same function.

 172 |                       {syncing[connector.id] ? 'Syncing…' : 'Sync now'}
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): `{syncing[connector.id] ? 'Syncing…' : 'Sync now'}` closes {CONNECTORS.map((connector) => { (opened on line 143). Names declared inside that block end here.

 173 |                     </button>
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

 174 |                     <button
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button`

 175 |                       className="btn-connector btn-connector-disconnect"
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): statement `className="btn-connector btn-connector-disconnect"`. It runs when ConnectorsPage runs, in order, before the next line of the same function.

 176 |                       onClick={() => handleDisconnect(connector)}
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): event prop `onClick={() => handleDisconnect(connector)}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 177 |                     >
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): statement `>`. It runs when ConnectorsPage runs, in order, before the next line of the same function.

 178 |                       Disconnect
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): statement `Disconnect`. It runs when ConnectorsPage runs, in order, before the next line of the same function.

 179 |                     </button>
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

 180 |                   </>
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): JSX `<element>`. This closes that element. Source: `</>`

 181 |                 ) : (
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): statement `) : (`. It runs when ConnectorsPage runs, in order, before the next line of the same function.

 182 |                   <button
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button`

 183 |                     className="btn-connector btn-connector-connect"
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): statement `className="btn-connector btn-connector-connect"`. It runs when ConnectorsPage runs, in order, before the next line of the same function.

 184 |                     onClick={() => handleConnect(connector)}
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): event prop `onClick={() => handleConnect(connector)}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 185 |                     disabled={connecting[connector.id]}
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): `disabled={connecting[connector.id]}` closes {CONNECTORS.map((connector) => { (opened on line 143). Names declared inside that block end here.

 186 |                     style={{ '--accent': connector.color }}
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): `style={{ '--accent': connector.color }}` closes {CONNECTORS.map((connector) => { (opened on line 143). Names declared inside that block end here.

 187 |                   >
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): statement `>`. It runs when ConnectorsPage runs, in order, before the next line of the same function.

 188 |                     {connecting[connector.id] ? 'Redirecting…' : 'Connect'}
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): `{connecting[connector.id] ? 'Redirecting…' : 'Connect'}` closes {CONNECTORS.map((connector) => { (opened on line 143). Names declared inside that block end here.

 189 |                   </button>
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

 190 |                 )}
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): `)}` closes {CONNECTORS.map((connector) => { (opened on line 143). Names declared inside that block end here.

 191 |               </div>
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 192 |             </div>
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 193 |           );
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): statement `);`. It runs when ConnectorsPage runs, in order, before the next line of the same function.

 194 |         })}
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): `})}` closes {CONNECTORS.map((connector) => { (opened on line 143). Names declared inside that block end here.

 195 |       </div>
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 196 | 
     | Blank line in `src/components/ConnectorsPage.jsx` (Gmail, Calendar, and Slack connect/sync/disconnect), inside ConnectorsPage. The parser skips it. It separates the previous statement from the next so the function is readable.

 197 |     </div>
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 198 |   );
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): statement `);`. It runs when ConnectorsPage runs, in order, before the next line of the same function.

 199 | }
     | In `ConnectorsPage` (src/components/ConnectorsPage.jsx): `}` closes ConnectorsPage (opened on line 52). Names declared inside that block end here.

