"""Per-line explanations. Every line must be explained from its own text and file role."""
from __future__ import annotations

import re

from explainers.engine import PURPOSE
from explainers.meanings import decl_meaning, fn_blurb, FN, DECL

# Hand-written notes keyed by (file, 1-based line). These win over the parser.
# Populated by register() calls at the bottom of sibling modules.
OVERRIDES: dict[tuple[str, int], tuple[str, str]] = {}


def register(rel, mapping):
    for n, pair in mapping.items():
        OVERRIDES[(rel, n)] = pair


def explain_file(rel, src):
    # Load override modules once.
    global _loaded
    if not _loaded:
        from explainers import overrides_boot  # noqa: F401
        from explainers import overrides_state  # noqa: F401
        from explainers import overrides_pages  # noqa: F401
        from explainers import overrides_shield  # noqa: F401
        from explainers import overrides_rest  # noqa: F401
        _loaded = True
    ctx = Scan()
    tech, eli5 = [], []
    for i, raw in enumerate(src, 1):
        mfn = re.search(r"function\s+([A-Za-z0-9_]+)", raw)
        if mfn:
            ctx.fn = mfn.group(1)
        else:
            ctx.fn = ctx.current_fn()
        hit = OVERRIDES.get((rel, i))
        if hit:
            t, e = hit
        else:
            t, e = fallback(rel, i, raw, src, ctx)
        if not t.strip() or not e.strip():
            raise RuntimeError(f"empty explanation {rel}:{i}")
        tech.append(t)
        eli5.append(e)
        ctx.note_comment(raw)
        ctx.see_close(raw)
        ctx.see_open(i, raw)
    return tech, eli5


_loaded = False


class Scan:
    def __init__(self):
        self.fn = "the top of the file"
        self.block_comment = False
        self.stack = []  # (label, line)

    def note_comment(self, raw):
        s = raw.strip()
        if self.block_comment:
            if "*/" in s:
                self.block_comment = False
            return
        if s.startswith("/*") and "*/" not in s:
            self.block_comment = True

    def see_open(self, i, raw):
        s = raw.strip()
        m = re.search(r"function\s+([A-Za-z0-9_]+)", s)
        if m and s.endswith("{"):
            self.fn = m.group(1)
            self.stack.append((m.group(1), i))
            return
        if "useEffect" in s and s.endswith("{"):
            self.stack.append((f"effect in {self.fn}", i))
            return
        if s.startswith("if ") or s.startswith("if(") or s.startswith("try") or s.startswith("for ") or s.startswith("while "):
            if s.endswith("{"):
                self.stack.append((s[:40], i))
                return
        if s.endswith("{") and not s.startswith("//") and not s.startswith("/*"):
            self.stack.append((s[:48], i))

    def current_fn(self):
        for label, _line in reversed(self.stack):
            if label.startswith("effect"):
                continue
            if any(ch in label for ch in " (="):
                continue
            if label[:1].isalpha():
                return label
        return "the top of the file"

    def close_label(self):
        if not self.stack:
            return "the nearest open block"
        label, line = self.stack[-1]
        return f"{label} (opened on line {line})"

    def see_close(self, raw):
        s = raw.strip()
        # Only a line that begins by closing a block. A `}` inside
        # destructuring or JSX (`const { user }`, `strokeWidth={2}`) is not a block end.
        if s.startswith("}") and self.stack:
            self.stack.pop()


def fallback(rel, i, raw, src, ctx):
    if rel.endswith(".css"):
        return css_line(i, raw, ctx)
    purpose = PURPOSE.get(rel, rel)
    s = raw.strip()
    if s == "":
        return (
            f"Blank line in `{rel}` ({purpose}), inside {ctx.fn}. The parser skips it. It separates the previous statement from the next so the function is readable.",
            "A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.",
        )
    if s.startswith("//"):
        return (
            f"Comment inside {ctx.fn}. Not executed. It documents the next code: {s[2:].strip()}",
            "A note written for people. The app does not run it.",
        )
    if ctx.block_comment or s.startswith("/*") or s.startswith("*") or (s.startswith("*/")):
        return (
            f"Comment inside {ctx.fn}. Not executed. Text: {s[:240]}",
            "A note for people. The app skips this line.",
        )
    fnm = re.match(r"(?:export\s+default\s+)?(?:async\s+)?function\s+([A-Za-z0-9_]+)", s)
    if fnm and fn_blurb(fnm.group(1)):
        return (
            f"Defines `{fnm.group(1)}` in {purpose}. {fn_blurb(fnm.group(1))}",
            f"This starts {fnm.group(1)}. {fn_blurb(fnm.group(1))}",
        )
    if s.startswith("import "):
        return import_pair(s, purpose)
    if s.startswith("export default "):
        return (
            f"Default export of {purpose}: `{s}`. Importers that write `import X from '{rel}'` receive this value.",
            "This tells other files: the main thing in this file is this.",
        )
    if s.startswith("export "):
        return (
            f"Named export from {purpose}: `{s}`.",
            "This lets another file use this piece by its name.",
        )
    t = describe_tech(s, ctx, rel)
    e = describe_kid(s, ctx)
    return (t, e)


JSX_TECH = {
    "StrictMode": "React's development wrapper. In dev it renders twice to surface unsafe side effects. It does not change what the user sees in production.",
    "BrowserRouter": "Watches the address bar. Everything under it may use Routes, Link, and useLocation.",
    "UserProvider": "Provides useUser() to every component inside. Must wrap App, and it does.",
    "App": "The shell. main.jsx mounts this one component; App then mounts every page.",
    "EnergyProvider": "Provides useEnergy() to the shell and every page.",
    "Sidebar": "Left nav. Rendered only when user is set.",
    "TopBar": "Header. Rendered only when user is set.",
    "BottomNav": "Phone nav. Rendered only when user is set.",
    "MoreSheet": "Phone 'more' sheet. Rendered only when user is set.",
    "FocusOverlay": "The tab-leave nudge. Mounted next to the routes, not inside a page, so it stays alive while you move between pages.",
    "DevNoticeBanner": "The under-development strip. Shown only when user is set.",
    "ProtectedRoute": "Swaps in Auth when nobody is logged in. The page component is its child.",
    "Routes": "The table of URL to page. Only one Route matches.",
    "Route": "One URL. element is what React renders when the path matches.",
    "Auth": "Google sign-in screen. Also used as the fallback inside ProtectedRoute.",
    "Home": "Today page, path /.",
    "Dashboard": "Progress charts, path /dashboard.",
    "FocusTimer": "Countdown, path /focus.",
    "TodoList": "Tasks, path /todo.",
    "Mindfulness": "Audio page, path /mindful.",
    "DeadlineTimer": "Due-date list, path /deadline.",
    "Calendar": "Month view, path /calendar.",
    "ConnectorsPage": "Gmail, Calendar, Slack, path /connectors.",
    "FocusShieldPage": "Blocking rules, path /blocking.",
    "ProfileSettings": "Account and theme, path /settings. Receives onThemeChange so a saved theme updates the shell immediately.",
    "EnergyControl": "The energy faces. compact is the sidebar dots; without it, the big buttons on Today.",
    "Logo": "The JB mark.",
    "NavLink": "A link that knows whether its route is active, so the CSS class 'active' can highlight it.",
    "Link": "A react-router link. Clicking it changes the URL without a full page reload.",
    "ShieldStatusCard": "Shared shield status. Home passes variant dashboard. The timer passes variant session and sessionActive.",
    "Affirmations": "The sentence box. The parent holds a ref and asks it for a line.",
    "Toggle": "On/off switch. The parent owns the boolean.",
    "PauseControl": "Pause buttons. Writes pausedUntil through the parent's update, which autosaves.",
    "PresetPicker": "Preset buttons. Merges domains into the block list.",
    "WebsiteListManager": "One domain list. The page renders two of these.",
    "AddWebsiteSheet": "Add-site dialog.",
    "EditRuleSheet": "Edit-one-rule dialog.",
    "WebsiteRow": "One domain row.",
    "Sheet": "Shared dialog frame.",
    "FullCalendar": "The month grid. events come from GET /tasks.",
    "svg": "Vector drawing. It does not fetch data.",
    "button": "A button. If it has onClick, that function runs on press.",
    "input": "A text or date field. If value and onChange are set, React owns what it shows.",
    "div": "A box that groups the elements inside it.",
    "span": "An inline box.",
    "a": "A normal link. If it has target=_blank it leaves the app.",
    "form": "A form. onSubmit runs handleProfileSave.",
    "select": "A dropdown. onChange writes the chosen value into state.",
    "audio": "The hidden audio element Mindfulness plays.",
    "textarea": "A multi-line box. Brain dump and rule notes use it.",
    "h1": "The page title.",
    "p": "A paragraph.",
    "section": "A grouped block on the settings-style pages.",
    "nav": "A navigation landmark.",
    "header": "The top bar landmark.",
    "main": "The page body landmark.",
    "aside": "A side column.",
    "ul": "A list.",
    "li": "One list item.",
    "label": "The caption for an input.",
    "img": "An image.",
}


def prop_meaning(s):
    known = {
        "baseURL:": "Prefix for every relative request. VITE_API_URL if set, otherwise http://localhost:4000/api. A call api.get('/tasks') therefore hits that host plus /tasks.",
        "withCredentials: true": "Send cookies. The refresh call needs the httpOnly refresh cookie, which JavaScript cannot read but the browser will attach.",
        "staleTime:": "React Query would treat data as fresh for 60 seconds. No screen reads this cache.",
        "retry:": "React Query would retry a failed query once.",
        "autoConnect: false": "The socket is created quiet. connectSocket() is what actually connects, and only after a token exists.",
        "registerType:": "The PWA service worker updates itself when a new build is published.",
        "navigateFallback:": "Disabled on purpose so the service worker does not serve a stale index.html for every navigation.",
        "globPatterns:": "Precache built js, css, and images. HTML is intentionally not in this list.",
        "port:": "The Vite dev server listens on 5173.",
        "target:": "Dev-server proxy: browser calls to /api are forwarded to localhost:3001.",
    }
    for key, meaning in known.items():
        if key in s:
            return meaning + f" Code: `{s[:160]}`."
    if "api.interceptors.request" in s:
        return "Registers a function that runs before every request. It will copy accessToken from localStorage onto the Authorization header."
    if "api.interceptors.response" in s:
        return "Registers success and error handlers for every response. Success returns res.data so callers do not see the Axios wrapper."
    if "(res) => res.data" in s:
        return "Success path of the response interceptor. Unwraps the JSON body. That is why Home can use the return value directly."
    if "status === 401" in s:
        return "The access token was rejected. The handler will try /auth/refresh once, then retry the original request."
    if "/auth/refresh" in s:
        return "POST /auth/refresh with an empty body and cookies. The server reads the refresh cookie and returns a new accessToken."
    if "api.request(err.config)" in s:
        return "Retries the request that just got a 401, now with the new bearer token."
    if "window.location.href = '/auth'" in s or 'window.location.href = "/auth"' in s:
        return "Refresh failed. Drop the token and send the browser to the sign-in route."
    if "Promise.reject" in s:
        return "Any other error is handed back to the caller as a rejected promise. The page's catch block runs."
    if "createRoot" in s:
        return "Finds <div id=\"root\"> in index.html and renders the React tree into it. This is the line that starts the UI."
    if "document.documentElement.setAttribute(\"data-theme\"" in s:
        return "Writes data-theme on <html>. styles.css uses :root[data-theme=light] to swap the color tokens. Dark is the default :root."
    if "Notification.requestPermission" in s:
        return "Asks the browser once, on startup, for notification permission. notify() later only works if this was granted."
    if "setFocusActive" in s:
        return "Talks to FocusOverlay through the module-level bridge. true starts the focused state; false returns the overlay to idle."
    if "visibilitychange" in s or "visibilityState" in s:
        return "The browser fires this when the tab is hidden or shown. FocusOverlay uses it for the 800ms nudge. Mindfulness uses it to stop audio."
    if "queryClient.invalidateQueries" in s:
        return "Marks a React Query cache key stale. No screen is subscribed to that cache, so the lists on screen do not refresh from this line."
    if "connectSocket" in s:
        return "Opens the Socket.IO connection with the access token. UserProvider does this whenever token changes."
    if "disconnectSocket" in s:
        return "Closes the socket. This is the effect cleanup, so logout and a token change both disconnect."
    if "sendToExtension" in s or "SET_AUTH" in s or "CLEAR_AUTH" in s:
        return "Messages the Chrome extension, if VITE_EXTENSION_ID is set, so the extension can reuse this login."
    return None


def describe_tech(s, ctx, rel):
    where = f"In `{ctx.fn}` ({rel})"
    if s.startswith("<"):
        tag = re.match(r"</?([A-Za-z0-9.]+)", s)
        name = tag.group(1) if tag else "element"
        if name in JSX_TECH:
            closer = "Closes it." if s.startswith("</") else "Opens it."
            return f"{where}: {closer} {JSX_TECH[name]} Source: `{s[:160]}`"
        extra = []
        if "className=" in s:
            extra.append("className chooses the CSS rules from styles.css")
        if "onClick=" in s:
            extra.append("onClick runs only after a click, not during this render")
        if "to=" in s:
            extra.append("the `to` prop is a route that react-router will render when the link is activated")
        if "value=" in s:
            extra.append("value is controlled by React state, so the DOM shows that state")
        tail = (". " + "; ".join(extra)) if extra else ""
        closer = " This closes that element." if s.startswith("</") else " React will create this node when the parent renders."
        return f"{where}: JSX `<{name}>`.{closer}{tail} Source: `{s[:200]}`"
    if re.match(r"(const|let|var)\s+", s) or re.match(r"export\s+(const|let|var)\s+", s):
        return f"{where}: {decl_meaning(s)}"
    fnm = re.match(r"(?:export\s+default\s+)?(?:async\s+)?function\s+([A-Za-z0-9_]+)", s)
    if fnm and fn_blurb(fnm.group(1)):
        return f"{where}: defines `{fnm.group(1)}`. {fn_blurb(fnm.group(1))}"
    if s.startswith("return"):
        return f"{where}: return `{s[:200]}`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM."
    if s.startswith("if ") or s.startswith("if(") or s.startswith("} else"):
        return f"{where}: branch `{s[:220]}`. Only one side runs."
    if "useState" in s:
        return f"{where}: `useState` — `{s[:220]}`. The setter schedules a re-render of this component only."
    if "useEffect" in s:
        return f"{where}: opens or continues an effect — `{s[:220]}`. The effect body runs after paint, and its cleanup runs before the next effect and on unmount."
    if "useRef" in s:
        return f"{where}: `useRef` — `{s[:200]}`. The `.current` box survives re-renders and writing it does not re-render."
    if "useMemo" in s or "useCallback" in s:
        return f"{where}: memo hook — `{s[:200]}`. The cached value changes only when the listed dependencies change."
    if re.search(r"\bapi\.(get|post|put|delete)\b", s):
        return f"{where}: HTTP via the shared Axios instance — `{s[:220]}`. The request interceptor adds `Authorization: Bearer <accessToken>`. The response interceptor returns `res.data`, so the awaited value is the JSON body."
    if "localStorage" in s:
        return f"{where}: browser storage — `{s[:220]}`. This survives reloads on this origin and is shared by any script that uses the same key."
    if "setTimeout" in s or "setInterval" in s or "clearTimeout" in s or "clearInterval" in s:
        return f"{where}: timer — `{s[:220]}`. The callback runs later on the event loop, not now."
    if s.startswith("await ") or s.startswith("await\t"):
        return f"{where}: `{s[:220]}`. The async function suspends until the promise fulfills, then assigns or continues."
    if "onClick" in s or "onChange" in s or "onSubmit" in s or "onKeyDown" in s or "onKey" in s:
        return f"{where}: event prop `{s[:220]}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref."
    if "}" in s and not s.startswith("<") and "=>" not in s and not s.startswith("/*"):
        closed = ctx.close_label()
        return f"{where}: `{s}` closes {closed}. Names declared inside that block end here."
    if s.startswith("case ") or s.startswith("default:"):
        return f"{where}: switch arm `{s}`."
    if s.startswith("throw ") or s.startswith("try") or s.startswith("catch") or s.startswith("finally"):
        return f"{where}: error path `{s[:200]}`."
    if s.startswith("for ") or s.startswith("while ") or ".map(" in s or ".filter(" in s or ".forEach(" in s:
        return f"{where}: iteration `{s[:220]}`."
    prop = prop_meaning(s)
    if prop:
        return f"{where}: {prop}"
    return f"{where}: statement `{s[:240]}`. It runs when {ctx.fn} runs, in order, before the next line of the same function."


IMPORTS = {
    "react": "Borrows React so this file can remember things and draw the screen.",
    "react-dom/client": "Borrows the tool that sticks the app onto the page.",
    "react-router-dom": "Borrows the address-bar tools: links, the current page, and page changes.",
    "./styles.css": "Loads the paint for the whole app.",
    "./App.jsx": "Gets the hallway that holds every room.",
    "./contexts/UserContext.jsx": "Gets the name-tag keeper.",
    "axios": "Borrows the mail carrier that talks to the server.",
    "socket.io-client": "Borrows the live phone line to the server.",
    "@tanstack/react-query": "Borrows a memory box for server answers. The screens do not actually use it.",
    "zustand": "Borrows a shared notebook that any room can read.",
    "howler": "Borrows a sound player.",
    "@fullcalendar/react": "Borrows the calendar picture.",
    "recharts": "Borrows the chart pictures.",
    "@capacitor/core": "Borrows the bridge to a phone app. The website stub does not block apps.",
}


def import_pair(statement, purpose):
    src = statement
    kid = "This file borrows a tool another file already made."
    for key, sentence in IMPORTS.items():
        if key in statement:
            kid = sentence
            break
    tech = (
        f"Import for {purpose}: `{src}`. "
        "The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect."
    )
    return tech, kid


def describe_kid(s, ctx):
    fnm = re.match(r"(?:export\s+default\s+)?(?:async\s+)?function\s+([A-Za-z0-9_]+)", s)
    if fnm and fnm.group(1) in FN:
        return f"This starts the job called {fnm.group(1)}. In kid words: {FN[fnm.group(1)]}"
    if s.startswith("<"):
        if s.startswith("</"):
            return f"This ends a drawing that {ctx.fn} started just above."
        return f"This draws one piece of the page while {ctx.fn} is showing."
    if s.startswith("const ") or s.startswith("let ") or s.startswith("var ") or s.startswith("export const"):
        m = re.search(r"(?:const|let|var)\s+(?:\[([^\]]+)\]|\{([^}]+)\}|([A-Za-z0-9_]+))", s)
        names = []
        if m:
            names = [p.strip() for p in re.split(r"[, ]+", (m.group(1) or m.group(2) or m.group(3) or "")) if p.strip()]
        known = [DECL[n] for n in names if n in DECL]
        if known:
            return known[0]
        return f"This gives a short name to a value so the rest of {ctx.fn} can use it."
    if "useState" in s:
        return "This is a memory for the screen. Change it, and this part draws again."
    if "useEffect" in s:
        return "This is an extra job that happens after the picture is drawn."
    if s.startswith("return"):
        return "This is the answer the function gives back. If it looks like a picture tag, that picture is what you see."
    if "api." in s:
        return "This asks the server (the office that keeps tasks and accounts) for something, or sends it something."
    if "localStorage" in s:
        return "This looks in the browser's pocket, or puts something there, so it is still around after a refresh."
    if "onClick" in s:
        return "This decides what happens when you press."
    if s.startswith("if "):
        return "This asks a yes-or-no question. The next bit runs only on yes."
    if "}" in s and not s.startswith("<"):
        return f"This ends {ctx.close_label()}."
    if s.startswith(")") or s.startswith("/>"):
        return "This closes a box of instructions that opened above."
    if "await" in s:
        return "This waits for an answer before the next step."
    return (
        f"Inside {ctx.fn}, this line runs as written: {s[:140]}. "
        "It happens in order, after the line above it and before the line below it."
    )


def css_line(i, raw, ctx):
    s = raw.strip()
    if s == "":
        return (
            "Blank line in styles.css. It does not create a rule. It separates groups of rules.",
            "A blank line in the paint file. It does not change how anything looks.",
        )
    if s.startswith("/*") or s.startswith("*") or ctx.block_comment or s.endswith("*/") and not s.endswith(";"):
        if s.startswith("/*") or s.startswith("*") or s == "*/" or s.endswith("*/"):
            return (
                f"CSS comment, ignored by the browser. It labels the next group of rules: {s[:180]}",
                "A label for people about the next chunk of paint. The browser ignores it.",
            )
    if s.startswith("@tailwind"):
        return (
            f"`{s}` tells Tailwind to inject its {s.split()[-1].rstrip(';')} styles here. Those utilities exist because tailwind.config.js scans the source.",
            "This pulls in a big box of ready-made paint from Tailwind.",
        )
    if s.startswith("@media"):
        return (
            f"Opens a media query `{s}`. The rules inside apply only when that screen condition is true, so the same components reflow on a phone.",
            "This says: only use the next paint rules when the screen is a certain size.",
        )
    if s.startswith("@keyframes"):
        return (
            f"Starts an animation definition `{s}`. Later rules refer to this name in an `animation` property.",
            "This starts a little movie of paint changes. Something else plays it by name.",
        )
    if s.endswith("{") and not s.endswith(";"):
        return (
            f"Opens a rule for selector `{s[:-1].strip()}`. Every property until the matching `}}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.",
            f"This starts paint instructions for things that match `{s[:-1].strip()}`.",
        )
    if s == "}":
        return (
            "Closes the rule or at-rule opened above. Properties after this belong to the next selector.",
            "This ends that group of paint instructions.",
        )
    if ":" in s and s.endswith(";"):
        prop, _, val = s.partition(":")
        return (
            f"Sets CSS property `{prop.strip()}` to `{val.strip().rstrip(';')}`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.",
            f"This sets one look: {prop.strip()} becomes {val.strip().rstrip(';')}.",
        )
    return (
        f"CSS line `{s[:200]}`. It is part of the stylesheet the browser applies while painting the React DOM.",
        "One paint instruction in the big style file.",
    )
