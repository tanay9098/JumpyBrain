# `src/services/api.ts`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import axios from 'axios'
     | Import for the HTTP client every page uses to reach the backend: `import axios from 'axios'`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   2 | 
     | Blank line in `src/services/api.ts` (the HTTP client every page uses to reach the backend), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   3 | const api = axios.create({
     | In `the top of the file` (src/services/api.ts): `api`: Creates the one Axios client every screen imports. baseURL is VITE_API_URL or http://localhost:4000/api. withCredentials sends cookies so /auth/refresh can read the refresh cookie. The code is `const api = axios.create({`.

   4 |   baseURL: import.meta.env.VITE_API_URL || 'http://localhost:4000/api',
     | In `the top of the file` (src/services/api.ts): Prefix for every relative request. VITE_API_URL if set, otherwise http://localhost:4000/api. A call api.get('/tasks') therefore hits that host plus /tasks. Code: `baseURL: import.meta.env.VITE_API_URL || 'http://localhost:4000/api',`.

   5 |   withCredentials: true,
     | In `the top of the file` (src/services/api.ts): Send cookies. The refresh call needs the httpOnly refresh cookie, which JavaScript cannot read but the browser will attach. Code: `withCredentials: true,`.

   6 | })
     | In `the top of the file` (src/services/api.ts): `})` closes const api = axios.create({ (opened on line 3). Names declared inside that block end here.

   7 | 
     | Blank line in `src/services/api.ts` (the HTTP client every page uses to reach the backend), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   8 | api.interceptors.request.use((config) => {
     | In `the top of the file` (src/services/api.ts): Registers a function that runs before every request. It will copy accessToken from localStorage onto the Authorization header.

   9 |   const token = localStorage.getItem('accessToken')
     | In `the top of the file` (src/services/api.ts): `token`: The access token in React state. The copy that Axios actually sends is localStorage accessToken, written by saveToken. The code is `const token = localStorage.getItem('accessToken')`.

  10 |   if (token) config.headers.Authorization = `Bearer ${token}`
     | In `the top of the file` (src/services/api.ts): branch `if (token) config.headers.Authorization = `Bearer ${token}``. Only one side runs.

  11 |   return config
     | In `the top of the file` (src/services/api.ts): return `return config`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  12 | })
     | In `the top of the file` (src/services/api.ts): `})` closes api.interceptors.request.use((config) => { (opened on line 8). Names declared inside that block end here.

  13 | 
     | Blank line in `src/services/api.ts` (the HTTP client every page uses to reach the backend), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  14 | api.interceptors.response.use(
     | In `the top of the file` (src/services/api.ts): Registers success and error handlers for every response. Success returns res.data so callers do not see the Axios wrapper.

  15 |   (res) => res.data,
     | In `the top of the file` (src/services/api.ts): Success path of the response interceptor. Unwraps the JSON body. That is why Home can use the return value directly.

  16 |   async (err) => {
     | In `the top of the file` (src/services/api.ts): statement `async (err) => {`. It runs when the top of the file runs, in order, before the next line of the same function.

  17 |     if (err.response?.status === 401) {
     | In `the top of the file` (src/services/api.ts): branch `if (err.response?.status === 401) {`. Only one side runs.

  18 |       try {
     | In `the top of the file` (src/services/api.ts): error path `try {`.

  19 |         const { data } = await axios.post(
     | In `the top of the file` (src/services/api.ts): `data` is assigned `await axios.post(`. Later lines in this function read that name.

  20 |           `${import.meta.env.VITE_API_URL || 'http://localhost:4000/api'}/auth/refresh`,
     | In `the top of the file` (src/services/api.ts): ``${import.meta.env.VITE_API_URL || 'http://localhost:4000/api'}/auth/refresh`,` closes try { (opened on line 18). Names declared inside that block end here.

  21 |           {},
     | In `the top of the file` (src/services/api.ts): `{},` closes try { (opened on line 18). Names declared inside that block end here.

  22 |           { withCredentials: true }
     | In `the top of the file` (src/services/api.ts): `{ withCredentials: true }` closes try { (opened on line 18). Names declared inside that block end here.

  23 |         )
     | In `the top of the file` (src/services/api.ts): statement `)`. It runs when the top of the file runs, in order, before the next line of the same function.

  24 |         localStorage.setItem('accessToken', data.accessToken)
     | In `the top of the file` (src/services/api.ts): browser storage — `localStorage.setItem('accessToken', data.accessToken)`. This survives reloads on this origin and is shared by any script that uses the same key.

  25 |         err.config.headers.Authorization = `Bearer ${data.accessToken}`
     | In `the top of the file` (src/services/api.ts): `err.config.headers.Authorization = `Bearer ${data.accessToken}`` closes try { (opened on line 18). Names declared inside that block end here.

  26 |         return api.request(err.config)
     | In `the top of the file` (src/services/api.ts): return `return api.request(err.config)`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  27 |       } catch {
     | In `the top of the file` (src/services/api.ts): `} catch {` closes try { (opened on line 18). Names declared inside that block end here.

  28 |         localStorage.removeItem('accessToken')
     | In `the top of the file` (src/services/api.ts): browser storage — `localStorage.removeItem('accessToken')`. This survives reloads on this origin and is shared by any script that uses the same key.

  29 |         window.location.href = '/auth'
     | In `the top of the file` (src/services/api.ts): Refresh failed. Drop the token and send the browser to the sign-in route.

  30 |       }
     | In `the top of the file` (src/services/api.ts): `}` closes } catch { (opened on line 27). Names declared inside that block end here.

  31 |     }
     | In `the top of the file` (src/services/api.ts): `}` closes if (err.response?.status === 401) { (opened on line 17). Names declared inside that block end here.

  32 |     return Promise.reject(err)
     | In `the top of the file` (src/services/api.ts): return `return Promise.reject(err)`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  33 |   }
     | In `the top of the file` (src/services/api.ts): `}` closes async (err) => { (opened on line 16). Names declared inside that block end here.

  34 | )
     | In `the top of the file` (src/services/api.ts): statement `)`. It runs when the top of the file runs, in order, before the next line of the same function.

  35 | 
     | Blank line in `src/services/api.ts` (the HTTP client every page uses to reach the backend), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  36 | export const getProfile = () => api.get('/profile')
     | Named export from the HTTP client every page uses to reach the backend: `export const getProfile = () => api.get('/profile')`.

  37 | export const updateProfile = (data: { name?: string; gender?: string; email?: string; preferredTheme?: string }) =>
     | Named export from the HTTP client every page uses to reach the backend: `export const updateProfile = (data: { name?: string; gender?: string; email?: string; preferredTheme?: string }) =>`.

  38 |   api.put('/profile', data)
     | In `the top of the file` (src/services/api.ts): HTTP via the shared Axios instance — `api.put('/profile', data)`. The request interceptor adds `Authorization: Bearer <accessToken>`. The response interceptor returns `res.data`, so the awaited value is the JSON body.

  39 | 
     | Blank line in `src/services/api.ts` (the HTTP client every page uses to reach the backend), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  40 | export default api
     | Default export of the HTTP client every page uses to reach the backend: `export default api`. Importers that write `import X from 'src/services/api.ts'` receive this value.

