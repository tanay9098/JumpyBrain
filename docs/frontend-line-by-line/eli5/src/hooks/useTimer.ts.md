# `src/hooks/useTimer.ts`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import { useEffect } from 'react'
     | Borrows React so this file can remember things and draw the screen.

   2 | import { useTimerStore } from '../stores/timerStore'
     | This file borrows a tool another file already made.

   3 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   4 | export function useTimer() {
     | This lets another file use this piece by its name.

   5 |   const { isRunning, tick } = useTimerStore()
     | This gives a short name to a value so the rest of useTimer can use it.

   6 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   7 |   useEffect(() => {
     | This is an extra job that happens after the picture is drawn.

   8 |     if (!isRunning) return
     | This asks a yes-or-no question. The next bit runs only on yes.

   9 |     const id = setInterval(tick, 1000)
     | This gives a short name to a value so the rest of useTimer can use it.

  10 |     return () => clearInterval(id)
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  11 |   }, [isRunning, tick])
     | This ends effect in useTimer (opened on line 7).

  12 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  13 |   return useTimerStore()
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  14 | }
     | This ends useTimer (opened on line 4).

