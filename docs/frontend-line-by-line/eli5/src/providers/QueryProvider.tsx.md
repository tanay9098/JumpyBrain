# `src/providers/QueryProvider.tsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
     | Borrows React so this file can remember things and draw the screen.

   2 | import { ReactNode } from 'react'
     | Borrows React so this file can remember things and draw the screen.

   3 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   4 | export const queryClient = new QueryClient({
     | This lets another file use this piece by its name.

   5 |   defaultOptions: {
     | Inside the top of the file, this line runs as written: defaultOptions: {. It happens in order, after the line above it and before the line below it.

   6 |     queries: {
     | Inside the top of the file, this line runs as written: queries: {. It happens in order, after the line above it and before the line below it.

   7 |       staleTime: 1000 * 60,
     | Inside the top of the file, this line runs as written: staleTime: 1000 * 60,. It happens in order, after the line above it and before the line below it.

   8 |       retry: 1,
     | Inside the top of the file, this line runs as written: retry: 1,. It happens in order, after the line above it and before the line below it.

   9 |     },
     | This ends queries: { (opened on line 6).

  10 |   },
     | This ends defaultOptions: { (opened on line 5).

  11 | })
     | This ends export const queryClient = new QueryClient({ (opened on line 4).

  12 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  13 | export function QueryProvider({ children }: { children: ReactNode }) {
     | This lets another file use this piece by its name.

  14 |   return <QueryClientProvider client={queryClient}>{children}</QueryClientProvider>
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  15 | }
     | This ends QueryProvider (opened on line 13).

