# `src/hooks/useFocusMode.ts`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import { useEffect, useRef } from 'react'
     | Import for an unused hook that emits FOCUS_LOST on the socket: `import { useEffect, useRef } from 'react'`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   2 | import { useFocusStore } from '../stores/focusStore'
     | Import for an unused hook that emits FOCUS_LOST on the socket: `import { useFocusStore } from '../stores/focusStore'`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   3 | import { getSocket } from '../services/socket'
     | Import for an unused hook that emits FOCUS_LOST on the socket: `import { getSocket } from '../services/socket'`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   4 | 
     | Blank line in `src/hooks/useFocusMode.ts` (an unused hook that emits FOCUS_LOST on the socket), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   5 | export function useFocusMode() {
     | Named export from an unused hook that emits FOCUS_LOST on the socket: `export function useFocusMode() {`.

   6 |   const { setFocused } = useFocusStore()
     | In `useFocusMode` (src/hooks/useFocusMode.ts): `setFocused` is assigned `useFocusStore()`. Later lines in this function read that name.

   7 |   const debounceRef = useRef<ReturnType<typeof setTimeout> | null>(null)
     | In `useFocusMode` (src/hooks/useFocusMode.ts): A ref `debounceRef`. `.current` survives re-renders and writing it does not re-render. `const debounceRef = useRef<ReturnType<typeof setTimeout> | null>(null)`

   8 | 
     | Blank line in `src/hooks/useFocusMode.ts` (an unused hook that emits FOCUS_LOST on the socket), inside useFocusMode. The parser skips it. It separates the previous statement from the next so the function is readable.

   9 |   useEffect(() => {
     | In `useFocusMode` (src/hooks/useFocusMode.ts): opens or continues an effect — `useEffect(() => {`. The effect body runs after paint, and its cleanup runs before the next effect and on unmount.

  10 |     const handleVisibilityChange = () => {
     | In `useFocusMode` (src/hooks/useFocusMode.ts): `handleVisibilityChange` is assigned `() => {`. Later lines in this function read that name.

  11 |       if (debounceRef.current) clearTimeout(debounceRef.current)
     | In `useFocusMode` (src/hooks/useFocusMode.ts): branch `if (debounceRef.current) clearTimeout(debounceRef.current)`. Only one side runs.

  12 |       debounceRef.current = setTimeout(() => {
     | In `useFocusMode` (src/hooks/useFocusMode.ts): timer — `debounceRef.current = setTimeout(() => {`. The callback runs later on the event loop, not now.

  13 |         const focused = document.visibilityState === 'visible'
     | In `useFocusMode` (src/hooks/useFocusMode.ts): `focused` is assigned `document.visibilityState === 'visible'`. Later lines in this function read that name.

  14 |         setFocused(focused)
     | In `useFocusMode` (src/hooks/useFocusMode.ts): statement `setFocused(focused)`. It runs when useFocusMode runs, in order, before the next line of the same function.

  15 |         if (!focused) {
     | In `useFocusMode` (src/hooks/useFocusMode.ts): branch `if (!focused) {`. Only one side runs.

  16 |           getSocket().emit('FOCUS_LOST', { timestamp: Date.now() })
     | In `useFocusMode` (src/hooks/useFocusMode.ts): `getSocket().emit('FOCUS_LOST', { timestamp: Date.now() })` closes if (!focused) { (opened on line 15). Names declared inside that block end here.

  17 |         }
     | In `useFocusMode` (src/hooks/useFocusMode.ts): `}` closes if (!focused) { (opened on line 15). Names declared inside that block end here.

  18 |       }, 800)
     | In `useFocusMode` (src/hooks/useFocusMode.ts): `}, 800)` closes debounceRef.current = setTimeout(() => { (opened on line 12). Names declared inside that block end here.

  19 |     }
     | In `useFocusMode` (src/hooks/useFocusMode.ts): `}` closes const handleVisibilityChange = () => { (opened on line 10). Names declared inside that block end here.

  20 | 
     | Blank line in `src/hooks/useFocusMode.ts` (an unused hook that emits FOCUS_LOST on the socket), inside useFocusMode. The parser skips it. It separates the previous statement from the next so the function is readable.

  21 |     const handleBlur = () => {
     | In `useFocusMode` (src/hooks/useFocusMode.ts): `handleBlur` is assigned `() => {`. Later lines in this function read that name.

  22 |       if (debounceRef.current) clearTimeout(debounceRef.current)
     | In `useFocusMode` (src/hooks/useFocusMode.ts): branch `if (debounceRef.current) clearTimeout(debounceRef.current)`. Only one side runs.

  23 |       debounceRef.current = setTimeout(() => {
     | In `useFocusMode` (src/hooks/useFocusMode.ts): timer — `debounceRef.current = setTimeout(() => {`. The callback runs later on the event loop, not now.

  24 |         setFocused(false)
     | In `useFocusMode` (src/hooks/useFocusMode.ts): statement `setFocused(false)`. It runs when useFocusMode runs, in order, before the next line of the same function.

  25 |         getSocket().emit('FOCUS_LOST', { timestamp: Date.now() })
     | In `useFocusMode` (src/hooks/useFocusMode.ts): `getSocket().emit('FOCUS_LOST', { timestamp: Date.now() })` closes debounceRef.current = setTimeout(() => { (opened on line 23). Names declared inside that block end here.

  26 |       }, 800)
     | In `useFocusMode` (src/hooks/useFocusMode.ts): `}, 800)` closes debounceRef.current = setTimeout(() => { (opened on line 23). Names declared inside that block end here.

  27 |     }
     | In `useFocusMode` (src/hooks/useFocusMode.ts): `}` closes const handleBlur = () => { (opened on line 21). Names declared inside that block end here.

  28 | 
     | Blank line in `src/hooks/useFocusMode.ts` (an unused hook that emits FOCUS_LOST on the socket), inside useFocusMode. The parser skips it. It separates the previous statement from the next so the function is readable.

  29 |     document.addEventListener('visibilitychange', handleVisibilityChange)
     | In `useFocusMode` (src/hooks/useFocusMode.ts): The browser fires this when the tab is hidden or shown. FocusOverlay uses it for the 800ms nudge. Mindfulness uses it to stop audio.

  30 |     window.addEventListener('blur', handleBlur)
     | In `useFocusMode` (src/hooks/useFocusMode.ts): statement `window.addEventListener('blur', handleBlur)`. It runs when useFocusMode runs, in order, before the next line of the same function.

  31 | 
     | Blank line in `src/hooks/useFocusMode.ts` (an unused hook that emits FOCUS_LOST on the socket), inside useFocusMode. The parser skips it. It separates the previous statement from the next so the function is readable.

  32 |     return () => {
     | In `useFocusMode` (src/hooks/useFocusMode.ts): return `return () => {`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  33 |       document.removeEventListener('visibilitychange', handleVisibilityChange)
     | In `useFocusMode` (src/hooks/useFocusMode.ts): The browser fires this when the tab is hidden or shown. FocusOverlay uses it for the 800ms nudge. Mindfulness uses it to stop audio.

  34 |       window.removeEventListener('blur', handleBlur)
     | In `useFocusMode` (src/hooks/useFocusMode.ts): statement `window.removeEventListener('blur', handleBlur)`. It runs when useFocusMode runs, in order, before the next line of the same function.

  35 |       if (debounceRef.current) clearTimeout(debounceRef.current)
     | In `useFocusMode` (src/hooks/useFocusMode.ts): branch `if (debounceRef.current) clearTimeout(debounceRef.current)`. Only one side runs.

  36 |     }
     | In `useFocusMode` (src/hooks/useFocusMode.ts): `}` closes return () => { (opened on line 32). Names declared inside that block end here.

  37 |   }, [setFocused])
     | In `useFocusMode` (src/hooks/useFocusMode.ts): `}, [setFocused])` closes effect in useFocusMode (opened on line 9). Names declared inside that block end here.

  38 | }
     | In `useFocusMode` (src/hooks/useFocusMode.ts): `}` closes useFocusMode (opened on line 5). Names declared inside that block end here.

