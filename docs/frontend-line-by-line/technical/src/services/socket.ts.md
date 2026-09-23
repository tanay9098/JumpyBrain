# `src/services/socket.ts`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import { io, Socket } from 'socket.io-client'
     | Import for the live socket opened after login: `import { io, Socket } from 'socket.io-client'`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   2 | 
     | Blank line in `src/services/socket.ts` (the live socket opened after login), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   3 | let socket: Socket | null = null
     | In `the top of the file` (src/services/socket.ts): declaration `let socket: Socket | null = null`.

   4 | 
     | Blank line in `src/services/socket.ts` (the live socket opened after login), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   5 | export const getSocket = (): Socket => {
     | Named export from the live socket opened after login: `export const getSocket = (): Socket => {`.

   6 |   if (!socket) {
     | In `the top of the file` (src/services/socket.ts): branch `if (!socket) {`. Only one side runs.

   7 |     socket = io(import.meta.env.VITE_API_URL?.replace('/api', '') || 'http://localhost:3001', {
     | In `the top of the file` (src/services/socket.ts): statement `socket = io(import.meta.env.VITE_API_URL?.replace('/api', '') || 'http://localhost:3001', {`. It runs when the top of the file runs, in order, before the next line of the same function.

   8 |       withCredentials: true,
     | In `the top of the file` (src/services/socket.ts): Send cookies. The refresh call needs the httpOnly refresh cookie, which JavaScript cannot read but the browser will attach. Code: `withCredentials: true,`.

   9 |       autoConnect: false,
     | In `the top of the file` (src/services/socket.ts): The socket is created quiet. connectSocket() is what actually connects, and only after a token exists. Code: `autoConnect: false,`.

  10 |     })
     | In `the top of the file` (src/services/socket.ts): `})` closes socket = io(import.meta.env.VITE_API_URL?.replac (opened on line 7). Names declared inside that block end here.

  11 |   }
     | In `the top of the file` (src/services/socket.ts): `}` closes if (!socket) { (opened on line 6). Names declared inside that block end here.

  12 |   return socket
     | In `the top of the file` (src/services/socket.ts): return `return socket`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  13 | }
     | In `the top of the file` (src/services/socket.ts): `}` closes export const getSocket = (): Socket => { (opened on line 5). Names declared inside that block end here.

  14 | 
     | Blank line in `src/services/socket.ts` (the live socket opened after login), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  15 | export const connectSocket = (token: string) => {
     | Named export from the live socket opened after login: `export const connectSocket = (token: string) => {`.

  16 |   const s = getSocket()
     | In `the top of the file` (src/services/socket.ts): `s` is assigned `getSocket()`. Later lines in this function read that name.

  17 |   s.auth = { token }
     | In `the top of the file` (src/services/socket.ts): `s.auth = { token }` closes export const connectSocket = (token: string) =>  (opened on line 15). Names declared inside that block end here.

  18 |   s.connect()
     | In `the top of the file` (src/services/socket.ts): statement `s.connect()`. It runs when the top of the file runs, in order, before the next line of the same function.

  19 |   return s
     | In `the top of the file` (src/services/socket.ts): return `return s`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  20 | }
     | In `the top of the file` (src/services/socket.ts): `}` closes export const connectSocket = (token: string) =>  (opened on line 15). Names declared inside that block end here.

  21 | 
     | Blank line in `src/services/socket.ts` (the live socket opened after login), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  22 | export const disconnectSocket = () => {
     | Named export from the live socket opened after login: `export const disconnectSocket = () => {`.

  23 |   socket?.disconnect()
     | In `the top of the file` (src/services/socket.ts): statement `socket?.disconnect()`. It runs when the top of the file runs, in order, before the next line of the same function.

  24 |   socket = null
     | In `the top of the file` (src/services/socket.ts): statement `socket = null`. It runs when the top of the file runs, in order, before the next line of the same function.

  25 | }
     | In `the top of the file` (src/services/socket.ts): `}` closes export const disconnectSocket = () => { (opened on line 22). Names declared inside that block end here.

