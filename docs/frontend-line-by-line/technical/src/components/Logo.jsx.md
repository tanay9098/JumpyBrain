# `src/components/Logo.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | const GRAD_ID_COUNTER = { n: 0 };
     | In `the top of the file` (src/components/Logo.jsx): `GRAD_ID_COUNTER` is assigned `{ n: 0 };`. Later lines in this function read that name.

   2 | 
     | Blank line in `src/components/Logo.jsx` (the JumpyBrain mark), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   3 | function useGradId() {
     | Defines `useGradId` in the JumpyBrain mark. Unused. Logo builds its own gradient id instead.

   4 |   return `jbg-${++GRAD_ID_COUNTER.n}`;
     | In `useGradId` (src/components/Logo.jsx): return `return `jbg-${++GRAD_ID_COUNTER.n}`;`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

   5 | }
     | In `useGradId` (src/components/Logo.jsx): `}` closes useGradId (opened on line 3). Names declared inside that block end here.

   6 | 
     | Blank line in `src/components/Logo.jsx` (the JumpyBrain mark), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   7 | function JBIcon({ size = 32, variant = "color", gradId }) {
     | Defines `JBIcon` in the JumpyBrain mark. The SVG paths for the monogram. mono-dark and mono-light are solid; anything else uses the purple-to-cyan gradient.

   8 |   const sw = size * 0.08;
     | In `JBIcon` (src/components/Logo.jsx): `sw` is assigned `size * 0.08;`. Later lines in this function read that name.

   9 |   const r = size * 0.055;
     | In `JBIcon` (src/components/Logo.jsx): `r` is assigned `size * 0.055;`. Later lines in this function read that name.

  10 | 
     | Blank line in `src/components/Logo.jsx` (the JumpyBrain mark), inside JBIcon. The parser skips it. It separates the previous statement from the next so the function is readable.

  11 |   if (variant === "mono-dark") {
     | In `JBIcon` (src/components/Logo.jsx): branch `if (variant === "mono-dark") {`. Only one side runs.

  12 |     return (
     | In `JBIcon` (src/components/Logo.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  13 |       <svg width={size} height={size} viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
     | In `JBIcon` (src/components/Logo.jsx): Opens it. Vector drawing. It does not fetch data. Source: `<svg width={size} height={size} viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">`

  14 |         <circle cx="23" cy="23" r="5.5" fill="#111128"/>
     | In `JBIcon` (src/components/Logo.jsx): JSX `<circle>`. React will create this node when the parent renders. Source: `<circle cx="23" cy="23" r="5.5" fill="#111128"/>`

  15 |         <path d="M 37 23 L 37 66 Q 37 80 20 80" stroke="#111128" strokeWidth={sw} strokeLinecap="round" strokeLinejoin="round"/>
     | In `JBIcon` (src/components/Logo.jsx): JSX `<path>`. React will create this node when the parent renders. Source: `<path d="M 37 23 L 37 66 Q 37 80 20 80" stroke="#111128" strokeWidth={sw} strokeLinecap="round" strokeLinejoin="round"/>`

  16 |         <path d="M 55 23 L 55 80" stroke="#111128" strokeWidth={sw} strokeLinecap="round"/>
     | In `JBIcon` (src/components/Logo.jsx): JSX `<path>`. React will create this node when the parent renders. Source: `<path d="M 55 23 L 55 80" stroke="#111128" strokeWidth={sw} strokeLinecap="round"/>`

  17 |         <path d="M 55 23 Q 78 23 78 38 Q 78 52 55 52" stroke="#111128" strokeWidth={sw} strokeLinecap="round" strokeLinejoin="round"/>
     | In `JBIcon` (src/components/Logo.jsx): JSX `<path>`. React will create this node when the parent renders. Source: `<path d="M 55 23 Q 78 23 78 38 Q 78 52 55 52" stroke="#111128" strokeWidth={sw} strokeLinecap="round" strokeLinejoin="round"/>`

  18 |         <path d="M 55 52 Q 82 52 82 66 Q 82 80 55 80" stroke="#111128" strokeWidth={sw} strokeLinecap="round" strokeLinejoin="round"/>
     | In `JBIcon` (src/components/Logo.jsx): JSX `<path>`. React will create this node when the parent renders. Source: `<path d="M 55 52 Q 82 52 82 66 Q 82 80 55 80" stroke="#111128" strokeWidth={sw} strokeLinecap="round" strokeLinejoin="round"/>`

  19 |       </svg>
     | In `JBIcon` (src/components/Logo.jsx): Closes it. Vector drawing. It does not fetch data. Source: `</svg>`

  20 |     );
     | In `JBIcon` (src/components/Logo.jsx): statement `);`. It runs when JBIcon runs, in order, before the next line of the same function.

  21 |   }
     | In `JBIcon` (src/components/Logo.jsx): `}` closes if (variant === "mono-dark") { (opened on line 11). Names declared inside that block end here.

  22 | 
     | Blank line in `src/components/Logo.jsx` (the JumpyBrain mark), inside JBIcon. The parser skips it. It separates the previous statement from the next so the function is readable.

  23 |   if (variant === "mono-light") {
     | In `JBIcon` (src/components/Logo.jsx): branch `if (variant === "mono-light") {`. Only one side runs.

  24 |     return (
     | In `JBIcon` (src/components/Logo.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  25 |       <svg width={size} height={size} viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
     | In `JBIcon` (src/components/Logo.jsx): Opens it. Vector drawing. It does not fetch data. Source: `<svg width={size} height={size} viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">`

  26 |         <circle cx="23" cy="23" r="5.5" fill="#ffffff"/>
     | In `JBIcon` (src/components/Logo.jsx): JSX `<circle>`. React will create this node when the parent renders. Source: `<circle cx="23" cy="23" r="5.5" fill="#ffffff"/>`

  27 |         <path d="M 37 23 L 37 66 Q 37 80 20 80" stroke="#ffffff" strokeWidth={sw} strokeLinecap="round" strokeLinejoin="round"/>
     | In `JBIcon` (src/components/Logo.jsx): JSX `<path>`. React will create this node when the parent renders. Source: `<path d="M 37 23 L 37 66 Q 37 80 20 80" stroke="#ffffff" strokeWidth={sw} strokeLinecap="round" strokeLinejoin="round"/>`

  28 |         <path d="M 55 23 L 55 80" stroke="#ffffff" strokeWidth={sw} strokeLinecap="round"/>
     | In `JBIcon` (src/components/Logo.jsx): JSX `<path>`. React will create this node when the parent renders. Source: `<path d="M 55 23 L 55 80" stroke="#ffffff" strokeWidth={sw} strokeLinecap="round"/>`

  29 |         <path d="M 55 23 Q 78 23 78 38 Q 78 52 55 52" stroke="#ffffff" strokeWidth={sw} strokeLinecap="round" strokeLinejoin="round"/>
     | In `JBIcon` (src/components/Logo.jsx): JSX `<path>`. React will create this node when the parent renders. Source: `<path d="M 55 23 Q 78 23 78 38 Q 78 52 55 52" stroke="#ffffff" strokeWidth={sw} strokeLinecap="round" strokeLinejoin="round"/>`

  30 |         <path d="M 55 52 Q 82 52 82 66 Q 82 80 55 80" stroke="#ffffff" strokeWidth={sw} strokeLinecap="round" strokeLinejoin="round"/>
     | In `JBIcon` (src/components/Logo.jsx): JSX `<path>`. React will create this node when the parent renders. Source: `<path d="M 55 52 Q 82 52 82 66 Q 82 80 55 80" stroke="#ffffff" strokeWidth={sw} strokeLinecap="round" strokeLinejoin="round"/>`

  31 |       </svg>
     | In `JBIcon` (src/components/Logo.jsx): Closes it. Vector drawing. It does not fetch data. Source: `</svg>`

  32 |     );
     | In `JBIcon` (src/components/Logo.jsx): statement `);`. It runs when JBIcon runs, in order, before the next line of the same function.

  33 |   }
     | In `JBIcon` (src/components/Logo.jsx): `}` closes if (variant === "mono-light") { (opened on line 23). Names declared inside that block end here.

  34 | 
     | Blank line in `src/components/Logo.jsx` (the JumpyBrain mark), inside JBIcon. The parser skips it. It separates the previous statement from the next so the function is readable.

  35 |   const g = gradId;
     | In `JBIcon` (src/components/Logo.jsx): `g` is assigned `gradId;`. Later lines in this function read that name.

  36 |   return (
     | In `JBIcon` (src/components/Logo.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  37 |     <svg width={size} height={size} viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
     | In `JBIcon` (src/components/Logo.jsx): Opens it. Vector drawing. It does not fetch data. Source: `<svg width={size} height={size} viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">`

  38 |       <defs>
     | In `JBIcon` (src/components/Logo.jsx): JSX `<defs>`. React will create this node when the parent renders. Source: `<defs>`

  39 |         <linearGradient id={g} x1="13" y1="17" x2="82" y2="80" gradientUnits="userSpaceOnUse">
     | In `JBIcon` (src/components/Logo.jsx): JSX `<linearGradient>`. React will create this node when the parent renders. Source: `<linearGradient id={g} x1="13" y1="17" x2="82" y2="80" gradientUnits="userSpaceOnUse">`

  40 |           <stop offset="0%" stopColor="#7C3AED"/>
     | In `JBIcon` (src/components/Logo.jsx): JSX `<stop>`. React will create this node when the parent renders. Source: `<stop offset="0%" stopColor="#7C3AED"/>`

  41 |           <stop offset="42%" stopColor="#6366F1"/>
     | In `JBIcon` (src/components/Logo.jsx): JSX `<stop>`. React will create this node when the parent renders. Source: `<stop offset="42%" stopColor="#6366F1"/>`

  42 |           <stop offset="100%" stopColor="#06B6D4"/>
     | In `JBIcon` (src/components/Logo.jsx): JSX `<stop>`. React will create this node when the parent renders. Source: `<stop offset="100%" stopColor="#06B6D4"/>`

  43 |         </linearGradient>
     | In `JBIcon` (src/components/Logo.jsx): JSX `<linearGradient>`. This closes that element. Source: `</linearGradient>`

  44 |       </defs>
     | In `JBIcon` (src/components/Logo.jsx): JSX `<defs>`. This closes that element. Source: `</defs>`

  45 |       <circle cx="23" cy="23" r="5.5" fill={`url(#${g})`}/>
     | In `JBIcon` (src/components/Logo.jsx): JSX `<circle>`. React will create this node when the parent renders. Source: `<circle cx="23" cy="23" r="5.5" fill={`url(#${g})`}/>`

  46 |       <path d="M 37 23 L 37 66 Q 37 80 20 80" stroke={`url(#${g})`} strokeWidth={sw} strokeLinecap="round" strokeLinejoin="round"/>
     | In `JBIcon` (src/components/Logo.jsx): JSX `<path>`. React will create this node when the parent renders. Source: `<path d="M 37 23 L 37 66 Q 37 80 20 80" stroke={`url(#${g})`} strokeWidth={sw} strokeLinecap="round" strokeLinejoin="round"/>`

  47 |       <path d="M 55 23 L 55 80" stroke={`url(#${g})`} strokeWidth={sw} strokeLinecap="round"/>
     | In `JBIcon` (src/components/Logo.jsx): JSX `<path>`. React will create this node when the parent renders. Source: `<path d="M 55 23 L 55 80" stroke={`url(#${g})`} strokeWidth={sw} strokeLinecap="round"/>`

  48 |       <path d="M 55 23 Q 78 23 78 38 Q 78 52 55 52" stroke={`url(#${g})`} strokeWidth={sw} strokeLinecap="round" strokeLinejoin="round"/>
     | In `JBIcon` (src/components/Logo.jsx): JSX `<path>`. React will create this node when the parent renders. Source: `<path d="M 55 23 Q 78 23 78 38 Q 78 52 55 52" stroke={`url(#${g})`} strokeWidth={sw} strokeLinecap="round" strokeLinejoin="round"/>`

  49 |       <path d="M 55 52 Q 82 52 82 66 Q 82 80 55 80" stroke={`url(#${g})`} strokeWidth={sw} strokeLinecap="round" strokeLinejoin="round"/>
     | In `JBIcon` (src/components/Logo.jsx): JSX `<path>`. React will create this node when the parent renders. Source: `<path d="M 55 52 Q 82 52 82 66 Q 82 80 55 80" stroke={`url(#${g})`} strokeWidth={sw} strokeLinecap="round" strokeLinejoin="round"/>`

  50 |     </svg>
     | In `JBIcon` (src/components/Logo.jsx): Closes it. Vector drawing. It does not fetch data. Source: `</svg>`

  51 |   );
     | In `JBIcon` (src/components/Logo.jsx): statement `);`. It runs when JBIcon runs, in order, before the next line of the same function.

  52 | }
     | In `JBIcon` (src/components/Logo.jsx): `}` closes JBIcon (opened on line 7). Names declared inside that block end here.

  53 | 
     | Blank line in `src/components/Logo.jsx` (the JumpyBrain mark), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  54 | /**
     | Comment inside the top of the file. Not executed. Text: /**

  55 |  * JumpyBrain Logo component.
     | Comment inside the top of the file. Not executed. Text: * JumpyBrain Logo component.

  56 |  *
     | Comment inside the top of the file. Not executed. Text: *

  57 |  * variant: "icon" | "full" | "mono-light" | "mono-dark"
     | Comment inside the top of the file. Not executed. Text: * variant: "icon" | "full" | "mono-light" | "mono-dark"

  58 |  * size: icon height in px (default 32)
     | Comment inside the top of the file. Not executed. Text: * size: icon height in px (default 32)

  59 |  * showWordmark: whether to show "Jumpy Brain" text beside icon (default true for "full")
     | Comment inside the top of the file. Not executed. Text: * showWordmark: whether to show "Jumpy Brain" text beside icon (default true for "full")

  60 |  */
     | Comment inside the top of the file. Not executed. Text: */

  61 | export default function Logo({ variant = "icon", size = 32, className = "", style = {} }) {
     | Defines `Logo` in the JumpyBrain mark. Draws the JB mark. variant full adds the wordmark. The gradient id includes size and variant so two logos on one page do not clash.

  62 |   const gradId = `jbg-${size}-${variant}`;
     | In `Logo` (src/components/Logo.jsx): `gradId` is assigned ``jbg-${size}-${variant}`;`. Later lines in this function read that name.

  63 | 
     | Blank line in `src/components/Logo.jsx` (the JumpyBrain mark), inside Logo. The parser skips it. It separates the previous statement from the next so the function is readable.

  64 |   if (variant === "full") {
     | In `Logo` (src/components/Logo.jsx): branch `if (variant === "full") {`. Only one side runs.

  65 |     return (
     | In `Logo` (src/components/Logo.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  66 |       <span
     | In `Logo` (src/components/Logo.jsx): Opens it. An inline box. Source: `<span`

  67 |         className={`jb-logo-full ${className}`}
     | In `Logo` (src/components/Logo.jsx): `className={`jb-logo-full ${className}`}` closes if (variant === "full") { (opened on line 64). Names declared inside that block end here.

  68 |         style={{ display: "inline-flex", alignItems: "center", gap: size * 0.35, ...style }}
     | In `Logo` (src/components/Logo.jsx): `style={{ display: "inline-flex", alignItems: "center", gap: size * 0.35, ...style }}` closes if (variant === "full") { (opened on line 64). Names declared inside that block end here.

  69 |         role="img"
     | In `Logo` (src/components/Logo.jsx): statement `role="img"`. It runs when Logo runs, in order, before the next line of the same function.

  70 |         aria-label="JumpyBrain"
     | In `Logo` (src/components/Logo.jsx): statement `aria-label="JumpyBrain"`. It runs when Logo runs, in order, before the next line of the same function.

  71 |       >
     | In `Logo` (src/components/Logo.jsx): statement `>`. It runs when Logo runs, in order, before the next line of the same function.

  72 |         <JBIcon size={size} variant="color" gradId={gradId} />
     | In `Logo` (src/components/Logo.jsx): JSX `<JBIcon>`. React will create this node when the parent renders. Source: `<JBIcon size={size} variant="color" gradId={gradId} />`

  73 |         <span style={{
     | In `Logo` (src/components/Logo.jsx): Opens it. An inline box. Source: `<span style={{`

  74 |           fontSize: size * 0.5,
     | In `Logo` (src/components/Logo.jsx): statement `fontSize: size * 0.5,`. It runs when Logo runs, in order, before the next line of the same function.

  75 |           fontWeight: 700,
     | In `Logo` (src/components/Logo.jsx): statement `fontWeight: 700,`. It runs when Logo runs, in order, before the next line of the same function.

  76 |           lineHeight: 1,
     | In `Logo` (src/components/Logo.jsx): statement `lineHeight: 1,`. It runs when Logo runs, in order, before the next line of the same function.

  77 |           letterSpacing: "-0.02em",
     | In `Logo` (src/components/Logo.jsx): statement `letterSpacing: "-0.02em",`. It runs when Logo runs, in order, before the next line of the same function.

  78 |           color: "var(--text)",
     | In `Logo` (src/components/Logo.jsx): statement `color: "var(--text)",`. It runs when Logo runs, in order, before the next line of the same function.

  79 |         }}>
     | In `Logo` (src/components/Logo.jsx): `}}>` closes <span style={{ (opened on line 73). Names declared inside that block end here.

  80 |           <span style={{ color: "var(--text)" }}>Jumpy</span>
     | In `Logo` (src/components/Logo.jsx): Opens it. An inline box. Source: `<span style={{ color: "var(--text)" }}>Jumpy</span>`

  81 |           <span style={{
     | In `Logo` (src/components/Logo.jsx): Opens it. An inline box. Source: `<span style={{`

  82 |             background: "linear-gradient(135deg, #7C3AED, #06B6D4)",
     | In `Logo` (src/components/Logo.jsx): statement `background: "linear-gradient(135deg, #7C3AED, #06B6D4)",`. It runs when Logo runs, in order, before the next line of the same function.

  83 |             WebkitBackgroundClip: "text",
     | In `Logo` (src/components/Logo.jsx): statement `WebkitBackgroundClip: "text",`. It runs when Logo runs, in order, before the next line of the same function.

  84 |             WebkitTextFillColor: "transparent",
     | In `Logo` (src/components/Logo.jsx): statement `WebkitTextFillColor: "transparent",`. It runs when Logo runs, in order, before the next line of the same function.

  85 |             backgroundClip: "text",
     | In `Logo` (src/components/Logo.jsx): statement `backgroundClip: "text",`. It runs when Logo runs, in order, before the next line of the same function.

  86 |           }}> Brain</span>
     | In `Logo` (src/components/Logo.jsx): `}}> Brain</span>` closes <span style={{ (opened on line 81). Names declared inside that block end here.

  87 |         </span>
     | In `Logo` (src/components/Logo.jsx): Closes it. An inline box. Source: `</span>`

  88 |       </span>
     | In `Logo` (src/components/Logo.jsx): Closes it. An inline box. Source: `</span>`

  89 |     );
     | In `Logo` (src/components/Logo.jsx): statement `);`. It runs when Logo runs, in order, before the next line of the same function.

  90 |   }
     | In `Logo` (src/components/Logo.jsx): `}` closes if (variant === "full") { (opened on line 64). Names declared inside that block end here.

  91 | 
     | Blank line in `src/components/Logo.jsx` (the JumpyBrain mark), inside Logo. The parser skips it. It separates the previous statement from the next so the function is readable.

  92 |   return (
     | In `Logo` (src/components/Logo.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  93 |     <span
     | In `Logo` (src/components/Logo.jsx): Opens it. An inline box. Source: `<span`

  94 |       className={`jb-logo ${className}`}
     | In `Logo` (src/components/Logo.jsx): `className={`jb-logo ${className}`}` closes Logo (opened on line 61). Names declared inside that block end here.

  95 |       style={style}
     | In `Logo` (src/components/Logo.jsx): `style={style}` closes Logo (opened on line 61). Names declared inside that block end here.

  96 |       role="img"
     | In `Logo` (src/components/Logo.jsx): statement `role="img"`. It runs when Logo runs, in order, before the next line of the same function.

  97 |       aria-label="JumpyBrain"
     | In `Logo` (src/components/Logo.jsx): statement `aria-label="JumpyBrain"`. It runs when Logo runs, in order, before the next line of the same function.

  98 |     >
     | In `Logo` (src/components/Logo.jsx): statement `>`. It runs when Logo runs, in order, before the next line of the same function.

  99 |       <JBIcon size={size} variant={variant} gradId={gradId} />
     | In `Logo` (src/components/Logo.jsx): JSX `<JBIcon>`. React will create this node when the parent renders. Source: `<JBIcon size={size} variant={variant} gradId={gradId} />`

 100 |     </span>
     | In `Logo` (src/components/Logo.jsx): Closes it. An inline box. Source: `</span>`

 101 |   );
     | In `Logo` (src/components/Logo.jsx): statement `);`. It runs when Logo runs, in order, before the next line of the same function.

 102 | }
     | In `Logo` (src/components/Logo.jsx): `}` closes Logo (opened on line 61). Names declared inside that block end here.

