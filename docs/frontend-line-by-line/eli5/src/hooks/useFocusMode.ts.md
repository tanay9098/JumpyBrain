# `src/hooks/useFocusMode.ts`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import { useEffect, useRef } from 'react'
     | Borrows React so this file can remember things and draw the screen.

   2 | import { useFocusStore } from '../stores/focusStore'
     | This file borrows a tool another file already made.

   3 | import { getSocket } from '../services/socket'
     | This file borrows a tool another file already made.

   4 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   5 | export function useFocusMode() {
     | This lets another file use this piece by its name.

   6 |   const { setFocused } = useFocusStore()
     | This gives a short name to a value so the rest of useFocusMode can use it.

   7 |   const debounceRef = useRef<ReturnType<typeof setTimeout> | null>(null)
     | This gives a short name to a value so the rest of useFocusMode can use it.

   8 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   9 |   useEffect(() => {
     | This is an extra job that happens after the picture is drawn.

  10 |     const handleVisibilityChange = () => {
     | This gives a short name to a value so the rest of useFocusMode can use it.

  11 |       if (debounceRef.current) clearTimeout(debounceRef.current)
     | This asks a yes-or-no question. The next bit runs only on yes.

  12 |       debounceRef.current = setTimeout(() => {
     | Inside useFocusMode, this line runs as written: debounceRef.current = setTimeout(() => {. It happens in order, after the line above it and before the line below it.

  13 |         const focused = document.visibilityState === 'visible'
     | This gives a short name to a value so the rest of useFocusMode can use it.

  14 |         setFocused(focused)
     | Inside useFocusMode, this line runs as written: setFocused(focused). It happens in order, after the line above it and before the line below it.

  15 |         if (!focused) {
     | This asks a yes-or-no question. The next bit runs only on yes.

  16 |           getSocket().emit('FOCUS_LOST', { timestamp: Date.now() })
     | This ends if (!focused) { (opened on line 15).

  17 |         }
     | This ends if (!focused) { (opened on line 15).

  18 |       }, 800)
     | This ends debounceRef.current = setTimeout(() => { (opened on line 12).

  19 |     }
     | This ends const handleVisibilityChange = () => { (opened on line 10).

  20 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  21 |     const handleBlur = () => {
     | This gives a short name to a value so the rest of useFocusMode can use it.

  22 |       if (debounceRef.current) clearTimeout(debounceRef.current)
     | This asks a yes-or-no question. The next bit runs only on yes.

  23 |       debounceRef.current = setTimeout(() => {
     | Inside useFocusMode, this line runs as written: debounceRef.current = setTimeout(() => {. It happens in order, after the line above it and before the line below it.

  24 |         setFocused(false)
     | Inside useFocusMode, this line runs as written: setFocused(false). It happens in order, after the line above it and before the line below it.

  25 |         getSocket().emit('FOCUS_LOST', { timestamp: Date.now() })
     | This ends debounceRef.current = setTimeout(() => { (opened on line 23).

  26 |       }, 800)
     | This ends debounceRef.current = setTimeout(() => { (opened on line 23).

  27 |     }
     | This ends const handleBlur = () => { (opened on line 21).

  28 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  29 |     document.addEventListener('visibilitychange', handleVisibilityChange)
     | Inside useFocusMode, this line runs as written: document.addEventListener('visibilitychange', handleVisibilityChange). It happens in order, after the line above it and before the line below it.

  30 |     window.addEventListener('blur', handleBlur)
     | Inside useFocusMode, this line runs as written: window.addEventListener('blur', handleBlur). It happens in order, after the line above it and before the line below it.

  31 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  32 |     return () => {
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  33 |       document.removeEventListener('visibilitychange', handleVisibilityChange)
     | Inside useFocusMode, this line runs as written: document.removeEventListener('visibilitychange', handleVisibilityChange). It happens in order, after the line above it and before the line below it.

  34 |       window.removeEventListener('blur', handleBlur)
     | Inside useFocusMode, this line runs as written: window.removeEventListener('blur', handleBlur). It happens in order, after the line above it and before the line below it.

  35 |       if (debounceRef.current) clearTimeout(debounceRef.current)
     | This asks a yes-or-no question. The next bit runs only on yes.

  36 |     }
     | This ends return () => { (opened on line 32).

  37 |   }, [setFocused])
     | This ends effect in useFocusMode (opened on line 9).

  38 | }
     | This ends useFocusMode (opened on line 5).

