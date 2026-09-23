# `src/services/api.ts`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import axios from 'axios'
     | Borrows the mail carrier that talks to the server.

   2 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   3 | const api = axios.create({
     | Creates the one Axios client every screen imports. baseURL is VITE_API_URL or http://localhost:4000/api. withCredentials sends cookies so /auth/refresh can read the refresh cookie.

   4 |   baseURL: import.meta.env.VITE_API_URL || 'http://localhost:4000/api',
     | Inside the top of the file, this line runs as written: baseURL: import.meta.env.VITE_API_URL || 'http://localhost:4000/api',. It happens in order, after the line above it and before the line below it.

   5 |   withCredentials: true,
     | Inside the top of the file, this line runs as written: withCredentials: true,. It happens in order, after the line above it and before the line below it.

   6 | })
     | This ends const api = axios.create({ (opened on line 3).

   7 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   8 | api.interceptors.request.use((config) => {
     | This asks the server (the office that keeps tasks and accounts) for something, or sends it something.

   9 |   const token = localStorage.getItem('accessToken')
     | The access token in React state. The copy that Axios actually sends is localStorage accessToken, written by saveToken.

  10 |   if (token) config.headers.Authorization = `Bearer ${token}`
     | This asks a yes-or-no question. The next bit runs only on yes.

  11 |   return config
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  12 | })
     | This ends api.interceptors.request.use((config) => { (opened on line 8).

  13 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  14 | api.interceptors.response.use(
     | This asks the server (the office that keeps tasks and accounts) for something, or sends it something.

  15 |   (res) => res.data,
     | Inside the top of the file, this line runs as written: (res) => res.data,. It happens in order, after the line above it and before the line below it.

  16 |   async (err) => {
     | Inside the top of the file, this line runs as written: async (err) => {. It happens in order, after the line above it and before the line below it.

  17 |     if (err.response?.status === 401) {
     | This asks a yes-or-no question. The next bit runs only on yes.

  18 |       try {
     | Inside the top of the file, this line runs as written: try {. It happens in order, after the line above it and before the line below it.

  19 |         const { data } = await axios.post(
     | This gives a short name to a value so the rest of the top of the file can use it.

  20 |           `${import.meta.env.VITE_API_URL || 'http://localhost:4000/api'}/auth/refresh`,
     | This ends try { (opened on line 18).

  21 |           {},
     | This ends try { (opened on line 18).

  22 |           { withCredentials: true }
     | This ends try { (opened on line 18).

  23 |         )
     | This closes a box of instructions that opened above.

  24 |         localStorage.setItem('accessToken', data.accessToken)
     | This looks in the browser's pocket, or puts something there, so it is still around after a refresh.

  25 |         err.config.headers.Authorization = `Bearer ${data.accessToken}`
     | This ends try { (opened on line 18).

  26 |         return api.request(err.config)
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  27 |       } catch {
     | This ends try { (opened on line 18).

  28 |         localStorage.removeItem('accessToken')
     | This looks in the browser's pocket, or puts something there, so it is still around after a refresh.

  29 |         window.location.href = '/auth'
     | Inside the top of the file, this line runs as written: window.location.href = '/auth'. It happens in order, after the line above it and before the line below it.

  30 |       }
     | This ends } catch { (opened on line 27).

  31 |     }
     | This ends if (err.response?.status === 401) { (opened on line 17).

  32 |     return Promise.reject(err)
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  33 |   }
     | This ends async (err) => { (opened on line 16).

  34 | )
     | This closes a box of instructions that opened above.

  35 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  36 | export const getProfile = () => api.get('/profile')
     | This lets another file use this piece by its name.

  37 | export const updateProfile = (data: { name?: string; gender?: string; email?: string; preferredTheme?: string }) =>
     | This lets another file use this piece by its name.

  38 |   api.put('/profile', data)
     | This asks the server (the office that keeps tasks and accounts) for something, or sends it something.

  39 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  40 | export default api
     | This tells other files: the main thing in this file is this.

