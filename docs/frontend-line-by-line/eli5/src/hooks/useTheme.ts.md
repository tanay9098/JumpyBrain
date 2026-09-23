# `src/hooks/useTheme.ts`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import { useEffect } from 'react'
     | Borrows React so this file can remember things and draw the screen.

   2 | import { useThemeStore, ThemeName } from '../stores/themeStore'
     | This file borrows a tool another file already made.

   3 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   4 | const themeVars: Record<ThemeName, Record<string, string>> = {
     | Five unused palettes (calm, focus, night, highContrast, minimal). The live theme is only dark/light, set by App on data-theme.

   5 |   calm: {
     | Inside the top of the file, this line runs as written: calm: {. It happens in order, after the line above it and before the line below it.

   6 |     '--bg-primary': '#f0f4f8',
     | Inside the top of the file, this line runs as written: '--bg-primary': '#f0f4f8',. It happens in order, after the line above it and before the line below it.

   7 |     '--bg-secondary': '#ffffff',
     | Inside the top of the file, this line runs as written: '--bg-secondary': '#ffffff',. It happens in order, after the line above it and before the line below it.

   8 |     '--text-primary': '#1a202c',
     | Inside the top of the file, this line runs as written: '--text-primary': '#1a202c',. It happens in order, after the line above it and before the line below it.

   9 |     '--text-secondary': '#4a5568',
     | Inside the top of the file, this line runs as written: '--text-secondary': '#4a5568',. It happens in order, after the line above it and before the line below it.

  10 |     '--accent': '#667eea',
     | Inside the top of the file, this line runs as written: '--accent': '#667eea',. It happens in order, after the line above it and before the line below it.

  11 |     '--accent-light': '#ebf4ff',
     | Inside the top of the file, this line runs as written: '--accent-light': '#ebf4ff',. It happens in order, after the line above it and before the line below it.

  12 |   },
     | This ends calm: { (opened on line 5).

  13 |   focus: {
     | Inside the top of the file, this line runs as written: focus: {. It happens in order, after the line above it and before the line below it.

  14 |     '--bg-primary': '#1a1a2e',
     | Inside the top of the file, this line runs as written: '--bg-primary': '#1a1a2e',. It happens in order, after the line above it and before the line below it.

  15 |     '--bg-secondary': '#16213e',
     | Inside the top of the file, this line runs as written: '--bg-secondary': '#16213e',. It happens in order, after the line above it and before the line below it.

  16 |     '--text-primary': '#e2e8f0',
     | Inside the top of the file, this line runs as written: '--text-primary': '#e2e8f0',. It happens in order, after the line above it and before the line below it.

  17 |     '--text-secondary': '#a0aec0',
     | Inside the top of the file, this line runs as written: '--text-secondary': '#a0aec0',. It happens in order, after the line above it and before the line below it.

  18 |     '--accent': '#e94560',
     | Inside the top of the file, this line runs as written: '--accent': '#e94560',. It happens in order, after the line above it and before the line below it.

  19 |     '--accent-light': '#2d1b2e',
     | Inside the top of the file, this line runs as written: '--accent-light': '#2d1b2e',. It happens in order, after the line above it and before the line below it.

  20 |   },
     | This ends focus: { (opened on line 13).

  21 |   night: {
     | Inside the top of the file, this line runs as written: night: {. It happens in order, after the line above it and before the line below it.

  22 |     '--bg-primary': '#0d1117',
     | Inside the top of the file, this line runs as written: '--bg-primary': '#0d1117',. It happens in order, after the line above it and before the line below it.

  23 |     '--bg-secondary': '#161b22',
     | Inside the top of the file, this line runs as written: '--bg-secondary': '#161b22',. It happens in order, after the line above it and before the line below it.

  24 |     '--text-primary': '#c9d1d9',
     | Inside the top of the file, this line runs as written: '--text-primary': '#c9d1d9',. It happens in order, after the line above it and before the line below it.

  25 |     '--text-secondary': '#8b949e',
     | Inside the top of the file, this line runs as written: '--text-secondary': '#8b949e',. It happens in order, after the line above it and before the line below it.

  26 |     '--accent': '#58a6ff',
     | Inside the top of the file, this line runs as written: '--accent': '#58a6ff',. It happens in order, after the line above it and before the line below it.

  27 |     '--accent-light': '#1f3148',
     | Inside the top of the file, this line runs as written: '--accent-light': '#1f3148',. It happens in order, after the line above it and before the line below it.

  28 |   },
     | This ends night: { (opened on line 21).

  29 |   highContrast: {
     | Inside the top of the file, this line runs as written: highContrast: {. It happens in order, after the line above it and before the line below it.

  30 |     '--bg-primary': '#000000',
     | Inside the top of the file, this line runs as written: '--bg-primary': '#000000',. It happens in order, after the line above it and before the line below it.

  31 |     '--bg-secondary': '#1a1a1a',
     | Inside the top of the file, this line runs as written: '--bg-secondary': '#1a1a1a',. It happens in order, after the line above it and before the line below it.

  32 |     '--text-primary': '#ffffff',
     | Inside the top of the file, this line runs as written: '--text-primary': '#ffffff',. It happens in order, after the line above it and before the line below it.

  33 |     '--text-secondary': '#ffff00',
     | Inside the top of the file, this line runs as written: '--text-secondary': '#ffff00',. It happens in order, after the line above it and before the line below it.

  34 |     '--accent': '#00ff00',
     | Inside the top of the file, this line runs as written: '--accent': '#00ff00',. It happens in order, after the line above it and before the line below it.

  35 |     '--accent-light': '#003300',
     | Inside the top of the file, this line runs as written: '--accent-light': '#003300',. It happens in order, after the line above it and before the line below it.

  36 |   },
     | This ends highContrast: { (opened on line 29).

  37 |   minimal: {
     | Inside the top of the file, this line runs as written: minimal: {. It happens in order, after the line above it and before the line below it.

  38 |     '--bg-primary': '#fafafa',
     | Inside the top of the file, this line runs as written: '--bg-primary': '#fafafa',. It happens in order, after the line above it and before the line below it.

  39 |     '--bg-secondary': '#ffffff',
     | Inside the top of the file, this line runs as written: '--bg-secondary': '#ffffff',. It happens in order, after the line above it and before the line below it.

  40 |     '--text-primary': '#212121',
     | Inside the top of the file, this line runs as written: '--text-primary': '#212121',. It happens in order, after the line above it and before the line below it.

  41 |     '--text-secondary': '#757575',
     | Inside the top of the file, this line runs as written: '--text-secondary': '#757575',. It happens in order, after the line above it and before the line below it.

  42 |     '--accent': '#212121',
     | Inside the top of the file, this line runs as written: '--accent': '#212121',. It happens in order, after the line above it and before the line below it.

  43 |     '--accent-light': '#f5f5f5',
     | Inside the top of the file, this line runs as written: '--accent-light': '#f5f5f5',. It happens in order, after the line above it and before the line below it.

  44 |   },
     | This ends minimal: { (opened on line 37).

  45 | }
     | This ends const themeVars: Record<ThemeName, Record<string (opened on line 4).

  46 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  47 | export function useTheme() {
     | This lets another file use this piece by its name.

  48 |   const { theme, setTheme } = useThemeStore()
     | App's dark or light string. Written onto <html data-theme> and localStorage bb-theme. This is not the unused five-palette themeStore.

  49 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  50 |   useEffect(() => {
     | This is an extra job that happens after the picture is drawn.

  51 |     const vars = themeVars[theme]
     | This gives a short name to a value so the rest of useTheme can use it.

  52 |     const root = document.documentElement
     | This gives a short name to a value so the rest of useTheme can use it.

  53 |     Object.entries(vars).forEach(([key, value]) => {
     | Inside useTheme, this line runs as written: Object.entries(vars).forEach(([key, value]) => {. It happens in order, after the line above it and before the line below it.

  54 |       root.style.setProperty(key, value)
     | Inside useTheme, this line runs as written: root.style.setProperty(key, value). It happens in order, after the line above it and before the line below it.

  55 |     })
     | This ends Object.entries(vars).forEach(([key, value]) => { (opened on line 53).

  56 |   }, [theme])
     | This ends effect in useTheme (opened on line 50).

  57 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  58 |   return { theme, setTheme }
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  59 | }
     | This ends useTheme (opened on line 47).

