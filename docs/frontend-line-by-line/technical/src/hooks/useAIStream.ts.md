# `src/hooks/useAIStream.ts`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import { useState, useCallback } from 'react'
     | Import for an unused hook that streams /ai/chat: `import { useState, useCallback } from 'react'`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   2 | import { createSSEStream } from '../services/sse'
     | Import for an unused hook that streams /ai/chat: `import { createSSEStream } from '../services/sse'`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   3 | 
     | Blank line in `src/hooks/useAIStream.ts` (an unused hook that streams /ai/chat), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   4 | export function useAIStream() {
     | Named export from an unused hook that streams /ai/chat: `export function useAIStream() {`.

   5 |   const [text, setText] = useState('')
     | In `useAIStream` (src/hooks/useAIStream.ts): React state `text, setText`. The value survives re-renders. Calling the setter re-renders this component. `const [text, setText] = useState('')`

   6 |   const [loading, setLoading] = useState(false)
     | In `useAIStream` (src/hooks/useAIStream.ts): `loading`: True until UserProvider finishes the first localStorage read. ProtectedRoute renders nothing during that moment so Auth does not flash. The code is `const [loading, setLoading] = useState(false)`.

   7 |   const [error, setError] = useState<string | null>(null)
     | In `useAIStream` (src/hooks/useAIStream.ts): React state `error, setError`. The value survives re-renders. Calling the setter re-renders this component. `const [error, setError] = useState<string | null>(null)`

   8 | 
     | Blank line in `src/hooks/useAIStream.ts` (an unused hook that streams /ai/chat), inside useAIStream. The parser skips it. It separates the previous statement from the next so the function is readable.

   9 |   const stream = useCallback((prompt: string) => {
     | In `useAIStream` (src/hooks/useAIStream.ts): A memoized function `stream`. `const stream = useCallback((prompt: string) => {`

  10 |     setText('')
     | In `useAIStream` (src/hooks/useAIStream.ts): statement `setText('')`. It runs when useAIStream runs, in order, before the next line of the same function.

  11 |     setLoading(true)
     | In `useAIStream` (src/hooks/useAIStream.ts): statement `setLoading(true)`. It runs when useAIStream runs, in order, before the next line of the same function.

  12 |     setError(null)
     | In `useAIStream` (src/hooks/useAIStream.ts): statement `setError(null)`. It runs when useAIStream runs, in order, before the next line of the same function.

  13 | 
     | Blank line in `src/hooks/useAIStream.ts` (an unused hook that streams /ai/chat), inside useAIStream. The parser skips it. It separates the previous statement from the next so the function is readable.

  14 |     const cancel = createSSEStream(
     | In `useAIStream` (src/hooks/useAIStream.ts): `cancel` is assigned `createSSEStream(`. Later lines in this function read that name.

  15 |       `/ai/chat?prompt=${encodeURIComponent(prompt)}`,
     | In `useAIStream` (src/hooks/useAIStream.ts): ``/ai/chat?prompt=${encodeURIComponent(prompt)}`,` closes const stream = useCallback((prompt: string) => { (opened on line 9). Names declared inside that block end here.

  16 |       (chunk) => setText((prev) => prev + chunk),
     | In `useAIStream` (src/hooks/useAIStream.ts): statement `(chunk) => setText((prev) => prev + chunk),`. It runs when useAIStream runs, in order, before the next line of the same function.

  17 |       () => setLoading(false),
     | In `useAIStream` (src/hooks/useAIStream.ts): statement `() => setLoading(false),`. It runs when useAIStream runs, in order, before the next line of the same function.

  18 |       (err) => { setError(err.message); setLoading(false) }
     | In `useAIStream` (src/hooks/useAIStream.ts): statement `(err) => { setError(err.message); setLoading(false) }`. It runs when useAIStream runs, in order, before the next line of the same function.

  19 |     )
     | In `useAIStream` (src/hooks/useAIStream.ts): statement `)`. It runs when useAIStream runs, in order, before the next line of the same function.

  20 | 
     | Blank line in `src/hooks/useAIStream.ts` (an unused hook that streams /ai/chat), inside useAIStream. The parser skips it. It separates the previous statement from the next so the function is readable.

  21 |     return cancel
     | In `useAIStream` (src/hooks/useAIStream.ts): return `return cancel`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  22 |   }, [])
     | In `useAIStream` (src/hooks/useAIStream.ts): `}, [])` closes const stream = useCallback((prompt: string) => { (opened on line 9). Names declared inside that block end here.

  23 | 
     | Blank line in `src/hooks/useAIStream.ts` (an unused hook that streams /ai/chat), inside useAIStream. The parser skips it. It separates the previous statement from the next so the function is readable.

  24 |   return { text, loading, error, stream }
     | In `useAIStream` (src/hooks/useAIStream.ts): return `return { text, loading, error, stream }`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  25 | }
     | In `useAIStream` (src/hooks/useAIStream.ts): `}` closes useAIStream (opened on line 4). Names declared inside that block end here.

