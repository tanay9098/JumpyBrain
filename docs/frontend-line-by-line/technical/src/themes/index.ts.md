# `src/themes/index.ts`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | export { useTheme } from '../hooks/useTheme'
     | Named export from a re-export of the unused five-palette theme hook: `export { useTheme } from '../hooks/useTheme'`.

   2 | export type { ThemeName } from '../stores/themeStore'
     | Named export from a re-export of the unused five-palette theme hook: `export type { ThemeName } from '../stores/themeStore'`.

   3 | 
     | Blank line in `src/themes/index.ts` (a re-export of the unused five-palette theme hook), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   4 | export const THEME_NAMES = ['calm', 'focus', 'night', 'highContrast', 'minimal'] as const
     | Named export from a re-export of the unused five-palette theme hook: `export const THEME_NAMES = ['calm', 'focus', 'night', 'highContrast', 'minimal'] as const`.

