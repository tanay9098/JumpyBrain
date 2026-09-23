# `src/components/ProfileSettings.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import React, { useState } from "react";
     | Import for name, email, theme, and the coffee link: `import React, { useState } from "react";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   2 | import { Link } from "react-router-dom";
     | Import for name, email, theme, and the coffee link: `import { Link } from "react-router-dom";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   3 | import { useUser } from "../contexts/UserContext";
     | Import for name, email, theme, and the coffee link: `import { useUser } from "../contexts/UserContext";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   4 | 
     | Blank line in `src/components/ProfileSettings.jsx` (name, email, theme, and the coffee link), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   5 | // Sourced from .github/FUNDING.yml at build time (see vite.config.ts) so
     | Comment inside the top of the file. Not executed. It documents the next code: Sourced from .github/FUNDING.yml at build time (see vite.config.ts) so

   6 | // this link and the sidebar's support button never drift apart.
     | Comment inside the top of the file. Not executed. It documents the next code: this link and the sidebar's support button never drift apart.

   7 | const FUNDING_URL = __FUNDING_URL__;
     | In `the top of the file` (src/components/ProfileSettings.jsx): `FUNDING_URL`: The Buy Me a Coffee URL injected at build time from .github/FUNDING.yml by vite.config.ts as __FUNDING_URL__. The code is `const FUNDING_URL = __FUNDING_URL__;`.

   8 | 
     | Blank line in `src/components/ProfileSettings.jsx` (name, email, theme, and the coffee link), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   9 | function CoffeeIcon() {
     | Defines `CoffeeIcon` in name, email, theme, and the coffee link. The cup SVG next to the support link.

  10 |   return (
     | In `CoffeeIcon` (src/components/ProfileSettings.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  11 |     <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}>
     | In `CoffeeIcon` (src/components/ProfileSettings.jsx): Opens it. Vector drawing. It does not fetch data. Source: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}>`

  12 |       <path d="M18 8h1a3 3 0 010 6h-1" />
     | In `CoffeeIcon` (src/components/ProfileSettings.jsx): JSX `<path>`. React will create this node when the parent renders. Source: `<path d="M18 8h1a3 3 0 010 6h-1" />`

  13 |       <path d="M3 8h15v6a4 4 0 01-4 4H7a4 4 0 01-4-4V8z" />
     | In `CoffeeIcon` (src/components/ProfileSettings.jsx): JSX `<path>`. React will create this node when the parent renders. Source: `<path d="M3 8h15v6a4 4 0 01-4 4H7a4 4 0 01-4-4V8z" />`

  14 |       <path d="M6 2v2M10 2v2M14 2v2" />
     | In `CoffeeIcon` (src/components/ProfileSettings.jsx): JSX `<path>`. React will create this node when the parent renders. Source: `<path d="M6 2v2M10 2v2M14 2v2" />`

  15 |     </svg>
     | In `CoffeeIcon` (src/components/ProfileSettings.jsx): Closes it. Vector drawing. It does not fetch data. Source: `</svg>`

  16 |   );
     | In `CoffeeIcon` (src/components/ProfileSettings.jsx): statement `);`. It runs when CoffeeIcon runs, in order, before the next line of the same function.

  17 | }
     | In `CoffeeIcon` (src/components/ProfileSettings.jsx): `}` closes CoffeeIcon (opened on line 9). Names declared inside that block end here.

  18 | 
     | Blank line in `src/components/ProfileSettings.jsx` (name, email, theme, and the coffee link), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  19 | const GENDER_OPTIONS = [
     | In `the top of the file` (src/components/ProfileSettings.jsx): `GENDER_OPTIONS`: The profile form's gender select. Empty string and prefer-not-to-say are both offered. The code is `const GENDER_OPTIONS = [`.

  20 |   { value: "", label: "Prefer not to say" },
     | In `the top of the file` (src/components/ProfileSettings.jsx): `{ value: "", label: "Prefer not to say" },` closes the nearest open block. Names declared inside that block end here.

  21 |   { value: "male", label: "Male" },
     | In `the top of the file` (src/components/ProfileSettings.jsx): `{ value: "male", label: "Male" },` closes the nearest open block. Names declared inside that block end here.

  22 |   { value: "female", label: "Female" },
     | In `the top of the file` (src/components/ProfileSettings.jsx): `{ value: "female", label: "Female" },` closes the nearest open block. Names declared inside that block end here.

  23 |   { value: "non-binary", label: "Non-binary" },
     | In `the top of the file` (src/components/ProfileSettings.jsx): `{ value: "non-binary", label: "Non-binary" },` closes the nearest open block. Names declared inside that block end here.

  24 |   { value: "prefer-not-to-say", label: "Rather not say" },
     | In `the top of the file` (src/components/ProfileSettings.jsx): `{ value: "prefer-not-to-say", label: "Rather not say" },` closes the nearest open block. Names declared inside that block end here.

  25 | ];
     | In `the top of the file` (src/components/ProfileSettings.jsx): statement `];`. It runs when the top of the file runs, in order, before the next line of the same function.

  26 | 
     | Blank line in `src/components/ProfileSettings.jsx` (name, email, theme, and the coffee link), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  27 | function getInitials(name, email) {
     | Defines `getInitials` in name, email, theme, and the coffee link. First letters of the first two words, or the email's first character. Same rule as the top-bar avatar.

  28 |   if (name && name.trim()) {
     | In `getInitials` (src/components/ProfileSettings.jsx): branch `if (name && name.trim()) {`. Only one side runs.

  29 |     return name
     | In `getInitials` (src/components/ProfileSettings.jsx): return `return name`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  30 |       .trim()
     | In `getInitials` (src/components/ProfileSettings.jsx): statement `.trim()`. It runs when getInitials runs, in order, before the next line of the same function.

  31 |       .split(/\s+/)
     | In `getInitials` (src/components/ProfileSettings.jsx): statement `.split(/\s+/)`. It runs when getInitials runs, in order, before the next line of the same function.

  32 |       .slice(0, 2)
     | In `getInitials` (src/components/ProfileSettings.jsx): statement `.slice(0, 2)`. It runs when getInitials runs, in order, before the next line of the same function.

  33 |       .map((w) => w[0].toUpperCase())
     | In `getInitials` (src/components/ProfileSettings.jsx): iteration `.map((w) => w[0].toUpperCase())`.

  34 |       .join("");
     | In `getInitials` (src/components/ProfileSettings.jsx): statement `.join("");`. It runs when getInitials runs, in order, before the next line of the same function.

  35 |   }
     | In `getInitials` (src/components/ProfileSettings.jsx): `}` closes if (name && name.trim()) { (opened on line 28). Names declared inside that block end here.

  36 |   return (email || "?")[0].toUpperCase();
     | In `getInitials` (src/components/ProfileSettings.jsx): return `return (email || "?")[0].toUpperCase();`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  37 | }
     | In `getInitials` (src/components/ProfileSettings.jsx): `}` closes getInitials (opened on line 27). Names declared inside that block end here.

  38 | 
     | Blank line in `src/components/ProfileSettings.jsx` (name, email, theme, and the coffee link), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  39 | export default function ProfileSettings({ onThemeChange }) {
     | Defines `ProfileSettings` in name, email, theme, and the coffee link. Edits name, email, gender through updateUser, and saves preferredTheme both on the server and into App's theme state.

  40 |   const { user, updateUser } = useUser();
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): `user`: The logged-in profile object. Null means ProtectedRoute renders Auth. The code is `const { user, updateUser } = useUser();`.

  41 | 
     | Blank line in `src/components/ProfileSettings.jsx` (name, email, theme, and the coffee link), inside ProfileSettings. The parser skips it. It separates the previous statement from the next so the function is readable.

  42 |   const [profileForm, setProfileForm] = useState({
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): React state `profileForm, setProfileForm`. The value survives re-renders. Calling the setter re-renders this component. `const [profileForm, setProfileForm] = useState({`

  43 |     name: user?.name || "",
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): statement `name: user?.name || "",`. It runs when ProfileSettings runs, in order, before the next line of the same function.

  44 |     email: user?.email || "",
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): statement `email: user?.email || "",`. It runs when ProfileSettings runs, in order, before the next line of the same function.

  45 |     gender: user?.gender || "",
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): statement `gender: user?.gender || "",`. It runs when ProfileSettings runs, in order, before the next line of the same function.

  46 |   });
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): `});` closes const [profileForm, setProfileForm] = useState({ (opened on line 42). Names declared inside that block end here.

  47 |   const [profileSaving, setProfileSaving] = useState(false);
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): React state `profileSaving, setProfileSaving`. The value survives re-renders. Calling the setter re-renders this component. `const [profileSaving, setProfileSaving] = useState(false);`

  48 |   const [profileMsg, setProfileMsg] = useState(null);
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): React state `profileMsg, setProfileMsg`. The value survives re-renders. Calling the setter re-renders this component. `const [profileMsg, setProfileMsg] = useState(null);`

  49 | 
     | Blank line in `src/components/ProfileSettings.jsx` (name, email, theme, and the coffee link), inside ProfileSettings. The parser skips it. It separates the previous statement from the next so the function is readable.

  50 |   const [selectedTheme, setSelectedTheme] = useState(user?.preferredTheme || "dark");
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): React state `selectedTheme, setSelectedTheme`. The value survives re-renders. Calling the setter re-renders this component. `const [selectedTheme, setSelectedTheme] = useState(user?.preferredTheme || "dark");`

  51 |   const [themeSaving, setThemeSaving] = useState(false);
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): React state `themeSaving, setThemeSaving`. The value survives re-renders. Calling the setter re-renders this component. `const [themeSaving, setThemeSaving] = useState(false);`

  52 |   const [themeMsg, setThemeMsg] = useState(null);
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): React state `themeMsg, setThemeMsg`. The value survives re-renders. Calling the setter re-renders this component. `const [themeMsg, setThemeMsg] = useState(null);`

  53 | 
     | Blank line in `src/components/ProfileSettings.jsx` (name, email, theme, and the coffee link), inside ProfileSettings. The parser skips it. It separates the previous statement from the next so the function is readable.

  54 |   async function handleProfileSave(e) {
     | Defines `handleProfileSave` in name, email, theme, and the coffee link. preventDefault, then updateUser. The success or error string is profileMsg.

  55 |     e.preventDefault();
     | In `handleProfileSave` (src/components/ProfileSettings.jsx): statement `e.preventDefault();`. It runs when handleProfileSave runs, in order, before the next line of the same function.

  56 |     setProfileSaving(true);
     | In `handleProfileSave` (src/components/ProfileSettings.jsx): statement `setProfileSaving(true);`. It runs when handleProfileSave runs, in order, before the next line of the same function.

  57 |     setProfileMsg(null);
     | In `handleProfileSave` (src/components/ProfileSettings.jsx): statement `setProfileMsg(null);`. It runs when handleProfileSave runs, in order, before the next line of the same function.

  58 |     try {
     | In `handleProfileSave` (src/components/ProfileSettings.jsx): error path `try {`.

  59 |       await updateUser({
     | In `handleProfileSave` (src/components/ProfileSettings.jsx): `await updateUser({`. The async function suspends until the promise fulfills, then assigns or continues.

  60 |         name: profileForm.name,
     | In `handleProfileSave` (src/components/ProfileSettings.jsx): statement `name: profileForm.name,`. It runs when handleProfileSave runs, in order, before the next line of the same function.

  61 |         email: profileForm.email,
     | In `handleProfileSave` (src/components/ProfileSettings.jsx): statement `email: profileForm.email,`. It runs when handleProfileSave runs, in order, before the next line of the same function.

  62 |         gender: profileForm.gender,
     | In `handleProfileSave` (src/components/ProfileSettings.jsx): statement `gender: profileForm.gender,`. It runs when handleProfileSave runs, in order, before the next line of the same function.

  63 |       });
     | In `handleProfileSave` (src/components/ProfileSettings.jsx): `});` closes await updateUser({ (opened on line 59). Names declared inside that block end here.

  64 |       setProfileMsg({ type: "success", text: "Profile updated successfully" });
     | In `handleProfileSave` (src/components/ProfileSettings.jsx): `setProfileMsg({ type: "success", text: "Profile updated successfully" });` closes try { (opened on line 58). Names declared inside that block end here.

  65 |     } catch (err) {
     | In `handleProfileSave` (src/components/ProfileSettings.jsx): `} catch (err) {` closes try { (opened on line 58). Names declared inside that block end here.

  66 |       const msg = err?.response?.data?.error || "Failed to update profile";
     | In `handleProfileSave` (src/components/ProfileSettings.jsx): `msg` is assigned `err?.response?.data?.error || "Failed to update profile";`. Later lines in this function read that name.

  67 |       setProfileMsg({ type: "error", text: msg });
     | In `handleProfileSave` (src/components/ProfileSettings.jsx): `setProfileMsg({ type: "error", text: msg });` closes } catch (err) { (opened on line 65). Names declared inside that block end here.

  68 |     } finally {
     | In `handleProfileSave` (src/components/ProfileSettings.jsx): `} finally {` closes } catch (err) { (opened on line 65). Names declared inside that block end here.

  69 |       setProfileSaving(false);
     | In `handleProfileSave` (src/components/ProfileSettings.jsx): statement `setProfileSaving(false);`. It runs when handleProfileSave runs, in order, before the next line of the same function.

  70 |     }
     | In `handleProfileSave` (src/components/ProfileSettings.jsx): `}` closes } finally { (opened on line 68). Names declared inside that block end here.

  71 |   }
     | In `handleProfileSave` (src/components/ProfileSettings.jsx): `}` closes handleProfileSave (opened on line 54). Names declared inside that block end here.

  72 | 
     | Blank line in `src/components/ProfileSettings.jsx` (name, email, theme, and the coffee link), inside ProfileSettings. The parser skips it. It separates the previous statement from the next so the function is readable.

  73 |   async function handleThemeSave(theme) {
     | Defines `handleThemeSave` in name, email, theme, and the coffee link. PUT preferredTheme, then onThemeChange so the shell updates before the next navigation.

  74 |     setThemeSaving(true);
     | In `handleThemeSave` (src/components/ProfileSettings.jsx): statement `setThemeSaving(true);`. It runs when handleThemeSave runs, in order, before the next line of the same function.

  75 |     setThemeMsg(null);
     | In `handleThemeSave` (src/components/ProfileSettings.jsx): statement `setThemeMsg(null);`. It runs when handleThemeSave runs, in order, before the next line of the same function.

  76 |     try {
     | In `handleThemeSave` (src/components/ProfileSettings.jsx): error path `try {`.

  77 |       await updateUser({ preferredTheme: theme });
     | In `handleThemeSave` (src/components/ProfileSettings.jsx): `await updateUser({ preferredTheme: theme });`. The async function suspends until the promise fulfills, then assigns or continues.

  78 |       onThemeChange(theme);
     | In `handleThemeSave` (src/components/ProfileSettings.jsx): statement `onThemeChange(theme);`. It runs when handleThemeSave runs, in order, before the next line of the same function.

  79 |       setThemeMsg({ type: "success", text: "Theme saved" });
     | In `handleThemeSave` (src/components/ProfileSettings.jsx): `setThemeMsg({ type: "success", text: "Theme saved" });` closes try { (opened on line 76). Names declared inside that block end here.

  80 |       setTimeout(() => setThemeMsg(null), 2000);
     | In `handleThemeSave` (src/components/ProfileSettings.jsx): timer — `setTimeout(() => setThemeMsg(null), 2000);`. The callback runs later on the event loop, not now.

  81 |     } catch {
     | In `handleThemeSave` (src/components/ProfileSettings.jsx): `} catch {` closes try { (opened on line 76). Names declared inside that block end here.

  82 |       setThemeMsg({ type: "error", text: "Failed to save theme" });
     | In `handleThemeSave` (src/components/ProfileSettings.jsx): `setThemeMsg({ type: "error", text: "Failed to save theme" });` closes } catch { (opened on line 81). Names declared inside that block end here.

  83 |     } finally {
     | In `handleThemeSave` (src/components/ProfileSettings.jsx): `} finally {` closes } catch { (opened on line 81). Names declared inside that block end here.

  84 |       setThemeSaving(false);
     | In `handleThemeSave` (src/components/ProfileSettings.jsx): statement `setThemeSaving(false);`. It runs when handleThemeSave runs, in order, before the next line of the same function.

  85 |     }
     | In `handleThemeSave` (src/components/ProfileSettings.jsx): `}` closes } finally { (opened on line 83). Names declared inside that block end here.

  86 |   }
     | In `handleThemeSave` (src/components/ProfileSettings.jsx): `}` closes handleThemeSave (opened on line 73). Names declared inside that block end here.

  87 | 
     | Blank line in `src/components/ProfileSettings.jsx` (name, email, theme, and the coffee link), inside ProfileSettings. The parser skips it. It separates the previous statement from the next so the function is readable.

  88 |   function handleThemeSelect(theme) {
     | Defines `handleThemeSelect` in name, email, theme, and the coffee link. Sets the local highlight and immediately saves. There is no separate Save button for theme.

  89 |     setSelectedTheme(theme);
     | In `handleThemeSelect` (src/components/ProfileSettings.jsx): statement `setSelectedTheme(theme);`. It runs when handleThemeSelect runs, in order, before the next line of the same function.

  90 |     handleThemeSave(theme);
     | In `handleThemeSelect` (src/components/ProfileSettings.jsx): statement `handleThemeSave(theme);`. It runs when handleThemeSelect runs, in order, before the next line of the same function.

  91 |   }
     | In `handleThemeSelect` (src/components/ProfileSettings.jsx): `}` closes handleThemeSelect (opened on line 88). Names declared inside that block end here.

  92 | 
     | Blank line in `src/components/ProfileSettings.jsx` (name, email, theme, and the coffee link), inside ProfileSettings. The parser skips it. It separates the previous statement from the next so the function is readable.

  93 |   return (
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  94 |     <div className="profile-settings-page">
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="profile-settings-page">`

  95 |       <div className="profile-settings-container">
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="profile-settings-container">`

  96 |         <div className="profile-settings-header">
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="profile-settings-header">`

  97 |           <h1 className="profile-settings-title">Profile &amp; Settings</h1>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. The page title. Source: `<h1 className="profile-settings-title">Profile &amp; Settings</h1>`

  98 |           <p className="profile-settings-subtitle">Manage your account details and appearance</p>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. A paragraph. Source: `<p className="profile-settings-subtitle">Manage your account details and appearance</p>`

  99 |         </div>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 100 | 
     | Blank line in `src/components/ProfileSettings.jsx` (name, email, theme, and the coffee link), inside ProfileSettings. The parser skips it. It separates the previous statement from the next so the function is readable.

 101 |         {/* Focus Shield quick access — mobile users land here from Profile too */}
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): `{/* Focus Shield quick access — mobile users land here from Profile too */}` closes ProfileSettings (opened on line 39). Names declared inside that block end here.

 102 |         <Link to="/blocking" className="profile-settings-card fs-quick-link">
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. A react-router link. Clicking it changes the URL without a full page reload. Source: `<Link to="/blocking" className="profile-settings-card fs-quick-link">`

 103 |           <span className="fs-quick-link-icon" aria-hidden="true">🛡️</span>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. An inline box. Source: `<span className="fs-quick-link-icon" aria-hidden="true">🛡️</span>`

 104 |           <span style={{ flex: 1, minWidth: 0 }}>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. An inline box. Source: `<span style={{ flex: 1, minWidth: 0 }}>`

 105 |             <span className="profile-settings-card-title" style={{ display: "block" }}>Focus Shield</span>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. An inline box. Source: `<span className="profile-settings-card-title" style={{ display: "block" }}>Focus Shield</span>`

 106 |             <span className="profile-settings-card-desc" style={{ display: "block", marginTop: 2 }}>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. An inline box. Source: `<span className="profile-settings-card-desc" style={{ display: "block", marginTop: 2 }}>`

 107 |               Manage blocked & whitelisted websites
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): statement `Manage blocked & whitelisted websites`. It runs when ProfileSettings runs, in order, before the next line of the same function.

 108 |             </span>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Closes it. An inline box. Source: `</span>`

 109 |           </span>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Closes it. An inline box. Source: `</span>`

 110 |           <span aria-hidden="true">→</span>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. An inline box. Source: `<span aria-hidden="true">→</span>`

 111 |         </Link>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Closes it. A react-router link. Clicking it changes the URL without a full page reload. Source: `</Link>`

 112 | 
     | Blank line in `src/components/ProfileSettings.jsx` (name, email, theme, and the coffee link), inside ProfileSettings. The parser skips it. It separates the previous statement from the next so the function is readable.

 113 |         {/* Profile Info */}
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): `{/* Profile Info */}` closes ProfileSettings (opened on line 39). Names declared inside that block end here.

 114 |         <section className="profile-settings-card">
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. A grouped block on the settings-style pages. Source: `<section className="profile-settings-card">`

 115 |           <div className="profile-settings-card-header">
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="profile-settings-card-header">`

 116 |             <h2 className="profile-settings-card-title">Profile Information</h2>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): JSX `<h2>`. React will create this node when the parent renders.. className chooses the CSS rules from styles.css Source: `<h2 className="profile-settings-card-title">Profile Information</h2>`

 117 |           </div>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 118 | 
     | Blank line in `src/components/ProfileSettings.jsx` (name, email, theme, and the coffee link), inside ProfileSettings. The parser skips it. It separates the previous statement from the next so the function is readable.

 119 |           <div className="profile-avatar-row">
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="profile-avatar-row">`

 120 |             <div className="profile-avatar">
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="profile-avatar">`

 121 |               {getInitials(user?.name, user?.email)}
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): `{getInitials(user?.name, user?.email)}` closes ProfileSettings (opened on line 39). Names declared inside that block end here.

 122 |             </div>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 123 |             <div>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. A box that groups the elements inside it. Source: `<div>`

 124 |               <div className="profile-avatar-name">{user?.name || "No name set"}</div>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="profile-avatar-name">{user?.name || "No name set"}</div>`

 125 |               <div className="profile-avatar-email">{user?.email}</div>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="profile-avatar-email">{user?.email}</div>`

 126 |             </div>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 127 |           </div>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 128 | 
     | Blank line in `src/components/ProfileSettings.jsx` (name, email, theme, and the coffee link), inside ProfileSettings. The parser skips it. It separates the previous statement from the next so the function is readable.

 129 |           <form onSubmit={handleProfileSave} className="profile-form">
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. A form. onSubmit runs handleProfileSave. Source: `<form onSubmit={handleProfileSave} className="profile-form">`

 130 |             <div className="profile-form-grid">
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="profile-form-grid">`

 131 |               <div className="profile-form-field">
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="profile-form-field">`

 132 |                 <label className="profile-form-label" htmlFor="ps-name">Display Name</label>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. The caption for an input. Source: `<label className="profile-form-label" htmlFor="ps-name">Display Name</label>`

 133 |                 <input
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. A text or date field. If value and onChange are set, React owns what it shows. Source: `<input`

 134 |                   id="ps-name"
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): statement `id="ps-name"`. It runs when ProfileSettings runs, in order, before the next line of the same function.

 135 |                   className="profile-form-input"
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): statement `className="profile-form-input"`. It runs when ProfileSettings runs, in order, before the next line of the same function.

 136 |                   type="text"
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): statement `type="text"`. It runs when ProfileSettings runs, in order, before the next line of the same function.

 137 |                   value={profileForm.name}
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): `value={profileForm.name}` closes ProfileSettings (opened on line 39). Names declared inside that block end here.

 138 |                   onChange={(e) => setProfileForm((f) => ({ ...f, name: e.target.value }))}
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): event prop `onChange={(e) => setProfileForm((f) => ({ ...f, name: e.target.value }))}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 139 |                   placeholder="Your name"
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): statement `placeholder="Your name"`. It runs when ProfileSettings runs, in order, before the next line of the same function.

 140 |                   maxLength={100}
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): `maxLength={100}` closes ProfileSettings (opened on line 39). Names declared inside that block end here.

 141 |                   autoComplete="name"
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): statement `autoComplete="name"`. It runs when ProfileSettings runs, in order, before the next line of the same function.

 142 |                 />
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): statement `/>`. It runs when ProfileSettings runs, in order, before the next line of the same function.

 143 |               </div>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 144 | 
     | Blank line in `src/components/ProfileSettings.jsx` (name, email, theme, and the coffee link), inside ProfileSettings. The parser skips it. It separates the previous statement from the next so the function is readable.

 145 |               <div className="profile-form-field">
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="profile-form-field">`

 146 |                 <label className="profile-form-label" htmlFor="ps-email">Email Address</label>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. The caption for an input. Source: `<label className="profile-form-label" htmlFor="ps-email">Email Address</label>`

 147 |                 <input
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. A text or date field. If value and onChange are set, React owns what it shows. Source: `<input`

 148 |                   id="ps-email"
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): statement `id="ps-email"`. It runs when ProfileSettings runs, in order, before the next line of the same function.

 149 |                   className="profile-form-input"
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): statement `className="profile-form-input"`. It runs when ProfileSettings runs, in order, before the next line of the same function.

 150 |                   type="email"
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): statement `type="email"`. It runs when ProfileSettings runs, in order, before the next line of the same function.

 151 |                   value={profileForm.email}
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): `value={profileForm.email}` closes ProfileSettings (opened on line 39). Names declared inside that block end here.

 152 |                   onChange={(e) => setProfileForm((f) => ({ ...f, email: e.target.value }))}
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): event prop `onChange={(e) => setProfileForm((f) => ({ ...f, email: e.target.value }))}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 153 |                   placeholder="you@example.com"
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): statement `placeholder="you@example.com"`. It runs when ProfileSettings runs, in order, before the next line of the same function.

 154 |                   autoComplete="email"
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): statement `autoComplete="email"`. It runs when ProfileSettings runs, in order, before the next line of the same function.

 155 |                 />
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): statement `/>`. It runs when ProfileSettings runs, in order, before the next line of the same function.

 156 |               </div>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 157 | 
     | Blank line in `src/components/ProfileSettings.jsx` (name, email, theme, and the coffee link), inside ProfileSettings. The parser skips it. It separates the previous statement from the next so the function is readable.

 158 |               <div className="profile-form-field">
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="profile-form-field">`

 159 |                 <label className="profile-form-label" htmlFor="ps-gender">Gender</label>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. The caption for an input. Source: `<label className="profile-form-label" htmlFor="ps-gender">Gender</label>`

 160 |                 <select
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. A dropdown. onChange writes the chosen value into state. Source: `<select`

 161 |                   id="ps-gender"
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): statement `id="ps-gender"`. It runs when ProfileSettings runs, in order, before the next line of the same function.

 162 |                   className="profile-form-input profile-form-select"
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): statement `className="profile-form-input profile-form-select"`. It runs when ProfileSettings runs, in order, before the next line of the same function.

 163 |                   value={profileForm.gender}
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): `value={profileForm.gender}` closes ProfileSettings (opened on line 39). Names declared inside that block end here.

 164 |                   onChange={(e) => setProfileForm((f) => ({ ...f, gender: e.target.value }))}
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): event prop `onChange={(e) => setProfileForm((f) => ({ ...f, gender: e.target.value }))}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 165 |                 >
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): statement `>`. It runs when ProfileSettings runs, in order, before the next line of the same function.

 166 |                   {GENDER_OPTIONS.map((o) => (
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): iteration `{GENDER_OPTIONS.map((o) => (`.

 167 |                     <option key={o.value} value={o.value}>{o.label}</option>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): JSX `<option>`. React will create this node when the parent renders.. value is controlled by React state, so the DOM shows that state Source: `<option key={o.value} value={o.value}>{o.label}</option>`

 168 |                   ))}
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): `))}` closes ProfileSettings (opened on line 39). Names declared inside that block end here.

 169 |                 </select>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Closes it. A dropdown. onChange writes the chosen value into state. Source: `</select>`

 170 |               </div>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 171 |             </div>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 172 | 
     | Blank line in `src/components/ProfileSettings.jsx` (name, email, theme, and the coffee link), inside ProfileSettings. The parser skips it. It separates the previous statement from the next so the function is readable.

 173 |             {profileMsg && (
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): statement `{profileMsg && (`. It runs when ProfileSettings runs, in order, before the next line of the same function.

 174 |               <div className={`profile-msg profile-msg--${profileMsg.type}`}>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. A box that groups the elements inside it. Source: `<div className={`profile-msg profile-msg--${profileMsg.type}`}>`

 175 |                 {profileMsg.text}
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): `{profileMsg.text}` closes ProfileSettings (opened on line 39). Names declared inside that block end here.

 176 |               </div>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 177 |             )}
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): `)}` closes ProfileSettings (opened on line 39). Names declared inside that block end here.

 178 | 
     | Blank line in `src/components/ProfileSettings.jsx` (name, email, theme, and the coffee link), inside ProfileSettings. The parser skips it. It separates the previous statement from the next so the function is readable.

 179 |             <div className="profile-form-actions">
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="profile-form-actions">`

 180 |               <button
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button`

 181 |                 type="submit"
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): statement `type="submit"`. It runs when ProfileSettings runs, in order, before the next line of the same function.

 182 |                 className="profile-save-btn"
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): statement `className="profile-save-btn"`. It runs when ProfileSettings runs, in order, before the next line of the same function.

 183 |                 disabled={profileSaving}
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): `disabled={profileSaving}` closes ProfileSettings (opened on line 39). Names declared inside that block end here.

 184 |               >
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): statement `>`. It runs when ProfileSettings runs, in order, before the next line of the same function.

 185 |                 {profileSaving ? "Saving…" : "Save Profile"}
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): `{profileSaving ? "Saving…" : "Save Profile"}` closes ProfileSettings (opened on line 39). Names declared inside that block end here.

 186 |               </button>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

 187 |             </div>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 188 |           </form>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Closes it. A form. onSubmit runs handleProfileSave. Source: `</form>`

 189 |         </section>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Closes it. A grouped block on the settings-style pages. Source: `</section>`

 190 | 
     | Blank line in `src/components/ProfileSettings.jsx` (name, email, theme, and the coffee link), inside ProfileSettings. The parser skips it. It separates the previous statement from the next so the function is readable.

 191 |         {/* Appearance */}
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): `{/* Appearance */}` closes ProfileSettings (opened on line 39). Names declared inside that block end here.

 192 |         <section className="profile-settings-card">
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. A grouped block on the settings-style pages. Source: `<section className="profile-settings-card">`

 193 |           <div className="profile-settings-card-header">
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="profile-settings-card-header">`

 194 |             <h2 className="profile-settings-card-title">Appearance</h2>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): JSX `<h2>`. React will create this node when the parent renders.. className chooses the CSS rules from styles.css Source: `<h2 className="profile-settings-card-title">Appearance</h2>`

 195 |             <p className="profile-settings-card-desc">Choose how JumpyBrain looks for you</p>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. A paragraph. Source: `<p className="profile-settings-card-desc">Choose how JumpyBrain looks for you</p>`

 196 |           </div>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 197 | 
     | Blank line in `src/components/ProfileSettings.jsx` (name, email, theme, and the coffee link), inside ProfileSettings. The parser skips it. It separates the previous statement from the next so the function is readable.

 198 |           <div className="theme-picker">
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="theme-picker">`

 199 |             <button
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button`

 200 |               className={`theme-option${selectedTheme === "dark" ? " active" : ""}`}
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): `className={`theme-option${selectedTheme === "dark" ? " active" : ""}`}` closes ProfileSettings (opened on line 39). Names declared inside that block end here.

 201 |               onClick={() => handleThemeSelect("dark")}
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): event prop `onClick={() => handleThemeSelect("dark")}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 202 |               disabled={themeSaving}
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): `disabled={themeSaving}` closes ProfileSettings (opened on line 39). Names declared inside that block end here.

 203 |               type="button"
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): statement `type="button"`. It runs when ProfileSettings runs, in order, before the next line of the same function.

 204 |               aria-pressed={selectedTheme === "dark"}
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): `aria-pressed={selectedTheme === "dark"}` closes ProfileSettings (opened on line 39). Names declared inside that block end here.

 205 |             >
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): statement `>`. It runs when ProfileSettings runs, in order, before the next line of the same function.

 206 |               <div className="theme-option-preview theme-option-preview--dark">
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="theme-option-preview theme-option-preview--dark">`

 207 |                 <div className="theme-preview-bar" />
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="theme-preview-bar" />`

 208 |                 <div className="theme-preview-card" />
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="theme-preview-card" />`

 209 |                 <div className="theme-preview-card theme-preview-card--sm" />
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="theme-preview-card theme-preview-card--sm" />`

 210 |               </div>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 211 |               <div className="theme-option-label">
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="theme-option-label">`

 212 |                 <span className="theme-option-name">Dark</span>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. An inline box. Source: `<span className="theme-option-name">Dark</span>`

 213 |                 <span className="theme-option-desc">Easy on the eyes at night</span>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. An inline box. Source: `<span className="theme-option-desc">Easy on the eyes at night</span>`

 214 |               </div>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 215 |               {selectedTheme === "dark" && <span className="theme-option-check">✓</span>}
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): `{selectedTheme === "dark" && <span className="theme-option-check">✓</span>}` closes ProfileSettings (opened on line 39). Names declared inside that block end here.

 216 |             </button>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

 217 | 
     | Blank line in `src/components/ProfileSettings.jsx` (name, email, theme, and the coffee link), inside ProfileSettings. The parser skips it. It separates the previous statement from the next so the function is readable.

 218 |             <button
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button`

 219 |               className={`theme-option${selectedTheme === "light" ? " active" : ""}`}
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): `className={`theme-option${selectedTheme === "light" ? " active" : ""}`}` closes ProfileSettings (opened on line 39). Names declared inside that block end here.

 220 |               onClick={() => handleThemeSelect("light")}
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): event prop `onClick={() => handleThemeSelect("light")}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 221 |               disabled={themeSaving}
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): `disabled={themeSaving}` closes ProfileSettings (opened on line 39). Names declared inside that block end here.

 222 |               type="button"
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): statement `type="button"`. It runs when ProfileSettings runs, in order, before the next line of the same function.

 223 |               aria-pressed={selectedTheme === "light"}
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): `aria-pressed={selectedTheme === "light"}` closes ProfileSettings (opened on line 39). Names declared inside that block end here.

 224 |             >
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): statement `>`. It runs when ProfileSettings runs, in order, before the next line of the same function.

 225 |               <div className="theme-option-preview theme-option-preview--light">
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="theme-option-preview theme-option-preview--light">`

 226 |                 <div className="theme-preview-bar" />
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="theme-preview-bar" />`

 227 |                 <div className="theme-preview-card" />
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="theme-preview-card" />`

 228 |                 <div className="theme-preview-card theme-preview-card--sm" />
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="theme-preview-card theme-preview-card--sm" />`

 229 |               </div>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 230 |               <div className="theme-option-label">
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="theme-option-label">`

 231 |                 <span className="theme-option-name">Light</span>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. An inline box. Source: `<span className="theme-option-name">Light</span>`

 232 |                 <span className="theme-option-desc">Bright and clear</span>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. An inline box. Source: `<span className="theme-option-desc">Bright and clear</span>`

 233 |               </div>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 234 |               {selectedTheme === "light" && <span className="theme-option-check">✓</span>}
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): `{selectedTheme === "light" && <span className="theme-option-check">✓</span>}` closes ProfileSettings (opened on line 39). Names declared inside that block end here.

 235 |             </button>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

 236 |           </div>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 237 | 
     | Blank line in `src/components/ProfileSettings.jsx` (name, email, theme, and the coffee link), inside ProfileSettings. The parser skips it. It separates the previous statement from the next so the function is readable.

 238 |           {themeMsg && (
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): statement `{themeMsg && (`. It runs when ProfileSettings runs, in order, before the next line of the same function.

 239 |             <div className={`profile-msg profile-msg--${themeMsg.type}`} style={{ marginTop: 12 }}>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. A box that groups the elements inside it. Source: `<div className={`profile-msg profile-msg--${themeMsg.type}`} style={{ marginTop: 12 }}>`

 240 |               {themeMsg.text}
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): `{themeMsg.text}` closes ProfileSettings (opened on line 39). Names declared inside that block end here.

 241 |             </div>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 242 |           )}
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): `)}` closes ProfileSettings (opened on line 39). Names declared inside that block end here.

 243 |         </section>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Closes it. A grouped block on the settings-style pages. Source: `</section>`

 244 | 
     | Blank line in `src/components/ProfileSettings.jsx` (name, email, theme, and the coffee link), inside ProfileSettings. The parser skips it. It separates the previous statement from the next so the function is readable.

 245 |         {/* Support */}
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): `{/* Support */}` closes ProfileSettings (opened on line 39). Names declared inside that block end here.

 246 |         <section className="profile-settings-card">
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. A grouped block on the settings-style pages. Source: `<section className="profile-settings-card">`

 247 |           <div className="profile-settings-card-header">
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="profile-settings-card-header">`

 248 |             <h2 className="profile-settings-card-title">Support JumpyBrain</h2>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): JSX `<h2>`. React will create this node when the parent renders.. className chooses the CSS rules from styles.css Source: `<h2 className="profile-settings-card-title">Support JumpyBrain</h2>`

 249 |             <p className="profile-settings-card-desc">
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. A paragraph. Source: `<p className="profile-settings-card-desc">`

 250 |               JumpyBrain is free and open source. If it&apos;s helped you focus, consider
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): statement `JumpyBrain is free and open source. If it&apos;s helped you focus, consider`. It runs when ProfileSettings runs, in order, before the next line of the same function.

 251 |               buying me a coffee — it helps me keep improving the app for the ADHD/ADD community.
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): statement `buying me a coffee — it helps me keep improving the app for the ADHD/ADD community.`. It runs when ProfileSettings runs, in order, before the next line of the same function.

 252 |             </p>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Closes it. A paragraph. Source: `</p>`

 253 |           </div>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 254 |           <a
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Opens it. A normal link. If it has target=_blank it leaves the app. Source: `<a`

 255 |             href={FUNDING_URL}
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): `href={FUNDING_URL}` closes ProfileSettings (opened on line 39). Names declared inside that block end here.

 256 |             target="_blank"
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): statement `target="_blank"`. It runs when ProfileSettings runs, in order, before the next line of the same function.

 257 |             rel="noopener noreferrer"
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): statement `rel="noopener noreferrer"`. It runs when ProfileSettings runs, in order, before the next line of the same function.

 258 |             className="support-btn"
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): statement `className="support-btn"`. It runs when ProfileSettings runs, in order, before the next line of the same function.

 259 |             style={{ width: "fit-content" }}
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): `style={{ width: "fit-content" }}` closes ProfileSettings (opened on line 39). Names declared inside that block end here.

 260 |             aria-label="Buy me a coffee (opens buymeacoffee.com in a new tab)"
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): statement `aria-label="Buy me a coffee (opens buymeacoffee.com in a new tab)"`. It runs when ProfileSettings runs, in order, before the next line of the same function.

 261 |           >
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): statement `>`. It runs when ProfileSettings runs, in order, before the next line of the same function.

 262 |             <CoffeeIcon />
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): JSX `<CoffeeIcon>`. React will create this node when the parent renders. Source: `<CoffeeIcon />`

 263 |             Buy me a coffee
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): statement `Buy me a coffee`. It runs when ProfileSettings runs, in order, before the next line of the same function.

 264 |           </a>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Closes it. A normal link. If it has target=_blank it leaves the app. Source: `</a>`

 265 |         </section>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Closes it. A grouped block on the settings-style pages. Source: `</section>`

 266 | 
     | Blank line in `src/components/ProfileSettings.jsx` (name, email, theme, and the coffee link), inside ProfileSettings. The parser skips it. It separates the previous statement from the next so the function is readable.

 267 |       </div>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 268 |     </div>
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 269 |   );
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): statement `);`. It runs when ProfileSettings runs, in order, before the next line of the same function.

 270 | }
     | In `ProfileSettings` (src/components/ProfileSettings.jsx): `}` closes ProfileSettings (opened on line 39). Names declared inside that block end here.

