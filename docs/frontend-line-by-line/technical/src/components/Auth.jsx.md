# `src/components/Auth.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import { useState, useEffect, useCallback, useRef } from "react";
     | Import for the Google sign-in screen: `import { useState, useEffect, useCallback, useRef } from "react";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   2 | import api from "../services/api";
     | Import for the Google sign-in screen: `import api from "../services/api";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   3 | import { useUser } from "../contexts/UserContext";
     | Import for the Google sign-in screen: `import { useUser } from "../contexts/UserContext";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   4 | import { useNavigate } from "react-router-dom";
     | Import for the Google sign-in screen: `import { useNavigate } from "react-router-dom";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   5 | import Logo from "./Logo";
     | Import for the Google sign-in screen: `import Logo from "./Logo";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   6 | 
     | Blank line in `src/components/Auth.jsx` (the Google sign-in screen), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   7 | const GOOGLE_CLIENT_ID = import.meta.env.VITE_GOOGLE_CLIENT_ID;
     | In `the top of the file` (src/components/Auth.jsx): `GOOGLE_CLIENT_ID`: Vite env VITE_GOOGLE_CLIENT_ID. If it is missing, Auth shows a disabled button instead of Google's widget. The code is `const GOOGLE_CLIENT_ID = import.meta.env.VITE_GOOGLE_CLIENT_ID;`.

   8 | 
     | Blank line in `src/components/Auth.jsx` (the Google sign-in screen), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   9 | export default function Auth() {
     | Defines `Auth` in the Google sign-in screen. Google sign-in only. Posts the Google credential to /auth/google, then setUser, setToken, and navigates to /.

  10 |   const { setUser, setToken } = useUser();
     | In `Auth` (src/components/Auth.jsx): `setUser, setToken` is assigned `useUser();`. Later lines in this function read that name.

  11 |   const [error, setError] = useState("");
     | In `Auth` (src/components/Auth.jsx): React state `error, setError`. The value survives re-renders. Calling the setter re-renders this component. `const [error, setError] = useState("");`

  12 |   const [googleLoading, setGoogleLoading] = useState(false);
     | In `Auth` (src/components/Auth.jsx): React state `googleLoading, setGoogleLoading`. The value survives re-renders. Calling the setter re-renders this component. `const [googleLoading, setGoogleLoading] = useState(false);`

  13 |   const navigate = useNavigate();
     | In `Auth` (src/components/Auth.jsx): `navigate` is assigned `useNavigate();`. Later lines in this function read that name.

  14 | 
     | Blank line in `src/components/Auth.jsx` (the Google sign-in screen), inside Auth. The parser skips it. It separates the previous statement from the next so the function is readable.

  15 |   const handleGoogleCredential = useCallback(async (response) => {
     | In `Auth` (src/components/Auth.jsx): A memoized function `handleGoogleCredential`. `const handleGoogleCredential = useCallback(async (response) => {`

  16 |     setGoogleLoading(true);
     | In `Auth` (src/components/Auth.jsx): statement `setGoogleLoading(true);`. It runs when Auth runs, in order, before the next line of the same function.

  17 |     setError("");
     | In `Auth` (src/components/Auth.jsx): statement `setError("");`. It runs when Auth runs, in order, before the next line of the same function.

  18 |     try {
     | In `Auth` (src/components/Auth.jsx): error path `try {`.

  19 |       const data = await api.post("/auth/google", { idToken: response.credential });
     | In `Auth` (src/components/Auth.jsx): `data` is assigned `await api.post("/auth/google", { idToken: response.credential });`. Later lines in this function read that name.

  20 |       setUser(data.user);
     | In `Auth` (src/components/Auth.jsx): statement `setUser(data.user);`. It runs when Auth runs, in order, before the next line of the same function.

  21 |       setToken(data.token);
     | In `Auth` (src/components/Auth.jsx): statement `setToken(data.token);`. It runs when Auth runs, in order, before the next line of the same function.

  22 |       navigate("/");
     | In `Auth` (src/components/Auth.jsx): statement `navigate("/");`. It runs when Auth runs, in order, before the next line of the same function.

  23 |     } catch (err) {
     | In `Auth` (src/components/Auth.jsx): `} catch (err) {` closes try { (opened on line 18). Names declared inside that block end here.

  24 |       const msg =
     | In `Auth` (src/components/Auth.jsx): `msg` is assigned ``. Later lines in this function read that name.

  25 |         err.response?.data?.error ||
     | In `Auth` (src/components/Auth.jsx): statement `err.response?.data?.error ||`. It runs when Auth runs, in order, before the next line of the same function.

  26 |         err.response?.data?.message ||
     | In `Auth` (src/components/Auth.jsx): statement `err.response?.data?.message ||`. It runs when Auth runs, in order, before the next line of the same function.

  27 |         err.message ||
     | In `Auth` (src/components/Auth.jsx): statement `err.message ||`. It runs when Auth runs, in order, before the next line of the same function.

  28 |         "Google sign-in failed";
     | In `Auth` (src/components/Auth.jsx): statement `"Google sign-in failed";`. It runs when Auth runs, in order, before the next line of the same function.

  29 |       setError(msg);
     | In `Auth` (src/components/Auth.jsx): statement `setError(msg);`. It runs when Auth runs, in order, before the next line of the same function.

  30 |     } finally {
     | In `Auth` (src/components/Auth.jsx): `} finally {` closes } catch (err) { (opened on line 23). Names declared inside that block end here.

  31 |       setGoogleLoading(false);
     | In `Auth` (src/components/Auth.jsx): statement `setGoogleLoading(false);`. It runs when Auth runs, in order, before the next line of the same function.

  32 |     }
     | In `Auth` (src/components/Auth.jsx): `}` closes } finally { (opened on line 30). Names declared inside that block end here.

  33 |   }, [navigate, setUser, setToken]);
     | In `Auth` (src/components/Auth.jsx): `}, [navigate, setUser, setToken]);` closes const handleGoogleCredential = useCallback(async (opened on line 15). Names declared inside that block end here.

  34 | 
     | Blank line in `src/components/Auth.jsx` (the Google sign-in screen), inside Auth. The parser skips it. It separates the previous statement from the next so the function is readable.

  35 |   const gsiInitializedRef = useRef(false);
     | In `Auth` (src/components/Auth.jsx): A ref `gsiInitializedRef`. `.current` survives re-renders and writing it does not re-render. `const gsiInitializedRef = useRef(false);`

  36 |   const googleButtonWrapRef = useRef(null);
     | In `Auth` (src/components/Auth.jsx): A ref `googleButtonWrapRef`. `.current` survives re-renders and writing it does not re-render. `const googleButtonWrapRef = useRef(null);`

  37 |   const googleButtonBoxRef = useRef(null);
     | In `Auth` (src/components/Auth.jsx): A ref `googleButtonBoxRef`. `.current` survives re-renders and writing it does not re-render. `const googleButtonBoxRef = useRef(null);`

  38 | 
     | Blank line in `src/components/Auth.jsx` (the Google sign-in screen), inside Auth. The parser skips it. It separates the previous statement from the next so the function is readable.

  39 |   const initGoogleIdentity = useCallback(() => {
     | In `Auth` (src/components/Auth.jsx): A memoized function `initGoogleIdentity`. `const initGoogleIdentity = useCallback(() => {`

  40 |     if (!GOOGLE_CLIENT_ID || !window.google) return false;
     | In `Auth` (src/components/Auth.jsx): branch `if (!GOOGLE_CLIENT_ID || !window.google) return false;`. Only one side runs.

  41 |     window.google.accounts.id.initialize({
     | In `Auth` (src/components/Auth.jsx): statement `window.google.accounts.id.initialize({`. It runs when Auth runs, in order, before the next line of the same function.

  42 |       client_id: GOOGLE_CLIENT_ID,
     | In `Auth` (src/components/Auth.jsx): statement `client_id: GOOGLE_CLIENT_ID,`. It runs when Auth runs, in order, before the next line of the same function.

  43 |       callback: handleGoogleCredential,
     | In `Auth` (src/components/Auth.jsx): statement `callback: handleGoogleCredential,`. It runs when Auth runs, in order, before the next line of the same function.

  44 |     });
     | In `Auth` (src/components/Auth.jsx): `});` closes window.google.accounts.id.initialize({ (opened on line 41). Names declared inside that block end here.

  45 |     // Render Google's own button on top of our styled one. Unlike One Tap's
     | Comment inside Auth. Not executed. It documents the next code: Render Google's own button on top of our styled one. Unlike One Tap's

  46 |     // silent prompt() below, a click on Google's real button always opens
     | Comment inside Auth. Not executed. It documents the next code: silent prompt() below, a click on Google's real button always opens

  47 |     // their standard account-chooser popup/redirect — this keeps working on
     | Comment inside Auth. Not executed. It documents the next code: their standard account-chooser popup/redirect — this keeps working on

  48 |     // a brand-new device/browser profile, with third-party cookies blocked,
     | Comment inside Auth. Not executed. It documents the next code: a brand-new device/browser profile, with third-party cookies blocked,

  49 |     // or anywhere else One Tap silently declines to show (which it does
     | Comment inside Auth. Not executed. It documents the next code: or anywhere else One Tap silently declines to show (which it does

  50 |     // without any error, just no UI at all).
     | Comment inside Auth. Not executed. It documents the next code: without any error, just no UI at all).

  51 |     if (googleButtonBoxRef.current) {
     | In `Auth` (src/components/Auth.jsx): branch `if (googleButtonBoxRef.current) {`. Only one side runs.

  52 |       const width = Math.min(400, Math.max(200, Math.round(
     | In `Auth` (src/components/Auth.jsx): `width` is assigned `Math.min(400, Math.max(200, Math.round(`. Later lines in this function read that name.

  53 |         googleButtonWrapRef.current?.getBoundingClientRect().width || 320
     | In `Auth` (src/components/Auth.jsx): statement `googleButtonWrapRef.current?.getBoundingClientRect().width || 320`. It runs when Auth runs, in order, before the next line of the same function.

  54 |       )));
     | In `Auth` (src/components/Auth.jsx): statement `)));`. It runs when Auth runs, in order, before the next line of the same function.

  55 |       window.google.accounts.id.renderButton(googleButtonBoxRef.current, {
     | In `Auth` (src/components/Auth.jsx): statement `window.google.accounts.id.renderButton(googleButtonBoxRef.current, {`. It runs when Auth runs, in order, before the next line of the same function.

  56 |         type: "standard",
     | In `Auth` (src/components/Auth.jsx): statement `type: "standard",`. It runs when Auth runs, in order, before the next line of the same function.

  57 |         theme: "outline",
     | In `Auth` (src/components/Auth.jsx): statement `theme: "outline",`. It runs when Auth runs, in order, before the next line of the same function.

  58 |         size: "large",
     | In `Auth` (src/components/Auth.jsx): statement `size: "large",`. It runs when Auth runs, in order, before the next line of the same function.

  59 |         shape: "pill",
     | In `Auth` (src/components/Auth.jsx): statement `shape: "pill",`. It runs when Auth runs, in order, before the next line of the same function.

  60 |         text: "continue_with",
     | In `Auth` (src/components/Auth.jsx): statement `text: "continue_with",`. It runs when Auth runs, in order, before the next line of the same function.

  61 |         logo_alignment: "center",
     | In `Auth` (src/components/Auth.jsx): statement `logo_alignment: "center",`. It runs when Auth runs, in order, before the next line of the same function.

  62 |         width,
     | In `Auth` (src/components/Auth.jsx): statement `width,`. It runs when Auth runs, in order, before the next line of the same function.

  63 |       });
     | In `Auth` (src/components/Auth.jsx): `});` closes window.google.accounts.id.renderButton(googleBut (opened on line 55). Names declared inside that block end here.

  64 |     }
     | In `Auth` (src/components/Auth.jsx): `}` closes if (googleButtonBoxRef.current) { (opened on line 51). Names declared inside that block end here.

  65 |     gsiInitializedRef.current = true;
     | In `Auth` (src/components/Auth.jsx): statement `gsiInitializedRef.current = true;`. It runs when Auth runs, in order, before the next line of the same function.

  66 |     // Also try the silent One Tap prompt for returning users on a device
     | Comment inside Auth. Not executed. It documents the next code: Also try the silent One Tap prompt for returning users on a device

  67 |     // Google already recognizes. If it can't be shown, notification carries
     | Comment inside Auth. Not executed. It documents the next code: Google already recognizes. If it can't be shown, notification carries

  68 |     // the reason but we don't surface it as an error — the real button
     | Comment inside Auth. Not executed. It documents the next code: the reason but we don't surface it as an error — the real button

  69 |     // above is always there as the reliable path.
     | Comment inside Auth. Not executed. It documents the next code: above is always there as the reliable path.

  70 |     window.google.accounts.id.prompt();
     | In `Auth` (src/components/Auth.jsx): statement `window.google.accounts.id.prompt();`. It runs when Auth runs, in order, before the next line of the same function.

  71 |     return true;
     | In `Auth` (src/components/Auth.jsx): return `return true;`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  72 |   }, [handleGoogleCredential]);
     | In `Auth` (src/components/Auth.jsx): `}, [handleGoogleCredential]);` closes const initGoogleIdentity = useCallback(() => { (opened on line 39). Names declared inside that block end here.

  73 | 
     | Blank line in `src/components/Auth.jsx` (the Google sign-in screen), inside Auth. The parser skips it. It separates the previous statement from the next so the function is readable.

  74 |   // Initialise Google Identity Services as soon as the script is ready.
     | Comment inside Auth. Not executed. It documents the next code: Initialise Google Identity Services as soon as the script is ready.

  75 |   // The script tag loads with `async defer`, so it may not be available yet
     | Comment inside Auth. Not executed. It documents the next code: The script tag loads with `async defer`, so it may not be available yet

  76 |   // on mount — poll briefly instead of giving up after a single check.
     | Comment inside Auth. Not executed. It documents the next code: on mount — poll briefly instead of giving up after a single check.

  77 |   useEffect(() => {
     | In `Auth` (src/components/Auth.jsx): opens or continues an effect — `useEffect(() => {`. The effect body runs after paint, and its cleanup runs before the next effect and on unmount.

  78 |     if (initGoogleIdentity()) return;
     | In `Auth` (src/components/Auth.jsx): branch `if (initGoogleIdentity()) return;`. Only one side runs.

  79 |     const interval = setInterval(() => {
     | In `Auth` (src/components/Auth.jsx): `interval` is assigned `setInterval(() => {`. Later lines in this function read that name.

  80 |       if (initGoogleIdentity()) clearInterval(interval);
     | In `Auth` (src/components/Auth.jsx): branch `if (initGoogleIdentity()) clearInterval(interval);`. Only one side runs.

  81 |     }, 200);
     | In `Auth` (src/components/Auth.jsx): `}, 200);` closes const interval = setInterval(() => { (opened on line 79). Names declared inside that block end here.

  82 |     return () => clearInterval(interval);
     | In `Auth` (src/components/Auth.jsx): return `return () => clearInterval(interval);`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  83 |   }, [initGoogleIdentity]);
     | In `Auth` (src/components/Auth.jsx): `}, [initGoogleIdentity]);` closes effect in Auth (opened on line 77). Names declared inside that block end here.

  84 | 
     | Blank line in `src/components/Auth.jsx` (the Google sign-in screen), inside Auth. The parser skips it. It separates the previous statement from the next so the function is readable.

  85 |   return (
     | In `Auth` (src/components/Auth.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  86 |     <div className="auth-page">
     | In `Auth` (src/components/Auth.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="auth-page">`

  87 |       <div className="card auth-card">
     | In `Auth` (src/components/Auth.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="card auth-card">`

  88 |         <div className="auth-header">
     | In `Auth` (src/components/Auth.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="auth-header">`

  89 |           <div className="auth-brand">
     | In `Auth` (src/components/Auth.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="auth-brand">`

  90 |             <Logo size={28} variant="icon" />
     | In `Auth` (src/components/Auth.jsx): Opens it. The JB mark. Source: `<Logo size={28} variant="icon" />`

  91 |           </div>
     | In `Auth` (src/components/Auth.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  92 |           <h1 className="auth-title">JumpyBrain</h1>
     | In `Auth` (src/components/Auth.jsx): Opens it. The page title. Source: `<h1 className="auth-title">JumpyBrain</h1>`

  93 |           <p className="auth-subtitle">Sign in to continue</p>
     | In `Auth` (src/components/Auth.jsx): Opens it. A paragraph. Source: `<p className="auth-subtitle">Sign in to continue</p>`

  94 |           <p className="auth-value">
     | In `Auth` (src/components/Auth.jsx): Opens it. A paragraph. Source: `<p className="auth-value">`

  95 |             Focus timers, habits, and gentle nudges that turn scattered days into steady progress.
     | In `Auth` (src/components/Auth.jsx): statement `Focus timers, habits, and gentle nudges that turn scattered days into steady progress.`. It runs when Auth runs, in order, before the next line of the same function.

  96 |           </p>
     | In `Auth` (src/components/Auth.jsx): Closes it. A paragraph. Source: `</p>`

  97 |         </div>
     | In `Auth` (src/components/Auth.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

  98 | 
     | Blank line in `src/components/Auth.jsx` (the Google sign-in screen), inside Auth. The parser skips it. It separates the previous statement from the next so the function is readable.

  99 |         <div className="auth-status" role="status" aria-live="polite">
     | In `Auth` (src/components/Auth.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="auth-status" role="status" aria-live="polite">`

 100 |           {error && <div className="auth-error">{error}</div>}
     | In `Auth` (src/components/Auth.jsx): `{error && <div className="auth-error">{error}</div>}` closes Auth (opened on line 9). Names declared inside that block end here.

 101 |         </div>
     | In `Auth` (src/components/Auth.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 102 | 
     | Blank line in `src/components/Auth.jsx` (the Google sign-in screen), inside Auth. The parser skips it. It separates the previous statement from the next so the function is readable.

 103 |         {GOOGLE_CLIENT_ID ? (
     | In `Auth` (src/components/Auth.jsx): statement `{GOOGLE_CLIENT_ID ? (`. It runs when Auth runs, in order, before the next line of the same function.

 104 |           <div className="google-btn-wrap" ref={googleButtonWrapRef}>
     | In `Auth` (src/components/Auth.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="google-btn-wrap" ref={googleButtonWrapRef}>`

 105 |             <button
     | In `Auth` (src/components/Auth.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button`

 106 |               type="button"
     | In `Auth` (src/components/Auth.jsx): statement `type="button"`. It runs when Auth runs, in order, before the next line of the same function.

 107 |               className="btn-google"
     | In `Auth` (src/components/Auth.jsx): statement `className="btn-google"`. It runs when Auth runs, in order, before the next line of the same function.

 108 |               disabled={googleLoading}
     | In `Auth` (src/components/Auth.jsx): `disabled={googleLoading}` closes Auth (opened on line 9). Names declared inside that block end here.

 109 |               tabIndex={-1}
     | In `Auth` (src/components/Auth.jsx): `tabIndex={-1}` closes Auth (opened on line 9). Names declared inside that block end here.

 110 |               aria-hidden="true"
     | In `Auth` (src/components/Auth.jsx): statement `aria-hidden="true"`. It runs when Auth runs, in order, before the next line of the same function.

 111 |             >
     | In `Auth` (src/components/Auth.jsx): statement `>`. It runs when Auth runs, in order, before the next line of the same function.

 112 |               {googleLoading ? (
     | In `Auth` (src/components/Auth.jsx): statement `{googleLoading ? (`. It runs when Auth runs, in order, before the next line of the same function.

 113 |                 <>
     | In `Auth` (src/components/Auth.jsx): JSX `<element>`. React will create this node when the parent renders. Source: `<>`

 114 |                   <span className="spinner" aria-hidden="true" />
     | In `Auth` (src/components/Auth.jsx): Opens it. An inline box. Source: `<span className="spinner" aria-hidden="true" />`

 115 |                   Redirecting…
     | In `Auth` (src/components/Auth.jsx): statement `Redirecting…`. It runs when Auth runs, in order, before the next line of the same function.

 116 |                 </>
     | In `Auth` (src/components/Auth.jsx): JSX `<element>`. This closes that element. Source: `</>`

 117 |               ) : (
     | In `Auth` (src/components/Auth.jsx): statement `) : (`. It runs when Auth runs, in order, before the next line of the same function.

 118 |                 <>
     | In `Auth` (src/components/Auth.jsx): JSX `<element>`. React will create this node when the parent renders. Source: `<>`

 119 |                   <svg width="18" height="18" viewBox="0 0 18 18" fill="none" aria-hidden="true">
     | In `Auth` (src/components/Auth.jsx): Opens it. Vector drawing. It does not fetch data. Source: `<svg width="18" height="18" viewBox="0 0 18 18" fill="none" aria-hidden="true">`

 120 |                     <path d="M17.64 9.2c0-.637-.057-1.251-.164-1.84H9v3.481h4.844c-.209 1.125-.843 2.078-1.796 2.717v2.258h2.908c1.702-1.567 2.684-3.874 2.684-6.615z" fill="#4285F4"/>
     | In `Auth` (src/components/Auth.jsx): JSX `<path>`. React will create this node when the parent renders. Source: `<path d="M17.64 9.2c0-.637-.057-1.251-.164-1.84H9v3.481h4.844c-.209 1.125-.843 2.078-1.796 2.717v2.258h2.908c1.702-1.567 2.684-3.874 2.684-6.615z" fill="#4285F4"/>`

 121 |                     <path d="M9 18c2.43 0 4.467-.806 5.956-2.184l-2.908-2.258c-.806.54-1.837.86-3.048.86-2.344 0-4.328-1.584-5.036-3.711H.957v2.332C2.438 15.983 5.482 18 9 18z" fill="#34A853"/>
     | In `Auth` (src/components/Auth.jsx): JSX `<path>`. React will create this node when the parent renders. Source: `<path d="M9 18c2.43 0 4.467-.806 5.956-2.184l-2.908-2.258c-.806.54-1.837.86-3.048.86-2.344 0-4.328-1.584-5.036-3.711H.957v2.332C2.438 15.983 5.482 18 9 18z" fill="#34A853"/>`

 122 |                     <path d="M3.964 10.707A5.41 5.41 0 0 1 3.682 9c0-.593.102-1.17.282-1.707V4.961H.957A8.996 8.996 0 0 0 0 9c0 1.452.348 2.827.957 4.039l3.007-2.332z" fill="#FBBC05"/>
     | In `Auth` (src/components/Auth.jsx): JSX `<path>`. React will create this node when the parent renders. Source: `<path d="M3.964 10.707A5.41 5.41 0 0 1 3.682 9c0-.593.102-1.17.282-1.707V4.961H.957A8.996 8.996 0 0 0 0 9c0 1.452.348 2.827.957 4.039l3.007-2.332z" fill="#FBBC05"/>`

 123 |                     <path d="M9 3.58c1.321 0 2.508.454 3.44 1.345l2.582-2.58C13.463.891 11.426 0 9 0 5.482 0 2.438 2.017.957 4.961L3.964 6.293C4.672 4.166 6.656 3.58 9 3.58z" fill="#EA4335"/>
     | In `Auth` (src/components/Auth.jsx): JSX `<path>`. React will create this node when the parent renders. Source: `<path d="M9 3.58c1.321 0 2.508.454 3.44 1.345l2.582-2.58C13.463.891 11.426 0 9 0 5.482 0 2.438 2.017.957 4.961L3.964 6.293C4.672 4.166 6.656 3.58 9 3.58z" fill="#EA4335"/>`

 124 |                   </svg>
     | In `Auth` (src/components/Auth.jsx): Closes it. Vector drawing. It does not fetch data. Source: `</svg>`

 125 |                   Continue with Google
     | In `Auth` (src/components/Auth.jsx): statement `Continue with Google`. It runs when Auth runs, in order, before the next line of the same function.

 126 |                 </>
     | In `Auth` (src/components/Auth.jsx): JSX `<element>`. This closes that element. Source: `</>`

 127 |               )}
     | In `Auth` (src/components/Auth.jsx): `)}` closes Auth (opened on line 9). Names declared inside that block end here.

 128 |             </button>
     | In `Auth` (src/components/Auth.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

 129 |             {/* Google renders its real, clickable button here on top of the
     | In `Auth` (src/components/Auth.jsx): statement `{/* Google renders its real, clickable button here on top of the`. It runs when Auth runs, in order, before the next line of the same function.

 130 |                 styled one above (see .google-btn-overlay) so clicks open
     | In `Auth` (src/components/Auth.jsx): statement `styled one above (see .google-btn-overlay) so clicks open`. It runs when Auth runs, in order, before the next line of the same function.

 131 |                 Google's own popup/redirect flow directly, instead of going
     | In `Auth` (src/components/Auth.jsx): statement `Google's own popup/redirect flow directly, instead of going`. It runs when Auth runs, in order, before the next line of the same function.

 132 |                 through the silent, less reliable One Tap prompt. */}
     | In `Auth` (src/components/Auth.jsx): `through the silent, less reliable One Tap prompt. */}` closes Auth (opened on line 9). Names declared inside that block end here.

 133 |             <div className="google-btn-overlay" ref={googleButtonBoxRef} />
     | In `Auth` (src/components/Auth.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="google-btn-overlay" ref={googleButtonBoxRef} />`

 134 |           </div>
     | In `Auth` (src/components/Auth.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 135 |         ) : (
     | In `Auth` (src/components/Auth.jsx): statement `) : (`. It runs when Auth runs, in order, before the next line of the same function.

 136 |           <button type="button" className="btn-google" disabled>
     | In `Auth` (src/components/Auth.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button type="button" className="btn-google" disabled>`

 137 |             Google Sign-In is not configured
     | In `Auth` (src/components/Auth.jsx): statement `Google Sign-In is not configured`. It runs when Auth runs, in order, before the next line of the same function.

 138 |           </button>
     | In `Auth` (src/components/Auth.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

 139 |         )}
     | In `Auth` (src/components/Auth.jsx): `)}` closes Auth (opened on line 9). Names declared inside that block end here.

 140 | 
     | Blank line in `src/components/Auth.jsx` (the Google sign-in screen), inside Auth. The parser skips it. It separates the previous statement from the next so the function is readable.

 141 |         <p className="auth-legal">
     | In `Auth` (src/components/Auth.jsx): Opens it. A paragraph. Source: `<p className="auth-legal">`

 142 |           By continuing you agree to our{" "}
     | In `Auth` (src/components/Auth.jsx): `By continuing you agree to our{" "}` closes Auth (opened on line 9). Names declared inside that block end here.

 143 |           <a href="/terms" className="text-link">Terms of Service</a> and{" "}
     | In `Auth` (src/components/Auth.jsx): Opens it. A normal link. If it has target=_blank it leaves the app. Source: `<a href="/terms" className="text-link">Terms of Service</a> and{" "}`

 144 |           <a href="/privacy" className="text-link">Privacy Policy</a>.
     | In `Auth` (src/components/Auth.jsx): Opens it. A normal link. If it has target=_blank it leaves the app. Source: `<a href="/privacy" className="text-link">Privacy Policy</a>.`

 145 |         </p>
     | In `Auth` (src/components/Auth.jsx): Closes it. A paragraph. Source: `</p>`

 146 |       </div>
     | In `Auth` (src/components/Auth.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 147 |     </div>
     | In `Auth` (src/components/Auth.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 148 |   );
     | In `Auth` (src/components/Auth.jsx): statement `);`. It runs when Auth runs, in order, before the next line of the same function.

 149 | }
     | In `Auth` (src/components/Auth.jsx): `}` closes Auth (opened on line 9). Names declared inside that block end here.

