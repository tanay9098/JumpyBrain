# `src/styles.css`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | @tailwind base;
     | This pulls in a big box of ready-made paint from Tailwind.

   2 | @tailwind components;
     | This pulls in a big box of ready-made paint from Tailwind.

   3 | @tailwind utilities;
     | This pulls in a big box of ready-made paint from Tailwind.

   4 | 
     | A blank line in the paint file. It does not change how anything looks.

   5 | /* ═══════════════════════════════════════════════════════
     | A label for people about the next chunk of paint. The browser ignores it.

   6 |    JUMPYBRAIN — JB MOMENTUM DESIGN SYSTEM v4
     | One paint instruction in the big style file.

   7 |    Token-driven theming: one CSS var change cascades everywhere
     | One paint instruction in the big style file.

   8 |    ═══════════════════════════════════════════════════════ */
     | A label for people about the next chunk of paint. The browser ignores it.

   9 | 
     | A blank line in the paint file. It does not change how anything looks.

  10 | /* ── Design Tokens (Dark Theme = default) ───────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

  11 | :root {
     | This starts paint instructions for things that match `:root`.

  12 |   /* Brand — JB Momentum palette */
     | A label for people about the next chunk of paint. The browser ignores it.

  13 |   --indigo: #6366f1;
     | This sets one look: --indigo becomes #6366f1.

  14 |   --indigo-light: #a5b4fc;
     | This sets one look: --indigo-light becomes #a5b4fc.

  15 |   --indigo-dim: rgba(99, 102, 241, 0.15);
     | This sets one look: --indigo-dim becomes rgba(99, 102, 241, 0.15).

  16 |   --violet: #7c3aed;
     | This sets one look: --violet becomes #7c3aed.

  17 |   --violet-light: #a78bfa;
     | This sets one look: --violet-light becomes #a78bfa.

  18 |   --violet-dim: rgba(124, 58, 237, 0.15);
     | This sets one look: --violet-dim becomes rgba(124, 58, 237, 0.15).

  19 |   --electric-blue: #2563eb;
     | This sets one look: --electric-blue becomes #2563eb.

  20 |   --cyan: #06b6d4;
     | This sets one look: --cyan becomes #06b6d4.

  21 |   --cyan-dim: rgba(6, 182, 212, 0.15);
     | This sets one look: --cyan-dim becomes rgba(6, 182, 212, 0.15).

  22 |   --teal: #10b981;
     | This sets one look: --teal becomes #10b981.

  23 | 
     | A blank line in the paint file. It does not change how anything looks.

  24 |   /* Semantic colors */
     | A label for people about the next chunk of paint. The browser ignores it.

  25 |   --green: #10b981;
     | This sets one look: --green becomes #10b981.

  26 |   --green-dim: rgba(16, 185, 129, 0.15);
     | This sets one look: --green-dim becomes rgba(16, 185, 129, 0.15).

  27 |   --amber: #f59e0b;
     | This sets one look: --amber becomes #f59e0b.

  28 |   --amber-dim: rgba(245, 158, 11, 0.15);
     | This sets one look: --amber-dim becomes rgba(245, 158, 11, 0.15).

  29 |   --red: #ef4444;
     | This sets one look: --red becomes #ef4444.

  30 |   --red-dim: rgba(239, 68, 68, 0.15);
     | This sets one look: --red-dim becomes rgba(239, 68, 68, 0.15).

  31 |   --blue: #2563eb;
     | This sets one look: --blue becomes #2563eb.

  32 | 
     | A blank line in the paint file. It does not change how anything looks.

  33 |   /* Reward (dopamine) */
     | A label for people about the next chunk of paint. The browser ignores it.

  34 |   --gold: #fbbf24;
     | This sets one look: --gold becomes #fbbf24.

  35 |   --pink: #f472b6;
     | This sets one look: --pink becomes #f472b6.

  36 | 
     | A blank line in the paint file. It does not change how anything looks.

  37 |   /* Neutral scale – dark — WCAG AA compliant */
     | A label for people about the next chunk of paint. The browser ignores it.

  38 |   --bg: #0f1020;
     | This sets one look: --bg becomes #0f1020.

  39 |   --surface: #1a1b2e;
     | This sets one look: --surface becomes #1a1b2e.

  40 |   --card: #1e1f35;
     | This sets one look: --card becomes #1e1f35.

  41 |   --card-hover: #252640;
     | This sets one look: --card-hover becomes #252640.

  42 |   --border: rgba(255, 255, 255, 0.08);
     | This sets one look: --border becomes rgba(255, 255, 255, 0.08).

  43 |   --border-active: rgba(99, 102, 241, 0.5);
     | This sets one look: --border-active becomes rgba(99, 102, 241, 0.5).

  44 |   --text: #eef0ff;           /* 14:1 on --bg */
     | A label for people about the next chunk of paint. The browser ignores it.

  45 |   --text-soft: #c0c4e8;      /* 8:1 on --bg */
     | A label for people about the next chunk of paint. The browser ignores it.

  46 |   --muted: #9196c0;          /* 4.6:1 on --bg */
     | A label for people about the next chunk of paint. The browser ignores it.

  47 |   --shadow: 0 4px 24px rgba(0, 0, 0, 0.45);
     | This sets one look: --shadow becomes 0 4px 24px rgba(0, 0, 0, 0.45).

  48 |   --shadow-card: 0 2px 12px rgba(0, 0, 0, 0.35);
     | This sets one look: --shadow-card becomes 0 2px 12px rgba(0, 0, 0, 0.35).

  49 | 
     | A blank line in the paint file. It does not change how anything looks.

  50 |   /* Brand gradient (used on logo, primary accents) */
     | A label for people about the next chunk of paint. The browser ignores it.

  51 |   --brand-gradient: linear-gradient(135deg, #7c3aed 0%, #6366f1 45%, #06b6d4 100%);
     | This sets one look: --brand-gradient becomes linear-gradient(135deg, #7c3aed 0%, #6366f1 45%, #06b6d4 100%).

  52 | 
     | A blank line in the paint file. It does not change how anything looks.

  53 |   /* Layout */
     | A label for people about the next chunk of paint. The browser ignores it.

  54 |   --sidebar-w: 224px;
     | This sets one look: --sidebar-w becomes 224px.

  55 |   --top-bar-h: 52px;
     | This sets one look: --top-bar-h becomes 52px.

  56 |   --bottom-nav-h: 60px;
     | This sets one look: --bottom-nav-h becomes 60px.

  57 |   --radius: 14px;
     | This sets one look: --radius becomes 14px.

  58 |   --radius-sm: 8px;
     | This sets one look: --radius-sm becomes 8px.

  59 |   --radius-lg: 20px;
     | This sets one look: --radius-lg becomes 20px.

  60 | 
     | A blank line in the paint file. It does not change how anything looks.

  61 |   /* Type scale — 3 steps: 12 / 14 / 22+ */
     | A label for people about the next chunk of paint. The browser ignores it.

  62 |   --text-xs: 12px;
     | This sets one look: --text-xs becomes 12px.

  63 |   --text-sm: 14px;
     | This sets one look: --text-sm becomes 14px.

  64 |   --text-base: 15px;
     | This sets one look: --text-base becomes 15px.

  65 |   --text-lg: 18px;
     | This sets one look: --text-lg becomes 18px.

  66 |   --text-xl: 22px;
     | This sets one look: --text-xl becomes 22px.

  67 | 
     | A blank line in the paint file. It does not change how anything looks.

  68 |   /* Spacing — 4-step scale */
     | A label for people about the next chunk of paint. The browser ignores it.

  69 |   --space-1: 4px;
     | This sets one look: --space-1 becomes 4px.

  70 |   --space-2: 8px;
     | This sets one look: --space-2 becomes 8px.

  71 |   --space-3: 12px;
     | This sets one look: --space-3 becomes 12px.

  72 |   --space-4: 16px;
     | This sets one look: --space-4 becomes 16px.

  73 |   --space-5: 20px;
     | This sets one look: --space-5 becomes 20px.

  74 |   --space-6: 24px;
     | This sets one look: --space-6 becomes 24px.

  75 | 
     | A blank line in the paint file. It does not change how anything looks.

  76 |   font-family: "Inter", "Plus Jakarta Sans", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
     | This sets one look: font-family becomes "Inter", "Plus Jakarta Sans", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif.

  77 |   -webkit-font-smoothing: antialiased;
     | This sets one look: -webkit-font-smoothing becomes antialiased.

  78 |   -moz-osx-font-smoothing: grayscale;
     | This sets one look: -moz-osx-font-smoothing becomes grayscale.

  79 | }
     | This ends that group of paint instructions.

  80 | 
     | A blank line in the paint file. It does not change how anything looks.

  81 | /* ── Light Theme ────────────────────────────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

  82 | :root[data-theme="light"] {
     | This starts paint instructions for things that match `:root[data-theme="light"]`.

  83 |   --bg: #f4f4fe;
     | This sets one look: --bg becomes #f4f4fe.

  84 |   --surface: #ffffff;
     | This sets one look: --surface becomes #ffffff.

  85 |   --card: #ffffff;
     | This sets one look: --card becomes #ffffff.

  86 |   --card-hover: #f8f8ff;
     | This sets one look: --card-hover becomes #f8f8ff.

  87 |   --border: rgba(0, 0, 0, 0.07);
     | This sets one look: --border becomes rgba(0, 0, 0, 0.07).

  88 |   --border-active: rgba(99, 102, 241, 0.4);
     | This sets one look: --border-active becomes rgba(99, 102, 241, 0.4).

  89 |   --text: #0d0e1f;           /* 16:1 on --bg */
     | A label for people about the next chunk of paint. The browser ignores it.

  90 |   --text-soft: #32355a;      /* 9.5:1 on --bg */
     | A label for people about the next chunk of paint. The browser ignores it.

  91 |   --muted: #5456a0;          /* 4.8:1 on --bg */
     | A label for people about the next chunk of paint. The browser ignores it.

  92 |   --shadow: 0 4px 24px rgba(0, 0, 0, 0.06);
     | This sets one look: --shadow becomes 0 4px 24px rgba(0, 0, 0, 0.06).

  93 |   --shadow-card: 0 2px 8px rgba(0, 0, 0, 0.05);
     | This sets one look: --shadow-card becomes 0 2px 8px rgba(0, 0, 0, 0.05).

  94 |   --violet-dim: rgba(124, 58, 237, 0.07);
     | This sets one look: --violet-dim becomes rgba(124, 58, 237, 0.07).

  95 |   --indigo-dim: rgba(99, 102, 241, 0.07);
     | This sets one look: --indigo-dim becomes rgba(99, 102, 241, 0.07).

  96 |   --cyan-dim: rgba(6, 182, 212, 0.07);
     | This sets one look: --cyan-dim becomes rgba(6, 182, 212, 0.07).

  97 |   --green-dim: rgba(16, 185, 129, 0.07);
     | This sets one look: --green-dim becomes rgba(16, 185, 129, 0.07).

  98 |   --amber-dim: rgba(245, 158, 11, 0.07);
     | This sets one look: --amber-dim becomes rgba(245, 158, 11, 0.07).

  99 |   --red-dim: rgba(239, 68, 68, 0.07);
     | This sets one look: --red-dim becomes rgba(239, 68, 68, 0.07).

 100 | }
     | This ends that group of paint instructions.

 101 | 
     | A blank line in the paint file. It does not change how anything looks.

 102 | /* ── Reset ──────────────────────────────────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

 103 | *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
     | A label for people about the next chunk of paint. The browser ignores it.

 104 | html, body, #root { height: 100%; width: 100%; }
     | One paint instruction in the big style file.

 105 | body {
     | This starts paint instructions for things that match `body`.

 106 |   background: var(--bg);
     | This sets one look: background becomes var(--bg).

 107 |   color: var(--text);
     | This sets one look: color becomes var(--text).

 108 |   transition: background 0.3s, color 0.3s;
     | This sets one look: transition becomes background 0.3s, color 0.3s.

 109 | }
     | This ends that group of paint instructions.

 110 | 
     | A blank line in the paint file. It does not change how anything looks.

 111 | /* ── Global focus rings (WCAG 2.4.7) ───────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

 112 | :focus-visible {
     | This starts paint instructions for things that match `:focus-visible`.

 113 |   outline: 2px solid var(--indigo-light);
     | This sets one look: outline becomes 2px solid var(--indigo-light).

 114 |   outline-offset: 2px;
     | This sets one look: outline-offset becomes 2px.

 115 |   border-radius: var(--radius-sm);
     | This sets one look: border-radius becomes var(--radius-sm).

 116 | }
     | This ends that group of paint instructions.

 117 | button:focus-visible,
     | One paint instruction in the big style file.

 118 | a:focus-visible,
     | One paint instruction in the big style file.

 119 | input:focus-visible,
     | One paint instruction in the big style file.

 120 | select:focus-visible,
     | One paint instruction in the big style file.

 121 | textarea:focus-visible {
     | This starts paint instructions for things that match `textarea:focus-visible`.

 122 |   outline: 2px solid var(--indigo-light);
     | This sets one look: outline becomes 2px solid var(--indigo-light).

 123 |   outline-offset: 2px;
     | This sets one look: outline-offset becomes 2px.

 124 | }
     | This ends that group of paint instructions.

 125 | 
     | A blank line in the paint file. It does not change how anything looks.

 126 | /* ── App Shell ──────────────────────────────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

 127 | .app-shell {
     | This starts paint instructions for things that match `.app-shell`.

 128 |   display: flex;
     | This sets one look: display becomes flex.

 129 |   width: 100%;
     | This sets one look: width becomes 100%.

 130 |   height: 100vh;
     | This sets one look: height becomes 100vh.

 131 |   overflow: hidden;
     | This sets one look: overflow becomes hidden.

 132 | }
     | This ends that group of paint instructions.

 133 | 
     | A blank line in the paint file. It does not change how anything looks.

 134 | .main-wrapper {
     | This starts paint instructions for things that match `.main-wrapper`.

 135 |   flex: 1;
     | This sets one look: flex becomes 1.

 136 |   display: flex;
     | This sets one look: display becomes flex.

 137 |   flex-direction: column;
     | This sets one look: flex-direction becomes column.

 138 |   min-width: 0;
     | This sets one look: min-width becomes 0.

 139 |   overflow: hidden;
     | This sets one look: overflow becomes hidden.

 140 | }
     | This ends that group of paint instructions.

 141 | 
     | A blank line in the paint file. It does not change how anything looks.

 142 | /* ── Top Bar ────────────────────────────────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

 143 | .top-bar {
     | This starts paint instructions for things that match `.top-bar`.

 144 |   display: flex;
     | This sets one look: display becomes flex.

 145 |   align-items: center;
     | This sets one look: align-items becomes center.

 146 |   justify-content: space-between;
     | This sets one look: justify-content becomes space-between.

 147 |   height: var(--top-bar-h);
     | This sets one look: height becomes var(--top-bar-h).

 148 |   padding: 0 var(--space-5);
     | This sets one look: padding becomes 0 var(--space-5).

 149 |   background: var(--surface);
     | This sets one look: background becomes var(--surface).

 150 |   border-bottom: 1px solid var(--border);
     | This sets one look: border-bottom becomes 1px solid var(--border).

 151 |   flex-shrink: 0;
     | This sets one look: flex-shrink becomes 0.

 152 |   gap: var(--space-3);
     | This sets one look: gap becomes var(--space-3).

 153 |   z-index: 50;
     | This sets one look: z-index becomes 50.

 154 | }
     | This ends that group of paint instructions.

 155 | 
     | A blank line in the paint file. It does not change how anything looks.

 156 | .top-bar-left {
     | This starts paint instructions for things that match `.top-bar-left`.

 157 |   display: flex;
     | This sets one look: display becomes flex.

 158 |   align-items: center;
     | This sets one look: align-items becomes center.

 159 |   gap: var(--space-3);
     | This sets one look: gap becomes var(--space-3).

 160 |   flex: 1;
     | This sets one look: flex becomes 1.

 161 |   min-width: 0;
     | This sets one look: min-width becomes 0.

 162 | }
     | This ends that group of paint instructions.

 163 | 
     | A blank line in the paint file. It does not change how anything looks.

 164 | .top-bar-right {
     | This starts paint instructions for things that match `.top-bar-right`.

 165 |   display: flex;
     | This sets one look: display becomes flex.

 166 |   align-items: center;
     | This sets one look: align-items becomes center.

 167 |   gap: var(--space-2);
     | This sets one look: gap becomes var(--space-2).

 168 |   flex-shrink: 0;
     | This sets one look: flex-shrink becomes 0.

 169 | }
     | This ends that group of paint instructions.

 170 | 
     | A blank line in the paint file. It does not change how anything looks.

 171 | .top-bar-menu-btn,
     | One paint instruction in the big style file.

 172 | .top-bar-icon-btn {
     | This starts paint instructions for things that match `.top-bar-icon-btn`.

 173 |   width: 36px;
     | This sets one look: width becomes 36px.

 174 |   height: 36px;
     | This sets one look: height becomes 36px.

 175 |   border: 1px solid var(--border);
     | This sets one look: border becomes 1px solid var(--border).

 176 |   border-radius: var(--radius-sm);
     | This sets one look: border-radius becomes var(--radius-sm).

 177 |   background: transparent;
     | This sets one look: background becomes transparent.

 178 |   color: var(--text-soft);
     | This sets one look: color becomes var(--text-soft).

 179 |   cursor: pointer;
     | This sets one look: cursor becomes pointer.

 180 |   display: flex;
     | This sets one look: display becomes flex.

 181 |   align-items: center;
     | This sets one look: align-items becomes center.

 182 |   justify-content: center;
     | This sets one look: justify-content becomes center.

 183 |   flex-shrink: 0;
     | This sets one look: flex-shrink becomes 0.

 184 |   transition: all 0.15s;
     | This sets one look: transition becomes all 0.15s.

 185 |   text-decoration: none;
     | This sets one look: text-decoration becomes none.

 186 | }
     | This ends that group of paint instructions.

 187 | 
     | A blank line in the paint file. It does not change how anything looks.

 188 | .top-bar-menu-btn:hover,
     | One paint instruction in the big style file.

 189 | .top-bar-icon-btn:hover {
     | This starts paint instructions for things that match `.top-bar-icon-btn:hover`.

 190 |   border-color: var(--border-active);
     | This sets one look: border-color becomes var(--border-active).

 191 |   color: var(--text);
     | This sets one look: color becomes var(--text).

 192 | }
     | This ends that group of paint instructions.

 193 | 
     | A blank line in the paint file. It does not change how anything looks.

 194 | .top-bar-icon-btn svg { width: 18px; height: 18px; }
     | One paint instruction in the big style file.

 195 | .top-bar-logout-btn { display: none; }
     | One paint instruction in the big style file.

 196 | .top-bar-more-btn { display: none; }
     | One paint instruction in the big style file.

 197 | .top-bar-feedback-btn { display: none; }
     | One paint instruction in the big style file.

 198 | 
     | A blank line in the paint file. It does not change how anything looks.

 199 | .top-bar-brand {
     | This starts paint instructions for things that match `.top-bar-brand`.

 200 |   display: flex;
     | This sets one look: display becomes flex.

 201 |   align-items: center;
     | This sets one look: align-items becomes center.

 202 |   gap: var(--space-2);
     | This sets one look: gap becomes var(--space-2).

 203 |   min-width: 0;
     | This sets one look: min-width becomes 0.

 204 | }
     | This ends that group of paint instructions.

 205 | 
     | A blank line in the paint file. It does not change how anything looks.

 206 | .top-bar-page-title {
     | This starts paint instructions for things that match `.top-bar-page-title`.

 207 |   font-size: var(--text-base);
     | This sets one look: font-size becomes var(--text-base).

 208 |   font-weight: 700;
     | This sets one look: font-weight becomes 700.

 209 |   color: var(--text);
     | This sets one look: color becomes var(--text).

 210 |   white-space: nowrap;
     | This sets one look: white-space becomes nowrap.

 211 |   overflow: hidden;
     | This sets one look: overflow becomes hidden.

 212 |   text-overflow: ellipsis;
     | This sets one look: text-overflow becomes ellipsis.

 213 | }
     | This ends that group of paint instructions.

 214 | 
     | A blank line in the paint file. It does not change how anything looks.

 215 | /* ── Sidebar ────────────────────────────────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

 216 | .sidebar {
     | This starts paint instructions for things that match `.sidebar`.

 217 |   width: var(--sidebar-w);
     | This sets one look: width becomes var(--sidebar-w).

 218 |   min-width: var(--sidebar-w);
     | This sets one look: min-width becomes var(--sidebar-w).

 219 |   height: 100vh;
     | This sets one look: height becomes 100vh.

 220 |   background: var(--surface);
     | This sets one look: background becomes var(--surface).

 221 |   border-right: 1px solid var(--border);
     | This sets one look: border-right becomes 1px solid var(--border).

 222 |   display: flex;
     | This sets one look: display becomes flex.

 223 |   flex-direction: column;
     | This sets one look: flex-direction becomes column.

 224 |   padding: var(--space-5) var(--space-4);
     | This sets one look: padding becomes var(--space-5) var(--space-4).

 225 |   gap: 0;
     | This sets one look: gap becomes 0.

 226 |   overflow-y: auto;
     | This sets one look: overflow-y becomes auto.

 227 |   transition: background 0.3s;
     | This sets one look: transition becomes background 0.3s.

 228 |   flex-shrink: 0;
     | This sets one look: flex-shrink becomes 0.

 229 | }
     | This ends that group of paint instructions.

 230 | 
     | A blank line in the paint file. It does not change how anything looks.

 231 | .sidebar-brand {
     | This starts paint instructions for things that match `.sidebar-brand`.

 232 |   display: flex;
     | This sets one look: display becomes flex.

 233 |   align-items: center;
     | This sets one look: align-items becomes center.

 234 |   gap: var(--space-3);
     | This sets one look: gap becomes var(--space-3).

 235 |   padding: 6px 6px 18px;
     | This sets one look: padding becomes 6px 6px 18px.

 236 |   border-bottom: 1px solid var(--border);
     | This sets one look: border-bottom becomes 1px solid var(--border).

 237 |   margin-bottom: var(--space-3);
     | This sets one look: margin-bottom becomes var(--space-3).

 238 | }
     | This ends that group of paint instructions.

 239 | 
     | A blank line in the paint file. It does not change how anything looks.

 240 | .sidebar-logo {
     | This starts paint instructions for things that match `.sidebar-logo`.

 241 |   width: 36px;
     | This sets one look: width becomes 36px.

 242 |   height: 36px;
     | This sets one look: height becomes 36px.

 243 |   display: flex;
     | This sets one look: display becomes flex.

 244 |   align-items: center;
     | This sets one look: align-items becomes center.

 245 |   justify-content: center;
     | This sets one look: justify-content becomes center.

 246 |   flex-shrink: 0;
     | This sets one look: flex-shrink becomes 0.

 247 | }
     | This ends that group of paint instructions.

 248 | 
     | A blank line in the paint file. It does not change how anything looks.

 249 | .sidebar-title {
     | This starts paint instructions for things that match `.sidebar-title`.

 250 |   font-weight: 700;
     | This sets one look: font-weight becomes 700.

 251 |   font-size: var(--text-sm);
     | This sets one look: font-size becomes var(--text-sm).

 252 |   color: var(--text);
     | This sets one look: color becomes var(--text).

 253 |   line-height: 1.2;
     | This sets one look: line-height becomes 1.2.

 254 |   letter-spacing: -0.01em;
     | This sets one look: letter-spacing becomes -0.01em.

 255 | }
     | This ends that group of paint instructions.

 256 | 
     | A blank line in the paint file. It does not change how anything looks.

 257 | .sidebar-title span {
     | This starts paint instructions for things that match `.sidebar-title span`.

 258 |   background: var(--brand-gradient);
     | This sets one look: background becomes var(--brand-gradient).

 259 |   -webkit-background-clip: text;
     | This sets one look: -webkit-background-clip becomes text.

 260 |   -webkit-text-fill-color: transparent;
     | This sets one look: -webkit-text-fill-color becomes transparent.

 261 |   background-clip: text;
     | This sets one look: background-clip becomes text.

 262 | }
     | This ends that group of paint instructions.

 263 | 
     | A blank line in the paint file. It does not change how anything looks.

 264 | .sidebar-subtitle {
     | This starts paint instructions for things that match `.sidebar-subtitle`.

 265 |   font-size: var(--text-xs);
     | This sets one look: font-size becomes var(--text-xs).

 266 |   color: var(--muted);
     | This sets one look: color becomes var(--muted).

 267 | }
     | This ends that group of paint instructions.

 268 | 
     | A blank line in the paint file. It does not change how anything looks.

 269 | .sidebar-nav-section {
     | This starts paint instructions for things that match `.sidebar-nav-section`.

 270 |   display: flex;
     | This sets one look: display becomes flex.

 271 |   flex-direction: column;
     | This sets one look: flex-direction becomes column.

 272 |   gap: 1px;
     | This sets one look: gap becomes 1px.

 273 | }
     | This ends that group of paint instructions.

 274 | 
     | A blank line in the paint file. It does not change how anything looks.

 275 | .sidebar-section-label {
     | This starts paint instructions for things that match `.sidebar-section-label`.

 276 |   font-size: var(--text-xs);
     | This sets one look: font-size becomes var(--text-xs).

 277 |   font-weight: 700;
     | This sets one look: font-weight becomes 700.

 278 |   color: var(--muted);
     | This sets one look: color becomes var(--muted).

 279 |   text-transform: uppercase;
     | This sets one look: text-transform becomes uppercase.

 280 |   letter-spacing: 0.8px;
     | This sets one look: letter-spacing becomes 0.8px.

 281 |   padding: 6px 10px 3px;
     | This sets one look: padding becomes 6px 10px 3px.

 282 | }
     | This ends that group of paint instructions.

 283 | 
     | A blank line in the paint file. It does not change how anything looks.

 284 | /* Primary nav items */
     | A label for people about the next chunk of paint. The browser ignores it.

 285 | .nav-item {
     | This starts paint instructions for things that match `.nav-item`.

 286 |   display: flex;
     | This sets one look: display becomes flex.

 287 |   align-items: center;
     | This sets one look: align-items becomes center.

 288 |   gap: var(--space-2);
     | This sets one look: gap becomes var(--space-2).

 289 |   padding: 9px 10px;
     | This sets one look: padding becomes 9px 10px.

 290 |   border-radius: var(--radius-sm);
     | This sets one look: border-radius becomes var(--radius-sm).

 291 |   cursor: pointer;
     | This sets one look: cursor becomes pointer.

 292 |   text-decoration: none;
     | This sets one look: text-decoration becomes none.

 293 |   color: var(--text-soft);
     | This sets one look: color becomes var(--text-soft).

 294 |   font-size: var(--text-sm);
     | This sets one look: font-size becomes var(--text-sm).

 295 |   font-weight: 500;
     | This sets one look: font-weight becomes 500.

 296 |   transition: all 0.15s;
     | This sets one look: transition becomes all 0.15s.

 297 |   border: none;
     | This sets one look: border becomes none.

 298 |   background: transparent;
     | This sets one look: background becomes transparent.

 299 |   width: 100%;
     | This sets one look: width becomes 100%.

 300 |   text-align: left;
     | This sets one look: text-align becomes left.

 301 | }
     | This ends that group of paint instructions.

 302 | 
     | A blank line in the paint file. It does not change how anything looks.

 303 | .nav-item:hover { background: var(--indigo-dim); color: var(--indigo-light); }
     | One paint instruction in the big style file.

 304 | .nav-item.active {
     | This starts paint instructions for things that match `.nav-item.active`.

 305 |   background: var(--indigo-dim);
     | This sets one look: background becomes var(--indigo-dim).

 306 |   color: var(--indigo-light);
     | This sets one look: color becomes var(--indigo-light).

 307 |   font-weight: 600;
     | This sets one look: font-weight becomes 600.

 308 | }
     | This ends that group of paint instructions.

 309 | .nav-item svg { width: 18px; height: 18px; flex-shrink: 0; }
     | One paint instruction in the big style file.

 310 | 
     | A blank line in the paint file. It does not change how anything looks.

 311 | /* Smaller secondary nav items */
     | A label for people about the next chunk of paint. The browser ignores it.

 312 | .nav-item-sm {
     | This starts paint instructions for things that match `.nav-item-sm`.

 313 |   padding: 6px 10px;
     | This sets one look: padding becomes 6px 10px.

 314 |   font-size: var(--text-xs);
     | This sets one look: font-size becomes var(--text-xs).

 315 | }
     | This ends that group of paint instructions.

 316 | .nav-item-sm svg { width: 15px; height: 15px; }
     | One paint instruction in the big style file.

 317 | 
     | A blank line in the paint file. It does not change how anything looks.

 318 | /* Feedback nav item — subtle accent so it's discoverable but not shouting */
     | A label for people about the next chunk of paint. The browser ignores it.

 319 | .nav-item-feedback {
     | This starts paint instructions for things that match `.nav-item-feedback`.

 320 |   background: var(--indigo-dim);
     | This sets one look: background becomes var(--indigo-dim).

 321 |   color: var(--indigo-light);
     | This sets one look: color becomes var(--indigo-light).

 322 | }
     | This ends that group of paint instructions.

 323 | .nav-item-feedback:hover { background: rgba(99, 102, 241, 0.22); color: var(--indigo-light); }
     | One paint instruction in the big style file.

 324 | 
     | A blank line in the paint file. It does not change how anything looks.

 325 | /* Compact connector rows */
     | A label for people about the next chunk of paint. The browser ignores it.

 326 | .connector-row {
     | This starts paint instructions for things that match `.connector-row`.

 327 |   display: flex;
     | This sets one look: display becomes flex.

 328 |   align-items: center;
     | This sets one look: align-items becomes center.

 329 |   gap: var(--space-2);
     | This sets one look: gap becomes var(--space-2).

 330 |   padding: 5px 10px;
     | This sets one look: padding becomes 5px 10px.

 331 |   border-radius: var(--radius-sm);
     | This sets one look: border-radius becomes var(--radius-sm).

 332 |   text-decoration: none;
     | This sets one look: text-decoration becomes none.

 333 |   color: var(--text-soft);
     | This sets one look: color becomes var(--text-soft).

 334 |   font-size: var(--text-xs);
     | This sets one look: font-size becomes var(--text-xs).

 335 |   font-weight: 500;
     | This sets one look: font-weight becomes 500.

 336 |   transition: all 0.15s;
     | This sets one look: transition becomes all 0.15s.

 337 | }
     | This ends that group of paint instructions.

 338 | .connector-row:hover { background: var(--indigo-dim); color: var(--text); }
     | One paint instruction in the big style file.

 339 | .connector-row.active { background: var(--indigo-dim); color: var(--indigo-light); }
     | One paint instruction in the big style file.

 340 | 
     | A blank line in the paint file. It does not change how anything looks.

 341 | .connector-row-icon {
     | This starts paint instructions for things that match `.connector-row-icon`.

 342 |   width: 20px;
     | This sets one look: width becomes 20px.

 343 |   height: 20px;
     | This sets one look: height becomes 20px.

 344 |   border-radius: 5px;
     | This sets one look: border-radius becomes 5px.

 345 |   display: flex;
     | This sets one look: display becomes flex.

 346 |   align-items: center;
     | This sets one look: align-items becomes center.

 347 |   justify-content: center;
     | This sets one look: justify-content becomes center.

 348 |   flex-shrink: 0;
     | This sets one look: flex-shrink becomes 0.

 349 | }
     | This ends that group of paint instructions.

 350 | .connector-row-label { flex: 1; }
     | One paint instruction in the big style file.

 351 | 
     | A blank line in the paint file. It does not change how anything looks.

 352 | /* Pinned energy in sidebar */
     | A label for people about the next chunk of paint. The browser ignores it.

 353 | .sidebar-energy {
     | This starts paint instructions for things that match `.sidebar-energy`.

 354 |   margin-top: var(--space-3);
     | This sets one look: margin-top becomes var(--space-3).

 355 |   padding: var(--space-2) 0;
     | This sets one look: padding becomes var(--space-2) 0.

 356 |   border-top: 1px solid var(--border);
     | This sets one look: border-top becomes 1px solid var(--border).

 357 | }
     | This ends that group of paint instructions.

 358 | 
     | A blank line in the paint file. It does not change how anything looks.

 359 | .sidebar-footer {
     | This starts paint instructions for things that match `.sidebar-footer`.

 360 |   margin-top: auto;
     | This sets one look: margin-top becomes auto.

 361 |   display: flex;
     | This sets one look: display becomes flex.

 362 |   flex-direction: column;
     | This sets one look: flex-direction becomes column.

 363 |   gap: var(--space-2);
     | This sets one look: gap becomes var(--space-2).

 364 |   padding-top: var(--space-3);
     | This sets one look: padding-top becomes var(--space-3).

 365 |   border-top: 1px solid var(--border);
     | This sets one look: border-top becomes 1px solid var(--border).

 366 | }
     | This ends that group of paint instructions.

 367 | 
     | A blank line in the paint file. It does not change how anything looks.

 368 | /* ── Energy Control ─────────────────────────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

 369 | .energy-control {}
     | One paint instruction in the big style file.

 370 | 
     | A blank line in the paint file. It does not change how anything looks.

 371 | .energy-control-row {
     | This starts paint instructions for things that match `.energy-control-row`.

 372 |   display: flex;
     | This sets one look: display becomes flex.

 373 |   gap: var(--space-2);
     | This sets one look: gap becomes var(--space-2).

 374 |   align-items: center;
     | This sets one look: align-items becomes center.

 375 |   flex-wrap: wrap;
     | This sets one look: flex-wrap becomes wrap.

 376 | }
     | This ends that group of paint instructions.

 377 | 
     | A blank line in the paint file. It does not change how anything looks.

 378 | .energy-current-label {
     | This starts paint instructions for things that match `.energy-current-label`.

 379 |   font-size: var(--text-xs);
     | This sets one look: font-size becomes var(--text-xs).

 380 |   color: var(--muted);
     | This sets one look: color becomes var(--muted).

 381 |   margin-left: var(--space-1);
     | This sets one look: margin-left becomes var(--space-1).

 382 | }
     | This ends that group of paint instructions.

 383 | 
     | A blank line in the paint file. It does not change how anything looks.

 384 | /* Compact dots for sidebar */
     | A label for people about the next chunk of paint. The browser ignores it.

 385 | .energy-control-compact {
     | This starts paint instructions for things that match `.energy-control-compact`.

 386 |   display: flex;
     | This sets one look: display becomes flex.

 387 |   gap: 5px;
     | This sets one look: gap becomes 5px.

 388 |   padding: 4px 6px;
     | This sets one look: padding becomes 4px 6px.

 389 | }
     | This ends that group of paint instructions.

 390 | 
     | A blank line in the paint file. It does not change how anything looks.

 391 | .energy-dot {
     | This starts paint instructions for things that match `.energy-dot`.

 392 |   width: 26px;
     | This sets one look: width becomes 26px.

 393 |   height: 26px;
     | This sets one look: height becomes 26px.

 394 |   border-radius: 50%;
     | This sets one look: border-radius becomes 50%.

 395 |   border: 2px solid var(--border);
     | This sets one look: border becomes 2px solid var(--border).

 396 |   cursor: pointer;
     | This sets one look: cursor becomes pointer.

 397 |   display: flex;
     | This sets one look: display becomes flex.

 398 |   align-items: center;
     | This sets one look: align-items becomes center.

 399 |   justify-content: center;
     | This sets one look: justify-content becomes center.

 400 |   font-size: 11px;
     | This sets one look: font-size becomes 11px.

 401 |   transition: all 0.15s;
     | This sets one look: transition becomes all 0.15s.

 402 |   background: transparent;
     | This sets one look: background becomes transparent.

 403 |   color: var(--muted);
     | This sets one look: color becomes var(--muted).

 404 |   padding: 0;
     | This sets one look: padding becomes 0.

 405 | }
     | This ends that group of paint instructions.

 406 | .energy-dot.filled {
     | This starts paint instructions for things that match `.energy-dot.filled`.

 407 |   border-color: var(--amber);
     | This sets one look: border-color becomes var(--amber).

 408 |   background: var(--amber-dim);
     | This sets one look: background becomes var(--amber-dim).

 409 |   color: var(--amber);
     | This sets one look: color becomes var(--amber).

 410 | }
     | This ends that group of paint instructions.

 411 | .energy-dot:hover { transform: scale(1.1); }
     | One paint instruction in the big style file.

 412 | 
     | A blank line in the paint file. It does not change how anything looks.

 413 | /* Large energy buttons (Home page) */
     | A label for people about the next chunk of paint. The browser ignores it.

 414 | .energy-btn {
     | This starts paint instructions for things that match `.energy-btn`.

 415 |   width: 44px;
     | This sets one look: width becomes 44px.

 416 |   height: 44px;
     | This sets one look: height becomes 44px.

 417 |   border-radius: 10px;
     | This sets one look: border-radius becomes 10px.

 418 |   border: 2px solid var(--border);
     | This sets one look: border becomes 2px solid var(--border).

 419 |   background: transparent;
     | This sets one look: background becomes transparent.

 420 |   cursor: pointer;
     | This sets one look: cursor becomes pointer.

 421 |   font-size: 18px;
     | This sets one look: font-size becomes 18px.

 422 |   transition: all 0.15s;
     | This sets one look: transition becomes all 0.15s.

 423 |   display: flex;
     | This sets one look: display becomes flex.

 424 |   align-items: center;
     | This sets one look: align-items becomes center.

 425 |   justify-content: center;
     | This sets one look: justify-content becomes center.

 426 | }
     | This ends that group of paint instructions.

 427 | .energy-btn:hover { transform: scale(1.1); }
     | One paint instruction in the big style file.

 428 | .energy-btn.selected {
     | This starts paint instructions for things that match `.energy-btn.selected`.

 429 |   border-color: var(--amber);
     | This sets one look: border-color becomes var(--amber).

 430 |   background: var(--amber-dim);
     | This sets one look: background becomes var(--amber-dim).

 431 |   transform: scale(1.1);
     | This sets one look: transform becomes scale(1.1).

 432 | }
     | This ends that group of paint instructions.

 433 | 
     | A blank line in the paint file. It does not change how anything looks.

 434 | /* ── Theme / Logout ─────────────────────────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

 435 | .theme-toggle {
     | This starts paint instructions for things that match `.theme-toggle`.

 436 |   display: flex;
     | This sets one look: display becomes flex.

 437 |   align-items: center;
     | This sets one look: align-items becomes center.

 438 |   gap: var(--space-2);
     | This sets one look: gap becomes var(--space-2).

 439 |   padding: 7px 10px;
     | This sets one look: padding becomes 7px 10px.

 440 |   border-radius: var(--radius-sm);
     | This sets one look: border-radius becomes var(--radius-sm).

 441 |   cursor: pointer;
     | This sets one look: cursor becomes pointer.

 442 |   border: 1px solid var(--border);
     | This sets one look: border becomes 1px solid var(--border).

 443 |   background: transparent;
     | This sets one look: background becomes transparent.

 444 |   color: var(--muted);
     | This sets one look: color becomes var(--muted).

 445 |   font-size: var(--text-xs);
     | This sets one look: font-size becomes var(--text-xs).

 446 |   font-family: inherit;
     | This sets one look: font-family becomes inherit.

 447 |   transition: all 0.15s;
     | This sets one look: transition becomes all 0.15s.

 448 |   width: 100%;
     | This sets one look: width becomes 100%.

 449 | }
     | This ends that group of paint instructions.

 450 | .theme-toggle:hover { border-color: var(--indigo); color: var(--text); }
     | One paint instruction in the big style file.

 451 | .theme-toggle svg { width: 15px; height: 15px; }
     | One paint instruction in the big style file.

 452 | 
     | A blank line in the paint file. It does not change how anything looks.

 453 | .logout-btn {
     | This starts paint instructions for things that match `.logout-btn`.

 454 |   display: flex;
     | This sets one look: display becomes flex.

 455 |   align-items: center;
     | This sets one look: align-items becomes center.

 456 |   gap: var(--space-2);
     | This sets one look: gap becomes var(--space-2).

 457 |   padding: 7px 10px;
     | This sets one look: padding becomes 7px 10px.

 458 |   border-radius: var(--radius-sm);
     | This sets one look: border-radius becomes var(--radius-sm).

 459 |   cursor: pointer;
     | This sets one look: cursor becomes pointer.

 460 |   border: 1px solid var(--border);
     | This sets one look: border becomes 1px solid var(--border).

 461 |   background: transparent;
     | This sets one look: background becomes transparent.

 462 |   color: var(--muted);
     | This sets one look: color becomes var(--muted).

 463 |   font-size: var(--text-xs);
     | This sets one look: font-size becomes var(--text-xs).

 464 |   font-family: inherit;
     | This sets one look: font-family becomes inherit.

 465 |   transition: all 0.15s;
     | This sets one look: transition becomes all 0.15s.

 466 |   width: 100%;
     | This sets one look: width becomes 100%.

 467 | }
     | This ends that group of paint instructions.

 468 | .logout-btn:hover { border-color: var(--red); color: var(--red); }
     | One paint instruction in the big style file.

 469 | .logout-btn svg { width: 15px; height: 15px; }
     | One paint instruction in the big style file.

 470 | 
     | A blank line in the paint file. It does not change how anything looks.

 471 | .support-btn {
     | This starts paint instructions for things that match `.support-btn`.

 472 |   display: flex;
     | This sets one look: display becomes flex.

 473 |   align-items: center;
     | This sets one look: align-items becomes center.

 474 |   gap: var(--space-2);
     | This sets one look: gap becomes var(--space-2).

 475 |   padding: 7px 10px;
     | This sets one look: padding becomes 7px 10px.

 476 |   border-radius: var(--radius-sm);
     | This sets one look: border-radius becomes var(--radius-sm).

 477 |   cursor: pointer;
     | This sets one look: cursor becomes pointer.

 478 |   border: 1px solid var(--border);
     | This sets one look: border becomes 1px solid var(--border).

 479 |   background: transparent;
     | This sets one look: background becomes transparent.

 480 |   color: var(--muted);
     | This sets one look: color becomes var(--muted).

 481 |   font-size: var(--text-xs);
     | This sets one look: font-size becomes var(--text-xs).

 482 |   font-family: inherit;
     | This sets one look: font-family becomes inherit.

 483 |   text-decoration: none;
     | This sets one look: text-decoration becomes none.

 484 |   transition: all 0.15s;
     | This sets one look: transition becomes all 0.15s.

 485 |   width: 100%;
     | This sets one look: width becomes 100%.

 486 |   box-sizing: border-box;
     | This sets one look: box-sizing becomes border-box.

 487 | }
     | This ends that group of paint instructions.

 488 | .support-btn:hover { border-color: var(--amber); color: var(--amber); background: var(--amber-dim); }
     | One paint instruction in the big style file.

 489 | .support-btn svg { width: 15px; height: 15px; }
     | One paint instruction in the big style file.

 490 | 
     | A blank line in the paint file. It does not change how anything looks.

 491 | /* ── Sidebar Backdrop ────────────────────────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

 492 | .sidebar-backdrop {
     | This starts paint instructions for things that match `.sidebar-backdrop`.

 493 |   display: none;
     | This sets one look: display becomes none.

 494 |   position: fixed;
     | This sets one look: position becomes fixed.

 495 |   inset: 0;
     | This sets one look: inset becomes 0.

 496 |   background: rgba(0, 0, 0, 0.5);
     | This sets one look: background becomes rgba(0, 0, 0, 0.5).

 497 |   z-index: 99;
     | This sets one look: z-index becomes 99.

 498 |   backdrop-filter: blur(2px);
     | This sets one look: backdrop-filter becomes blur(2px).

 499 | }
     | This ends that group of paint instructions.

 500 | 
     | A blank line in the paint file. It does not change how anything looks.

 501 | /* ── Main Content ────────────────────────────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

 502 | .main-content {
     | This starts paint instructions for things that match `.main-content`.

 503 |   flex: 1;
     | This sets one look: flex becomes 1.

 504 |   overflow-y: auto;
     | This sets one look: overflow-y becomes auto.

 505 |   overflow-x: hidden;
     | This sets one look: overflow-x becomes hidden.

 506 |   padding: var(--space-6) 32px;
     | This sets one look: padding becomes var(--space-6) 32px.

 507 |   min-width: 0;
     | This sets one look: min-width becomes 0.

 508 |   min-height: 0;
     | This sets one look: min-height becomes 0.

 509 | }
     | This ends that group of paint instructions.

 510 | 
     | A blank line in the paint file. It does not change how anything looks.

 511 | /* ── Bottom Nav (mobile) ─────────────────────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

 512 | .bottom-nav {
     | This starts paint instructions for things that match `.bottom-nav`.

 513 |   display: none;
     | This sets one look: display becomes none.

 514 |   height: var(--bottom-nav-h);
     | This sets one look: height becomes var(--bottom-nav-h).

 515 |   background: var(--surface);
     | This sets one look: background becomes var(--surface).

 516 |   border-top: 1px solid var(--border);
     | This sets one look: border-top becomes 1px solid var(--border).

 517 |   flex-shrink: 0;
     | This sets one look: flex-shrink becomes 0.

 518 | }
     | This ends that group of paint instructions.

 519 | 
     | A blank line in the paint file. It does not change how anything looks.

 520 | .bottom-nav-item {
     | This starts paint instructions for things that match `.bottom-nav-item`.

 521 |   flex: 1;
     | This sets one look: flex becomes 1.

 522 |   display: flex;
     | This sets one look: display becomes flex.

 523 |   flex-direction: column;
     | This sets one look: flex-direction becomes column.

 524 |   align-items: center;
     | This sets one look: align-items becomes center.

 525 |   justify-content: center;
     | This sets one look: justify-content becomes center.

 526 |   gap: 3px;
     | This sets one look: gap becomes 3px.

 527 |   padding: 8px 4px;
     | This sets one look: padding becomes 8px 4px.

 528 |   text-decoration: none;
     | This sets one look: text-decoration becomes none.

 529 |   color: var(--muted);
     | This sets one look: color becomes var(--muted).

 530 |   font-size: 11px;
     | This sets one look: font-size becomes 11px.

 531 |   font-weight: 600;
     | This sets one look: font-weight becomes 600.

 532 |   transition: color 0.15s, transform 0.1s;
     | This sets one look: transition becomes color 0.15s, transform 0.1s.

 533 |   min-height: 56px;
     | This sets one look: min-height becomes 56px.

 534 |   cursor: pointer;
     | This sets one look: cursor becomes pointer.

 535 |   border: none;
     | This sets one look: border becomes none.

 536 |   background: transparent;
     | This sets one look: background becomes transparent.

 537 |   font-family: inherit;
     | This sets one look: font-family becomes inherit.

 538 | }
     | This ends that group of paint instructions.

 539 | .bottom-nav-item svg { width: 22px; height: 22px; }
     | One paint instruction in the big style file.

 540 | .bottom-nav-item.active { color: var(--indigo-light); }
     | One paint instruction in the big style file.

 541 | .bottom-nav-item:hover { color: var(--text-soft); }
     | One paint instruction in the big style file.

 542 | .bottom-nav-item:active { transform: scale(0.9); }
     | One paint instruction in the big style file.

 543 | 
     | A blank line in the paint file. It does not change how anything looks.

 544 | /* ── Responsive ──────────────────────────────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

 545 | @media (max-width: 1024px) {
     | This says: only use the next paint rules when the screen is a certain size.

 546 |   .main-content { padding: var(--space-5) var(--space-6); }
     | One paint instruction in the big style file.

 547 | }
     | This ends that group of paint instructions.

 548 | 
     | A blank line in the paint file. It does not change how anything looks.

 549 | @media (max-width: 768px) {
     | This says: only use the next paint rules when the screen is a certain size.

 550 |   .sidebar {
     | This starts paint instructions for things that match `.sidebar`.

 551 |     position: fixed;
     | This sets one look: position becomes fixed.

 552 |     top: 0;
     | This sets one look: top becomes 0.

 553 |     left: 0;
     | This sets one look: left becomes 0.

 554 |     height: 100vh;
     | This sets one look: height becomes 100vh.

 555 |     z-index: 100;
     | This sets one look: z-index becomes 100.

 556 |     transform: translateX(-100%);
     | This sets one look: transform becomes translateX(-100%).

 557 |     transition: transform 0.28s cubic-bezier(0.4, 0, 0.2, 1);
     | This sets one look: transition becomes transform 0.28s cubic-bezier(0.4, 0, 0.2, 1).

 558 |     box-shadow: 4px 0 24px rgba(0, 0, 0, 0.3);
     | This sets one look: box-shadow becomes 4px 0 24px rgba(0, 0, 0, 0.3).

 559 |   }
     | This ends that group of paint instructions.

 560 |   .sidebar.open { transform: translateX(0); }
     | One paint instruction in the big style file.

 561 |   .sidebar-backdrop { display: block; }
     | One paint instruction in the big style file.

 562 | 
     | A blank line in the paint file. It does not change how anything looks.

 563 |   /* Hide hamburger on mobile — bottom nav + More sheet handles it */
     | A label for people about the next chunk of paint. The browser ignores it.

 564 |   .top-bar-menu-btn { display: none; }
     | One paint instruction in the big style file.

 565 | 
     | A blank line in the paint file. It does not change how anything looks.

 566 |   /* Show logout in top bar on mobile (sidebar logout not visible) */
     | A label for people about the next chunk of paint. The browser ignores it.

 567 |   .top-bar-logout-btn { display: flex; }
     | One paint instruction in the big style file.

 568 | 
     | A blank line in the paint file. It does not change how anything looks.

 569 |   /* Show "More" trigger on mobile — opens the bottom sheet with Focus Timer, Focus Shield, etc. */
     | A label for people about the next chunk of paint. The browser ignores it.

 570 |   .top-bar-more-btn { display: flex; }
     | One paint instruction in the big style file.

 571 | 
     | A blank line in the paint file. It does not change how anything looks.

 572 |   /* Show feedback icon in top bar on mobile — sidebar nav item handles desktop */
     | A label for people about the next chunk of paint. The browser ignores it.

 573 |   .top-bar-feedback-btn { display: flex; }
     | One paint instruction in the big style file.

 574 | 
     | A blank line in the paint file. It does not change how anything looks.

 575 |   .bottom-nav { display: flex; }
     | One paint instruction in the big style file.

 576 |   .bottom-sheet-overlay {
     | This starts paint instructions for things that match `.bottom-sheet-overlay`.

 577 |     display: block;
     | This sets one look: display becomes block.

 578 |     opacity: 0;
     | This sets one look: opacity becomes 0.

 579 |     pointer-events: none;
     | This sets one look: pointer-events becomes none.

 580 |     transition: opacity 0.3s;
     | This sets one look: transition becomes opacity 0.3s.

 581 |   }
     | This ends that group of paint instructions.

 582 |   .bottom-sheet-overlay.open {
     | This starts paint instructions for things that match `.bottom-sheet-overlay.open`.

 583 |     opacity: 1;
     | This sets one look: opacity becomes 1.

 584 |     pointer-events: auto;
     | This sets one look: pointer-events becomes auto.

 585 |   }
     | This ends that group of paint instructions.

 586 |   .bottom-sheet { display: block; }
     | One paint instruction in the big style file.

 587 | 
     | A blank line in the paint file. It does not change how anything looks.

 588 |   .main-content {
     | This starts paint instructions for things that match `.main-content`.

 589 |     padding: var(--space-4);
     | This sets one look: padding becomes var(--space-4).

 590 |     padding-bottom: calc(var(--bottom-nav-h) + var(--space-4));
     | This sets one look: padding-bottom becomes calc(var(--bottom-nav-h) + var(--space-4)).

 591 |   }
     | This ends that group of paint instructions.

 592 | 
     | A blank line in the paint file. It does not change how anything looks.

 593 |   .page-title { font-size: 20px; }
     | One paint instruction in the big style file.

 594 |   .page-subtitle { margin-bottom: 16px; }
     | One paint instruction in the big style file.

 595 |   .connectors-page { padding: 0; }
     | One paint instruction in the big style file.

 596 |   .ring-container { width: 180px; height: 180px; }
     | One paint instruction in the big style file.

 597 |   .ring-svg { width: 180px; height: 180px; }
     | One paint instruction in the big style file.

 598 |   .ring-time { font-size: 32px; }
     | One paint instruction in the big style file.

 599 |   .focus-overlay-card { padding: 24px 20px; }
     | One paint instruction in the big style file.

 600 |   .connector-card { flex-wrap: wrap; gap: 12px; }
     | One paint instruction in the big style file.

 601 |   .connector-card-actions { flex-direction: row; align-items: center; width: 100%; }
     | One paint instruction in the big style file.

 602 |   .stat-value { font-size: 28px; }
     | One paint instruction in the big style file.

 603 |   .audio-time { font-size: 34px; }
     | One paint instruction in the big style file.

 604 |   .task-actions { padding-left: 0; flex-wrap: wrap; }
     | One paint instruction in the big style file.

 605 |   .task-meta { padding-left: 0; }
     | One paint instruction in the big style file.

 606 |   .subtask-list { padding-left: 0; }
     | One paint instruction in the big style file.

 607 | }
     | This ends that group of paint instructions.

 608 | 
     | A blank line in the paint file. It does not change how anything looks.

 609 | /* ── Touch feedback ──────────────────────────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

 610 | .btn:active:not(:disabled) { transform: scale(0.97) !important; opacity: 0.9; }
     | One paint instruction in the big style file.

 611 | .task-check:active { transform: scale(0.88); }
     | One paint instruction in the big style file.

 612 | .energy-btn:active { transform: scale(1.05); }
     | One paint instruction in the big style file.

 613 | .energy-dot:active { transform: scale(1.2); }
     | One paint instruction in the big style file.

 614 | 
     | A blank line in the paint file. It does not change how anything looks.

 615 | @media (max-width: 480px) {
     | This says: only use the next paint rules when the screen is a certain size.

 616 |   .main-content { padding: 12px; padding-bottom: calc(var(--bottom-nav-h) + 12px); }
     | One paint instruction in the big style file.

 617 |   .card { padding: 14px; }
     | One paint instruction in the big style file.

 618 |   .card-sm { padding: 10px; }
     | One paint instruction in the big style file.

 619 |   .page-title { font-size: 18px; }
     | One paint instruction in the big style file.

 620 |   .ring-container { width: 160px; height: 160px; }
     | One paint instruction in the big style file.

 621 |   .ring-svg { width: 160px; height: 160px; }
     | One paint instruction in the big style file.

 622 |   .ring-time { font-size: 28px; }
     | One paint instruction in the big style file.

 623 |   .btn { font-size: 13px; padding: 8px 12px; }
     | One paint instruction in the big style file.

 624 |   .btn-lg { font-size: 14px; padding: 10px 18px; }
     | One paint instruction in the big style file.

 625 |   .stat-tile { padding: 12px 14px; }
     | One paint instruction in the big style file.

 626 |   .stat-value { font-size: 24px; }
     | One paint instruction in the big style file.

 627 |   .what-next-task { font-size: 16px; }
     | One paint instruction in the big style file.

 628 |   .audio-time { font-size: 28px; }
     | One paint instruction in the big style file.

 629 |   .audio-player { padding: 20px 16px; }
     | One paint instruction in the big style file.

 630 |   .connectors-toast { top: 12px; right: 12px; left: 12px; right: auto; width: calc(100% - 24px); }
     | One paint instruction in the big style file.

 631 | }
     | This ends that group of paint instructions.

 632 | 
     | A blank line in the paint file. It does not change how anything looks.

 633 | /* ── Page structure ─────────────────────────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

 634 | .page-title {
     | This starts paint instructions for things that match `.page-title`.

 635 |   font-size: var(--text-xl);
     | This sets one look: font-size becomes var(--text-xl).

 636 |   font-weight: 800;
     | This sets one look: font-weight becomes 800.

 637 |   color: var(--text);
     | This sets one look: color becomes var(--text).

 638 |   margin-bottom: 4px;
     | This sets one look: margin-bottom becomes 4px.

 639 | }
     | This ends that group of paint instructions.

 640 | 
     | A blank line in the paint file. It does not change how anything looks.

 641 | .page-subtitle {
     | This starts paint instructions for things that match `.page-subtitle`.

 642 |   font-size: var(--text-sm);
     | This sets one look: font-size becomes var(--text-sm).

 643 |   color: var(--muted);
     | This sets one look: color becomes var(--muted).

 644 |   margin-bottom: var(--space-5);
     | This sets one look: margin-bottom becomes var(--space-5).

 645 | }
     | This ends that group of paint instructions.

 646 | 
     | A blank line in the paint file. It does not change how anything looks.

 647 | /* ── Cards ──────────────────────────────────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

 648 | .card {
     | This starts paint instructions for things that match `.card`.

 649 |   background: var(--card);
     | This sets one look: background becomes var(--card).

 650 |   border-radius: var(--radius);
     | This sets one look: border-radius becomes var(--radius).

 651 |   border: 1px solid var(--border);
     | This sets one look: border becomes 1px solid var(--border).

 652 |   padding: var(--space-5);
     | This sets one look: padding becomes var(--space-5).

 653 |   box-shadow: var(--shadow-card);
     | This sets one look: box-shadow becomes var(--shadow-card).

 654 |   transition: background 0.3s, border 0.3s;
     | This sets one look: transition becomes background 0.3s, border 0.3s.

 655 | }
     | This ends that group of paint instructions.

 656 | 
     | A blank line in the paint file. It does not change how anything looks.

 657 | .card-sm { padding: 14px; }
     | One paint instruction in the big style file.

 658 | 
     | A blank line in the paint file. It does not change how anything looks.

 659 | .card-title {
     | This starts paint instructions for things that match `.card-title`.

 660 |   font-size: var(--text-xs);
     | This sets one look: font-size becomes var(--text-xs).

 661 |   font-weight: 700;
     | This sets one look: font-weight becomes 700.

 662 |   color: var(--muted);
     | This sets one look: color becomes var(--muted).

 663 |   text-transform: uppercase;
     | This sets one look: text-transform becomes uppercase.

 664 |   letter-spacing: 0.8px;
     | This sets one look: letter-spacing becomes 0.8px.

 665 |   margin-bottom: 10px;
     | This sets one look: margin-bottom becomes 10px.

 666 | }
     | This ends that group of paint instructions.

 667 | 
     | A blank line in the paint file. It does not change how anything looks.

 668 | /* ── Grid layouts ───────────────────────────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

 669 | .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: var(--space-4); }
     | One paint instruction in the big style file.

 670 | .grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: var(--space-4); }
     | One paint instruction in the big style file.

 671 | .grid-4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: var(--space-4); }
     | One paint instruction in the big style file.

 672 | 
     | A blank line in the paint file. It does not change how anything looks.

 673 | .grid-main {
     | This starts paint instructions for things that match `.grid-main`.

 674 |   display: grid;
     | This sets one look: display becomes grid.

 675 |   grid-template-columns: 1fr 340px;
     | This sets one look: grid-template-columns becomes 1fr 340px.

 676 |   gap: var(--space-5);
     | This sets one look: gap becomes var(--space-5).

 677 | }
     | This ends that group of paint instructions.

 678 | 
     | A blank line in the paint file. It does not change how anything looks.

 679 | @media (max-width: 1024px) {
     | This says: only use the next paint rules when the screen is a certain size.

 680 |   .grid-main { grid-template-columns: 1fr; }
     | One paint instruction in the big style file.

 681 |   .grid-4 { grid-template-columns: repeat(2, 1fr); }
     | One paint instruction in the big style file.

 682 | }
     | This ends that group of paint instructions.

 683 | 
     | A blank line in the paint file. It does not change how anything looks.

 684 | @media (max-width: 768px) {
     | This says: only use the next paint rules when the screen is a certain size.

 685 |   .grid-2, .grid-3, .grid-4, .grid-main { grid-template-columns: 1fr; }
     | One paint instruction in the big style file.

 686 | }
     | This ends that group of paint instructions.

 687 | 
     | A blank line in the paint file. It does not change how anything looks.

 688 | @media (min-width: 480px) and (max-width: 768px) {
     | This says: only use the next paint rules when the screen is a certain size.

 689 |   .grid-3 { grid-template-columns: repeat(3, 1fr); }
     | One paint instruction in the big style file.

 690 |   .grid-2 { grid-template-columns: repeat(2, 1fr); }
     | One paint instruction in the big style file.

 691 | }
     | This ends that group of paint instructions.

 692 | 
     | A blank line in the paint file. It does not change how anything looks.

 693 | /* ── Buttons ────────────────────────────────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

 694 | .btn {
     | This starts paint instructions for things that match `.btn`.

 695 |   display: inline-flex;
     | This sets one look: display becomes inline-flex.

 696 |   align-items: center;
     | This sets one look: align-items becomes center.

 697 |   gap: 6px;
     | This sets one look: gap becomes 6px.

 698 |   padding: 9px 16px;
     | This sets one look: padding becomes 9px 16px.

 699 |   border-radius: var(--radius-sm);
     | This sets one look: border-radius becomes var(--radius-sm).

 700 |   border: none;
     | This sets one look: border becomes none.

 701 |   cursor: pointer;
     | This sets one look: cursor becomes pointer.

 702 |   font-weight: 600;
     | This sets one look: font-weight becomes 600.

 703 |   font-size: var(--text-sm);
     | This sets one look: font-size becomes var(--text-sm).

 704 |   font-family: inherit;
     | This sets one look: font-family becomes inherit.

 705 |   transition: all 0.15s;
     | This sets one look: transition becomes all 0.15s.

 706 |   text-decoration: none;
     | This sets one look: text-decoration becomes none.

 707 |   white-space: nowrap;
     | This sets one look: white-space becomes nowrap.

 708 | }
     | This ends that group of paint instructions.

 709 | 
     | A blank line in the paint file. It does not change how anything looks.

 710 | .btn-primary {
     | This starts paint instructions for things that match `.btn-primary`.

 711 |   background: var(--brand-gradient);
     | This sets one look: background becomes var(--brand-gradient).

 712 |   color: #fff;
     | This sets one look: color becomes #fff.

 713 |   box-shadow: 0 2px 10px rgba(99, 102, 241, 0.35);
     | This sets one look: box-shadow becomes 0 2px 10px rgba(99, 102, 241, 0.35).

 714 | }
     | This ends that group of paint instructions.

 715 | .btn-primary:hover { filter: brightness(1.08); transform: translateY(-1px); }
     | One paint instruction in the big style file.

 716 | .btn-primary:active { transform: none; filter: brightness(1); }
     | One paint instruction in the big style file.

 717 | 
     | A blank line in the paint file. It does not change how anything looks.

 718 | .btn-secondary {
     | This starts paint instructions for things that match `.btn-secondary`.

 719 |   background: var(--indigo-dim);
     | This sets one look: background becomes var(--indigo-dim).

 720 |   color: var(--indigo-light);
     | This sets one look: color becomes var(--indigo-light).

 721 |   border: 1px solid rgba(99, 102, 241, 0.2);
     | This sets one look: border becomes 1px solid rgba(99, 102, 241, 0.2).

 722 | }
     | This ends that group of paint instructions.

 723 | .btn-secondary:hover { background: rgba(99, 102, 241, 0.2); }
     | One paint instruction in the big style file.

 724 | 
     | A blank line in the paint file. It does not change how anything looks.

 725 | .btn-ghost {
     | This starts paint instructions for things that match `.btn-ghost`.

 726 |   background: transparent;
     | This sets one look: background becomes transparent.

 727 |   color: var(--muted);
     | This sets one look: color becomes var(--muted).

 728 |   border: 1px solid var(--border);
     | This sets one look: border becomes 1px solid var(--border).

 729 | }
     | This ends that group of paint instructions.

 730 | .btn-ghost:hover { color: var(--text); border-color: rgba(255, 255, 255, 0.2); }
     | One paint instruction in the big style file.

 731 | :root[data-theme="light"] .btn-ghost:hover { border-color: rgba(0,0,0,0.2); }
     | One paint instruction in the big style file.

 732 | 
     | A blank line in the paint file. It does not change how anything looks.

 733 | .btn-danger {
     | This starts paint instructions for things that match `.btn-danger`.

 734 |   background: var(--red-dim);
     | This sets one look: background becomes var(--red-dim).

 735 |   color: var(--red);
     | This sets one look: color becomes var(--red).

 736 |   border: 1px solid rgba(239, 68, 68, 0.2);
     | This sets one look: border becomes 1px solid rgba(239, 68, 68, 0.2).

 737 | }
     | This ends that group of paint instructions.

 738 | .btn-danger:hover { background: rgba(239, 68, 68, 0.2); }
     | One paint instruction in the big style file.

 739 | 
     | A blank line in the paint file. It does not change how anything looks.

 740 | .btn-success {
     | This starts paint instructions for things that match `.btn-success`.

 741 |   background: var(--green-dim);
     | This sets one look: background becomes var(--green-dim).

 742 |   color: var(--green);
     | This sets one look: color becomes var(--green).

 743 |   border: 1px solid rgba(16, 185, 129, 0.2);
     | This sets one look: border becomes 1px solid rgba(16, 185, 129, 0.2).

 744 | }
     | This ends that group of paint instructions.

 745 | .btn-success:hover { background: rgba(16, 185, 129, 0.2); }
     | One paint instruction in the big style file.

 746 | 
     | A blank line in the paint file. It does not change how anything looks.

 747 | .btn-amber {
     | This starts paint instructions for things that match `.btn-amber`.

 748 |   background: var(--amber-dim);
     | This sets one look: background becomes var(--amber-dim).

 749 |   color: var(--amber);
     | This sets one look: color becomes var(--amber).

 750 |   border: 1px solid rgba(245, 158, 11, 0.2);
     | This sets one look: border becomes 1px solid rgba(245, 158, 11, 0.2).

 751 | }
     | This ends that group of paint instructions.

 752 | 
     | A blank line in the paint file. It does not change how anything looks.

 753 | .btn-sm { padding: 5px 10px; font-size: var(--text-xs); }
     | One paint instruction in the big style file.

 754 | .btn-lg { padding: 12px 24px; font-size: 16px; }
     | One paint instruction in the big style file.

 755 | .btn:disabled { opacity: 0.5; cursor: not-allowed; transform: none !important; }
     | One paint instruction in the big style file.

 756 | 
     | A blank line in the paint file. It does not change how anything looks.

 757 | /* ── Inputs ─────────────────────────────────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

 758 | .input, .textarea, .select {
     | This starts paint instructions for things that match `.input, .textarea, .select`.

 759 |   width: 100%;
     | This sets one look: width becomes 100%.

 760 |   padding: 10px 14px;
     | This sets one look: padding becomes 10px 14px.

 761 |   border-radius: var(--radius-sm);
     | This sets one look: border-radius becomes var(--radius-sm).

 762 |   border: 1px solid var(--border);
     | This sets one look: border becomes 1px solid var(--border).

 763 |   background: var(--surface);
     | This sets one look: background becomes var(--surface).

 764 |   color: var(--text);
     | This sets one look: color becomes var(--text).

 765 |   font-size: var(--text-sm);
     | This sets one look: font-size becomes var(--text-sm).

 766 |   font-family: inherit;
     | This sets one look: font-family becomes inherit.

 767 |   outline: none;
     | This sets one look: outline becomes none.

 768 |   transition: border 0.15s;
     | This sets one look: transition becomes border 0.15s.

 769 | }
     | This ends that group of paint instructions.

 770 | .input:focus, .textarea:focus, .select:focus {
     | This starts paint instructions for things that match `.input:focus, .textarea:focus, .select:focus`.

 771 |   border-color: var(--indigo);
     | This sets one look: border-color becomes var(--indigo).

 772 |   box-shadow: 0 0 0 3px var(--indigo-dim);
     | This sets one look: box-shadow becomes 0 0 0 3px var(--indigo-dim).

 773 | }
     | This ends that group of paint instructions.

 774 | .textarea { resize: vertical; min-height: 100px; }
     | One paint instruction in the big style file.

 775 | .select option { background: var(--card); }
     | One paint instruction in the big style file.

 776 | 
     | A blank line in the paint file. It does not change how anything looks.

 777 | /* Text link */
     | A label for people about the next chunk of paint. The browser ignores it.

 778 | .text-link {
     | This starts paint instructions for things that match `.text-link`.

 779 |   color: var(--indigo-light);
     | This sets one look: color becomes var(--indigo-light).

 780 |   text-decoration: underline;
     | This sets one look: text-decoration becomes underline.

 781 |   cursor: pointer;
     | This sets one look: cursor becomes pointer.

 782 | }
     | This ends that group of paint instructions.

 783 | 
     | A blank line in the paint file. It does not change how anything looks.

 784 | /* ── Badges ─────────────────────────────────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

 785 | .badge {
     | This starts paint instructions for things that match `.badge`.

 786 |   display: inline-flex;
     | This sets one look: display becomes inline-flex.

 787 |   align-items: center;
     | This sets one look: align-items becomes center.

 788 |   padding: 2px 8px;
     | This sets one look: padding becomes 2px 8px.

 789 |   border-radius: 20px;
     | This sets one look: border-radius becomes 20px.

 790 |   font-size: var(--text-xs);
     | This sets one look: font-size becomes var(--text-xs).

 791 |   font-weight: 700;
     | This sets one look: font-weight becomes 700.

 792 |   letter-spacing: 0.3px;
     | This sets one look: letter-spacing becomes 0.3px.

 793 | }
     | This ends that group of paint instructions.

 794 | .badge-high { background: var(--red-dim); color: var(--red); }
     | One paint instruction in the big style file.

 795 | .badge-medium { background: var(--amber-dim); color: var(--amber); }
     | One paint instruction in the big style file.

 796 | .badge-low { background: var(--green-dim); color: var(--green); }
     | One paint instruction in the big style file.

 797 | .badge-violet { background: var(--indigo-dim); color: var(--indigo-light); }
     | One paint instruction in the big style file.

 798 | 
     | A blank line in the paint file. It does not change how anything looks.

 799 | /* ── Nav divider ────────────────────────────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

 800 | .nav-divider { height: 1px; background: var(--border); margin: 8px 0; }
     | One paint instruction in the big style file.

 801 | 
     | A blank line in the paint file. It does not change how anything looks.

 802 | /* ── Dread Meter ────────────────────────────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

 803 | .dread-meter { display: flex; gap: 3px; align-items: center; }
     | One paint instruction in the big style file.

 804 | 
     | A blank line in the paint file. It does not change how anything looks.

 805 | .dread-pip {
     | This starts paint instructions for things that match `.dread-pip`.

 806 |   width: 10px;
     | This sets one look: width becomes 10px.

 807 |   height: 10px;
     | This sets one look: height becomes 10px.

 808 |   border-radius: 2px;
     | This sets one look: border-radius becomes 2px.

 809 |   background: var(--border);
     | This sets one look: background becomes var(--border).

 810 |   cursor: pointer;
     | This sets one look: cursor becomes pointer.

 811 |   transition: background 0.1s, transform 0.1s;
     | This sets one look: transition becomes background 0.1s, transform 0.1s.

 812 | }
     | This ends that group of paint instructions.

 813 | .dread-pip:hover { transform: scale(1.2); }
     | One paint instruction in the big style file.

 814 | .dread-pip.active-1 { background: var(--green); }
     | One paint instruction in the big style file.

 815 | .dread-pip.active-2 { background: #84cc16; }
     | One paint instruction in the big style file.

 816 | .dread-pip.active-3 { background: var(--amber); }
     | One paint instruction in the big style file.

 817 | .dread-pip.active-4 { background: #f97316; }
     | One paint instruction in the big style file.

 818 | .dread-pip.active-5 { background: var(--red); }
     | One paint instruction in the big style file.

 819 | 
     | A blank line in the paint file. It does not change how anything looks.

 820 | /* ── Focus Ring Timer ───────────────────────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

 821 | .ring-container {
     | This starts paint instructions for things that match `.ring-container`.

 822 |   position: relative;
     | This sets one look: position becomes relative.

 823 |   width: 220px;
     | This sets one look: width becomes 220px.

 824 |   height: 220px;
     | This sets one look: height becomes 220px.

 825 |   margin: 0 auto 20px;
     | This sets one look: margin becomes 0 auto 20px.

 826 | }
     | This ends that group of paint instructions.

 827 | 
     | A blank line in the paint file. It does not change how anything looks.

 828 | .ring-svg { transform: rotate(-90deg); }
     | One paint instruction in the big style file.

 829 | .ring-track { fill: none; stroke: var(--border); stroke-width: 10; }
     | One paint instruction in the big style file.

 830 | .ring-progress {
     | This starts paint instructions for things that match `.ring-progress`.

 831 |   fill: none;
     | This sets one look: fill becomes none.

 832 |   stroke-width: 10;
     | This sets one look: stroke-width becomes 10.

 833 |   stroke-linecap: round;
     | This sets one look: stroke-linecap becomes round.

 834 |   transition: stroke-dashoffset 1s linear, stroke 0.3s;
     | This sets one look: transition becomes stroke-dashoffset 1s linear, stroke 0.3s.

 835 | }
     | This ends that group of paint instructions.

 836 | .ring-progress.work { stroke: var(--indigo); filter: drop-shadow(0 0 6px rgba(99,102,241,0.5)); }
     | One paint instruction in the big style file.

 837 | .ring-progress.brk { stroke: var(--green); filter: drop-shadow(0 0 6px rgba(16,185,129,0.4)); }
     | One paint instruction in the big style file.

 838 | 
     | A blank line in the paint file. It does not change how anything looks.

 839 | .ring-text {
     | This starts paint instructions for things that match `.ring-text`.

 840 |   position: absolute;
     | This sets one look: position becomes absolute.

 841 |   top: 50%;
     | This sets one look: top becomes 50%.

 842 |   left: 50%;
     | This sets one look: left becomes 50%.

 843 |   transform: translate(-50%, -50%);
     | This sets one look: transform becomes translate(-50%, -50%).

 844 |   text-align: center;
     | This sets one look: text-align becomes center.

 845 | }
     | This ends that group of paint instructions.

 846 | .ring-time {
     | This starts paint instructions for things that match `.ring-time`.

 847 |   font-size: 38px;
     | This sets one look: font-size becomes 38px.

 848 |   font-weight: 800;
     | This sets one look: font-weight becomes 800.

 849 |   font-variant-numeric: tabular-nums;
     | This sets one look: font-variant-numeric becomes tabular-nums.

 850 |   color: var(--text);
     | This sets one look: color becomes var(--text).

 851 |   line-height: 1;
     | This sets one look: line-height becomes 1.

 852 | }
     | This ends that group of paint instructions.

 853 | .ring-label {
     | This starts paint instructions for things that match `.ring-label`.

 854 |   font-size: var(--text-xs);
     | This sets one look: font-size becomes var(--text-xs).

 855 |   color: var(--muted);
     | This sets one look: color becomes var(--muted).

 856 |   margin-top: 4px;
     | This sets one look: margin-top becomes 4px.

 857 |   text-transform: uppercase;
     | This sets one look: text-transform becomes uppercase.

 858 |   letter-spacing: 0.5px;
     | This sets one look: letter-spacing becomes 0.5px.

 859 | }
     | This ends that group of paint instructions.

 860 | 
     | A blank line in the paint file. It does not change how anything looks.

 861 | /* ── Task picker (FocusTimer) ───────────────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

 862 | .task-link-picker {
     | This starts paint instructions for things that match `.task-link-picker`.

 863 |   border: 1px solid var(--border);
     | This sets one look: border becomes 1px solid var(--border).

 864 |   border-radius: var(--radius-sm);
     | This sets one look: border-radius becomes var(--radius-sm).

 865 |   padding: var(--space-3) var(--space-4);
     | This sets one look: padding becomes var(--space-3) var(--space-4).

 866 |   background: var(--surface);
     | This sets one look: background becomes var(--surface).

 867 | }
     | This ends that group of paint instructions.

 868 | 
     | A blank line in the paint file. It does not change how anything looks.

 869 | .linked-task-badge {
     | This starts paint instructions for things that match `.linked-task-badge`.

 870 |   display: flex;
     | This sets one look: display becomes flex.

 871 |   align-items: center;
     | This sets one look: align-items becomes center.

 872 |   gap: var(--space-2);
     | This sets one look: gap becomes var(--space-2).

 873 |   margin-top: var(--space-2);
     | This sets one look: margin-top becomes var(--space-2).

 874 |   padding: 6px 10px;
     | This sets one look: padding becomes 6px 10px.

 875 |   border-radius: var(--radius-sm);
     | This sets one look: border-radius becomes var(--radius-sm).

 876 |   background: var(--indigo-dim);
     | This sets one look: background becomes var(--indigo-dim).

 877 |   border: 1px solid rgba(99, 102, 241, 0.2);
     | This sets one look: border becomes 1px solid rgba(99, 102, 241, 0.2).

 878 |   font-size: var(--text-xs);
     | This sets one look: font-size becomes var(--text-xs).

 879 |   font-weight: 600;
     | This sets one look: font-weight becomes 600.

 880 |   color: var(--indigo-light);
     | This sets one look: color becomes var(--indigo-light).

 881 | }
     | This ends that group of paint instructions.

 882 | 
     | A blank line in the paint file. It does not change how anything looks.

 883 | /* ── Add Task Row ───────────────────────────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

 884 | .add-task-row {}
     | One paint instruction in the big style file.

 885 | 
     | A blank line in the paint file. It does not change how anything looks.

 886 | .add-task-details {
     | This starts paint instructions for things that match `.add-task-details`.

 887 |   margin-top: var(--space-3);
     | This sets one look: margin-top becomes var(--space-3).

 888 |   padding-top: var(--space-3);
     | This sets one look: padding-top becomes var(--space-3).

 889 |   border-top: 1px solid var(--border);
     | This sets one look: border-top becomes 1px solid var(--border).

 890 | }
     | This ends that group of paint instructions.

 891 | 
     | A blank line in the paint file. It does not change how anything looks.

 892 | /* ── Empty States ───────────────────────────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

 893 | .empty-state {
     | This starts paint instructions for things that match `.empty-state`.

 894 |   display: flex;
     | This sets one look: display becomes flex.

 895 |   flex-direction: column;
     | This sets one look: flex-direction becomes column.

 896 |   align-items: center;
     | This sets one look: align-items becomes center.

 897 |   text-align: center;
     | This sets one look: text-align becomes center.

 898 |   padding: 40px 20px;
     | This sets one look: padding becomes 40px 20px.

 899 |   gap: var(--space-3);
     | This sets one look: gap becomes var(--space-3).

 900 |   color: var(--muted);
     | This sets one look: color becomes var(--muted).

 901 | }
     | This ends that group of paint instructions.

 902 | 
     | A blank line in the paint file. It does not change how anything looks.

 903 | .empty-state-icon { font-size: 36px; }
     | One paint instruction in the big style file.

 904 | .empty-state-title { font-weight: 700; font-size: var(--text-base); color: var(--text-soft); }
     | One paint instruction in the big style file.

 905 | .empty-state-body { font-size: var(--text-sm); line-height: 1.6; max-width: 280px; }
     | One paint instruction in the big style file.

 906 | 
     | A blank line in the paint file. It does not change how anything looks.

 907 | /* ── Task Cards ─────────────────────────────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

 908 | .task-card {
     | This starts paint instructions for things that match `.task-card`.

 909 |   background: var(--card);
     | This sets one look: background becomes var(--card).

 910 |   border: 1px solid var(--border);
     | This sets one look: border becomes 1px solid var(--border).

 911 |   border-radius: var(--radius);
     | This sets one look: border-radius becomes var(--radius).

 912 |   padding: 14px 16px;
     | This sets one look: padding becomes 14px 16px.

 913 |   transition: all 0.2s;
     | This sets one look: transition becomes all 0.2s.

 914 | }
     | This ends that group of paint instructions.

 915 | 
     | A blank line in the paint file. It does not change how anything looks.

 916 | .task-card:hover {
     | This starts paint instructions for things that match `.task-card:hover`.

 917 |   border-color: rgba(99, 102, 241, 0.25);
     | This sets one look: border-color becomes rgba(99, 102, 241, 0.25).

 918 |   transform: translateY(-1px);
     | This sets one look: transform becomes translateY(-1px).

 919 |   box-shadow: var(--shadow-card);
     | This sets one look: box-shadow becomes var(--shadow-card).

 920 | }
     | This ends that group of paint instructions.

 921 | 
     | A blank line in the paint file. It does not change how anything looks.

 922 | .task-card.completing {
     | This starts paint instructions for things that match `.task-card.completing`.

 923 |   animation: taskComplete 0.45s ease-out forwards;
     | This sets one look: animation becomes taskComplete 0.45s ease-out forwards.

 924 | }
     | This ends that group of paint instructions.

 925 | 
     | A blank line in the paint file. It does not change how anything looks.

 926 | @keyframes taskComplete {
     | This starts a little movie of paint changes. Something else plays it by name.

 927 |   0%   { transform: scale(1); opacity: 1; }
     | One paint instruction in the big style file.

 928 |   50%  { transform: scale(1.02); background: var(--green-dim); border-color: var(--green); }
     | One paint instruction in the big style file.

 929 |   100% { transform: scale(0.95); opacity: 0; height: 0; padding: 0; margin: 0; overflow: hidden; }
     | One paint instruction in the big style file.

 930 | }
     | This ends that group of paint instructions.

 931 | 
     | A blank line in the paint file. It does not change how anything looks.

 932 | .task-header {
     | This starts paint instructions for things that match `.task-header`.

 933 |   display: flex;
     | This sets one look: display becomes flex.

 934 |   align-items: flex-start;
     | This sets one look: align-items becomes flex-start.

 935 |   gap: 10px;
     | This sets one look: gap becomes 10px.

 936 |   margin-bottom: 8px;
     | This sets one look: margin-bottom becomes 8px.

 937 | }
     | This ends that group of paint instructions.

 938 | 
     | A blank line in the paint file. It does not change how anything looks.

 939 | .task-check {
     | This starts paint instructions for things that match `.task-check`.

 940 |   width: 20px;
     | This sets one look: width becomes 20px.

 941 |   height: 20px;
     | This sets one look: height becomes 20px.

 942 |   border-radius: 6px;
     | This sets one look: border-radius becomes 6px.

 943 |   border: 2px solid var(--border);
     | This sets one look: border becomes 2px solid var(--border).

 944 |   cursor: pointer;
     | This sets one look: cursor becomes pointer.

 945 |   flex-shrink: 0;
     | This sets one look: flex-shrink becomes 0.

 946 |   margin-top: 2px;
     | This sets one look: margin-top becomes 2px.

 947 |   display: flex;
     | This sets one look: display becomes flex.

 948 |   align-items: center;
     | This sets one look: align-items becomes center.

 949 |   justify-content: center;
     | This sets one look: justify-content becomes center.

 950 |   transition: all 0.15s;
     | This sets one look: transition becomes all 0.15s.

 951 |   background: transparent;
     | This sets one look: background becomes transparent.

 952 |   padding: 0;
     | This sets one look: padding becomes 0.

 953 |   font-size: 11px;
     | This sets one look: font-size becomes 11px.

 954 |   color: transparent;
     | This sets one look: color becomes transparent.

 955 | }
     | This ends that group of paint instructions.

 956 | .task-check:hover { border-color: var(--green); background: var(--green-dim); color: var(--green); }
     | One paint instruction in the big style file.

 957 | 
     | A blank line in the paint file. It does not change how anything looks.

 958 | .task-title-text {
     | This starts paint instructions for things that match `.task-title-text`.

 959 |   font-weight: 600;
     | This sets one look: font-weight becomes 600.

 960 |   font-size: var(--text-base);
     | This sets one look: font-size becomes var(--text-base).

 961 |   color: var(--text);
     | This sets one look: color becomes var(--text).

 962 |   line-height: 1.4;
     | This sets one look: line-height becomes 1.4.

 963 |   flex: 1;
     | This sets one look: flex becomes 1.

 964 | }
     | This ends that group of paint instructions.

 965 | 
     | A blank line in the paint file. It does not change how anything looks.

 966 | .task-meta {
     | This starts paint instructions for things that match `.task-meta`.

 967 |   display: flex;
     | This sets one look: display becomes flex.

 968 |   gap: 8px;
     | This sets one look: gap becomes 8px.

 969 |   flex-wrap: wrap;
     | This sets one look: flex-wrap becomes wrap.

 970 |   align-items: center;
     | This sets one look: align-items becomes center.

 971 |   margin-bottom: 10px;
     | This sets one look: margin-bottom becomes 10px.

 972 |   font-size: var(--text-xs);
     | This sets one look: font-size becomes var(--text-xs).

 973 |   color: var(--muted);
     | This sets one look: color becomes var(--muted).

 974 |   padding-left: 30px;
     | This sets one look: padding-left becomes 30px.

 975 | }
     | This ends that group of paint instructions.

 976 | 
     | A blank line in the paint file. It does not change how anything looks.

 977 | .task-actions {
     | This starts paint instructions for things that match `.task-actions`.

 978 |   display: flex;
     | This sets one look: display becomes flex.

 979 |   gap: 6px;
     | This sets one look: gap becomes 6px.

 980 |   flex-wrap: wrap;
     | This sets one look: flex-wrap becomes wrap.

 981 |   padding-left: 30px;
     | This sets one look: padding-left becomes 30px.

 982 | }
     | This ends that group of paint instructions.

 983 | 
     | A blank line in the paint file. It does not change how anything looks.

 984 | /* ── Brain Dump ─────────────────────────────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

 985 | .brain-dump-wrap { position: relative; }
     | One paint instruction in the big style file.

 986 | 
     | A blank line in the paint file. It does not change how anything looks.

 987 | .brain-dump-hint {
     | This starts paint instructions for things that match `.brain-dump-hint`.

 988 |   position: absolute;
     | This sets one look: position becomes absolute.

 989 |   bottom: 10px;
     | This sets one look: bottom becomes 10px.

 990 |   right: 12px;
     | This sets one look: right becomes 12px.

 991 |   font-size: var(--text-xs);
     | This sets one look: font-size becomes var(--text-xs).

 992 |   color: var(--muted);
     | This sets one look: color becomes var(--muted).

 993 |   pointer-events: none;
     | This sets one look: pointer-events becomes none.

 994 | }
     | This ends that group of paint instructions.

 995 | 
     | A blank line in the paint file. It does not change how anything looks.

 996 | /* ── Stat Tiles ─────────────────────────────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

 997 | .stat-tile {
     | This starts paint instructions for things that match `.stat-tile`.

 998 |   background: var(--card);
     | This sets one look: background becomes var(--card).

 999 |   border: 1px solid var(--border);
     | This sets one look: border becomes 1px solid var(--border).

1000 |   border-radius: var(--radius);
     | This sets one look: border-radius becomes var(--radius).

1001 |   padding: 18px var(--space-5);
     | This sets one look: padding becomes 18px var(--space-5).

1002 |   display: flex;
     | This sets one look: display becomes flex.

1003 |   flex-direction: column;
     | This sets one look: flex-direction becomes column.

1004 |   gap: 6px;
     | This sets one look: gap becomes 6px.

1005 | }
     | This ends that group of paint instructions.

1006 | .stat-value {
     | This starts paint instructions for things that match `.stat-value`.

1007 |   font-size: 34px;
     | This sets one look: font-size becomes 34px.

1008 |   font-weight: 800;
     | This sets one look: font-weight becomes 800.

1009 |   line-height: 1;
     | This sets one look: line-height becomes 1.

1010 | }
     | This ends that group of paint instructions.

1011 | .stat-label {
     | This starts paint instructions for things that match `.stat-label`.

1012 |   font-size: var(--text-xs);
     | This sets one look: font-size becomes var(--text-xs).

1013 |   color: var(--muted);
     | This sets one look: color becomes var(--muted).

1014 |   text-transform: uppercase;
     | This sets one look: text-transform becomes uppercase.

1015 |   letter-spacing: 0.6px;
     | This sets one look: letter-spacing becomes 0.6px.

1016 | }
     | This ends that group of paint instructions.

1017 | .stat-violet { color: var(--indigo-light); }
     | One paint instruction in the big style file.

1018 | .stat-green { color: var(--green); }
     | One paint instruction in the big style file.

1019 | .stat-amber { color: var(--amber); }
     | One paint instruction in the big style file.

1020 | .stat-red { color: var(--red); }
     | One paint instruction in the big style file.

1021 | 
     | A blank line in the paint file. It does not change how anything looks.

1022 | /* ── Streak Badge ───────────────────────────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

1023 | .streak-badge {
     | This starts paint instructions for things that match `.streak-badge`.

1024 |   display: inline-flex;
     | This sets one look: display becomes inline-flex.

1025 |   align-items: center;
     | This sets one look: align-items becomes center.

1026 |   gap: 6px;
     | This sets one look: gap becomes 6px.

1027 |   background: linear-gradient(135deg, #fbbf24, #f97316);
     | This sets one look: background becomes linear-gradient(135deg, #fbbf24, #f97316).

1028 |   color: #fff;
     | This sets one look: color becomes #fff.

1029 |   padding: 5px 14px;
     | This sets one look: padding becomes 5px 14px.

1030 |   border-radius: 20px;
     | This sets one look: border-radius becomes 20px.

1031 |   font-weight: 700;
     | This sets one look: font-weight becomes 700.

1032 |   font-size: var(--text-sm);
     | This sets one look: font-size becomes var(--text-sm).

1033 |   box-shadow: 0 2px 8px rgba(251, 191, 36, 0.4);
     | This sets one look: box-shadow becomes 0 2px 8px rgba(251, 191, 36, 0.4).

1034 | }
     | This ends that group of paint instructions.

1035 | 
     | A blank line in the paint file. It does not change how anything looks.

1036 | /* ── Focus Overlay ──────────────────────────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

1037 | .focus-overlay {
     | This starts paint instructions for things that match `.focus-overlay`.

1038 |   position: fixed;
     | This sets one look: position becomes fixed.

1039 |   inset: 0;
     | This sets one look: inset becomes 0.

1040 |   background: rgba(0, 0, 0, 0.85);
     | This sets one look: background becomes rgba(0, 0, 0, 0.85).

1041 |   backdrop-filter: blur(8px);
     | This sets one look: backdrop-filter becomes blur(8px).

1042 |   z-index: 1000;
     | This sets one look: z-index becomes 1000.

1043 |   display: flex;
     | This sets one look: display becomes flex.

1044 |   align-items: center;
     | This sets one look: align-items becomes center.

1045 |   justify-content: center;
     | This sets one look: justify-content becomes center.

1046 |   animation: overlayIn 0.3s ease;
     | This sets one look: animation becomes overlayIn 0.3s ease.

1047 | }
     | This ends that group of paint instructions.

1048 | 
     | A blank line in the paint file. It does not change how anything looks.

1049 | @keyframes overlayIn {
     | This starts a little movie of paint changes. Something else plays it by name.

1050 |   from { opacity: 0; }
     | One paint instruction in the big style file.

1051 |   to   { opacity: 1; }
     | One paint instruction in the big style file.

1052 | }
     | This ends that group of paint instructions.

1053 | 
     | A blank line in the paint file. It does not change how anything looks.

1054 | .focus-overlay-card {
     | This starts paint instructions for things that match `.focus-overlay-card`.

1055 |   background: var(--card);
     | This sets one look: background becomes var(--card).

1056 |   border: 1px solid var(--indigo);
     | This sets one look: border becomes 1px solid var(--indigo).

1057 |   border-radius: var(--radius-lg);
     | This sets one look: border-radius becomes var(--radius-lg).

1058 |   padding: 36px 40px;
     | This sets one look: padding becomes 36px 40px.

1059 |   text-align: center;
     | This sets one look: text-align becomes center.

1060 |   max-width: 380px;
     | This sets one look: max-width becomes 380px.

1061 |   width: 90%;
     | This sets one look: width becomes 90%.

1062 |   box-shadow: 0 0 60px rgba(99, 102, 241, 0.3);
     | This sets one look: box-shadow becomes 0 0 60px rgba(99, 102, 241, 0.3).

1063 |   animation: overlayCardIn 0.3s ease;
     | This sets one look: animation becomes overlayCardIn 0.3s ease.

1064 | }
     | This ends that group of paint instructions.

1065 | 
     | A blank line in the paint file. It does not change how anything looks.

1066 | @keyframes overlayCardIn {
     | This starts a little movie of paint changes. Something else plays it by name.

1067 |   from { transform: scale(0.95); opacity: 0; }
     | One paint instruction in the big style file.

1068 |   to   { transform: scale(1); opacity: 1; }
     | One paint instruction in the big style file.

1069 | }
     | This ends that group of paint instructions.

1070 | 
     | A blank line in the paint file. It does not change how anything looks.

1071 | .focus-overlay-icon { font-size: 48px; margin-bottom: 12px; }
     | One paint instruction in the big style file.

1072 | 
     | A blank line in the paint file. It does not change how anything looks.

1073 | .focus-overlay-title {
     | This starts paint instructions for things that match `.focus-overlay-title`.

1074 |   font-size: var(--text-lg);
     | This sets one look: font-size becomes var(--text-lg).

1075 |   font-weight: 800;
     | This sets one look: font-weight becomes 800.

1076 |   color: var(--text);
     | This sets one look: color becomes var(--text).

1077 |   margin-bottom: 8px;
     | This sets one look: margin-bottom becomes 8px.

1078 | }
     | This ends that group of paint instructions.

1079 | 
     | A blank line in the paint file. It does not change how anything looks.

1080 | .focus-overlay-text {
     | This starts paint instructions for things that match `.focus-overlay-text`.

1081 |   font-size: var(--text-sm);
     | This sets one look: font-size becomes var(--text-sm).

1082 |   color: var(--muted);
     | This sets one look: color becomes var(--muted).

1083 |   line-height: 1.7;
     | This sets one look: line-height becomes 1.7.

1084 |   margin-bottom: 20px;
     | This sets one look: margin-bottom becomes 20px.

1085 | }
     | This ends that group of paint instructions.

1086 | 
     | A blank line in the paint file. It does not change how anything looks.

1087 | /* ── Reward Burst ───────────────────────────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

1088 | .reward-burst {
     | This starts paint instructions for things that match `.reward-burst`.

1089 |   position: fixed;
     | This sets one look: position becomes fixed.

1090 |   top: 50%;
     | This sets one look: top becomes 50%.

1091 |   left: 50%;
     | This sets one look: left becomes 50%.

1092 |   transform: translate(-50%, -50%);
     | This sets one look: transform becomes translate(-50%, -50%).

1093 |   pointer-events: none;
     | This sets one look: pointer-events becomes none.

1094 |   z-index: 500;
     | This sets one look: z-index becomes 500.

1095 |   font-size: 52px;
     | This sets one look: font-size becomes 52px.

1096 |   animation: burstOut 0.9s ease-out forwards;
     | This sets one look: animation becomes burstOut 0.9s ease-out forwards.

1097 | }
     | This ends that group of paint instructions.

1098 | 
     | A blank line in the paint file. It does not change how anything looks.

1099 | @keyframes burstOut {
     | This starts a little movie of paint changes. Something else plays it by name.

1100 |   0%   { opacity: 1; transform: translate(-50%, -50%) scale(0.4); }
     | One paint instruction in the big style file.

1101 |   40%  { opacity: 1; transform: translate(-50%, -60%) scale(1.3); }
     | One paint instruction in the big style file.

1102 |   100% { opacity: 0; transform: translate(-50%, -100%) scale(0.8); }
     | One paint instruction in the big style file.

1103 | }
     | This ends that group of paint instructions.

1104 | 
     | A blank line in the paint file. It does not change how anything looks.

1105 | /* ── Auth ───────────────────────────────────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

1106 | .auth-page {
     | This starts paint instructions for things that match `.auth-page`.

1107 |   display: flex;
     | This sets one look: display becomes flex.

1108 |   align-items: center;
     | This sets one look: align-items becomes center.

1109 |   justify-content: center;
     | This sets one look: justify-content becomes center.

1110 |   min-height: 100dvh;
     | This sets one look: min-height becomes 100dvh.

1111 |   width: 100%;
     | This sets one look: width becomes 100%.

1112 |   background: var(--bg);
     | This sets one look: background becomes var(--bg).

1113 | }
     | This ends that group of paint instructions.

1114 | 
     | A blank line in the paint file. It does not change how anything looks.

1115 | .auth-card {
     | This starts paint instructions for things that match `.auth-card`.

1116 |   width: calc(100% - 48px);
     | This sets one look: width becomes calc(100% - 48px).

1117 |   max-width: 400px;
     | This sets one look: max-width becomes 400px.

1118 |   background: var(--card-hover);
     | This sets one look: background becomes var(--card-hover).

1119 |   border: 1px solid var(--border-active);
     | This sets one look: border becomes 1px solid var(--border-active).

1120 |   padding: var(--space-6);
     | This sets one look: padding becomes var(--space-6).

1121 |   display: flex;
     | This sets one look: display becomes flex.

1122 |   flex-direction: column;
     | This sets one look: flex-direction becomes column.

1123 |   gap: var(--space-4);
     | This sets one look: gap becomes var(--space-4).

1124 | }
     | This ends that group of paint instructions.

1125 | 
     | A blank line in the paint file. It does not change how anything looks.

1126 | .auth-brand {
     | This starts paint instructions for things that match `.auth-brand`.

1127 |   display: flex;
     | This sets one look: display becomes flex.

1128 |   align-items: center;
     | This sets one look: align-items becomes center.

1129 |   justify-content: center;
     | This sets one look: justify-content becomes center.

1130 | }
     | This ends that group of paint instructions.

1131 | 
     | A blank line in the paint file. It does not change how anything looks.

1132 | .auth-header {
     | This starts paint instructions for things that match `.auth-header`.

1133 |   text-align: center;
     | This sets one look: text-align becomes center.

1134 |   display: flex;
     | This sets one look: display becomes flex.

1135 |   flex-direction: column;
     | This sets one look: flex-direction becomes column.

1136 |   gap: 6px;
     | This sets one look: gap becomes 6px.

1137 | }
     | This ends that group of paint instructions.

1138 | 
     | A blank line in the paint file. It does not change how anything looks.

1139 | .auth-title {
     | This starts paint instructions for things that match `.auth-title`.

1140 |   font-size: var(--text-xl);
     | This sets one look: font-size becomes var(--text-xl).

1141 |   font-weight: 800;
     | This sets one look: font-weight becomes 800.

1142 |   margin-bottom: 4px;
     | This sets one look: margin-bottom becomes 4px.

1143 | }
     | This ends that group of paint instructions.

1144 | 
     | A blank line in the paint file. It does not change how anything looks.

1145 | .auth-subtitle {
     | This starts paint instructions for things that match `.auth-subtitle`.

1146 |   font-size: var(--text-sm);
     | This sets one look: font-size becomes var(--text-sm).

1147 |   color: var(--muted);
     | This sets one look: color becomes var(--muted).

1148 | }
     | This ends that group of paint instructions.

1149 | 
     | A blank line in the paint file. It does not change how anything looks.

1150 | .auth-value {
     | This starts paint instructions for things that match `.auth-value`.

1151 |   font-size: var(--text-sm);
     | This sets one look: font-size becomes var(--text-sm).

1152 |   color: var(--muted);
     | This sets one look: color becomes var(--muted).

1153 |   display: -webkit-box;
     | This sets one look: display becomes -webkit-box.

1154 |   -webkit-line-clamp: 2;
     | This sets one look: -webkit-line-clamp becomes 2.

1155 |   -webkit-box-orient: vertical;
     | This sets one look: -webkit-box-orient becomes vertical.

1156 |   overflow: hidden;
     | This sets one look: overflow becomes hidden.

1157 | }
     | This ends that group of paint instructions.

1158 | 
     | A blank line in the paint file. It does not change how anything looks.

1159 | .auth-status:empty { display: none; }
     | One paint instruction in the big style file.

1160 | 
     | A blank line in the paint file. It does not change how anything looks.

1161 | .auth-error {
     | This starts paint instructions for things that match `.auth-error`.

1162 |   padding: 10px 14px;
     | This sets one look: padding becomes 10px 14px.

1163 |   border-radius: var(--radius-sm);
     | This sets one look: border-radius becomes var(--radius-sm).

1164 |   background: var(--red-dim);
     | This sets one look: background becomes var(--red-dim).

1165 |   color: var(--red);
     | This sets one look: color becomes var(--red).

1166 |   font-size: 13px;
     | This sets one look: font-size becomes 13px.

1167 | }
     | This ends that group of paint instructions.

1168 | 
     | A blank line in the paint file. It does not change how anything looks.

1169 | .auth-legal {
     | This starts paint instructions for things that match `.auth-legal`.

1170 |   font-size: 12px;
     | This sets one look: font-size becomes 12px.

1171 |   color: var(--muted);
     | This sets one look: color becomes var(--muted).

1172 |   text-align: center;
     | This sets one look: text-align becomes center.

1173 |   line-height: 1.5;
     | This sets one look: line-height becomes 1.5.

1174 | }
     | This ends that group of paint instructions.

1175 | 
     | A blank line in the paint file. It does not change how anything looks.

1176 | /* ── Google sign-in button ────────────────────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

1177 | .btn-google {
     | This starts paint instructions for things that match `.btn-google`.

1178 |   display: flex;
     | This sets one look: display becomes flex.

1179 |   align-items: center;
     | This sets one look: align-items becomes center.

1180 |   justify-content: center;
     | This sets one look: justify-content becomes center.

1181 |   gap: 10px;
     | This sets one look: gap becomes 10px.

1182 |   width: 100%;
     | This sets one look: width becomes 100%.

1183 |   min-height: 44px;
     | This sets one look: min-height becomes 44px.

1184 |   padding: 10px 16px;
     | This sets one look: padding becomes 10px 16px.

1185 |   border-radius: var(--radius-sm);
     | This sets one look: border-radius becomes var(--radius-sm).

1186 |   border: 1px solid var(--border);
     | This sets one look: border becomes 1px solid var(--border).

1187 |   background: var(--surface);
     | This sets one look: background becomes var(--surface).

1188 |   color: var(--text);
     | This sets one look: color becomes var(--text).

1189 |   font-size: var(--text-sm);
     | This sets one look: font-size becomes var(--text-sm).

1190 |   font-weight: 600;
     | This sets one look: font-weight becomes 600.

1191 |   font-family: inherit;
     | This sets one look: font-family becomes inherit.

1192 |   cursor: pointer;
     | This sets one look: cursor becomes pointer.

1193 |   transition: background 0.15s, border-color 0.15s, transform 0.1s;
     | This sets one look: transition becomes background 0.15s, border-color 0.15s, transform 0.1s.

1194 | }
     | This ends that group of paint instructions.

1195 | .btn-google:hover:not(:disabled) { background: var(--card); border-color: var(--border-active); }
     | One paint instruction in the big style file.

1196 | .btn-google:active:not(:disabled) { transform: translateY(1px); }
     | One paint instruction in the big style file.

1197 | .btn-google:disabled { opacity: 0.7; cursor: not-allowed; }
     | One paint instruction in the big style file.

1198 | 
     | A blank line in the paint file. It does not change how anything looks.

1199 | .google-btn-wrap {
     | This starts paint instructions for things that match `.google-btn-wrap`.

1200 |   position: relative;
     | This sets one look: position becomes relative.

1201 | }
     | This ends that group of paint instructions.

1202 | .google-btn-wrap .btn-google {
     | This starts paint instructions for things that match `.google-btn-wrap .btn-google`.

1203 |   pointer-events: none;
     | This sets one look: pointer-events becomes none.

1204 | }
     | This ends that group of paint instructions.

1205 | /* Google's real "Sign in with Google" button (from renderButton) is
     | A label for people about the next chunk of paint. The browser ignores it.

1206 |    mounted here, stretched over the styled button above and hidden via
     | One paint instruction in the big style file.

1207 |    opacity so the click a user makes actually lands on Google's own
     | One paint instruction in the big style file.

1208 |    element -- required for their popup/redirect flow to open reliably. */
     | A label for people about the next chunk of paint. The browser ignores it.

1209 | .google-btn-overlay {
     | This starts paint instructions for things that match `.google-btn-overlay`.

1210 |   position: absolute;
     | This sets one look: position becomes absolute.

1211 |   inset: 0;
     | This sets one look: inset becomes 0.

1212 |   display: flex;
     | This sets one look: display becomes flex.

1213 |   align-items: center;
     | This sets one look: align-items becomes center.

1214 |   justify-content: center;
     | This sets one look: justify-content becomes center.

1215 |   overflow: hidden;
     | This sets one look: overflow becomes hidden.

1216 |   opacity: 0;
     | This sets one look: opacity becomes 0.

1217 |   cursor: pointer;
     | This sets one look: cursor becomes pointer.

1218 | }
     | This ends that group of paint instructions.

1219 | 
     | A blank line in the paint file. It does not change how anything looks.

1220 | /* ── Inline spinner ───────────────────────────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

1221 | .spinner {
     | This starts paint instructions for things that match `.spinner`.

1222 |   width: 16px;
     | This sets one look: width becomes 16px.

1223 |   height: 16px;
     | This sets one look: height becomes 16px.

1224 |   flex-shrink: 0;
     | This sets one look: flex-shrink becomes 0.

1225 |   border: 2px solid var(--border);
     | This sets one look: border becomes 2px solid var(--border).

1226 |   border-top-color: currentColor;
     | This sets one look: border-top-color becomes currentColor.

1227 |   border-radius: 50%;
     | This sets one look: border-radius becomes 50%.

1228 |   display: inline-block;
     | This sets one look: display becomes inline-block.

1229 |   animation: spin 0.6s linear infinite;
     | This sets one look: animation becomes spin 0.6s linear infinite.

1230 | }
     | This ends that group of paint instructions.

1231 | @keyframes spin { to { transform: rotate(360deg); } }
     | This starts a little movie of paint changes. Something else plays it by name.

1232 | 
     | A blank line in the paint file. It does not change how anything looks.

1233 | .auth-switch {
     | This starts paint instructions for things that match `.auth-switch`.

1234 |   font-size: 13px;
     | This sets one look: font-size becomes 13px.

1235 |   color: var(--muted);
     | This sets one look: color becomes var(--muted).

1236 |   margin-top: 14px;
     | This sets one look: margin-top becomes 14px.

1237 |   text-align: center;
     | This sets one look: text-align becomes center.

1238 | }
     | This ends that group of paint instructions.

1239 | 
     | A blank line in the paint file. It does not change how anything looks.

1240 | .auth-link {
     | This starts paint instructions for things that match `.auth-link`.

1241 |   color: var(--indigo-light);
     | This sets one look: color becomes var(--indigo-light).

1242 |   cursor: pointer;
     | This sets one look: cursor becomes pointer.

1243 |   margin-left: 6px;
     | This sets one look: margin-left becomes 6px.

1244 |   font-weight: 600;
     | This sets one look: font-weight becomes 600.

1245 | }
     | This ends that group of paint instructions.

1246 | 
     | A blank line in the paint file. It does not change how anything looks.

1247 | /* ── Mode Tabs ──────────────────────────────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

1248 | .mode-tabs {
     | This starts paint instructions for things that match `.mode-tabs`.

1249 |   display: flex;
     | This sets one look: display becomes flex.

1250 |   gap: 4px;
     | This sets one look: gap becomes 4px.

1251 |   padding: 4px;
     | This sets one look: padding becomes 4px.

1252 |   background: var(--surface);
     | This sets one look: background becomes var(--surface).

1253 |   border-radius: var(--radius-sm);
     | This sets one look: border-radius becomes var(--radius-sm).

1254 |   margin-bottom: var(--space-5);
     | This sets one look: margin-bottom becomes var(--space-5).

1255 | }
     | This ends that group of paint instructions.

1256 | 
     | A blank line in the paint file. It does not change how anything looks.

1257 | .mode-tab {
     | This starts paint instructions for things that match `.mode-tab`.

1258 |   flex: 1;
     | This sets one look: flex becomes 1.

1259 |   padding: 7px 10px;
     | This sets one look: padding becomes 7px 10px.

1260 |   border-radius: 6px;
     | This sets one look: border-radius becomes 6px.

1261 |   border: none;
     | This sets one look: border becomes none.

1262 |   cursor: pointer;
     | This sets one look: cursor becomes pointer.

1263 |   font-size: 13px;
     | This sets one look: font-size becomes 13px.

1264 |   font-weight: 600;
     | This sets one look: font-weight becomes 600.

1265 |   color: var(--muted);
     | This sets one look: color becomes var(--muted).

1266 |   background: transparent;
     | This sets one look: background becomes transparent.

1267 |   font-family: inherit;
     | This sets one look: font-family becomes inherit.

1268 |   transition: all 0.15s;
     | This sets one look: transition becomes all 0.15s.

1269 | }
     | This ends that group of paint instructions.

1270 | 
     | A blank line in the paint file. It does not change how anything looks.

1271 | .mode-tab.active {
     | This starts paint instructions for things that match `.mode-tab.active`.

1272 |   background: var(--card);
     | This sets one look: background becomes var(--card).

1273 |   color: var(--indigo-light);
     | This sets one look: color becomes var(--indigo-light).

1274 |   box-shadow: var(--shadow-card);
     | This sets one look: box-shadow becomes var(--shadow-card).

1275 | }
     | This ends that group of paint instructions.

1276 | 
     | A blank line in the paint file. It does not change how anything looks.

1277 | /* ── Dev Notice Banner ──────────────────────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

1278 | .dev-banner {
     | This starts paint instructions for things that match `.dev-banner`.

1279 |   display: flex;
     | This sets one look: display becomes flex.

1280 |   align-items: flex-start;
     | This sets one look: align-items becomes flex-start.

1281 |   justify-content: space-between;
     | This sets one look: justify-content becomes space-between.

1282 |   gap: var(--space-4);
     | This sets one look: gap becomes var(--space-4).

1283 |   background: var(--card);
     | This sets one look: background becomes var(--card).

1284 |   border: 1px solid var(--border);
     | This sets one look: border becomes 1px solid var(--border).

1285 |   border-radius: var(--radius);
     | This sets one look: border-radius becomes var(--radius).

1286 |   padding: var(--space-4) var(--space-5);
     | This sets one look: padding becomes var(--space-4) var(--space-5).

1287 |   margin-bottom: var(--space-5);
     | This sets one look: margin-bottom becomes var(--space-5).

1288 |   box-shadow: var(--shadow-card);
     | This sets one look: box-shadow becomes var(--shadow-card).

1289 | }
     | This ends that group of paint instructions.

1290 | 
     | A blank line in the paint file. It does not change how anything looks.

1291 | .dev-banner-main {
     | This starts paint instructions for things that match `.dev-banner-main`.

1292 |   display: flex;
     | This sets one look: display becomes flex.

1293 |   align-items: flex-start;
     | This sets one look: align-items becomes flex-start.

1294 |   gap: var(--space-3);
     | This sets one look: gap becomes var(--space-3).

1295 |   min-width: 0;
     | This sets one look: min-width becomes 0.

1296 | }
     | This ends that group of paint instructions.

1297 | 
     | A blank line in the paint file. It does not change how anything looks.

1298 | .dev-banner-icon {
     | This starts paint instructions for things that match `.dev-banner-icon`.

1299 |   width: 20px;
     | This sets one look: width becomes 20px.

1300 |   height: 20px;
     | This sets one look: height becomes 20px.

1301 |   border-radius: 50%;
     | This sets one look: border-radius becomes 50%.

1302 |   background: var(--indigo-dim);
     | This sets one look: background becomes var(--indigo-dim).

1303 |   color: var(--indigo-light);
     | This sets one look: color becomes var(--indigo-light).

1304 |   font-size: 12px;
     | This sets one look: font-size becomes 12px.

1305 |   font-weight: 700;
     | This sets one look: font-weight becomes 700.

1306 |   font-style: italic;
     | This sets one look: font-style becomes italic.

1307 |   display: flex;
     | This sets one look: display becomes flex.

1308 |   align-items: center;
     | This sets one look: align-items becomes center.

1309 |   justify-content: center;
     | This sets one look: justify-content becomes center.

1310 |   flex-shrink: 0;
     | This sets one look: flex-shrink becomes 0.

1311 |   margin-top: 1px;
     | This sets one look: margin-top becomes 1px.

1312 | }
     | This ends that group of paint instructions.

1313 | 
     | A blank line in the paint file. It does not change how anything looks.

1314 | .dev-banner-text {
     | This starts paint instructions for things that match `.dev-banner-text`.

1315 |   font-size: var(--text-sm);
     | This sets one look: font-size becomes var(--text-sm).

1316 |   color: var(--text-soft);
     | This sets one look: color becomes var(--text-soft).

1317 |   line-height: 1.6;
     | This sets one look: line-height becomes 1.6.

1318 | }
     | This ends that group of paint instructions.

1319 | 
     | A blank line in the paint file. It does not change how anything looks.

1320 | .dev-banner-text strong { color: var(--text); }
     | One paint instruction in the big style file.

1321 | .dev-banner-text-short { display: none; }
     | One paint instruction in the big style file.

1322 | 
     | A blank line in the paint file. It does not change how anything looks.

1323 | .dev-banner-inline-link {
     | This starts paint instructions for things that match `.dev-banner-inline-link`.

1324 |   color: var(--indigo-light);
     | This sets one look: color becomes var(--indigo-light).

1325 |   font-weight: 600;
     | This sets one look: font-weight becomes 600.

1326 |   text-decoration: none;
     | This sets one look: text-decoration becomes none.

1327 | }
     | This ends that group of paint instructions.

1328 | .dev-banner-inline-link:hover { text-decoration: underline; }
     | One paint instruction in the big style file.

1329 | 
     | A blank line in the paint file. It does not change how anything looks.

1330 | .dev-banner-cta {
     | This starts paint instructions for things that match `.dev-banner-cta`.

1331 |   color: var(--indigo-light);
     | This sets one look: color becomes var(--indigo-light).

1332 |   font-weight: 600;
     | This sets one look: font-weight becomes 600.

1333 |   font-size: var(--text-sm);
     | This sets one look: font-size becomes var(--text-sm).

1334 |   text-decoration: none;
     | This sets one look: text-decoration becomes none.

1335 |   white-space: nowrap;
     | This sets one look: white-space becomes nowrap.

1336 |   flex-shrink: 0;
     | This sets one look: flex-shrink becomes 0.

1337 |   margin-top: 2px;
     | This sets one look: margin-top becomes 2px.

1338 | }
     | This ends that group of paint instructions.

1339 | .dev-banner-cta:hover { text-decoration: underline; }
     | One paint instruction in the big style file.

1340 | 
     | A blank line in the paint file. It does not change how anything looks.

1341 | @media (max-width: 768px) {
     | This says: only use the next paint rules when the screen is a certain size.

1342 |   .dev-banner { padding: var(--space-3) var(--space-4); margin-bottom: var(--space-4); }
     | One paint instruction in the big style file.

1343 |   .dev-banner-text-full { display: none; }
     | One paint instruction in the big style file.

1344 |   .dev-banner-text-short { display: inline; }
     | One paint instruction in the big style file.

1345 |   .dev-banner-cta { display: none; }
     | One paint instruction in the big style file.

1346 | }
     | This ends that group of paint instructions.

1347 | 
     | A blank line in the paint file. It does not change how anything looks.

1348 | /* ── Feedback CTA Card ──────────────────────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

1349 | .feedback-cta-title {
     | This starts paint instructions for things that match `.feedback-cta-title`.

1350 |   font-size: 15px;
     | This sets one look: font-size becomes 15px.

1351 |   font-weight: 700;
     | This sets one look: font-weight becomes 700.

1352 |   color: var(--text);
     | This sets one look: color becomes var(--text).

1353 |   margin-bottom: 6px;
     | This sets one look: margin-bottom becomes 6px.

1354 | }
     | This ends that group of paint instructions.

1355 | 
     | A blank line in the paint file. It does not change how anything looks.

1356 | .feedback-cta-mobile { display: none; }
     | One paint instruction in the big style file.

1357 | 
     | A blank line in the paint file. It does not change how anything looks.

1358 | @media (max-width: 1024px) {
     | This says: only use the next paint rules when the screen is a certain size.

1359 |   .feedback-cta-desktop { display: none; }
     | One paint instruction in the big style file.

1360 |   .feedback-cta-mobile { display: block; }
     | One paint instruction in the big style file.

1361 | }
     | This ends that group of paint instructions.

1362 | 
     | A blank line in the paint file. It does not change how anything looks.

1363 | /* ── What Next Card ─────────────────────────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

1364 | .what-next-card {
     | This starts paint instructions for things that match `.what-next-card`.

1365 |   background: linear-gradient(135deg, var(--indigo-dim), rgba(99, 102, 241, 0.04));
     | This sets one look: background becomes linear-gradient(135deg, var(--indigo-dim), rgba(99, 102, 241, 0.04)).

1366 |   border: 1px solid rgba(99, 102, 241, 0.2);
     | This sets one look: border becomes 1px solid rgba(99, 102, 241, 0.2).

1367 |   border-radius: var(--radius);
     | This sets one look: border-radius becomes var(--radius).

1368 |   padding: var(--space-5);
     | This sets one look: padding becomes var(--space-5).

1369 |   position: relative;
     | This sets one look: position becomes relative.

1370 |   overflow: hidden;
     | This sets one look: overflow becomes hidden.

1371 | }
     | This ends that group of paint instructions.

1372 | 
     | A blank line in the paint file. It does not change how anything looks.

1373 | .what-next-card::before {
     | This starts paint instructions for things that match `.what-next-card::before`.

1374 |   content: '';
     | This sets one look: content becomes ''.

1375 |   position: absolute;
     | This sets one look: position becomes absolute.

1376 |   top: -20px; right: -20px;
     | This sets one look: top becomes -20px; right: -20px.

1377 |   width: 120px; height: 120px;
     | This sets one look: width becomes 120px; height: 120px.

1378 |   background: radial-gradient(circle, rgba(99, 102, 241, 0.15), transparent 70%);
     | This sets one look: background becomes radial-gradient(circle, rgba(99, 102, 241, 0.15), transparent 70%).

1379 |   pointer-events: none;
     | This sets one look: pointer-events becomes none.

1380 | }
     | This ends that group of paint instructions.

1381 | 
     | A blank line in the paint file. It does not change how anything looks.

1382 | .what-next-label {
     | This starts paint instructions for things that match `.what-next-label`.

1383 |   font-size: var(--text-xs);
     | This sets one look: font-size becomes var(--text-xs).

1384 |   text-transform: uppercase;
     | This sets one look: text-transform becomes uppercase.

1385 |   letter-spacing: 1px;
     | This sets one look: letter-spacing becomes 1px.

1386 |   color: var(--indigo-light);
     | This sets one look: color becomes var(--indigo-light).

1387 |   font-weight: 700;
     | This sets one look: font-weight becomes 700.

1388 |   margin-bottom: 8px;
     | This sets one look: margin-bottom becomes 8px.

1389 | }
     | This ends that group of paint instructions.

1390 | 
     | A blank line in the paint file. It does not change how anything looks.

1391 | .what-next-task {
     | This starts paint instructions for things that match `.what-next-task`.

1392 |   font-size: 18px;
     | This sets one look: font-size becomes 18px.

1393 |   font-weight: 700;
     | This sets one look: font-weight becomes 700.

1394 |   color: var(--text);
     | This sets one look: color becomes var(--text).

1395 |   margin-bottom: 6px;
     | This sets one look: margin-bottom becomes 6px.

1396 |   line-height: 1.3;
     | This sets one look: line-height becomes 1.3.

1397 | }
     | This ends that group of paint instructions.

1398 | 
     | A blank line in the paint file. It does not change how anything looks.

1399 | .what-next-reason {
     | This starts paint instructions for things that match `.what-next-reason`.

1400 |   font-size: var(--text-sm);
     | This sets one look: font-size becomes var(--text-sm).

1401 |   color: var(--text-soft);
     | This sets one look: color becomes var(--text-soft).

1402 |   margin-bottom: 14px;
     | This sets one look: margin-bottom becomes 14px.

1403 |   line-height: 1.5;
     | This sets one look: line-height becomes 1.5.

1404 | }
     | This ends that group of paint instructions.

1405 | 
     | A blank line in the paint file. It does not change how anything looks.

1406 | /* ── Subtasks ───────────────────────────────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

1407 | .subtask-list {
     | This starts paint instructions for things that match `.subtask-list`.

1408 |   padding-left: 30px;
     | This sets one look: padding-left becomes 30px.

1409 |   margin-top: 8px;
     | This sets one look: margin-top becomes 8px.

1410 |   display: flex;
     | This sets one look: display becomes flex.

1411 |   flex-direction: column;
     | This sets one look: flex-direction becomes column.

1412 |   gap: 6px;
     | This sets one look: gap becomes 6px.

1413 | }
     | This ends that group of paint instructions.

1414 | 
     | A blank line in the paint file. It does not change how anything looks.

1415 | .subtask-item {
     | This starts paint instructions for things that match `.subtask-item`.

1416 |   display: flex;
     | This sets one look: display becomes flex.

1417 |   align-items: center;
     | This sets one look: align-items becomes center.

1418 |   gap: 8px;
     | This sets one look: gap becomes 8px.

1419 |   font-size: 13px;
     | This sets one look: font-size becomes 13px.

1420 |   color: var(--text-soft);
     | This sets one look: color becomes var(--text-soft).

1421 | }
     | This ends that group of paint instructions.

1422 | 
     | A blank line in the paint file. It does not change how anything looks.

1423 | .subtask-dot {
     | This starts paint instructions for things that match `.subtask-dot`.

1424 |   width: 5px;
     | This sets one look: width becomes 5px.

1425 |   height: 5px;
     | This sets one look: height becomes 5px.

1426 |   border-radius: 50%;
     | This sets one look: border-radius becomes 50%.

1427 |   background: var(--indigo);
     | This sets one look: background becomes var(--indigo).

1428 |   flex-shrink: 0;
     | This sets one look: flex-shrink becomes 0.

1429 | }
     | This ends that group of paint instructions.

1430 | 
     | A blank line in the paint file. It does not change how anything looks.

1431 | /* ── Mindfulness Audio Player ───────────────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

1432 | .audio-player {
     | This starts paint instructions for things that match `.audio-player`.

1433 |   background: var(--surface);
     | This sets one look: background becomes var(--surface).

1434 |   border-radius: var(--radius);
     | This sets one look: border-radius becomes var(--radius).

1435 |   padding: 28px 24px;
     | This sets one look: padding becomes 28px 24px.

1436 |   text-align: center;
     | This sets one look: text-align becomes center.

1437 |   border: 1px solid var(--border);
     | This sets one look: border becomes 1px solid var(--border).

1438 |   transition: background 0.3s;
     | This sets one look: transition becomes background 0.3s.

1439 | }
     | This ends that group of paint instructions.

1440 | 
     | A blank line in the paint file. It does not change how anything looks.

1441 | .audio-player.playing {
     | This starts paint instructions for things that match `.audio-player.playing`.

1442 |   background: linear-gradient(135deg, rgba(99, 102, 241, 0.12), rgba(6, 182, 212, 0.06));
     | This sets one look: background becomes linear-gradient(135deg, rgba(99, 102, 241, 0.12), rgba(6, 182, 212, 0.06)).

1443 |   border-color: rgba(99, 102, 241, 0.3);
     | This sets one look: border-color becomes rgba(99, 102, 241, 0.3).

1444 | }
     | This ends that group of paint instructions.

1445 | 
     | A blank line in the paint file. It does not change how anything looks.

1446 | .audio-state-label { font-size: var(--text-sm); color: var(--muted); margin-bottom: 8px; }
     | One paint instruction in the big style file.

1447 | .audio-time { font-size: 42px; font-weight: 800; font-variant-numeric: tabular-nums; color: var(--text); }
     | One paint instruction in the big style file.

1448 | .audio-duration { font-size: var(--text-xs); color: var(--muted); margin-top: 4px; margin-bottom: 16px; }
     | One paint instruction in the big style file.

1449 | 
     | A blank line in the paint file. It does not change how anything looks.

1450 | .audio-progress {
     | This starts paint instructions for things that match `.audio-progress`.

1451 |   width: 100%;
     | This sets one look: width becomes 100%.

1452 |   height: 4px;
     | This sets one look: height becomes 4px.

1453 |   background: var(--border);
     | This sets one look: background becomes var(--border).

1454 |   border-radius: 2px;
     | This sets one look: border-radius becomes 2px.

1455 |   margin-bottom: 20px;
     | This sets one look: margin-bottom becomes 20px.

1456 |   overflow: hidden;
     | This sets one look: overflow becomes hidden.

1457 | }
     | This ends that group of paint instructions.

1458 | 
     | A blank line in the paint file. It does not change how anything looks.

1459 | .audio-progress-fill {
     | This starts paint instructions for things that match `.audio-progress-fill`.

1460 |   height: 100%;
     | This sets one look: height becomes 100%.

1461 |   background: var(--brand-gradient);
     | This sets one look: background becomes var(--brand-gradient).

1462 |   border-radius: 2px;
     | This sets one look: border-radius becomes 2px.

1463 |   transition: width 0.5s;
     | This sets one look: transition becomes width 0.5s.

1464 | }
     | This ends that group of paint instructions.

1465 | 
     | A blank line in the paint file. It does not change how anything looks.

1466 | /* ── Affirmation ────────────────────────────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

1467 | .affirmation-card {
     | This starts paint instructions for things that match `.affirmation-card`.

1468 |   background: linear-gradient(135deg, var(--indigo-dim), var(--green-dim));
     | This sets one look: background becomes linear-gradient(135deg, var(--indigo-dim), var(--green-dim)).

1469 |   border: 1px solid rgba(99, 102, 241, 0.2);
     | This sets one look: border becomes 1px solid rgba(99, 102, 241, 0.2).

1470 |   border-radius: var(--radius);
     | This sets one look: border-radius becomes var(--radius).

1471 |   padding: 16px 20px;
     | This sets one look: padding becomes 16px 20px.

1472 |   font-weight: 600;
     | This sets one look: font-weight becomes 600.

1473 |   font-size: var(--text-base);
     | This sets one look: font-size becomes var(--text-base).

1474 |   line-height: 1.5;
     | This sets one look: line-height becomes 1.5.

1475 |   color: var(--text-soft);
     | This sets one look: color becomes var(--text-soft).

1476 |   text-align: center;
     | This sets one look: text-align becomes center.

1477 | }
     | This ends that group of paint instructions.

1478 | 
     | A blank line in the paint file. It does not change how anything looks.

1479 | /* ── Focus Status Pill ──────────────────────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

1480 | .focus-status {
     | This starts paint instructions for things that match `.focus-status`.

1481 |   display: inline-flex;
     | This sets one look: display becomes inline-flex.

1482 |   align-items: center;
     | This sets one look: align-items becomes center.

1483 |   gap: 6px;
     | This sets one look: gap becomes 6px.

1484 |   padding: 4px 12px;
     | This sets one look: padding becomes 4px 12px.

1485 |   border-radius: 20px;
     | This sets one look: border-radius becomes 20px.

1486 |   font-size: var(--text-xs);
     | This sets one look: font-size becomes var(--text-xs).

1487 |   font-weight: 600;
     | This sets one look: font-weight becomes 600.

1488 | }
     | This ends that group of paint instructions.

1489 | .focus-status-dot {
     | This starts paint instructions for things that match `.focus-status-dot`.

1490 |   width: 6px;
     | This sets one look: width becomes 6px.

1491 |   height: 6px;
     | This sets one look: height becomes 6px.

1492 |   border-radius: 50%;
     | This sets one look: border-radius becomes 50%.

1493 |   background: currentColor;
     | This sets one look: background becomes currentColor.

1494 | }
     | This ends that group of paint instructions.

1495 | 
     | A blank line in the paint file. It does not change how anything looks.

1496 | /* ── Connectors Page ─────────────────────────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

1497 | .connectors-page { display: flex; flex-direction: column; gap: var(--space-4); }
     | One paint instruction in the big style file.

1498 | 
     | A blank line in the paint file. It does not change how anything looks.

1499 | .connectors-list { display: flex; flex-direction: column; gap: var(--space-3); }
     | One paint instruction in the big style file.

1500 | 
     | A blank line in the paint file. It does not change how anything looks.

1501 | .connector-card {
     | This starts paint instructions for things that match `.connector-card`.

1502 |   display: flex;
     | This sets one look: display becomes flex.

1503 |   align-items: center;
     | This sets one look: align-items becomes center.

1504 |   gap: var(--space-4);
     | This sets one look: gap becomes var(--space-4).

1505 |   background: var(--card);
     | This sets one look: background becomes var(--card).

1506 |   border: 1px solid var(--border);
     | This sets one look: border becomes 1px solid var(--border).

1507 |   border-radius: var(--radius);
     | This sets one look: border-radius becomes var(--radius).

1508 |   padding: var(--space-4) var(--space-5);
     | This sets one look: padding becomes var(--space-4) var(--space-5).

1509 |   transition: border-color 0.15s;
     | This sets one look: transition becomes border-color 0.15s.

1510 | }
     | This ends that group of paint instructions.

1511 | .connector-card:hover { border-color: var(--border-active); }
     | One paint instruction in the big style file.

1512 | 
     | A blank line in the paint file. It does not change how anything looks.

1513 | .connector-card-icon {
     | This starts paint instructions for things that match `.connector-card-icon`.

1514 |   width: 44px;
     | This sets one look: width becomes 44px.

1515 |   height: 44px;
     | This sets one look: height becomes 44px.

1516 |   border-radius: 12px;
     | This sets one look: border-radius becomes 12px.

1517 |   display: flex;
     | This sets one look: display becomes flex.

1518 |   align-items: center;
     | This sets one look: align-items becomes center.

1519 |   justify-content: center;
     | This sets one look: justify-content becomes center.

1520 |   flex-shrink: 0;
     | This sets one look: flex-shrink becomes 0.

1521 | }
     | This ends that group of paint instructions.

1522 | 
     | A blank line in the paint file. It does not change how anything looks.

1523 | .connector-card-body { flex: 1; min-width: 0; }
     | One paint instruction in the big style file.

1524 | .connector-card-title { font-weight: 700; font-size: var(--text-sm); color: var(--text); margin-bottom: 2px; }
     | One paint instruction in the big style file.

1525 | .connector-card-desc { font-size: var(--text-xs); color: var(--muted); line-height: 1.5; }
     | One paint instruction in the big style file.

1526 | .connector-card-meta { font-size: var(--text-xs); color: var(--muted); margin-top: 4px; }
     | One paint instruction in the big style file.

1527 | 
     | A blank line in the paint file. It does not change how anything looks.

1528 | .connector-card-actions { display: flex; gap: var(--space-2); flex-shrink: 0; align-items: center; }
     | One paint instruction in the big style file.

1529 | 
     | A blank line in the paint file. It does not change how anything looks.

1530 | .btn-connector {
     | This starts paint instructions for things that match `.btn-connector`.

1531 |   padding: 8px 16px;
     | This sets one look: padding becomes 8px 16px.

1532 |   border-radius: var(--radius-sm);
     | This sets one look: border-radius becomes var(--radius-sm).

1533 |   font-size: var(--text-xs);
     | This sets one look: font-size becomes var(--text-xs).

1534 |   font-weight: 700;
     | This sets one look: font-weight becomes 700.

1535 |   cursor: pointer;
     | This sets one look: cursor becomes pointer.

1536 |   border: none;
     | This sets one look: border becomes none.

1537 |   font-family: inherit;
     | This sets one look: font-family becomes inherit.

1538 |   transition: all 0.15s;
     | This sets one look: transition becomes all 0.15s.

1539 |   white-space: nowrap;
     | This sets one look: white-space becomes nowrap.

1540 |   min-height: 36px;
     | This sets one look: min-height becomes 36px.

1541 | }
     | This ends that group of paint instructions.

1542 | .btn-connector:disabled { opacity: 0.6; cursor: not-allowed; }
     | One paint instruction in the big style file.

1543 | .btn-connector-connect {
     | This starts paint instructions for things that match `.btn-connector-connect`.

1544 |   background: var(--brand-gradient);
     | This sets one look: background becomes var(--brand-gradient).

1545 |   color: #fff;
     | This sets one look: color becomes #fff.

1546 |   box-shadow: 0 2px 8px rgba(99, 102, 241, 0.3);
     | This sets one look: box-shadow becomes 0 2px 8px rgba(99, 102, 241, 0.3).

1547 | }
     | This ends that group of paint instructions.

1548 | .btn-connector-connect:hover:not(:disabled) { filter: brightness(1.1); }
     | One paint instruction in the big style file.

1549 | .btn-connector-sync {
     | This starts paint instructions for things that match `.btn-connector-sync`.

1550 |   background: var(--indigo-dim);
     | This sets one look: background becomes var(--indigo-dim).

1551 |   color: var(--indigo-light);
     | This sets one look: color becomes var(--indigo-light).

1552 |   border: 1px solid rgba(99, 102, 241, 0.2);
     | This sets one look: border becomes 1px solid rgba(99, 102, 241, 0.2).

1553 | }
     | This ends that group of paint instructions.

1554 | .btn-connector-sync:hover:not(:disabled) { background: rgba(99, 102, 241, 0.2); }
     | One paint instruction in the big style file.

1555 | .btn-connector-disconnect {
     | This starts paint instructions for things that match `.btn-connector-disconnect`.

1556 |   background: transparent;
     | This sets one look: background becomes transparent.

1557 |   color: var(--muted);
     | This sets one look: color becomes var(--muted).

1558 |   border: 1px solid var(--border);
     | This sets one look: border becomes 1px solid var(--border).

1559 | }
     | This ends that group of paint instructions.

1560 | .btn-connector-disconnect:hover { color: var(--red); border-color: var(--red); }
     | One paint instruction in the big style file.

1561 | 
     | A blank line in the paint file. It does not change how anything looks.

1562 | .connectors-toast {
     | This starts paint instructions for things that match `.connectors-toast`.

1563 |   position: fixed;
     | This sets one look: position becomes fixed.

1564 |   top: calc(var(--top-bar-h) + 12px);
     | This sets one look: top becomes calc(var(--top-bar-h) + 12px).

1565 |   right: 20px;
     | This sets one look: right becomes 20px.

1566 |   padding: 10px 18px;
     | This sets one look: padding becomes 10px 18px.

1567 |   border-radius: var(--radius-sm);
     | This sets one look: border-radius becomes var(--radius-sm).

1568 |   font-size: var(--text-sm);
     | This sets one look: font-size becomes var(--text-sm).

1569 |   font-weight: 600;
     | This sets one look: font-weight becomes 600.

1570 |   z-index: 300;
     | This sets one look: z-index becomes 300.

1571 |   box-shadow: var(--shadow);
     | This sets one look: box-shadow becomes var(--shadow).

1572 |   animation: toastIn 0.2s ease;
     | This sets one look: animation becomes toastIn 0.2s ease.

1573 | }
     | This ends that group of paint instructions.

1574 | .connectors-toast--success { background: var(--green); color: #fff; }
     | One paint instruction in the big style file.

1575 | .connectors-toast--error { background: var(--red); color: #fff; }
     | One paint instruction in the big style file.

1576 | 
     | A blank line in the paint file. It does not change how anything looks.

1577 | @keyframes toastIn {
     | This starts a little movie of paint changes. Something else plays it by name.

1578 |   from { opacity: 0; transform: translateY(-8px); }
     | One paint instruction in the big style file.

1579 |   to   { opacity: 1; transform: none; }
     | One paint instruction in the big style file.

1580 | }
     | This ends that group of paint instructions.

1581 | 
     | A blank line in the paint file. It does not change how anything looks.

1582 | /* ── Chart Legend ────────────────────────────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

1583 | .chart-header {
     | This starts paint instructions for things that match `.chart-header`.

1584 |   display: flex;
     | This sets one look: display becomes flex.

1585 |   align-items: center;
     | This sets one look: align-items becomes center.

1586 |   justify-content: space-between;
     | This sets one look: justify-content becomes space-between.

1587 |   flex-wrap: wrap;
     | This sets one look: flex-wrap becomes wrap.

1588 |   gap: 8px;
     | This sets one look: gap becomes 8px.

1589 |   margin-bottom: 12px;
     | This sets one look: margin-bottom becomes 12px.

1590 | }
     | This ends that group of paint instructions.

1591 | .chart-legend {
     | This starts paint instructions for things that match `.chart-legend`.

1592 |   display: flex;
     | This sets one look: display becomes flex.

1593 |   gap: var(--space-4);
     | This sets one look: gap becomes var(--space-4).

1594 |   align-items: center;
     | This sets one look: align-items becomes center.

1595 |   flex-wrap: wrap;
     | This sets one look: flex-wrap becomes wrap.

1596 | }
     | This ends that group of paint instructions.

1597 | .chart-legend-item {
     | This starts paint instructions for things that match `.chart-legend-item`.

1598 |   display: flex;
     | This sets one look: display becomes flex.

1599 |   align-items: center;
     | This sets one look: align-items becomes center.

1600 |   gap: 6px;
     | This sets one look: gap becomes 6px.

1601 |   font-size: var(--text-xs);
     | This sets one look: font-size becomes var(--text-xs).

1602 |   color: var(--muted);
     | This sets one look: color becomes var(--muted).

1603 | }
     | This ends that group of paint instructions.

1604 | .chart-legend-swatch {
     | This starts paint instructions for things that match `.chart-legend-swatch`.

1605 |   width: 16px;
     | This sets one look: width becomes 16px.

1606 |   height: 3px;
     | This sets one look: height becomes 3px.

1607 |   border-radius: 2px;
     | This sets one look: border-radius becomes 2px.

1608 |   flex-shrink: 0;
     | This sets one look: flex-shrink becomes 0.

1609 | }
     | This ends that group of paint instructions.

1610 | 
     | A blank line in the paint file. It does not change how anything looks.

1611 | /* ── Bottom Sheet (mobile slide-up) ──────────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

1612 | .bottom-sheet-overlay {
     | This starts paint instructions for things that match `.bottom-sheet-overlay`.

1613 |   display: none;
     | This sets one look: display becomes none.

1614 |   position: fixed;
     | This sets one look: position becomes fixed.

1615 |   inset: 0;
     | This sets one look: inset becomes 0.

1616 |   background: rgba(0, 0, 0, 0.5);
     | This sets one look: background becomes rgba(0, 0, 0, 0.5).

1617 |   z-index: 149;
     | This sets one look: z-index becomes 149.

1618 |   backdrop-filter: blur(2px);
     | This sets one look: backdrop-filter becomes blur(2px).

1619 | }
     | This ends that group of paint instructions.

1620 | .bottom-sheet {
     | This starts paint instructions for things that match `.bottom-sheet`.

1621 |   display: none;
     | This sets one look: display becomes none.

1622 |   position: fixed;
     | This sets one look: position becomes fixed.

1623 |   bottom: 0;
     | This sets one look: bottom becomes 0.

1624 |   left: 0;
     | This sets one look: left becomes 0.

1625 |   right: 0;
     | This sets one look: right becomes 0.

1626 |   background: var(--surface);
     | This sets one look: background becomes var(--surface).

1627 |   border-radius: 20px 20px 0 0;
     | This sets one look: border-radius becomes 20px 20px 0 0.

1628 |   border-top: 1px solid var(--border);
     | This sets one look: border-top becomes 1px solid var(--border).

1629 |   z-index: 150;
     | This sets one look: z-index becomes 150.

1630 |   transform: translateY(100%);
     | This sets one look: transform becomes translateY(100%).

1631 |   transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
     | This sets one look: transition becomes transform 0.3s cubic-bezier(0.4, 0, 0.2, 1).

1632 |   padding: 0 var(--space-4) env(safe-area-inset-bottom, var(--space-5));
     | This sets one look: padding becomes 0 var(--space-4) env(safe-area-inset-bottom, var(--space-5)).

1633 |   padding-bottom: calc(env(safe-area-inset-bottom, 0px) + var(--space-5));
     | This sets one look: padding-bottom becomes calc(env(safe-area-inset-bottom, 0px) + var(--space-5)).

1634 |   max-height: 85vh;
     | This sets one look: max-height becomes 85vh.

1635 |   overflow-y: auto;
     | This sets one look: overflow-y becomes auto.

1636 |   box-shadow: 0 -4px 24px rgba(0, 0, 0, 0.3);
     | This sets one look: box-shadow becomes 0 -4px 24px rgba(0, 0, 0, 0.3).

1637 | }
     | This ends that group of paint instructions.

1638 | .bottom-sheet.open { transform: translateY(0); }
     | One paint instruction in the big style file.

1639 | .bottom-sheet-handle {
     | This starts paint instructions for things that match `.bottom-sheet-handle`.

1640 |   width: 36px;
     | This sets one look: width becomes 36px.

1641 |   height: 4px;
     | This sets one look: height becomes 4px.

1642 |   border-radius: 2px;
     | This sets one look: border-radius becomes 2px.

1643 |   background: var(--border);
     | This sets one look: background becomes var(--border).

1644 |   margin: 12px auto 16px;
     | This sets one look: margin becomes 12px auto 16px.

1645 |   flex-shrink: 0;
     | This sets one look: flex-shrink becomes 0.

1646 | }
     | This ends that group of paint instructions.

1647 | .bottom-sheet-section {
     | This starts paint instructions for things that match `.bottom-sheet-section`.

1648 |   display: flex;
     | This sets one look: display becomes flex.

1649 |   flex-direction: column;
     | This sets one look: flex-direction becomes column.

1650 |   gap: 1px;
     | This sets one look: gap becomes 1px.

1651 |   padding-bottom: var(--space-3);
     | This sets one look: padding-bottom becomes var(--space-3).

1652 |   margin-bottom: var(--space-2);
     | This sets one look: margin-bottom becomes var(--space-2).

1653 |   border-bottom: 1px solid var(--border);
     | This sets one look: border-bottom becomes 1px solid var(--border).

1654 | }
     | This ends that group of paint instructions.

1655 | .bottom-sheet-section:last-of-type { border-bottom: none; }
     | One paint instruction in the big style file.

1656 | .bottom-sheet-footer {
     | This starts paint instructions for things that match `.bottom-sheet-footer`.

1657 |   display: flex;
     | This sets one look: display becomes flex.

1658 |   flex-direction: column;
     | This sets one look: flex-direction becomes column.

1659 |   gap: var(--space-2);
     | This sets one look: gap becomes var(--space-2).

1660 |   padding: var(--space-3) 0 var(--space-2);
     | This sets one look: padding becomes var(--space-3) 0 var(--space-2).

1661 |   position: sticky;
     | This sets one look: position becomes sticky.

1662 |   bottom: 0;
     | This sets one look: bottom becomes 0.

1663 |   background: var(--surface);
     | This sets one look: background becomes var(--surface).

1664 |   border-top: 1px solid var(--border);
     | This sets one look: border-top becomes 1px solid var(--border).

1665 |   margin-top: var(--space-2);
     | This sets one look: margin-top becomes var(--space-2).

1666 | }
     | This ends that group of paint instructions.

1667 | 
     | A blank line in the paint file. It does not change how anything looks.

1668 | /* Sheet connector rows */
     | A label for people about the next chunk of paint. The browser ignores it.

1669 | .sheet-connectors { display: flex; flex-direction: column; gap: 2px; }
     | One paint instruction in the big style file.

1670 | .sheet-connector-row {
     | This starts paint instructions for things that match `.sheet-connector-row`.

1671 |   display: flex;
     | This sets one look: display becomes flex.

1672 |   align-items: center;
     | This sets one look: align-items becomes center.

1673 |   gap: var(--space-2);
     | This sets one look: gap becomes var(--space-2).

1674 |   padding: 7px 4px;
     | This sets one look: padding becomes 7px 4px.

1675 |   border-radius: var(--radius-sm);
     | This sets one look: border-radius becomes var(--radius-sm).

1676 | }
     | This ends that group of paint instructions.

1677 | .sheet-connector-icon {
     | This starts paint instructions for things that match `.sheet-connector-icon`.

1678 |   display: flex;
     | This sets one look: display becomes flex.

1679 |   align-items: center;
     | This sets one look: align-items becomes center.

1680 |   justify-content: center;
     | This sets one look: justify-content becomes center.

1681 |   width: 26px;
     | This sets one look: width becomes 26px.

1682 |   height: 26px;
     | This sets one look: height becomes 26px.

1683 |   border-radius: 6px;
     | This sets one look: border-radius becomes 6px.

1684 |   flex-shrink: 0;
     | This sets one look: flex-shrink becomes 0.

1685 | }
     | This ends that group of paint instructions.

1686 | .sheet-connector-label {
     | This starts paint instructions for things that match `.sheet-connector-label`.

1687 |   flex: 1;
     | This sets one look: flex becomes 1.

1688 |   font-size: var(--text-sm);
     | This sets one look: font-size becomes var(--text-sm).

1689 |   color: var(--text);
     | This sets one look: color becomes var(--text).

1690 | }
     | This ends that group of paint instructions.

1691 | .sheet-connector-dot {
     | This starts paint instructions for things that match `.sheet-connector-dot`.

1692 |   width: 7px;
     | This sets one look: width becomes 7px.

1693 |   height: 7px;
     | This sets one look: height becomes 7px.

1694 |   border-radius: 50%;
     | This sets one look: border-radius becomes 50%.

1695 |   background: var(--muted);
     | This sets one look: background becomes var(--muted).

1696 |   flex-shrink: 0;
     | This sets one look: flex-shrink becomes 0.

1697 | }
     | This ends that group of paint instructions.

1698 | .sheet-connector-dot.connected { background: #22c55e; }
     | One paint instruction in the big style file.

1699 | .sheet-connector-btn {
     | This starts paint instructions for things that match `.sheet-connector-btn`.

1700 |   font-size: 11px;
     | This sets one look: font-size becomes 11px.

1701 |   padding: 3px 9px;
     | This sets one look: padding becomes 3px 9px.

1702 |   border-radius: var(--radius-sm);
     | This sets one look: border-radius becomes var(--radius-sm).

1703 |   border: 1px solid var(--border);
     | This sets one look: border becomes 1px solid var(--border).

1704 |   background: transparent;
     | This sets one look: background becomes transparent.

1705 |   color: var(--text-muted);
     | This sets one look: color becomes var(--text-muted).

1706 |   cursor: pointer;
     | This sets one look: cursor becomes pointer.

1707 |   font-family: inherit;
     | This sets one look: font-family becomes inherit.

1708 |   transition: all 0.15s;
     | This sets one look: transition becomes all 0.15s.

1709 |   white-space: nowrap;
     | This sets one look: white-space becomes nowrap.

1710 | }
     | This ends that group of paint instructions.

1711 | .sheet-connector-btn:hover { border-color: var(--border-active); color: var(--text); }
     | One paint instruction in the big style file.

1712 | .sheet-connector-btn:disabled { opacity: 0.5; cursor: not-allowed; }
     | One paint instruction in the big style file.

1713 | .sheet-connector-btn--on {
     | This starts paint instructions for things that match `.sheet-connector-btn--on`.

1714 |   border-color: var(--c, var(--indigo));
     | This sets one look: border-color becomes var(--c, var(--indigo)).

1715 |   color: var(--c, var(--indigo));
     | This sets one look: color becomes var(--c, var(--indigo)).

1716 | }
     | This ends that group of paint instructions.

1717 | .sheet-connector-btn--on:hover { background: color-mix(in srgb, var(--c, var(--indigo)) 12%, transparent); }
     | One paint instruction in the big style file.

1718 | .sheet-connector-btn--off { color: var(--red); border-color: transparent; font-size: 14px; padding: 2px 7px; }
     | One paint instruction in the big style file.

1719 | .sheet-connector-btn--off:hover { border-color: var(--red); }
     | One paint instruction in the big style file.

1720 | 
     | A blank line in the paint file. It does not change how anything looks.

1721 | /* ── Scrollbar ───────────────────────────────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

1722 | ::-webkit-scrollbar { width: 6px; }
     | One paint instruction in the big style file.

1723 | ::-webkit-scrollbar-track { background: transparent; }
     | One paint instruction in the big style file.

1724 | ::-webkit-scrollbar-thumb { background: var(--border); border-radius: 3px; }
     | One paint instruction in the big style file.

1725 | ::-webkit-scrollbar-thumb:hover { background: var(--muted); }
     | One paint instruction in the big style file.

1726 | 
     | A blank line in the paint file. It does not change how anything looks.

1727 | /* ── Utility ─────────────────────────────────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

1728 | .flex { display: flex; }
     | One paint instruction in the big style file.

1729 | .flex-col { display: flex; flex-direction: column; }
     | One paint instruction in the big style file.

1730 | .items-center { align-items: center; }
     | One paint instruction in the big style file.

1731 | .justify-between { justify-content: space-between; }
     | One paint instruction in the big style file.

1732 | .gap-1 { gap: var(--space-1); }
     | One paint instruction in the big style file.

1733 | .gap-2 { gap: var(--space-2); }
     | One paint instruction in the big style file.

1734 | .gap-3 { gap: var(--space-3); }
     | One paint instruction in the big style file.

1735 | .gap-4 { gap: var(--space-4); }
     | One paint instruction in the big style file.

1736 | .mb-1 { margin-bottom: var(--space-1); }
     | One paint instruction in the big style file.

1737 | .mb-2 { margin-bottom: var(--space-2); }
     | One paint instruction in the big style file.

1738 | .mb-3 { margin-bottom: var(--space-3); }
     | One paint instruction in the big style file.

1739 | .mb-4 { margin-bottom: var(--space-4); }
     | One paint instruction in the big style file.

1740 | .mt-1 { margin-top: var(--space-1); }
     | One paint instruction in the big style file.

1741 | .mt-2 { margin-top: var(--space-2); }
     | One paint instruction in the big style file.

1742 | .mt-3 { margin-top: var(--space-3); }
     | One paint instruction in the big style file.

1743 | .mt-4 { margin-top: var(--space-4); }
     | One paint instruction in the big style file.

1744 | .text-sm { font-size: var(--text-sm); }
     | One paint instruction in the big style file.

1745 | .text-xs { font-size: var(--text-xs); }
     | One paint instruction in the big style file.

1746 | .text-muted { color: var(--muted); }
     | One paint instruction in the big style file.

1747 | .text-soft { color: var(--text-soft); }
     | One paint instruction in the big style file.

1748 | .font-bold { font-weight: 700; }
     | One paint instruction in the big style file.

1749 | .font-semibold { font-weight: 600; }
     | One paint instruction in the big style file.

1750 | .w-full { width: 100%; }
     | One paint instruction in the big style file.

1751 | .stack { display: flex; flex-direction: column; gap: 12px; }
     | One paint instruction in the big style file.

1752 | .stack-sm { display: flex; flex-direction: column; gap: 8px; }
     | One paint instruction in the big style file.

1753 | 
     | A blank line in the paint file. It does not change how anything looks.

1754 | /* ── Top Bar Avatar ─────────────────────────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

1755 | .top-bar-avatar {
     | This starts paint instructions for things that match `.top-bar-avatar`.

1756 |   width: 32px;
     | This sets one look: width becomes 32px.

1757 |   height: 32px;
     | This sets one look: height becomes 32px.

1758 |   border-radius: 50%;
     | This sets one look: border-radius becomes 50%.

1759 |   background: var(--brand-gradient);
     | This sets one look: background becomes var(--brand-gradient).

1760 |   color: #fff;
     | This sets one look: color becomes #fff.

1761 |   font-size: 12px;
     | This sets one look: font-size becomes 12px.

1762 |   font-weight: 700;
     | This sets one look: font-weight becomes 700.

1763 |   display: flex;
     | This sets one look: display becomes flex.

1764 |   align-items: center;
     | This sets one look: align-items becomes center.

1765 |   justify-content: center;
     | This sets one look: justify-content becomes center.

1766 |   flex-shrink: 0;
     | This sets one look: flex-shrink becomes 0.

1767 |   text-decoration: none;
     | This sets one look: text-decoration becomes none.

1768 |   cursor: pointer;
     | This sets one look: cursor becomes pointer.

1769 |   transition: opacity 0.15s, box-shadow 0.15s;
     | This sets one look: transition becomes opacity 0.15s, box-shadow 0.15s.

1770 |   box-shadow: 0 2px 8px rgba(99, 102, 241, 0.35);
     | This sets one look: box-shadow becomes 0 2px 8px rgba(99, 102, 241, 0.35).

1771 |   letter-spacing: 0.5px;
     | This sets one look: letter-spacing becomes 0.5px.

1772 | }
     | This ends that group of paint instructions.

1773 | .top-bar-avatar:hover { opacity: 0.85; box-shadow: 0 2px 12px rgba(99, 102, 241, 0.55); }
     | One paint instruction in the big style file.

1774 | 
     | A blank line in the paint file. It does not change how anything looks.

1775 | /* ── Profile Settings Page ──────────────────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

1776 | .profile-settings-page {
     | This starts paint instructions for things that match `.profile-settings-page`.

1777 |   flex: 1;
     | This sets one look: flex becomes 1.

1778 |   overflow-y: auto;
     | This sets one look: overflow-y becomes auto.

1779 |   padding: var(--space-6);
     | This sets one look: padding becomes var(--space-6).

1780 | }
     | This ends that group of paint instructions.

1781 | 
     | A blank line in the paint file. It does not change how anything looks.

1782 | .profile-settings-container {
     | This starts paint instructions for things that match `.profile-settings-container`.

1783 |   max-width: 680px;
     | This sets one look: max-width becomes 680px.

1784 |   margin: 0 auto;
     | This sets one look: margin becomes 0 auto.

1785 |   display: flex;
     | This sets one look: display becomes flex.

1786 |   flex-direction: column;
     | This sets one look: flex-direction becomes column.

1787 |   gap: var(--space-5);
     | This sets one look: gap becomes var(--space-5).

1788 | }
     | This ends that group of paint instructions.

1789 | 
     | A blank line in the paint file. It does not change how anything looks.

1790 | .profile-settings-header {
     | This starts paint instructions for things that match `.profile-settings-header`.

1791 |   padding-bottom: var(--space-3);
     | This sets one look: padding-bottom becomes var(--space-3).

1792 | }
     | This ends that group of paint instructions.

1793 | 
     | A blank line in the paint file. It does not change how anything looks.

1794 | .profile-settings-title {
     | This starts paint instructions for things that match `.profile-settings-title`.

1795 |   font-size: var(--text-xl);
     | This sets one look: font-size becomes var(--text-xl).

1796 |   font-weight: 800;
     | This sets one look: font-weight becomes 800.

1797 |   color: var(--text);
     | This sets one look: color becomes var(--text).

1798 |   margin-bottom: var(--space-1);
     | This sets one look: margin-bottom becomes var(--space-1).

1799 | }
     | This ends that group of paint instructions.

1800 | 
     | A blank line in the paint file. It does not change how anything looks.

1801 | .profile-settings-subtitle {
     | This starts paint instructions for things that match `.profile-settings-subtitle`.

1802 |   font-size: var(--text-sm);
     | This sets one look: font-size becomes var(--text-sm).

1803 |   color: var(--muted);
     | This sets one look: color becomes var(--muted).

1804 | }
     | This ends that group of paint instructions.

1805 | 
     | A blank line in the paint file. It does not change how anything looks.

1806 | /* Settings card */
     | A label for people about the next chunk of paint. The browser ignores it.

1807 | .profile-settings-card {
     | This starts paint instructions for things that match `.profile-settings-card`.

1808 |   background: var(--card);
     | This sets one look: background becomes var(--card).

1809 |   border: 1px solid var(--border);
     | This sets one look: border becomes 1px solid var(--border).

1810 |   border-radius: var(--radius);
     | This sets one look: border-radius becomes var(--radius).

1811 |   padding: var(--space-5);
     | This sets one look: padding becomes var(--space-5).

1812 |   display: flex;
     | This sets one look: display becomes flex.

1813 |   flex-direction: column;
     | This sets one look: flex-direction becomes column.

1814 |   gap: var(--space-4);
     | This sets one look: gap becomes var(--space-4).

1815 | }
     | This ends that group of paint instructions.

1816 | 
     | A blank line in the paint file. It does not change how anything looks.

1817 | .profile-settings-card-header {
     | This starts paint instructions for things that match `.profile-settings-card-header`.

1818 |   border-bottom: 1px solid var(--border);
     | This sets one look: border-bottom becomes 1px solid var(--border).

1819 |   padding-bottom: var(--space-3);
     | This sets one look: padding-bottom becomes var(--space-3).

1820 | }
     | This ends that group of paint instructions.

1821 | 
     | A blank line in the paint file. It does not change how anything looks.

1822 | .profile-settings-card-title {
     | This starts paint instructions for things that match `.profile-settings-card-title`.

1823 |   font-size: var(--text-base);
     | This sets one look: font-size becomes var(--text-base).

1824 |   font-weight: 700;
     | This sets one look: font-weight becomes 700.

1825 |   color: var(--text);
     | This sets one look: color becomes var(--text).

1826 | }
     | This ends that group of paint instructions.

1827 | 
     | A blank line in the paint file. It does not change how anything looks.

1828 | .profile-settings-card-desc {
     | This starts paint instructions for things that match `.profile-settings-card-desc`.

1829 |   font-size: var(--text-xs);
     | This sets one look: font-size becomes var(--text-xs).

1830 |   color: var(--muted);
     | This sets one look: color becomes var(--muted).

1831 |   margin-top: var(--space-1);
     | This sets one look: margin-top becomes var(--space-1).

1832 | }
     | This ends that group of paint instructions.

1833 | 
     | A blank line in the paint file. It does not change how anything looks.

1834 | /* Avatar row */
     | A label for people about the next chunk of paint. The browser ignores it.

1835 | .profile-avatar-row {
     | This starts paint instructions for things that match `.profile-avatar-row`.

1836 |   display: flex;
     | This sets one look: display becomes flex.

1837 |   align-items: center;
     | This sets one look: align-items becomes center.

1838 |   gap: var(--space-4);
     | This sets one look: gap becomes var(--space-4).

1839 | }
     | This ends that group of paint instructions.

1840 | 
     | A blank line in the paint file. It does not change how anything looks.

1841 | .profile-avatar {
     | This starts paint instructions for things that match `.profile-avatar`.

1842 |   width: 60px;
     | This sets one look: width becomes 60px.

1843 |   height: 60px;
     | This sets one look: height becomes 60px.

1844 |   border-radius: 50%;
     | This sets one look: border-radius becomes 50%.

1845 |   background: var(--brand-gradient);
     | This sets one look: background becomes var(--brand-gradient).

1846 |   color: #fff;
     | This sets one look: color becomes #fff.

1847 |   font-size: 22px;
     | This sets one look: font-size becomes 22px.

1848 |   font-weight: 800;
     | This sets one look: font-weight becomes 800.

1849 |   display: flex;
     | This sets one look: display becomes flex.

1850 |   align-items: center;
     | This sets one look: align-items becomes center.

1851 |   justify-content: center;
     | This sets one look: justify-content becomes center.

1852 |   flex-shrink: 0;
     | This sets one look: flex-shrink becomes 0.

1853 |   box-shadow: 0 4px 16px rgba(99, 102, 241, 0.35);
     | This sets one look: box-shadow becomes 0 4px 16px rgba(99, 102, 241, 0.35).

1854 |   letter-spacing: 1px;
     | This sets one look: letter-spacing becomes 1px.

1855 | }
     | This ends that group of paint instructions.

1856 | 
     | A blank line in the paint file. It does not change how anything looks.

1857 | .profile-avatar-name {
     | This starts paint instructions for things that match `.profile-avatar-name`.

1858 |   font-size: var(--text-base);
     | This sets one look: font-size becomes var(--text-base).

1859 |   font-weight: 600;
     | This sets one look: font-weight becomes 600.

1860 |   color: var(--text);
     | This sets one look: color becomes var(--text).

1861 | }
     | This ends that group of paint instructions.

1862 | 
     | A blank line in the paint file. It does not change how anything looks.

1863 | .profile-avatar-email {
     | This starts paint instructions for things that match `.profile-avatar-email`.

1864 |   font-size: var(--text-xs);
     | This sets one look: font-size becomes var(--text-xs).

1865 |   color: var(--muted);
     | This sets one look: color becomes var(--muted).

1866 |   margin-top: 2px;
     | This sets one look: margin-top becomes 2px.

1867 | }
     | This ends that group of paint instructions.

1868 | 
     | A blank line in the paint file. It does not change how anything looks.

1869 | /* Form */
     | A label for people about the next chunk of paint. The browser ignores it.

1870 | .profile-form {
     | This starts paint instructions for things that match `.profile-form`.

1871 |   display: flex;
     | This sets one look: display becomes flex.

1872 |   flex-direction: column;
     | This sets one look: flex-direction becomes column.

1873 |   gap: var(--space-4);
     | This sets one look: gap becomes var(--space-4).

1874 | }
     | This ends that group of paint instructions.

1875 | 
     | A blank line in the paint file. It does not change how anything looks.

1876 | .profile-form-grid {
     | This starts paint instructions for things that match `.profile-form-grid`.

1877 |   display: grid;
     | This sets one look: display becomes grid.

1878 |   grid-template-columns: 1fr 1fr;
     | This sets one look: grid-template-columns becomes 1fr 1fr.

1879 |   gap: var(--space-4);
     | This sets one look: gap becomes var(--space-4).

1880 | }
     | This ends that group of paint instructions.

1881 | 
     | A blank line in the paint file. It does not change how anything looks.

1882 | .profile-form-grid--single {
     | This starts paint instructions for things that match `.profile-form-grid--single`.

1883 |   grid-template-columns: 1fr;
     | This sets one look: grid-template-columns becomes 1fr.

1884 | }
     | This ends that group of paint instructions.

1885 | 
     | A blank line in the paint file. It does not change how anything looks.

1886 | .profile-form-field {
     | This starts paint instructions for things that match `.profile-form-field`.

1887 |   display: flex;
     | This sets one look: display becomes flex.

1888 |   flex-direction: column;
     | This sets one look: flex-direction becomes column.

1889 |   gap: var(--space-1);
     | This sets one look: gap becomes var(--space-1).

1890 | }
     | This ends that group of paint instructions.

1891 | 
     | A blank line in the paint file. It does not change how anything looks.

1892 | .profile-form-label {
     | This starts paint instructions for things that match `.profile-form-label`.

1893 |   font-size: var(--text-xs);
     | This sets one look: font-size becomes var(--text-xs).

1894 |   font-weight: 600;
     | This sets one look: font-weight becomes 600.

1895 |   color: var(--text-soft);
     | This sets one look: color becomes var(--text-soft).

1896 |   text-transform: uppercase;
     | This sets one look: text-transform becomes uppercase.

1897 |   letter-spacing: 0.6px;
     | This sets one look: letter-spacing becomes 0.6px.

1898 | }
     | This ends that group of paint instructions.

1899 | 
     | A blank line in the paint file. It does not change how anything looks.

1900 | .profile-form-input {
     | This starts paint instructions for things that match `.profile-form-input`.

1901 |   width: 100%;
     | This sets one look: width becomes 100%.

1902 |   padding: 9px 12px;
     | This sets one look: padding becomes 9px 12px.

1903 |   border: 1px solid var(--border);
     | This sets one look: border becomes 1px solid var(--border).

1904 |   border-radius: var(--radius-sm);
     | This sets one look: border-radius becomes var(--radius-sm).

1905 |   background: var(--surface);
     | This sets one look: background becomes var(--surface).

1906 |   color: var(--text);
     | This sets one look: color becomes var(--text).

1907 |   font-size: var(--text-sm);
     | This sets one look: font-size becomes var(--text-sm).

1908 |   font-family: inherit;
     | This sets one look: font-family becomes inherit.

1909 |   transition: border-color 0.15s;
     | This sets one look: transition becomes border-color 0.15s.

1910 | }
     | This ends that group of paint instructions.

1911 | 
     | A blank line in the paint file. It does not change how anything looks.

1912 | .profile-form-input:focus {
     | This starts paint instructions for things that match `.profile-form-input:focus`.

1913 |   outline: none;
     | This sets one look: outline becomes none.

1914 |   border-color: var(--border-active);
     | This sets one look: border-color becomes var(--border-active).

1915 | }
     | This ends that group of paint instructions.

1916 | 
     | A blank line in the paint file. It does not change how anything looks.

1917 | .profile-form-select {
     | This starts paint instructions for things that match `.profile-form-select`.

1918 |   cursor: pointer;
     | This sets one look: cursor becomes pointer.

1919 |   appearance: none;
     | This sets one look: appearance becomes none.

1920 |   background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8' viewBox='0 0 12 8'%3E%3Cpath d='M1 1l5 5 5-5' stroke='%239898be' stroke-width='1.5' fill='none' stroke-linecap='round'/%3E%3C/svg%3E");
     | This sets one look: background-image becomes url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8' viewBox='0 0 12 8'%3E%3Cpath d='M1 1l5 5 5-5' stroke='%239898be' stroke-width='1.5' fill='none' stroke-linecap='round'/%3E%3C/svg%3E").

1921 |   background-repeat: no-repeat;
     | This sets one look: background-repeat becomes no-repeat.

1922 |   background-position: right 12px center;
     | This sets one look: background-position becomes right 12px center.

1923 |   padding-right: 36px;
     | This sets one look: padding-right becomes 36px.

1924 | }
     | This ends that group of paint instructions.

1925 | 
     | A blank line in the paint file. It does not change how anything looks.

1926 | .profile-form-actions {
     | This starts paint instructions for things that match `.profile-form-actions`.

1927 |   display: flex;
     | This sets one look: display becomes flex.

1928 |   justify-content: flex-end;
     | This sets one look: justify-content becomes flex-end.

1929 | }
     | This ends that group of paint instructions.

1930 | 
     | A blank line in the paint file. It does not change how anything looks.

1931 | .profile-save-btn {
     | This starts paint instructions for things that match `.profile-save-btn`.

1932 |   padding: 9px 22px;
     | This sets one look: padding becomes 9px 22px.

1933 |   border-radius: var(--radius-sm);
     | This sets one look: border-radius becomes var(--radius-sm).

1934 |   border: none;
     | This sets one look: border becomes none.

1935 |   background: var(--violet);
     | This sets one look: background becomes var(--violet).

1936 |   color: #fff;
     | This sets one look: color becomes #fff.

1937 |   font-size: var(--text-sm);
     | This sets one look: font-size becomes var(--text-sm).

1938 |   font-weight: 600;
     | This sets one look: font-weight becomes 600.

1939 |   font-family: inherit;
     | This sets one look: font-family becomes inherit.

1940 |   cursor: pointer;
     | This sets one look: cursor becomes pointer.

1941 |   transition: opacity 0.15s;
     | This sets one look: transition becomes opacity 0.15s.

1942 | }
     | This ends that group of paint instructions.

1943 | 
     | A blank line in the paint file. It does not change how anything looks.

1944 | .profile-save-btn:hover { opacity: 0.88; }
     | One paint instruction in the big style file.

1945 | .profile-save-btn:disabled { opacity: 0.5; cursor: not-allowed; }
     | One paint instruction in the big style file.

1946 | 
     | A blank line in the paint file. It does not change how anything looks.

1947 | /* Feedback messages */
     | A label for people about the next chunk of paint. The browser ignores it.

1948 | .profile-msg {
     | This starts paint instructions for things that match `.profile-msg`.

1949 |   font-size: var(--text-sm);
     | This sets one look: font-size becomes var(--text-sm).

1950 |   padding: 9px 12px;
     | This sets one look: padding becomes 9px 12px.

1951 |   border-radius: var(--radius-sm);
     | This sets one look: border-radius becomes var(--radius-sm).

1952 |   border: 1px solid transparent;
     | This sets one look: border becomes 1px solid transparent.

1953 | }
     | This ends that group of paint instructions.

1954 | 
     | A blank line in the paint file. It does not change how anything looks.

1955 | .profile-msg--success {
     | This starts paint instructions for things that match `.profile-msg--success`.

1956 |   background: var(--green-dim);
     | This sets one look: background becomes var(--green-dim).

1957 |   border-color: rgba(16, 185, 129, 0.3);
     | This sets one look: border-color becomes rgba(16, 185, 129, 0.3).

1958 |   color: var(--green);
     | This sets one look: color becomes var(--green).

1959 | }
     | This ends that group of paint instructions.

1960 | 
     | A blank line in the paint file. It does not change how anything looks.

1961 | .profile-msg--error {
     | This starts paint instructions for things that match `.profile-msg--error`.

1962 |   background: var(--red-dim);
     | This sets one look: background becomes var(--red-dim).

1963 |   border-color: rgba(239, 68, 68, 0.3);
     | This sets one look: border-color becomes rgba(239, 68, 68, 0.3).

1964 |   color: var(--red);
     | This sets one look: color becomes var(--red).

1965 | }
     | This ends that group of paint instructions.

1966 | 
     | A blank line in the paint file. It does not change how anything looks.

1967 | /* Theme Picker */
     | A label for people about the next chunk of paint. The browser ignores it.

1968 | .theme-picker {
     | This starts paint instructions for things that match `.theme-picker`.

1969 |   display: grid;
     | This sets one look: display becomes grid.

1970 |   grid-template-columns: 1fr 1fr;
     | This sets one look: grid-template-columns becomes 1fr 1fr.

1971 |   gap: var(--space-3);
     | This sets one look: gap becomes var(--space-3).

1972 | }
     | This ends that group of paint instructions.

1973 | 
     | A blank line in the paint file. It does not change how anything looks.

1974 | .theme-option {
     | This starts paint instructions for things that match `.theme-option`.

1975 |   position: relative;
     | This sets one look: position becomes relative.

1976 |   display: flex;
     | This sets one look: display becomes flex.

1977 |   flex-direction: column;
     | This sets one look: flex-direction becomes column.

1978 |   gap: var(--space-3);
     | This sets one look: gap becomes var(--space-3).

1979 |   padding: var(--space-4);
     | This sets one look: padding becomes var(--space-4).

1980 |   border: 2px solid var(--border);
     | This sets one look: border becomes 2px solid var(--border).

1981 |   border-radius: var(--radius);
     | This sets one look: border-radius becomes var(--radius).

1982 |   background: var(--surface);
     | This sets one look: background becomes var(--surface).

1983 |   cursor: pointer;
     | This sets one look: cursor becomes pointer.

1984 |   transition: border-color 0.15s, background 0.15s;
     | This sets one look: transition becomes border-color 0.15s, background 0.15s.

1985 |   text-align: left;
     | This sets one look: text-align becomes left.

1986 |   font-family: inherit;
     | This sets one look: font-family becomes inherit.

1987 | }
     | This ends that group of paint instructions.

1988 | 
     | A blank line in the paint file. It does not change how anything looks.

1989 | .theme-option:hover { border-color: var(--indigo-light); }
     | One paint instruction in the big style file.

1990 | .theme-option.active { border-color: var(--indigo); background: var(--indigo-dim); }
     | One paint instruction in the big style file.

1991 | .theme-option:disabled { opacity: 0.6; cursor: not-allowed; }
     | One paint instruction in the big style file.

1992 | 
     | A blank line in the paint file. It does not change how anything looks.

1993 | .theme-option-preview {
     | This starts paint instructions for things that match `.theme-option-preview`.

1994 |   width: 100%;
     | This sets one look: width becomes 100%.

1995 |   height: 72px;
     | This sets one look: height becomes 72px.

1996 |   border-radius: var(--radius-sm);
     | This sets one look: border-radius becomes var(--radius-sm).

1997 |   overflow: hidden;
     | This sets one look: overflow becomes hidden.

1998 |   display: flex;
     | This sets one look: display becomes flex.

1999 |   flex-direction: column;
     | This sets one look: flex-direction becomes column.

2000 |   gap: 5px;
     | This sets one look: gap becomes 5px.

2001 |   padding: 8px;
     | This sets one look: padding becomes 8px.

2002 | }
     | This ends that group of paint instructions.

2003 | 
     | A blank line in the paint file. It does not change how anything looks.

2004 | .theme-option-preview--dark {
     | This starts paint instructions for things that match `.theme-option-preview--dark`.

2005 |   background: #0d0d18;
     | This sets one look: background becomes #0d0d18.

2006 |   border: 1px solid rgba(255, 255, 255, 0.08);
     | This sets one look: border becomes 1px solid rgba(255, 255, 255, 0.08).

2007 | }
     | This ends that group of paint instructions.

2008 | 
     | A blank line in the paint file. It does not change how anything looks.

2009 | .theme-option-preview--light {
     | This starts paint instructions for things that match `.theme-option-preview--light`.

2010 |   background: #f5f4ff;
     | This sets one look: background becomes #f5f4ff.

2011 |   border: 1px solid rgba(0, 0, 0, 0.08);
     | This sets one look: border becomes 1px solid rgba(0, 0, 0, 0.08).

2012 | }
     | This ends that group of paint instructions.

2013 | 
     | A blank line in the paint file. It does not change how anything looks.

2014 | .theme-preview-bar {
     | This starts paint instructions for things that match `.theme-preview-bar`.

2015 |   height: 10px;
     | This sets one look: height becomes 10px.

2016 |   border-radius: 4px;
     | This sets one look: border-radius becomes 4px.

2017 |   width: 60%;
     | This sets one look: width becomes 60%.

2018 | }
     | This ends that group of paint instructions.

2019 | 
     | A blank line in the paint file. It does not change how anything looks.

2020 | .theme-option-preview--dark .theme-preview-bar { background: rgba(255,255,255,0.15); }
     | One paint instruction in the big style file.

2021 | .theme-option-preview--light .theme-preview-bar { background: rgba(0,0,0,0.12); }
     | One paint instruction in the big style file.

2022 | 
     | A blank line in the paint file. It does not change how anything looks.

2023 | .theme-preview-card {
     | This starts paint instructions for things that match `.theme-preview-card`.

2024 |   height: 18px;
     | This sets one look: height becomes 18px.

2025 |   border-radius: 4px;
     | This sets one look: border-radius becomes 4px.

2026 |   width: 100%;
     | This sets one look: width becomes 100%.

2027 | }
     | This ends that group of paint instructions.

2028 | 
     | A blank line in the paint file. It does not change how anything looks.

2029 | .theme-preview-card--sm { width: 70%; }
     | One paint instruction in the big style file.

2030 | .theme-option-preview--dark .theme-preview-card { background: #1c1c2e; }
     | One paint instruction in the big style file.

2031 | .theme-option-preview--light .theme-preview-card { background: #ffffff; border: 1px solid rgba(0,0,0,0.06); }
     | One paint instruction in the big style file.

2032 | 
     | A blank line in the paint file. It does not change how anything looks.

2033 | .theme-option-label {
     | This starts paint instructions for things that match `.theme-option-label`.

2034 |   display: flex;
     | This sets one look: display becomes flex.

2035 |   flex-direction: column;
     | This sets one look: flex-direction becomes column.

2036 |   gap: 2px;
     | This sets one look: gap becomes 2px.

2037 | }
     | This ends that group of paint instructions.

2038 | 
     | A blank line in the paint file. It does not change how anything looks.

2039 | .theme-option-name {
     | This starts paint instructions for things that match `.theme-option-name`.

2040 |   font-size: var(--text-sm);
     | This sets one look: font-size becomes var(--text-sm).

2041 |   font-weight: 600;
     | This sets one look: font-weight becomes 600.

2042 |   color: var(--text);
     | This sets one look: color becomes var(--text).

2043 | }
     | This ends that group of paint instructions.

2044 | 
     | A blank line in the paint file. It does not change how anything looks.

2045 | .theme-option-desc {
     | This starts paint instructions for things that match `.theme-option-desc`.

2046 |   font-size: var(--text-xs);
     | This sets one look: font-size becomes var(--text-xs).

2047 |   color: var(--muted);
     | This sets one look: color becomes var(--muted).

2048 | }
     | This ends that group of paint instructions.

2049 | 
     | A blank line in the paint file. It does not change how anything looks.

2050 | .theme-option-check {
     | This starts paint instructions for things that match `.theme-option-check`.

2051 |   position: absolute;
     | This sets one look: position becomes absolute.

2052 |   top: 10px;
     | This sets one look: top becomes 10px.

2053 |   right: 12px;
     | This sets one look: right becomes 12px.

2054 |   color: var(--indigo-light);
     | This sets one look: color becomes var(--indigo-light).

2055 |   font-size: 15px;
     | This sets one look: font-size becomes 15px.

2056 |   font-weight: 700;
     | This sets one look: font-weight becomes 700.

2057 | }
     | This ends that group of paint instructions.

2058 | 
     | A blank line in the paint file. It does not change how anything looks.

2059 | /* ── Profile Settings Responsive ────────────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

2060 | @media (max-width: 768px) {
     | This says: only use the next paint rules when the screen is a certain size.

2061 |   .profile-settings-page {
     | This starts paint instructions for things that match `.profile-settings-page`.

2062 |     padding: var(--space-4) var(--space-4);
     | This sets one look: padding becomes var(--space-4) var(--space-4).

2063 |   }
     | This ends that group of paint instructions.

2064 | 
     | A blank line in the paint file. It does not change how anything looks.

2065 |   .profile-settings-card {
     | This starts paint instructions for things that match `.profile-settings-card`.

2066 |     padding: var(--space-4);
     | This sets one look: padding becomes var(--space-4).

2067 |     border-radius: var(--radius-sm);
     | This sets one look: border-radius becomes var(--radius-sm).

2068 |   }
     | This ends that group of paint instructions.

2069 | 
     | A blank line in the paint file. It does not change how anything looks.

2070 |   .profile-form-grid {
     | This starts paint instructions for things that match `.profile-form-grid`.

2071 |     grid-template-columns: 1fr;
     | This sets one look: grid-template-columns becomes 1fr.

2072 |   }
     | This ends that group of paint instructions.

2073 | 
     | A blank line in the paint file. It does not change how anything looks.

2074 |   .theme-picker {
     | This starts paint instructions for things that match `.theme-picker`.

2075 |     grid-template-columns: 1fr 1fr;
     | This sets one look: grid-template-columns becomes 1fr 1fr.

2076 |     gap: var(--space-2);
     | This sets one look: gap becomes var(--space-2).

2077 |   }
     | This ends that group of paint instructions.

2078 | 
     | A blank line in the paint file. It does not change how anything looks.

2079 |   .theme-option {
     | This starts paint instructions for things that match `.theme-option`.

2080 |     padding: var(--space-3);
     | This sets one look: padding becomes var(--space-3).

2081 |   }
     | This ends that group of paint instructions.

2082 | 
     | A blank line in the paint file. It does not change how anything looks.

2083 |   .theme-option-preview {
     | This starts paint instructions for things that match `.theme-option-preview`.

2084 |     height: 56px;
     | This sets one look: height becomes 56px.

2085 |   }
     | This ends that group of paint instructions.

2086 | 
     | A blank line in the paint file. It does not change how anything looks.

2087 |   .profile-avatar {
     | This starts paint instructions for things that match `.profile-avatar`.

2088 |     width: 48px;
     | This sets one look: width becomes 48px.

2089 |     height: 48px;
     | This sets one look: height becomes 48px.

2090 |     font-size: 18px;
     | This sets one look: font-size becomes 18px.

2091 |   }
     | This ends that group of paint instructions.

2092 | }
     | This ends that group of paint instructions.

2093 | 
     | A blank line in the paint file. It does not change how anything looks.

2094 | @media (max-width: 480px) {
     | This says: only use the next paint rules when the screen is a certain size.

2095 |   .profile-settings-page {
     | This starts paint instructions for things that match `.profile-settings-page`.

2096 |     padding: var(--space-3);
     | This sets one look: padding becomes var(--space-3).

2097 |   }
     | This ends that group of paint instructions.

2098 | 
     | A blank line in the paint file. It does not change how anything looks.

2099 |   .theme-picker {
     | This starts paint instructions for things that match `.theme-picker`.

2100 |     grid-template-columns: 1fr;
     | This sets one look: grid-template-columns becomes 1fr.

2101 |   }
     | This ends that group of paint instructions.

2102 | 
     | A blank line in the paint file. It does not change how anything looks.

2103 |   .profile-form-actions {
     | This starts paint instructions for things that match `.profile-form-actions`.

2104 |     justify-content: stretch;
     | This sets one look: justify-content becomes stretch.

2105 |   }
     | This ends that group of paint instructions.

2106 | 
     | A blank line in the paint file. It does not change how anything looks.

2107 |   .profile-save-btn {
     | This starts paint instructions for things that match `.profile-save-btn`.

2108 |     width: 100%;
     | This sets one look: width becomes 100%.

2109 |     text-align: center;
     | This sets one look: text-align becomes center.

2110 |   }
     | This ends that group of paint instructions.

2111 | }
     | This ends that group of paint instructions.

2112 | 
     | A blank line in the paint file. It does not change how anything looks.

2113 | /* ═══════════════════════════════════════════════════════
     | A label for people about the next chunk of paint. The browser ignores it.

2114 |    FOCUS SHIELD — website blocking / whitelisting UI
     | One paint instruction in the big style file.

2115 |    ═══════════════════════════════════════════════════════ */
     | A label for people about the next chunk of paint. The browser ignores it.

2116 | 
     | A blank line in the paint file. It does not change how anything looks.

2117 | /* Toggle switch — shared by master toggle + per-row enable switch */
     | A label for people about the next chunk of paint. The browser ignores it.

2118 | .fs-toggle {
     | This starts paint instructions for things that match `.fs-toggle`.

2119 |   width: 44px;
     | This sets one look: width becomes 44px.

2120 |   height: 24px;
     | This sets one look: height becomes 24px.

2121 |   min-width: 44px;
     | This sets one look: min-width becomes 44px.

2122 |   border-radius: 12px;
     | This sets one look: border-radius becomes 12px.

2123 |   border: none;
     | This sets one look: border becomes none.

2124 |   cursor: pointer;
     | This sets one look: cursor becomes pointer.

2125 |   background: var(--border);
     | This sets one look: background becomes var(--border).

2126 |   position: relative;
     | This sets one look: position becomes relative.

2127 |   transition: background 0.2s;
     | This sets one look: transition becomes background 0.2s.

2128 |   flex-shrink: 0;
     | This sets one look: flex-shrink becomes 0.

2129 |   padding: 0;
     | This sets one look: padding becomes 0.

2130 | }
     | This ends that group of paint instructions.

2131 | .fs-toggle[data-checked] { background: var(--indigo); }
     | One paint instruction in the big style file.

2132 | .fs-toggle:disabled { opacity: 0.5; cursor: not-allowed; }
     | One paint instruction in the big style file.

2133 | .fs-toggle-knob {
     | This starts paint instructions for things that match `.fs-toggle-knob`.

2134 |   position: absolute;
     | This sets one look: position becomes absolute.

2135 |   top: 3px;
     | This sets one look: top becomes 3px.

2136 |   left: 3px;
     | This sets one look: left becomes 3px.

2137 |   width: 18px;
     | This sets one look: width becomes 18px.

2138 |   height: 18px;
     | This sets one look: height becomes 18px.

2139 |   border-radius: 50%;
     | This sets one look: border-radius becomes 50%.

2140 |   background: #fff;
     | This sets one look: background becomes #fff.

2141 |   transition: left 0.2s;
     | This sets one look: transition becomes left 0.2s.

2142 |   display: block;
     | This sets one look: display becomes block.

2143 | }
     | This ends that group of paint instructions.

2144 | .fs-toggle[data-checked] .fs-toggle-knob { left: 23px; }
     | One paint instruction in the big style file.

2145 | 
     | A blank line in the paint file. It does not change how anything looks.

2146 | /* Status card + pill (dashboard card, session panel, page header) */
     | A label for people about the next chunk of paint. The browser ignores it.

2147 | .fs-status-card { display: flex; flex-direction: column; }
     | One paint instruction in the big style file.

2148 | .fs-status-card-header { display: flex; align-items: center; justify-content: space-between; gap: 10px; flex-wrap: wrap; }
     | One paint instruction in the big style file.

2149 | .fs-status-pill {
     | This starts paint instructions for things that match `.fs-status-pill`.

2150 |   display: inline-flex;
     | This sets one look: display becomes inline-flex.

2151 |   align-items: center;
     | This sets one look: align-items becomes center.

2152 |   gap: 6px;
     | This sets one look: gap becomes 6px.

2153 |   padding: 4px 10px;
     | This sets one look: padding becomes 4px 10px.

2154 |   border-radius: 20px;
     | This sets one look: border-radius becomes 20px.

2155 |   font-size: var(--text-xs);
     | This sets one look: font-size becomes var(--text-xs).

2156 |   font-weight: 700;
     | This sets one look: font-weight becomes 700.

2157 |   white-space: nowrap;
     | This sets one look: white-space becomes nowrap.

2158 | }
     | This ends that group of paint instructions.

2159 | .fs-status-pill--off { background: var(--border); color: var(--muted); }
     | One paint instruction in the big style file.

2160 | .fs-status-pill--armed { background: var(--indigo-dim); color: var(--indigo-light); }
     | One paint instruction in the big style file.

2161 | .fs-status-pill--active { background: var(--green-dim); color: var(--green); }
     | One paint instruction in the big style file.

2162 | .fs-status-pill--paused { background: var(--amber-dim); color: var(--amber); }
     | One paint instruction in the big style file.

2163 | .fs-status-dot { width: 7px; height: 7px; border-radius: 50%; background: currentColor; flex-shrink: 0; }
     | One paint instruction in the big style file.

2164 | .fs-dashboard-counts { display: flex; gap: var(--space-5); }
     | One paint instruction in the big style file.

2165 | .fs-session-site-list {
     | This starts paint instructions for things that match `.fs-session-site-list`.

2166 |   list-style: none;
     | This sets one look: list-style becomes none.

2167 |   display: flex;
     | This sets one look: display becomes flex.

2168 |   flex-direction: column;
     | This sets one look: flex-direction becomes column.

2169 |   gap: 4px;
     | This sets one look: gap becomes 4px.

2170 |   font-size: var(--text-sm);
     | This sets one look: font-size becomes var(--text-sm).

2171 |   color: var(--text-soft);
     | This sets one look: color becomes var(--text-soft).

2172 |   margin-bottom: 12px;
     | This sets one look: margin-bottom becomes 12px.

2173 | }
     | This ends that group of paint instructions.

2174 | .fs-session-site-list li::before { content: "🚫 "; }
     | One paint instruction in the big style file.

2175 | 
     | A blank line in the paint file. It does not change how anything looks.

2176 | /* Pause control */
     | A label for people about the next chunk of paint. The browser ignores it.

2177 | .fs-pause-banner {
     | This starts paint instructions for things that match `.fs-pause-banner`.

2178 |   display: flex;
     | This sets one look: display becomes flex.

2179 |   align-items: center;
     | This sets one look: align-items becomes center.

2180 |   justify-content: space-between;
     | This sets one look: justify-content becomes space-between.

2181 |   gap: 10px;
     | This sets one look: gap becomes 10px.

2182 |   flex-wrap: wrap;
     | This sets one look: flex-wrap becomes wrap.

2183 |   padding: 10px 14px;
     | This sets one look: padding becomes 10px 14px.

2184 |   border-radius: var(--radius-sm);
     | This sets one look: border-radius becomes var(--radius-sm).

2185 |   background: var(--amber-dim);
     | This sets one look: background becomes var(--amber-dim).

2186 |   border: 1px solid rgba(245, 158, 11, 0.25);
     | This sets one look: border becomes 1px solid rgba(245, 158, 11, 0.25).

2187 |   color: var(--text);
     | This sets one look: color becomes var(--text).

2188 |   font-size: var(--text-sm);
     | This sets one look: font-size becomes var(--text-sm).

2189 |   font-weight: 600;
     | This sets one look: font-weight becomes 600.

2190 | }
     | This ends that group of paint instructions.

2191 | .fs-pause-row { display: flex; gap: 8px; flex-wrap: wrap; }
     | One paint instruction in the big style file.

2192 | .fs-pause-custom { display: flex; align-items: center; gap: 8px; margin-top: 10px; flex-wrap: wrap; }
     | One paint instruction in the big style file.

2193 | 
     | A blank line in the paint file. It does not change how anything looks.

2194 | /* Page header with autosave indicator */
     | A label for people about the next chunk of paint. The browser ignores it.

2195 | .fs-page-header { display: flex; align-items: flex-start; justify-content: space-between; gap: 12px; flex-wrap: wrap; }
     | One paint instruction in the big style file.

2196 | .fs-save-indicator { font-size: var(--text-xs); color: var(--muted); white-space: nowrap; padding-top: 4px; }
     | One paint instruction in the big style file.

2197 | 
     | A blank line in the paint file. It does not change how anything looks.

2198 | /* Section header with inline "Add website" action */
     | A label for people about the next chunk of paint. The browser ignores it.

2199 | .fs-section-header { display: flex; align-items: flex-start; justify-content: space-between; gap: 12px; flex-wrap: wrap; }
     | One paint instruction in the big style file.

2200 | 
     | A blank line in the paint file. It does not change how anything looks.

2201 | /* Search + bulk toolbar */
     | A label for people about the next chunk of paint. The browser ignores it.

2202 | .fs-toolbar { display: flex; align-items: center; justify-content: space-between; gap: 10px; flex-wrap: wrap; }
     | One paint instruction in the big style file.

2203 | .fs-bulk-toolbar { display: flex; align-items: center; gap: 6px; flex-wrap: wrap; }
     | One paint instruction in the big style file.

2204 | 
     | A blank line in the paint file. It does not change how anything looks.

2205 | /* Website rows */
     | A label for people about the next chunk of paint. The browser ignores it.

2206 | .fs-row-list { display: flex; flex-direction: column; gap: 6px; }
     | One paint instruction in the big style file.

2207 | .fs-row {
     | This starts paint instructions for things that match `.fs-row`.

2208 |   display: flex;
     | This sets one look: display becomes flex.

2209 |   align-items: center;
     | This sets one look: align-items becomes center.

2210 |   gap: 12px;
     | This sets one look: gap becomes 12px.

2211 |   padding: 10px 12px;
     | This sets one look: padding becomes 10px 12px.

2212 |   border: 1px solid var(--border);
     | This sets one look: border becomes 1px solid var(--border).

2213 |   border-radius: var(--radius-sm);
     | This sets one look: border-radius becomes var(--radius-sm).

2214 |   background: var(--surface);
     | This sets one look: background becomes var(--surface).

2215 |   flex-wrap: wrap;
     | This sets one look: flex-wrap becomes wrap.

2216 |   transition: border-color 0.15s;
     | This sets one look: transition becomes border-color 0.15s.

2217 | }
     | This ends that group of paint instructions.

2218 | .fs-row--selected { border-color: var(--border-active); background: var(--indigo-dim); }
     | One paint instruction in the big style file.

2219 | .fs-row-checkbox { width: 18px; height: 18px; flex-shrink: 0; accent-color: var(--indigo); cursor: pointer; }
     | One paint instruction in the big style file.

2220 | .fs-row-main { flex: 1; min-width: 160px; display: flex; flex-direction: column; gap: 4px; }
     | One paint instruction in the big style file.

2221 | .fs-row-domain { font-size: var(--text-sm); color: var(--text); font-weight: 600; word-break: break-all; display: flex; flex-direction: column; }
     | One paint instruction in the big style file.

2222 | .fs-row-domain-sub { font-size: var(--text-xs); color: var(--muted); font-weight: 400; }
     | One paint instruction in the big style file.

2223 | .fs-row-meta { display: flex; align-items: center; gap: 6px; flex-wrap: wrap; }
     | One paint instruction in the big style file.

2224 | .fs-row-notes { font-style: italic; }
     | One paint instruction in the big style file.

2225 | .fs-row-actions { display: flex; align-items: center; gap: 10px; flex-shrink: 0; margin-left: auto; }
     | One paint instruction in the big style file.

2226 | 
     | A blank line in the paint file. It does not change how anything looks.

2227 | /* Three-dot row menu */
     | A label for people about the next chunk of paint. The browser ignores it.

2228 | .fs-row-menu { position: relative; }
     | One paint instruction in the big style file.

2229 | .fs-row-menu-btn {
     | This starts paint instructions for things that match `.fs-row-menu-btn`.

2230 |   width: 32px;
     | This sets one look: width becomes 32px.

2231 |   height: 32px;
     | This sets one look: height becomes 32px.

2232 |   border-radius: var(--radius-sm);
     | This sets one look: border-radius becomes var(--radius-sm).

2233 |   border: 1px solid transparent;
     | This sets one look: border becomes 1px solid transparent.

2234 |   background: transparent;
     | This sets one look: background becomes transparent.

2235 |   color: var(--muted);
     | This sets one look: color becomes var(--muted).

2236 |   cursor: pointer;
     | This sets one look: cursor becomes pointer.

2237 |   font-size: 16px;
     | This sets one look: font-size becomes 16px.

2238 |   line-height: 1;
     | This sets one look: line-height becomes 1.

2239 | }
     | This ends that group of paint instructions.

2240 | .fs-row-menu-btn:hover { background: var(--border); color: var(--text); }
     | One paint instruction in the big style file.

2241 | .fs-row-menu-list {
     | This starts paint instructions for things that match `.fs-row-menu-list`.

2242 |   position: absolute;
     | This sets one look: position becomes absolute.

2243 |   right: 0;
     | This sets one look: right becomes 0.

2244 |   top: 36px;
     | This sets one look: top becomes 36px.

2245 |   min-width: 140px;
     | This sets one look: min-width becomes 140px.

2246 |   background: var(--card);
     | This sets one look: background becomes var(--card).

2247 |   border: 1px solid var(--border);
     | This sets one look: border becomes 1px solid var(--border).

2248 |   border-radius: var(--radius-sm);
     | This sets one look: border-radius becomes var(--radius-sm).

2249 |   box-shadow: var(--shadow);
     | This sets one look: box-shadow becomes var(--shadow).

2250 |   display: flex;
     | This sets one look: display becomes flex.

2251 |   flex-direction: column;
     | This sets one look: flex-direction becomes column.

2252 |   padding: 4px;
     | This sets one look: padding becomes 4px.

2253 |   z-index: 20;
     | This sets one look: z-index becomes 20.

2254 | }
     | This ends that group of paint instructions.

2255 | .fs-row-menu-list button {
     | This starts paint instructions for things that match `.fs-row-menu-list button`.

2256 |   text-align: left;
     | This sets one look: text-align becomes left.

2257 |   padding: 8px 10px;
     | This sets one look: padding becomes 8px 10px.

2258 |   background: none;
     | This sets one look: background becomes none.

2259 |   border: none;
     | This sets one look: border becomes none.

2260 |   border-radius: 6px;
     | This sets one look: border-radius becomes 6px.

2261 |   color: var(--text-soft);
     | This sets one look: color becomes var(--text-soft).

2262 |   font-size: var(--text-sm);
     | This sets one look: font-size becomes var(--text-sm).

2263 |   cursor: pointer;
     | This sets one look: cursor becomes pointer.

2264 |   font-family: inherit;
     | This sets one look: font-family becomes inherit.

2265 | }
     | This ends that group of paint instructions.

2266 | .fs-row-menu-list button:hover { background: var(--indigo-dim); color: var(--indigo-light); }
     | One paint instruction in the big style file.

2267 | .fs-row-menu-danger { color: var(--red) !important; }
     | One paint instruction in the big style file.

2268 | .fs-row-menu-danger:hover { background: var(--red-dim) !important; color: var(--red) !important; }
     | One paint instruction in the big style file.

2269 | 
     | A blank line in the paint file. It does not change how anything looks.

2270 | /* Blocked-apps rows (simple list, no domain validation) */
     | A label for people about the next chunk of paint. The browser ignores it.

2271 | .fs-app-row {
     | This starts paint instructions for things that match `.fs-app-row`.

2272 |   display: flex;
     | This sets one look: display becomes flex.

2273 |   align-items: center;
     | This sets one look: align-items becomes center.

2274 |   gap: 8px;
     | This sets one look: gap becomes 8px.

2275 |   background: var(--surface);
     | This sets one look: background becomes var(--surface).

2276 |   border-radius: var(--radius-sm);
     | This sets one look: border-radius becomes var(--radius-sm).

2277 |   padding: 6px 10px;
     | This sets one look: padding becomes 6px 10px.

2278 |   border: 1px solid var(--border);
     | This sets one look: border becomes 1px solid var(--border).

2279 | }
     | This ends that group of paint instructions.

2280 | .fs-app-row .fs-row-domain { flex: 1; font-weight: 400; }
     | One paint instruction in the big style file.

2281 | .fs-app-remove { background: none; border: none; color: var(--muted); cursor: pointer; font-size: 16px; line-height: 1; padding: 0 2px; }
     | One paint instruction in the big style file.

2282 | .fs-app-remove:hover { color: var(--red); }
     | One paint instruction in the big style file.

2283 | 
     | A blank line in the paint file. It does not change how anything looks.

2284 | /* Schedule day pills */
     | A label for people about the next chunk of paint. The browser ignores it.

2285 | .fs-day-pill {
     | This starts paint instructions for things that match `.fs-day-pill`.

2286 |   padding: 4px 10px;
     | This sets one look: padding becomes 4px 10px.

2287 |   min-height: 30px;
     | This sets one look: min-height becomes 30px.

2288 |   border-radius: var(--radius-sm);
     | This sets one look: border-radius becomes var(--radius-sm).

2289 |   border: 1px solid var(--border);
     | This sets one look: border becomes 1px solid var(--border).

2290 |   background: transparent;
     | This sets one look: background becomes transparent.

2291 |   color: var(--muted);
     | This sets one look: color becomes var(--muted).

2292 |   font-size: var(--text-xs);
     | This sets one look: font-size becomes var(--text-xs).

2293 |   font-weight: 400;
     | This sets one look: font-weight becomes 400.

2294 |   cursor: pointer;
     | This sets one look: cursor becomes pointer.

2295 |   transition: all 0.15s;
     | This sets one look: transition becomes all 0.15s.

2296 | }
     | This ends that group of paint instructions.

2297 | .fs-day-pill--active { border-color: var(--indigo); background: var(--indigo-dim); color: var(--indigo-light); font-weight: 600; }
     | One paint instruction in the big style file.

2298 | 
     | A blank line in the paint file. It does not change how anything looks.

2299 | .fs-notice {
     | This starts paint instructions for things that match `.fs-notice`.

2300 |   display: flex;
     | This sets one look: display becomes flex.

2301 |   align-items: flex-start;
     | This sets one look: align-items becomes flex-start.

2302 |   gap: 8px;
     | This sets one look: gap becomes 8px.

2303 |   padding: 8px 12px;
     | This sets one look: padding becomes 8px 12px.

2304 |   background: var(--amber-dim);
     | This sets one look: background becomes var(--amber-dim).

2305 |   border-radius: var(--radius-sm);
     | This sets one look: border-radius becomes var(--radius-sm).

2306 |   border: 1px solid var(--amber);
     | This sets one look: border becomes 1px solid var(--amber).

2307 | }
     | This ends that group of paint instructions.

2308 | 
     | A blank line in the paint file. It does not change how anything looks.

2309 | /* Focus Shield quick-access row on Profile & Settings */
     | A label for people about the next chunk of paint. The browser ignores it.

2310 | .fs-quick-link {
     | This starts paint instructions for things that match `.fs-quick-link`.

2311 |   display: flex;
     | This sets one look: display becomes flex.

2312 |   align-items: center;
     | This sets one look: align-items becomes center.

2313 |   gap: 12px;
     | This sets one look: gap becomes 12px.

2314 |   text-decoration: none;
     | This sets one look: text-decoration becomes none.

2315 |   cursor: pointer;
     | This sets one look: cursor becomes pointer.

2316 |   transition: border-color 0.15s;
     | This sets one look: transition becomes border-color 0.15s.

2317 | }
     | This ends that group of paint instructions.

2318 | .fs-quick-link:hover { border-color: var(--border-active); }
     | One paint instruction in the big style file.

2319 | .fs-quick-link-icon { font-size: 24px; flex-shrink: 0; }
     | One paint instruction in the big style file.

2320 | 
     | A blank line in the paint file. It does not change how anything looks.

2321 | /* Sheet (bottom sheet on mobile, centered modal on desktop) */
     | A label for people about the next chunk of paint. The browser ignores it.

2322 | .fs-sheet-overlay {
     | This starts paint instructions for things that match `.fs-sheet-overlay`.

2323 |   position: fixed;
     | This sets one look: position becomes fixed.

2324 |   inset: 0;
     | This sets one look: inset becomes 0.

2325 |   background: rgba(0, 0, 0, 0.5);
     | This sets one look: background becomes rgba(0, 0, 0, 0.5).

2326 |   backdrop-filter: blur(2px);
     | This sets one look: backdrop-filter becomes blur(2px).

2327 |   z-index: 199;
     | This sets one look: z-index becomes 199.

2328 | }
     | This ends that group of paint instructions.

2329 | .fs-sheet {
     | This starts paint instructions for things that match `.fs-sheet`.

2330 |   position: fixed;
     | This sets one look: position becomes fixed.

2331 |   left: 0;
     | This sets one look: left becomes 0.

2332 |   right: 0;
     | This sets one look: right becomes 0.

2333 |   bottom: 0;
     | This sets one look: bottom becomes 0.

2334 |   background: var(--surface);
     | This sets one look: background becomes var(--surface).

2335 |   border-radius: 20px 20px 0 0;
     | This sets one look: border-radius becomes 20px 20px 0 0.

2336 |   border-top: 1px solid var(--border);
     | This sets one look: border-top becomes 1px solid var(--border).

2337 |   z-index: 200;
     | This sets one look: z-index becomes 200.

2338 |   max-height: 85vh;
     | This sets one look: max-height becomes 85vh.

2339 |   overflow-y: auto;
     | This sets one look: overflow-y becomes auto.

2340 |   padding: 0 var(--space-4) calc(env(safe-area-inset-bottom, 0px) + var(--space-5));
     | This sets one look: padding becomes 0 var(--space-4) calc(env(safe-area-inset-bottom, 0px) + var(--space-5)).

2341 |   box-shadow: 0 -4px 24px rgba(0, 0, 0, 0.3);
     | This sets one look: box-shadow becomes 0 -4px 24px rgba(0, 0, 0, 0.3).

2342 | }
     | This ends that group of paint instructions.

2343 | .fs-sheet-header { display: flex; align-items: center; justify-content: space-between; padding: 4px 0 12px; }
     | One paint instruction in the big style file.

2344 | .fs-sheet-title { font-size: var(--text-lg); font-weight: 700; color: var(--text); }
     | One paint instruction in the big style file.

2345 | .fs-sheet-close {
     | This starts paint instructions for things that match `.fs-sheet-close`.

2346 |   width: 32px;
     | This sets one look: width becomes 32px.

2347 |   height: 32px;
     | This sets one look: height becomes 32px.

2348 |   border-radius: var(--radius-sm);
     | This sets one look: border-radius becomes var(--radius-sm).

2349 |   border: none;
     | This sets one look: border becomes none.

2350 |   background: transparent;
     | This sets one look: background becomes transparent.

2351 |   color: var(--muted);
     | This sets one look: color becomes var(--muted).

2352 |   font-size: 22px;
     | This sets one look: font-size becomes 22px.

2353 |   line-height: 1;
     | This sets one look: line-height becomes 1.

2354 |   cursor: pointer;
     | This sets one look: cursor becomes pointer.

2355 | }
     | This ends that group of paint instructions.

2356 | .fs-sheet-close:hover { background: var(--border); color: var(--text); }
     | One paint instruction in the big style file.

2357 | .fs-sheet-body { display: flex; flex-direction: column; }
     | One paint instruction in the big style file.

2358 | .fs-sheet-divider { height: 1px; background: var(--border); margin: 16px 0; }
     | One paint instruction in the big style file.

2359 | .fs-sheet-footer { position: sticky; bottom: 0; background: var(--surface); padding: 14px 0 4px; margin-top: 10px; }
     | One paint instruction in the big style file.

2360 | .fs-sheet-footer--split { display: flex; gap: 10px; justify-content: flex-end; }
     | One paint instruction in the big style file.

2361 | 
     | A blank line in the paint file. It does not change how anything looks.

2362 | @media (min-width: 769px) {
     | This says: only use the next paint rules when the screen is a certain size.

2363 |   .fs-sheet {
     | This starts paint instructions for things that match `.fs-sheet`.

2364 |     position: fixed;
     | This sets one look: position becomes fixed.

2365 |     top: 50%;
     | This sets one look: top becomes 50%.

2366 |     left: 50%;
     | This sets one look: left becomes 50%.

2367 |     right: auto;
     | This sets one look: right becomes auto.

2368 |     bottom: auto;
     | This sets one look: bottom becomes auto.

2369 |     transform: translate(-50%, -50%);
     | This sets one look: transform becomes translate(-50%, -50%).

2370 |     width: calc(100% - 2 * var(--space-5));
     | This sets one look: width becomes calc(100% - 2 * var(--space-5)).

2371 |     max-width: 460px;
     | This sets one look: max-width becomes 460px.

2372 |     border-radius: var(--radius-lg);
     | This sets one look: border-radius becomes var(--radius-lg).

2373 |     border: 1px solid var(--border);
     | This sets one look: border becomes 1px solid var(--border).

2374 |     max-height: 80vh;
     | This sets one look: max-height becomes 80vh.

2375 |     padding: var(--space-5);
     | This sets one look: padding becomes var(--space-5).

2376 |     box-shadow: var(--shadow);
     | This sets one look: box-shadow becomes var(--shadow).

2377 |   }
     | This ends that group of paint instructions.

2378 |   .fs-sheet .bottom-sheet-handle { display: none; }
     | One paint instruction in the big style file.

2379 | }
     | This ends that group of paint instructions.

2380 | 
     | A blank line in the paint file. It does not change how anything looks.

2381 | /* Popular website chips */
     | A label for people about the next chunk of paint. The browser ignores it.

2382 | .fs-popular-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; }
     | One paint instruction in the big style file.

2383 | .fs-popular-chip {
     | This starts paint instructions for things that match `.fs-popular-chip`.

2384 |   display: flex;
     | This sets one look: display becomes flex.

2385 |   flex-direction: column;
     | This sets one look: flex-direction becomes column.

2386 |   align-items: center;
     | This sets one look: align-items becomes center.

2387 |   gap: 4px;
     | This sets one look: gap becomes 4px.

2388 |   padding: 12px 8px;
     | This sets one look: padding becomes 12px 8px.

2389 |   min-height: 44px;
     | This sets one look: min-height becomes 44px.

2390 |   border-radius: var(--radius-sm);
     | This sets one look: border-radius becomes var(--radius-sm).

2391 |   border: 1px solid var(--border);
     | This sets one look: border becomes 1px solid var(--border).

2392 |   background: var(--surface);
     | This sets one look: background becomes var(--surface).

2393 |   cursor: pointer;
     | This sets one look: cursor becomes pointer.

2394 |   transition: all 0.15s;
     | This sets one look: transition becomes all 0.15s.

2395 |   font-family: inherit;
     | This sets one look: font-family becomes inherit.

2396 | }
     | This ends that group of paint instructions.

2397 | .fs-popular-chip:hover:not(:disabled) { border-color: var(--border-active); background: var(--indigo-dim); }
     | One paint instruction in the big style file.

2398 | .fs-popular-chip:disabled { cursor: default; opacity: 0.7; }
     | One paint instruction in the big style file.

2399 | .fs-popular-chip--added { border-color: var(--green); background: var(--green-dim); }
     | One paint instruction in the big style file.

2400 | .fs-popular-emoji { font-size: 20px; }
     | One paint instruction in the big style file.

2401 | .fs-popular-label { font-size: var(--text-xs); font-weight: 600; color: var(--text); text-align: center; }
     | One paint instruction in the big style file.

2402 | .fs-popular-status { font-size: 10px; color: var(--muted); }
     | One paint instruction in the big style file.

2403 | .fs-popular-chip--added .fs-popular-status { color: var(--green); }
     | One paint instruction in the big style file.

2404 | 
     | A blank line in the paint file. It does not change how anything looks.

2405 | .fs-custom-domain-row { display: flex; gap: 8px; }
     | One paint instruction in the big style file.

2406 | .fs-custom-domain-row .profile-form-input { flex: 1; }
     | One paint instruction in the big style file.

2407 | 
     | A blank line in the paint file. It does not change how anything looks.

2408 | /* Smart preset cards */
     | A label for people about the next chunk of paint. The browser ignores it.

2409 | .fs-preset-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)); gap: 10px; }
     | One paint instruction in the big style file.

2410 | .fs-preset-card {
     | This starts paint instructions for things that match `.fs-preset-card`.

2411 |   display: flex;
     | This sets one look: display becomes flex.

2412 |   flex-direction: column;
     | This sets one look: flex-direction becomes column.

2413 |   gap: 4px;
     | This sets one look: gap becomes 4px.

2414 |   align-items: flex-start;
     | This sets one look: align-items becomes flex-start.

2415 |   text-align: left;
     | This sets one look: text-align becomes left.

2416 |   padding: 14px;
     | This sets one look: padding becomes 14px.

2417 |   border-radius: var(--radius-sm);
     | This sets one look: border-radius becomes var(--radius-sm).

2418 |   border: 1px solid var(--border);
     | This sets one look: border becomes 1px solid var(--border).

2419 |   background: var(--surface);
     | This sets one look: background becomes var(--surface).

2420 |   cursor: pointer;
     | This sets one look: cursor becomes pointer.

2421 |   transition: all 0.15s;
     | This sets one look: transition becomes all 0.15s.

2422 |   font-family: inherit;
     | This sets one look: font-family becomes inherit.

2423 | }
     | This ends that group of paint instructions.

2424 | .fs-preset-card:hover { border-color: var(--border-active); background: var(--card-hover); }
     | One paint instruction in the big style file.

2425 | .fs-preset-emoji { font-size: 22px; }
     | One paint instruction in the big style file.

2426 | .fs-preset-label { font-size: var(--text-sm); font-weight: 700; color: var(--text); }
     | One paint instruction in the big style file.

2427 | .fs-preset-desc { font-size: var(--text-xs); color: var(--muted); line-height: 1.4; }
     | One paint instruction in the big style file.

2428 | .fs-preset-status { font-size: 10px; font-weight: 600; color: var(--indigo-light); margin-top: 4px; }
     | One paint instruction in the big style file.

2429 | 
     | A blank line in the paint file. It does not change how anything looks.

2430 | @media (max-width: 640px) {
     | This says: only use the next paint rules when the screen is a certain size.

2431 |   .fs-popular-grid { grid-template-columns: repeat(2, 1fr); }
     | One paint instruction in the big style file.

2432 |   .fs-row { gap: 8px; }
     | One paint instruction in the big style file.

2433 |   .fs-row-actions { margin-left: 0; width: 100%; justify-content: space-between; }
     | One paint instruction in the big style file.

2434 | }
     | This ends that group of paint instructions.

2435 | 
     | A blank line in the paint file. It does not change how anything looks.

2436 | /* ── Reduced motion ─────────────────────────────────── */
     | A label for people about the next chunk of paint. The browser ignores it.

2437 | @media (prefers-reduced-motion: reduce) {
     | This says: only use the next paint rules when the screen is a certain size.

2438 |   *, *::before, *::after {
     | A label for people about the next chunk of paint. The browser ignores it.

2439 |     animation-duration: 0.01ms !important;
     | This sets one look: animation-duration becomes 0.01ms !important.

2440 |     animation-iteration-count: 1 !important;
     | This sets one look: animation-iteration-count becomes 1 !important.

2441 |     transition-duration: 0.01ms !important;
     | This sets one look: transition-duration becomes 0.01ms !important.

2442 |     scroll-behavior: auto !important;
     | This sets one look: scroll-behavior becomes auto !important.

2443 |   }
     | This ends that group of paint instructions.

2444 | }
     | This ends that group of paint instructions.

