# `src/themes/index.ts`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | export { useTheme } from '../hooks/useTheme'
     | This lets another file use this piece by its name.

   2 | export type { ThemeName } from '../stores/themeStore'
     | This lets another file use this piece by its name.

   3 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   4 | export const THEME_NAMES = ['calm', 'focus', 'night', 'highContrast', 'minimal'] as const
     | This lets another file use this piece by its name.

