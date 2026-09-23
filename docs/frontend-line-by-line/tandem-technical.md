# How the frontend files run together

Every line of every source file is annotated in the two folders next to this note:

- `technical/` — one markdown file per source file. Each source line is printed, then what that line does.
- `eli5/` — the same lines, explained simply.

This file is the call graph those lines sit in.

## Boot

1. `index.html` creates `<div id="root">` and loads `src/main.jsx` as a module. It also loads Google’s Identity Services script.
2. `main.jsx` imports `styles.css` (side effect: the browser applies it), then `createRoot(#root).render` of `StrictMode → BrowserRouter → UserProvider → App`.
3. `vite.config.ts` is not imported by the app. Vite runs it. It injects `__FUNDING_URL__` from `.github/FUNDING.yml`, builds the PWA service worker, and in dev proxies `/api` to `localhost:3001`.

## Who holds shared data

| Holder | File | Who reads it | Who writes it |
| --- | --- | --- | --- |
| Logged-in user and access token | `contexts/UserContext.jsx` | `App` (`ProtectedRoute`, `TopBar`, logout), `Auth`, `Home`, `ProfileSettings` | `Auth` after Google sign-in, `ProfileSettings` via `updateUser`, `App.logout` |
| Energy 1–5 | `contexts/EnergyContext.jsx` | `EnergyControl`, `Home`, `TodoList` | `EnergyControl` only. Also mirrored to `localStorage["bb-energy"]`, which `FocusTimer` reads directly when posting a session |
| Shield rules | `stores/blockingStore.ts` | `Home`, `FocusTimer`, `FocusShieldPage` | `Home` and `FocusTimer` load with `GET /blocking`. `FocusShieldPage` loads and then `PUT /blocking` |
| Theme string | `App` state, not the Zustand theme store | the `data-theme` attribute, which `styles.css` matches | the theme buttons, and `user.preferredTheme` after login |

`services/api.ts` is the only HTTP stack. Its request interceptor reads `localStorage.accessToken` (written by `UserProvider.saveToken`). Its response interceptor returns `res.data`. On 401 it posts `/auth/refresh` with cookies and retries once.

`UserProvider` also calls `services/socket.ts` `connectSocket(token)` and, on `task:*` / `habit:*`, `queryClient.invalidateQueries`. No screen calls `useQuery`, and `QueryProvider` is never mounted, so those invalidations do not refresh the lists. Screens reload by calling `api.get` themselves.

## What a click actually crosses

**Sign in.** `Auth.handleGoogleCredential` → `api.post("/auth/google")` → `setUser` / `setToken` (React state + localStorage) → `navigate("/")`. The effect in `UserProvider` then `sendToExtension({type:'SET_AUTH'})` and `connectSocket`.

**Open a page.** A `Link` or `NavLink` changes the URL. `App`’s `<Routes>` renders one element. Every route except `/auth` is wrapped in `ProtectedRoute`, which renders `Auth` when `user` is null.

**Change energy.** `EnergyControl` → `setEnergy` → `EnergyContext` re-renders `Home` and `TodoList`. `Home`’s effect depends on `energy` and calls `loadWhatNext`. `TodoList`’s effect depends on `energy` and calls `fetchSuggestions`. `scoreTask` reads `energy` during render, so the sort order changes on the same render.

**Add or complete a task.** `TodoList` → `api.post("/tasks")` or `api.put("/tasks/:id/complete")` → `load()` → `GET /tasks`. If the task has `dueAt`, `utils/deadlineScheduler.js` keeps a `setTimeout` that calls `utils/notify.js`. `Calendar` and `DeadlineTimer` have their own `GET /tasks`; they do not share `TodoList`’s state. They only meet again on the next fetch.

**Finish a focus block.** `FocusTimer`’s interval reaches 0 → `setFocusActive(false)` (module function in `FocusOverlay.jsx`, not a prop) → `handleComplete` reads `getDistractionCount()` from that same module → `api.post("/sessions")`. While the timer was running, `FocusOverlay`’s `visibilitychange` listener moved idle → focused → distracted → alert after 800ms, played `utils/sound.js`, and called `notify`.

**Edit the shield.** A `Toggle`, `WebsiteListManager`, `PresetPicker`, or `PauseControl` calls a callback that ends in `FocusShieldPage.update`, which sets `local`. An effect on `local` waits 600ms and `api.put("/blocking")`, then `setRules` on the Zustand store. `getShieldStatus` in `utils/focusShield.js` is what `ShieldStatusCard` and the shield page both call, so the label is computed in one place. The website does not block sites. `plugins/AppBlocker.ts` is the native bridge, and no screen calls it. The page text says enforcement is the Chrome extension or the native app.

**Connect Gmail, Calendar, or Slack.** `ConnectorsPage` or `SheetConnectors` → `api.get(urlEndpoint)` → `window.location = url`. The provider redirects back to `/connectors?connected=`. `ConnectorsPage` reads that query, toasts, and `GET /integrations/status`. Sync is `api.post(syncEndpoint)`.

## Files that are not on this path

These exist and are annotated line by line, and nothing in the routes imports them: `hooks/useTimer.ts`, `hooks/useTheme.ts`, `hooks/useAIStream.ts`, `hooks/useFocusMode.ts`, `stores/timerStore.ts`, `stores/themeStore.ts`, `stores/focusStore.ts`, `stores/uiStore.ts`, `themes/index.ts`, and the `QueryProvider` component. `Mindfulness.jsx` lines 1–252 are an old implementation inside a block comment; the function that runs starts at the third `Mindfulness`.
