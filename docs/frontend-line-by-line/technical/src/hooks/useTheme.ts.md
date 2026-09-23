# `src/hooks/useTheme.ts`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import { useEffect } from 'react'
     | Import for an unused hook that writes five palettes as CSS variables: `import { useEffect } from 'react'`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   2 | import { useThemeStore, ThemeName } from '../stores/themeStore'
     | Import for an unused hook that writes five palettes as CSS variables: `import { useThemeStore, ThemeName } from '../stores/themeStore'`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   3 | 
     | Blank line in `src/hooks/useTheme.ts` (an unused hook that writes five palettes as CSS variables), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   4 | const themeVars: Record<ThemeName, Record<string, string>> = {
     | In `the top of the file` (src/hooks/useTheme.ts): declaration `const themeVars: Record<ThemeName, Record<string, string>> = {`.

   5 |   calm: {
     | In `the top of the file` (src/hooks/useTheme.ts): statement `calm: {`. It runs when the top of the file runs, in order, before the next line of the same function.

   6 |     '--bg-primary': '#f0f4f8',
     | In `the top of the file` (src/hooks/useTheme.ts): statement `'--bg-primary': '#f0f4f8',`. It runs when the top of the file runs, in order, before the next line of the same function.

   7 |     '--bg-secondary': '#ffffff',
     | In `the top of the file` (src/hooks/useTheme.ts): statement `'--bg-secondary': '#ffffff',`. It runs when the top of the file runs, in order, before the next line of the same function.

   8 |     '--text-primary': '#1a202c',
     | In `the top of the file` (src/hooks/useTheme.ts): statement `'--text-primary': '#1a202c',`. It runs when the top of the file runs, in order, before the next line of the same function.

   9 |     '--text-secondary': '#4a5568',
     | In `the top of the file` (src/hooks/useTheme.ts): statement `'--text-secondary': '#4a5568',`. It runs when the top of the file runs, in order, before the next line of the same function.

  10 |     '--accent': '#667eea',
     | In `the top of the file` (src/hooks/useTheme.ts): statement `'--accent': '#667eea',`. It runs when the top of the file runs, in order, before the next line of the same function.

  11 |     '--accent-light': '#ebf4ff',
     | In `the top of the file` (src/hooks/useTheme.ts): statement `'--accent-light': '#ebf4ff',`. It runs when the top of the file runs, in order, before the next line of the same function.

  12 |   },
     | In `the top of the file` (src/hooks/useTheme.ts): `},` closes calm: { (opened on line 5). Names declared inside that block end here.

  13 |   focus: {
     | In `the top of the file` (src/hooks/useTheme.ts): statement `focus: {`. It runs when the top of the file runs, in order, before the next line of the same function.

  14 |     '--bg-primary': '#1a1a2e',
     | In `the top of the file` (src/hooks/useTheme.ts): statement `'--bg-primary': '#1a1a2e',`. It runs when the top of the file runs, in order, before the next line of the same function.

  15 |     '--bg-secondary': '#16213e',
     | In `the top of the file` (src/hooks/useTheme.ts): statement `'--bg-secondary': '#16213e',`. It runs when the top of the file runs, in order, before the next line of the same function.

  16 |     '--text-primary': '#e2e8f0',
     | In `the top of the file` (src/hooks/useTheme.ts): statement `'--text-primary': '#e2e8f0',`. It runs when the top of the file runs, in order, before the next line of the same function.

  17 |     '--text-secondary': '#a0aec0',
     | In `the top of the file` (src/hooks/useTheme.ts): statement `'--text-secondary': '#a0aec0',`. It runs when the top of the file runs, in order, before the next line of the same function.

  18 |     '--accent': '#e94560',
     | In `the top of the file` (src/hooks/useTheme.ts): statement `'--accent': '#e94560',`. It runs when the top of the file runs, in order, before the next line of the same function.

  19 |     '--accent-light': '#2d1b2e',
     | In `the top of the file` (src/hooks/useTheme.ts): statement `'--accent-light': '#2d1b2e',`. It runs when the top of the file runs, in order, before the next line of the same function.

  20 |   },
     | In `the top of the file` (src/hooks/useTheme.ts): `},` closes focus: { (opened on line 13). Names declared inside that block end here.

  21 |   night: {
     | In `the top of the file` (src/hooks/useTheme.ts): statement `night: {`. It runs when the top of the file runs, in order, before the next line of the same function.

  22 |     '--bg-primary': '#0d1117',
     | In `the top of the file` (src/hooks/useTheme.ts): statement `'--bg-primary': '#0d1117',`. It runs when the top of the file runs, in order, before the next line of the same function.

  23 |     '--bg-secondary': '#161b22',
     | In `the top of the file` (src/hooks/useTheme.ts): statement `'--bg-secondary': '#161b22',`. It runs when the top of the file runs, in order, before the next line of the same function.

  24 |     '--text-primary': '#c9d1d9',
     | In `the top of the file` (src/hooks/useTheme.ts): statement `'--text-primary': '#c9d1d9',`. It runs when the top of the file runs, in order, before the next line of the same function.

  25 |     '--text-secondary': '#8b949e',
     | In `the top of the file` (src/hooks/useTheme.ts): statement `'--text-secondary': '#8b949e',`. It runs when the top of the file runs, in order, before the next line of the same function.

  26 |     '--accent': '#58a6ff',
     | In `the top of the file` (src/hooks/useTheme.ts): statement `'--accent': '#58a6ff',`. It runs when the top of the file runs, in order, before the next line of the same function.

  27 |     '--accent-light': '#1f3148',
     | In `the top of the file` (src/hooks/useTheme.ts): statement `'--accent-light': '#1f3148',`. It runs when the top of the file runs, in order, before the next line of the same function.

  28 |   },
     | In `the top of the file` (src/hooks/useTheme.ts): `},` closes night: { (opened on line 21). Names declared inside that block end here.

  29 |   highContrast: {
     | In `the top of the file` (src/hooks/useTheme.ts): statement `highContrast: {`. It runs when the top of the file runs, in order, before the next line of the same function.

  30 |     '--bg-primary': '#000000',
     | In `the top of the file` (src/hooks/useTheme.ts): statement `'--bg-primary': '#000000',`. It runs when the top of the file runs, in order, before the next line of the same function.

  31 |     '--bg-secondary': '#1a1a1a',
     | In `the top of the file` (src/hooks/useTheme.ts): statement `'--bg-secondary': '#1a1a1a',`. It runs when the top of the file runs, in order, before the next line of the same function.

  32 |     '--text-primary': '#ffffff',
     | In `the top of the file` (src/hooks/useTheme.ts): statement `'--text-primary': '#ffffff',`. It runs when the top of the file runs, in order, before the next line of the same function.

  33 |     '--text-secondary': '#ffff00',
     | In `the top of the file` (src/hooks/useTheme.ts): statement `'--text-secondary': '#ffff00',`. It runs when the top of the file runs, in order, before the next line of the same function.

  34 |     '--accent': '#00ff00',
     | In `the top of the file` (src/hooks/useTheme.ts): statement `'--accent': '#00ff00',`. It runs when the top of the file runs, in order, before the next line of the same function.

  35 |     '--accent-light': '#003300',
     | In `the top of the file` (src/hooks/useTheme.ts): statement `'--accent-light': '#003300',`. It runs when the top of the file runs, in order, before the next line of the same function.

  36 |   },
     | In `the top of the file` (src/hooks/useTheme.ts): `},` closes highContrast: { (opened on line 29). Names declared inside that block end here.

  37 |   minimal: {
     | In `the top of the file` (src/hooks/useTheme.ts): statement `minimal: {`. It runs when the top of the file runs, in order, before the next line of the same function.

  38 |     '--bg-primary': '#fafafa',
     | In `the top of the file` (src/hooks/useTheme.ts): statement `'--bg-primary': '#fafafa',`. It runs when the top of the file runs, in order, before the next line of the same function.

  39 |     '--bg-secondary': '#ffffff',
     | In `the top of the file` (src/hooks/useTheme.ts): statement `'--bg-secondary': '#ffffff',`. It runs when the top of the file runs, in order, before the next line of the same function.

  40 |     '--text-primary': '#212121',
     | In `the top of the file` (src/hooks/useTheme.ts): statement `'--text-primary': '#212121',`. It runs when the top of the file runs, in order, before the next line of the same function.

  41 |     '--text-secondary': '#757575',
     | In `the top of the file` (src/hooks/useTheme.ts): statement `'--text-secondary': '#757575',`. It runs when the top of the file runs, in order, before the next line of the same function.

  42 |     '--accent': '#212121',
     | In `the top of the file` (src/hooks/useTheme.ts): statement `'--accent': '#212121',`. It runs when the top of the file runs, in order, before the next line of the same function.

  43 |     '--accent-light': '#f5f5f5',
     | In `the top of the file` (src/hooks/useTheme.ts): statement `'--accent-light': '#f5f5f5',`. It runs when the top of the file runs, in order, before the next line of the same function.

  44 |   },
     | In `the top of the file` (src/hooks/useTheme.ts): `},` closes minimal: { (opened on line 37). Names declared inside that block end here.

  45 | }
     | In `the top of the file` (src/hooks/useTheme.ts): `}` closes const themeVars: Record<ThemeName, Record<string (opened on line 4). Names declared inside that block end here.

  46 | 
     | Blank line in `src/hooks/useTheme.ts` (an unused hook that writes five palettes as CSS variables), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  47 | export function useTheme() {
     | Named export from an unused hook that writes five palettes as CSS variables: `export function useTheme() {`.

  48 |   const { theme, setTheme } = useThemeStore()
     | In `useTheme` (src/hooks/useTheme.ts): `theme`: App's dark or light string. Written onto <html data-theme> and localStorage bb-theme. This is not the unused five-palette themeStore. The code is `const { theme, setTheme } = useThemeStore()`.

  49 | 
     | Blank line in `src/hooks/useTheme.ts` (an unused hook that writes five palettes as CSS variables), inside useTheme. The parser skips it. It separates the previous statement from the next so the function is readable.

  50 |   useEffect(() => {
     | In `useTheme` (src/hooks/useTheme.ts): opens or continues an effect — `useEffect(() => {`. The effect body runs after paint, and its cleanup runs before the next effect and on unmount.

  51 |     const vars = themeVars[theme]
     | In `useTheme` (src/hooks/useTheme.ts): `vars` is assigned `themeVars[theme]`. Later lines in this function read that name.

  52 |     const root = document.documentElement
     | In `useTheme` (src/hooks/useTheme.ts): `root` is assigned `document.documentElement`. Later lines in this function read that name.

  53 |     Object.entries(vars).forEach(([key, value]) => {
     | In `useTheme` (src/hooks/useTheme.ts): iteration `Object.entries(vars).forEach(([key, value]) => {`.

  54 |       root.style.setProperty(key, value)
     | In `useTheme` (src/hooks/useTheme.ts): statement `root.style.setProperty(key, value)`. It runs when useTheme runs, in order, before the next line of the same function.

  55 |     })
     | In `useTheme` (src/hooks/useTheme.ts): `})` closes Object.entries(vars).forEach(([key, value]) => { (opened on line 53). Names declared inside that block end here.

  56 |   }, [theme])
     | In `useTheme` (src/hooks/useTheme.ts): `}, [theme])` closes effect in useTheme (opened on line 50). Names declared inside that block end here.

  57 | 
     | Blank line in `src/hooks/useTheme.ts` (an unused hook that writes five palettes as CSS variables), inside useTheme. The parser skips it. It separates the previous statement from the next so the function is readable.

  58 |   return { theme, setTheme }
     | In `useTheme` (src/hooks/useTheme.ts): return `return { theme, setTheme }`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  59 | }
     | In `useTheme` (src/hooks/useTheme.ts): `}` closes useTheme (opened on line 47). Names declared inside that block end here.

