# `src/services/socket.ts`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import { io, Socket } from 'socket.io-client'
     | Borrows the live phone line to the server.

   2 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   3 | let socket: Socket | null = null
     | The single Socket.IO client. connectSocket sets auth.token and connects. disconnectSocket drops it on logout.

   4 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   5 | export const getSocket = (): Socket => {
     | This lets another file use this piece by its name.

   6 |   if (!socket) {
     | This asks a yes-or-no question. The next bit runs only on yes.

   7 |     socket = io(import.meta.env.VITE_API_URL?.replace('/api', '') || 'http://localhost:3001', {
     | Inside the top of the file, this line runs as written: socket = io(import.meta.env.VITE_API_URL?.replace('/api', '') || 'http://localhost:3001', {. It happens in order, after the line above it and before the line below it.

   8 |       withCredentials: true,
     | Inside the top of the file, this line runs as written: withCredentials: true,. It happens in order, after the line above it and before the line below it.

   9 |       autoConnect: false,
     | Inside the top of the file, this line runs as written: autoConnect: false,. It happens in order, after the line above it and before the line below it.

  10 |     })
     | This ends socket = io(import.meta.env.VITE_API_URL?.replac (opened on line 7).

  11 |   }
     | This ends if (!socket) { (opened on line 6).

  12 |   return socket
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  13 | }
     | This ends export const getSocket = (): Socket => { (opened on line 5).

  14 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  15 | export const connectSocket = (token: string) => {
     | This lets another file use this piece by its name.

  16 |   const s = getSocket()
     | This gives a short name to a value so the rest of the top of the file can use it.

  17 |   s.auth = { token }
     | This ends export const connectSocket = (token: string) =>  (opened on line 15).

  18 |   s.connect()
     | Inside the top of the file, this line runs as written: s.connect(). It happens in order, after the line above it and before the line below it.

  19 |   return s
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  20 | }
     | This ends export const connectSocket = (token: string) =>  (opened on line 15).

  21 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  22 | export const disconnectSocket = () => {
     | This lets another file use this piece by its name.

  23 |   socket?.disconnect()
     | Inside the top of the file, this line runs as written: socket?.disconnect(). It happens in order, after the line above it and before the line below it.

  24 |   socket = null
     | Inside the top of the file, this line runs as written: socket = null. It happens in order, after the line above it and before the line below it.

  25 | }
     | This ends export const disconnectSocket = () => { (opened on line 22).

