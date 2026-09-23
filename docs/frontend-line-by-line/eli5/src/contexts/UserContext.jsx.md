# `src/contexts/UserContext.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import React, { createContext, useContext, useState, useEffect } from "react";
     | Borrows React so this file can remember things and draw the screen.

   2 | import api, { updateProfile } from "../services/api";
     | This file borrows a tool another file already made.

   3 | import { connectSocket, disconnectSocket, getSocket } from "../services/socket";
     | This file borrows a tool another file already made.

   4 | import { queryClient } from "../providers/QueryProvider";
     | This file borrows a tool another file already made.

   5 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   6 | const ctx = createContext();
     | This gives a short name to a value so the rest of the top of the file can use it.

   7 | export const useUser = () => useContext(ctx);
     | This lets another file use this piece by its name.

   8 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   9 | // Chrome extension ID to sync auth into (see chrome-extension/public/manifest.json's
     | A note written for people. The app does not run it.

  10 | // "externally_connectable" and the background service worker's onMessageExternal
     | A note written for people. The app does not run it.

  11 | // listener). Left unset, this is a silent no-op — the extension just keeps its own
     | A note written for people. The app does not run it.

  12 | // separate Google sign-in.
     | A note written for people. The app does not run it.

  13 | const EXTENSION_ID = import.meta.env.VITE_EXTENSION_ID;
     | VITE_EXTENSION_ID. If unset, sendToExtension does nothing and the Chrome extension keeps its own login.

  14 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  15 | function sendToExtension(message) {
     | This starts sendToExtension. chrome.runtime.sendMessage to EXTENSION_ID. Swallows the 'no extension' error.

  16 |   const chromeRuntime = window.chrome?.runtime;
     | This gives a short name to a value so the rest of sendToExtension can use it.

  17 |   if (!EXTENSION_ID || !chromeRuntime?.sendMessage) return;
     | This asks a yes-or-no question. The next bit runs only on yes.

  18 |   try {
     | Inside sendToExtension, this line runs as written: try {. It happens in order, after the line above it and before the line below it.

  19 |     chromeRuntime.sendMessage(EXTENSION_ID, message, () => {
     | Inside sendToExtension, this line runs as written: chromeRuntime.sendMessage(EXTENSION_ID, message, () => {. It happens in order, after the line above it and before the line below it.

  20 |       void chromeRuntime.lastError; // extension not installed / no listener — ignore
     | Inside sendToExtension, this line runs as written: void chromeRuntime.lastError; // extension not installed / no listener — ignore. It happens in order, after the line above it and before the line below it.

  21 |     });
     | This ends chromeRuntime.sendMessage(EXTENSION_ID, message, (opened on line 19).

  22 |   } catch {
     | This ends try { (opened on line 18).

  23 |     // chrome.runtime unavailable in this context — ignore
     | A note written for people. The app does not run it.

  24 |   }
     | This ends } catch { (opened on line 22).

  25 | }
     | This ends sendToExtension (opened on line 15).

  26 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  27 | export function UserProvider({ children }) {
     | This lets another file use this piece by its name.

  28 |   const [user, setUser] = useState(null);
     | The logged-in profile object. Null means ProtectedRoute renders Auth.

  29 |   const [token, setToken] = useState(null);
     | The access token in React state. The copy that Axios actually sends is localStorage accessToken, written by saveToken.

  30 |   const [loading, setLoading] = useState(true);
     | True until UserProvider finishes the first localStorage read. ProtectedRoute renders nothing during that moment so Auth does not flash.

  31 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  32 |   // Load token and user from localStorage on app start
     | A note written for people. The app does not run it.

  33 |   useEffect(() => {
     | This is an extra job that happens after the picture is drawn.

  34 |     const storedToken = localStorage.getItem("accessToken");
     | This gives a short name to a value so the rest of UserProvider can use it.

  35 |     const storedUser = localStorage.getItem("user");
     | This gives a short name to a value so the rest of UserProvider can use it.

  36 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  37 |     if (storedToken) {
     | This asks a yes-or-no question. The next bit runs only on yes.

  38 |       setToken(storedToken);
     | Inside UserProvider, this line runs as written: setToken(storedToken);. It happens in order, after the line above it and before the line below it.

  39 |     }
     | This ends if (storedToken) { (opened on line 37).

  40 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  41 |     if (storedUser && storedUser !== "undefined") {
     | This asks a yes-or-no question. The next bit runs only on yes.

  42 |       try {
     | Inside UserProvider, this line runs as written: try {. It happens in order, after the line above it and before the line below it.

  43 |         setUser(JSON.parse(storedUser));
     | Inside UserProvider, this line runs as written: setUser(JSON.parse(storedUser));. It happens in order, after the line above it and before the line below it.

  44 |       } catch {
     | This ends try { (opened on line 42).

  45 |         localStorage.removeItem("user");
     | This looks in the browser's pocket, or puts something there, so it is still around after a refresh.

  46 |       }
     | This ends } catch { (opened on line 44).

  47 |     }
     | This ends if (storedUser && storedUser !== "undefi (opened on line 41).

  48 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  49 |     setLoading(false);
     | Inside UserProvider, this line runs as written: setLoading(false);. It happens in order, after the line above it and before the line below it.

  50 |   }, []);
     | This ends effect in UserProvider (opened on line 33).

  51 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  52 |   // Push auth state to the Chrome extension (if installed) so users don't have to sign
     | A note written for people. The app does not run it.

  53 |   // in twice — mirrors this context's token/user into chrome.storage.local via a message
     | A note written for people. The app does not run it.

  54 |   // the extension's background service worker listens for.
     | A note written for people. The app does not run it.

  55 |   useEffect(() => {
     | This is an extra job that happens after the picture is drawn.

  56 |     if (loading) return; // wait for the initial localStorage read to finish
     | This looks in the browser's pocket, or puts something there, so it is still around after a refresh.

  57 |     if (token && user) {
     | This asks a yes-or-no question. The next bit runs only on yes.

  58 |       sendToExtension({
     | Inside UserProvider, this line runs as written: sendToExtension({. It happens in order, after the line above it and before the line below it.

  59 |         type: 'SET_AUTH',
     | Inside UserProvider, this line runs as written: type: 'SET_AUTH',. It happens in order, after the line above it and before the line below it.

  60 |         payload: { authToken: token, apiUrl: import.meta.env.VITE_API_URL || 'http://localhost:4000/api', user },
     | This ends sendToExtension({ (opened on line 58).

  61 |       });
     | This ends sendToExtension({ (opened on line 58).

  62 |     } else if (!token) {
     | This ends if (token && user) { (opened on line 57).

  63 |       sendToExtension({ type: 'CLEAR_AUTH' });
     | This ends } else if (!token) { (opened on line 62).

  64 |     }
     | This ends } else if (!token) { (opened on line 62).

  65 |   }, [token, user, loading]);
     | This ends effect in UserProvider (opened on line 55).

  66 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  67 |   // Connect socket when we have a token, disconnect on logout
     | A note written for people. The app does not run it.

  68 |   useEffect(() => {
     | This is an extra job that happens after the picture is drawn.

  69 |     if (!token) return;
     | This asks a yes-or-no question. The next bit runs only on yes.

  70 |     const socket = connectSocket(token);
     | The single Socket.IO client. connectSocket sets auth.token and connects. disconnectSocket drops it on logout.

  71 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  72 |     socket.on('task:created', () => queryClient.invalidateQueries({ queryKey: ['tasks'] }));
     | This ends effect in UserProvider (opened on line 68).

  73 |     socket.on('task:updated', () => queryClient.invalidateQueries({ queryKey: ['tasks'] }));
     | This ends effect in UserProvider (opened on line 68).

  74 |     socket.on('tasks:refetch', () => queryClient.invalidateQueries({ queryKey: ['tasks'] }));
     | This ends effect in UserProvider (opened on line 68).

  75 |     socket.on('habit:created', () => queryClient.invalidateQueries({ queryKey: ['habits'] }));
     | This ends effect in UserProvider (opened on line 68).

  76 |     socket.on('habit:updated', () => queryClient.invalidateQueries({ queryKey: ['habits'] }));
     | This ends effect in UserProvider (opened on line 68).

  77 |     socket.on('habit:deleted', () => queryClient.invalidateQueries({ queryKey: ['habits'] }));
     | This ends effect in UserProvider (opened on line 68).

  78 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  79 |     return () => {
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  80 |       disconnectSocket();
     | Inside UserProvider, this line runs as written: disconnectSocket();. It happens in order, after the line above it and before the line below it.

  81 |     };
     | This ends return () => { (opened on line 79).

  82 |   }, [token]);
     | This ends effect in UserProvider (opened on line 68).

  83 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  84 |   // Save token whenever it changes
     | A note written for people. The app does not run it.

  85 |   function saveToken(t) {
     | This starts saveToken. React state plus localStorage accessToken. Axios reads localStorage, not React state.

  86 |     setToken(t);
     | Inside saveToken, this line runs as written: setToken(t);. It happens in order, after the line above it and before the line below it.

  87 |     localStorage.setItem("accessToken", t);
     | This looks in the browser's pocket, or puts something there, so it is still around after a refresh.

  88 |   }
     | This ends saveToken (opened on line 85).

  89 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  90 |   // Save user whenever it changes
     | A note written for people. The app does not run it.

  91 |   function saveUser(u) {
     | This starts saveUser. React state plus localStorage user. Passing null removes the key. Logout uses this.

  92 |     setUser(u);
     | Inside saveUser, this line runs as written: setUser(u);. It happens in order, after the line above it and before the line below it.

  93 |     if (u) {
     | This asks a yes-or-no question. The next bit runs only on yes.

  94 |       localStorage.setItem("user", JSON.stringify(u));
     | This looks in the browser's pocket, or puts something there, so it is still around after a refresh.

  95 |     } else {
     | This ends if (u) { (opened on line 93).

  96 |       localStorage.removeItem("user");
     | This looks in the browser's pocket, or puts something there, so it is still around after a refresh.

  97 |     }
     | This ends } else { (opened on line 95).

  98 |   }
     | This ends saveUser (opened on line 91).

  99 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 100 |   // Update user profile via API and sync local state
     | A note written for people. The app does not run it.

 101 |   async function updateUser(data) {
     | This starts updateUser. PUT /profile via updateProfile, then merges the response onto the stored user.

 102 |     const updated = await updateProfile(data);
     | This gives a short name to a value so the rest of updateUser can use it.

 103 |     saveUser({ ...user, ...updated });
     | This ends updateUser (opened on line 101).

 104 |     return updated;
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

 105 |   }
     | This ends updateUser (opened on line 101).

 106 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 107 |   return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

 108 |     <ctx.Provider value={{ user, setUser: saveUser, updateUser, token, setToken: saveToken, loading }}>
     | This draws one piece of the page while UserProvider is showing.

 109 |       {children}
     | This ends UserProvider (opened on line 27).

 110 |     </ctx.Provider>
     | This ends a drawing that UserProvider started just above.

 111 |   );
     | This closes a box of instructions that opened above.

 112 | }
     | This ends UserProvider (opened on line 27).

 113 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

