#!/usr/bin/env python3
"""Build line-by-line walkthroughs. Fails if any line has no specific note."""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from explainers.specific import explain_file  # noqa: E402

FRONT = ROOT / "frontend"
OUT = ROOT / "docs" / "frontend-line-by-line"

FILES = [
    "index.html",
    "vite.config.ts",
    "capacitor.config.ts",
    "eslint.config.js",
    "postcss.config.js",
    "tailwind.config.js",
    "src/main.jsx",
    "src/vite-env.d.ts",
    "src/App.jsx",
    "src/styles.css",
    "src/services/api.ts",
    "src/services/socket.ts",
    "src/services/sse.ts",
    "src/providers/QueryProvider.tsx",
    "src/contexts/UserContext.jsx",
    "src/contexts/EnergyContext.jsx",
    "src/utils/sound.js",
    "src/utils/notify.js",
    "src/utils/deadlineScheduler.js",
    "src/utils/focusShield.js",
    "src/themes/index.ts",
    "src/hooks/useTimer.ts",
    "src/hooks/useTheme.ts",
    "src/hooks/useAIStream.ts",
    "src/hooks/useFocusMode.ts",
    "src/stores/focusStore.ts",
    "src/stores/uiStore.ts",
    "src/stores/blockingStore.ts",
    "src/stores/timerStore.ts",
    "src/stores/themeStore.ts",
    "src/plugins/AppBlocker.ts",
    "src/plugins/AppBlockerWeb.ts",
    "src/components/Auth.jsx",
    "src/components/Home.jsx",
    "src/components/EnergyControl.jsx",
    "src/components/Logo.jsx",
    "src/components/Affirmations.jsx",
    "src/components/TodoList.jsx",
    "src/components/FocusTimer.jsx",
    "src/components/FocusOverlay.jsx",
    "src/components/Dashboard.jsx",
    "src/components/Calendar.jsx",
    "src/components/DeadlineTimer.jsx",
    "src/components/ConnectorsPage.jsx",
    "src/components/Mindfulness.jsx",
    "src/components/ProfileSettings.jsx",
    "src/components/focus-shield/FocusShieldPage.jsx",
    "src/components/focus-shield/WebsiteListManager.jsx",
    "src/components/focus-shield/WebsiteRow.jsx",
    "src/components/focus-shield/AddWebsiteSheet.jsx",
    "src/components/focus-shield/EditRuleSheet.jsx",
    "src/components/focus-shield/Sheet.jsx",
    "src/components/focus-shield/PauseControl.jsx",
    "src/components/focus-shield/PresetPicker.jsx",
    "src/components/focus-shield/ShieldStatusCard.jsx",
    "src/components/focus-shield/Toggle.jsx",
]


def main():
    missing = []
    for rel in FILES:
        src = (FRONT / rel).read_text().splitlines()
        try:
            tech, eli5 = explain_file(rel, src)
        except Exception as e:
            missing.append(str(e))
            continue
        if len(tech) != len(src) or len(eli5) != len(src):
            missing.append(f"{rel} length mismatch")
            continue
        for kind, notes in (("technical", tech), ("eli5", eli5)):
            dest = OUT / kind / f"{rel}.md"
            dest.parent.mkdir(parents=True, exist_ok=True)
            parts = [
                f"# `{rel}`",
                "",
                "The source line is on the left of `|`. The explanation of that line is underneath it.",
                "",
            ]
            for i, (line, note) in enumerate(zip(src, notes), 1):
                if not note or not str(note).strip():
                    missing.append(f"empty {kind} {rel}:{i}")
                parts.append(f"{i:4d} | {line}")
                parts.append(f"     | {note}")
                parts.append("")
            dest.write_text("\n".join(parts) + "\n")
        print(f"ok {rel} ({len(src)})")
    if missing:
        print("FAILURES:")
        for m in missing:
            print(m)
        sys.exit(1)


if __name__ == "__main__":
    main()
