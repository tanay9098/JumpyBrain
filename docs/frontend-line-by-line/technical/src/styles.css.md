# `src/styles.css`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | @tailwind base;
     | `@tailwind base;` tells Tailwind to inject its base styles here. Those utilities exist because tailwind.config.js scans the source.

   2 | @tailwind components;
     | `@tailwind components;` tells Tailwind to inject its components styles here. Those utilities exist because tailwind.config.js scans the source.

   3 | @tailwind utilities;
     | `@tailwind utilities;` tells Tailwind to inject its utilities styles here. Those utilities exist because tailwind.config.js scans the source.

   4 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

   5 | /* ═══════════════════════════════════════════════════════
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ═══════════════════════════════════════════════════════

   6 |    JUMPYBRAIN — JB MOMENTUM DESIGN SYSTEM v4
     | CSS line `JUMPYBRAIN — JB MOMENTUM DESIGN SYSTEM v4`. It is part of the stylesheet the browser applies while painting the React DOM.

   7 |    Token-driven theming: one CSS var change cascades everywhere
     | CSS line `Token-driven theming: one CSS var change cascades everywhere`. It is part of the stylesheet the browser applies while painting the React DOM.

   8 |    ═══════════════════════════════════════════════════════ */
     | CSS comment, ignored by the browser. It labels the next group of rules: ═══════════════════════════════════════════════════════ */

   9 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

  10 | /* ── Design Tokens (Dark Theme = default) ───────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── Design Tokens (Dark Theme = default) ───────────── */

  11 | :root {
     | Opens a rule for selector `:root`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

  12 |   /* Brand — JB Momentum palette */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* Brand — JB Momentum palette */

  13 |   --indigo: #6366f1;
     | Sets CSS property `--indigo` to `#6366f1`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  14 |   --indigo-light: #a5b4fc;
     | Sets CSS property `--indigo-light` to `#a5b4fc`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  15 |   --indigo-dim: rgba(99, 102, 241, 0.15);
     | Sets CSS property `--indigo-dim` to `rgba(99, 102, 241, 0.15)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  16 |   --violet: #7c3aed;
     | Sets CSS property `--violet` to `#7c3aed`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  17 |   --violet-light: #a78bfa;
     | Sets CSS property `--violet-light` to `#a78bfa`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  18 |   --violet-dim: rgba(124, 58, 237, 0.15);
     | Sets CSS property `--violet-dim` to `rgba(124, 58, 237, 0.15)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  19 |   --electric-blue: #2563eb;
     | Sets CSS property `--electric-blue` to `#2563eb`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  20 |   --cyan: #06b6d4;
     | Sets CSS property `--cyan` to `#06b6d4`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  21 |   --cyan-dim: rgba(6, 182, 212, 0.15);
     | Sets CSS property `--cyan-dim` to `rgba(6, 182, 212, 0.15)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  22 |   --teal: #10b981;
     | Sets CSS property `--teal` to `#10b981`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  23 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

  24 |   /* Semantic colors */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* Semantic colors */

  25 |   --green: #10b981;
     | Sets CSS property `--green` to `#10b981`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  26 |   --green-dim: rgba(16, 185, 129, 0.15);
     | Sets CSS property `--green-dim` to `rgba(16, 185, 129, 0.15)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  27 |   --amber: #f59e0b;
     | Sets CSS property `--amber` to `#f59e0b`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  28 |   --amber-dim: rgba(245, 158, 11, 0.15);
     | Sets CSS property `--amber-dim` to `rgba(245, 158, 11, 0.15)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  29 |   --red: #ef4444;
     | Sets CSS property `--red` to `#ef4444`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  30 |   --red-dim: rgba(239, 68, 68, 0.15);
     | Sets CSS property `--red-dim` to `rgba(239, 68, 68, 0.15)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  31 |   --blue: #2563eb;
     | Sets CSS property `--blue` to `#2563eb`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  32 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

  33 |   /* Reward (dopamine) */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* Reward (dopamine) */

  34 |   --gold: #fbbf24;
     | Sets CSS property `--gold` to `#fbbf24`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  35 |   --pink: #f472b6;
     | Sets CSS property `--pink` to `#f472b6`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  36 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

  37 |   /* Neutral scale – dark — WCAG AA compliant */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* Neutral scale – dark — WCAG AA compliant */

  38 |   --bg: #0f1020;
     | Sets CSS property `--bg` to `#0f1020`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  39 |   --surface: #1a1b2e;
     | Sets CSS property `--surface` to `#1a1b2e`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  40 |   --card: #1e1f35;
     | Sets CSS property `--card` to `#1e1f35`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  41 |   --card-hover: #252640;
     | Sets CSS property `--card-hover` to `#252640`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  42 |   --border: rgba(255, 255, 255, 0.08);
     | Sets CSS property `--border` to `rgba(255, 255, 255, 0.08)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  43 |   --border-active: rgba(99, 102, 241, 0.5);
     | Sets CSS property `--border-active` to `rgba(99, 102, 241, 0.5)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  44 |   --text: #eef0ff;           /* 14:1 on --bg */
     | CSS comment, ignored by the browser. It labels the next group of rules: --text: #eef0ff;           /* 14:1 on --bg */

  45 |   --text-soft: #c0c4e8;      /* 8:1 on --bg */
     | CSS comment, ignored by the browser. It labels the next group of rules: --text-soft: #c0c4e8;      /* 8:1 on --bg */

  46 |   --muted: #9196c0;          /* 4.6:1 on --bg */
     | CSS comment, ignored by the browser. It labels the next group of rules: --muted: #9196c0;          /* 4.6:1 on --bg */

  47 |   --shadow: 0 4px 24px rgba(0, 0, 0, 0.45);
     | Sets CSS property `--shadow` to `0 4px 24px rgba(0, 0, 0, 0.45)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  48 |   --shadow-card: 0 2px 12px rgba(0, 0, 0, 0.35);
     | Sets CSS property `--shadow-card` to `0 2px 12px rgba(0, 0, 0, 0.35)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  49 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

  50 |   /* Brand gradient (used on logo, primary accents) */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* Brand gradient (used on logo, primary accents) */

  51 |   --brand-gradient: linear-gradient(135deg, #7c3aed 0%, #6366f1 45%, #06b6d4 100%);
     | Sets CSS property `--brand-gradient` to `linear-gradient(135deg, #7c3aed 0%, #6366f1 45%, #06b6d4 100%)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  52 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

  53 |   /* Layout */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* Layout */

  54 |   --sidebar-w: 224px;
     | Sets CSS property `--sidebar-w` to `224px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  55 |   --top-bar-h: 52px;
     | Sets CSS property `--top-bar-h` to `52px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  56 |   --bottom-nav-h: 60px;
     | Sets CSS property `--bottom-nav-h` to `60px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  57 |   --radius: 14px;
     | Sets CSS property `--radius` to `14px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  58 |   --radius-sm: 8px;
     | Sets CSS property `--radius-sm` to `8px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  59 |   --radius-lg: 20px;
     | Sets CSS property `--radius-lg` to `20px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  60 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

  61 |   /* Type scale — 3 steps: 12 / 14 / 22+ */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* Type scale — 3 steps: 12 / 14 / 22+ */

  62 |   --text-xs: 12px;
     | Sets CSS property `--text-xs` to `12px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  63 |   --text-sm: 14px;
     | Sets CSS property `--text-sm` to `14px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  64 |   --text-base: 15px;
     | Sets CSS property `--text-base` to `15px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  65 |   --text-lg: 18px;
     | Sets CSS property `--text-lg` to `18px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  66 |   --text-xl: 22px;
     | Sets CSS property `--text-xl` to `22px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  67 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

  68 |   /* Spacing — 4-step scale */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* Spacing — 4-step scale */

  69 |   --space-1: 4px;
     | Sets CSS property `--space-1` to `4px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  70 |   --space-2: 8px;
     | Sets CSS property `--space-2` to `8px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  71 |   --space-3: 12px;
     | Sets CSS property `--space-3` to `12px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  72 |   --space-4: 16px;
     | Sets CSS property `--space-4` to `16px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  73 |   --space-5: 20px;
     | Sets CSS property `--space-5` to `20px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  74 |   --space-6: 24px;
     | Sets CSS property `--space-6` to `24px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  75 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

  76 |   font-family: "Inter", "Plus Jakarta Sans", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
     | Sets CSS property `font-family` to `"Inter", "Plus Jakarta Sans", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  77 |   -webkit-font-smoothing: antialiased;
     | Sets CSS property `-webkit-font-smoothing` to `antialiased`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  78 |   -moz-osx-font-smoothing: grayscale;
     | Sets CSS property `-moz-osx-font-smoothing` to `grayscale`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  79 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

  80 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

  81 | /* ── Light Theme ────────────────────────────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── Light Theme ────────────────────────────────────── */

  82 | :root[data-theme="light"] {
     | Opens a rule for selector `:root[data-theme="light"]`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

  83 |   --bg: #f4f4fe;
     | Sets CSS property `--bg` to `#f4f4fe`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  84 |   --surface: #ffffff;
     | Sets CSS property `--surface` to `#ffffff`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  85 |   --card: #ffffff;
     | Sets CSS property `--card` to `#ffffff`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  86 |   --card-hover: #f8f8ff;
     | Sets CSS property `--card-hover` to `#f8f8ff`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  87 |   --border: rgba(0, 0, 0, 0.07);
     | Sets CSS property `--border` to `rgba(0, 0, 0, 0.07)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  88 |   --border-active: rgba(99, 102, 241, 0.4);
     | Sets CSS property `--border-active` to `rgba(99, 102, 241, 0.4)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  89 |   --text: #0d0e1f;           /* 16:1 on --bg */
     | CSS comment, ignored by the browser. It labels the next group of rules: --text: #0d0e1f;           /* 16:1 on --bg */

  90 |   --text-soft: #32355a;      /* 9.5:1 on --bg */
     | CSS comment, ignored by the browser. It labels the next group of rules: --text-soft: #32355a;      /* 9.5:1 on --bg */

  91 |   --muted: #5456a0;          /* 4.8:1 on --bg */
     | CSS comment, ignored by the browser. It labels the next group of rules: --muted: #5456a0;          /* 4.8:1 on --bg */

  92 |   --shadow: 0 4px 24px rgba(0, 0, 0, 0.06);
     | Sets CSS property `--shadow` to `0 4px 24px rgba(0, 0, 0, 0.06)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  93 |   --shadow-card: 0 2px 8px rgba(0, 0, 0, 0.05);
     | Sets CSS property `--shadow-card` to `0 2px 8px rgba(0, 0, 0, 0.05)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  94 |   --violet-dim: rgba(124, 58, 237, 0.07);
     | Sets CSS property `--violet-dim` to `rgba(124, 58, 237, 0.07)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  95 |   --indigo-dim: rgba(99, 102, 241, 0.07);
     | Sets CSS property `--indigo-dim` to `rgba(99, 102, 241, 0.07)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  96 |   --cyan-dim: rgba(6, 182, 212, 0.07);
     | Sets CSS property `--cyan-dim` to `rgba(6, 182, 212, 0.07)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  97 |   --green-dim: rgba(16, 185, 129, 0.07);
     | Sets CSS property `--green-dim` to `rgba(16, 185, 129, 0.07)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  98 |   --amber-dim: rgba(245, 158, 11, 0.07);
     | Sets CSS property `--amber-dim` to `rgba(245, 158, 11, 0.07)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

  99 |   --red-dim: rgba(239, 68, 68, 0.07);
     | Sets CSS property `--red-dim` to `rgba(239, 68, 68, 0.07)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 100 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 101 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 102 | /* ── Reset ──────────────────────────────────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── Reset ──────────────────────────────────────────── */

 103 | *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
     | CSS comment, ignored by the browser. It labels the next group of rules: *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

 104 | html, body, #root { height: 100%; width: 100%; }
     | CSS line `html, body, #root { height: 100%; width: 100%; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 105 | body {
     | Opens a rule for selector `body`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 106 |   background: var(--bg);
     | Sets CSS property `background` to `var(--bg)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 107 |   color: var(--text);
     | Sets CSS property `color` to `var(--text)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 108 |   transition: background 0.3s, color 0.3s;
     | Sets CSS property `transition` to `background 0.3s, color 0.3s`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 109 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 110 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 111 | /* ── Global focus rings (WCAG 2.4.7) ───────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── Global focus rings (WCAG 2.4.7) ───────────────── */

 112 | :focus-visible {
     | Opens a rule for selector `:focus-visible`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 113 |   outline: 2px solid var(--indigo-light);
     | Sets CSS property `outline` to `2px solid var(--indigo-light)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 114 |   outline-offset: 2px;
     | Sets CSS property `outline-offset` to `2px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 115 |   border-radius: var(--radius-sm);
     | Sets CSS property `border-radius` to `var(--radius-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 116 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 117 | button:focus-visible,
     | CSS line `button:focus-visible,`. It is part of the stylesheet the browser applies while painting the React DOM.

 118 | a:focus-visible,
     | CSS line `a:focus-visible,`. It is part of the stylesheet the browser applies while painting the React DOM.

 119 | input:focus-visible,
     | CSS line `input:focus-visible,`. It is part of the stylesheet the browser applies while painting the React DOM.

 120 | select:focus-visible,
     | CSS line `select:focus-visible,`. It is part of the stylesheet the browser applies while painting the React DOM.

 121 | textarea:focus-visible {
     | Opens a rule for selector `textarea:focus-visible`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 122 |   outline: 2px solid var(--indigo-light);
     | Sets CSS property `outline` to `2px solid var(--indigo-light)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 123 |   outline-offset: 2px;
     | Sets CSS property `outline-offset` to `2px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 124 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 125 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 126 | /* ── App Shell ──────────────────────────────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── App Shell ──────────────────────────────────────── */

 127 | .app-shell {
     | Opens a rule for selector `.app-shell`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 128 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 129 |   width: 100%;
     | Sets CSS property `width` to `100%`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 130 |   height: 100vh;
     | Sets CSS property `height` to `100vh`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 131 |   overflow: hidden;
     | Sets CSS property `overflow` to `hidden`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 132 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 133 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 134 | .main-wrapper {
     | Opens a rule for selector `.main-wrapper`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 135 |   flex: 1;
     | Sets CSS property `flex` to `1`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 136 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 137 |   flex-direction: column;
     | Sets CSS property `flex-direction` to `column`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 138 |   min-width: 0;
     | Sets CSS property `min-width` to `0`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 139 |   overflow: hidden;
     | Sets CSS property `overflow` to `hidden`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 140 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 141 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 142 | /* ── Top Bar ────────────────────────────────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── Top Bar ────────────────────────────────────────── */

 143 | .top-bar {
     | Opens a rule for selector `.top-bar`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 144 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 145 |   align-items: center;
     | Sets CSS property `align-items` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 146 |   justify-content: space-between;
     | Sets CSS property `justify-content` to `space-between`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 147 |   height: var(--top-bar-h);
     | Sets CSS property `height` to `var(--top-bar-h)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 148 |   padding: 0 var(--space-5);
     | Sets CSS property `padding` to `0 var(--space-5)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 149 |   background: var(--surface);
     | Sets CSS property `background` to `var(--surface)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 150 |   border-bottom: 1px solid var(--border);
     | Sets CSS property `border-bottom` to `1px solid var(--border)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 151 |   flex-shrink: 0;
     | Sets CSS property `flex-shrink` to `0`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 152 |   gap: var(--space-3);
     | Sets CSS property `gap` to `var(--space-3)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 153 |   z-index: 50;
     | Sets CSS property `z-index` to `50`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 154 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 155 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 156 | .top-bar-left {
     | Opens a rule for selector `.top-bar-left`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 157 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 158 |   align-items: center;
     | Sets CSS property `align-items` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 159 |   gap: var(--space-3);
     | Sets CSS property `gap` to `var(--space-3)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 160 |   flex: 1;
     | Sets CSS property `flex` to `1`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 161 |   min-width: 0;
     | Sets CSS property `min-width` to `0`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 162 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 163 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 164 | .top-bar-right {
     | Opens a rule for selector `.top-bar-right`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 165 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 166 |   align-items: center;
     | Sets CSS property `align-items` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 167 |   gap: var(--space-2);
     | Sets CSS property `gap` to `var(--space-2)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 168 |   flex-shrink: 0;
     | Sets CSS property `flex-shrink` to `0`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 169 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 170 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 171 | .top-bar-menu-btn,
     | CSS line `.top-bar-menu-btn,`. It is part of the stylesheet the browser applies while painting the React DOM.

 172 | .top-bar-icon-btn {
     | Opens a rule for selector `.top-bar-icon-btn`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 173 |   width: 36px;
     | Sets CSS property `width` to `36px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 174 |   height: 36px;
     | Sets CSS property `height` to `36px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 175 |   border: 1px solid var(--border);
     | Sets CSS property `border` to `1px solid var(--border)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 176 |   border-radius: var(--radius-sm);
     | Sets CSS property `border-radius` to `var(--radius-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 177 |   background: transparent;
     | Sets CSS property `background` to `transparent`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 178 |   color: var(--text-soft);
     | Sets CSS property `color` to `var(--text-soft)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 179 |   cursor: pointer;
     | Sets CSS property `cursor` to `pointer`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 180 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 181 |   align-items: center;
     | Sets CSS property `align-items` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 182 |   justify-content: center;
     | Sets CSS property `justify-content` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 183 |   flex-shrink: 0;
     | Sets CSS property `flex-shrink` to `0`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 184 |   transition: all 0.15s;
     | Sets CSS property `transition` to `all 0.15s`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 185 |   text-decoration: none;
     | Sets CSS property `text-decoration` to `none`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 186 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 187 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 188 | .top-bar-menu-btn:hover,
     | CSS line `.top-bar-menu-btn:hover,`. It is part of the stylesheet the browser applies while painting the React DOM.

 189 | .top-bar-icon-btn:hover {
     | Opens a rule for selector `.top-bar-icon-btn:hover`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 190 |   border-color: var(--border-active);
     | Sets CSS property `border-color` to `var(--border-active)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 191 |   color: var(--text);
     | Sets CSS property `color` to `var(--text)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 192 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 193 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 194 | .top-bar-icon-btn svg { width: 18px; height: 18px; }
     | CSS line `.top-bar-icon-btn svg { width: 18px; height: 18px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 195 | .top-bar-logout-btn { display: none; }
     | CSS line `.top-bar-logout-btn { display: none; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 196 | .top-bar-more-btn { display: none; }
     | CSS line `.top-bar-more-btn { display: none; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 197 | .top-bar-feedback-btn { display: none; }
     | CSS line `.top-bar-feedback-btn { display: none; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 198 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 199 | .top-bar-brand {
     | Opens a rule for selector `.top-bar-brand`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 200 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 201 |   align-items: center;
     | Sets CSS property `align-items` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 202 |   gap: var(--space-2);
     | Sets CSS property `gap` to `var(--space-2)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 203 |   min-width: 0;
     | Sets CSS property `min-width` to `0`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 204 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 205 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 206 | .top-bar-page-title {
     | Opens a rule for selector `.top-bar-page-title`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 207 |   font-size: var(--text-base);
     | Sets CSS property `font-size` to `var(--text-base)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 208 |   font-weight: 700;
     | Sets CSS property `font-weight` to `700`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 209 |   color: var(--text);
     | Sets CSS property `color` to `var(--text)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 210 |   white-space: nowrap;
     | Sets CSS property `white-space` to `nowrap`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 211 |   overflow: hidden;
     | Sets CSS property `overflow` to `hidden`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 212 |   text-overflow: ellipsis;
     | Sets CSS property `text-overflow` to `ellipsis`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 213 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 214 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 215 | /* ── Sidebar ────────────────────────────────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── Sidebar ────────────────────────────────────────── */

 216 | .sidebar {
     | Opens a rule for selector `.sidebar`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 217 |   width: var(--sidebar-w);
     | Sets CSS property `width` to `var(--sidebar-w)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 218 |   min-width: var(--sidebar-w);
     | Sets CSS property `min-width` to `var(--sidebar-w)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 219 |   height: 100vh;
     | Sets CSS property `height` to `100vh`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 220 |   background: var(--surface);
     | Sets CSS property `background` to `var(--surface)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 221 |   border-right: 1px solid var(--border);
     | Sets CSS property `border-right` to `1px solid var(--border)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 222 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 223 |   flex-direction: column;
     | Sets CSS property `flex-direction` to `column`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 224 |   padding: var(--space-5) var(--space-4);
     | Sets CSS property `padding` to `var(--space-5) var(--space-4)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 225 |   gap: 0;
     | Sets CSS property `gap` to `0`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 226 |   overflow-y: auto;
     | Sets CSS property `overflow-y` to `auto`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 227 |   transition: background 0.3s;
     | Sets CSS property `transition` to `background 0.3s`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 228 |   flex-shrink: 0;
     | Sets CSS property `flex-shrink` to `0`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 229 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 230 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 231 | .sidebar-brand {
     | Opens a rule for selector `.sidebar-brand`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 232 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 233 |   align-items: center;
     | Sets CSS property `align-items` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 234 |   gap: var(--space-3);
     | Sets CSS property `gap` to `var(--space-3)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 235 |   padding: 6px 6px 18px;
     | Sets CSS property `padding` to `6px 6px 18px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 236 |   border-bottom: 1px solid var(--border);
     | Sets CSS property `border-bottom` to `1px solid var(--border)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 237 |   margin-bottom: var(--space-3);
     | Sets CSS property `margin-bottom` to `var(--space-3)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 238 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 239 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 240 | .sidebar-logo {
     | Opens a rule for selector `.sidebar-logo`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 241 |   width: 36px;
     | Sets CSS property `width` to `36px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 242 |   height: 36px;
     | Sets CSS property `height` to `36px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 243 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 244 |   align-items: center;
     | Sets CSS property `align-items` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 245 |   justify-content: center;
     | Sets CSS property `justify-content` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 246 |   flex-shrink: 0;
     | Sets CSS property `flex-shrink` to `0`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 247 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 248 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 249 | .sidebar-title {
     | Opens a rule for selector `.sidebar-title`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 250 |   font-weight: 700;
     | Sets CSS property `font-weight` to `700`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 251 |   font-size: var(--text-sm);
     | Sets CSS property `font-size` to `var(--text-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 252 |   color: var(--text);
     | Sets CSS property `color` to `var(--text)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 253 |   line-height: 1.2;
     | Sets CSS property `line-height` to `1.2`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 254 |   letter-spacing: -0.01em;
     | Sets CSS property `letter-spacing` to `-0.01em`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 255 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 256 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 257 | .sidebar-title span {
     | Opens a rule for selector `.sidebar-title span`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 258 |   background: var(--brand-gradient);
     | Sets CSS property `background` to `var(--brand-gradient)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 259 |   -webkit-background-clip: text;
     | Sets CSS property `-webkit-background-clip` to `text`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 260 |   -webkit-text-fill-color: transparent;
     | Sets CSS property `-webkit-text-fill-color` to `transparent`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 261 |   background-clip: text;
     | Sets CSS property `background-clip` to `text`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 262 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 263 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 264 | .sidebar-subtitle {
     | Opens a rule for selector `.sidebar-subtitle`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 265 |   font-size: var(--text-xs);
     | Sets CSS property `font-size` to `var(--text-xs)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 266 |   color: var(--muted);
     | Sets CSS property `color` to `var(--muted)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 267 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 268 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 269 | .sidebar-nav-section {
     | Opens a rule for selector `.sidebar-nav-section`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 270 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 271 |   flex-direction: column;
     | Sets CSS property `flex-direction` to `column`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 272 |   gap: 1px;
     | Sets CSS property `gap` to `1px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 273 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 274 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 275 | .sidebar-section-label {
     | Opens a rule for selector `.sidebar-section-label`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 276 |   font-size: var(--text-xs);
     | Sets CSS property `font-size` to `var(--text-xs)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 277 |   font-weight: 700;
     | Sets CSS property `font-weight` to `700`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 278 |   color: var(--muted);
     | Sets CSS property `color` to `var(--muted)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 279 |   text-transform: uppercase;
     | Sets CSS property `text-transform` to `uppercase`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 280 |   letter-spacing: 0.8px;
     | Sets CSS property `letter-spacing` to `0.8px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 281 |   padding: 6px 10px 3px;
     | Sets CSS property `padding` to `6px 10px 3px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 282 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 283 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 284 | /* Primary nav items */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* Primary nav items */

 285 | .nav-item {
     | Opens a rule for selector `.nav-item`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 286 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 287 |   align-items: center;
     | Sets CSS property `align-items` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 288 |   gap: var(--space-2);
     | Sets CSS property `gap` to `var(--space-2)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 289 |   padding: 9px 10px;
     | Sets CSS property `padding` to `9px 10px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 290 |   border-radius: var(--radius-sm);
     | Sets CSS property `border-radius` to `var(--radius-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 291 |   cursor: pointer;
     | Sets CSS property `cursor` to `pointer`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 292 |   text-decoration: none;
     | Sets CSS property `text-decoration` to `none`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 293 |   color: var(--text-soft);
     | Sets CSS property `color` to `var(--text-soft)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 294 |   font-size: var(--text-sm);
     | Sets CSS property `font-size` to `var(--text-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 295 |   font-weight: 500;
     | Sets CSS property `font-weight` to `500`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 296 |   transition: all 0.15s;
     | Sets CSS property `transition` to `all 0.15s`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 297 |   border: none;
     | Sets CSS property `border` to `none`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 298 |   background: transparent;
     | Sets CSS property `background` to `transparent`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 299 |   width: 100%;
     | Sets CSS property `width` to `100%`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 300 |   text-align: left;
     | Sets CSS property `text-align` to `left`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 301 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 302 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 303 | .nav-item:hover { background: var(--indigo-dim); color: var(--indigo-light); }
     | CSS line `.nav-item:hover { background: var(--indigo-dim); color: var(--indigo-light); }`. It is part of the stylesheet the browser applies while painting the React DOM.

 304 | .nav-item.active {
     | Opens a rule for selector `.nav-item.active`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 305 |   background: var(--indigo-dim);
     | Sets CSS property `background` to `var(--indigo-dim)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 306 |   color: var(--indigo-light);
     | Sets CSS property `color` to `var(--indigo-light)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 307 |   font-weight: 600;
     | Sets CSS property `font-weight` to `600`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 308 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 309 | .nav-item svg { width: 18px; height: 18px; flex-shrink: 0; }
     | CSS line `.nav-item svg { width: 18px; height: 18px; flex-shrink: 0; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 310 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 311 | /* Smaller secondary nav items */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* Smaller secondary nav items */

 312 | .nav-item-sm {
     | Opens a rule for selector `.nav-item-sm`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 313 |   padding: 6px 10px;
     | Sets CSS property `padding` to `6px 10px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 314 |   font-size: var(--text-xs);
     | Sets CSS property `font-size` to `var(--text-xs)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 315 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 316 | .nav-item-sm svg { width: 15px; height: 15px; }
     | CSS line `.nav-item-sm svg { width: 15px; height: 15px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 317 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 318 | /* Feedback nav item — subtle accent so it's discoverable but not shouting */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* Feedback nav item — subtle accent so it's discoverable but not shouting */

 319 | .nav-item-feedback {
     | Opens a rule for selector `.nav-item-feedback`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 320 |   background: var(--indigo-dim);
     | Sets CSS property `background` to `var(--indigo-dim)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 321 |   color: var(--indigo-light);
     | Sets CSS property `color` to `var(--indigo-light)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 322 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 323 | .nav-item-feedback:hover { background: rgba(99, 102, 241, 0.22); color: var(--indigo-light); }
     | CSS line `.nav-item-feedback:hover { background: rgba(99, 102, 241, 0.22); color: var(--indigo-light); }`. It is part of the stylesheet the browser applies while painting the React DOM.

 324 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 325 | /* Compact connector rows */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* Compact connector rows */

 326 | .connector-row {
     | Opens a rule for selector `.connector-row`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 327 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 328 |   align-items: center;
     | Sets CSS property `align-items` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 329 |   gap: var(--space-2);
     | Sets CSS property `gap` to `var(--space-2)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 330 |   padding: 5px 10px;
     | Sets CSS property `padding` to `5px 10px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 331 |   border-radius: var(--radius-sm);
     | Sets CSS property `border-radius` to `var(--radius-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 332 |   text-decoration: none;
     | Sets CSS property `text-decoration` to `none`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 333 |   color: var(--text-soft);
     | Sets CSS property `color` to `var(--text-soft)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 334 |   font-size: var(--text-xs);
     | Sets CSS property `font-size` to `var(--text-xs)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 335 |   font-weight: 500;
     | Sets CSS property `font-weight` to `500`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 336 |   transition: all 0.15s;
     | Sets CSS property `transition` to `all 0.15s`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 337 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 338 | .connector-row:hover { background: var(--indigo-dim); color: var(--text); }
     | CSS line `.connector-row:hover { background: var(--indigo-dim); color: var(--text); }`. It is part of the stylesheet the browser applies while painting the React DOM.

 339 | .connector-row.active { background: var(--indigo-dim); color: var(--indigo-light); }
     | CSS line `.connector-row.active { background: var(--indigo-dim); color: var(--indigo-light); }`. It is part of the stylesheet the browser applies while painting the React DOM.

 340 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 341 | .connector-row-icon {
     | Opens a rule for selector `.connector-row-icon`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 342 |   width: 20px;
     | Sets CSS property `width` to `20px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 343 |   height: 20px;
     | Sets CSS property `height` to `20px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 344 |   border-radius: 5px;
     | Sets CSS property `border-radius` to `5px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 345 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 346 |   align-items: center;
     | Sets CSS property `align-items` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 347 |   justify-content: center;
     | Sets CSS property `justify-content` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 348 |   flex-shrink: 0;
     | Sets CSS property `flex-shrink` to `0`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 349 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 350 | .connector-row-label { flex: 1; }
     | CSS line `.connector-row-label { flex: 1; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 351 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 352 | /* Pinned energy in sidebar */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* Pinned energy in sidebar */

 353 | .sidebar-energy {
     | Opens a rule for selector `.sidebar-energy`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 354 |   margin-top: var(--space-3);
     | Sets CSS property `margin-top` to `var(--space-3)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 355 |   padding: var(--space-2) 0;
     | Sets CSS property `padding` to `var(--space-2) 0`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 356 |   border-top: 1px solid var(--border);
     | Sets CSS property `border-top` to `1px solid var(--border)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 357 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 358 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 359 | .sidebar-footer {
     | Opens a rule for selector `.sidebar-footer`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 360 |   margin-top: auto;
     | Sets CSS property `margin-top` to `auto`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 361 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 362 |   flex-direction: column;
     | Sets CSS property `flex-direction` to `column`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 363 |   gap: var(--space-2);
     | Sets CSS property `gap` to `var(--space-2)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 364 |   padding-top: var(--space-3);
     | Sets CSS property `padding-top` to `var(--space-3)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 365 |   border-top: 1px solid var(--border);
     | Sets CSS property `border-top` to `1px solid var(--border)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 366 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 367 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 368 | /* ── Energy Control ─────────────────────────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── Energy Control ─────────────────────────────────── */

 369 | .energy-control {}
     | CSS line `.energy-control {}`. It is part of the stylesheet the browser applies while painting the React DOM.

 370 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 371 | .energy-control-row {
     | Opens a rule for selector `.energy-control-row`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 372 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 373 |   gap: var(--space-2);
     | Sets CSS property `gap` to `var(--space-2)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 374 |   align-items: center;
     | Sets CSS property `align-items` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 375 |   flex-wrap: wrap;
     | Sets CSS property `flex-wrap` to `wrap`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 376 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 377 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 378 | .energy-current-label {
     | Opens a rule for selector `.energy-current-label`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 379 |   font-size: var(--text-xs);
     | Sets CSS property `font-size` to `var(--text-xs)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 380 |   color: var(--muted);
     | Sets CSS property `color` to `var(--muted)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 381 |   margin-left: var(--space-1);
     | Sets CSS property `margin-left` to `var(--space-1)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 382 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 383 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 384 | /* Compact dots for sidebar */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* Compact dots for sidebar */

 385 | .energy-control-compact {
     | Opens a rule for selector `.energy-control-compact`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 386 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 387 |   gap: 5px;
     | Sets CSS property `gap` to `5px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 388 |   padding: 4px 6px;
     | Sets CSS property `padding` to `4px 6px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 389 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 390 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 391 | .energy-dot {
     | Opens a rule for selector `.energy-dot`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 392 |   width: 26px;
     | Sets CSS property `width` to `26px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 393 |   height: 26px;
     | Sets CSS property `height` to `26px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 394 |   border-radius: 50%;
     | Sets CSS property `border-radius` to `50%`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 395 |   border: 2px solid var(--border);
     | Sets CSS property `border` to `2px solid var(--border)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 396 |   cursor: pointer;
     | Sets CSS property `cursor` to `pointer`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 397 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 398 |   align-items: center;
     | Sets CSS property `align-items` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 399 |   justify-content: center;
     | Sets CSS property `justify-content` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 400 |   font-size: 11px;
     | Sets CSS property `font-size` to `11px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 401 |   transition: all 0.15s;
     | Sets CSS property `transition` to `all 0.15s`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 402 |   background: transparent;
     | Sets CSS property `background` to `transparent`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 403 |   color: var(--muted);
     | Sets CSS property `color` to `var(--muted)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 404 |   padding: 0;
     | Sets CSS property `padding` to `0`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 405 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 406 | .energy-dot.filled {
     | Opens a rule for selector `.energy-dot.filled`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 407 |   border-color: var(--amber);
     | Sets CSS property `border-color` to `var(--amber)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 408 |   background: var(--amber-dim);
     | Sets CSS property `background` to `var(--amber-dim)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 409 |   color: var(--amber);
     | Sets CSS property `color` to `var(--amber)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 410 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 411 | .energy-dot:hover { transform: scale(1.1); }
     | CSS line `.energy-dot:hover { transform: scale(1.1); }`. It is part of the stylesheet the browser applies while painting the React DOM.

 412 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 413 | /* Large energy buttons (Home page) */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* Large energy buttons (Home page) */

 414 | .energy-btn {
     | Opens a rule for selector `.energy-btn`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 415 |   width: 44px;
     | Sets CSS property `width` to `44px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 416 |   height: 44px;
     | Sets CSS property `height` to `44px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 417 |   border-radius: 10px;
     | Sets CSS property `border-radius` to `10px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 418 |   border: 2px solid var(--border);
     | Sets CSS property `border` to `2px solid var(--border)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 419 |   background: transparent;
     | Sets CSS property `background` to `transparent`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 420 |   cursor: pointer;
     | Sets CSS property `cursor` to `pointer`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 421 |   font-size: 18px;
     | Sets CSS property `font-size` to `18px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 422 |   transition: all 0.15s;
     | Sets CSS property `transition` to `all 0.15s`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 423 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 424 |   align-items: center;
     | Sets CSS property `align-items` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 425 |   justify-content: center;
     | Sets CSS property `justify-content` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 426 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 427 | .energy-btn:hover { transform: scale(1.1); }
     | CSS line `.energy-btn:hover { transform: scale(1.1); }`. It is part of the stylesheet the browser applies while painting the React DOM.

 428 | .energy-btn.selected {
     | Opens a rule for selector `.energy-btn.selected`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 429 |   border-color: var(--amber);
     | Sets CSS property `border-color` to `var(--amber)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 430 |   background: var(--amber-dim);
     | Sets CSS property `background` to `var(--amber-dim)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 431 |   transform: scale(1.1);
     | Sets CSS property `transform` to `scale(1.1)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 432 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 433 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 434 | /* ── Theme / Logout ─────────────────────────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── Theme / Logout ─────────────────────────────────── */

 435 | .theme-toggle {
     | Opens a rule for selector `.theme-toggle`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 436 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 437 |   align-items: center;
     | Sets CSS property `align-items` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 438 |   gap: var(--space-2);
     | Sets CSS property `gap` to `var(--space-2)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 439 |   padding: 7px 10px;
     | Sets CSS property `padding` to `7px 10px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 440 |   border-radius: var(--radius-sm);
     | Sets CSS property `border-radius` to `var(--radius-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 441 |   cursor: pointer;
     | Sets CSS property `cursor` to `pointer`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 442 |   border: 1px solid var(--border);
     | Sets CSS property `border` to `1px solid var(--border)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 443 |   background: transparent;
     | Sets CSS property `background` to `transparent`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 444 |   color: var(--muted);
     | Sets CSS property `color` to `var(--muted)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 445 |   font-size: var(--text-xs);
     | Sets CSS property `font-size` to `var(--text-xs)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 446 |   font-family: inherit;
     | Sets CSS property `font-family` to `inherit`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 447 |   transition: all 0.15s;
     | Sets CSS property `transition` to `all 0.15s`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 448 |   width: 100%;
     | Sets CSS property `width` to `100%`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 449 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 450 | .theme-toggle:hover { border-color: var(--indigo); color: var(--text); }
     | CSS line `.theme-toggle:hover { border-color: var(--indigo); color: var(--text); }`. It is part of the stylesheet the browser applies while painting the React DOM.

 451 | .theme-toggle svg { width: 15px; height: 15px; }
     | CSS line `.theme-toggle svg { width: 15px; height: 15px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 452 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 453 | .logout-btn {
     | Opens a rule for selector `.logout-btn`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 454 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 455 |   align-items: center;
     | Sets CSS property `align-items` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 456 |   gap: var(--space-2);
     | Sets CSS property `gap` to `var(--space-2)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 457 |   padding: 7px 10px;
     | Sets CSS property `padding` to `7px 10px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 458 |   border-radius: var(--radius-sm);
     | Sets CSS property `border-radius` to `var(--radius-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 459 |   cursor: pointer;
     | Sets CSS property `cursor` to `pointer`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 460 |   border: 1px solid var(--border);
     | Sets CSS property `border` to `1px solid var(--border)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 461 |   background: transparent;
     | Sets CSS property `background` to `transparent`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 462 |   color: var(--muted);
     | Sets CSS property `color` to `var(--muted)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 463 |   font-size: var(--text-xs);
     | Sets CSS property `font-size` to `var(--text-xs)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 464 |   font-family: inherit;
     | Sets CSS property `font-family` to `inherit`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 465 |   transition: all 0.15s;
     | Sets CSS property `transition` to `all 0.15s`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 466 |   width: 100%;
     | Sets CSS property `width` to `100%`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 467 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 468 | .logout-btn:hover { border-color: var(--red); color: var(--red); }
     | CSS line `.logout-btn:hover { border-color: var(--red); color: var(--red); }`. It is part of the stylesheet the browser applies while painting the React DOM.

 469 | .logout-btn svg { width: 15px; height: 15px; }
     | CSS line `.logout-btn svg { width: 15px; height: 15px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 470 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 471 | .support-btn {
     | Opens a rule for selector `.support-btn`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 472 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 473 |   align-items: center;
     | Sets CSS property `align-items` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 474 |   gap: var(--space-2);
     | Sets CSS property `gap` to `var(--space-2)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 475 |   padding: 7px 10px;
     | Sets CSS property `padding` to `7px 10px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 476 |   border-radius: var(--radius-sm);
     | Sets CSS property `border-radius` to `var(--radius-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 477 |   cursor: pointer;
     | Sets CSS property `cursor` to `pointer`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 478 |   border: 1px solid var(--border);
     | Sets CSS property `border` to `1px solid var(--border)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 479 |   background: transparent;
     | Sets CSS property `background` to `transparent`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 480 |   color: var(--muted);
     | Sets CSS property `color` to `var(--muted)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 481 |   font-size: var(--text-xs);
     | Sets CSS property `font-size` to `var(--text-xs)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 482 |   font-family: inherit;
     | Sets CSS property `font-family` to `inherit`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 483 |   text-decoration: none;
     | Sets CSS property `text-decoration` to `none`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 484 |   transition: all 0.15s;
     | Sets CSS property `transition` to `all 0.15s`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 485 |   width: 100%;
     | Sets CSS property `width` to `100%`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 486 |   box-sizing: border-box;
     | Sets CSS property `box-sizing` to `border-box`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 487 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 488 | .support-btn:hover { border-color: var(--amber); color: var(--amber); background: var(--amber-dim); }
     | CSS line `.support-btn:hover { border-color: var(--amber); color: var(--amber); background: var(--amber-dim); }`. It is part of the stylesheet the browser applies while painting the React DOM.

 489 | .support-btn svg { width: 15px; height: 15px; }
     | CSS line `.support-btn svg { width: 15px; height: 15px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 490 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 491 | /* ── Sidebar Backdrop ────────────────────────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── Sidebar Backdrop ────────────────────────────────── */

 492 | .sidebar-backdrop {
     | Opens a rule for selector `.sidebar-backdrop`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 493 |   display: none;
     | Sets CSS property `display` to `none`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 494 |   position: fixed;
     | Sets CSS property `position` to `fixed`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 495 |   inset: 0;
     | Sets CSS property `inset` to `0`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 496 |   background: rgba(0, 0, 0, 0.5);
     | Sets CSS property `background` to `rgba(0, 0, 0, 0.5)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 497 |   z-index: 99;
     | Sets CSS property `z-index` to `99`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 498 |   backdrop-filter: blur(2px);
     | Sets CSS property `backdrop-filter` to `blur(2px)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 499 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 500 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 501 | /* ── Main Content ────────────────────────────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── Main Content ────────────────────────────────────── */

 502 | .main-content {
     | Opens a rule for selector `.main-content`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 503 |   flex: 1;
     | Sets CSS property `flex` to `1`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 504 |   overflow-y: auto;
     | Sets CSS property `overflow-y` to `auto`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 505 |   overflow-x: hidden;
     | Sets CSS property `overflow-x` to `hidden`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 506 |   padding: var(--space-6) 32px;
     | Sets CSS property `padding` to `var(--space-6) 32px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 507 |   min-width: 0;
     | Sets CSS property `min-width` to `0`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 508 |   min-height: 0;
     | Sets CSS property `min-height` to `0`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 509 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 510 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 511 | /* ── Bottom Nav (mobile) ─────────────────────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── Bottom Nav (mobile) ─────────────────────────────── */

 512 | .bottom-nav {
     | Opens a rule for selector `.bottom-nav`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 513 |   display: none;
     | Sets CSS property `display` to `none`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 514 |   height: var(--bottom-nav-h);
     | Sets CSS property `height` to `var(--bottom-nav-h)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 515 |   background: var(--surface);
     | Sets CSS property `background` to `var(--surface)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 516 |   border-top: 1px solid var(--border);
     | Sets CSS property `border-top` to `1px solid var(--border)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 517 |   flex-shrink: 0;
     | Sets CSS property `flex-shrink` to `0`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 518 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 519 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 520 | .bottom-nav-item {
     | Opens a rule for selector `.bottom-nav-item`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 521 |   flex: 1;
     | Sets CSS property `flex` to `1`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 522 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 523 |   flex-direction: column;
     | Sets CSS property `flex-direction` to `column`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 524 |   align-items: center;
     | Sets CSS property `align-items` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 525 |   justify-content: center;
     | Sets CSS property `justify-content` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 526 |   gap: 3px;
     | Sets CSS property `gap` to `3px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 527 |   padding: 8px 4px;
     | Sets CSS property `padding` to `8px 4px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 528 |   text-decoration: none;
     | Sets CSS property `text-decoration` to `none`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 529 |   color: var(--muted);
     | Sets CSS property `color` to `var(--muted)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 530 |   font-size: 11px;
     | Sets CSS property `font-size` to `11px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 531 |   font-weight: 600;
     | Sets CSS property `font-weight` to `600`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 532 |   transition: color 0.15s, transform 0.1s;
     | Sets CSS property `transition` to `color 0.15s, transform 0.1s`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 533 |   min-height: 56px;
     | Sets CSS property `min-height` to `56px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 534 |   cursor: pointer;
     | Sets CSS property `cursor` to `pointer`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 535 |   border: none;
     | Sets CSS property `border` to `none`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 536 |   background: transparent;
     | Sets CSS property `background` to `transparent`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 537 |   font-family: inherit;
     | Sets CSS property `font-family` to `inherit`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 538 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 539 | .bottom-nav-item svg { width: 22px; height: 22px; }
     | CSS line `.bottom-nav-item svg { width: 22px; height: 22px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 540 | .bottom-nav-item.active { color: var(--indigo-light); }
     | CSS line `.bottom-nav-item.active { color: var(--indigo-light); }`. It is part of the stylesheet the browser applies while painting the React DOM.

 541 | .bottom-nav-item:hover { color: var(--text-soft); }
     | CSS line `.bottom-nav-item:hover { color: var(--text-soft); }`. It is part of the stylesheet the browser applies while painting the React DOM.

 542 | .bottom-nav-item:active { transform: scale(0.9); }
     | CSS line `.bottom-nav-item:active { transform: scale(0.9); }`. It is part of the stylesheet the browser applies while painting the React DOM.

 543 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 544 | /* ── Responsive ──────────────────────────────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── Responsive ──────────────────────────────────────── */

 545 | @media (max-width: 1024px) {
     | Opens a media query `@media (max-width: 1024px) {`. The rules inside apply only when that screen condition is true, so the same components reflow on a phone.

 546 |   .main-content { padding: var(--space-5) var(--space-6); }
     | CSS line `.main-content { padding: var(--space-5) var(--space-6); }`. It is part of the stylesheet the browser applies while painting the React DOM.

 547 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 548 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 549 | @media (max-width: 768px) {
     | Opens a media query `@media (max-width: 768px) {`. The rules inside apply only when that screen condition is true, so the same components reflow on a phone.

 550 |   .sidebar {
     | Opens a rule for selector `.sidebar`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 551 |     position: fixed;
     | Sets CSS property `position` to `fixed`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 552 |     top: 0;
     | Sets CSS property `top` to `0`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 553 |     left: 0;
     | Sets CSS property `left` to `0`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 554 |     height: 100vh;
     | Sets CSS property `height` to `100vh`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 555 |     z-index: 100;
     | Sets CSS property `z-index` to `100`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 556 |     transform: translateX(-100%);
     | Sets CSS property `transform` to `translateX(-100%)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 557 |     transition: transform 0.28s cubic-bezier(0.4, 0, 0.2, 1);
     | Sets CSS property `transition` to `transform 0.28s cubic-bezier(0.4, 0, 0.2, 1)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 558 |     box-shadow: 4px 0 24px rgba(0, 0, 0, 0.3);
     | Sets CSS property `box-shadow` to `4px 0 24px rgba(0, 0, 0, 0.3)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 559 |   }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 560 |   .sidebar.open { transform: translateX(0); }
     | CSS line `.sidebar.open { transform: translateX(0); }`. It is part of the stylesheet the browser applies while painting the React DOM.

 561 |   .sidebar-backdrop { display: block; }
     | CSS line `.sidebar-backdrop { display: block; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 562 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 563 |   /* Hide hamburger on mobile — bottom nav + More sheet handles it */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* Hide hamburger on mobile — bottom nav + More sheet handles it */

 564 |   .top-bar-menu-btn { display: none; }
     | CSS line `.top-bar-menu-btn { display: none; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 565 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 566 |   /* Show logout in top bar on mobile (sidebar logout not visible) */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* Show logout in top bar on mobile (sidebar logout not visible) */

 567 |   .top-bar-logout-btn { display: flex; }
     | CSS line `.top-bar-logout-btn { display: flex; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 568 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 569 |   /* Show "More" trigger on mobile — opens the bottom sheet with Focus Timer, Focus Shield, etc. */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* Show "More" trigger on mobile — opens the bottom sheet with Focus Timer, Focus Shield, etc. */

 570 |   .top-bar-more-btn { display: flex; }
     | CSS line `.top-bar-more-btn { display: flex; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 571 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 572 |   /* Show feedback icon in top bar on mobile — sidebar nav item handles desktop */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* Show feedback icon in top bar on mobile — sidebar nav item handles desktop */

 573 |   .top-bar-feedback-btn { display: flex; }
     | CSS line `.top-bar-feedback-btn { display: flex; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 574 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 575 |   .bottom-nav { display: flex; }
     | CSS line `.bottom-nav { display: flex; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 576 |   .bottom-sheet-overlay {
     | Opens a rule for selector `.bottom-sheet-overlay`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 577 |     display: block;
     | Sets CSS property `display` to `block`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 578 |     opacity: 0;
     | Sets CSS property `opacity` to `0`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 579 |     pointer-events: none;
     | Sets CSS property `pointer-events` to `none`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 580 |     transition: opacity 0.3s;
     | Sets CSS property `transition` to `opacity 0.3s`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 581 |   }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 582 |   .bottom-sheet-overlay.open {
     | Opens a rule for selector `.bottom-sheet-overlay.open`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 583 |     opacity: 1;
     | Sets CSS property `opacity` to `1`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 584 |     pointer-events: auto;
     | Sets CSS property `pointer-events` to `auto`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 585 |   }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 586 |   .bottom-sheet { display: block; }
     | CSS line `.bottom-sheet { display: block; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 587 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 588 |   .main-content {
     | Opens a rule for selector `.main-content`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 589 |     padding: var(--space-4);
     | Sets CSS property `padding` to `var(--space-4)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 590 |     padding-bottom: calc(var(--bottom-nav-h) + var(--space-4));
     | Sets CSS property `padding-bottom` to `calc(var(--bottom-nav-h) + var(--space-4))`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 591 |   }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 592 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 593 |   .page-title { font-size: 20px; }
     | CSS line `.page-title { font-size: 20px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 594 |   .page-subtitle { margin-bottom: 16px; }
     | CSS line `.page-subtitle { margin-bottom: 16px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 595 |   .connectors-page { padding: 0; }
     | CSS line `.connectors-page { padding: 0; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 596 |   .ring-container { width: 180px; height: 180px; }
     | CSS line `.ring-container { width: 180px; height: 180px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 597 |   .ring-svg { width: 180px; height: 180px; }
     | CSS line `.ring-svg { width: 180px; height: 180px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 598 |   .ring-time { font-size: 32px; }
     | CSS line `.ring-time { font-size: 32px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 599 |   .focus-overlay-card { padding: 24px 20px; }
     | CSS line `.focus-overlay-card { padding: 24px 20px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 600 |   .connector-card { flex-wrap: wrap; gap: 12px; }
     | CSS line `.connector-card { flex-wrap: wrap; gap: 12px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 601 |   .connector-card-actions { flex-direction: row; align-items: center; width: 100%; }
     | CSS line `.connector-card-actions { flex-direction: row; align-items: center; width: 100%; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 602 |   .stat-value { font-size: 28px; }
     | CSS line `.stat-value { font-size: 28px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 603 |   .audio-time { font-size: 34px; }
     | CSS line `.audio-time { font-size: 34px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 604 |   .task-actions { padding-left: 0; flex-wrap: wrap; }
     | CSS line `.task-actions { padding-left: 0; flex-wrap: wrap; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 605 |   .task-meta { padding-left: 0; }
     | CSS line `.task-meta { padding-left: 0; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 606 |   .subtask-list { padding-left: 0; }
     | CSS line `.subtask-list { padding-left: 0; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 607 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 608 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 609 | /* ── Touch feedback ──────────────────────────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── Touch feedback ──────────────────────────────────── */

 610 | .btn:active:not(:disabled) { transform: scale(0.97) !important; opacity: 0.9; }
     | CSS line `.btn:active:not(:disabled) { transform: scale(0.97) !important; opacity: 0.9; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 611 | .task-check:active { transform: scale(0.88); }
     | CSS line `.task-check:active { transform: scale(0.88); }`. It is part of the stylesheet the browser applies while painting the React DOM.

 612 | .energy-btn:active { transform: scale(1.05); }
     | CSS line `.energy-btn:active { transform: scale(1.05); }`. It is part of the stylesheet the browser applies while painting the React DOM.

 613 | .energy-dot:active { transform: scale(1.2); }
     | CSS line `.energy-dot:active { transform: scale(1.2); }`. It is part of the stylesheet the browser applies while painting the React DOM.

 614 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 615 | @media (max-width: 480px) {
     | Opens a media query `@media (max-width: 480px) {`. The rules inside apply only when that screen condition is true, so the same components reflow on a phone.

 616 |   .main-content { padding: 12px; padding-bottom: calc(var(--bottom-nav-h) + 12px); }
     | CSS line `.main-content { padding: 12px; padding-bottom: calc(var(--bottom-nav-h) + 12px); }`. It is part of the stylesheet the browser applies while painting the React DOM.

 617 |   .card { padding: 14px; }
     | CSS line `.card { padding: 14px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 618 |   .card-sm { padding: 10px; }
     | CSS line `.card-sm { padding: 10px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 619 |   .page-title { font-size: 18px; }
     | CSS line `.page-title { font-size: 18px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 620 |   .ring-container { width: 160px; height: 160px; }
     | CSS line `.ring-container { width: 160px; height: 160px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 621 |   .ring-svg { width: 160px; height: 160px; }
     | CSS line `.ring-svg { width: 160px; height: 160px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 622 |   .ring-time { font-size: 28px; }
     | CSS line `.ring-time { font-size: 28px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 623 |   .btn { font-size: 13px; padding: 8px 12px; }
     | CSS line `.btn { font-size: 13px; padding: 8px 12px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 624 |   .btn-lg { font-size: 14px; padding: 10px 18px; }
     | CSS line `.btn-lg { font-size: 14px; padding: 10px 18px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 625 |   .stat-tile { padding: 12px 14px; }
     | CSS line `.stat-tile { padding: 12px 14px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 626 |   .stat-value { font-size: 24px; }
     | CSS line `.stat-value { font-size: 24px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 627 |   .what-next-task { font-size: 16px; }
     | CSS line `.what-next-task { font-size: 16px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 628 |   .audio-time { font-size: 28px; }
     | CSS line `.audio-time { font-size: 28px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 629 |   .audio-player { padding: 20px 16px; }
     | CSS line `.audio-player { padding: 20px 16px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 630 |   .connectors-toast { top: 12px; right: 12px; left: 12px; right: auto; width: calc(100% - 24px); }
     | CSS line `.connectors-toast { top: 12px; right: 12px; left: 12px; right: auto; width: calc(100% - 24px); }`. It is part of the stylesheet the browser applies while painting the React DOM.

 631 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 632 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 633 | /* ── Page structure ─────────────────────────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── Page structure ─────────────────────────────────── */

 634 | .page-title {
     | Opens a rule for selector `.page-title`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 635 |   font-size: var(--text-xl);
     | Sets CSS property `font-size` to `var(--text-xl)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 636 |   font-weight: 800;
     | Sets CSS property `font-weight` to `800`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 637 |   color: var(--text);
     | Sets CSS property `color` to `var(--text)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 638 |   margin-bottom: 4px;
     | Sets CSS property `margin-bottom` to `4px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 639 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 640 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 641 | .page-subtitle {
     | Opens a rule for selector `.page-subtitle`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 642 |   font-size: var(--text-sm);
     | Sets CSS property `font-size` to `var(--text-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 643 |   color: var(--muted);
     | Sets CSS property `color` to `var(--muted)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 644 |   margin-bottom: var(--space-5);
     | Sets CSS property `margin-bottom` to `var(--space-5)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 645 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 646 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 647 | /* ── Cards ──────────────────────────────────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── Cards ──────────────────────────────────────────── */

 648 | .card {
     | Opens a rule for selector `.card`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 649 |   background: var(--card);
     | Sets CSS property `background` to `var(--card)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 650 |   border-radius: var(--radius);
     | Sets CSS property `border-radius` to `var(--radius)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 651 |   border: 1px solid var(--border);
     | Sets CSS property `border` to `1px solid var(--border)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 652 |   padding: var(--space-5);
     | Sets CSS property `padding` to `var(--space-5)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 653 |   box-shadow: var(--shadow-card);
     | Sets CSS property `box-shadow` to `var(--shadow-card)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 654 |   transition: background 0.3s, border 0.3s;
     | Sets CSS property `transition` to `background 0.3s, border 0.3s`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 655 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 656 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 657 | .card-sm { padding: 14px; }
     | CSS line `.card-sm { padding: 14px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 658 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 659 | .card-title {
     | Opens a rule for selector `.card-title`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 660 |   font-size: var(--text-xs);
     | Sets CSS property `font-size` to `var(--text-xs)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 661 |   font-weight: 700;
     | Sets CSS property `font-weight` to `700`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 662 |   color: var(--muted);
     | Sets CSS property `color` to `var(--muted)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 663 |   text-transform: uppercase;
     | Sets CSS property `text-transform` to `uppercase`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 664 |   letter-spacing: 0.8px;
     | Sets CSS property `letter-spacing` to `0.8px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 665 |   margin-bottom: 10px;
     | Sets CSS property `margin-bottom` to `10px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 666 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 667 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 668 | /* ── Grid layouts ───────────────────────────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── Grid layouts ───────────────────────────────────── */

 669 | .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: var(--space-4); }
     | CSS line `.grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: var(--space-4); }`. It is part of the stylesheet the browser applies while painting the React DOM.

 670 | .grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: var(--space-4); }
     | CSS line `.grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: var(--space-4); }`. It is part of the stylesheet the browser applies while painting the React DOM.

 671 | .grid-4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: var(--space-4); }
     | CSS line `.grid-4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: var(--space-4); }`. It is part of the stylesheet the browser applies while painting the React DOM.

 672 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 673 | .grid-main {
     | Opens a rule for selector `.grid-main`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 674 |   display: grid;
     | Sets CSS property `display` to `grid`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 675 |   grid-template-columns: 1fr 340px;
     | Sets CSS property `grid-template-columns` to `1fr 340px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 676 |   gap: var(--space-5);
     | Sets CSS property `gap` to `var(--space-5)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 677 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 678 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 679 | @media (max-width: 1024px) {
     | Opens a media query `@media (max-width: 1024px) {`. The rules inside apply only when that screen condition is true, so the same components reflow on a phone.

 680 |   .grid-main { grid-template-columns: 1fr; }
     | CSS line `.grid-main { grid-template-columns: 1fr; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 681 |   .grid-4 { grid-template-columns: repeat(2, 1fr); }
     | CSS line `.grid-4 { grid-template-columns: repeat(2, 1fr); }`. It is part of the stylesheet the browser applies while painting the React DOM.

 682 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 683 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 684 | @media (max-width: 768px) {
     | Opens a media query `@media (max-width: 768px) {`. The rules inside apply only when that screen condition is true, so the same components reflow on a phone.

 685 |   .grid-2, .grid-3, .grid-4, .grid-main { grid-template-columns: 1fr; }
     | CSS line `.grid-2, .grid-3, .grid-4, .grid-main { grid-template-columns: 1fr; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 686 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 687 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 688 | @media (min-width: 480px) and (max-width: 768px) {
     | Opens a media query `@media (min-width: 480px) and (max-width: 768px) {`. The rules inside apply only when that screen condition is true, so the same components reflow on a phone.

 689 |   .grid-3 { grid-template-columns: repeat(3, 1fr); }
     | CSS line `.grid-3 { grid-template-columns: repeat(3, 1fr); }`. It is part of the stylesheet the browser applies while painting the React DOM.

 690 |   .grid-2 { grid-template-columns: repeat(2, 1fr); }
     | CSS line `.grid-2 { grid-template-columns: repeat(2, 1fr); }`. It is part of the stylesheet the browser applies while painting the React DOM.

 691 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 692 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 693 | /* ── Buttons ────────────────────────────────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── Buttons ────────────────────────────────────────── */

 694 | .btn {
     | Opens a rule for selector `.btn`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 695 |   display: inline-flex;
     | Sets CSS property `display` to `inline-flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 696 |   align-items: center;
     | Sets CSS property `align-items` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 697 |   gap: 6px;
     | Sets CSS property `gap` to `6px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 698 |   padding: 9px 16px;
     | Sets CSS property `padding` to `9px 16px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 699 |   border-radius: var(--radius-sm);
     | Sets CSS property `border-radius` to `var(--radius-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 700 |   border: none;
     | Sets CSS property `border` to `none`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 701 |   cursor: pointer;
     | Sets CSS property `cursor` to `pointer`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 702 |   font-weight: 600;
     | Sets CSS property `font-weight` to `600`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 703 |   font-size: var(--text-sm);
     | Sets CSS property `font-size` to `var(--text-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 704 |   font-family: inherit;
     | Sets CSS property `font-family` to `inherit`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 705 |   transition: all 0.15s;
     | Sets CSS property `transition` to `all 0.15s`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 706 |   text-decoration: none;
     | Sets CSS property `text-decoration` to `none`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 707 |   white-space: nowrap;
     | Sets CSS property `white-space` to `nowrap`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 708 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 709 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 710 | .btn-primary {
     | Opens a rule for selector `.btn-primary`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 711 |   background: var(--brand-gradient);
     | Sets CSS property `background` to `var(--brand-gradient)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 712 |   color: #fff;
     | Sets CSS property `color` to `#fff`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 713 |   box-shadow: 0 2px 10px rgba(99, 102, 241, 0.35);
     | Sets CSS property `box-shadow` to `0 2px 10px rgba(99, 102, 241, 0.35)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 714 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 715 | .btn-primary:hover { filter: brightness(1.08); transform: translateY(-1px); }
     | CSS line `.btn-primary:hover { filter: brightness(1.08); transform: translateY(-1px); }`. It is part of the stylesheet the browser applies while painting the React DOM.

 716 | .btn-primary:active { transform: none; filter: brightness(1); }
     | CSS line `.btn-primary:active { transform: none; filter: brightness(1); }`. It is part of the stylesheet the browser applies while painting the React DOM.

 717 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 718 | .btn-secondary {
     | Opens a rule for selector `.btn-secondary`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 719 |   background: var(--indigo-dim);
     | Sets CSS property `background` to `var(--indigo-dim)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 720 |   color: var(--indigo-light);
     | Sets CSS property `color` to `var(--indigo-light)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 721 |   border: 1px solid rgba(99, 102, 241, 0.2);
     | Sets CSS property `border` to `1px solid rgba(99, 102, 241, 0.2)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 722 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 723 | .btn-secondary:hover { background: rgba(99, 102, 241, 0.2); }
     | CSS line `.btn-secondary:hover { background: rgba(99, 102, 241, 0.2); }`. It is part of the stylesheet the browser applies while painting the React DOM.

 724 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 725 | .btn-ghost {
     | Opens a rule for selector `.btn-ghost`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 726 |   background: transparent;
     | Sets CSS property `background` to `transparent`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 727 |   color: var(--muted);
     | Sets CSS property `color` to `var(--muted)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 728 |   border: 1px solid var(--border);
     | Sets CSS property `border` to `1px solid var(--border)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 729 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 730 | .btn-ghost:hover { color: var(--text); border-color: rgba(255, 255, 255, 0.2); }
     | CSS line `.btn-ghost:hover { color: var(--text); border-color: rgba(255, 255, 255, 0.2); }`. It is part of the stylesheet the browser applies while painting the React DOM.

 731 | :root[data-theme="light"] .btn-ghost:hover { border-color: rgba(0,0,0,0.2); }
     | CSS line `:root[data-theme="light"] .btn-ghost:hover { border-color: rgba(0,0,0,0.2); }`. It is part of the stylesheet the browser applies while painting the React DOM.

 732 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 733 | .btn-danger {
     | Opens a rule for selector `.btn-danger`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 734 |   background: var(--red-dim);
     | Sets CSS property `background` to `var(--red-dim)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 735 |   color: var(--red);
     | Sets CSS property `color` to `var(--red)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 736 |   border: 1px solid rgba(239, 68, 68, 0.2);
     | Sets CSS property `border` to `1px solid rgba(239, 68, 68, 0.2)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 737 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 738 | .btn-danger:hover { background: rgba(239, 68, 68, 0.2); }
     | CSS line `.btn-danger:hover { background: rgba(239, 68, 68, 0.2); }`. It is part of the stylesheet the browser applies while painting the React DOM.

 739 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 740 | .btn-success {
     | Opens a rule for selector `.btn-success`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 741 |   background: var(--green-dim);
     | Sets CSS property `background` to `var(--green-dim)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 742 |   color: var(--green);
     | Sets CSS property `color` to `var(--green)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 743 |   border: 1px solid rgba(16, 185, 129, 0.2);
     | Sets CSS property `border` to `1px solid rgba(16, 185, 129, 0.2)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 744 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 745 | .btn-success:hover { background: rgba(16, 185, 129, 0.2); }
     | CSS line `.btn-success:hover { background: rgba(16, 185, 129, 0.2); }`. It is part of the stylesheet the browser applies while painting the React DOM.

 746 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 747 | .btn-amber {
     | Opens a rule for selector `.btn-amber`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 748 |   background: var(--amber-dim);
     | Sets CSS property `background` to `var(--amber-dim)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 749 |   color: var(--amber);
     | Sets CSS property `color` to `var(--amber)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 750 |   border: 1px solid rgba(245, 158, 11, 0.2);
     | Sets CSS property `border` to `1px solid rgba(245, 158, 11, 0.2)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 751 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 752 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 753 | .btn-sm { padding: 5px 10px; font-size: var(--text-xs); }
     | CSS line `.btn-sm { padding: 5px 10px; font-size: var(--text-xs); }`. It is part of the stylesheet the browser applies while painting the React DOM.

 754 | .btn-lg { padding: 12px 24px; font-size: 16px; }
     | CSS line `.btn-lg { padding: 12px 24px; font-size: 16px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 755 | .btn:disabled { opacity: 0.5; cursor: not-allowed; transform: none !important; }
     | CSS line `.btn:disabled { opacity: 0.5; cursor: not-allowed; transform: none !important; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 756 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 757 | /* ── Inputs ─────────────────────────────────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── Inputs ─────────────────────────────────────────── */

 758 | .input, .textarea, .select {
     | Opens a rule for selector `.input, .textarea, .select`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 759 |   width: 100%;
     | Sets CSS property `width` to `100%`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 760 |   padding: 10px 14px;
     | Sets CSS property `padding` to `10px 14px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 761 |   border-radius: var(--radius-sm);
     | Sets CSS property `border-radius` to `var(--radius-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 762 |   border: 1px solid var(--border);
     | Sets CSS property `border` to `1px solid var(--border)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 763 |   background: var(--surface);
     | Sets CSS property `background` to `var(--surface)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 764 |   color: var(--text);
     | Sets CSS property `color` to `var(--text)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 765 |   font-size: var(--text-sm);
     | Sets CSS property `font-size` to `var(--text-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 766 |   font-family: inherit;
     | Sets CSS property `font-family` to `inherit`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 767 |   outline: none;
     | Sets CSS property `outline` to `none`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 768 |   transition: border 0.15s;
     | Sets CSS property `transition` to `border 0.15s`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 769 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 770 | .input:focus, .textarea:focus, .select:focus {
     | Opens a rule for selector `.input:focus, .textarea:focus, .select:focus`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 771 |   border-color: var(--indigo);
     | Sets CSS property `border-color` to `var(--indigo)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 772 |   box-shadow: 0 0 0 3px var(--indigo-dim);
     | Sets CSS property `box-shadow` to `0 0 0 3px var(--indigo-dim)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 773 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 774 | .textarea { resize: vertical; min-height: 100px; }
     | CSS line `.textarea { resize: vertical; min-height: 100px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 775 | .select option { background: var(--card); }
     | CSS line `.select option { background: var(--card); }`. It is part of the stylesheet the browser applies while painting the React DOM.

 776 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 777 | /* Text link */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* Text link */

 778 | .text-link {
     | Opens a rule for selector `.text-link`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 779 |   color: var(--indigo-light);
     | Sets CSS property `color` to `var(--indigo-light)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 780 |   text-decoration: underline;
     | Sets CSS property `text-decoration` to `underline`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 781 |   cursor: pointer;
     | Sets CSS property `cursor` to `pointer`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 782 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 783 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 784 | /* ── Badges ─────────────────────────────────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── Badges ─────────────────────────────────────────── */

 785 | .badge {
     | Opens a rule for selector `.badge`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 786 |   display: inline-flex;
     | Sets CSS property `display` to `inline-flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 787 |   align-items: center;
     | Sets CSS property `align-items` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 788 |   padding: 2px 8px;
     | Sets CSS property `padding` to `2px 8px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 789 |   border-radius: 20px;
     | Sets CSS property `border-radius` to `20px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 790 |   font-size: var(--text-xs);
     | Sets CSS property `font-size` to `var(--text-xs)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 791 |   font-weight: 700;
     | Sets CSS property `font-weight` to `700`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 792 |   letter-spacing: 0.3px;
     | Sets CSS property `letter-spacing` to `0.3px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 793 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 794 | .badge-high { background: var(--red-dim); color: var(--red); }
     | CSS line `.badge-high { background: var(--red-dim); color: var(--red); }`. It is part of the stylesheet the browser applies while painting the React DOM.

 795 | .badge-medium { background: var(--amber-dim); color: var(--amber); }
     | CSS line `.badge-medium { background: var(--amber-dim); color: var(--amber); }`. It is part of the stylesheet the browser applies while painting the React DOM.

 796 | .badge-low { background: var(--green-dim); color: var(--green); }
     | CSS line `.badge-low { background: var(--green-dim); color: var(--green); }`. It is part of the stylesheet the browser applies while painting the React DOM.

 797 | .badge-violet { background: var(--indigo-dim); color: var(--indigo-light); }
     | CSS line `.badge-violet { background: var(--indigo-dim); color: var(--indigo-light); }`. It is part of the stylesheet the browser applies while painting the React DOM.

 798 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 799 | /* ── Nav divider ────────────────────────────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── Nav divider ────────────────────────────────────── */

 800 | .nav-divider { height: 1px; background: var(--border); margin: 8px 0; }
     | CSS line `.nav-divider { height: 1px; background: var(--border); margin: 8px 0; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 801 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 802 | /* ── Dread Meter ────────────────────────────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── Dread Meter ────────────────────────────────────── */

 803 | .dread-meter { display: flex; gap: 3px; align-items: center; }
     | CSS line `.dread-meter { display: flex; gap: 3px; align-items: center; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 804 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 805 | .dread-pip {
     | Opens a rule for selector `.dread-pip`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 806 |   width: 10px;
     | Sets CSS property `width` to `10px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 807 |   height: 10px;
     | Sets CSS property `height` to `10px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 808 |   border-radius: 2px;
     | Sets CSS property `border-radius` to `2px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 809 |   background: var(--border);
     | Sets CSS property `background` to `var(--border)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 810 |   cursor: pointer;
     | Sets CSS property `cursor` to `pointer`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 811 |   transition: background 0.1s, transform 0.1s;
     | Sets CSS property `transition` to `background 0.1s, transform 0.1s`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 812 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 813 | .dread-pip:hover { transform: scale(1.2); }
     | CSS line `.dread-pip:hover { transform: scale(1.2); }`. It is part of the stylesheet the browser applies while painting the React DOM.

 814 | .dread-pip.active-1 { background: var(--green); }
     | CSS line `.dread-pip.active-1 { background: var(--green); }`. It is part of the stylesheet the browser applies while painting the React DOM.

 815 | .dread-pip.active-2 { background: #84cc16; }
     | CSS line `.dread-pip.active-2 { background: #84cc16; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 816 | .dread-pip.active-3 { background: var(--amber); }
     | CSS line `.dread-pip.active-3 { background: var(--amber); }`. It is part of the stylesheet the browser applies while painting the React DOM.

 817 | .dread-pip.active-4 { background: #f97316; }
     | CSS line `.dread-pip.active-4 { background: #f97316; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 818 | .dread-pip.active-5 { background: var(--red); }
     | CSS line `.dread-pip.active-5 { background: var(--red); }`. It is part of the stylesheet the browser applies while painting the React DOM.

 819 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 820 | /* ── Focus Ring Timer ───────────────────────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── Focus Ring Timer ───────────────────────────────── */

 821 | .ring-container {
     | Opens a rule for selector `.ring-container`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 822 |   position: relative;
     | Sets CSS property `position` to `relative`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 823 |   width: 220px;
     | Sets CSS property `width` to `220px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 824 |   height: 220px;
     | Sets CSS property `height` to `220px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 825 |   margin: 0 auto 20px;
     | Sets CSS property `margin` to `0 auto 20px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 826 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 827 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 828 | .ring-svg { transform: rotate(-90deg); }
     | CSS line `.ring-svg { transform: rotate(-90deg); }`. It is part of the stylesheet the browser applies while painting the React DOM.

 829 | .ring-track { fill: none; stroke: var(--border); stroke-width: 10; }
     | CSS line `.ring-track { fill: none; stroke: var(--border); stroke-width: 10; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 830 | .ring-progress {
     | Opens a rule for selector `.ring-progress`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 831 |   fill: none;
     | Sets CSS property `fill` to `none`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 832 |   stroke-width: 10;
     | Sets CSS property `stroke-width` to `10`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 833 |   stroke-linecap: round;
     | Sets CSS property `stroke-linecap` to `round`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 834 |   transition: stroke-dashoffset 1s linear, stroke 0.3s;
     | Sets CSS property `transition` to `stroke-dashoffset 1s linear, stroke 0.3s`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 835 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 836 | .ring-progress.work { stroke: var(--indigo); filter: drop-shadow(0 0 6px rgba(99,102,241,0.5)); }
     | CSS line `.ring-progress.work { stroke: var(--indigo); filter: drop-shadow(0 0 6px rgba(99,102,241,0.5)); }`. It is part of the stylesheet the browser applies while painting the React DOM.

 837 | .ring-progress.brk { stroke: var(--green); filter: drop-shadow(0 0 6px rgba(16,185,129,0.4)); }
     | CSS line `.ring-progress.brk { stroke: var(--green); filter: drop-shadow(0 0 6px rgba(16,185,129,0.4)); }`. It is part of the stylesheet the browser applies while painting the React DOM.

 838 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 839 | .ring-text {
     | Opens a rule for selector `.ring-text`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 840 |   position: absolute;
     | Sets CSS property `position` to `absolute`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 841 |   top: 50%;
     | Sets CSS property `top` to `50%`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 842 |   left: 50%;
     | Sets CSS property `left` to `50%`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 843 |   transform: translate(-50%, -50%);
     | Sets CSS property `transform` to `translate(-50%, -50%)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 844 |   text-align: center;
     | Sets CSS property `text-align` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 845 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 846 | .ring-time {
     | Opens a rule for selector `.ring-time`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 847 |   font-size: 38px;
     | Sets CSS property `font-size` to `38px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 848 |   font-weight: 800;
     | Sets CSS property `font-weight` to `800`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 849 |   font-variant-numeric: tabular-nums;
     | Sets CSS property `font-variant-numeric` to `tabular-nums`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 850 |   color: var(--text);
     | Sets CSS property `color` to `var(--text)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 851 |   line-height: 1;
     | Sets CSS property `line-height` to `1`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 852 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 853 | .ring-label {
     | Opens a rule for selector `.ring-label`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 854 |   font-size: var(--text-xs);
     | Sets CSS property `font-size` to `var(--text-xs)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 855 |   color: var(--muted);
     | Sets CSS property `color` to `var(--muted)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 856 |   margin-top: 4px;
     | Sets CSS property `margin-top` to `4px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 857 |   text-transform: uppercase;
     | Sets CSS property `text-transform` to `uppercase`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 858 |   letter-spacing: 0.5px;
     | Sets CSS property `letter-spacing` to `0.5px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 859 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 860 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 861 | /* ── Task picker (FocusTimer) ───────────────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── Task picker (FocusTimer) ───────────────────────── */

 862 | .task-link-picker {
     | Opens a rule for selector `.task-link-picker`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 863 |   border: 1px solid var(--border);
     | Sets CSS property `border` to `1px solid var(--border)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 864 |   border-radius: var(--radius-sm);
     | Sets CSS property `border-radius` to `var(--radius-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 865 |   padding: var(--space-3) var(--space-4);
     | Sets CSS property `padding` to `var(--space-3) var(--space-4)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 866 |   background: var(--surface);
     | Sets CSS property `background` to `var(--surface)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 867 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 868 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 869 | .linked-task-badge {
     | Opens a rule for selector `.linked-task-badge`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 870 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 871 |   align-items: center;
     | Sets CSS property `align-items` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 872 |   gap: var(--space-2);
     | Sets CSS property `gap` to `var(--space-2)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 873 |   margin-top: var(--space-2);
     | Sets CSS property `margin-top` to `var(--space-2)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 874 |   padding: 6px 10px;
     | Sets CSS property `padding` to `6px 10px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 875 |   border-radius: var(--radius-sm);
     | Sets CSS property `border-radius` to `var(--radius-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 876 |   background: var(--indigo-dim);
     | Sets CSS property `background` to `var(--indigo-dim)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 877 |   border: 1px solid rgba(99, 102, 241, 0.2);
     | Sets CSS property `border` to `1px solid rgba(99, 102, 241, 0.2)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 878 |   font-size: var(--text-xs);
     | Sets CSS property `font-size` to `var(--text-xs)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 879 |   font-weight: 600;
     | Sets CSS property `font-weight` to `600`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 880 |   color: var(--indigo-light);
     | Sets CSS property `color` to `var(--indigo-light)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 881 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 882 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 883 | /* ── Add Task Row ───────────────────────────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── Add Task Row ───────────────────────────────────── */

 884 | .add-task-row {}
     | CSS line `.add-task-row {}`. It is part of the stylesheet the browser applies while painting the React DOM.

 885 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 886 | .add-task-details {
     | Opens a rule for selector `.add-task-details`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 887 |   margin-top: var(--space-3);
     | Sets CSS property `margin-top` to `var(--space-3)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 888 |   padding-top: var(--space-3);
     | Sets CSS property `padding-top` to `var(--space-3)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 889 |   border-top: 1px solid var(--border);
     | Sets CSS property `border-top` to `1px solid var(--border)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 890 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 891 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 892 | /* ── Empty States ───────────────────────────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── Empty States ───────────────────────────────────── */

 893 | .empty-state {
     | Opens a rule for selector `.empty-state`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 894 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 895 |   flex-direction: column;
     | Sets CSS property `flex-direction` to `column`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 896 |   align-items: center;
     | Sets CSS property `align-items` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 897 |   text-align: center;
     | Sets CSS property `text-align` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 898 |   padding: 40px 20px;
     | Sets CSS property `padding` to `40px 20px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 899 |   gap: var(--space-3);
     | Sets CSS property `gap` to `var(--space-3)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 900 |   color: var(--muted);
     | Sets CSS property `color` to `var(--muted)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 901 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 902 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 903 | .empty-state-icon { font-size: 36px; }
     | CSS line `.empty-state-icon { font-size: 36px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 904 | .empty-state-title { font-weight: 700; font-size: var(--text-base); color: var(--text-soft); }
     | CSS line `.empty-state-title { font-weight: 700; font-size: var(--text-base); color: var(--text-soft); }`. It is part of the stylesheet the browser applies while painting the React DOM.

 905 | .empty-state-body { font-size: var(--text-sm); line-height: 1.6; max-width: 280px; }
     | CSS line `.empty-state-body { font-size: var(--text-sm); line-height: 1.6; max-width: 280px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 906 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 907 | /* ── Task Cards ─────────────────────────────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── Task Cards ─────────────────────────────────────── */

 908 | .task-card {
     | Opens a rule for selector `.task-card`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 909 |   background: var(--card);
     | Sets CSS property `background` to `var(--card)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 910 |   border: 1px solid var(--border);
     | Sets CSS property `border` to `1px solid var(--border)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 911 |   border-radius: var(--radius);
     | Sets CSS property `border-radius` to `var(--radius)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 912 |   padding: 14px 16px;
     | Sets CSS property `padding` to `14px 16px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 913 |   transition: all 0.2s;
     | Sets CSS property `transition` to `all 0.2s`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 914 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 915 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 916 | .task-card:hover {
     | Opens a rule for selector `.task-card:hover`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 917 |   border-color: rgba(99, 102, 241, 0.25);
     | Sets CSS property `border-color` to `rgba(99, 102, 241, 0.25)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 918 |   transform: translateY(-1px);
     | Sets CSS property `transform` to `translateY(-1px)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 919 |   box-shadow: var(--shadow-card);
     | Sets CSS property `box-shadow` to `var(--shadow-card)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 920 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 921 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 922 | .task-card.completing {
     | Opens a rule for selector `.task-card.completing`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 923 |   animation: taskComplete 0.45s ease-out forwards;
     | Sets CSS property `animation` to `taskComplete 0.45s ease-out forwards`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 924 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 925 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 926 | @keyframes taskComplete {
     | Starts an animation definition `@keyframes taskComplete {`. Later rules refer to this name in an `animation` property.

 927 |   0%   { transform: scale(1); opacity: 1; }
     | CSS line `0%   { transform: scale(1); opacity: 1; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 928 |   50%  { transform: scale(1.02); background: var(--green-dim); border-color: var(--green); }
     | CSS line `50%  { transform: scale(1.02); background: var(--green-dim); border-color: var(--green); }`. It is part of the stylesheet the browser applies while painting the React DOM.

 929 |   100% { transform: scale(0.95); opacity: 0; height: 0; padding: 0; margin: 0; overflow: hidden; }
     | CSS line `100% { transform: scale(0.95); opacity: 0; height: 0; padding: 0; margin: 0; overflow: hidden; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 930 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 931 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 932 | .task-header {
     | Opens a rule for selector `.task-header`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 933 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 934 |   align-items: flex-start;
     | Sets CSS property `align-items` to `flex-start`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 935 |   gap: 10px;
     | Sets CSS property `gap` to `10px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 936 |   margin-bottom: 8px;
     | Sets CSS property `margin-bottom` to `8px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 937 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 938 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 939 | .task-check {
     | Opens a rule for selector `.task-check`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 940 |   width: 20px;
     | Sets CSS property `width` to `20px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 941 |   height: 20px;
     | Sets CSS property `height` to `20px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 942 |   border-radius: 6px;
     | Sets CSS property `border-radius` to `6px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 943 |   border: 2px solid var(--border);
     | Sets CSS property `border` to `2px solid var(--border)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 944 |   cursor: pointer;
     | Sets CSS property `cursor` to `pointer`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 945 |   flex-shrink: 0;
     | Sets CSS property `flex-shrink` to `0`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 946 |   margin-top: 2px;
     | Sets CSS property `margin-top` to `2px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 947 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 948 |   align-items: center;
     | Sets CSS property `align-items` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 949 |   justify-content: center;
     | Sets CSS property `justify-content` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 950 |   transition: all 0.15s;
     | Sets CSS property `transition` to `all 0.15s`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 951 |   background: transparent;
     | Sets CSS property `background` to `transparent`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 952 |   padding: 0;
     | Sets CSS property `padding` to `0`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 953 |   font-size: 11px;
     | Sets CSS property `font-size` to `11px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 954 |   color: transparent;
     | Sets CSS property `color` to `transparent`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 955 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 956 | .task-check:hover { border-color: var(--green); background: var(--green-dim); color: var(--green); }
     | CSS line `.task-check:hover { border-color: var(--green); background: var(--green-dim); color: var(--green); }`. It is part of the stylesheet the browser applies while painting the React DOM.

 957 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 958 | .task-title-text {
     | Opens a rule for selector `.task-title-text`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 959 |   font-weight: 600;
     | Sets CSS property `font-weight` to `600`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 960 |   font-size: var(--text-base);
     | Sets CSS property `font-size` to `var(--text-base)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 961 |   color: var(--text);
     | Sets CSS property `color` to `var(--text)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 962 |   line-height: 1.4;
     | Sets CSS property `line-height` to `1.4`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 963 |   flex: 1;
     | Sets CSS property `flex` to `1`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 964 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 965 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 966 | .task-meta {
     | Opens a rule for selector `.task-meta`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 967 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 968 |   gap: 8px;
     | Sets CSS property `gap` to `8px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 969 |   flex-wrap: wrap;
     | Sets CSS property `flex-wrap` to `wrap`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 970 |   align-items: center;
     | Sets CSS property `align-items` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 971 |   margin-bottom: 10px;
     | Sets CSS property `margin-bottom` to `10px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 972 |   font-size: var(--text-xs);
     | Sets CSS property `font-size` to `var(--text-xs)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 973 |   color: var(--muted);
     | Sets CSS property `color` to `var(--muted)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 974 |   padding-left: 30px;
     | Sets CSS property `padding-left` to `30px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 975 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 976 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 977 | .task-actions {
     | Opens a rule for selector `.task-actions`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 978 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 979 |   gap: 6px;
     | Sets CSS property `gap` to `6px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 980 |   flex-wrap: wrap;
     | Sets CSS property `flex-wrap` to `wrap`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 981 |   padding-left: 30px;
     | Sets CSS property `padding-left` to `30px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 982 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 983 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 984 | /* ── Brain Dump ─────────────────────────────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── Brain Dump ─────────────────────────────────────── */

 985 | .brain-dump-wrap { position: relative; }
     | CSS line `.brain-dump-wrap { position: relative; }`. It is part of the stylesheet the browser applies while painting the React DOM.

 986 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 987 | .brain-dump-hint {
     | Opens a rule for selector `.brain-dump-hint`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 988 |   position: absolute;
     | Sets CSS property `position` to `absolute`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 989 |   bottom: 10px;
     | Sets CSS property `bottom` to `10px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 990 |   right: 12px;
     | Sets CSS property `right` to `12px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 991 |   font-size: var(--text-xs);
     | Sets CSS property `font-size` to `var(--text-xs)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 992 |   color: var(--muted);
     | Sets CSS property `color` to `var(--muted)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 993 |   pointer-events: none;
     | Sets CSS property `pointer-events` to `none`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 994 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

 995 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

 996 | /* ── Stat Tiles ─────────────────────────────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── Stat Tiles ─────────────────────────────────────── */

 997 | .stat-tile {
     | Opens a rule for selector `.stat-tile`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

 998 |   background: var(--card);
     | Sets CSS property `background` to `var(--card)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

 999 |   border: 1px solid var(--border);
     | Sets CSS property `border` to `1px solid var(--border)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1000 |   border-radius: var(--radius);
     | Sets CSS property `border-radius` to `var(--radius)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1001 |   padding: 18px var(--space-5);
     | Sets CSS property `padding` to `18px var(--space-5)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1002 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1003 |   flex-direction: column;
     | Sets CSS property `flex-direction` to `column`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1004 |   gap: 6px;
     | Sets CSS property `gap` to `6px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1005 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1006 | .stat-value {
     | Opens a rule for selector `.stat-value`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1007 |   font-size: 34px;
     | Sets CSS property `font-size` to `34px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1008 |   font-weight: 800;
     | Sets CSS property `font-weight` to `800`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1009 |   line-height: 1;
     | Sets CSS property `line-height` to `1`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1010 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1011 | .stat-label {
     | Opens a rule for selector `.stat-label`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1012 |   font-size: var(--text-xs);
     | Sets CSS property `font-size` to `var(--text-xs)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1013 |   color: var(--muted);
     | Sets CSS property `color` to `var(--muted)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1014 |   text-transform: uppercase;
     | Sets CSS property `text-transform` to `uppercase`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1015 |   letter-spacing: 0.6px;
     | Sets CSS property `letter-spacing` to `0.6px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1016 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1017 | .stat-violet { color: var(--indigo-light); }
     | CSS line `.stat-violet { color: var(--indigo-light); }`. It is part of the stylesheet the browser applies while painting the React DOM.

1018 | .stat-green { color: var(--green); }
     | CSS line `.stat-green { color: var(--green); }`. It is part of the stylesheet the browser applies while painting the React DOM.

1019 | .stat-amber { color: var(--amber); }
     | CSS line `.stat-amber { color: var(--amber); }`. It is part of the stylesheet the browser applies while painting the React DOM.

1020 | .stat-red { color: var(--red); }
     | CSS line `.stat-red { color: var(--red); }`. It is part of the stylesheet the browser applies while painting the React DOM.

1021 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1022 | /* ── Streak Badge ───────────────────────────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── Streak Badge ───────────────────────────────────── */

1023 | .streak-badge {
     | Opens a rule for selector `.streak-badge`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1024 |   display: inline-flex;
     | Sets CSS property `display` to `inline-flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1025 |   align-items: center;
     | Sets CSS property `align-items` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1026 |   gap: 6px;
     | Sets CSS property `gap` to `6px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1027 |   background: linear-gradient(135deg, #fbbf24, #f97316);
     | Sets CSS property `background` to `linear-gradient(135deg, #fbbf24, #f97316)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1028 |   color: #fff;
     | Sets CSS property `color` to `#fff`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1029 |   padding: 5px 14px;
     | Sets CSS property `padding` to `5px 14px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1030 |   border-radius: 20px;
     | Sets CSS property `border-radius` to `20px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1031 |   font-weight: 700;
     | Sets CSS property `font-weight` to `700`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1032 |   font-size: var(--text-sm);
     | Sets CSS property `font-size` to `var(--text-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1033 |   box-shadow: 0 2px 8px rgba(251, 191, 36, 0.4);
     | Sets CSS property `box-shadow` to `0 2px 8px rgba(251, 191, 36, 0.4)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1034 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1035 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1036 | /* ── Focus Overlay ──────────────────────────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── Focus Overlay ──────────────────────────────────── */

1037 | .focus-overlay {
     | Opens a rule for selector `.focus-overlay`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1038 |   position: fixed;
     | Sets CSS property `position` to `fixed`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1039 |   inset: 0;
     | Sets CSS property `inset` to `0`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1040 |   background: rgba(0, 0, 0, 0.85);
     | Sets CSS property `background` to `rgba(0, 0, 0, 0.85)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1041 |   backdrop-filter: blur(8px);
     | Sets CSS property `backdrop-filter` to `blur(8px)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1042 |   z-index: 1000;
     | Sets CSS property `z-index` to `1000`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1043 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1044 |   align-items: center;
     | Sets CSS property `align-items` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1045 |   justify-content: center;
     | Sets CSS property `justify-content` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1046 |   animation: overlayIn 0.3s ease;
     | Sets CSS property `animation` to `overlayIn 0.3s ease`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1047 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1048 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1049 | @keyframes overlayIn {
     | Starts an animation definition `@keyframes overlayIn {`. Later rules refer to this name in an `animation` property.

1050 |   from { opacity: 0; }
     | CSS line `from { opacity: 0; }`. It is part of the stylesheet the browser applies while painting the React DOM.

1051 |   to   { opacity: 1; }
     | CSS line `to   { opacity: 1; }`. It is part of the stylesheet the browser applies while painting the React DOM.

1052 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1053 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1054 | .focus-overlay-card {
     | Opens a rule for selector `.focus-overlay-card`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1055 |   background: var(--card);
     | Sets CSS property `background` to `var(--card)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1056 |   border: 1px solid var(--indigo);
     | Sets CSS property `border` to `1px solid var(--indigo)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1057 |   border-radius: var(--radius-lg);
     | Sets CSS property `border-radius` to `var(--radius-lg)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1058 |   padding: 36px 40px;
     | Sets CSS property `padding` to `36px 40px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1059 |   text-align: center;
     | Sets CSS property `text-align` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1060 |   max-width: 380px;
     | Sets CSS property `max-width` to `380px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1061 |   width: 90%;
     | Sets CSS property `width` to `90%`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1062 |   box-shadow: 0 0 60px rgba(99, 102, 241, 0.3);
     | Sets CSS property `box-shadow` to `0 0 60px rgba(99, 102, 241, 0.3)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1063 |   animation: overlayCardIn 0.3s ease;
     | Sets CSS property `animation` to `overlayCardIn 0.3s ease`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1064 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1065 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1066 | @keyframes overlayCardIn {
     | Starts an animation definition `@keyframes overlayCardIn {`. Later rules refer to this name in an `animation` property.

1067 |   from { transform: scale(0.95); opacity: 0; }
     | CSS line `from { transform: scale(0.95); opacity: 0; }`. It is part of the stylesheet the browser applies while painting the React DOM.

1068 |   to   { transform: scale(1); opacity: 1; }
     | CSS line `to   { transform: scale(1); opacity: 1; }`. It is part of the stylesheet the browser applies while painting the React DOM.

1069 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1070 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1071 | .focus-overlay-icon { font-size: 48px; margin-bottom: 12px; }
     | CSS line `.focus-overlay-icon { font-size: 48px; margin-bottom: 12px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

1072 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1073 | .focus-overlay-title {
     | Opens a rule for selector `.focus-overlay-title`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1074 |   font-size: var(--text-lg);
     | Sets CSS property `font-size` to `var(--text-lg)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1075 |   font-weight: 800;
     | Sets CSS property `font-weight` to `800`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1076 |   color: var(--text);
     | Sets CSS property `color` to `var(--text)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1077 |   margin-bottom: 8px;
     | Sets CSS property `margin-bottom` to `8px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1078 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1079 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1080 | .focus-overlay-text {
     | Opens a rule for selector `.focus-overlay-text`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1081 |   font-size: var(--text-sm);
     | Sets CSS property `font-size` to `var(--text-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1082 |   color: var(--muted);
     | Sets CSS property `color` to `var(--muted)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1083 |   line-height: 1.7;
     | Sets CSS property `line-height` to `1.7`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1084 |   margin-bottom: 20px;
     | Sets CSS property `margin-bottom` to `20px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1085 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1086 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1087 | /* ── Reward Burst ───────────────────────────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── Reward Burst ───────────────────────────────────── */

1088 | .reward-burst {
     | Opens a rule for selector `.reward-burst`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1089 |   position: fixed;
     | Sets CSS property `position` to `fixed`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1090 |   top: 50%;
     | Sets CSS property `top` to `50%`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1091 |   left: 50%;
     | Sets CSS property `left` to `50%`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1092 |   transform: translate(-50%, -50%);
     | Sets CSS property `transform` to `translate(-50%, -50%)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1093 |   pointer-events: none;
     | Sets CSS property `pointer-events` to `none`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1094 |   z-index: 500;
     | Sets CSS property `z-index` to `500`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1095 |   font-size: 52px;
     | Sets CSS property `font-size` to `52px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1096 |   animation: burstOut 0.9s ease-out forwards;
     | Sets CSS property `animation` to `burstOut 0.9s ease-out forwards`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1097 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1098 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1099 | @keyframes burstOut {
     | Starts an animation definition `@keyframes burstOut {`. Later rules refer to this name in an `animation` property.

1100 |   0%   { opacity: 1; transform: translate(-50%, -50%) scale(0.4); }
     | CSS line `0%   { opacity: 1; transform: translate(-50%, -50%) scale(0.4); }`. It is part of the stylesheet the browser applies while painting the React DOM.

1101 |   40%  { opacity: 1; transform: translate(-50%, -60%) scale(1.3); }
     | CSS line `40%  { opacity: 1; transform: translate(-50%, -60%) scale(1.3); }`. It is part of the stylesheet the browser applies while painting the React DOM.

1102 |   100% { opacity: 0; transform: translate(-50%, -100%) scale(0.8); }
     | CSS line `100% { opacity: 0; transform: translate(-50%, -100%) scale(0.8); }`. It is part of the stylesheet the browser applies while painting the React DOM.

1103 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1104 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1105 | /* ── Auth ───────────────────────────────────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── Auth ───────────────────────────────────────────── */

1106 | .auth-page {
     | Opens a rule for selector `.auth-page`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1107 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1108 |   align-items: center;
     | Sets CSS property `align-items` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1109 |   justify-content: center;
     | Sets CSS property `justify-content` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1110 |   min-height: 100dvh;
     | Sets CSS property `min-height` to `100dvh`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1111 |   width: 100%;
     | Sets CSS property `width` to `100%`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1112 |   background: var(--bg);
     | Sets CSS property `background` to `var(--bg)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1113 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1114 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1115 | .auth-card {
     | Opens a rule for selector `.auth-card`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1116 |   width: calc(100% - 48px);
     | Sets CSS property `width` to `calc(100% - 48px)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1117 |   max-width: 400px;
     | Sets CSS property `max-width` to `400px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1118 |   background: var(--card-hover);
     | Sets CSS property `background` to `var(--card-hover)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1119 |   border: 1px solid var(--border-active);
     | Sets CSS property `border` to `1px solid var(--border-active)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1120 |   padding: var(--space-6);
     | Sets CSS property `padding` to `var(--space-6)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1121 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1122 |   flex-direction: column;
     | Sets CSS property `flex-direction` to `column`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1123 |   gap: var(--space-4);
     | Sets CSS property `gap` to `var(--space-4)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1124 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1125 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1126 | .auth-brand {
     | Opens a rule for selector `.auth-brand`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1127 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1128 |   align-items: center;
     | Sets CSS property `align-items` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1129 |   justify-content: center;
     | Sets CSS property `justify-content` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1130 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1131 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1132 | .auth-header {
     | Opens a rule for selector `.auth-header`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1133 |   text-align: center;
     | Sets CSS property `text-align` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1134 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1135 |   flex-direction: column;
     | Sets CSS property `flex-direction` to `column`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1136 |   gap: 6px;
     | Sets CSS property `gap` to `6px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1137 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1138 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1139 | .auth-title {
     | Opens a rule for selector `.auth-title`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1140 |   font-size: var(--text-xl);
     | Sets CSS property `font-size` to `var(--text-xl)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1141 |   font-weight: 800;
     | Sets CSS property `font-weight` to `800`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1142 |   margin-bottom: 4px;
     | Sets CSS property `margin-bottom` to `4px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1143 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1144 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1145 | .auth-subtitle {
     | Opens a rule for selector `.auth-subtitle`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1146 |   font-size: var(--text-sm);
     | Sets CSS property `font-size` to `var(--text-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1147 |   color: var(--muted);
     | Sets CSS property `color` to `var(--muted)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1148 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1149 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1150 | .auth-value {
     | Opens a rule for selector `.auth-value`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1151 |   font-size: var(--text-sm);
     | Sets CSS property `font-size` to `var(--text-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1152 |   color: var(--muted);
     | Sets CSS property `color` to `var(--muted)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1153 |   display: -webkit-box;
     | Sets CSS property `display` to `-webkit-box`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1154 |   -webkit-line-clamp: 2;
     | Sets CSS property `-webkit-line-clamp` to `2`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1155 |   -webkit-box-orient: vertical;
     | Sets CSS property `-webkit-box-orient` to `vertical`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1156 |   overflow: hidden;
     | Sets CSS property `overflow` to `hidden`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1157 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1158 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1159 | .auth-status:empty { display: none; }
     | CSS line `.auth-status:empty { display: none; }`. It is part of the stylesheet the browser applies while painting the React DOM.

1160 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1161 | .auth-error {
     | Opens a rule for selector `.auth-error`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1162 |   padding: 10px 14px;
     | Sets CSS property `padding` to `10px 14px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1163 |   border-radius: var(--radius-sm);
     | Sets CSS property `border-radius` to `var(--radius-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1164 |   background: var(--red-dim);
     | Sets CSS property `background` to `var(--red-dim)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1165 |   color: var(--red);
     | Sets CSS property `color` to `var(--red)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1166 |   font-size: 13px;
     | Sets CSS property `font-size` to `13px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1167 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1168 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1169 | .auth-legal {
     | Opens a rule for selector `.auth-legal`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1170 |   font-size: 12px;
     | Sets CSS property `font-size` to `12px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1171 |   color: var(--muted);
     | Sets CSS property `color` to `var(--muted)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1172 |   text-align: center;
     | Sets CSS property `text-align` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1173 |   line-height: 1.5;
     | Sets CSS property `line-height` to `1.5`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1174 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1175 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1176 | /* ── Google sign-in button ────────────────────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── Google sign-in button ────────────────────────────── */

1177 | .btn-google {
     | Opens a rule for selector `.btn-google`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1178 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1179 |   align-items: center;
     | Sets CSS property `align-items` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1180 |   justify-content: center;
     | Sets CSS property `justify-content` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1181 |   gap: 10px;
     | Sets CSS property `gap` to `10px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1182 |   width: 100%;
     | Sets CSS property `width` to `100%`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1183 |   min-height: 44px;
     | Sets CSS property `min-height` to `44px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1184 |   padding: 10px 16px;
     | Sets CSS property `padding` to `10px 16px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1185 |   border-radius: var(--radius-sm);
     | Sets CSS property `border-radius` to `var(--radius-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1186 |   border: 1px solid var(--border);
     | Sets CSS property `border` to `1px solid var(--border)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1187 |   background: var(--surface);
     | Sets CSS property `background` to `var(--surface)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1188 |   color: var(--text);
     | Sets CSS property `color` to `var(--text)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1189 |   font-size: var(--text-sm);
     | Sets CSS property `font-size` to `var(--text-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1190 |   font-weight: 600;
     | Sets CSS property `font-weight` to `600`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1191 |   font-family: inherit;
     | Sets CSS property `font-family` to `inherit`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1192 |   cursor: pointer;
     | Sets CSS property `cursor` to `pointer`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1193 |   transition: background 0.15s, border-color 0.15s, transform 0.1s;
     | Sets CSS property `transition` to `background 0.15s, border-color 0.15s, transform 0.1s`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1194 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1195 | .btn-google:hover:not(:disabled) { background: var(--card); border-color: var(--border-active); }
     | CSS line `.btn-google:hover:not(:disabled) { background: var(--card); border-color: var(--border-active); }`. It is part of the stylesheet the browser applies while painting the React DOM.

1196 | .btn-google:active:not(:disabled) { transform: translateY(1px); }
     | CSS line `.btn-google:active:not(:disabled) { transform: translateY(1px); }`. It is part of the stylesheet the browser applies while painting the React DOM.

1197 | .btn-google:disabled { opacity: 0.7; cursor: not-allowed; }
     | CSS line `.btn-google:disabled { opacity: 0.7; cursor: not-allowed; }`. It is part of the stylesheet the browser applies while painting the React DOM.

1198 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1199 | .google-btn-wrap {
     | Opens a rule for selector `.google-btn-wrap`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1200 |   position: relative;
     | Sets CSS property `position` to `relative`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1201 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1202 | .google-btn-wrap .btn-google {
     | Opens a rule for selector `.google-btn-wrap .btn-google`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1203 |   pointer-events: none;
     | Sets CSS property `pointer-events` to `none`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1204 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1205 | /* Google's real "Sign in with Google" button (from renderButton) is
     | CSS comment, ignored by the browser. It labels the next group of rules: /* Google's real "Sign in with Google" button (from renderButton) is

1206 |    mounted here, stretched over the styled button above and hidden via
     | CSS line `mounted here, stretched over the styled button above and hidden via`. It is part of the stylesheet the browser applies while painting the React DOM.

1207 |    opacity so the click a user makes actually lands on Google's own
     | CSS line `opacity so the click a user makes actually lands on Google's own`. It is part of the stylesheet the browser applies while painting the React DOM.

1208 |    element -- required for their popup/redirect flow to open reliably. */
     | CSS comment, ignored by the browser. It labels the next group of rules: element -- required for their popup/redirect flow to open reliably. */

1209 | .google-btn-overlay {
     | Opens a rule for selector `.google-btn-overlay`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1210 |   position: absolute;
     | Sets CSS property `position` to `absolute`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1211 |   inset: 0;
     | Sets CSS property `inset` to `0`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1212 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1213 |   align-items: center;
     | Sets CSS property `align-items` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1214 |   justify-content: center;
     | Sets CSS property `justify-content` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1215 |   overflow: hidden;
     | Sets CSS property `overflow` to `hidden`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1216 |   opacity: 0;
     | Sets CSS property `opacity` to `0`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1217 |   cursor: pointer;
     | Sets CSS property `cursor` to `pointer`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1218 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1219 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1220 | /* ── Inline spinner ───────────────────────────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── Inline spinner ───────────────────────────────────── */

1221 | .spinner {
     | Opens a rule for selector `.spinner`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1222 |   width: 16px;
     | Sets CSS property `width` to `16px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1223 |   height: 16px;
     | Sets CSS property `height` to `16px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1224 |   flex-shrink: 0;
     | Sets CSS property `flex-shrink` to `0`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1225 |   border: 2px solid var(--border);
     | Sets CSS property `border` to `2px solid var(--border)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1226 |   border-top-color: currentColor;
     | Sets CSS property `border-top-color` to `currentColor`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1227 |   border-radius: 50%;
     | Sets CSS property `border-radius` to `50%`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1228 |   display: inline-block;
     | Sets CSS property `display` to `inline-block`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1229 |   animation: spin 0.6s linear infinite;
     | Sets CSS property `animation` to `spin 0.6s linear infinite`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1230 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1231 | @keyframes spin { to { transform: rotate(360deg); } }
     | Starts an animation definition `@keyframes spin { to { transform: rotate(360deg); } }`. Later rules refer to this name in an `animation` property.

1232 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1233 | .auth-switch {
     | Opens a rule for selector `.auth-switch`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1234 |   font-size: 13px;
     | Sets CSS property `font-size` to `13px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1235 |   color: var(--muted);
     | Sets CSS property `color` to `var(--muted)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1236 |   margin-top: 14px;
     | Sets CSS property `margin-top` to `14px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1237 |   text-align: center;
     | Sets CSS property `text-align` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1238 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1239 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1240 | .auth-link {
     | Opens a rule for selector `.auth-link`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1241 |   color: var(--indigo-light);
     | Sets CSS property `color` to `var(--indigo-light)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1242 |   cursor: pointer;
     | Sets CSS property `cursor` to `pointer`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1243 |   margin-left: 6px;
     | Sets CSS property `margin-left` to `6px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1244 |   font-weight: 600;
     | Sets CSS property `font-weight` to `600`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1245 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1246 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1247 | /* ── Mode Tabs ──────────────────────────────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── Mode Tabs ──────────────────────────────────────── */

1248 | .mode-tabs {
     | Opens a rule for selector `.mode-tabs`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1249 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1250 |   gap: 4px;
     | Sets CSS property `gap` to `4px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1251 |   padding: 4px;
     | Sets CSS property `padding` to `4px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1252 |   background: var(--surface);
     | Sets CSS property `background` to `var(--surface)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1253 |   border-radius: var(--radius-sm);
     | Sets CSS property `border-radius` to `var(--radius-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1254 |   margin-bottom: var(--space-5);
     | Sets CSS property `margin-bottom` to `var(--space-5)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1255 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1256 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1257 | .mode-tab {
     | Opens a rule for selector `.mode-tab`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1258 |   flex: 1;
     | Sets CSS property `flex` to `1`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1259 |   padding: 7px 10px;
     | Sets CSS property `padding` to `7px 10px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1260 |   border-radius: 6px;
     | Sets CSS property `border-radius` to `6px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1261 |   border: none;
     | Sets CSS property `border` to `none`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1262 |   cursor: pointer;
     | Sets CSS property `cursor` to `pointer`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1263 |   font-size: 13px;
     | Sets CSS property `font-size` to `13px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1264 |   font-weight: 600;
     | Sets CSS property `font-weight` to `600`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1265 |   color: var(--muted);
     | Sets CSS property `color` to `var(--muted)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1266 |   background: transparent;
     | Sets CSS property `background` to `transparent`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1267 |   font-family: inherit;
     | Sets CSS property `font-family` to `inherit`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1268 |   transition: all 0.15s;
     | Sets CSS property `transition` to `all 0.15s`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1269 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1270 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1271 | .mode-tab.active {
     | Opens a rule for selector `.mode-tab.active`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1272 |   background: var(--card);
     | Sets CSS property `background` to `var(--card)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1273 |   color: var(--indigo-light);
     | Sets CSS property `color` to `var(--indigo-light)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1274 |   box-shadow: var(--shadow-card);
     | Sets CSS property `box-shadow` to `var(--shadow-card)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1275 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1276 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1277 | /* ── Dev Notice Banner ──────────────────────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── Dev Notice Banner ──────────────────────────────── */

1278 | .dev-banner {
     | Opens a rule for selector `.dev-banner`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1279 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1280 |   align-items: flex-start;
     | Sets CSS property `align-items` to `flex-start`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1281 |   justify-content: space-between;
     | Sets CSS property `justify-content` to `space-between`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1282 |   gap: var(--space-4);
     | Sets CSS property `gap` to `var(--space-4)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1283 |   background: var(--card);
     | Sets CSS property `background` to `var(--card)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1284 |   border: 1px solid var(--border);
     | Sets CSS property `border` to `1px solid var(--border)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1285 |   border-radius: var(--radius);
     | Sets CSS property `border-radius` to `var(--radius)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1286 |   padding: var(--space-4) var(--space-5);
     | Sets CSS property `padding` to `var(--space-4) var(--space-5)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1287 |   margin-bottom: var(--space-5);
     | Sets CSS property `margin-bottom` to `var(--space-5)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1288 |   box-shadow: var(--shadow-card);
     | Sets CSS property `box-shadow` to `var(--shadow-card)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1289 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1290 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1291 | .dev-banner-main {
     | Opens a rule for selector `.dev-banner-main`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1292 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1293 |   align-items: flex-start;
     | Sets CSS property `align-items` to `flex-start`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1294 |   gap: var(--space-3);
     | Sets CSS property `gap` to `var(--space-3)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1295 |   min-width: 0;
     | Sets CSS property `min-width` to `0`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1296 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1297 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1298 | .dev-banner-icon {
     | Opens a rule for selector `.dev-banner-icon`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1299 |   width: 20px;
     | Sets CSS property `width` to `20px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1300 |   height: 20px;
     | Sets CSS property `height` to `20px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1301 |   border-radius: 50%;
     | Sets CSS property `border-radius` to `50%`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1302 |   background: var(--indigo-dim);
     | Sets CSS property `background` to `var(--indigo-dim)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1303 |   color: var(--indigo-light);
     | Sets CSS property `color` to `var(--indigo-light)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1304 |   font-size: 12px;
     | Sets CSS property `font-size` to `12px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1305 |   font-weight: 700;
     | Sets CSS property `font-weight` to `700`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1306 |   font-style: italic;
     | Sets CSS property `font-style` to `italic`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1307 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1308 |   align-items: center;
     | Sets CSS property `align-items` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1309 |   justify-content: center;
     | Sets CSS property `justify-content` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1310 |   flex-shrink: 0;
     | Sets CSS property `flex-shrink` to `0`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1311 |   margin-top: 1px;
     | Sets CSS property `margin-top` to `1px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1312 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1313 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1314 | .dev-banner-text {
     | Opens a rule for selector `.dev-banner-text`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1315 |   font-size: var(--text-sm);
     | Sets CSS property `font-size` to `var(--text-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1316 |   color: var(--text-soft);
     | Sets CSS property `color` to `var(--text-soft)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1317 |   line-height: 1.6;
     | Sets CSS property `line-height` to `1.6`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1318 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1319 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1320 | .dev-banner-text strong { color: var(--text); }
     | CSS line `.dev-banner-text strong { color: var(--text); }`. It is part of the stylesheet the browser applies while painting the React DOM.

1321 | .dev-banner-text-short { display: none; }
     | CSS line `.dev-banner-text-short { display: none; }`. It is part of the stylesheet the browser applies while painting the React DOM.

1322 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1323 | .dev-banner-inline-link {
     | Opens a rule for selector `.dev-banner-inline-link`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1324 |   color: var(--indigo-light);
     | Sets CSS property `color` to `var(--indigo-light)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1325 |   font-weight: 600;
     | Sets CSS property `font-weight` to `600`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1326 |   text-decoration: none;
     | Sets CSS property `text-decoration` to `none`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1327 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1328 | .dev-banner-inline-link:hover { text-decoration: underline; }
     | CSS line `.dev-banner-inline-link:hover { text-decoration: underline; }`. It is part of the stylesheet the browser applies while painting the React DOM.

1329 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1330 | .dev-banner-cta {
     | Opens a rule for selector `.dev-banner-cta`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1331 |   color: var(--indigo-light);
     | Sets CSS property `color` to `var(--indigo-light)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1332 |   font-weight: 600;
     | Sets CSS property `font-weight` to `600`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1333 |   font-size: var(--text-sm);
     | Sets CSS property `font-size` to `var(--text-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1334 |   text-decoration: none;
     | Sets CSS property `text-decoration` to `none`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1335 |   white-space: nowrap;
     | Sets CSS property `white-space` to `nowrap`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1336 |   flex-shrink: 0;
     | Sets CSS property `flex-shrink` to `0`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1337 |   margin-top: 2px;
     | Sets CSS property `margin-top` to `2px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1338 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1339 | .dev-banner-cta:hover { text-decoration: underline; }
     | CSS line `.dev-banner-cta:hover { text-decoration: underline; }`. It is part of the stylesheet the browser applies while painting the React DOM.

1340 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1341 | @media (max-width: 768px) {
     | Opens a media query `@media (max-width: 768px) {`. The rules inside apply only when that screen condition is true, so the same components reflow on a phone.

1342 |   .dev-banner { padding: var(--space-3) var(--space-4); margin-bottom: var(--space-4); }
     | CSS line `.dev-banner { padding: var(--space-3) var(--space-4); margin-bottom: var(--space-4); }`. It is part of the stylesheet the browser applies while painting the React DOM.

1343 |   .dev-banner-text-full { display: none; }
     | CSS line `.dev-banner-text-full { display: none; }`. It is part of the stylesheet the browser applies while painting the React DOM.

1344 |   .dev-banner-text-short { display: inline; }
     | CSS line `.dev-banner-text-short { display: inline; }`. It is part of the stylesheet the browser applies while painting the React DOM.

1345 |   .dev-banner-cta { display: none; }
     | CSS line `.dev-banner-cta { display: none; }`. It is part of the stylesheet the browser applies while painting the React DOM.

1346 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1347 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1348 | /* ── Feedback CTA Card ──────────────────────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── Feedback CTA Card ──────────────────────────────── */

1349 | .feedback-cta-title {
     | Opens a rule for selector `.feedback-cta-title`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1350 |   font-size: 15px;
     | Sets CSS property `font-size` to `15px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1351 |   font-weight: 700;
     | Sets CSS property `font-weight` to `700`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1352 |   color: var(--text);
     | Sets CSS property `color` to `var(--text)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1353 |   margin-bottom: 6px;
     | Sets CSS property `margin-bottom` to `6px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1354 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1355 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1356 | .feedback-cta-mobile { display: none; }
     | CSS line `.feedback-cta-mobile { display: none; }`. It is part of the stylesheet the browser applies while painting the React DOM.

1357 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1358 | @media (max-width: 1024px) {
     | Opens a media query `@media (max-width: 1024px) {`. The rules inside apply only when that screen condition is true, so the same components reflow on a phone.

1359 |   .feedback-cta-desktop { display: none; }
     | CSS line `.feedback-cta-desktop { display: none; }`. It is part of the stylesheet the browser applies while painting the React DOM.

1360 |   .feedback-cta-mobile { display: block; }
     | CSS line `.feedback-cta-mobile { display: block; }`. It is part of the stylesheet the browser applies while painting the React DOM.

1361 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1362 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1363 | /* ── What Next Card ─────────────────────────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── What Next Card ─────────────────────────────────── */

1364 | .what-next-card {
     | Opens a rule for selector `.what-next-card`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1365 |   background: linear-gradient(135deg, var(--indigo-dim), rgba(99, 102, 241, 0.04));
     | Sets CSS property `background` to `linear-gradient(135deg, var(--indigo-dim), rgba(99, 102, 241, 0.04))`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1366 |   border: 1px solid rgba(99, 102, 241, 0.2);
     | Sets CSS property `border` to `1px solid rgba(99, 102, 241, 0.2)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1367 |   border-radius: var(--radius);
     | Sets CSS property `border-radius` to `var(--radius)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1368 |   padding: var(--space-5);
     | Sets CSS property `padding` to `var(--space-5)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1369 |   position: relative;
     | Sets CSS property `position` to `relative`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1370 |   overflow: hidden;
     | Sets CSS property `overflow` to `hidden`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1371 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1372 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1373 | .what-next-card::before {
     | Opens a rule for selector `.what-next-card::before`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1374 |   content: '';
     | Sets CSS property `content` to `''`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1375 |   position: absolute;
     | Sets CSS property `position` to `absolute`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1376 |   top: -20px; right: -20px;
     | Sets CSS property `top` to `-20px; right: -20px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1377 |   width: 120px; height: 120px;
     | Sets CSS property `width` to `120px; height: 120px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1378 |   background: radial-gradient(circle, rgba(99, 102, 241, 0.15), transparent 70%);
     | Sets CSS property `background` to `radial-gradient(circle, rgba(99, 102, 241, 0.15), transparent 70%)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1379 |   pointer-events: none;
     | Sets CSS property `pointer-events` to `none`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1380 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1381 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1382 | .what-next-label {
     | Opens a rule for selector `.what-next-label`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1383 |   font-size: var(--text-xs);
     | Sets CSS property `font-size` to `var(--text-xs)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1384 |   text-transform: uppercase;
     | Sets CSS property `text-transform` to `uppercase`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1385 |   letter-spacing: 1px;
     | Sets CSS property `letter-spacing` to `1px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1386 |   color: var(--indigo-light);
     | Sets CSS property `color` to `var(--indigo-light)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1387 |   font-weight: 700;
     | Sets CSS property `font-weight` to `700`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1388 |   margin-bottom: 8px;
     | Sets CSS property `margin-bottom` to `8px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1389 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1390 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1391 | .what-next-task {
     | Opens a rule for selector `.what-next-task`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1392 |   font-size: 18px;
     | Sets CSS property `font-size` to `18px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1393 |   font-weight: 700;
     | Sets CSS property `font-weight` to `700`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1394 |   color: var(--text);
     | Sets CSS property `color` to `var(--text)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1395 |   margin-bottom: 6px;
     | Sets CSS property `margin-bottom` to `6px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1396 |   line-height: 1.3;
     | Sets CSS property `line-height` to `1.3`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1397 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1398 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1399 | .what-next-reason {
     | Opens a rule for selector `.what-next-reason`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1400 |   font-size: var(--text-sm);
     | Sets CSS property `font-size` to `var(--text-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1401 |   color: var(--text-soft);
     | Sets CSS property `color` to `var(--text-soft)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1402 |   margin-bottom: 14px;
     | Sets CSS property `margin-bottom` to `14px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1403 |   line-height: 1.5;
     | Sets CSS property `line-height` to `1.5`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1404 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1405 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1406 | /* ── Subtasks ───────────────────────────────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── Subtasks ───────────────────────────────────────── */

1407 | .subtask-list {
     | Opens a rule for selector `.subtask-list`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1408 |   padding-left: 30px;
     | Sets CSS property `padding-left` to `30px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1409 |   margin-top: 8px;
     | Sets CSS property `margin-top` to `8px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1410 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1411 |   flex-direction: column;
     | Sets CSS property `flex-direction` to `column`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1412 |   gap: 6px;
     | Sets CSS property `gap` to `6px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1413 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1414 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1415 | .subtask-item {
     | Opens a rule for selector `.subtask-item`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1416 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1417 |   align-items: center;
     | Sets CSS property `align-items` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1418 |   gap: 8px;
     | Sets CSS property `gap` to `8px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1419 |   font-size: 13px;
     | Sets CSS property `font-size` to `13px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1420 |   color: var(--text-soft);
     | Sets CSS property `color` to `var(--text-soft)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1421 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1422 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1423 | .subtask-dot {
     | Opens a rule for selector `.subtask-dot`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1424 |   width: 5px;
     | Sets CSS property `width` to `5px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1425 |   height: 5px;
     | Sets CSS property `height` to `5px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1426 |   border-radius: 50%;
     | Sets CSS property `border-radius` to `50%`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1427 |   background: var(--indigo);
     | Sets CSS property `background` to `var(--indigo)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1428 |   flex-shrink: 0;
     | Sets CSS property `flex-shrink` to `0`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1429 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1430 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1431 | /* ── Mindfulness Audio Player ───────────────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── Mindfulness Audio Player ───────────────────────── */

1432 | .audio-player {
     | Opens a rule for selector `.audio-player`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1433 |   background: var(--surface);
     | Sets CSS property `background` to `var(--surface)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1434 |   border-radius: var(--radius);
     | Sets CSS property `border-radius` to `var(--radius)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1435 |   padding: 28px 24px;
     | Sets CSS property `padding` to `28px 24px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1436 |   text-align: center;
     | Sets CSS property `text-align` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1437 |   border: 1px solid var(--border);
     | Sets CSS property `border` to `1px solid var(--border)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1438 |   transition: background 0.3s;
     | Sets CSS property `transition` to `background 0.3s`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1439 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1440 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1441 | .audio-player.playing {
     | Opens a rule for selector `.audio-player.playing`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1442 |   background: linear-gradient(135deg, rgba(99, 102, 241, 0.12), rgba(6, 182, 212, 0.06));
     | Sets CSS property `background` to `linear-gradient(135deg, rgba(99, 102, 241, 0.12), rgba(6, 182, 212, 0.06))`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1443 |   border-color: rgba(99, 102, 241, 0.3);
     | Sets CSS property `border-color` to `rgba(99, 102, 241, 0.3)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1444 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1445 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1446 | .audio-state-label { font-size: var(--text-sm); color: var(--muted); margin-bottom: 8px; }
     | CSS line `.audio-state-label { font-size: var(--text-sm); color: var(--muted); margin-bottom: 8px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

1447 | .audio-time { font-size: 42px; font-weight: 800; font-variant-numeric: tabular-nums; color: var(--text); }
     | CSS line `.audio-time { font-size: 42px; font-weight: 800; font-variant-numeric: tabular-nums; color: var(--text); }`. It is part of the stylesheet the browser applies while painting the React DOM.

1448 | .audio-duration { font-size: var(--text-xs); color: var(--muted); margin-top: 4px; margin-bottom: 16px; }
     | CSS line `.audio-duration { font-size: var(--text-xs); color: var(--muted); margin-top: 4px; margin-bottom: 16px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

1449 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1450 | .audio-progress {
     | Opens a rule for selector `.audio-progress`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1451 |   width: 100%;
     | Sets CSS property `width` to `100%`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1452 |   height: 4px;
     | Sets CSS property `height` to `4px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1453 |   background: var(--border);
     | Sets CSS property `background` to `var(--border)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1454 |   border-radius: 2px;
     | Sets CSS property `border-radius` to `2px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1455 |   margin-bottom: 20px;
     | Sets CSS property `margin-bottom` to `20px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1456 |   overflow: hidden;
     | Sets CSS property `overflow` to `hidden`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1457 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1458 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1459 | .audio-progress-fill {
     | Opens a rule for selector `.audio-progress-fill`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1460 |   height: 100%;
     | Sets CSS property `height` to `100%`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1461 |   background: var(--brand-gradient);
     | Sets CSS property `background` to `var(--brand-gradient)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1462 |   border-radius: 2px;
     | Sets CSS property `border-radius` to `2px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1463 |   transition: width 0.5s;
     | Sets CSS property `transition` to `width 0.5s`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1464 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1465 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1466 | /* ── Affirmation ────────────────────────────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── Affirmation ────────────────────────────────────── */

1467 | .affirmation-card {
     | Opens a rule for selector `.affirmation-card`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1468 |   background: linear-gradient(135deg, var(--indigo-dim), var(--green-dim));
     | Sets CSS property `background` to `linear-gradient(135deg, var(--indigo-dim), var(--green-dim))`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1469 |   border: 1px solid rgba(99, 102, 241, 0.2);
     | Sets CSS property `border` to `1px solid rgba(99, 102, 241, 0.2)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1470 |   border-radius: var(--radius);
     | Sets CSS property `border-radius` to `var(--radius)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1471 |   padding: 16px 20px;
     | Sets CSS property `padding` to `16px 20px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1472 |   font-weight: 600;
     | Sets CSS property `font-weight` to `600`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1473 |   font-size: var(--text-base);
     | Sets CSS property `font-size` to `var(--text-base)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1474 |   line-height: 1.5;
     | Sets CSS property `line-height` to `1.5`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1475 |   color: var(--text-soft);
     | Sets CSS property `color` to `var(--text-soft)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1476 |   text-align: center;
     | Sets CSS property `text-align` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1477 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1478 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1479 | /* ── Focus Status Pill ──────────────────────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── Focus Status Pill ──────────────────────────────── */

1480 | .focus-status {
     | Opens a rule for selector `.focus-status`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1481 |   display: inline-flex;
     | Sets CSS property `display` to `inline-flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1482 |   align-items: center;
     | Sets CSS property `align-items` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1483 |   gap: 6px;
     | Sets CSS property `gap` to `6px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1484 |   padding: 4px 12px;
     | Sets CSS property `padding` to `4px 12px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1485 |   border-radius: 20px;
     | Sets CSS property `border-radius` to `20px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1486 |   font-size: var(--text-xs);
     | Sets CSS property `font-size` to `var(--text-xs)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1487 |   font-weight: 600;
     | Sets CSS property `font-weight` to `600`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1488 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1489 | .focus-status-dot {
     | Opens a rule for selector `.focus-status-dot`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1490 |   width: 6px;
     | Sets CSS property `width` to `6px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1491 |   height: 6px;
     | Sets CSS property `height` to `6px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1492 |   border-radius: 50%;
     | Sets CSS property `border-radius` to `50%`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1493 |   background: currentColor;
     | Sets CSS property `background` to `currentColor`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1494 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1495 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1496 | /* ── Connectors Page ─────────────────────────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── Connectors Page ─────────────────────────────────── */

1497 | .connectors-page { display: flex; flex-direction: column; gap: var(--space-4); }
     | CSS line `.connectors-page { display: flex; flex-direction: column; gap: var(--space-4); }`. It is part of the stylesheet the browser applies while painting the React DOM.

1498 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1499 | .connectors-list { display: flex; flex-direction: column; gap: var(--space-3); }
     | CSS line `.connectors-list { display: flex; flex-direction: column; gap: var(--space-3); }`. It is part of the stylesheet the browser applies while painting the React DOM.

1500 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1501 | .connector-card {
     | Opens a rule for selector `.connector-card`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1502 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1503 |   align-items: center;
     | Sets CSS property `align-items` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1504 |   gap: var(--space-4);
     | Sets CSS property `gap` to `var(--space-4)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1505 |   background: var(--card);
     | Sets CSS property `background` to `var(--card)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1506 |   border: 1px solid var(--border);
     | Sets CSS property `border` to `1px solid var(--border)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1507 |   border-radius: var(--radius);
     | Sets CSS property `border-radius` to `var(--radius)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1508 |   padding: var(--space-4) var(--space-5);
     | Sets CSS property `padding` to `var(--space-4) var(--space-5)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1509 |   transition: border-color 0.15s;
     | Sets CSS property `transition` to `border-color 0.15s`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1510 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1511 | .connector-card:hover { border-color: var(--border-active); }
     | CSS line `.connector-card:hover { border-color: var(--border-active); }`. It is part of the stylesheet the browser applies while painting the React DOM.

1512 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1513 | .connector-card-icon {
     | Opens a rule for selector `.connector-card-icon`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1514 |   width: 44px;
     | Sets CSS property `width` to `44px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1515 |   height: 44px;
     | Sets CSS property `height` to `44px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1516 |   border-radius: 12px;
     | Sets CSS property `border-radius` to `12px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1517 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1518 |   align-items: center;
     | Sets CSS property `align-items` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1519 |   justify-content: center;
     | Sets CSS property `justify-content` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1520 |   flex-shrink: 0;
     | Sets CSS property `flex-shrink` to `0`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1521 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1522 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1523 | .connector-card-body { flex: 1; min-width: 0; }
     | CSS line `.connector-card-body { flex: 1; min-width: 0; }`. It is part of the stylesheet the browser applies while painting the React DOM.

1524 | .connector-card-title { font-weight: 700; font-size: var(--text-sm); color: var(--text); margin-bottom: 2px; }
     | CSS line `.connector-card-title { font-weight: 700; font-size: var(--text-sm); color: var(--text); margin-bottom: 2px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

1525 | .connector-card-desc { font-size: var(--text-xs); color: var(--muted); line-height: 1.5; }
     | CSS line `.connector-card-desc { font-size: var(--text-xs); color: var(--muted); line-height: 1.5; }`. It is part of the stylesheet the browser applies while painting the React DOM.

1526 | .connector-card-meta { font-size: var(--text-xs); color: var(--muted); margin-top: 4px; }
     | CSS line `.connector-card-meta { font-size: var(--text-xs); color: var(--muted); margin-top: 4px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

1527 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1528 | .connector-card-actions { display: flex; gap: var(--space-2); flex-shrink: 0; align-items: center; }
     | CSS line `.connector-card-actions { display: flex; gap: var(--space-2); flex-shrink: 0; align-items: center; }`. It is part of the stylesheet the browser applies while painting the React DOM.

1529 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1530 | .btn-connector {
     | Opens a rule for selector `.btn-connector`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1531 |   padding: 8px 16px;
     | Sets CSS property `padding` to `8px 16px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1532 |   border-radius: var(--radius-sm);
     | Sets CSS property `border-radius` to `var(--radius-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1533 |   font-size: var(--text-xs);
     | Sets CSS property `font-size` to `var(--text-xs)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1534 |   font-weight: 700;
     | Sets CSS property `font-weight` to `700`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1535 |   cursor: pointer;
     | Sets CSS property `cursor` to `pointer`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1536 |   border: none;
     | Sets CSS property `border` to `none`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1537 |   font-family: inherit;
     | Sets CSS property `font-family` to `inherit`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1538 |   transition: all 0.15s;
     | Sets CSS property `transition` to `all 0.15s`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1539 |   white-space: nowrap;
     | Sets CSS property `white-space` to `nowrap`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1540 |   min-height: 36px;
     | Sets CSS property `min-height` to `36px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1541 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1542 | .btn-connector:disabled { opacity: 0.6; cursor: not-allowed; }
     | CSS line `.btn-connector:disabled { opacity: 0.6; cursor: not-allowed; }`. It is part of the stylesheet the browser applies while painting the React DOM.

1543 | .btn-connector-connect {
     | Opens a rule for selector `.btn-connector-connect`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1544 |   background: var(--brand-gradient);
     | Sets CSS property `background` to `var(--brand-gradient)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1545 |   color: #fff;
     | Sets CSS property `color` to `#fff`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1546 |   box-shadow: 0 2px 8px rgba(99, 102, 241, 0.3);
     | Sets CSS property `box-shadow` to `0 2px 8px rgba(99, 102, 241, 0.3)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1547 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1548 | .btn-connector-connect:hover:not(:disabled) { filter: brightness(1.1); }
     | CSS line `.btn-connector-connect:hover:not(:disabled) { filter: brightness(1.1); }`. It is part of the stylesheet the browser applies while painting the React DOM.

1549 | .btn-connector-sync {
     | Opens a rule for selector `.btn-connector-sync`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1550 |   background: var(--indigo-dim);
     | Sets CSS property `background` to `var(--indigo-dim)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1551 |   color: var(--indigo-light);
     | Sets CSS property `color` to `var(--indigo-light)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1552 |   border: 1px solid rgba(99, 102, 241, 0.2);
     | Sets CSS property `border` to `1px solid rgba(99, 102, 241, 0.2)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1553 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1554 | .btn-connector-sync:hover:not(:disabled) { background: rgba(99, 102, 241, 0.2); }
     | CSS line `.btn-connector-sync:hover:not(:disabled) { background: rgba(99, 102, 241, 0.2); }`. It is part of the stylesheet the browser applies while painting the React DOM.

1555 | .btn-connector-disconnect {
     | Opens a rule for selector `.btn-connector-disconnect`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1556 |   background: transparent;
     | Sets CSS property `background` to `transparent`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1557 |   color: var(--muted);
     | Sets CSS property `color` to `var(--muted)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1558 |   border: 1px solid var(--border);
     | Sets CSS property `border` to `1px solid var(--border)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1559 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1560 | .btn-connector-disconnect:hover { color: var(--red); border-color: var(--red); }
     | CSS line `.btn-connector-disconnect:hover { color: var(--red); border-color: var(--red); }`. It is part of the stylesheet the browser applies while painting the React DOM.

1561 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1562 | .connectors-toast {
     | Opens a rule for selector `.connectors-toast`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1563 |   position: fixed;
     | Sets CSS property `position` to `fixed`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1564 |   top: calc(var(--top-bar-h) + 12px);
     | Sets CSS property `top` to `calc(var(--top-bar-h) + 12px)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1565 |   right: 20px;
     | Sets CSS property `right` to `20px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1566 |   padding: 10px 18px;
     | Sets CSS property `padding` to `10px 18px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1567 |   border-radius: var(--radius-sm);
     | Sets CSS property `border-radius` to `var(--radius-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1568 |   font-size: var(--text-sm);
     | Sets CSS property `font-size` to `var(--text-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1569 |   font-weight: 600;
     | Sets CSS property `font-weight` to `600`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1570 |   z-index: 300;
     | Sets CSS property `z-index` to `300`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1571 |   box-shadow: var(--shadow);
     | Sets CSS property `box-shadow` to `var(--shadow)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1572 |   animation: toastIn 0.2s ease;
     | Sets CSS property `animation` to `toastIn 0.2s ease`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1573 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1574 | .connectors-toast--success { background: var(--green); color: #fff; }
     | CSS line `.connectors-toast--success { background: var(--green); color: #fff; }`. It is part of the stylesheet the browser applies while painting the React DOM.

1575 | .connectors-toast--error { background: var(--red); color: #fff; }
     | CSS line `.connectors-toast--error { background: var(--red); color: #fff; }`. It is part of the stylesheet the browser applies while painting the React DOM.

1576 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1577 | @keyframes toastIn {
     | Starts an animation definition `@keyframes toastIn {`. Later rules refer to this name in an `animation` property.

1578 |   from { opacity: 0; transform: translateY(-8px); }
     | CSS line `from { opacity: 0; transform: translateY(-8px); }`. It is part of the stylesheet the browser applies while painting the React DOM.

1579 |   to   { opacity: 1; transform: none; }
     | CSS line `to   { opacity: 1; transform: none; }`. It is part of the stylesheet the browser applies while painting the React DOM.

1580 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1581 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1582 | /* ── Chart Legend ────────────────────────────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── Chart Legend ────────────────────────────────────── */

1583 | .chart-header {
     | Opens a rule for selector `.chart-header`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1584 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1585 |   align-items: center;
     | Sets CSS property `align-items` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1586 |   justify-content: space-between;
     | Sets CSS property `justify-content` to `space-between`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1587 |   flex-wrap: wrap;
     | Sets CSS property `flex-wrap` to `wrap`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1588 |   gap: 8px;
     | Sets CSS property `gap` to `8px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1589 |   margin-bottom: 12px;
     | Sets CSS property `margin-bottom` to `12px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1590 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1591 | .chart-legend {
     | Opens a rule for selector `.chart-legend`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1592 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1593 |   gap: var(--space-4);
     | Sets CSS property `gap` to `var(--space-4)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1594 |   align-items: center;
     | Sets CSS property `align-items` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1595 |   flex-wrap: wrap;
     | Sets CSS property `flex-wrap` to `wrap`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1596 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1597 | .chart-legend-item {
     | Opens a rule for selector `.chart-legend-item`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1598 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1599 |   align-items: center;
     | Sets CSS property `align-items` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1600 |   gap: 6px;
     | Sets CSS property `gap` to `6px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1601 |   font-size: var(--text-xs);
     | Sets CSS property `font-size` to `var(--text-xs)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1602 |   color: var(--muted);
     | Sets CSS property `color` to `var(--muted)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1603 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1604 | .chart-legend-swatch {
     | Opens a rule for selector `.chart-legend-swatch`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1605 |   width: 16px;
     | Sets CSS property `width` to `16px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1606 |   height: 3px;
     | Sets CSS property `height` to `3px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1607 |   border-radius: 2px;
     | Sets CSS property `border-radius` to `2px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1608 |   flex-shrink: 0;
     | Sets CSS property `flex-shrink` to `0`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1609 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1610 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1611 | /* ── Bottom Sheet (mobile slide-up) ──────────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── Bottom Sheet (mobile slide-up) ──────────────────── */

1612 | .bottom-sheet-overlay {
     | Opens a rule for selector `.bottom-sheet-overlay`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1613 |   display: none;
     | Sets CSS property `display` to `none`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1614 |   position: fixed;
     | Sets CSS property `position` to `fixed`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1615 |   inset: 0;
     | Sets CSS property `inset` to `0`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1616 |   background: rgba(0, 0, 0, 0.5);
     | Sets CSS property `background` to `rgba(0, 0, 0, 0.5)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1617 |   z-index: 149;
     | Sets CSS property `z-index` to `149`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1618 |   backdrop-filter: blur(2px);
     | Sets CSS property `backdrop-filter` to `blur(2px)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1619 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1620 | .bottom-sheet {
     | Opens a rule for selector `.bottom-sheet`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1621 |   display: none;
     | Sets CSS property `display` to `none`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1622 |   position: fixed;
     | Sets CSS property `position` to `fixed`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1623 |   bottom: 0;
     | Sets CSS property `bottom` to `0`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1624 |   left: 0;
     | Sets CSS property `left` to `0`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1625 |   right: 0;
     | Sets CSS property `right` to `0`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1626 |   background: var(--surface);
     | Sets CSS property `background` to `var(--surface)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1627 |   border-radius: 20px 20px 0 0;
     | Sets CSS property `border-radius` to `20px 20px 0 0`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1628 |   border-top: 1px solid var(--border);
     | Sets CSS property `border-top` to `1px solid var(--border)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1629 |   z-index: 150;
     | Sets CSS property `z-index` to `150`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1630 |   transform: translateY(100%);
     | Sets CSS property `transform` to `translateY(100%)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1631 |   transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
     | Sets CSS property `transition` to `transform 0.3s cubic-bezier(0.4, 0, 0.2, 1)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1632 |   padding: 0 var(--space-4) env(safe-area-inset-bottom, var(--space-5));
     | Sets CSS property `padding` to `0 var(--space-4) env(safe-area-inset-bottom, var(--space-5))`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1633 |   padding-bottom: calc(env(safe-area-inset-bottom, 0px) + var(--space-5));
     | Sets CSS property `padding-bottom` to `calc(env(safe-area-inset-bottom, 0px) + var(--space-5))`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1634 |   max-height: 85vh;
     | Sets CSS property `max-height` to `85vh`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1635 |   overflow-y: auto;
     | Sets CSS property `overflow-y` to `auto`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1636 |   box-shadow: 0 -4px 24px rgba(0, 0, 0, 0.3);
     | Sets CSS property `box-shadow` to `0 -4px 24px rgba(0, 0, 0, 0.3)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1637 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1638 | .bottom-sheet.open { transform: translateY(0); }
     | CSS line `.bottom-sheet.open { transform: translateY(0); }`. It is part of the stylesheet the browser applies while painting the React DOM.

1639 | .bottom-sheet-handle {
     | Opens a rule for selector `.bottom-sheet-handle`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1640 |   width: 36px;
     | Sets CSS property `width` to `36px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1641 |   height: 4px;
     | Sets CSS property `height` to `4px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1642 |   border-radius: 2px;
     | Sets CSS property `border-radius` to `2px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1643 |   background: var(--border);
     | Sets CSS property `background` to `var(--border)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1644 |   margin: 12px auto 16px;
     | Sets CSS property `margin` to `12px auto 16px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1645 |   flex-shrink: 0;
     | Sets CSS property `flex-shrink` to `0`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1646 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1647 | .bottom-sheet-section {
     | Opens a rule for selector `.bottom-sheet-section`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1648 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1649 |   flex-direction: column;
     | Sets CSS property `flex-direction` to `column`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1650 |   gap: 1px;
     | Sets CSS property `gap` to `1px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1651 |   padding-bottom: var(--space-3);
     | Sets CSS property `padding-bottom` to `var(--space-3)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1652 |   margin-bottom: var(--space-2);
     | Sets CSS property `margin-bottom` to `var(--space-2)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1653 |   border-bottom: 1px solid var(--border);
     | Sets CSS property `border-bottom` to `1px solid var(--border)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1654 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1655 | .bottom-sheet-section:last-of-type { border-bottom: none; }
     | CSS line `.bottom-sheet-section:last-of-type { border-bottom: none; }`. It is part of the stylesheet the browser applies while painting the React DOM.

1656 | .bottom-sheet-footer {
     | Opens a rule for selector `.bottom-sheet-footer`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1657 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1658 |   flex-direction: column;
     | Sets CSS property `flex-direction` to `column`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1659 |   gap: var(--space-2);
     | Sets CSS property `gap` to `var(--space-2)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1660 |   padding: var(--space-3) 0 var(--space-2);
     | Sets CSS property `padding` to `var(--space-3) 0 var(--space-2)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1661 |   position: sticky;
     | Sets CSS property `position` to `sticky`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1662 |   bottom: 0;
     | Sets CSS property `bottom` to `0`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1663 |   background: var(--surface);
     | Sets CSS property `background` to `var(--surface)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1664 |   border-top: 1px solid var(--border);
     | Sets CSS property `border-top` to `1px solid var(--border)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1665 |   margin-top: var(--space-2);
     | Sets CSS property `margin-top` to `var(--space-2)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1666 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1667 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1668 | /* Sheet connector rows */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* Sheet connector rows */

1669 | .sheet-connectors { display: flex; flex-direction: column; gap: 2px; }
     | CSS line `.sheet-connectors { display: flex; flex-direction: column; gap: 2px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

1670 | .sheet-connector-row {
     | Opens a rule for selector `.sheet-connector-row`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1671 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1672 |   align-items: center;
     | Sets CSS property `align-items` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1673 |   gap: var(--space-2);
     | Sets CSS property `gap` to `var(--space-2)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1674 |   padding: 7px 4px;
     | Sets CSS property `padding` to `7px 4px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1675 |   border-radius: var(--radius-sm);
     | Sets CSS property `border-radius` to `var(--radius-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1676 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1677 | .sheet-connector-icon {
     | Opens a rule for selector `.sheet-connector-icon`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1678 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1679 |   align-items: center;
     | Sets CSS property `align-items` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1680 |   justify-content: center;
     | Sets CSS property `justify-content` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1681 |   width: 26px;
     | Sets CSS property `width` to `26px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1682 |   height: 26px;
     | Sets CSS property `height` to `26px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1683 |   border-radius: 6px;
     | Sets CSS property `border-radius` to `6px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1684 |   flex-shrink: 0;
     | Sets CSS property `flex-shrink` to `0`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1685 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1686 | .sheet-connector-label {
     | Opens a rule for selector `.sheet-connector-label`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1687 |   flex: 1;
     | Sets CSS property `flex` to `1`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1688 |   font-size: var(--text-sm);
     | Sets CSS property `font-size` to `var(--text-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1689 |   color: var(--text);
     | Sets CSS property `color` to `var(--text)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1690 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1691 | .sheet-connector-dot {
     | Opens a rule for selector `.sheet-connector-dot`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1692 |   width: 7px;
     | Sets CSS property `width` to `7px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1693 |   height: 7px;
     | Sets CSS property `height` to `7px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1694 |   border-radius: 50%;
     | Sets CSS property `border-radius` to `50%`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1695 |   background: var(--muted);
     | Sets CSS property `background` to `var(--muted)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1696 |   flex-shrink: 0;
     | Sets CSS property `flex-shrink` to `0`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1697 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1698 | .sheet-connector-dot.connected { background: #22c55e; }
     | CSS line `.sheet-connector-dot.connected { background: #22c55e; }`. It is part of the stylesheet the browser applies while painting the React DOM.

1699 | .sheet-connector-btn {
     | Opens a rule for selector `.sheet-connector-btn`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1700 |   font-size: 11px;
     | Sets CSS property `font-size` to `11px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1701 |   padding: 3px 9px;
     | Sets CSS property `padding` to `3px 9px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1702 |   border-radius: var(--radius-sm);
     | Sets CSS property `border-radius` to `var(--radius-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1703 |   border: 1px solid var(--border);
     | Sets CSS property `border` to `1px solid var(--border)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1704 |   background: transparent;
     | Sets CSS property `background` to `transparent`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1705 |   color: var(--text-muted);
     | Sets CSS property `color` to `var(--text-muted)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1706 |   cursor: pointer;
     | Sets CSS property `cursor` to `pointer`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1707 |   font-family: inherit;
     | Sets CSS property `font-family` to `inherit`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1708 |   transition: all 0.15s;
     | Sets CSS property `transition` to `all 0.15s`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1709 |   white-space: nowrap;
     | Sets CSS property `white-space` to `nowrap`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1710 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1711 | .sheet-connector-btn:hover { border-color: var(--border-active); color: var(--text); }
     | CSS line `.sheet-connector-btn:hover { border-color: var(--border-active); color: var(--text); }`. It is part of the stylesheet the browser applies while painting the React DOM.

1712 | .sheet-connector-btn:disabled { opacity: 0.5; cursor: not-allowed; }
     | CSS line `.sheet-connector-btn:disabled { opacity: 0.5; cursor: not-allowed; }`. It is part of the stylesheet the browser applies while painting the React DOM.

1713 | .sheet-connector-btn--on {
     | Opens a rule for selector `.sheet-connector-btn--on`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1714 |   border-color: var(--c, var(--indigo));
     | Sets CSS property `border-color` to `var(--c, var(--indigo))`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1715 |   color: var(--c, var(--indigo));
     | Sets CSS property `color` to `var(--c, var(--indigo))`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1716 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1717 | .sheet-connector-btn--on:hover { background: color-mix(in srgb, var(--c, var(--indigo)) 12%, transparent); }
     | CSS line `.sheet-connector-btn--on:hover { background: color-mix(in srgb, var(--c, var(--indigo)) 12%, transparent); }`. It is part of the stylesheet the browser applies while painting the React DOM.

1718 | .sheet-connector-btn--off { color: var(--red); border-color: transparent; font-size: 14px; padding: 2px 7px; }
     | CSS line `.sheet-connector-btn--off { color: var(--red); border-color: transparent; font-size: 14px; padding: 2px 7px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

1719 | .sheet-connector-btn--off:hover { border-color: var(--red); }
     | CSS line `.sheet-connector-btn--off:hover { border-color: var(--red); }`. It is part of the stylesheet the browser applies while painting the React DOM.

1720 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1721 | /* ── Scrollbar ───────────────────────────────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── Scrollbar ───────────────────────────────────────── */

1722 | ::-webkit-scrollbar { width: 6px; }
     | CSS line `::-webkit-scrollbar { width: 6px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

1723 | ::-webkit-scrollbar-track { background: transparent; }
     | CSS line `::-webkit-scrollbar-track { background: transparent; }`. It is part of the stylesheet the browser applies while painting the React DOM.

1724 | ::-webkit-scrollbar-thumb { background: var(--border); border-radius: 3px; }
     | CSS line `::-webkit-scrollbar-thumb { background: var(--border); border-radius: 3px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

1725 | ::-webkit-scrollbar-thumb:hover { background: var(--muted); }
     | CSS line `::-webkit-scrollbar-thumb:hover { background: var(--muted); }`. It is part of the stylesheet the browser applies while painting the React DOM.

1726 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1727 | /* ── Utility ─────────────────────────────────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── Utility ─────────────────────────────────────────── */

1728 | .flex { display: flex; }
     | CSS line `.flex { display: flex; }`. It is part of the stylesheet the browser applies while painting the React DOM.

1729 | .flex-col { display: flex; flex-direction: column; }
     | CSS line `.flex-col { display: flex; flex-direction: column; }`. It is part of the stylesheet the browser applies while painting the React DOM.

1730 | .items-center { align-items: center; }
     | CSS line `.items-center { align-items: center; }`. It is part of the stylesheet the browser applies while painting the React DOM.

1731 | .justify-between { justify-content: space-between; }
     | CSS line `.justify-between { justify-content: space-between; }`. It is part of the stylesheet the browser applies while painting the React DOM.

1732 | .gap-1 { gap: var(--space-1); }
     | CSS line `.gap-1 { gap: var(--space-1); }`. It is part of the stylesheet the browser applies while painting the React DOM.

1733 | .gap-2 { gap: var(--space-2); }
     | CSS line `.gap-2 { gap: var(--space-2); }`. It is part of the stylesheet the browser applies while painting the React DOM.

1734 | .gap-3 { gap: var(--space-3); }
     | CSS line `.gap-3 { gap: var(--space-3); }`. It is part of the stylesheet the browser applies while painting the React DOM.

1735 | .gap-4 { gap: var(--space-4); }
     | CSS line `.gap-4 { gap: var(--space-4); }`. It is part of the stylesheet the browser applies while painting the React DOM.

1736 | .mb-1 { margin-bottom: var(--space-1); }
     | CSS line `.mb-1 { margin-bottom: var(--space-1); }`. It is part of the stylesheet the browser applies while painting the React DOM.

1737 | .mb-2 { margin-bottom: var(--space-2); }
     | CSS line `.mb-2 { margin-bottom: var(--space-2); }`. It is part of the stylesheet the browser applies while painting the React DOM.

1738 | .mb-3 { margin-bottom: var(--space-3); }
     | CSS line `.mb-3 { margin-bottom: var(--space-3); }`. It is part of the stylesheet the browser applies while painting the React DOM.

1739 | .mb-4 { margin-bottom: var(--space-4); }
     | CSS line `.mb-4 { margin-bottom: var(--space-4); }`. It is part of the stylesheet the browser applies while painting the React DOM.

1740 | .mt-1 { margin-top: var(--space-1); }
     | CSS line `.mt-1 { margin-top: var(--space-1); }`. It is part of the stylesheet the browser applies while painting the React DOM.

1741 | .mt-2 { margin-top: var(--space-2); }
     | CSS line `.mt-2 { margin-top: var(--space-2); }`. It is part of the stylesheet the browser applies while painting the React DOM.

1742 | .mt-3 { margin-top: var(--space-3); }
     | CSS line `.mt-3 { margin-top: var(--space-3); }`. It is part of the stylesheet the browser applies while painting the React DOM.

1743 | .mt-4 { margin-top: var(--space-4); }
     | CSS line `.mt-4 { margin-top: var(--space-4); }`. It is part of the stylesheet the browser applies while painting the React DOM.

1744 | .text-sm { font-size: var(--text-sm); }
     | CSS line `.text-sm { font-size: var(--text-sm); }`. It is part of the stylesheet the browser applies while painting the React DOM.

1745 | .text-xs { font-size: var(--text-xs); }
     | CSS line `.text-xs { font-size: var(--text-xs); }`. It is part of the stylesheet the browser applies while painting the React DOM.

1746 | .text-muted { color: var(--muted); }
     | CSS line `.text-muted { color: var(--muted); }`. It is part of the stylesheet the browser applies while painting the React DOM.

1747 | .text-soft { color: var(--text-soft); }
     | CSS line `.text-soft { color: var(--text-soft); }`. It is part of the stylesheet the browser applies while painting the React DOM.

1748 | .font-bold { font-weight: 700; }
     | CSS line `.font-bold { font-weight: 700; }`. It is part of the stylesheet the browser applies while painting the React DOM.

1749 | .font-semibold { font-weight: 600; }
     | CSS line `.font-semibold { font-weight: 600; }`. It is part of the stylesheet the browser applies while painting the React DOM.

1750 | .w-full { width: 100%; }
     | CSS line `.w-full { width: 100%; }`. It is part of the stylesheet the browser applies while painting the React DOM.

1751 | .stack { display: flex; flex-direction: column; gap: 12px; }
     | CSS line `.stack { display: flex; flex-direction: column; gap: 12px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

1752 | .stack-sm { display: flex; flex-direction: column; gap: 8px; }
     | CSS line `.stack-sm { display: flex; flex-direction: column; gap: 8px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

1753 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1754 | /* ── Top Bar Avatar ─────────────────────────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── Top Bar Avatar ─────────────────────────────────── */

1755 | .top-bar-avatar {
     | Opens a rule for selector `.top-bar-avatar`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1756 |   width: 32px;
     | Sets CSS property `width` to `32px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1757 |   height: 32px;
     | Sets CSS property `height` to `32px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1758 |   border-radius: 50%;
     | Sets CSS property `border-radius` to `50%`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1759 |   background: var(--brand-gradient);
     | Sets CSS property `background` to `var(--brand-gradient)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1760 |   color: #fff;
     | Sets CSS property `color` to `#fff`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1761 |   font-size: 12px;
     | Sets CSS property `font-size` to `12px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1762 |   font-weight: 700;
     | Sets CSS property `font-weight` to `700`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1763 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1764 |   align-items: center;
     | Sets CSS property `align-items` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1765 |   justify-content: center;
     | Sets CSS property `justify-content` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1766 |   flex-shrink: 0;
     | Sets CSS property `flex-shrink` to `0`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1767 |   text-decoration: none;
     | Sets CSS property `text-decoration` to `none`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1768 |   cursor: pointer;
     | Sets CSS property `cursor` to `pointer`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1769 |   transition: opacity 0.15s, box-shadow 0.15s;
     | Sets CSS property `transition` to `opacity 0.15s, box-shadow 0.15s`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1770 |   box-shadow: 0 2px 8px rgba(99, 102, 241, 0.35);
     | Sets CSS property `box-shadow` to `0 2px 8px rgba(99, 102, 241, 0.35)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1771 |   letter-spacing: 0.5px;
     | Sets CSS property `letter-spacing` to `0.5px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1772 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1773 | .top-bar-avatar:hover { opacity: 0.85; box-shadow: 0 2px 12px rgba(99, 102, 241, 0.55); }
     | CSS line `.top-bar-avatar:hover { opacity: 0.85; box-shadow: 0 2px 12px rgba(99, 102, 241, 0.55); }`. It is part of the stylesheet the browser applies while painting the React DOM.

1774 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1775 | /* ── Profile Settings Page ──────────────────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── Profile Settings Page ──────────────────────────── */

1776 | .profile-settings-page {
     | Opens a rule for selector `.profile-settings-page`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1777 |   flex: 1;
     | Sets CSS property `flex` to `1`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1778 |   overflow-y: auto;
     | Sets CSS property `overflow-y` to `auto`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1779 |   padding: var(--space-6);
     | Sets CSS property `padding` to `var(--space-6)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1780 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1781 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1782 | .profile-settings-container {
     | Opens a rule for selector `.profile-settings-container`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1783 |   max-width: 680px;
     | Sets CSS property `max-width` to `680px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1784 |   margin: 0 auto;
     | Sets CSS property `margin` to `0 auto`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1785 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1786 |   flex-direction: column;
     | Sets CSS property `flex-direction` to `column`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1787 |   gap: var(--space-5);
     | Sets CSS property `gap` to `var(--space-5)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1788 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1789 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1790 | .profile-settings-header {
     | Opens a rule for selector `.profile-settings-header`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1791 |   padding-bottom: var(--space-3);
     | Sets CSS property `padding-bottom` to `var(--space-3)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1792 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1793 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1794 | .profile-settings-title {
     | Opens a rule for selector `.profile-settings-title`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1795 |   font-size: var(--text-xl);
     | Sets CSS property `font-size` to `var(--text-xl)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1796 |   font-weight: 800;
     | Sets CSS property `font-weight` to `800`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1797 |   color: var(--text);
     | Sets CSS property `color` to `var(--text)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1798 |   margin-bottom: var(--space-1);
     | Sets CSS property `margin-bottom` to `var(--space-1)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1799 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1800 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1801 | .profile-settings-subtitle {
     | Opens a rule for selector `.profile-settings-subtitle`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1802 |   font-size: var(--text-sm);
     | Sets CSS property `font-size` to `var(--text-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1803 |   color: var(--muted);
     | Sets CSS property `color` to `var(--muted)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1804 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1805 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1806 | /* Settings card */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* Settings card */

1807 | .profile-settings-card {
     | Opens a rule for selector `.profile-settings-card`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1808 |   background: var(--card);
     | Sets CSS property `background` to `var(--card)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1809 |   border: 1px solid var(--border);
     | Sets CSS property `border` to `1px solid var(--border)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1810 |   border-radius: var(--radius);
     | Sets CSS property `border-radius` to `var(--radius)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1811 |   padding: var(--space-5);
     | Sets CSS property `padding` to `var(--space-5)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1812 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1813 |   flex-direction: column;
     | Sets CSS property `flex-direction` to `column`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1814 |   gap: var(--space-4);
     | Sets CSS property `gap` to `var(--space-4)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1815 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1816 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1817 | .profile-settings-card-header {
     | Opens a rule for selector `.profile-settings-card-header`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1818 |   border-bottom: 1px solid var(--border);
     | Sets CSS property `border-bottom` to `1px solid var(--border)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1819 |   padding-bottom: var(--space-3);
     | Sets CSS property `padding-bottom` to `var(--space-3)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1820 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1821 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1822 | .profile-settings-card-title {
     | Opens a rule for selector `.profile-settings-card-title`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1823 |   font-size: var(--text-base);
     | Sets CSS property `font-size` to `var(--text-base)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1824 |   font-weight: 700;
     | Sets CSS property `font-weight` to `700`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1825 |   color: var(--text);
     | Sets CSS property `color` to `var(--text)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1826 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1827 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1828 | .profile-settings-card-desc {
     | Opens a rule for selector `.profile-settings-card-desc`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1829 |   font-size: var(--text-xs);
     | Sets CSS property `font-size` to `var(--text-xs)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1830 |   color: var(--muted);
     | Sets CSS property `color` to `var(--muted)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1831 |   margin-top: var(--space-1);
     | Sets CSS property `margin-top` to `var(--space-1)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1832 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1833 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1834 | /* Avatar row */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* Avatar row */

1835 | .profile-avatar-row {
     | Opens a rule for selector `.profile-avatar-row`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1836 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1837 |   align-items: center;
     | Sets CSS property `align-items` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1838 |   gap: var(--space-4);
     | Sets CSS property `gap` to `var(--space-4)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1839 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1840 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1841 | .profile-avatar {
     | Opens a rule for selector `.profile-avatar`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1842 |   width: 60px;
     | Sets CSS property `width` to `60px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1843 |   height: 60px;
     | Sets CSS property `height` to `60px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1844 |   border-radius: 50%;
     | Sets CSS property `border-radius` to `50%`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1845 |   background: var(--brand-gradient);
     | Sets CSS property `background` to `var(--brand-gradient)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1846 |   color: #fff;
     | Sets CSS property `color` to `#fff`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1847 |   font-size: 22px;
     | Sets CSS property `font-size` to `22px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1848 |   font-weight: 800;
     | Sets CSS property `font-weight` to `800`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1849 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1850 |   align-items: center;
     | Sets CSS property `align-items` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1851 |   justify-content: center;
     | Sets CSS property `justify-content` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1852 |   flex-shrink: 0;
     | Sets CSS property `flex-shrink` to `0`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1853 |   box-shadow: 0 4px 16px rgba(99, 102, 241, 0.35);
     | Sets CSS property `box-shadow` to `0 4px 16px rgba(99, 102, 241, 0.35)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1854 |   letter-spacing: 1px;
     | Sets CSS property `letter-spacing` to `1px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1855 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1856 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1857 | .profile-avatar-name {
     | Opens a rule for selector `.profile-avatar-name`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1858 |   font-size: var(--text-base);
     | Sets CSS property `font-size` to `var(--text-base)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1859 |   font-weight: 600;
     | Sets CSS property `font-weight` to `600`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1860 |   color: var(--text);
     | Sets CSS property `color` to `var(--text)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1861 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1862 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1863 | .profile-avatar-email {
     | Opens a rule for selector `.profile-avatar-email`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1864 |   font-size: var(--text-xs);
     | Sets CSS property `font-size` to `var(--text-xs)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1865 |   color: var(--muted);
     | Sets CSS property `color` to `var(--muted)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1866 |   margin-top: 2px;
     | Sets CSS property `margin-top` to `2px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1867 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1868 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1869 | /* Form */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* Form */

1870 | .profile-form {
     | Opens a rule for selector `.profile-form`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1871 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1872 |   flex-direction: column;
     | Sets CSS property `flex-direction` to `column`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1873 |   gap: var(--space-4);
     | Sets CSS property `gap` to `var(--space-4)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1874 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1875 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1876 | .profile-form-grid {
     | Opens a rule for selector `.profile-form-grid`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1877 |   display: grid;
     | Sets CSS property `display` to `grid`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1878 |   grid-template-columns: 1fr 1fr;
     | Sets CSS property `grid-template-columns` to `1fr 1fr`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1879 |   gap: var(--space-4);
     | Sets CSS property `gap` to `var(--space-4)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1880 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1881 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1882 | .profile-form-grid--single {
     | Opens a rule for selector `.profile-form-grid--single`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1883 |   grid-template-columns: 1fr;
     | Sets CSS property `grid-template-columns` to `1fr`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1884 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1885 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1886 | .profile-form-field {
     | Opens a rule for selector `.profile-form-field`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1887 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1888 |   flex-direction: column;
     | Sets CSS property `flex-direction` to `column`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1889 |   gap: var(--space-1);
     | Sets CSS property `gap` to `var(--space-1)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1890 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1891 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1892 | .profile-form-label {
     | Opens a rule for selector `.profile-form-label`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1893 |   font-size: var(--text-xs);
     | Sets CSS property `font-size` to `var(--text-xs)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1894 |   font-weight: 600;
     | Sets CSS property `font-weight` to `600`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1895 |   color: var(--text-soft);
     | Sets CSS property `color` to `var(--text-soft)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1896 |   text-transform: uppercase;
     | Sets CSS property `text-transform` to `uppercase`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1897 |   letter-spacing: 0.6px;
     | Sets CSS property `letter-spacing` to `0.6px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1898 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1899 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1900 | .profile-form-input {
     | Opens a rule for selector `.profile-form-input`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1901 |   width: 100%;
     | Sets CSS property `width` to `100%`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1902 |   padding: 9px 12px;
     | Sets CSS property `padding` to `9px 12px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1903 |   border: 1px solid var(--border);
     | Sets CSS property `border` to `1px solid var(--border)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1904 |   border-radius: var(--radius-sm);
     | Sets CSS property `border-radius` to `var(--radius-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1905 |   background: var(--surface);
     | Sets CSS property `background` to `var(--surface)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1906 |   color: var(--text);
     | Sets CSS property `color` to `var(--text)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1907 |   font-size: var(--text-sm);
     | Sets CSS property `font-size` to `var(--text-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1908 |   font-family: inherit;
     | Sets CSS property `font-family` to `inherit`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1909 |   transition: border-color 0.15s;
     | Sets CSS property `transition` to `border-color 0.15s`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1910 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1911 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1912 | .profile-form-input:focus {
     | Opens a rule for selector `.profile-form-input:focus`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1913 |   outline: none;
     | Sets CSS property `outline` to `none`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1914 |   border-color: var(--border-active);
     | Sets CSS property `border-color` to `var(--border-active)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1915 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1916 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1917 | .profile-form-select {
     | Opens a rule for selector `.profile-form-select`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1918 |   cursor: pointer;
     | Sets CSS property `cursor` to `pointer`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1919 |   appearance: none;
     | Sets CSS property `appearance` to `none`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1920 |   background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8' viewBox='0 0 12 8'%3E%3Cpath d='M1 1l5 5 5-5' stroke='%239898be' stroke-width='1.5' fill='none' stroke-linecap='round'/%3E%3C/svg%3E");
     | Sets CSS property `background-image` to `url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8' viewBox='0 0 12 8'%3E%3Cpath d='M1 1l5 5 5-5' stroke='%239898be' stroke-width='1.5' fill='none' stroke-linecap='round'/%3E%3C/svg%3E")`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1921 |   background-repeat: no-repeat;
     | Sets CSS property `background-repeat` to `no-repeat`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1922 |   background-position: right 12px center;
     | Sets CSS property `background-position` to `right 12px center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1923 |   padding-right: 36px;
     | Sets CSS property `padding-right` to `36px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1924 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1925 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1926 | .profile-form-actions {
     | Opens a rule for selector `.profile-form-actions`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1927 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1928 |   justify-content: flex-end;
     | Sets CSS property `justify-content` to `flex-end`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1929 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1930 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1931 | .profile-save-btn {
     | Opens a rule for selector `.profile-save-btn`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1932 |   padding: 9px 22px;
     | Sets CSS property `padding` to `9px 22px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1933 |   border-radius: var(--radius-sm);
     | Sets CSS property `border-radius` to `var(--radius-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1934 |   border: none;
     | Sets CSS property `border` to `none`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1935 |   background: var(--violet);
     | Sets CSS property `background` to `var(--violet)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1936 |   color: #fff;
     | Sets CSS property `color` to `#fff`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1937 |   font-size: var(--text-sm);
     | Sets CSS property `font-size` to `var(--text-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1938 |   font-weight: 600;
     | Sets CSS property `font-weight` to `600`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1939 |   font-family: inherit;
     | Sets CSS property `font-family` to `inherit`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1940 |   cursor: pointer;
     | Sets CSS property `cursor` to `pointer`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1941 |   transition: opacity 0.15s;
     | Sets CSS property `transition` to `opacity 0.15s`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1942 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1943 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1944 | .profile-save-btn:hover { opacity: 0.88; }
     | CSS line `.profile-save-btn:hover { opacity: 0.88; }`. It is part of the stylesheet the browser applies while painting the React DOM.

1945 | .profile-save-btn:disabled { opacity: 0.5; cursor: not-allowed; }
     | CSS line `.profile-save-btn:disabled { opacity: 0.5; cursor: not-allowed; }`. It is part of the stylesheet the browser applies while painting the React DOM.

1946 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1947 | /* Feedback messages */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* Feedback messages */

1948 | .profile-msg {
     | Opens a rule for selector `.profile-msg`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1949 |   font-size: var(--text-sm);
     | Sets CSS property `font-size` to `var(--text-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1950 |   padding: 9px 12px;
     | Sets CSS property `padding` to `9px 12px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1951 |   border-radius: var(--radius-sm);
     | Sets CSS property `border-radius` to `var(--radius-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1952 |   border: 1px solid transparent;
     | Sets CSS property `border` to `1px solid transparent`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1953 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1954 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1955 | .profile-msg--success {
     | Opens a rule for selector `.profile-msg--success`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1956 |   background: var(--green-dim);
     | Sets CSS property `background` to `var(--green-dim)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1957 |   border-color: rgba(16, 185, 129, 0.3);
     | Sets CSS property `border-color` to `rgba(16, 185, 129, 0.3)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1958 |   color: var(--green);
     | Sets CSS property `color` to `var(--green)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1959 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1960 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1961 | .profile-msg--error {
     | Opens a rule for selector `.profile-msg--error`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1962 |   background: var(--red-dim);
     | Sets CSS property `background` to `var(--red-dim)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1963 |   border-color: rgba(239, 68, 68, 0.3);
     | Sets CSS property `border-color` to `rgba(239, 68, 68, 0.3)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1964 |   color: var(--red);
     | Sets CSS property `color` to `var(--red)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1965 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1966 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1967 | /* Theme Picker */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* Theme Picker */

1968 | .theme-picker {
     | Opens a rule for selector `.theme-picker`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1969 |   display: grid;
     | Sets CSS property `display` to `grid`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1970 |   grid-template-columns: 1fr 1fr;
     | Sets CSS property `grid-template-columns` to `1fr 1fr`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1971 |   gap: var(--space-3);
     | Sets CSS property `gap` to `var(--space-3)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1972 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1973 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1974 | .theme-option {
     | Opens a rule for selector `.theme-option`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1975 |   position: relative;
     | Sets CSS property `position` to `relative`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1976 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1977 |   flex-direction: column;
     | Sets CSS property `flex-direction` to `column`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1978 |   gap: var(--space-3);
     | Sets CSS property `gap` to `var(--space-3)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1979 |   padding: var(--space-4);
     | Sets CSS property `padding` to `var(--space-4)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1980 |   border: 2px solid var(--border);
     | Sets CSS property `border` to `2px solid var(--border)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1981 |   border-radius: var(--radius);
     | Sets CSS property `border-radius` to `var(--radius)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1982 |   background: var(--surface);
     | Sets CSS property `background` to `var(--surface)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1983 |   cursor: pointer;
     | Sets CSS property `cursor` to `pointer`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1984 |   transition: border-color 0.15s, background 0.15s;
     | Sets CSS property `transition` to `border-color 0.15s, background 0.15s`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1985 |   text-align: left;
     | Sets CSS property `text-align` to `left`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1986 |   font-family: inherit;
     | Sets CSS property `font-family` to `inherit`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1987 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

1988 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1989 | .theme-option:hover { border-color: var(--indigo-light); }
     | CSS line `.theme-option:hover { border-color: var(--indigo-light); }`. It is part of the stylesheet the browser applies while painting the React DOM.

1990 | .theme-option.active { border-color: var(--indigo); background: var(--indigo-dim); }
     | CSS line `.theme-option.active { border-color: var(--indigo); background: var(--indigo-dim); }`. It is part of the stylesheet the browser applies while painting the React DOM.

1991 | .theme-option:disabled { opacity: 0.6; cursor: not-allowed; }
     | CSS line `.theme-option:disabled { opacity: 0.6; cursor: not-allowed; }`. It is part of the stylesheet the browser applies while painting the React DOM.

1992 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

1993 | .theme-option-preview {
     | Opens a rule for selector `.theme-option-preview`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

1994 |   width: 100%;
     | Sets CSS property `width` to `100%`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1995 |   height: 72px;
     | Sets CSS property `height` to `72px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1996 |   border-radius: var(--radius-sm);
     | Sets CSS property `border-radius` to `var(--radius-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1997 |   overflow: hidden;
     | Sets CSS property `overflow` to `hidden`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1998 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

1999 |   flex-direction: column;
     | Sets CSS property `flex-direction` to `column`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2000 |   gap: 5px;
     | Sets CSS property `gap` to `5px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2001 |   padding: 8px;
     | Sets CSS property `padding` to `8px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2002 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

2003 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

2004 | .theme-option-preview--dark {
     | Opens a rule for selector `.theme-option-preview--dark`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

2005 |   background: #0d0d18;
     | Sets CSS property `background` to `#0d0d18`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2006 |   border: 1px solid rgba(255, 255, 255, 0.08);
     | Sets CSS property `border` to `1px solid rgba(255, 255, 255, 0.08)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2007 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

2008 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

2009 | .theme-option-preview--light {
     | Opens a rule for selector `.theme-option-preview--light`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

2010 |   background: #f5f4ff;
     | Sets CSS property `background` to `#f5f4ff`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2011 |   border: 1px solid rgba(0, 0, 0, 0.08);
     | Sets CSS property `border` to `1px solid rgba(0, 0, 0, 0.08)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2012 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

2013 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

2014 | .theme-preview-bar {
     | Opens a rule for selector `.theme-preview-bar`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

2015 |   height: 10px;
     | Sets CSS property `height` to `10px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2016 |   border-radius: 4px;
     | Sets CSS property `border-radius` to `4px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2017 |   width: 60%;
     | Sets CSS property `width` to `60%`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2018 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

2019 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

2020 | .theme-option-preview--dark .theme-preview-bar { background: rgba(255,255,255,0.15); }
     | CSS line `.theme-option-preview--dark .theme-preview-bar { background: rgba(255,255,255,0.15); }`. It is part of the stylesheet the browser applies while painting the React DOM.

2021 | .theme-option-preview--light .theme-preview-bar { background: rgba(0,0,0,0.12); }
     | CSS line `.theme-option-preview--light .theme-preview-bar { background: rgba(0,0,0,0.12); }`. It is part of the stylesheet the browser applies while painting the React DOM.

2022 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

2023 | .theme-preview-card {
     | Opens a rule for selector `.theme-preview-card`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

2024 |   height: 18px;
     | Sets CSS property `height` to `18px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2025 |   border-radius: 4px;
     | Sets CSS property `border-radius` to `4px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2026 |   width: 100%;
     | Sets CSS property `width` to `100%`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2027 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

2028 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

2029 | .theme-preview-card--sm { width: 70%; }
     | CSS line `.theme-preview-card--sm { width: 70%; }`. It is part of the stylesheet the browser applies while painting the React DOM.

2030 | .theme-option-preview--dark .theme-preview-card { background: #1c1c2e; }
     | CSS line `.theme-option-preview--dark .theme-preview-card { background: #1c1c2e; }`. It is part of the stylesheet the browser applies while painting the React DOM.

2031 | .theme-option-preview--light .theme-preview-card { background: #ffffff; border: 1px solid rgba(0,0,0,0.06); }
     | CSS line `.theme-option-preview--light .theme-preview-card { background: #ffffff; border: 1px solid rgba(0,0,0,0.06); }`. It is part of the stylesheet the browser applies while painting the React DOM.

2032 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

2033 | .theme-option-label {
     | Opens a rule for selector `.theme-option-label`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

2034 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2035 |   flex-direction: column;
     | Sets CSS property `flex-direction` to `column`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2036 |   gap: 2px;
     | Sets CSS property `gap` to `2px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2037 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

2038 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

2039 | .theme-option-name {
     | Opens a rule for selector `.theme-option-name`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

2040 |   font-size: var(--text-sm);
     | Sets CSS property `font-size` to `var(--text-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2041 |   font-weight: 600;
     | Sets CSS property `font-weight` to `600`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2042 |   color: var(--text);
     | Sets CSS property `color` to `var(--text)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2043 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

2044 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

2045 | .theme-option-desc {
     | Opens a rule for selector `.theme-option-desc`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

2046 |   font-size: var(--text-xs);
     | Sets CSS property `font-size` to `var(--text-xs)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2047 |   color: var(--muted);
     | Sets CSS property `color` to `var(--muted)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2048 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

2049 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

2050 | .theme-option-check {
     | Opens a rule for selector `.theme-option-check`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

2051 |   position: absolute;
     | Sets CSS property `position` to `absolute`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2052 |   top: 10px;
     | Sets CSS property `top` to `10px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2053 |   right: 12px;
     | Sets CSS property `right` to `12px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2054 |   color: var(--indigo-light);
     | Sets CSS property `color` to `var(--indigo-light)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2055 |   font-size: 15px;
     | Sets CSS property `font-size` to `15px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2056 |   font-weight: 700;
     | Sets CSS property `font-weight` to `700`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2057 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

2058 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

2059 | /* ── Profile Settings Responsive ────────────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── Profile Settings Responsive ────────────────────── */

2060 | @media (max-width: 768px) {
     | Opens a media query `@media (max-width: 768px) {`. The rules inside apply only when that screen condition is true, so the same components reflow on a phone.

2061 |   .profile-settings-page {
     | Opens a rule for selector `.profile-settings-page`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

2062 |     padding: var(--space-4) var(--space-4);
     | Sets CSS property `padding` to `var(--space-4) var(--space-4)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2063 |   }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

2064 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

2065 |   .profile-settings-card {
     | Opens a rule for selector `.profile-settings-card`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

2066 |     padding: var(--space-4);
     | Sets CSS property `padding` to `var(--space-4)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2067 |     border-radius: var(--radius-sm);
     | Sets CSS property `border-radius` to `var(--radius-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2068 |   }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

2069 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

2070 |   .profile-form-grid {
     | Opens a rule for selector `.profile-form-grid`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

2071 |     grid-template-columns: 1fr;
     | Sets CSS property `grid-template-columns` to `1fr`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2072 |   }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

2073 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

2074 |   .theme-picker {
     | Opens a rule for selector `.theme-picker`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

2075 |     grid-template-columns: 1fr 1fr;
     | Sets CSS property `grid-template-columns` to `1fr 1fr`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2076 |     gap: var(--space-2);
     | Sets CSS property `gap` to `var(--space-2)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2077 |   }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

2078 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

2079 |   .theme-option {
     | Opens a rule for selector `.theme-option`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

2080 |     padding: var(--space-3);
     | Sets CSS property `padding` to `var(--space-3)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2081 |   }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

2082 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

2083 |   .theme-option-preview {
     | Opens a rule for selector `.theme-option-preview`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

2084 |     height: 56px;
     | Sets CSS property `height` to `56px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2085 |   }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

2086 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

2087 |   .profile-avatar {
     | Opens a rule for selector `.profile-avatar`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

2088 |     width: 48px;
     | Sets CSS property `width` to `48px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2089 |     height: 48px;
     | Sets CSS property `height` to `48px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2090 |     font-size: 18px;
     | Sets CSS property `font-size` to `18px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2091 |   }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

2092 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

2093 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

2094 | @media (max-width: 480px) {
     | Opens a media query `@media (max-width: 480px) {`. The rules inside apply only when that screen condition is true, so the same components reflow on a phone.

2095 |   .profile-settings-page {
     | Opens a rule for selector `.profile-settings-page`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

2096 |     padding: var(--space-3);
     | Sets CSS property `padding` to `var(--space-3)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2097 |   }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

2098 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

2099 |   .theme-picker {
     | Opens a rule for selector `.theme-picker`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

2100 |     grid-template-columns: 1fr;
     | Sets CSS property `grid-template-columns` to `1fr`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2101 |   }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

2102 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

2103 |   .profile-form-actions {
     | Opens a rule for selector `.profile-form-actions`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

2104 |     justify-content: stretch;
     | Sets CSS property `justify-content` to `stretch`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2105 |   }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

2106 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

2107 |   .profile-save-btn {
     | Opens a rule for selector `.profile-save-btn`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

2108 |     width: 100%;
     | Sets CSS property `width` to `100%`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2109 |     text-align: center;
     | Sets CSS property `text-align` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2110 |   }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

2111 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

2112 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

2113 | /* ═══════════════════════════════════════════════════════
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ═══════════════════════════════════════════════════════

2114 |    FOCUS SHIELD — website blocking / whitelisting UI
     | CSS line `FOCUS SHIELD — website blocking / whitelisting UI`. It is part of the stylesheet the browser applies while painting the React DOM.

2115 |    ═══════════════════════════════════════════════════════ */
     | CSS comment, ignored by the browser. It labels the next group of rules: ═══════════════════════════════════════════════════════ */

2116 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

2117 | /* Toggle switch — shared by master toggle + per-row enable switch */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* Toggle switch — shared by master toggle + per-row enable switch */

2118 | .fs-toggle {
     | Opens a rule for selector `.fs-toggle`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

2119 |   width: 44px;
     | Sets CSS property `width` to `44px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2120 |   height: 24px;
     | Sets CSS property `height` to `24px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2121 |   min-width: 44px;
     | Sets CSS property `min-width` to `44px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2122 |   border-radius: 12px;
     | Sets CSS property `border-radius` to `12px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2123 |   border: none;
     | Sets CSS property `border` to `none`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2124 |   cursor: pointer;
     | Sets CSS property `cursor` to `pointer`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2125 |   background: var(--border);
     | Sets CSS property `background` to `var(--border)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2126 |   position: relative;
     | Sets CSS property `position` to `relative`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2127 |   transition: background 0.2s;
     | Sets CSS property `transition` to `background 0.2s`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2128 |   flex-shrink: 0;
     | Sets CSS property `flex-shrink` to `0`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2129 |   padding: 0;
     | Sets CSS property `padding` to `0`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2130 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

2131 | .fs-toggle[data-checked] { background: var(--indigo); }
     | CSS line `.fs-toggle[data-checked] { background: var(--indigo); }`. It is part of the stylesheet the browser applies while painting the React DOM.

2132 | .fs-toggle:disabled { opacity: 0.5; cursor: not-allowed; }
     | CSS line `.fs-toggle:disabled { opacity: 0.5; cursor: not-allowed; }`. It is part of the stylesheet the browser applies while painting the React DOM.

2133 | .fs-toggle-knob {
     | Opens a rule for selector `.fs-toggle-knob`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

2134 |   position: absolute;
     | Sets CSS property `position` to `absolute`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2135 |   top: 3px;
     | Sets CSS property `top` to `3px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2136 |   left: 3px;
     | Sets CSS property `left` to `3px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2137 |   width: 18px;
     | Sets CSS property `width` to `18px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2138 |   height: 18px;
     | Sets CSS property `height` to `18px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2139 |   border-radius: 50%;
     | Sets CSS property `border-radius` to `50%`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2140 |   background: #fff;
     | Sets CSS property `background` to `#fff`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2141 |   transition: left 0.2s;
     | Sets CSS property `transition` to `left 0.2s`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2142 |   display: block;
     | Sets CSS property `display` to `block`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2143 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

2144 | .fs-toggle[data-checked] .fs-toggle-knob { left: 23px; }
     | CSS line `.fs-toggle[data-checked] .fs-toggle-knob { left: 23px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

2145 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

2146 | /* Status card + pill (dashboard card, session panel, page header) */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* Status card + pill (dashboard card, session panel, page header) */

2147 | .fs-status-card { display: flex; flex-direction: column; }
     | CSS line `.fs-status-card { display: flex; flex-direction: column; }`. It is part of the stylesheet the browser applies while painting the React DOM.

2148 | .fs-status-card-header { display: flex; align-items: center; justify-content: space-between; gap: 10px; flex-wrap: wrap; }
     | CSS line `.fs-status-card-header { display: flex; align-items: center; justify-content: space-between; gap: 10px; flex-wrap: wrap; }`. It is part of the stylesheet the browser applies while painting the React DOM.

2149 | .fs-status-pill {
     | Opens a rule for selector `.fs-status-pill`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

2150 |   display: inline-flex;
     | Sets CSS property `display` to `inline-flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2151 |   align-items: center;
     | Sets CSS property `align-items` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2152 |   gap: 6px;
     | Sets CSS property `gap` to `6px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2153 |   padding: 4px 10px;
     | Sets CSS property `padding` to `4px 10px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2154 |   border-radius: 20px;
     | Sets CSS property `border-radius` to `20px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2155 |   font-size: var(--text-xs);
     | Sets CSS property `font-size` to `var(--text-xs)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2156 |   font-weight: 700;
     | Sets CSS property `font-weight` to `700`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2157 |   white-space: nowrap;
     | Sets CSS property `white-space` to `nowrap`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2158 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

2159 | .fs-status-pill--off { background: var(--border); color: var(--muted); }
     | CSS line `.fs-status-pill--off { background: var(--border); color: var(--muted); }`. It is part of the stylesheet the browser applies while painting the React DOM.

2160 | .fs-status-pill--armed { background: var(--indigo-dim); color: var(--indigo-light); }
     | CSS line `.fs-status-pill--armed { background: var(--indigo-dim); color: var(--indigo-light); }`. It is part of the stylesheet the browser applies while painting the React DOM.

2161 | .fs-status-pill--active { background: var(--green-dim); color: var(--green); }
     | CSS line `.fs-status-pill--active { background: var(--green-dim); color: var(--green); }`. It is part of the stylesheet the browser applies while painting the React DOM.

2162 | .fs-status-pill--paused { background: var(--amber-dim); color: var(--amber); }
     | CSS line `.fs-status-pill--paused { background: var(--amber-dim); color: var(--amber); }`. It is part of the stylesheet the browser applies while painting the React DOM.

2163 | .fs-status-dot { width: 7px; height: 7px; border-radius: 50%; background: currentColor; flex-shrink: 0; }
     | CSS line `.fs-status-dot { width: 7px; height: 7px; border-radius: 50%; background: currentColor; flex-shrink: 0; }`. It is part of the stylesheet the browser applies while painting the React DOM.

2164 | .fs-dashboard-counts { display: flex; gap: var(--space-5); }
     | CSS line `.fs-dashboard-counts { display: flex; gap: var(--space-5); }`. It is part of the stylesheet the browser applies while painting the React DOM.

2165 | .fs-session-site-list {
     | Opens a rule for selector `.fs-session-site-list`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

2166 |   list-style: none;
     | Sets CSS property `list-style` to `none`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2167 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2168 |   flex-direction: column;
     | Sets CSS property `flex-direction` to `column`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2169 |   gap: 4px;
     | Sets CSS property `gap` to `4px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2170 |   font-size: var(--text-sm);
     | Sets CSS property `font-size` to `var(--text-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2171 |   color: var(--text-soft);
     | Sets CSS property `color` to `var(--text-soft)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2172 |   margin-bottom: 12px;
     | Sets CSS property `margin-bottom` to `12px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2173 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

2174 | .fs-session-site-list li::before { content: "🚫 "; }
     | CSS line `.fs-session-site-list li::before { content: "🚫 "; }`. It is part of the stylesheet the browser applies while painting the React DOM.

2175 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

2176 | /* Pause control */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* Pause control */

2177 | .fs-pause-banner {
     | Opens a rule for selector `.fs-pause-banner`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

2178 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2179 |   align-items: center;
     | Sets CSS property `align-items` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2180 |   justify-content: space-between;
     | Sets CSS property `justify-content` to `space-between`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2181 |   gap: 10px;
     | Sets CSS property `gap` to `10px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2182 |   flex-wrap: wrap;
     | Sets CSS property `flex-wrap` to `wrap`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2183 |   padding: 10px 14px;
     | Sets CSS property `padding` to `10px 14px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2184 |   border-radius: var(--radius-sm);
     | Sets CSS property `border-radius` to `var(--radius-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2185 |   background: var(--amber-dim);
     | Sets CSS property `background` to `var(--amber-dim)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2186 |   border: 1px solid rgba(245, 158, 11, 0.25);
     | Sets CSS property `border` to `1px solid rgba(245, 158, 11, 0.25)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2187 |   color: var(--text);
     | Sets CSS property `color` to `var(--text)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2188 |   font-size: var(--text-sm);
     | Sets CSS property `font-size` to `var(--text-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2189 |   font-weight: 600;
     | Sets CSS property `font-weight` to `600`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2190 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

2191 | .fs-pause-row { display: flex; gap: 8px; flex-wrap: wrap; }
     | CSS line `.fs-pause-row { display: flex; gap: 8px; flex-wrap: wrap; }`. It is part of the stylesheet the browser applies while painting the React DOM.

2192 | .fs-pause-custom { display: flex; align-items: center; gap: 8px; margin-top: 10px; flex-wrap: wrap; }
     | CSS line `.fs-pause-custom { display: flex; align-items: center; gap: 8px; margin-top: 10px; flex-wrap: wrap; }`. It is part of the stylesheet the browser applies while painting the React DOM.

2193 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

2194 | /* Page header with autosave indicator */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* Page header with autosave indicator */

2195 | .fs-page-header { display: flex; align-items: flex-start; justify-content: space-between; gap: 12px; flex-wrap: wrap; }
     | CSS line `.fs-page-header { display: flex; align-items: flex-start; justify-content: space-between; gap: 12px; flex-wrap: wrap; }`. It is part of the stylesheet the browser applies while painting the React DOM.

2196 | .fs-save-indicator { font-size: var(--text-xs); color: var(--muted); white-space: nowrap; padding-top: 4px; }
     | CSS line `.fs-save-indicator { font-size: var(--text-xs); color: var(--muted); white-space: nowrap; padding-top: 4px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

2197 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

2198 | /* Section header with inline "Add website" action */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* Section header with inline "Add website" action */

2199 | .fs-section-header { display: flex; align-items: flex-start; justify-content: space-between; gap: 12px; flex-wrap: wrap; }
     | CSS line `.fs-section-header { display: flex; align-items: flex-start; justify-content: space-between; gap: 12px; flex-wrap: wrap; }`. It is part of the stylesheet the browser applies while painting the React DOM.

2200 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

2201 | /* Search + bulk toolbar */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* Search + bulk toolbar */

2202 | .fs-toolbar { display: flex; align-items: center; justify-content: space-between; gap: 10px; flex-wrap: wrap; }
     | CSS line `.fs-toolbar { display: flex; align-items: center; justify-content: space-between; gap: 10px; flex-wrap: wrap; }`. It is part of the stylesheet the browser applies while painting the React DOM.

2203 | .fs-bulk-toolbar { display: flex; align-items: center; gap: 6px; flex-wrap: wrap; }
     | CSS line `.fs-bulk-toolbar { display: flex; align-items: center; gap: 6px; flex-wrap: wrap; }`. It is part of the stylesheet the browser applies while painting the React DOM.

2204 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

2205 | /* Website rows */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* Website rows */

2206 | .fs-row-list { display: flex; flex-direction: column; gap: 6px; }
     | CSS line `.fs-row-list { display: flex; flex-direction: column; gap: 6px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

2207 | .fs-row {
     | Opens a rule for selector `.fs-row`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

2208 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2209 |   align-items: center;
     | Sets CSS property `align-items` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2210 |   gap: 12px;
     | Sets CSS property `gap` to `12px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2211 |   padding: 10px 12px;
     | Sets CSS property `padding` to `10px 12px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2212 |   border: 1px solid var(--border);
     | Sets CSS property `border` to `1px solid var(--border)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2213 |   border-radius: var(--radius-sm);
     | Sets CSS property `border-radius` to `var(--radius-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2214 |   background: var(--surface);
     | Sets CSS property `background` to `var(--surface)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2215 |   flex-wrap: wrap;
     | Sets CSS property `flex-wrap` to `wrap`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2216 |   transition: border-color 0.15s;
     | Sets CSS property `transition` to `border-color 0.15s`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2217 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

2218 | .fs-row--selected { border-color: var(--border-active); background: var(--indigo-dim); }
     | CSS line `.fs-row--selected { border-color: var(--border-active); background: var(--indigo-dim); }`. It is part of the stylesheet the browser applies while painting the React DOM.

2219 | .fs-row-checkbox { width: 18px; height: 18px; flex-shrink: 0; accent-color: var(--indigo); cursor: pointer; }
     | CSS line `.fs-row-checkbox { width: 18px; height: 18px; flex-shrink: 0; accent-color: var(--indigo); cursor: pointer; }`. It is part of the stylesheet the browser applies while painting the React DOM.

2220 | .fs-row-main { flex: 1; min-width: 160px; display: flex; flex-direction: column; gap: 4px; }
     | CSS line `.fs-row-main { flex: 1; min-width: 160px; display: flex; flex-direction: column; gap: 4px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

2221 | .fs-row-domain { font-size: var(--text-sm); color: var(--text); font-weight: 600; word-break: break-all; display: flex; flex-direction: column; }
     | CSS line `.fs-row-domain { font-size: var(--text-sm); color: var(--text); font-weight: 600; word-break: break-all; display: flex; flex-direction: column; }`. It is part of the stylesheet the browser applies while painting the React DOM.

2222 | .fs-row-domain-sub { font-size: var(--text-xs); color: var(--muted); font-weight: 400; }
     | CSS line `.fs-row-domain-sub { font-size: var(--text-xs); color: var(--muted); font-weight: 400; }`. It is part of the stylesheet the browser applies while painting the React DOM.

2223 | .fs-row-meta { display: flex; align-items: center; gap: 6px; flex-wrap: wrap; }
     | CSS line `.fs-row-meta { display: flex; align-items: center; gap: 6px; flex-wrap: wrap; }`. It is part of the stylesheet the browser applies while painting the React DOM.

2224 | .fs-row-notes { font-style: italic; }
     | CSS line `.fs-row-notes { font-style: italic; }`. It is part of the stylesheet the browser applies while painting the React DOM.

2225 | .fs-row-actions { display: flex; align-items: center; gap: 10px; flex-shrink: 0; margin-left: auto; }
     | CSS line `.fs-row-actions { display: flex; align-items: center; gap: 10px; flex-shrink: 0; margin-left: auto; }`. It is part of the stylesheet the browser applies while painting the React DOM.

2226 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

2227 | /* Three-dot row menu */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* Three-dot row menu */

2228 | .fs-row-menu { position: relative; }
     | CSS line `.fs-row-menu { position: relative; }`. It is part of the stylesheet the browser applies while painting the React DOM.

2229 | .fs-row-menu-btn {
     | Opens a rule for selector `.fs-row-menu-btn`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

2230 |   width: 32px;
     | Sets CSS property `width` to `32px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2231 |   height: 32px;
     | Sets CSS property `height` to `32px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2232 |   border-radius: var(--radius-sm);
     | Sets CSS property `border-radius` to `var(--radius-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2233 |   border: 1px solid transparent;
     | Sets CSS property `border` to `1px solid transparent`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2234 |   background: transparent;
     | Sets CSS property `background` to `transparent`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2235 |   color: var(--muted);
     | Sets CSS property `color` to `var(--muted)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2236 |   cursor: pointer;
     | Sets CSS property `cursor` to `pointer`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2237 |   font-size: 16px;
     | Sets CSS property `font-size` to `16px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2238 |   line-height: 1;
     | Sets CSS property `line-height` to `1`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2239 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

2240 | .fs-row-menu-btn:hover { background: var(--border); color: var(--text); }
     | CSS line `.fs-row-menu-btn:hover { background: var(--border); color: var(--text); }`. It is part of the stylesheet the browser applies while painting the React DOM.

2241 | .fs-row-menu-list {
     | Opens a rule for selector `.fs-row-menu-list`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

2242 |   position: absolute;
     | Sets CSS property `position` to `absolute`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2243 |   right: 0;
     | Sets CSS property `right` to `0`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2244 |   top: 36px;
     | Sets CSS property `top` to `36px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2245 |   min-width: 140px;
     | Sets CSS property `min-width` to `140px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2246 |   background: var(--card);
     | Sets CSS property `background` to `var(--card)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2247 |   border: 1px solid var(--border);
     | Sets CSS property `border` to `1px solid var(--border)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2248 |   border-radius: var(--radius-sm);
     | Sets CSS property `border-radius` to `var(--radius-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2249 |   box-shadow: var(--shadow);
     | Sets CSS property `box-shadow` to `var(--shadow)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2250 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2251 |   flex-direction: column;
     | Sets CSS property `flex-direction` to `column`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2252 |   padding: 4px;
     | Sets CSS property `padding` to `4px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2253 |   z-index: 20;
     | Sets CSS property `z-index` to `20`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2254 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

2255 | .fs-row-menu-list button {
     | Opens a rule for selector `.fs-row-menu-list button`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

2256 |   text-align: left;
     | Sets CSS property `text-align` to `left`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2257 |   padding: 8px 10px;
     | Sets CSS property `padding` to `8px 10px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2258 |   background: none;
     | Sets CSS property `background` to `none`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2259 |   border: none;
     | Sets CSS property `border` to `none`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2260 |   border-radius: 6px;
     | Sets CSS property `border-radius` to `6px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2261 |   color: var(--text-soft);
     | Sets CSS property `color` to `var(--text-soft)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2262 |   font-size: var(--text-sm);
     | Sets CSS property `font-size` to `var(--text-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2263 |   cursor: pointer;
     | Sets CSS property `cursor` to `pointer`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2264 |   font-family: inherit;
     | Sets CSS property `font-family` to `inherit`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2265 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

2266 | .fs-row-menu-list button:hover { background: var(--indigo-dim); color: var(--indigo-light); }
     | CSS line `.fs-row-menu-list button:hover { background: var(--indigo-dim); color: var(--indigo-light); }`. It is part of the stylesheet the browser applies while painting the React DOM.

2267 | .fs-row-menu-danger { color: var(--red) !important; }
     | CSS line `.fs-row-menu-danger { color: var(--red) !important; }`. It is part of the stylesheet the browser applies while painting the React DOM.

2268 | .fs-row-menu-danger:hover { background: var(--red-dim) !important; color: var(--red) !important; }
     | CSS line `.fs-row-menu-danger:hover { background: var(--red-dim) !important; color: var(--red) !important; }`. It is part of the stylesheet the browser applies while painting the React DOM.

2269 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

2270 | /* Blocked-apps rows (simple list, no domain validation) */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* Blocked-apps rows (simple list, no domain validation) */

2271 | .fs-app-row {
     | Opens a rule for selector `.fs-app-row`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

2272 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2273 |   align-items: center;
     | Sets CSS property `align-items` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2274 |   gap: 8px;
     | Sets CSS property `gap` to `8px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2275 |   background: var(--surface);
     | Sets CSS property `background` to `var(--surface)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2276 |   border-radius: var(--radius-sm);
     | Sets CSS property `border-radius` to `var(--radius-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2277 |   padding: 6px 10px;
     | Sets CSS property `padding` to `6px 10px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2278 |   border: 1px solid var(--border);
     | Sets CSS property `border` to `1px solid var(--border)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2279 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

2280 | .fs-app-row .fs-row-domain { flex: 1; font-weight: 400; }
     | CSS line `.fs-app-row .fs-row-domain { flex: 1; font-weight: 400; }`. It is part of the stylesheet the browser applies while painting the React DOM.

2281 | .fs-app-remove { background: none; border: none; color: var(--muted); cursor: pointer; font-size: 16px; line-height: 1; padding: 0 2px; }
     | CSS line `.fs-app-remove { background: none; border: none; color: var(--muted); cursor: pointer; font-size: 16px; line-height: 1; padding: 0 2px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

2282 | .fs-app-remove:hover { color: var(--red); }
     | CSS line `.fs-app-remove:hover { color: var(--red); }`. It is part of the stylesheet the browser applies while painting the React DOM.

2283 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

2284 | /* Schedule day pills */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* Schedule day pills */

2285 | .fs-day-pill {
     | Opens a rule for selector `.fs-day-pill`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

2286 |   padding: 4px 10px;
     | Sets CSS property `padding` to `4px 10px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2287 |   min-height: 30px;
     | Sets CSS property `min-height` to `30px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2288 |   border-radius: var(--radius-sm);
     | Sets CSS property `border-radius` to `var(--radius-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2289 |   border: 1px solid var(--border);
     | Sets CSS property `border` to `1px solid var(--border)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2290 |   background: transparent;
     | Sets CSS property `background` to `transparent`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2291 |   color: var(--muted);
     | Sets CSS property `color` to `var(--muted)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2292 |   font-size: var(--text-xs);
     | Sets CSS property `font-size` to `var(--text-xs)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2293 |   font-weight: 400;
     | Sets CSS property `font-weight` to `400`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2294 |   cursor: pointer;
     | Sets CSS property `cursor` to `pointer`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2295 |   transition: all 0.15s;
     | Sets CSS property `transition` to `all 0.15s`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2296 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

2297 | .fs-day-pill--active { border-color: var(--indigo); background: var(--indigo-dim); color: var(--indigo-light); font-weight: 600; }
     | CSS line `.fs-day-pill--active { border-color: var(--indigo); background: var(--indigo-dim); color: var(--indigo-light); font-weight: 600; }`. It is part of the stylesheet the browser applies while painting the React DOM.

2298 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

2299 | .fs-notice {
     | Opens a rule for selector `.fs-notice`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

2300 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2301 |   align-items: flex-start;
     | Sets CSS property `align-items` to `flex-start`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2302 |   gap: 8px;
     | Sets CSS property `gap` to `8px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2303 |   padding: 8px 12px;
     | Sets CSS property `padding` to `8px 12px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2304 |   background: var(--amber-dim);
     | Sets CSS property `background` to `var(--amber-dim)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2305 |   border-radius: var(--radius-sm);
     | Sets CSS property `border-radius` to `var(--radius-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2306 |   border: 1px solid var(--amber);
     | Sets CSS property `border` to `1px solid var(--amber)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2307 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

2308 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

2309 | /* Focus Shield quick-access row on Profile & Settings */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* Focus Shield quick-access row on Profile & Settings */

2310 | .fs-quick-link {
     | Opens a rule for selector `.fs-quick-link`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

2311 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2312 |   align-items: center;
     | Sets CSS property `align-items` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2313 |   gap: 12px;
     | Sets CSS property `gap` to `12px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2314 |   text-decoration: none;
     | Sets CSS property `text-decoration` to `none`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2315 |   cursor: pointer;
     | Sets CSS property `cursor` to `pointer`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2316 |   transition: border-color 0.15s;
     | Sets CSS property `transition` to `border-color 0.15s`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2317 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

2318 | .fs-quick-link:hover { border-color: var(--border-active); }
     | CSS line `.fs-quick-link:hover { border-color: var(--border-active); }`. It is part of the stylesheet the browser applies while painting the React DOM.

2319 | .fs-quick-link-icon { font-size: 24px; flex-shrink: 0; }
     | CSS line `.fs-quick-link-icon { font-size: 24px; flex-shrink: 0; }`. It is part of the stylesheet the browser applies while painting the React DOM.

2320 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

2321 | /* Sheet (bottom sheet on mobile, centered modal on desktop) */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* Sheet (bottom sheet on mobile, centered modal on desktop) */

2322 | .fs-sheet-overlay {
     | Opens a rule for selector `.fs-sheet-overlay`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

2323 |   position: fixed;
     | Sets CSS property `position` to `fixed`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2324 |   inset: 0;
     | Sets CSS property `inset` to `0`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2325 |   background: rgba(0, 0, 0, 0.5);
     | Sets CSS property `background` to `rgba(0, 0, 0, 0.5)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2326 |   backdrop-filter: blur(2px);
     | Sets CSS property `backdrop-filter` to `blur(2px)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2327 |   z-index: 199;
     | Sets CSS property `z-index` to `199`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2328 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

2329 | .fs-sheet {
     | Opens a rule for selector `.fs-sheet`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

2330 |   position: fixed;
     | Sets CSS property `position` to `fixed`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2331 |   left: 0;
     | Sets CSS property `left` to `0`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2332 |   right: 0;
     | Sets CSS property `right` to `0`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2333 |   bottom: 0;
     | Sets CSS property `bottom` to `0`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2334 |   background: var(--surface);
     | Sets CSS property `background` to `var(--surface)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2335 |   border-radius: 20px 20px 0 0;
     | Sets CSS property `border-radius` to `20px 20px 0 0`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2336 |   border-top: 1px solid var(--border);
     | Sets CSS property `border-top` to `1px solid var(--border)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2337 |   z-index: 200;
     | Sets CSS property `z-index` to `200`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2338 |   max-height: 85vh;
     | Sets CSS property `max-height` to `85vh`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2339 |   overflow-y: auto;
     | Sets CSS property `overflow-y` to `auto`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2340 |   padding: 0 var(--space-4) calc(env(safe-area-inset-bottom, 0px) + var(--space-5));
     | Sets CSS property `padding` to `0 var(--space-4) calc(env(safe-area-inset-bottom, 0px) + var(--space-5))`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2341 |   box-shadow: 0 -4px 24px rgba(0, 0, 0, 0.3);
     | Sets CSS property `box-shadow` to `0 -4px 24px rgba(0, 0, 0, 0.3)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2342 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

2343 | .fs-sheet-header { display: flex; align-items: center; justify-content: space-between; padding: 4px 0 12px; }
     | CSS line `.fs-sheet-header { display: flex; align-items: center; justify-content: space-between; padding: 4px 0 12px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

2344 | .fs-sheet-title { font-size: var(--text-lg); font-weight: 700; color: var(--text); }
     | CSS line `.fs-sheet-title { font-size: var(--text-lg); font-weight: 700; color: var(--text); }`. It is part of the stylesheet the browser applies while painting the React DOM.

2345 | .fs-sheet-close {
     | Opens a rule for selector `.fs-sheet-close`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

2346 |   width: 32px;
     | Sets CSS property `width` to `32px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2347 |   height: 32px;
     | Sets CSS property `height` to `32px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2348 |   border-radius: var(--radius-sm);
     | Sets CSS property `border-radius` to `var(--radius-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2349 |   border: none;
     | Sets CSS property `border` to `none`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2350 |   background: transparent;
     | Sets CSS property `background` to `transparent`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2351 |   color: var(--muted);
     | Sets CSS property `color` to `var(--muted)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2352 |   font-size: 22px;
     | Sets CSS property `font-size` to `22px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2353 |   line-height: 1;
     | Sets CSS property `line-height` to `1`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2354 |   cursor: pointer;
     | Sets CSS property `cursor` to `pointer`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2355 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

2356 | .fs-sheet-close:hover { background: var(--border); color: var(--text); }
     | CSS line `.fs-sheet-close:hover { background: var(--border); color: var(--text); }`. It is part of the stylesheet the browser applies while painting the React DOM.

2357 | .fs-sheet-body { display: flex; flex-direction: column; }
     | CSS line `.fs-sheet-body { display: flex; flex-direction: column; }`. It is part of the stylesheet the browser applies while painting the React DOM.

2358 | .fs-sheet-divider { height: 1px; background: var(--border); margin: 16px 0; }
     | CSS line `.fs-sheet-divider { height: 1px; background: var(--border); margin: 16px 0; }`. It is part of the stylesheet the browser applies while painting the React DOM.

2359 | .fs-sheet-footer { position: sticky; bottom: 0; background: var(--surface); padding: 14px 0 4px; margin-top: 10px; }
     | CSS line `.fs-sheet-footer { position: sticky; bottom: 0; background: var(--surface); padding: 14px 0 4px; margin-top: 10px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

2360 | .fs-sheet-footer--split { display: flex; gap: 10px; justify-content: flex-end; }
     | CSS line `.fs-sheet-footer--split { display: flex; gap: 10px; justify-content: flex-end; }`. It is part of the stylesheet the browser applies while painting the React DOM.

2361 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

2362 | @media (min-width: 769px) {
     | Opens a media query `@media (min-width: 769px) {`. The rules inside apply only when that screen condition is true, so the same components reflow on a phone.

2363 |   .fs-sheet {
     | Opens a rule for selector `.fs-sheet`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

2364 |     position: fixed;
     | Sets CSS property `position` to `fixed`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2365 |     top: 50%;
     | Sets CSS property `top` to `50%`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2366 |     left: 50%;
     | Sets CSS property `left` to `50%`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2367 |     right: auto;
     | Sets CSS property `right` to `auto`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2368 |     bottom: auto;
     | Sets CSS property `bottom` to `auto`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2369 |     transform: translate(-50%, -50%);
     | Sets CSS property `transform` to `translate(-50%, -50%)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2370 |     width: calc(100% - 2 * var(--space-5));
     | Sets CSS property `width` to `calc(100% - 2 * var(--space-5))`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2371 |     max-width: 460px;
     | Sets CSS property `max-width` to `460px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2372 |     border-radius: var(--radius-lg);
     | Sets CSS property `border-radius` to `var(--radius-lg)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2373 |     border: 1px solid var(--border);
     | Sets CSS property `border` to `1px solid var(--border)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2374 |     max-height: 80vh;
     | Sets CSS property `max-height` to `80vh`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2375 |     padding: var(--space-5);
     | Sets CSS property `padding` to `var(--space-5)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2376 |     box-shadow: var(--shadow);
     | Sets CSS property `box-shadow` to `var(--shadow)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2377 |   }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

2378 |   .fs-sheet .bottom-sheet-handle { display: none; }
     | CSS line `.fs-sheet .bottom-sheet-handle { display: none; }`. It is part of the stylesheet the browser applies while painting the React DOM.

2379 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

2380 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

2381 | /* Popular website chips */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* Popular website chips */

2382 | .fs-popular-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; }
     | CSS line `.fs-popular-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

2383 | .fs-popular-chip {
     | Opens a rule for selector `.fs-popular-chip`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

2384 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2385 |   flex-direction: column;
     | Sets CSS property `flex-direction` to `column`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2386 |   align-items: center;
     | Sets CSS property `align-items` to `center`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2387 |   gap: 4px;
     | Sets CSS property `gap` to `4px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2388 |   padding: 12px 8px;
     | Sets CSS property `padding` to `12px 8px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2389 |   min-height: 44px;
     | Sets CSS property `min-height` to `44px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2390 |   border-radius: var(--radius-sm);
     | Sets CSS property `border-radius` to `var(--radius-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2391 |   border: 1px solid var(--border);
     | Sets CSS property `border` to `1px solid var(--border)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2392 |   background: var(--surface);
     | Sets CSS property `background` to `var(--surface)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2393 |   cursor: pointer;
     | Sets CSS property `cursor` to `pointer`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2394 |   transition: all 0.15s;
     | Sets CSS property `transition` to `all 0.15s`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2395 |   font-family: inherit;
     | Sets CSS property `font-family` to `inherit`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2396 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

2397 | .fs-popular-chip:hover:not(:disabled) { border-color: var(--border-active); background: var(--indigo-dim); }
     | CSS line `.fs-popular-chip:hover:not(:disabled) { border-color: var(--border-active); background: var(--indigo-dim); }`. It is part of the stylesheet the browser applies while painting the React DOM.

2398 | .fs-popular-chip:disabled { cursor: default; opacity: 0.7; }
     | CSS line `.fs-popular-chip:disabled { cursor: default; opacity: 0.7; }`. It is part of the stylesheet the browser applies while painting the React DOM.

2399 | .fs-popular-chip--added { border-color: var(--green); background: var(--green-dim); }
     | CSS line `.fs-popular-chip--added { border-color: var(--green); background: var(--green-dim); }`. It is part of the stylesheet the browser applies while painting the React DOM.

2400 | .fs-popular-emoji { font-size: 20px; }
     | CSS line `.fs-popular-emoji { font-size: 20px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

2401 | .fs-popular-label { font-size: var(--text-xs); font-weight: 600; color: var(--text); text-align: center; }
     | CSS line `.fs-popular-label { font-size: var(--text-xs); font-weight: 600; color: var(--text); text-align: center; }`. It is part of the stylesheet the browser applies while painting the React DOM.

2402 | .fs-popular-status { font-size: 10px; color: var(--muted); }
     | CSS line `.fs-popular-status { font-size: 10px; color: var(--muted); }`. It is part of the stylesheet the browser applies while painting the React DOM.

2403 | .fs-popular-chip--added .fs-popular-status { color: var(--green); }
     | CSS line `.fs-popular-chip--added .fs-popular-status { color: var(--green); }`. It is part of the stylesheet the browser applies while painting the React DOM.

2404 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

2405 | .fs-custom-domain-row { display: flex; gap: 8px; }
     | CSS line `.fs-custom-domain-row { display: flex; gap: 8px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

2406 | .fs-custom-domain-row .profile-form-input { flex: 1; }
     | CSS line `.fs-custom-domain-row .profile-form-input { flex: 1; }`. It is part of the stylesheet the browser applies while painting the React DOM.

2407 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

2408 | /* Smart preset cards */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* Smart preset cards */

2409 | .fs-preset-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)); gap: 10px; }
     | CSS line `.fs-preset-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)); gap: 10px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

2410 | .fs-preset-card {
     | Opens a rule for selector `.fs-preset-card`. Every property until the matching `}` applies to elements that match that selector. Changing data-theme or a class on the element turns these on or off.

2411 |   display: flex;
     | Sets CSS property `display` to `flex`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2412 |   flex-direction: column;
     | Sets CSS property `flex-direction` to `column`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2413 |   gap: 4px;
     | Sets CSS property `gap` to `4px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2414 |   align-items: flex-start;
     | Sets CSS property `align-items` to `flex-start`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2415 |   text-align: left;
     | Sets CSS property `text-align` to `left`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2416 |   padding: 14px;
     | Sets CSS property `padding` to `14px`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2417 |   border-radius: var(--radius-sm);
     | Sets CSS property `border-radius` to `var(--radius-sm)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2418 |   border: 1px solid var(--border);
     | Sets CSS property `border` to `1px solid var(--border)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2419 |   background: var(--surface);
     | Sets CSS property `background` to `var(--surface)`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2420 |   cursor: pointer;
     | Sets CSS property `cursor` to `pointer`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2421 |   transition: all 0.15s;
     | Sets CSS property `transition` to `all 0.15s`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2422 |   font-family: inherit;
     | Sets CSS property `font-family` to `inherit`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2423 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

2424 | .fs-preset-card:hover { border-color: var(--border-active); background: var(--card-hover); }
     | CSS line `.fs-preset-card:hover { border-color: var(--border-active); background: var(--card-hover); }`. It is part of the stylesheet the browser applies while painting the React DOM.

2425 | .fs-preset-emoji { font-size: 22px; }
     | CSS line `.fs-preset-emoji { font-size: 22px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

2426 | .fs-preset-label { font-size: var(--text-sm); font-weight: 700; color: var(--text); }
     | CSS line `.fs-preset-label { font-size: var(--text-sm); font-weight: 700; color: var(--text); }`. It is part of the stylesheet the browser applies while painting the React DOM.

2427 | .fs-preset-desc { font-size: var(--text-xs); color: var(--muted); line-height: 1.4; }
     | CSS line `.fs-preset-desc { font-size: var(--text-xs); color: var(--muted); line-height: 1.4; }`. It is part of the stylesheet the browser applies while painting the React DOM.

2428 | .fs-preset-status { font-size: 10px; font-weight: 600; color: var(--indigo-light); margin-top: 4px; }
     | CSS line `.fs-preset-status { font-size: 10px; font-weight: 600; color: var(--indigo-light); margin-top: 4px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

2429 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

2430 | @media (max-width: 640px) {
     | Opens a media query `@media (max-width: 640px) {`. The rules inside apply only when that screen condition is true, so the same components reflow on a phone.

2431 |   .fs-popular-grid { grid-template-columns: repeat(2, 1fr); }
     | CSS line `.fs-popular-grid { grid-template-columns: repeat(2, 1fr); }`. It is part of the stylesheet the browser applies while painting the React DOM.

2432 |   .fs-row { gap: 8px; }
     | CSS line `.fs-row { gap: 8px; }`. It is part of the stylesheet the browser applies while painting the React DOM.

2433 |   .fs-row-actions { margin-left: 0; width: 100%; justify-content: space-between; }
     | CSS line `.fs-row-actions { margin-left: 0; width: 100%; justify-content: space-between; }`. It is part of the stylesheet the browser applies while painting the React DOM.

2434 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

2435 | 
     | Blank line in styles.css. It does not create a rule. It separates groups of rules.

2436 | /* ── Reduced motion ─────────────────────────────────── */
     | CSS comment, ignored by the browser. It labels the next group of rules: /* ── Reduced motion ─────────────────────────────────── */

2437 | @media (prefers-reduced-motion: reduce) {
     | Opens a media query `@media (prefers-reduced-motion: reduce) {`. The rules inside apply only when that screen condition is true, so the same components reflow on a phone.

2438 |   *, *::before, *::after {
     | CSS comment, ignored by the browser. It labels the next group of rules: *, *::before, *::after {

2439 |     animation-duration: 0.01ms !important;
     | Sets CSS property `animation-duration` to `0.01ms !important`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2440 |     animation-iteration-count: 1 !important;
     | Sets CSS property `animation-iteration-count` to `1 !important`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2441 |     transition-duration: 0.01ms !important;
     | Sets CSS property `transition-duration` to `0.01ms !important`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2442 |     scroll-behavior: auto !important;
     | Sets CSS property `scroll-behavior` to `auto !important`. The cascade uses this when the surrounding selector matches. `var(--…)` reads a token defined on `:root` or `:root[data-theme=light]`.

2443 |   }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

2444 | }
     | Closes the rule or at-rule opened above. Properties after this belong to the next selector.

