"""Match each source line to a specific explanation. Unmatched lines fail the build."""
from __future__ import annotations

import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
FRONT = ROOT / "frontend"


class Miss(Exception):
    pass


def miss(rel, i, raw):
    raise Miss(f"UNMATCHED {rel}:{i}: {raw!r}")


# File-level purpose, used when a generic syntactic note still needs a home.
PURPOSE = {
    "index.html": "the browser page that boots React",
    "src/main.jsx": "the startup file that mounts the React tree",
    "src/App.jsx": "the shell: theme, menus, and which page is visible",
    "src/vite-env.d.ts": "TypeScript's knowledge of Vite globals",
    "vite.config.ts": "the Vite build and dev-server setup",
    "src/services/api.ts": "the HTTP client every page uses to reach the backend",
    "src/services/socket.ts": "the live socket opened after login",
    "src/services/sse.ts": "a helper that reads a streaming AI response",
    "src/providers/QueryProvider.tsx": "a React Query cache that the screens do not mount",
    "src/contexts/UserContext.jsx": "who is logged in, stored in memory and localStorage",
    "src/contexts/EnergyContext.jsx": "the 1–5 energy level shared by Home, the sidebar, and Tasks",
    "src/utils/sound.js": "the tab-switch alert sound",
    "src/utils/notify.js": "desktop notifications for deadlines and focus nudges",
    "src/utils/deadlineScheduler.js": "browser timers that fire when a task is due",
    "src/utils/focusShield.js": "pure rules for the Focus Shield, shared by several screens",
    "src/themes/index.ts": "a re-export of the unused five-palette theme hook",
    "src/components/Auth.jsx": "the Google sign-in screen",
    "src/components/Home.jsx": "the Today page",
    "src/components/EnergyControl.jsx": "the five energy buttons",
    "src/components/Logo.jsx": "the JumpyBrain mark",
    "src/components/Affirmations.jsx": "short encouragement lines the timer and mindfulness can request",
    "src/components/TodoList.jsx": "the task list, brain dump, and AI suggestion cards",
    "src/components/FocusTimer.jsx": "the countdown ring and session saver",
    "src/components/FocusOverlay.jsx": "the full-screen nudge when you leave a focus tab",
    "src/components/Dashboard.jsx": "the progress charts",
    "src/components/Calendar.jsx": "the month view of tasks",
    "src/components/DeadlineTimer.jsx": "the list of tasks that have due dates",
    "src/components/ConnectorsPage.jsx": "Gmail, Calendar, and Slack connect/sync/disconnect",
    "src/components/Mindfulness.jsx": "the audio breathing page; the top of the file is old commented code",
    "src/components/ProfileSettings.jsx": "name, email, theme, and the coffee link",
    "src/components/focus-shield/FocusShieldPage.jsx": "the page that edits and autosaves blocking rules",
    "src/components/focus-shield/WebsiteListManager.jsx": "search, add, edit, and bulk-edit one domain list",
    "src/components/focus-shield/WebsiteRow.jsx": "one website row",
    "src/components/focus-shield/AddWebsiteSheet.jsx": "the sheet for adding a popular or custom site",
    "src/components/focus-shield/EditRuleSheet.jsx": "the sheet for editing one rule",
    "src/components/focus-shield/Sheet.jsx": "the shared popup/bottom-sheet frame",
    "src/components/focus-shield/PauseControl.jsx": "pause blocking for a few minutes or until tomorrow",
    "src/components/focus-shield/PresetPicker.jsx": "one-click blocklists",
    "src/components/focus-shield/ShieldStatusCard.jsx": "the shared status card on Today and the timer",
    "src/components/focus-shield/Toggle.jsx": "the shared on/off switch",
    "src/hooks/useTimer.ts": "an unused countdown hook backed by timerStore",
    "src/hooks/useTheme.ts": "an unused hook that writes five palettes as CSS variables",
    "src/hooks/useAIStream.ts": "an unused hook that streams /ai/chat",
    "src/hooks/useFocusMode.ts": "an unused hook that emits FOCUS_LOST on the socket",
    "src/stores/focusStore.ts": "Zustand state for the unused focus hook",
    "src/stores/uiStore.ts": "Zustand sidebar/modal state that App.jsx does not read",
    "src/stores/blockingStore.ts": "the shared Focus Shield rules object",
    "src/stores/timerStore.ts": "Zustand state for the unused timer hook",
    "src/stores/themeStore.ts": "Zustand state for the unused five-palette theme",
    "src/plugins/AppBlocker.ts": "the Capacitor bridge to native app blocking",
    "src/plugins/AppBlockerWeb.ts": "the web stub that reports blocking as unavailable",
    "src/styles.css": "every visual rule for the app",
    "capacitor.config.ts": "Capacitor's native app id and web dir",
    "eslint.config.js": "lint rules for the frontend",
    "postcss.config.js": "PostCSS plugin list (Tailwind)",
    "tailwind.config.js": "Tailwind content paths and theme",
}


def generic(rel, i, raw):
    """Last-resort syntactic explanation. Still names this line. Prefer specific matches."""
    s = raw.strip()
    purpose = PURPOSE.get(rel, rel)
    if s == "":
        return (
            f"Blank line in {purpose}. It does not run. It separates the previous statement from the next.",
            "A blank line. The computer skips it. It is only there to make the file easier to read.",
        )
    if s.startswith("//") or s.startswith("/*") or s.startswith("*") or s.startswith("*/"):
        return (
            f"Comment in {purpose}. The program ignores it. The note says: {s[:180]}",
            "A note for humans. The computer skips this whole line.",
        )
    if s.startswith("import "):
        return (
            f"Import in {purpose}. This line loads {s}. Later lines in this file call those names.",
            f"This line borrows something another file already made: {s}",
        )
    if s.startswith("export "):
        return (
            f"Export in {purpose}. {s} makes this name available to other files that import this one.",
            "This line lets other files use what this file made.",
        )
    return None
