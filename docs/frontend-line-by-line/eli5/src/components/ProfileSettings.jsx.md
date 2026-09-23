# `src/components/ProfileSettings.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import React, { useState } from "react";
     | Borrows React so this file can remember things and draw the screen.

   2 | import { Link } from "react-router-dom";
     | Borrows React so this file can remember things and draw the screen.

   3 | import { useUser } from "../contexts/UserContext";
     | This file borrows a tool another file already made.

   4 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   5 | // Sourced from .github/FUNDING.yml at build time (see vite.config.ts) so
     | A note written for people. The app does not run it.

   6 | // this link and the sidebar's support button never drift apart.
     | A note written for people. The app does not run it.

   7 | const FUNDING_URL = __FUNDING_URL__;
     | The Buy Me a Coffee URL injected at build time from .github/FUNDING.yml by vite.config.ts as __FUNDING_URL__.

   8 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   9 | function CoffeeIcon() {
     | This starts CoffeeIcon. The cup SVG next to the support link.

  10 |   return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  11 |     <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}>
     | This draws one piece of the page while CoffeeIcon is showing.

  12 |       <path d="M18 8h1a3 3 0 010 6h-1" />
     | This draws one piece of the page while CoffeeIcon is showing.

  13 |       <path d="M3 8h15v6a4 4 0 01-4 4H7a4 4 0 01-4-4V8z" />
     | This draws one piece of the page while CoffeeIcon is showing.

  14 |       <path d="M6 2v2M10 2v2M14 2v2" />
     | This draws one piece of the page while CoffeeIcon is showing.

  15 |     </svg>
     | This ends a drawing that CoffeeIcon started just above.

  16 |   );
     | This closes a box of instructions that opened above.

  17 | }
     | This ends CoffeeIcon (opened on line 9).

  18 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  19 | const GENDER_OPTIONS = [
     | The profile form's gender select. Empty string and prefer-not-to-say are both offered.

  20 |   { value: "", label: "Prefer not to say" },
     | This ends the nearest open block.

  21 |   { value: "male", label: "Male" },
     | This ends the nearest open block.

  22 |   { value: "female", label: "Female" },
     | This ends the nearest open block.

  23 |   { value: "non-binary", label: "Non-binary" },
     | This ends the nearest open block.

  24 |   { value: "prefer-not-to-say", label: "Rather not say" },
     | This ends the nearest open block.

  25 | ];
     | Inside the top of the file, this line runs as written: ];. It happens in order, after the line above it and before the line below it.

  26 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  27 | function getInitials(name, email) {
     | This starts getInitials. First letters of the first two words, or the email's first character. Same rule as the top-bar avatar.

  28 |   if (name && name.trim()) {
     | This asks a yes-or-no question. The next bit runs only on yes.

  29 |     return name
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  30 |       .trim()
     | Inside getInitials, this line runs as written: .trim(). It happens in order, after the line above it and before the line below it.

  31 |       .split(/\s+/)
     | Inside getInitials, this line runs as written: .split(/\s+/). It happens in order, after the line above it and before the line below it.

  32 |       .slice(0, 2)
     | Inside getInitials, this line runs as written: .slice(0, 2). It happens in order, after the line above it and before the line below it.

  33 |       .map((w) => w[0].toUpperCase())
     | Inside getInitials, this line runs as written: .map((w) => w[0].toUpperCase()). It happens in order, after the line above it and before the line below it.

  34 |       .join("");
     | Inside getInitials, this line runs as written: .join("");. It happens in order, after the line above it and before the line below it.

  35 |   }
     | This ends if (name && name.trim()) { (opened on line 28).

  36 |   return (email || "?")[0].toUpperCase();
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  37 | }
     | This ends getInitials (opened on line 27).

  38 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  39 | export default function ProfileSettings({ onThemeChange }) {
     | This starts ProfileSettings. Edits name, email, gender through updateUser, and saves preferredTheme both on the server and into App's theme state.

  40 |   const { user, updateUser } = useUser();
     | The logged-in profile object. Null means ProtectedRoute renders Auth.

  41 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  42 |   const [profileForm, setProfileForm] = useState({
     | This gives a short name to a value so the rest of ProfileSettings can use it.

  43 |     name: user?.name || "",
     | Inside ProfileSettings, this line runs as written: name: user?.name || "",. It happens in order, after the line above it and before the line below it.

  44 |     email: user?.email || "",
     | Inside ProfileSettings, this line runs as written: email: user?.email || "",. It happens in order, after the line above it and before the line below it.

  45 |     gender: user?.gender || "",
     | Inside ProfileSettings, this line runs as written: gender: user?.gender || "",. It happens in order, after the line above it and before the line below it.

  46 |   });
     | This ends const [profileForm, setProfileForm] = useState({ (opened on line 42).

  47 |   const [profileSaving, setProfileSaving] = useState(false);
     | This gives a short name to a value so the rest of ProfileSettings can use it.

  48 |   const [profileMsg, setProfileMsg] = useState(null);
     | This gives a short name to a value so the rest of ProfileSettings can use it.

  49 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  50 |   const [selectedTheme, setSelectedTheme] = useState(user?.preferredTheme || "dark");
     | This gives a short name to a value so the rest of ProfileSettings can use it.

  51 |   const [themeSaving, setThemeSaving] = useState(false);
     | This gives a short name to a value so the rest of ProfileSettings can use it.

  52 |   const [themeMsg, setThemeMsg] = useState(null);
     | This gives a short name to a value so the rest of ProfileSettings can use it.

  53 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  54 |   async function handleProfileSave(e) {
     | This starts handleProfileSave. preventDefault, then updateUser. The success or error string is profileMsg.

  55 |     e.preventDefault();
     | Inside handleProfileSave, this line runs as written: e.preventDefault();. It happens in order, after the line above it and before the line below it.

  56 |     setProfileSaving(true);
     | Inside handleProfileSave, this line runs as written: setProfileSaving(true);. It happens in order, after the line above it and before the line below it.

  57 |     setProfileMsg(null);
     | Inside handleProfileSave, this line runs as written: setProfileMsg(null);. It happens in order, after the line above it and before the line below it.

  58 |     try {
     | Inside handleProfileSave, this line runs as written: try {. It happens in order, after the line above it and before the line below it.

  59 |       await updateUser({
     | This waits for an answer before the next step.

  60 |         name: profileForm.name,
     | Inside handleProfileSave, this line runs as written: name: profileForm.name,. It happens in order, after the line above it and before the line below it.

  61 |         email: profileForm.email,
     | Inside handleProfileSave, this line runs as written: email: profileForm.email,. It happens in order, after the line above it and before the line below it.

  62 |         gender: profileForm.gender,
     | Inside handleProfileSave, this line runs as written: gender: profileForm.gender,. It happens in order, after the line above it and before the line below it.

  63 |       });
     | This ends await updateUser({ (opened on line 59).

  64 |       setProfileMsg({ type: "success", text: "Profile updated successfully" });
     | This ends try { (opened on line 58).

  65 |     } catch (err) {
     | This ends try { (opened on line 58).

  66 |       const msg = err?.response?.data?.error || "Failed to update profile";
     | This gives a short name to a value so the rest of handleProfileSave can use it.

  67 |       setProfileMsg({ type: "error", text: msg });
     | This ends } catch (err) { (opened on line 65).

  68 |     } finally {
     | This ends } catch (err) { (opened on line 65).

  69 |       setProfileSaving(false);
     | Inside handleProfileSave, this line runs as written: setProfileSaving(false);. It happens in order, after the line above it and before the line below it.

  70 |     }
     | This ends } finally { (opened on line 68).

  71 |   }
     | This ends handleProfileSave (opened on line 54).

  72 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  73 |   async function handleThemeSave(theme) {
     | This starts handleThemeSave. PUT preferredTheme, then onThemeChange so the shell updates before the next navigation.

  74 |     setThemeSaving(true);
     | Inside handleThemeSave, this line runs as written: setThemeSaving(true);. It happens in order, after the line above it and before the line below it.

  75 |     setThemeMsg(null);
     | Inside handleThemeSave, this line runs as written: setThemeMsg(null);. It happens in order, after the line above it and before the line below it.

  76 |     try {
     | Inside handleThemeSave, this line runs as written: try {. It happens in order, after the line above it and before the line below it.

  77 |       await updateUser({ preferredTheme: theme });
     | This ends try { (opened on line 76).

  78 |       onThemeChange(theme);
     | Inside handleThemeSave, this line runs as written: onThemeChange(theme);. It happens in order, after the line above it and before the line below it.

  79 |       setThemeMsg({ type: "success", text: "Theme saved" });
     | This ends try { (opened on line 76).

  80 |       setTimeout(() => setThemeMsg(null), 2000);
     | Inside handleThemeSave, this line runs as written: setTimeout(() => setThemeMsg(null), 2000);. It happens in order, after the line above it and before the line below it.

  81 |     } catch {
     | This ends try { (opened on line 76).

  82 |       setThemeMsg({ type: "error", text: "Failed to save theme" });
     | This ends } catch { (opened on line 81).

  83 |     } finally {
     | This ends } catch { (opened on line 81).

  84 |       setThemeSaving(false);
     | Inside handleThemeSave, this line runs as written: setThemeSaving(false);. It happens in order, after the line above it and before the line below it.

  85 |     }
     | This ends } finally { (opened on line 83).

  86 |   }
     | This ends handleThemeSave (opened on line 73).

  87 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  88 |   function handleThemeSelect(theme) {
     | This starts handleThemeSelect. Sets the local highlight and immediately saves. There is no separate Save button for theme.

  89 |     setSelectedTheme(theme);
     | Inside handleThemeSelect, this line runs as written: setSelectedTheme(theme);. It happens in order, after the line above it and before the line below it.

  90 |     handleThemeSave(theme);
     | Inside handleThemeSelect, this line runs as written: handleThemeSave(theme);. It happens in order, after the line above it and before the line below it.

  91 |   }
     | This ends handleThemeSelect (opened on line 88).

  92 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  93 |   return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  94 |     <div className="profile-settings-page">
     | This draws one piece of the page while ProfileSettings is showing.

  95 |       <div className="profile-settings-container">
     | This draws one piece of the page while ProfileSettings is showing.

  96 |         <div className="profile-settings-header">
     | This draws one piece of the page while ProfileSettings is showing.

  97 |           <h1 className="profile-settings-title">Profile &amp; Settings</h1>
     | This draws one piece of the page while ProfileSettings is showing.

  98 |           <p className="profile-settings-subtitle">Manage your account details and appearance</p>
     | This draws one piece of the page while ProfileSettings is showing.

  99 |         </div>
     | This ends a drawing that ProfileSettings started just above.

 100 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 101 |         {/* Focus Shield quick access — mobile users land here from Profile too */}
     | This ends ProfileSettings (opened on line 39).

 102 |         <Link to="/blocking" className="profile-settings-card fs-quick-link">
     | This draws one piece of the page while ProfileSettings is showing.

 103 |           <span className="fs-quick-link-icon" aria-hidden="true">🛡️</span>
     | This draws one piece of the page while ProfileSettings is showing.

 104 |           <span style={{ flex: 1, minWidth: 0 }}>
     | This draws one piece of the page while ProfileSettings is showing.

 105 |             <span className="profile-settings-card-title" style={{ display: "block" }}>Focus Shield</span>
     | This draws one piece of the page while ProfileSettings is showing.

 106 |             <span className="profile-settings-card-desc" style={{ display: "block", marginTop: 2 }}>
     | This draws one piece of the page while ProfileSettings is showing.

 107 |               Manage blocked & whitelisted websites
     | Inside ProfileSettings, this line runs as written: Manage blocked & whitelisted websites. It happens in order, after the line above it and before the line below it.

 108 |             </span>
     | This ends a drawing that ProfileSettings started just above.

 109 |           </span>
     | This ends a drawing that ProfileSettings started just above.

 110 |           <span aria-hidden="true">→</span>
     | This draws one piece of the page while ProfileSettings is showing.

 111 |         </Link>
     | This ends a drawing that ProfileSettings started just above.

 112 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 113 |         {/* Profile Info */}
     | This ends ProfileSettings (opened on line 39).

 114 |         <section className="profile-settings-card">
     | This draws one piece of the page while ProfileSettings is showing.

 115 |           <div className="profile-settings-card-header">
     | This draws one piece of the page while ProfileSettings is showing.

 116 |             <h2 className="profile-settings-card-title">Profile Information</h2>
     | This draws one piece of the page while ProfileSettings is showing.

 117 |           </div>
     | This ends a drawing that ProfileSettings started just above.

 118 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 119 |           <div className="profile-avatar-row">
     | This draws one piece of the page while ProfileSettings is showing.

 120 |             <div className="profile-avatar">
     | This draws one piece of the page while ProfileSettings is showing.

 121 |               {getInitials(user?.name, user?.email)}
     | This ends ProfileSettings (opened on line 39).

 122 |             </div>
     | This ends a drawing that ProfileSettings started just above.

 123 |             <div>
     | This draws one piece of the page while ProfileSettings is showing.

 124 |               <div className="profile-avatar-name">{user?.name || "No name set"}</div>
     | This draws one piece of the page while ProfileSettings is showing.

 125 |               <div className="profile-avatar-email">{user?.email}</div>
     | This draws one piece of the page while ProfileSettings is showing.

 126 |             </div>
     | This ends a drawing that ProfileSettings started just above.

 127 |           </div>
     | This ends a drawing that ProfileSettings started just above.

 128 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 129 |           <form onSubmit={handleProfileSave} className="profile-form">
     | This draws one piece of the page while ProfileSettings is showing.

 130 |             <div className="profile-form-grid">
     | This draws one piece of the page while ProfileSettings is showing.

 131 |               <div className="profile-form-field">
     | This draws one piece of the page while ProfileSettings is showing.

 132 |                 <label className="profile-form-label" htmlFor="ps-name">Display Name</label>
     | This draws one piece of the page while ProfileSettings is showing.

 133 |                 <input
     | This draws one piece of the page while ProfileSettings is showing.

 134 |                   id="ps-name"
     | Inside ProfileSettings, this line runs as written: id="ps-name". It happens in order, after the line above it and before the line below it.

 135 |                   className="profile-form-input"
     | Inside ProfileSettings, this line runs as written: className="profile-form-input". It happens in order, after the line above it and before the line below it.

 136 |                   type="text"
     | Inside ProfileSettings, this line runs as written: type="text". It happens in order, after the line above it and before the line below it.

 137 |                   value={profileForm.name}
     | This ends ProfileSettings (opened on line 39).

 138 |                   onChange={(e) => setProfileForm((f) => ({ ...f, name: e.target.value }))}
     | This ends ProfileSettings (opened on line 39).

 139 |                   placeholder="Your name"
     | Inside ProfileSettings, this line runs as written: placeholder="Your name". It happens in order, after the line above it and before the line below it.

 140 |                   maxLength={100}
     | This ends ProfileSettings (opened on line 39).

 141 |                   autoComplete="name"
     | Inside ProfileSettings, this line runs as written: autoComplete="name". It happens in order, after the line above it and before the line below it.

 142 |                 />
     | This closes a box of instructions that opened above.

 143 |               </div>
     | This ends a drawing that ProfileSettings started just above.

 144 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 145 |               <div className="profile-form-field">
     | This draws one piece of the page while ProfileSettings is showing.

 146 |                 <label className="profile-form-label" htmlFor="ps-email">Email Address</label>
     | This draws one piece of the page while ProfileSettings is showing.

 147 |                 <input
     | This draws one piece of the page while ProfileSettings is showing.

 148 |                   id="ps-email"
     | Inside ProfileSettings, this line runs as written: id="ps-email". It happens in order, after the line above it and before the line below it.

 149 |                   className="profile-form-input"
     | Inside ProfileSettings, this line runs as written: className="profile-form-input". It happens in order, after the line above it and before the line below it.

 150 |                   type="email"
     | Inside ProfileSettings, this line runs as written: type="email". It happens in order, after the line above it and before the line below it.

 151 |                   value={profileForm.email}
     | This ends ProfileSettings (opened on line 39).

 152 |                   onChange={(e) => setProfileForm((f) => ({ ...f, email: e.target.value }))}
     | This ends ProfileSettings (opened on line 39).

 153 |                   placeholder="you@example.com"
     | Inside ProfileSettings, this line runs as written: placeholder="you@example.com". It happens in order, after the line above it and before the line below it.

 154 |                   autoComplete="email"
     | Inside ProfileSettings, this line runs as written: autoComplete="email". It happens in order, after the line above it and before the line below it.

 155 |                 />
     | This closes a box of instructions that opened above.

 156 |               </div>
     | This ends a drawing that ProfileSettings started just above.

 157 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 158 |               <div className="profile-form-field">
     | This draws one piece of the page while ProfileSettings is showing.

 159 |                 <label className="profile-form-label" htmlFor="ps-gender">Gender</label>
     | This draws one piece of the page while ProfileSettings is showing.

 160 |                 <select
     | This draws one piece of the page while ProfileSettings is showing.

 161 |                   id="ps-gender"
     | Inside ProfileSettings, this line runs as written: id="ps-gender". It happens in order, after the line above it and before the line below it.

 162 |                   className="profile-form-input profile-form-select"
     | Inside ProfileSettings, this line runs as written: className="profile-form-input profile-form-select". It happens in order, after the line above it and before the line below it.

 163 |                   value={profileForm.gender}
     | This ends ProfileSettings (opened on line 39).

 164 |                   onChange={(e) => setProfileForm((f) => ({ ...f, gender: e.target.value }))}
     | This ends ProfileSettings (opened on line 39).

 165 |                 >
     | Inside ProfileSettings, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 166 |                   {GENDER_OPTIONS.map((o) => (
     | Inside ProfileSettings, this line runs as written: {GENDER_OPTIONS.map((o) => (. It happens in order, after the line above it and before the line below it.

 167 |                     <option key={o.value} value={o.value}>{o.label}</option>
     | This draws one piece of the page while ProfileSettings is showing.

 168 |                   ))}
     | This ends ProfileSettings (opened on line 39).

 169 |                 </select>
     | This ends a drawing that ProfileSettings started just above.

 170 |               </div>
     | This ends a drawing that ProfileSettings started just above.

 171 |             </div>
     | This ends a drawing that ProfileSettings started just above.

 172 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 173 |             {profileMsg && (
     | Inside ProfileSettings, this line runs as written: {profileMsg && (. It happens in order, after the line above it and before the line below it.

 174 |               <div className={`profile-msg profile-msg--${profileMsg.type}`}>
     | This draws one piece of the page while ProfileSettings is showing.

 175 |                 {profileMsg.text}
     | This ends ProfileSettings (opened on line 39).

 176 |               </div>
     | This ends a drawing that ProfileSettings started just above.

 177 |             )}
     | This ends ProfileSettings (opened on line 39).

 178 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 179 |             <div className="profile-form-actions">
     | This draws one piece of the page while ProfileSettings is showing.

 180 |               <button
     | This draws one piece of the page while ProfileSettings is showing.

 181 |                 type="submit"
     | Inside ProfileSettings, this line runs as written: type="submit". It happens in order, after the line above it and before the line below it.

 182 |                 className="profile-save-btn"
     | Inside ProfileSettings, this line runs as written: className="profile-save-btn". It happens in order, after the line above it and before the line below it.

 183 |                 disabled={profileSaving}
     | This ends ProfileSettings (opened on line 39).

 184 |               >
     | Inside ProfileSettings, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 185 |                 {profileSaving ? "Saving…" : "Save Profile"}
     | This ends ProfileSettings (opened on line 39).

 186 |               </button>
     | This ends a drawing that ProfileSettings started just above.

 187 |             </div>
     | This ends a drawing that ProfileSettings started just above.

 188 |           </form>
     | This ends a drawing that ProfileSettings started just above.

 189 |         </section>
     | This ends a drawing that ProfileSettings started just above.

 190 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 191 |         {/* Appearance */}
     | This ends ProfileSettings (opened on line 39).

 192 |         <section className="profile-settings-card">
     | This draws one piece of the page while ProfileSettings is showing.

 193 |           <div className="profile-settings-card-header">
     | This draws one piece of the page while ProfileSettings is showing.

 194 |             <h2 className="profile-settings-card-title">Appearance</h2>
     | This draws one piece of the page while ProfileSettings is showing.

 195 |             <p className="profile-settings-card-desc">Choose how JumpyBrain looks for you</p>
     | This draws one piece of the page while ProfileSettings is showing.

 196 |           </div>
     | This ends a drawing that ProfileSettings started just above.

 197 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 198 |           <div className="theme-picker">
     | This draws one piece of the page while ProfileSettings is showing.

 199 |             <button
     | This draws one piece of the page while ProfileSettings is showing.

 200 |               className={`theme-option${selectedTheme === "dark" ? " active" : ""}`}
     | This ends ProfileSettings (opened on line 39).

 201 |               onClick={() => handleThemeSelect("dark")}
     | This decides what happens when you press.

 202 |               disabled={themeSaving}
     | This ends ProfileSettings (opened on line 39).

 203 |               type="button"
     | Inside ProfileSettings, this line runs as written: type="button". It happens in order, after the line above it and before the line below it.

 204 |               aria-pressed={selectedTheme === "dark"}
     | This ends ProfileSettings (opened on line 39).

 205 |             >
     | Inside ProfileSettings, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 206 |               <div className="theme-option-preview theme-option-preview--dark">
     | This draws one piece of the page while ProfileSettings is showing.

 207 |                 <div className="theme-preview-bar" />
     | This draws one piece of the page while ProfileSettings is showing.

 208 |                 <div className="theme-preview-card" />
     | This draws one piece of the page while ProfileSettings is showing.

 209 |                 <div className="theme-preview-card theme-preview-card--sm" />
     | This draws one piece of the page while ProfileSettings is showing.

 210 |               </div>
     | This ends a drawing that ProfileSettings started just above.

 211 |               <div className="theme-option-label">
     | This draws one piece of the page while ProfileSettings is showing.

 212 |                 <span className="theme-option-name">Dark</span>
     | This draws one piece of the page while ProfileSettings is showing.

 213 |                 <span className="theme-option-desc">Easy on the eyes at night</span>
     | This draws one piece of the page while ProfileSettings is showing.

 214 |               </div>
     | This ends a drawing that ProfileSettings started just above.

 215 |               {selectedTheme === "dark" && <span className="theme-option-check">✓</span>}
     | This ends ProfileSettings (opened on line 39).

 216 |             </button>
     | This ends a drawing that ProfileSettings started just above.

 217 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 218 |             <button
     | This draws one piece of the page while ProfileSettings is showing.

 219 |               className={`theme-option${selectedTheme === "light" ? " active" : ""}`}
     | This ends ProfileSettings (opened on line 39).

 220 |               onClick={() => handleThemeSelect("light")}
     | This decides what happens when you press.

 221 |               disabled={themeSaving}
     | This ends ProfileSettings (opened on line 39).

 222 |               type="button"
     | Inside ProfileSettings, this line runs as written: type="button". It happens in order, after the line above it and before the line below it.

 223 |               aria-pressed={selectedTheme === "light"}
     | This ends ProfileSettings (opened on line 39).

 224 |             >
     | Inside ProfileSettings, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 225 |               <div className="theme-option-preview theme-option-preview--light">
     | This draws one piece of the page while ProfileSettings is showing.

 226 |                 <div className="theme-preview-bar" />
     | This draws one piece of the page while ProfileSettings is showing.

 227 |                 <div className="theme-preview-card" />
     | This draws one piece of the page while ProfileSettings is showing.

 228 |                 <div className="theme-preview-card theme-preview-card--sm" />
     | This draws one piece of the page while ProfileSettings is showing.

 229 |               </div>
     | This ends a drawing that ProfileSettings started just above.

 230 |               <div className="theme-option-label">
     | This draws one piece of the page while ProfileSettings is showing.

 231 |                 <span className="theme-option-name">Light</span>
     | This draws one piece of the page while ProfileSettings is showing.

 232 |                 <span className="theme-option-desc">Bright and clear</span>
     | This draws one piece of the page while ProfileSettings is showing.

 233 |               </div>
     | This ends a drawing that ProfileSettings started just above.

 234 |               {selectedTheme === "light" && <span className="theme-option-check">✓</span>}
     | This ends ProfileSettings (opened on line 39).

 235 |             </button>
     | This ends a drawing that ProfileSettings started just above.

 236 |           </div>
     | This ends a drawing that ProfileSettings started just above.

 237 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 238 |           {themeMsg && (
     | Inside ProfileSettings, this line runs as written: {themeMsg && (. It happens in order, after the line above it and before the line below it.

 239 |             <div className={`profile-msg profile-msg--${themeMsg.type}`} style={{ marginTop: 12 }}>
     | This draws one piece of the page while ProfileSettings is showing.

 240 |               {themeMsg.text}
     | This ends ProfileSettings (opened on line 39).

 241 |             </div>
     | This ends a drawing that ProfileSettings started just above.

 242 |           )}
     | This ends ProfileSettings (opened on line 39).

 243 |         </section>
     | This ends a drawing that ProfileSettings started just above.

 244 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 245 |         {/* Support */}
     | This ends ProfileSettings (opened on line 39).

 246 |         <section className="profile-settings-card">
     | This draws one piece of the page while ProfileSettings is showing.

 247 |           <div className="profile-settings-card-header">
     | This draws one piece of the page while ProfileSettings is showing.

 248 |             <h2 className="profile-settings-card-title">Support JumpyBrain</h2>
     | This draws one piece of the page while ProfileSettings is showing.

 249 |             <p className="profile-settings-card-desc">
     | This draws one piece of the page while ProfileSettings is showing.

 250 |               JumpyBrain is free and open source. If it&apos;s helped you focus, consider
     | Inside ProfileSettings, this line runs as written: JumpyBrain is free and open source. If it&apos;s helped you focus, consider. It happens in order, after the line above it and before the line below it.

 251 |               buying me a coffee — it helps me keep improving the app for the ADHD/ADD community.
     | Inside ProfileSettings, this line runs as written: buying me a coffee — it helps me keep improving the app for the ADHD/ADD community.. It happens in order, after the line above it and before the line below it.

 252 |             </p>
     | This ends a drawing that ProfileSettings started just above.

 253 |           </div>
     | This ends a drawing that ProfileSettings started just above.

 254 |           <a
     | This draws one piece of the page while ProfileSettings is showing.

 255 |             href={FUNDING_URL}
     | This ends ProfileSettings (opened on line 39).

 256 |             target="_blank"
     | Inside ProfileSettings, this line runs as written: target="_blank". It happens in order, after the line above it and before the line below it.

 257 |             rel="noopener noreferrer"
     | Inside ProfileSettings, this line runs as written: rel="noopener noreferrer". It happens in order, after the line above it and before the line below it.

 258 |             className="support-btn"
     | Inside ProfileSettings, this line runs as written: className="support-btn". It happens in order, after the line above it and before the line below it.

 259 |             style={{ width: "fit-content" }}
     | This ends ProfileSettings (opened on line 39).

 260 |             aria-label="Buy me a coffee (opens buymeacoffee.com in a new tab)"
     | Inside ProfileSettings, this line runs as written: aria-label="Buy me a coffee (opens buymeacoffee.com in a new tab)". It happens in order, after the line above it and before the line below it.

 261 |           >
     | Inside ProfileSettings, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 262 |             <CoffeeIcon />
     | This draws one piece of the page while ProfileSettings is showing.

 263 |             Buy me a coffee
     | Inside ProfileSettings, this line runs as written: Buy me a coffee. It happens in order, after the line above it and before the line below it.

 264 |           </a>
     | This ends a drawing that ProfileSettings started just above.

 265 |         </section>
     | This ends a drawing that ProfileSettings started just above.

 266 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 267 |       </div>
     | This ends a drawing that ProfileSettings started just above.

 268 |     </div>
     | This ends a drawing that ProfileSettings started just above.

 269 |   );
     | This closes a box of instructions that opened above.

 270 | }
     | This ends ProfileSettings (opened on line 39).

