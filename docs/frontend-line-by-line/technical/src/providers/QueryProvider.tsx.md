# `src/providers/QueryProvider.tsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
     | Import for a React Query cache that the screens do not mount: `import { QueryClient, QueryClientProvider } from '@tanstack/react-query'`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   2 | import { ReactNode } from 'react'
     | Import for a React Query cache that the screens do not mount: `import { ReactNode } from 'react'`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   3 | 
     | Blank line in `src/providers/QueryProvider.tsx` (a React Query cache that the screens do not mount), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   4 | export const queryClient = new QueryClient({
     | Named export from a React Query cache that the screens do not mount: `export const queryClient = new QueryClient({`.

   5 |   defaultOptions: {
     | In `the top of the file` (src/providers/QueryProvider.tsx): statement `defaultOptions: {`. It runs when the top of the file runs, in order, before the next line of the same function.

   6 |     queries: {
     | In `the top of the file` (src/providers/QueryProvider.tsx): statement `queries: {`. It runs when the top of the file runs, in order, before the next line of the same function.

   7 |       staleTime: 1000 * 60,
     | In `the top of the file` (src/providers/QueryProvider.tsx): React Query would treat data as fresh for 60 seconds. No screen reads this cache. Code: `staleTime: 1000 * 60,`.

   8 |       retry: 1,
     | In `the top of the file` (src/providers/QueryProvider.tsx): React Query would retry a failed query once. Code: `retry: 1,`.

   9 |     },
     | In `the top of the file` (src/providers/QueryProvider.tsx): `},` closes queries: { (opened on line 6). Names declared inside that block end here.

  10 |   },
     | In `the top of the file` (src/providers/QueryProvider.tsx): `},` closes defaultOptions: { (opened on line 5). Names declared inside that block end here.

  11 | })
     | In `the top of the file` (src/providers/QueryProvider.tsx): `})` closes export const queryClient = new QueryClient({ (opened on line 4). Names declared inside that block end here.

  12 | 
     | Blank line in `src/providers/QueryProvider.tsx` (a React Query cache that the screens do not mount), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  13 | export function QueryProvider({ children }: { children: ReactNode }) {
     | Named export from a React Query cache that the screens do not mount: `export function QueryProvider({ children }: { children: ReactNode }) {`.

  14 |   return <QueryClientProvider client={queryClient}>{children}</QueryClientProvider>
     | In `QueryProvider` (src/providers/QueryProvider.tsx): return `return <QueryClientProvider client={queryClient}>{children}</QueryClientProvider>`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  15 | }
     | In `QueryProvider` (src/providers/QueryProvider.tsx): `}` closes QueryProvider (opened on line 13). Names declared inside that block end here.

