# `src/components/Logo.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | const GRAD_ID_COUNTER = { n: 0 };
     | This gives a short name to a value so the rest of the top of the file can use it.

   2 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   3 | function useGradId() {
     | This starts useGradId. Unused. Logo builds its own gradient id instead.

   4 |   return `jbg-${++GRAD_ID_COUNTER.n}`;
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

   5 | }
     | This ends useGradId (opened on line 3).

   6 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   7 | function JBIcon({ size = 32, variant = "color", gradId }) {
     | This starts JBIcon. The SVG paths for the monogram. mono-dark and mono-light are solid; anything else uses the purple-to-cyan gradient.

   8 |   const sw = size * 0.08;
     | This gives a short name to a value so the rest of JBIcon can use it.

   9 |   const r = size * 0.055;
     | This gives a short name to a value so the rest of JBIcon can use it.

  10 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  11 |   if (variant === "mono-dark") {
     | This asks a yes-or-no question. The next bit runs only on yes.

  12 |     return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  13 |       <svg width={size} height={size} viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
     | This draws one piece of the page while JBIcon is showing.

  14 |         <circle cx="23" cy="23" r="5.5" fill="#111128"/>
     | This draws one piece of the page while JBIcon is showing.

  15 |         <path d="M 37 23 L 37 66 Q 37 80 20 80" stroke="#111128" strokeWidth={sw} strokeLinecap="round" strokeLinejoin="round"/>
     | This draws one piece of the page while JBIcon is showing.

  16 |         <path d="M 55 23 L 55 80" stroke="#111128" strokeWidth={sw} strokeLinecap="round"/>
     | This draws one piece of the page while JBIcon is showing.

  17 |         <path d="M 55 23 Q 78 23 78 38 Q 78 52 55 52" stroke="#111128" strokeWidth={sw} strokeLinecap="round" strokeLinejoin="round"/>
     | This draws one piece of the page while JBIcon is showing.

  18 |         <path d="M 55 52 Q 82 52 82 66 Q 82 80 55 80" stroke="#111128" strokeWidth={sw} strokeLinecap="round" strokeLinejoin="round"/>
     | This draws one piece of the page while JBIcon is showing.

  19 |       </svg>
     | This ends a drawing that JBIcon started just above.

  20 |     );
     | This closes a box of instructions that opened above.

  21 |   }
     | This ends if (variant === "mono-dark") { (opened on line 11).

  22 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  23 |   if (variant === "mono-light") {
     | This asks a yes-or-no question. The next bit runs only on yes.

  24 |     return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  25 |       <svg width={size} height={size} viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
     | This draws one piece of the page while JBIcon is showing.

  26 |         <circle cx="23" cy="23" r="5.5" fill="#ffffff"/>
     | This draws one piece of the page while JBIcon is showing.

  27 |         <path d="M 37 23 L 37 66 Q 37 80 20 80" stroke="#ffffff" strokeWidth={sw} strokeLinecap="round" strokeLinejoin="round"/>
     | This draws one piece of the page while JBIcon is showing.

  28 |         <path d="M 55 23 L 55 80" stroke="#ffffff" strokeWidth={sw} strokeLinecap="round"/>
     | This draws one piece of the page while JBIcon is showing.

  29 |         <path d="M 55 23 Q 78 23 78 38 Q 78 52 55 52" stroke="#ffffff" strokeWidth={sw} strokeLinecap="round" strokeLinejoin="round"/>
     | This draws one piece of the page while JBIcon is showing.

  30 |         <path d="M 55 52 Q 82 52 82 66 Q 82 80 55 80" stroke="#ffffff" strokeWidth={sw} strokeLinecap="round" strokeLinejoin="round"/>
     | This draws one piece of the page while JBIcon is showing.

  31 |       </svg>
     | This ends a drawing that JBIcon started just above.

  32 |     );
     | This closes a box of instructions that opened above.

  33 |   }
     | This ends if (variant === "mono-light") { (opened on line 23).

  34 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  35 |   const g = gradId;
     | This gives a short name to a value so the rest of JBIcon can use it.

  36 |   return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  37 |     <svg width={size} height={size} viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
     | This draws one piece of the page while JBIcon is showing.

  38 |       <defs>
     | This draws one piece of the page while JBIcon is showing.

  39 |         <linearGradient id={g} x1="13" y1="17" x2="82" y2="80" gradientUnits="userSpaceOnUse">
     | This draws one piece of the page while JBIcon is showing.

  40 |           <stop offset="0%" stopColor="#7C3AED"/>
     | This draws one piece of the page while JBIcon is showing.

  41 |           <stop offset="42%" stopColor="#6366F1"/>
     | This draws one piece of the page while JBIcon is showing.

  42 |           <stop offset="100%" stopColor="#06B6D4"/>
     | This draws one piece of the page while JBIcon is showing.

  43 |         </linearGradient>
     | This ends a drawing that JBIcon started just above.

  44 |       </defs>
     | This ends a drawing that JBIcon started just above.

  45 |       <circle cx="23" cy="23" r="5.5" fill={`url(#${g})`}/>
     | This draws one piece of the page while JBIcon is showing.

  46 |       <path d="M 37 23 L 37 66 Q 37 80 20 80" stroke={`url(#${g})`} strokeWidth={sw} strokeLinecap="round" strokeLinejoin="round"/>
     | This draws one piece of the page while JBIcon is showing.

  47 |       <path d="M 55 23 L 55 80" stroke={`url(#${g})`} strokeWidth={sw} strokeLinecap="round"/>
     | This draws one piece of the page while JBIcon is showing.

  48 |       <path d="M 55 23 Q 78 23 78 38 Q 78 52 55 52" stroke={`url(#${g})`} strokeWidth={sw} strokeLinecap="round" strokeLinejoin="round"/>
     | This draws one piece of the page while JBIcon is showing.

  49 |       <path d="M 55 52 Q 82 52 82 66 Q 82 80 55 80" stroke={`url(#${g})`} strokeWidth={sw} strokeLinecap="round" strokeLinejoin="round"/>
     | This draws one piece of the page while JBIcon is showing.

  50 |     </svg>
     | This ends a drawing that JBIcon started just above.

  51 |   );
     | This closes a box of instructions that opened above.

  52 | }
     | This ends JBIcon (opened on line 7).

  53 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  54 | /**
     | A note for people. The app skips this line.

  55 |  * JumpyBrain Logo component.
     | A note for people. The app skips this line.

  56 |  *
     | A note for people. The app skips this line.

  57 |  * variant: "icon" | "full" | "mono-light" | "mono-dark"
     | A note for people. The app skips this line.

  58 |  * size: icon height in px (default 32)
     | A note for people. The app skips this line.

  59 |  * showWordmark: whether to show "Jumpy Brain" text beside icon (default true for "full")
     | A note for people. The app skips this line.

  60 |  */
     | A note for people. The app skips this line.

  61 | export default function Logo({ variant = "icon", size = 32, className = "", style = {} }) {
     | This starts Logo. Draws the JB mark. variant full adds the wordmark. The gradient id includes size and variant so two logos on one page do not clash.

  62 |   const gradId = `jbg-${size}-${variant}`;
     | This gives a short name to a value so the rest of Logo can use it.

  63 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  64 |   if (variant === "full") {
     | This asks a yes-or-no question. The next bit runs only on yes.

  65 |     return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  66 |       <span
     | This draws one piece of the page while Logo is showing.

  67 |         className={`jb-logo-full ${className}`}
     | This ends if (variant === "full") { (opened on line 64).

  68 |         style={{ display: "inline-flex", alignItems: "center", gap: size * 0.35, ...style }}
     | This ends if (variant === "full") { (opened on line 64).

  69 |         role="img"
     | Inside Logo, this line runs as written: role="img". It happens in order, after the line above it and before the line below it.

  70 |         aria-label="JumpyBrain"
     | Inside Logo, this line runs as written: aria-label="JumpyBrain". It happens in order, after the line above it and before the line below it.

  71 |       >
     | Inside Logo, this line runs as written: >. It happens in order, after the line above it and before the line below it.

  72 |         <JBIcon size={size} variant="color" gradId={gradId} />
     | This draws one piece of the page while Logo is showing.

  73 |         <span style={{
     | This draws one piece of the page while Logo is showing.

  74 |           fontSize: size * 0.5,
     | Inside Logo, this line runs as written: fontSize: size * 0.5,. It happens in order, after the line above it and before the line below it.

  75 |           fontWeight: 700,
     | Inside Logo, this line runs as written: fontWeight: 700,. It happens in order, after the line above it and before the line below it.

  76 |           lineHeight: 1,
     | Inside Logo, this line runs as written: lineHeight: 1,. It happens in order, after the line above it and before the line below it.

  77 |           letterSpacing: "-0.02em",
     | Inside Logo, this line runs as written: letterSpacing: "-0.02em",. It happens in order, after the line above it and before the line below it.

  78 |           color: "var(--text)",
     | Inside Logo, this line runs as written: color: "var(--text)",. It happens in order, after the line above it and before the line below it.

  79 |         }}>
     | This ends <span style={{ (opened on line 73).

  80 |           <span style={{ color: "var(--text)" }}>Jumpy</span>
     | This draws one piece of the page while Logo is showing.

  81 |           <span style={{
     | This draws one piece of the page while Logo is showing.

  82 |             background: "linear-gradient(135deg, #7C3AED, #06B6D4)",
     | Inside Logo, this line runs as written: background: "linear-gradient(135deg, #7C3AED, #06B6D4)",. It happens in order, after the line above it and before the line below it.

  83 |             WebkitBackgroundClip: "text",
     | Inside Logo, this line runs as written: WebkitBackgroundClip: "text",. It happens in order, after the line above it and before the line below it.

  84 |             WebkitTextFillColor: "transparent",
     | Inside Logo, this line runs as written: WebkitTextFillColor: "transparent",. It happens in order, after the line above it and before the line below it.

  85 |             backgroundClip: "text",
     | Inside Logo, this line runs as written: backgroundClip: "text",. It happens in order, after the line above it and before the line below it.

  86 |           }}> Brain</span>
     | This ends <span style={{ (opened on line 81).

  87 |         </span>
     | This ends a drawing that Logo started just above.

  88 |       </span>
     | This ends a drawing that Logo started just above.

  89 |     );
     | This closes a box of instructions that opened above.

  90 |   }
     | This ends if (variant === "full") { (opened on line 64).

  91 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  92 |   return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  93 |     <span
     | This draws one piece of the page while Logo is showing.

  94 |       className={`jb-logo ${className}`}
     | This ends Logo (opened on line 61).

  95 |       style={style}
     | This ends Logo (opened on line 61).

  96 |       role="img"
     | Inside Logo, this line runs as written: role="img". It happens in order, after the line above it and before the line below it.

  97 |       aria-label="JumpyBrain"
     | Inside Logo, this line runs as written: aria-label="JumpyBrain". It happens in order, after the line above it and before the line below it.

  98 |     >
     | Inside Logo, this line runs as written: >. It happens in order, after the line above it and before the line below it.

  99 |       <JBIcon size={size} variant={variant} gradId={gradId} />
     | This draws one piece of the page while Logo is showing.

 100 |     </span>
     | This ends a drawing that Logo started just above.

 101 |   );
     | This closes a box of instructions that opened above.

 102 | }
     | This ends Logo (opened on line 61).

