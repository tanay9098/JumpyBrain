# `src/hooks/useAIStream.ts`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import { useState, useCallback } from 'react'
     | Borrows React so this file can remember things and draw the screen.

   2 | import { createSSEStream } from '../services/sse'
     | This file borrows a tool another file already made.

   3 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   4 | export function useAIStream() {
     | This lets another file use this piece by its name.

   5 |   const [text, setText] = useState('')
     | This gives a short name to a value so the rest of useAIStream can use it.

   6 |   const [loading, setLoading] = useState(false)
     | True until UserProvider finishes the first localStorage read. ProtectedRoute renders nothing during that moment so Auth does not flash.

   7 |   const [error, setError] = useState<string | null>(null)
     | This gives a short name to a value so the rest of useAIStream can use it.

   8 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   9 |   const stream = useCallback((prompt: string) => {
     | This gives a short name to a value so the rest of useAIStream can use it.

  10 |     setText('')
     | Inside useAIStream, this line runs as written: setText(''). It happens in order, after the line above it and before the line below it.

  11 |     setLoading(true)
     | Inside useAIStream, this line runs as written: setLoading(true). It happens in order, after the line above it and before the line below it.

  12 |     setError(null)
     | Inside useAIStream, this line runs as written: setError(null). It happens in order, after the line above it and before the line below it.

  13 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  14 |     const cancel = createSSEStream(
     | This gives a short name to a value so the rest of useAIStream can use it.

  15 |       `/ai/chat?prompt=${encodeURIComponent(prompt)}`,
     | This ends const stream = useCallback((prompt: string) => { (opened on line 9).

  16 |       (chunk) => setText((prev) => prev + chunk),
     | Inside useAIStream, this line runs as written: (chunk) => setText((prev) => prev + chunk),. It happens in order, after the line above it and before the line below it.

  17 |       () => setLoading(false),
     | Inside useAIStream, this line runs as written: () => setLoading(false),. It happens in order, after the line above it and before the line below it.

  18 |       (err) => { setError(err.message); setLoading(false) }
     | This ends const stream = useCallback((prompt: string) => { (opened on line 9).

  19 |     )
     | This closes a box of instructions that opened above.

  20 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  21 |     return cancel
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  22 |   }, [])
     | This ends const stream = useCallback((prompt: string) => { (opened on line 9).

  23 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  24 |   return { text, loading, error, stream }
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  25 | }
     | This ends useAIStream (opened on line 4).

