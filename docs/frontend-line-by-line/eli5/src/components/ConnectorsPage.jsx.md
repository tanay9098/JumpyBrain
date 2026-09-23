# `src/components/ConnectorsPage.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import React, { useEffect, useState, useCallback } from 'react';
     | Borrows React so this file can remember things and draw the screen.

   2 | import { useSearchParams } from 'react-router-dom';
     | Borrows React so this file can remember things and draw the screen.

   3 | import api from '../services/api';
     | This file borrows a tool another file already made.

   4 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   5 | const CONNECTORS = [
     | Gmail, Slack, and Google Calendar. Each entry knows the OAuth URL path and the sync path the buttons call.

   6 |   {
     | Inside the top of the file, this line runs as written: {. It happens in order, after the line above it and before the line below it.

   7 |     id: 'gmail',
     | Inside the top of the file, this line runs as written: id: 'gmail',. It happens in order, after the line above it and before the line below it.

   8 |     label: 'Gmail',
     | Inside the top of the file, this line runs as written: label: 'Gmail',. It happens in order, after the line above it and before the line below it.

   9 |     description: 'Import unread emails as tasks automatically',
     | Inside the top of the file, this line runs as written: description: 'Import unread emails as tasks automatically',. It happens in order, after the line above it and before the line below it.

  10 |     color: '#ea4335',
     | Inside the top of the file, this line runs as written: color: '#ea4335',. It happens in order, after the line above it and before the line below it.

  11 |     urlEndpoint: '/integrations/google/url',
     | Inside the top of the file, this line runs as written: urlEndpoint: '/integrations/google/url',. It happens in order, after the line above it and before the line below it.

  12 |     syncEndpoint: '/integrations/gmail/sync',
     | Inside the top of the file, this line runs as written: syncEndpoint: '/integrations/gmail/sync',. It happens in order, after the line above it and before the line below it.

  13 |     icon: (
     | Inside the top of the file, this line runs as written: icon: (. It happens in order, after the line above it and before the line below it.

  14 |       <svg viewBox="0 0 24 24" fill="currentColor" width="22" height="22">
     | This draws one piece of the page while the top of the file is showing.

  15 |         <path d="M20 4H4C2.9 4 2 4.9 2 6v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 2-8 5-8-5h16zm0 12H4V8l8 5 8-5v10z" />
     | This draws one piece of the page while the top of the file is showing.

  16 |       </svg>
     | This ends a drawing that the top of the file started just above.

  17 |     ),
     | This closes a box of instructions that opened above.

  18 |   },
     | This ends { (opened on line 6).

  19 |   {
     | Inside the top of the file, this line runs as written: {. It happens in order, after the line above it and before the line below it.

  20 |     id: 'gcal',
     | Inside the top of the file, this line runs as written: id: 'gcal',. It happens in order, after the line above it and before the line below it.

  21 |     label: 'Google Calendar',
     | Inside the top of the file, this line runs as written: label: 'Google Calendar',. It happens in order, after the line above it and before the line below it.

  22 |     description: 'Sync upcoming events as deadlines',
     | Inside the top of the file, this line runs as written: description: 'Sync upcoming events as deadlines',. It happens in order, after the line above it and before the line below it.

  23 |     color: '#1a73e8',
     | Inside the top of the file, this line runs as written: color: '#1a73e8',. It happens in order, after the line above it and before the line below it.

  24 |     urlEndpoint: '/integrations/google/url',
     | Inside the top of the file, this line runs as written: urlEndpoint: '/integrations/google/url',. It happens in order, after the line above it and before the line below it.

  25 |     syncEndpoint: '/integrations/gcal/sync',
     | Inside the top of the file, this line runs as written: syncEndpoint: '/integrations/gcal/sync',. It happens in order, after the line above it and before the line below it.

  26 |     icon: (
     | Inside the top of the file, this line runs as written: icon: (. It happens in order, after the line above it and before the line below it.

  27 |       <svg viewBox="0 0 24 24" fill="currentColor" width="22" height="22">
     | This draws one piece of the page while the top of the file is showing.

  28 |         <path d="M19 3h-1V1h-2v2H8V1H6v2H5C3.9 3 3 3.9 3 5v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V8h14v11zM7 10h5v5H7z" />
     | This draws one piece of the page while the top of the file is showing.

  29 |       </svg>
     | This ends a drawing that the top of the file started just above.

  30 |     ),
     | This closes a box of instructions that opened above.

  31 |   },
     | This ends { (opened on line 19).

  32 |   {
     | Inside the top of the file, this line runs as written: {. It happens in order, after the line above it and before the line below it.

  33 |     id: 'slack',
     | Inside the top of the file, this line runs as written: id: 'slack',. It happens in order, after the line above it and before the line below it.

  34 |     label: 'Slack',
     | Inside the top of the file, this line runs as written: label: 'Slack',. It happens in order, after the line above it and before the line below it.

  35 |     description: 'Turn starred Slack messages into tasks',
     | Inside the top of the file, this line runs as written: description: 'Turn starred Slack messages into tasks',. It happens in order, after the line above it and before the line below it.

  36 |     color: '#611f69',
     | Inside the top of the file, this line runs as written: color: '#611f69',. It happens in order, after the line above it and before the line below it.

  37 |     urlEndpoint: '/integrations/slack/url',
     | Inside the top of the file, this line runs as written: urlEndpoint: '/integrations/slack/url',. It happens in order, after the line above it and before the line below it.

  38 |     syncEndpoint: '/integrations/slack/sync',
     | Inside the top of the file, this line runs as written: syncEndpoint: '/integrations/slack/sync',. It happens in order, after the line above it and before the line below it.

  39 |     icon: (
     | Inside the top of the file, this line runs as written: icon: (. It happens in order, after the line above it and before the line below it.

  40 |       <svg viewBox="0 0 24 24" fill="currentColor" width="22" height="22">
     | This draws one piece of the page while the top of the file is showing.

  41 |         <path d="M5.042 15.165a2.528 2.528 0 01-2.52 2.523A2.528 2.528 0 010 15.165a2.527 2.527 0 012.522-2.52h2.52v2.52zM6.313 15.165a2.527 2.527 0 012.521-2.52 2.527 2.527 0 012.521 2.52v6.313A2.528 2.528 0 018.834 24a2.528 2.528 0 01-2.521-2.522v-6.313zM8.834 5.042a2.528 2.528 0 01-2.521-2.52A2.528 2.528 0 018.834 0a2.528 2.528 0 012.521 2.522v2.52H8.834zM8.834 6.313a2.528 2.528 0 012.521 2.521 2.528 2.528 0 01-2.521 2.521H2.522A2.528 2.528 0 010 8.834a2.528 2.528 0 012.522-2.521h6.312zM18.956 8.834a2.528 2.528 0 012.522-2.521A2.528 2.528 0 0124 8.834a2.528 2.528 0 01-2.522 2.521h-2.522V8.834zM17.688 8.834a2.528 2.528 0 01-2.523 2.521 2.527 2.527 0 01-2.52-2.521V2.522A2.527 2.527 0 0115.165 0a2.528 2.528 0 012.523 2.522v6.312zM15.165 18.956a2.528 2.528 0 012.523 2.522A2.528 2.528 0 0115.165 24a2.527 2.527 0 01-2.52-2.522v-2.522h2.52zM15.165 17.688a2.527 2.527 0 01-2.52-2.523 2.526 2.526 0 012.52-2.52h6.313A2.527 2.527 0 0124 15.165a2.528 2.528 0 01-2.522 2.523h-6.313z" />
     | This draws one piece of the page while the top of the file is showing.

  42 |       </svg>
     | This ends a drawing that the top of the file started just above.

  43 |     ),
     | This closes a box of instructions that opened above.

  44 |   },
     | This ends { (opened on line 32).

  45 | ];
     | Inside the top of the file, this line runs as written: ];. It happens in order, after the line above it and before the line below it.

  46 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  47 | function fmtDate(iso) {
     | This starts fmtDate. Short local date-time for 'last synced'.

  48 |   if (!iso) return null;
     | This asks a yes-or-no question. The next bit runs only on yes.

  49 |   return new Date(iso).toLocaleDateString(undefined, { month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' });
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  50 | }
     | This ends fmtDate (opened on line 47).

  51 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  52 | export default function ConnectorsPage() {
     | This starts ConnectorsPage. Full-page version of the three connectors, plus toasts and the OAuth return query string.

  53 |   const [status, setStatus] = useState(null);
     | This gives a short name to a value so the rest of ConnectorsPage can use it.

  54 |   const [syncing, setSyncing] = useState({});
     | This gives a short name to a value so the rest of ConnectorsPage can use it.

  55 |   const [connecting, setConnecting] = useState({});
     | This gives a short name to a value so the rest of ConnectorsPage can use it.

  56 |   const [toast, setToast] = useState(null);
     | This gives a short name to a value so the rest of ConnectorsPage can use it.

  57 |   const [searchParams, setSearchParams] = useSearchParams();
     | This gives a short name to a value so the rest of ConnectorsPage can use it.

  58 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  59 |   const loadStatus = useCallback(async () => {
     | This gives a short name to a value so the rest of ConnectorsPage can use it.

  60 |     try {
     | Inside ConnectorsPage, this line runs as written: try {. It happens in order, after the line above it and before the line below it.

  61 |       const data = await api.get('/integrations/status');
     | This gives a short name to a value so the rest of ConnectorsPage can use it.

  62 |       setStatus(data);
     | Inside ConnectorsPage, this line runs as written: setStatus(data);. It happens in order, after the line above it and before the line below it.

  63 |     } catch {
     | This ends try { (opened on line 60).

  64 |       // ignore
     | A note written for people. The app does not run it.

  65 |     }
     | This ends } catch { (opened on line 63).

  66 |   }, []);
     | This ends const loadStatus = useCallback(async () => { (opened on line 59).

  67 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  68 |   useEffect(() => {
     | This is an extra job that happens after the picture is drawn.

  69 |     loadStatus();
     | Inside ConnectorsPage, this line runs as written: loadStatus();. It happens in order, after the line above it and before the line below it.

  70 |   }, [loadStatus]);
     | This ends effect in ConnectorsPage (opened on line 68).

  71 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  72 |   // Handle redirect back from OAuth
     | A note written for people. The app does not run it.

  73 |   useEffect(() => {
     | This is an extra job that happens after the picture is drawn.

  74 |     const connected = searchParams.get('connected');
     | This gives a short name to a value so the rest of ConnectorsPage can use it.

  75 |     const error = searchParams.get('error');
     | This gives a short name to a value so the rest of ConnectorsPage can use it.

  76 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  77 |     if (connected) {
     | This asks a yes-or-no question. The next bit runs only on yes.

  78 |       showToast(`${connected === 'google' ? 'Gmail & Google Calendar' : 'Slack'} connected!`, 'success');
     | This ends if (connected) { (opened on line 77).

  79 |       setSearchParams({});
     | This ends if (connected) { (opened on line 77).

  80 |       loadStatus();
     | Inside ConnectorsPage, this line runs as written: loadStatus();. It happens in order, after the line above it and before the line below it.

  81 |     } else if (error) {
     | This ends if (connected) { (opened on line 77).

  82 |       showToast('Connection failed. Please try again.', 'error');
     | Inside ConnectorsPage, this line runs as written: showToast('Connection failed. Please try again.', 'error');. It happens in order, after the line above it and before the line below it.

  83 |       setSearchParams({});
     | This ends } else if (error) { (opened on line 81).

  84 |     }
     | This ends } else if (error) { (opened on line 81).

  85 |   }, [searchParams, setSearchParams, loadStatus]);
     | This ends effect in ConnectorsPage (opened on line 73).

  86 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  87 |   function showToast(message, type = 'success') {
     | This starts showToast. Sets toast state and clears it after 4 seconds.

  88 |     setToast({ message, type });
     | This ends showToast (opened on line 87).

  89 |     setTimeout(() => setToast(null), 4000);
     | Inside showToast, this line runs as written: setTimeout(() => setToast(null), 4000);. It happens in order, after the line above it and before the line below it.

  90 |   }
     | This ends showToast (opened on line 87).

  91 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  92 |   async function handleConnect(connector) {
     | This starts handleConnect. GET the connector's urlEndpoint and set window.location to that OAuth URL.

  93 |     setConnecting(p => ({ ...p, [connector.id]: true }));
     | This ends handleConnect (opened on line 92).

  94 |     try {
     | Inside handleConnect, this line runs as written: try {. It happens in order, after the line above it and before the line below it.

  95 |       const { url } = await api.get(connector.urlEndpoint);
     | This gives a short name to a value so the rest of handleConnect can use it.

  96 |       window.location.href = url;
     | Inside handleConnect, this line runs as written: window.location.href = url;. It happens in order, after the line above it and before the line below it.

  97 |     } catch {
     | This ends try { (opened on line 94).

  98 |       showToast('Connection unavailable. Please try again later.', 'error');
     | Inside handleConnect, this line runs as written: showToast('Connection unavailable. Please try again later.', 'error');. It happens in order, after the line above it and before the line below it.

  99 |       setConnecting(p => ({ ...p, [connector.id]: false }));
     | This ends } catch { (opened on line 97).

 100 |     }
     | This ends } catch { (opened on line 97).

 101 |   }
     | This ends handleConnect (opened on line 92).

 102 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 103 |   async function handleSync(connector) {
     | This starts handleSync. POST the sync endpoint. The page toast includes result.synced and result.created.

 104 |     setSyncing(p => ({ ...p, [connector.id]: true }));
     | This ends handleSync (opened on line 103).

 105 |     try {
     | Inside handleSync, this line runs as written: try {. It happens in order, after the line above it and before the line below it.

 106 |       const result = await api.post(connector.syncEndpoint);
     | This gives a short name to a value so the rest of handleSync can use it.

 107 |       showToast(`Synced ${result.synced} items, created ${result.created} new tasks.`, 'success');
     | This ends try { (opened on line 105).

 108 |       loadStatus();
     | Inside handleSync, this line runs as written: loadStatus();. It happens in order, after the line above it and before the line below it.

 109 |     } catch (err) {
     | This ends try { (opened on line 105).

 110 |       const msg = err.response?.data?.error || 'Sync failed.';
     | This gives a short name to a value so the rest of handleSync can use it.

 111 |       showToast(msg, 'error');
     | Inside handleSync, this line runs as written: showToast(msg, 'error');. It happens in order, after the line above it and before the line below it.

 112 |     } finally {
     | This ends } catch (err) { (opened on line 109).

 113 |       setSyncing(p => ({ ...p, [connector.id]: false }));
     | This ends } finally { (opened on line 112).

 114 |     }
     | This ends } finally { (opened on line 112).

 115 |   }
     | This ends handleSync (opened on line 103).

 116 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 117 |   async function handleDisconnect(connector) {
     | This starts handleDisconnect. DELETE /integrations/:id and refresh status.

 118 |     try {
     | Inside handleDisconnect, this line runs as written: try {. It happens in order, after the line above it and before the line below it.

 119 |       await api.delete(`/integrations/${connector.id}`);
     | This asks the server (the office that keeps tasks and accounts) for something, or sends it something.

 120 |       showToast(`${connector.label} disconnected.`, 'success');
     | This ends try { (opened on line 118).

 121 |       loadStatus();
     | Inside handleDisconnect, this line runs as written: loadStatus();. It happens in order, after the line above it and before the line below it.

 122 |     } catch {
     | This ends try { (opened on line 118).

 123 |       showToast('Failed to disconnect.', 'error');
     | Inside handleDisconnect, this line runs as written: showToast('Failed to disconnect.', 'error');. It happens in order, after the line above it and before the line below it.

 124 |     }
     | This ends } catch { (opened on line 122).

 125 |   }
     | This ends handleDisconnect (opened on line 117).

 126 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 127 |   return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

 128 |     <div className="connectors-page">
     | This draws one piece of the page while ConnectorsPage is showing.

 129 |       {toast && (
     | Inside ConnectorsPage, this line runs as written: {toast && (. It happens in order, after the line above it and before the line below it.

 130 |         <div className={`connectors-toast connectors-toast--${toast.type}`}>
     | This draws one piece of the page while ConnectorsPage is showing.

 131 |           {toast.message}
     | This ends ConnectorsPage (opened on line 52).

 132 |         </div>
     | This ends a drawing that ConnectorsPage started just above.

 133 |       )}
     | This ends ConnectorsPage (opened on line 52).

 134 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 135 |       <div className="page-header">
     | This draws one piece of the page while ConnectorsPage is showing.

 136 |         <h1 className="page-title">Connectors</h1>
     | This draws one piece of the page while ConnectorsPage is showing.

 137 |         <p className="page-subtitle">
     | This draws one piece of the page while ConnectorsPage is showing.

 138 |           Link your tools to automatically pull emails, events, and messages as tasks.
     | Inside ConnectorsPage, this line runs as written: Link your tools to automatically pull emails, events, and messages as tasks.. It happens in order, after the line above it and before the line below it.

 139 |         </p>
     | This ends a drawing that ConnectorsPage started just above.

 140 |       </div>
     | This ends a drawing that ConnectorsPage started just above.

 141 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 142 |       <div className="connectors-list">
     | This draws one piece of the page while ConnectorsPage is showing.

 143 |         {CONNECTORS.map((connector) => {
     | Inside ConnectorsPage, this line runs as written: {CONNECTORS.map((connector) => {. It happens in order, after the line above it and before the line below it.

 144 |           const s = status?.[connector.id];
     | This gives a short name to a value so the rest of ConnectorsPage can use it.

 145 |           const isConnected = !!s?.connected;
     | This gives a short name to a value so the rest of ConnectorsPage can use it.

 146 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 147 |           return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

 148 |             <div key={connector.id} className="connector-card">
     | This draws one piece of the page while ConnectorsPage is showing.

 149 |               <div className="connector-card-icon" style={{ color: connector.color, background: connector.color + '18' }}>
     | This draws one piece of the page while ConnectorsPage is showing.

 150 |                 {connector.icon}
     | This ends {CONNECTORS.map((connector) => { (opened on line 143).

 151 |               </div>
     | This ends a drawing that ConnectorsPage started just above.

 152 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 153 |               <div className="connector-card-body">
     | This draws one piece of the page while ConnectorsPage is showing.

 154 |                 <div className="connector-card-title">{connector.label}</div>
     | This draws one piece of the page while ConnectorsPage is showing.

 155 |                 <div className="connector-card-desc">{connector.description}</div>
     | This draws one piece of the page while ConnectorsPage is showing.

 156 |                 {isConnected && s.lastSyncedAt && (
     | Inside ConnectorsPage, this line runs as written: {isConnected && s.lastSyncedAt && (. It happens in order, after the line above it and before the line below it.

 157 |                   <div className="connector-card-meta">Last synced {fmtDate(s.lastSyncedAt)}</div>
     | This draws one piece of the page while ConnectorsPage is showing.

 158 |                 )}
     | This ends {CONNECTORS.map((connector) => { (opened on line 143).

 159 |                 {isConnected && !s.lastSyncedAt && (
     | Inside ConnectorsPage, this line runs as written: {isConnected && !s.lastSyncedAt && (. It happens in order, after the line above it and before the line below it.

 160 |                   <div className="connector-card-meta">Connected {fmtDate(s.connectedAt)} · Never synced</div>
     | This draws one piece of the page while ConnectorsPage is showing.

 161 |                 )}
     | This ends {CONNECTORS.map((connector) => { (opened on line 143).

 162 |               </div>
     | This ends a drawing that ConnectorsPage started just above.

 163 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 164 |               <div className="connector-card-actions">
     | This draws one piece of the page while ConnectorsPage is showing.

 165 |                 {isConnected ? (
     | Inside ConnectorsPage, this line runs as written: {isConnected ? (. It happens in order, after the line above it and before the line below it.

 166 |                   <>
     | This draws one piece of the page while ConnectorsPage is showing.

 167 |                     <button
     | This draws one piece of the page while ConnectorsPage is showing.

 168 |                       className="btn-connector btn-connector-sync"
     | Inside ConnectorsPage, this line runs as written: className="btn-connector btn-connector-sync". It happens in order, after the line above it and before the line below it.

 169 |                       onClick={() => handleSync(connector)}
     | This decides what happens when you press.

 170 |                       disabled={syncing[connector.id]}
     | This ends {CONNECTORS.map((connector) => { (opened on line 143).

 171 |                     >
     | Inside ConnectorsPage, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 172 |                       {syncing[connector.id] ? 'Syncing…' : 'Sync now'}
     | This ends {CONNECTORS.map((connector) => { (opened on line 143).

 173 |                     </button>
     | This ends a drawing that ConnectorsPage started just above.

 174 |                     <button
     | This draws one piece of the page while ConnectorsPage is showing.

 175 |                       className="btn-connector btn-connector-disconnect"
     | Inside ConnectorsPage, this line runs as written: className="btn-connector btn-connector-disconnect". It happens in order, after the line above it and before the line below it.

 176 |                       onClick={() => handleDisconnect(connector)}
     | This decides what happens when you press.

 177 |                     >
     | Inside ConnectorsPage, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 178 |                       Disconnect
     | Inside ConnectorsPage, this line runs as written: Disconnect. It happens in order, after the line above it and before the line below it.

 179 |                     </button>
     | This ends a drawing that ConnectorsPage started just above.

 180 |                   </>
     | This ends a drawing that ConnectorsPage started just above.

 181 |                 ) : (
     | This closes a box of instructions that opened above.

 182 |                   <button
     | This draws one piece of the page while ConnectorsPage is showing.

 183 |                     className="btn-connector btn-connector-connect"
     | Inside ConnectorsPage, this line runs as written: className="btn-connector btn-connector-connect". It happens in order, after the line above it and before the line below it.

 184 |                     onClick={() => handleConnect(connector)}
     | This decides what happens when you press.

 185 |                     disabled={connecting[connector.id]}
     | This ends {CONNECTORS.map((connector) => { (opened on line 143).

 186 |                     style={{ '--accent': connector.color }}
     | This ends {CONNECTORS.map((connector) => { (opened on line 143).

 187 |                   >
     | Inside ConnectorsPage, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 188 |                     {connecting[connector.id] ? 'Redirecting…' : 'Connect'}
     | This ends {CONNECTORS.map((connector) => { (opened on line 143).

 189 |                   </button>
     | This ends a drawing that ConnectorsPage started just above.

 190 |                 )}
     | This ends {CONNECTORS.map((connector) => { (opened on line 143).

 191 |               </div>
     | This ends a drawing that ConnectorsPage started just above.

 192 |             </div>
     | This ends a drawing that ConnectorsPage started just above.

 193 |           );
     | This closes a box of instructions that opened above.

 194 |         })}
     | This ends {CONNECTORS.map((connector) => { (opened on line 143).

 195 |       </div>
     | This ends a drawing that ConnectorsPage started just above.

 196 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 197 |     </div>
     | This ends a drawing that ConnectorsPage started just above.

 198 |   );
     | This closes a box of instructions that opened above.

 199 | }
     | This ends ConnectorsPage (opened on line 52).

