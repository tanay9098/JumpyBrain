# `src/services/sse.ts`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | export function createSSEStream(
     | Named export from a helper that reads a streaming AI response: `export function createSSEStream(`.

   2 |   url: string,
     | In `the top of the file` (src/services/sse.ts): statement `url: string,`. It runs when the top of the file runs, in order, before the next line of the same function.

   3 |   onChunk: (text: string) => void,
     | In `the top of the file` (src/services/sse.ts): statement `onChunk: (text: string) => void,`. It runs when the top of the file runs, in order, before the next line of the same function.

   4 |   onDone: () => void,
     | In `the top of the file` (src/services/sse.ts): statement `onDone: () => void,`. It runs when the top of the file runs, in order, before the next line of the same function.

   5 |   onError: (err: Error) => void
     | In `the top of the file` (src/services/sse.ts): statement `onError: (err: Error) => void`. It runs when the top of the file runs, in order, before the next line of the same function.

   6 | ): () => void {
     | In `the top of the file` (src/services/sse.ts): statement `): () => void {`. It runs when the top of the file runs, in order, before the next line of the same function.

   7 |   const controller = new AbortController()
     | In `the top of the file` (src/services/sse.ts): `controller` is assigned `new AbortController()`. Later lines in this function read that name.

   8 |   const token = localStorage.getItem('accessToken')
     | In `the top of the file` (src/services/sse.ts): `token`: The access token in React state. The copy that Axios actually sends is localStorage accessToken, written by saveToken. The code is `const token = localStorage.getItem('accessToken')`.

   9 | 
     | Blank line in `src/services/sse.ts` (a helper that reads a streaming AI response), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  10 |   fetch(`${import.meta.env.VITE_API_URL || 'http://localhost:4000/api'}${url}`, {
     | In `the top of the file` (src/services/sse.ts): `fetch(`${import.meta.env.VITE_API_URL || 'http://localhost:4000/api'}${url}`, {` closes ): () => void { (opened on line 6). Names declared inside that block end here.

  11 |     headers: { Authorization: `Bearer ${token}` },
     | In `the top of the file` (src/services/sse.ts): `headers: { Authorization: `Bearer ${token}` },` closes fetch(`${import.meta.env.VITE_API_URL || 'http:/ (opened on line 10). Names declared inside that block end here.

  12 |     signal: controller.signal,
     | In `the top of the file` (src/services/sse.ts): statement `signal: controller.signal,`. It runs when the top of the file runs, in order, before the next line of the same function.

  13 |   })
     | In `the top of the file` (src/services/sse.ts): `})` closes fetch(`${import.meta.env.VITE_API_URL || 'http:/ (opened on line 10). Names declared inside that block end here.

  14 |     .then(async (res) => {
     | In `the top of the file` (src/services/sse.ts): statement `.then(async (res) => {`. It runs when the top of the file runs, in order, before the next line of the same function.

  15 |       const reader = res.body!.getReader()
     | In `the top of the file` (src/services/sse.ts): `reader` is assigned `res.body!.getReader()`. Later lines in this function read that name.

  16 |       const decoder = new TextDecoder()
     | In `the top of the file` (src/services/sse.ts): `decoder` is assigned `new TextDecoder()`. Later lines in this function read that name.

  17 |       while (true) {
     | In `the top of the file` (src/services/sse.ts): iteration `while (true) {`.

  18 |         const { done, value } = await reader.read()
     | In `the top of the file` (src/services/sse.ts): `done, value` is assigned `await reader.read()`. Later lines in this function read that name.

  19 |         if (done) { onDone(); break }
     | In `the top of the file` (src/services/sse.ts): branch `if (done) { onDone(); break }`. Only one side runs.

  20 |         const text = decoder.decode(value)
     | In `the top of the file` (src/services/sse.ts): `text` is assigned `decoder.decode(value)`. Later lines in this function read that name.

  21 |         const lines = text.split('\n')
     | In `the top of the file` (src/services/sse.ts): `lines` is assigned `text.split('\n')`. Later lines in this function read that name.

  22 |         for (const line of lines) {
     | In `the top of the file` (src/services/sse.ts): iteration `for (const line of lines) {`.

  23 |           if (line.startsWith('data: ')) {
     | In `the top of the file` (src/services/sse.ts): branch `if (line.startsWith('data: ')) {`. Only one side runs.

  24 |             const data = line.slice(6)
     | In `the top of the file` (src/services/sse.ts): `data` is assigned `line.slice(6)`. Later lines in this function read that name.

  25 |             if (data === '[DONE]') { onDone(); return }
     | In `the top of the file` (src/services/sse.ts): branch `if (data === '[DONE]') { onDone(); return }`. Only one side runs.

  26 |             try {
     | In `the top of the file` (src/services/sse.ts): error path `try {`.

  27 |               const parsed = JSON.parse(data)
     | In `the top of the file` (src/services/sse.ts): `parsed` is assigned `JSON.parse(data)`. Later lines in this function read that name.

  28 |               onChunk(parsed.text || '')
     | In `the top of the file` (src/services/sse.ts): statement `onChunk(parsed.text || '')`. It runs when the top of the file runs, in order, before the next line of the same function.

  29 |             } catch {}
     | In `the top of the file` (src/services/sse.ts): `} catch {}` closes try { (opened on line 26). Names declared inside that block end here.

  30 |           }
     | In `the top of the file` (src/services/sse.ts): `}` closes if (line.startsWith('data: ')) { (opened on line 23). Names declared inside that block end here.

  31 |         }
     | In `the top of the file` (src/services/sse.ts): `}` closes for (const line of lines) { (opened on line 22). Names declared inside that block end here.

  32 |       }
     | In `the top of the file` (src/services/sse.ts): `}` closes while (true) { (opened on line 17). Names declared inside that block end here.

  33 |     })
     | In `the top of the file` (src/services/sse.ts): `})` closes .then(async (res) => { (opened on line 14). Names declared inside that block end here.

  34 |     .catch((err) => {
     | In `the top of the file` (src/services/sse.ts): statement `.catch((err) => {`. It runs when the top of the file runs, in order, before the next line of the same function.

  35 |       if (err.name !== 'AbortError') onError(err)
     | In `the top of the file` (src/services/sse.ts): branch `if (err.name !== 'AbortError') onError(err)`. Only one side runs.

  36 |     })
     | In `the top of the file` (src/services/sse.ts): `})` closes .catch((err) => { (opened on line 34). Names declared inside that block end here.

  37 | 
     | Blank line in `src/services/sse.ts` (a helper that reads a streaming AI response), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  38 |   return () => controller.abort()
     | In `the top of the file` (src/services/sse.ts): return `return () => controller.abort()`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  39 | }
     | In `the top of the file` (src/services/sse.ts): `}` closes ): () => void { (opened on line 6). Names declared inside that block end here.

