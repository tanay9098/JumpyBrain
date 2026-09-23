# `src/main.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import { StrictMode } from 'react'
     | Borrows React so this file can remember things and draw the screen.

   2 | import { createRoot } from 'react-dom/client'
     | Borrows React so this file can remember things and draw the screen.

   3 | import { BrowserRouter } from 'react-router-dom';
     | Borrows React so this file can remember things and draw the screen.

   4 | import './styles.css'
     | Loads the paint for the whole app.

   5 | import App from './App.jsx'
     | Gets the hallway that holds every room.

   6 | import { UserProvider } from './contexts/UserContext.jsx'
     | Gets the name-tag keeper.

   7 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   8 | createRoot(document.getElementById('root')).render(
     | Inside the top of the file, this line runs as written: createRoot(document.getElementById('root')).render(. It happens in order, after the line above it and before the line below it.

   9 |   <StrictMode>
     | This draws one piece of the page while the top of the file is showing.

  10 |     <BrowserRouter>
     | This draws one piece of the page while the top of the file is showing.

  11 |       <UserProvider>
     | This draws one piece of the page while the top of the file is showing.

  12 |         <App />
     | This draws one piece of the page while the top of the file is showing.

  13 |       </UserProvider>
     | This ends a drawing that the top of the file started just above.

  14 |     </BrowserRouter>
     | This ends a drawing that the top of the file started just above.

  15 |   </StrictMode>,
     | This ends a drawing that the top of the file started just above.

  16 | )
     | This closes a box of instructions that opened above.

