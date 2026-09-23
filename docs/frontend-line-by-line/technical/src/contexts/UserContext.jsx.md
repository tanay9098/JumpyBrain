# `src/contexts/UserContext.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import React, { createContext, useContext, useState, useEffect } from "react";
     | Import for who is logged in, stored in memory and localStorage: `import React, { createContext, useContext, useState, useEffect } from "react";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   2 | import api, { updateProfile } from "../services/api";
     | Import for who is logged in, stored in memory and localStorage: `import api, { updateProfile } from "../services/api";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   3 | import { connectSocket, disconnectSocket, getSocket } from "../services/socket";
     | Import for who is logged in, stored in memory and localStorage: `import { connectSocket, disconnectSocket, getSocket } from "../services/socket";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   4 | import { queryClient } from "../providers/QueryProvider";
     | Import for who is logged in, stored in memory and localStorage: `import { queryClient } from "../providers/QueryProvider";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   5 | 
     | Blank line in `src/contexts/UserContext.jsx` (who is logged in, stored in memory and localStorage), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   6 | const ctx = createContext();
     | In `the top of the file` (src/contexts/UserContext.jsx): `ctx` is assigned `createContext();`. Later lines in this function read that name.

   7 | export const useUser = () => useContext(ctx);
     | Named export from who is logged in, stored in memory and localStorage: `export const useUser = () => useContext(ctx);`.

   8 | 
     | Blank line in `src/contexts/UserContext.jsx` (who is logged in, stored in memory and localStorage), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   9 | // Chrome extension ID to sync auth into (see chrome-extension/public/manifest.json's
     | Comment inside the top of the file. Not executed. It documents the next code: Chrome extension ID to sync auth into (see chrome-extension/public/manifest.json's

  10 | // "externally_connectable" and the background service worker's onMessageExternal
     | Comment inside the top of the file. Not executed. It documents the next code: "externally_connectable" and the background service worker's onMessageExternal

  11 | // listener). Left unset, this is a silent no-op — the extension just keeps its own
     | Comment inside the top of the file. Not executed. It documents the next code: listener). Left unset, this is a silent no-op — the extension just keeps its own

  12 | // separate Google sign-in.
     | Comment inside the top of the file. Not executed. It documents the next code: separate Google sign-in.

  13 | const EXTENSION_ID = import.meta.env.VITE_EXTENSION_ID;
     | In `the top of the file` (src/contexts/UserContext.jsx): `EXTENSION_ID`: VITE_EXTENSION_ID. If unset, sendToExtension does nothing and the Chrome extension keeps its own login. The code is `const EXTENSION_ID = import.meta.env.VITE_EXTENSION_ID;`.

  14 | 
     | Blank line in `src/contexts/UserContext.jsx` (who is logged in, stored in memory and localStorage), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  15 | function sendToExtension(message) {
     | Defines `sendToExtension` in who is logged in, stored in memory and localStorage. chrome.runtime.sendMessage to EXTENSION_ID. Swallows the 'no extension' error.

  16 |   const chromeRuntime = window.chrome?.runtime;
     | In `sendToExtension` (src/contexts/UserContext.jsx): `chromeRuntime` is assigned `window.chrome?.runtime;`. Later lines in this function read that name.

  17 |   if (!EXTENSION_ID || !chromeRuntime?.sendMessage) return;
     | In `sendToExtension` (src/contexts/UserContext.jsx): branch `if (!EXTENSION_ID || !chromeRuntime?.sendMessage) return;`. Only one side runs.

  18 |   try {
     | In `sendToExtension` (src/contexts/UserContext.jsx): error path `try {`.

  19 |     chromeRuntime.sendMessage(EXTENSION_ID, message, () => {
     | In `sendToExtension` (src/contexts/UserContext.jsx): statement `chromeRuntime.sendMessage(EXTENSION_ID, message, () => {`. It runs when sendToExtension runs, in order, before the next line of the same function.

  20 |       void chromeRuntime.lastError; // extension not installed / no listener — ignore
     | In `sendToExtension` (src/contexts/UserContext.jsx): statement `void chromeRuntime.lastError; // extension not installed / no listener — ignore`. It runs when sendToExtension runs, in order, before the next line of the same function.

  21 |     });
     | In `sendToExtension` (src/contexts/UserContext.jsx): `});` closes chromeRuntime.sendMessage(EXTENSION_ID, message, (opened on line 19). Names declared inside that block end here.

  22 |   } catch {
     | In `sendToExtension` (src/contexts/UserContext.jsx): `} catch {` closes try { (opened on line 18). Names declared inside that block end here.

  23 |     // chrome.runtime unavailable in this context — ignore
     | Comment inside sendToExtension. Not executed. It documents the next code: chrome.runtime unavailable in this context — ignore

  24 |   }
     | In `sendToExtension` (src/contexts/UserContext.jsx): `}` closes } catch { (opened on line 22). Names declared inside that block end here.

  25 | }
     | In `sendToExtension` (src/contexts/UserContext.jsx): `}` closes sendToExtension (opened on line 15). Names declared inside that block end here.

  26 | 
     | Blank line in `src/contexts/UserContext.jsx` (who is logged in, stored in memory and localStorage), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  27 | export function UserProvider({ children }) {
     | Named export from who is logged in, stored in memory and localStorage: `export function UserProvider({ children }) {`.

  28 |   const [user, setUser] = useState(null);
     | In `UserProvider` (src/contexts/UserContext.jsx): `user`: The logged-in profile object. Null means ProtectedRoute renders Auth. The code is `const [user, setUser] = useState(null);`.

  29 |   const [token, setToken] = useState(null);
     | In `UserProvider` (src/contexts/UserContext.jsx): `token`: The access token in React state. The copy that Axios actually sends is localStorage accessToken, written by saveToken. The code is `const [token, setToken] = useState(null);`.

  30 |   const [loading, setLoading] = useState(true);
     | In `UserProvider` (src/contexts/UserContext.jsx): `loading`: True until UserProvider finishes the first localStorage read. ProtectedRoute renders nothing during that moment so Auth does not flash. The code is `const [loading, setLoading] = useState(true);`.

  31 | 
     | Blank line in `src/contexts/UserContext.jsx` (who is logged in, stored in memory and localStorage), inside UserProvider. The parser skips it. It separates the previous statement from the next so the function is readable.

  32 |   // Load token and user from localStorage on app start
     | Comment inside UserProvider. Not executed. It documents the next code: Load token and user from localStorage on app start

  33 |   useEffect(() => {
     | In `UserProvider` (src/contexts/UserContext.jsx): opens or continues an effect — `useEffect(() => {`. The effect body runs after paint, and its cleanup runs before the next effect and on unmount.

  34 |     const storedToken = localStorage.getItem("accessToken");
     | In `UserProvider` (src/contexts/UserContext.jsx): `storedToken` is assigned `localStorage.getItem("accessToken");`. Later lines in this function read that name.

  35 |     const storedUser = localStorage.getItem("user");
     | In `UserProvider` (src/contexts/UserContext.jsx): `storedUser` is assigned `localStorage.getItem("user");`. Later lines in this function read that name.

  36 | 
     | Blank line in `src/contexts/UserContext.jsx` (who is logged in, stored in memory and localStorage), inside UserProvider. The parser skips it. It separates the previous statement from the next so the function is readable.

  37 |     if (storedToken) {
     | In `UserProvider` (src/contexts/UserContext.jsx): branch `if (storedToken) {`. Only one side runs.

  38 |       setToken(storedToken);
     | In `UserProvider` (src/contexts/UserContext.jsx): statement `setToken(storedToken);`. It runs when UserProvider runs, in order, before the next line of the same function.

  39 |     }
     | In `UserProvider` (src/contexts/UserContext.jsx): `}` closes if (storedToken) { (opened on line 37). Names declared inside that block end here.

  40 | 
     | Blank line in `src/contexts/UserContext.jsx` (who is logged in, stored in memory and localStorage), inside UserProvider. The parser skips it. It separates the previous statement from the next so the function is readable.

  41 |     if (storedUser && storedUser !== "undefined") {
     | In `UserProvider` (src/contexts/UserContext.jsx): branch `if (storedUser && storedUser !== "undefined") {`. Only one side runs.

  42 |       try {
     | In `UserProvider` (src/contexts/UserContext.jsx): error path `try {`.

  43 |         setUser(JSON.parse(storedUser));
     | In `UserProvider` (src/contexts/UserContext.jsx): statement `setUser(JSON.parse(storedUser));`. It runs when UserProvider runs, in order, before the next line of the same function.

  44 |       } catch {
     | In `UserProvider` (src/contexts/UserContext.jsx): `} catch {` closes try { (opened on line 42). Names declared inside that block end here.

  45 |         localStorage.removeItem("user");
     | In `UserProvider` (src/contexts/UserContext.jsx): browser storage — `localStorage.removeItem("user");`. This survives reloads on this origin and is shared by any script that uses the same key.

  46 |       }
     | In `UserProvider` (src/contexts/UserContext.jsx): `}` closes } catch { (opened on line 44). Names declared inside that block end here.

  47 |     }
     | In `UserProvider` (src/contexts/UserContext.jsx): `}` closes if (storedUser && storedUser !== "undefi (opened on line 41). Names declared inside that block end here.

  48 | 
     | Blank line in `src/contexts/UserContext.jsx` (who is logged in, stored in memory and localStorage), inside UserProvider. The parser skips it. It separates the previous statement from the next so the function is readable.

  49 |     setLoading(false);
     | In `UserProvider` (src/contexts/UserContext.jsx): statement `setLoading(false);`. It runs when UserProvider runs, in order, before the next line of the same function.

  50 |   }, []);
     | In `UserProvider` (src/contexts/UserContext.jsx): `}, []);` closes effect in UserProvider (opened on line 33). Names declared inside that block end here.

  51 | 
     | Blank line in `src/contexts/UserContext.jsx` (who is logged in, stored in memory and localStorage), inside UserProvider. The parser skips it. It separates the previous statement from the next so the function is readable.

  52 |   // Push auth state to the Chrome extension (if installed) so users don't have to sign
     | Comment inside UserProvider. Not executed. It documents the next code: Push auth state to the Chrome extension (if installed) so users don't have to sign

  53 |   // in twice — mirrors this context's token/user into chrome.storage.local via a message
     | Comment inside UserProvider. Not executed. It documents the next code: in twice — mirrors this context's token/user into chrome.storage.local via a message

  54 |   // the extension's background service worker listens for.
     | Comment inside UserProvider. Not executed. It documents the next code: the extension's background service worker listens for.

  55 |   useEffect(() => {
     | In `UserProvider` (src/contexts/UserContext.jsx): opens or continues an effect — `useEffect(() => {`. The effect body runs after paint, and its cleanup runs before the next effect and on unmount.

  56 |     if (loading) return; // wait for the initial localStorage read to finish
     | In `UserProvider` (src/contexts/UserContext.jsx): branch `if (loading) return; // wait for the initial localStorage read to finish`. Only one side runs.

  57 |     if (token && user) {
     | In `UserProvider` (src/contexts/UserContext.jsx): branch `if (token && user) {`. Only one side runs.

  58 |       sendToExtension({
     | In `UserProvider` (src/contexts/UserContext.jsx): Messages the Chrome extension, if VITE_EXTENSION_ID is set, so the extension can reuse this login.

  59 |         type: 'SET_AUTH',
     | In `UserProvider` (src/contexts/UserContext.jsx): Messages the Chrome extension, if VITE_EXTENSION_ID is set, so the extension can reuse this login.

  60 |         payload: { authToken: token, apiUrl: import.meta.env.VITE_API_URL || 'http://localhost:4000/api', user },
     | In `UserProvider` (src/contexts/UserContext.jsx): `payload: { authToken: token, apiUrl: import.meta.env.VITE_API_URL || 'http://localhost:4000/api', user },` closes sendToExtension({ (opened on line 58). Names declared inside that block end here.

  61 |       });
     | In `UserProvider` (src/contexts/UserContext.jsx): `});` closes sendToExtension({ (opened on line 58). Names declared inside that block end here.

  62 |     } else if (!token) {
     | In `UserProvider` (src/contexts/UserContext.jsx): branch `} else if (!token) {`. Only one side runs.

  63 |       sendToExtension({ type: 'CLEAR_AUTH' });
     | In `UserProvider` (src/contexts/UserContext.jsx): `sendToExtension({ type: 'CLEAR_AUTH' });` closes } else if (!token) { (opened on line 62). Names declared inside that block end here.

  64 |     }
     | In `UserProvider` (src/contexts/UserContext.jsx): `}` closes } else if (!token) { (opened on line 62). Names declared inside that block end here.

  65 |   }, [token, user, loading]);
     | In `UserProvider` (src/contexts/UserContext.jsx): `}, [token, user, loading]);` closes effect in UserProvider (opened on line 55). Names declared inside that block end here.

  66 | 
     | Blank line in `src/contexts/UserContext.jsx` (who is logged in, stored in memory and localStorage), inside UserProvider. The parser skips it. It separates the previous statement from the next so the function is readable.

  67 |   // Connect socket when we have a token, disconnect on logout
     | Comment inside UserProvider. Not executed. It documents the next code: Connect socket when we have a token, disconnect on logout

  68 |   useEffect(() => {
     | In `UserProvider` (src/contexts/UserContext.jsx): opens or continues an effect — `useEffect(() => {`. The effect body runs after paint, and its cleanup runs before the next effect and on unmount.

  69 |     if (!token) return;
     | In `UserProvider` (src/contexts/UserContext.jsx): branch `if (!token) return;`. Only one side runs.

  70 |     const socket = connectSocket(token);
     | In `UserProvider` (src/contexts/UserContext.jsx): `socket`: The single Socket.IO client. connectSocket sets auth.token and connects. disconnectSocket drops it on logout. The code is `const socket = connectSocket(token);`.

  71 | 
     | Blank line in `src/contexts/UserContext.jsx` (who is logged in, stored in memory and localStorage), inside UserProvider. The parser skips it. It separates the previous statement from the next so the function is readable.

  72 |     socket.on('task:created', () => queryClient.invalidateQueries({ queryKey: ['tasks'] }));
     | In `UserProvider` (src/contexts/UserContext.jsx): Marks a React Query cache key stale. No screen is subscribed to that cache, so the lists on screen do not refresh from this line.

  73 |     socket.on('task:updated', () => queryClient.invalidateQueries({ queryKey: ['tasks'] }));
     | In `UserProvider` (src/contexts/UserContext.jsx): Marks a React Query cache key stale. No screen is subscribed to that cache, so the lists on screen do not refresh from this line.

  74 |     socket.on('tasks:refetch', () => queryClient.invalidateQueries({ queryKey: ['tasks'] }));
     | In `UserProvider` (src/contexts/UserContext.jsx): Marks a React Query cache key stale. No screen is subscribed to that cache, so the lists on screen do not refresh from this line.

  75 |     socket.on('habit:created', () => queryClient.invalidateQueries({ queryKey: ['habits'] }));
     | In `UserProvider` (src/contexts/UserContext.jsx): Marks a React Query cache key stale. No screen is subscribed to that cache, so the lists on screen do not refresh from this line.

  76 |     socket.on('habit:updated', () => queryClient.invalidateQueries({ queryKey: ['habits'] }));
     | In `UserProvider` (src/contexts/UserContext.jsx): Marks a React Query cache key stale. No screen is subscribed to that cache, so the lists on screen do not refresh from this line.

  77 |     socket.on('habit:deleted', () => queryClient.invalidateQueries({ queryKey: ['habits'] }));
     | In `UserProvider` (src/contexts/UserContext.jsx): Marks a React Query cache key stale. No screen is subscribed to that cache, so the lists on screen do not refresh from this line.

  78 | 
     | Blank line in `src/contexts/UserContext.jsx` (who is logged in, stored in memory and localStorage), inside UserProvider. The parser skips it. It separates the previous statement from the next so the function is readable.

  79 |     return () => {
     | In `UserProvider` (src/contexts/UserContext.jsx): return `return () => {`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  80 |       disconnectSocket();
     | In `UserProvider` (src/contexts/UserContext.jsx): Opens the Socket.IO connection with the access token. UserProvider does this whenever token changes.

  81 |     };
     | In `UserProvider` (src/contexts/UserContext.jsx): `};` closes return () => { (opened on line 79). Names declared inside that block end here.

  82 |   }, [token]);
     | In `UserProvider` (src/contexts/UserContext.jsx): `}, [token]);` closes effect in UserProvider (opened on line 68). Names declared inside that block end here.

  83 | 
     | Blank line in `src/contexts/UserContext.jsx` (who is logged in, stored in memory and localStorage), inside UserProvider. The parser skips it. It separates the previous statement from the next so the function is readable.

  84 |   // Save token whenever it changes
     | Comment inside UserProvider. Not executed. It documents the next code: Save token whenever it changes

  85 |   function saveToken(t) {
     | Defines `saveToken` in who is logged in, stored in memory and localStorage. React state plus localStorage accessToken. Axios reads localStorage, not React state.

  86 |     setToken(t);
     | In `saveToken` (src/contexts/UserContext.jsx): statement `setToken(t);`. It runs when saveToken runs, in order, before the next line of the same function.

  87 |     localStorage.setItem("accessToken", t);
     | In `saveToken` (src/contexts/UserContext.jsx): browser storage — `localStorage.setItem("accessToken", t);`. This survives reloads on this origin and is shared by any script that uses the same key.

  88 |   }
     | In `saveToken` (src/contexts/UserContext.jsx): `}` closes saveToken (opened on line 85). Names declared inside that block end here.

  89 | 
     | Blank line in `src/contexts/UserContext.jsx` (who is logged in, stored in memory and localStorage), inside UserProvider. The parser skips it. It separates the previous statement from the next so the function is readable.

  90 |   // Save user whenever it changes
     | Comment inside UserProvider. Not executed. It documents the next code: Save user whenever it changes

  91 |   function saveUser(u) {
     | Defines `saveUser` in who is logged in, stored in memory and localStorage. React state plus localStorage user. Passing null removes the key. Logout uses this.

  92 |     setUser(u);
     | In `saveUser` (src/contexts/UserContext.jsx): statement `setUser(u);`. It runs when saveUser runs, in order, before the next line of the same function.

  93 |     if (u) {
     | In `saveUser` (src/contexts/UserContext.jsx): branch `if (u) {`. Only one side runs.

  94 |       localStorage.setItem("user", JSON.stringify(u));
     | In `saveUser` (src/contexts/UserContext.jsx): browser storage — `localStorage.setItem("user", JSON.stringify(u));`. This survives reloads on this origin and is shared by any script that uses the same key.

  95 |     } else {
     | In `saveUser` (src/contexts/UserContext.jsx): branch `} else {`. Only one side runs.

  96 |       localStorage.removeItem("user");
     | In `saveUser` (src/contexts/UserContext.jsx): browser storage — `localStorage.removeItem("user");`. This survives reloads on this origin and is shared by any script that uses the same key.

  97 |     }
     | In `saveUser` (src/contexts/UserContext.jsx): `}` closes } else { (opened on line 95). Names declared inside that block end here.

  98 |   }
     | In `saveUser` (src/contexts/UserContext.jsx): `}` closes saveUser (opened on line 91). Names declared inside that block end here.

  99 | 
     | Blank line in `src/contexts/UserContext.jsx` (who is logged in, stored in memory and localStorage), inside UserProvider. The parser skips it. It separates the previous statement from the next so the function is readable.

 100 |   // Update user profile via API and sync local state
     | Comment inside UserProvider. Not executed. It documents the next code: Update user profile via API and sync local state

 101 |   async function updateUser(data) {
     | Defines `updateUser` in who is logged in, stored in memory and localStorage. PUT /profile via updateProfile, then merges the response onto the stored user.

 102 |     const updated = await updateProfile(data);
     | In `updateUser` (src/contexts/UserContext.jsx): `updated` is assigned `await updateProfile(data);`. Later lines in this function read that name.

 103 |     saveUser({ ...user, ...updated });
     | In `updateUser` (src/contexts/UserContext.jsx): `saveUser({ ...user, ...updated });` closes updateUser (opened on line 101). Names declared inside that block end here.

 104 |     return updated;
     | In `updateUser` (src/contexts/UserContext.jsx): return `return updated;`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

 105 |   }
     | In `updateUser` (src/contexts/UserContext.jsx): `}` closes updateUser (opened on line 101). Names declared inside that block end here.

 106 | 
     | Blank line in `src/contexts/UserContext.jsx` (who is logged in, stored in memory and localStorage), inside UserProvider. The parser skips it. It separates the previous statement from the next so the function is readable.

 107 |   return (
     | In `UserProvider` (src/contexts/UserContext.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

 108 |     <ctx.Provider value={{ user, setUser: saveUser, updateUser, token, setToken: saveToken, loading }}>
     | In `UserProvider` (src/contexts/UserContext.jsx): JSX `<ctx.Provider>`. React will create this node when the parent renders.. value is controlled by React state, so the DOM shows that state Source: `<ctx.Provider value={{ user, setUser: saveUser, updateUser, token, setToken: saveToken, loading }}>`

 109 |       {children}
     | In `UserProvider` (src/contexts/UserContext.jsx): `{children}` closes UserProvider (opened on line 27). Names declared inside that block end here.

 110 |     </ctx.Provider>
     | In `UserProvider` (src/contexts/UserContext.jsx): JSX `<ctx.Provider>`. This closes that element. Source: `</ctx.Provider>`

 111 |   );
     | In `UserProvider` (src/contexts/UserContext.jsx): statement `);`. It runs when UserProvider runs, in order, before the next line of the same function.

 112 | }
     | In `UserProvider` (src/contexts/UserContext.jsx): `}` closes UserProvider (opened on line 27). Names declared inside that block end here.

 113 | 
     | Blank line in `src/contexts/UserContext.jsx` (who is logged in, stored in memory and localStorage), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

