# `src/services/sse.ts`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | export function createSSEStream(
     | This lets another file use this piece by its name.

   2 |   url: string,
     | Inside the top of the file, this line runs as written: url: string,. It happens in order, after the line above it and before the line below it.

   3 |   onChunk: (text: string) => void,
     | Inside the top of the file, this line runs as written: onChunk: (text: string) => void,. It happens in order, after the line above it and before the line below it.

   4 |   onDone: () => void,
     | Inside the top of the file, this line runs as written: onDone: () => void,. It happens in order, after the line above it and before the line below it.

   5 |   onError: (err: Error) => void
     | Inside the top of the file, this line runs as written: onError: (err: Error) => void. It happens in order, after the line above it and before the line below it.

   6 | ): () => void {
     | This closes a box of instructions that opened above.

   7 |   const controller = new AbortController()
     | This gives a short name to a value so the rest of the top of the file can use it.

   8 |   const token = localStorage.getItem('accessToken')
     | The access token in React state. The copy that Axios actually sends is localStorage accessToken, written by saveToken.

   9 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  10 |   fetch(`${import.meta.env.VITE_API_URL || 'http://localhost:4000/api'}${url}`, {
     | This ends ): () => void { (opened on line 6).

  11 |     headers: { Authorization: `Bearer ${token}` },
     | This ends fetch(`${import.meta.env.VITE_API_URL || 'http:/ (opened on line 10).

  12 |     signal: controller.signal,
     | Inside the top of the file, this line runs as written: signal: controller.signal,. It happens in order, after the line above it and before the line below it.

  13 |   })
     | This ends fetch(`${import.meta.env.VITE_API_URL || 'http:/ (opened on line 10).

  14 |     .then(async (res) => {
     | Inside the top of the file, this line runs as written: .then(async (res) => {. It happens in order, after the line above it and before the line below it.

  15 |       const reader = res.body!.getReader()
     | This gives a short name to a value so the rest of the top of the file can use it.

  16 |       const decoder = new TextDecoder()
     | This gives a short name to a value so the rest of the top of the file can use it.

  17 |       while (true) {
     | Inside the top of the file, this line runs as written: while (true) {. It happens in order, after the line above it and before the line below it.

  18 |         const { done, value } = await reader.read()
     | This gives a short name to a value so the rest of the top of the file can use it.

  19 |         if (done) { onDone(); break }
     | This asks a yes-or-no question. The next bit runs only on yes.

  20 |         const text = decoder.decode(value)
     | This gives a short name to a value so the rest of the top of the file can use it.

  21 |         const lines = text.split('\n')
     | This gives a short name to a value so the rest of the top of the file can use it.

  22 |         for (const line of lines) {
     | Inside the top of the file, this line runs as written: for (const line of lines) {. It happens in order, after the line above it and before the line below it.

  23 |           if (line.startsWith('data: ')) {
     | This asks a yes-or-no question. The next bit runs only on yes.

  24 |             const data = line.slice(6)
     | This gives a short name to a value so the rest of the top of the file can use it.

  25 |             if (data === '[DONE]') { onDone(); return }
     | This asks a yes-or-no question. The next bit runs only on yes.

  26 |             try {
     | Inside the top of the file, this line runs as written: try {. It happens in order, after the line above it and before the line below it.

  27 |               const parsed = JSON.parse(data)
     | This gives a short name to a value so the rest of the top of the file can use it.

  28 |               onChunk(parsed.text || '')
     | Inside the top of the file, this line runs as written: onChunk(parsed.text || ''). It happens in order, after the line above it and before the line below it.

  29 |             } catch {}
     | This ends try { (opened on line 26).

  30 |           }
     | This ends if (line.startsWith('data: ')) { (opened on line 23).

  31 |         }
     | This ends for (const line of lines) { (opened on line 22).

  32 |       }
     | This ends while (true) { (opened on line 17).

  33 |     })
     | This ends .then(async (res) => { (opened on line 14).

  34 |     .catch((err) => {
     | Inside the top of the file, this line runs as written: .catch((err) => {. It happens in order, after the line above it and before the line below it.

  35 |       if (err.name !== 'AbortError') onError(err)
     | This asks a yes-or-no question. The next bit runs only on yes.

  36 |     })
     | This ends .catch((err) => { (opened on line 34).

  37 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  38 |   return () => controller.abort()
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  39 | }
     | This ends ): () => void { (opened on line 6).

