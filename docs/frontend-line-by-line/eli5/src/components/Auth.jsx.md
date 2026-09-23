# `src/components/Auth.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import { useState, useEffect, useCallback, useRef } from "react";
     | Borrows React so this file can remember things and draw the screen.

   2 | import api from "../services/api";
     | This file borrows a tool another file already made.

   3 | import { useUser } from "../contexts/UserContext";
     | This file borrows a tool another file already made.

   4 | import { useNavigate } from "react-router-dom";
     | Borrows React so this file can remember things and draw the screen.

   5 | import Logo from "./Logo";
     | This file borrows a tool another file already made.

   6 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   7 | const GOOGLE_CLIENT_ID = import.meta.env.VITE_GOOGLE_CLIENT_ID;
     | Vite env VITE_GOOGLE_CLIENT_ID. If it is missing, Auth shows a disabled button instead of Google's widget.

   8 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   9 | export default function Auth() {
     | This starts Auth. Google sign-in only. Posts the Google credential to /auth/google, then setUser, setToken, and navigates to /.

  10 |   const { setUser, setToken } = useUser();
     | This gives a short name to a value so the rest of Auth can use it.

  11 |   const [error, setError] = useState("");
     | This gives a short name to a value so the rest of Auth can use it.

  12 |   const [googleLoading, setGoogleLoading] = useState(false);
     | This gives a short name to a value so the rest of Auth can use it.

  13 |   const navigate = useNavigate();
     | This gives a short name to a value so the rest of Auth can use it.

  14 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  15 |   const handleGoogleCredential = useCallback(async (response) => {
     | This gives a short name to a value so the rest of Auth can use it.

  16 |     setGoogleLoading(true);
     | Inside Auth, this line runs as written: setGoogleLoading(true);. It happens in order, after the line above it and before the line below it.

  17 |     setError("");
     | Inside Auth, this line runs as written: setError("");. It happens in order, after the line above it and before the line below it.

  18 |     try {
     | Inside Auth, this line runs as written: try {. It happens in order, after the line above it and before the line below it.

  19 |       const data = await api.post("/auth/google", { idToken: response.credential });
     | This gives a short name to a value so the rest of Auth can use it.

  20 |       setUser(data.user);
     | Inside Auth, this line runs as written: setUser(data.user);. It happens in order, after the line above it and before the line below it.

  21 |       setToken(data.token);
     | Inside Auth, this line runs as written: setToken(data.token);. It happens in order, after the line above it and before the line below it.

  22 |       navigate("/");
     | Inside Auth, this line runs as written: navigate("/");. It happens in order, after the line above it and before the line below it.

  23 |     } catch (err) {
     | This ends try { (opened on line 18).

  24 |       const msg =
     | This gives a short name to a value so the rest of Auth can use it.

  25 |         err.response?.data?.error ||
     | Inside Auth, this line runs as written: err.response?.data?.error ||. It happens in order, after the line above it and before the line below it.

  26 |         err.response?.data?.message ||
     | Inside Auth, this line runs as written: err.response?.data?.message ||. It happens in order, after the line above it and before the line below it.

  27 |         err.message ||
     | Inside Auth, this line runs as written: err.message ||. It happens in order, after the line above it and before the line below it.

  28 |         "Google sign-in failed";
     | Inside Auth, this line runs as written: "Google sign-in failed";. It happens in order, after the line above it and before the line below it.

  29 |       setError(msg);
     | Inside Auth, this line runs as written: setError(msg);. It happens in order, after the line above it and before the line below it.

  30 |     } finally {
     | This ends } catch (err) { (opened on line 23).

  31 |       setGoogleLoading(false);
     | Inside Auth, this line runs as written: setGoogleLoading(false);. It happens in order, after the line above it and before the line below it.

  32 |     }
     | This ends } finally { (opened on line 30).

  33 |   }, [navigate, setUser, setToken]);
     | This ends const handleGoogleCredential = useCallback(async (opened on line 15).

  34 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  35 |   const gsiInitializedRef = useRef(false);
     | This gives a short name to a value so the rest of Auth can use it.

  36 |   const googleButtonWrapRef = useRef(null);
     | This gives a short name to a value so the rest of Auth can use it.

  37 |   const googleButtonBoxRef = useRef(null);
     | This gives a short name to a value so the rest of Auth can use it.

  38 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  39 |   const initGoogleIdentity = useCallback(() => {
     | This gives a short name to a value so the rest of Auth can use it.

  40 |     if (!GOOGLE_CLIENT_ID || !window.google) return false;
     | This asks a yes-or-no question. The next bit runs only on yes.

  41 |     window.google.accounts.id.initialize({
     | Inside Auth, this line runs as written: window.google.accounts.id.initialize({. It happens in order, after the line above it and before the line below it.

  42 |       client_id: GOOGLE_CLIENT_ID,
     | Inside Auth, this line runs as written: client_id: GOOGLE_CLIENT_ID,. It happens in order, after the line above it and before the line below it.

  43 |       callback: handleGoogleCredential,
     | Inside Auth, this line runs as written: callback: handleGoogleCredential,. It happens in order, after the line above it and before the line below it.

  44 |     });
     | This ends window.google.accounts.id.initialize({ (opened on line 41).

  45 |     // Render Google's own button on top of our styled one. Unlike One Tap's
     | A note written for people. The app does not run it.

  46 |     // silent prompt() below, a click on Google's real button always opens
     | A note written for people. The app does not run it.

  47 |     // their standard account-chooser popup/redirect — this keeps working on
     | A note written for people. The app does not run it.

  48 |     // a brand-new device/browser profile, with third-party cookies blocked,
     | A note written for people. The app does not run it.

  49 |     // or anywhere else One Tap silently declines to show (which it does
     | A note written for people. The app does not run it.

  50 |     // without any error, just no UI at all).
     | A note written for people. The app does not run it.

  51 |     if (googleButtonBoxRef.current) {
     | This asks a yes-or-no question. The next bit runs only on yes.

  52 |       const width = Math.min(400, Math.max(200, Math.round(
     | This gives a short name to a value so the rest of Auth can use it.

  53 |         googleButtonWrapRef.current?.getBoundingClientRect().width || 320
     | Inside Auth, this line runs as written: googleButtonWrapRef.current?.getBoundingClientRect().width || 320. It happens in order, after the line above it and before the line below it.

  54 |       )));
     | This closes a box of instructions that opened above.

  55 |       window.google.accounts.id.renderButton(googleButtonBoxRef.current, {
     | Inside Auth, this line runs as written: window.google.accounts.id.renderButton(googleButtonBoxRef.current, {. It happens in order, after the line above it and before the line below it.

  56 |         type: "standard",
     | Inside Auth, this line runs as written: type: "standard",. It happens in order, after the line above it and before the line below it.

  57 |         theme: "outline",
     | Inside Auth, this line runs as written: theme: "outline",. It happens in order, after the line above it and before the line below it.

  58 |         size: "large",
     | Inside Auth, this line runs as written: size: "large",. It happens in order, after the line above it and before the line below it.

  59 |         shape: "pill",
     | Inside Auth, this line runs as written: shape: "pill",. It happens in order, after the line above it and before the line below it.

  60 |         text: "continue_with",
     | Inside Auth, this line runs as written: text: "continue_with",. It happens in order, after the line above it and before the line below it.

  61 |         logo_alignment: "center",
     | Inside Auth, this line runs as written: logo_alignment: "center",. It happens in order, after the line above it and before the line below it.

  62 |         width,
     | Inside Auth, this line runs as written: width,. It happens in order, after the line above it and before the line below it.

  63 |       });
     | This ends window.google.accounts.id.renderButton(googleBut (opened on line 55).

  64 |     }
     | This ends if (googleButtonBoxRef.current) { (opened on line 51).

  65 |     gsiInitializedRef.current = true;
     | Inside Auth, this line runs as written: gsiInitializedRef.current = true;. It happens in order, after the line above it and before the line below it.

  66 |     // Also try the silent One Tap prompt for returning users on a device
     | A note written for people. The app does not run it.

  67 |     // Google already recognizes. If it can't be shown, notification carries
     | A note written for people. The app does not run it.

  68 |     // the reason but we don't surface it as an error — the real button
     | A note written for people. The app does not run it.

  69 |     // above is always there as the reliable path.
     | A note written for people. The app does not run it.

  70 |     window.google.accounts.id.prompt();
     | Inside Auth, this line runs as written: window.google.accounts.id.prompt();. It happens in order, after the line above it and before the line below it.

  71 |     return true;
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  72 |   }, [handleGoogleCredential]);
     | This ends const initGoogleIdentity = useCallback(() => { (opened on line 39).

  73 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  74 |   // Initialise Google Identity Services as soon as the script is ready.
     | A note written for people. The app does not run it.

  75 |   // The script tag loads with `async defer`, so it may not be available yet
     | A note written for people. The app does not run it.

  76 |   // on mount — poll briefly instead of giving up after a single check.
     | A note written for people. The app does not run it.

  77 |   useEffect(() => {
     | This is an extra job that happens after the picture is drawn.

  78 |     if (initGoogleIdentity()) return;
     | This asks a yes-or-no question. The next bit runs only on yes.

  79 |     const interval = setInterval(() => {
     | This gives a short name to a value so the rest of Auth can use it.

  80 |       if (initGoogleIdentity()) clearInterval(interval);
     | This asks a yes-or-no question. The next bit runs only on yes.

  81 |     }, 200);
     | This ends const interval = setInterval(() => { (opened on line 79).

  82 |     return () => clearInterval(interval);
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  83 |   }, [initGoogleIdentity]);
     | This ends effect in Auth (opened on line 77).

  84 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  85 |   return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  86 |     <div className="auth-page">
     | This draws one piece of the page while Auth is showing.

  87 |       <div className="card auth-card">
     | This draws one piece of the page while Auth is showing.

  88 |         <div className="auth-header">
     | This draws one piece of the page while Auth is showing.

  89 |           <div className="auth-brand">
     | This draws one piece of the page while Auth is showing.

  90 |             <Logo size={28} variant="icon" />
     | This draws one piece of the page while Auth is showing.

  91 |           </div>
     | This ends a drawing that Auth started just above.

  92 |           <h1 className="auth-title">JumpyBrain</h1>
     | This draws one piece of the page while Auth is showing.

  93 |           <p className="auth-subtitle">Sign in to continue</p>
     | This draws one piece of the page while Auth is showing.

  94 |           <p className="auth-value">
     | This draws one piece of the page while Auth is showing.

  95 |             Focus timers, habits, and gentle nudges that turn scattered days into steady progress.
     | Inside Auth, this line runs as written: Focus timers, habits, and gentle nudges that turn scattered days into steady progress.. It happens in order, after the line above it and before the line below it.

  96 |           </p>
     | This ends a drawing that Auth started just above.

  97 |         </div>
     | This ends a drawing that Auth started just above.

  98 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  99 |         <div className="auth-status" role="status" aria-live="polite">
     | This draws one piece of the page while Auth is showing.

 100 |           {error && <div className="auth-error">{error}</div>}
     | This ends Auth (opened on line 9).

 101 |         </div>
     | This ends a drawing that Auth started just above.

 102 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 103 |         {GOOGLE_CLIENT_ID ? (
     | Inside Auth, this line runs as written: {GOOGLE_CLIENT_ID ? (. It happens in order, after the line above it and before the line below it.

 104 |           <div className="google-btn-wrap" ref={googleButtonWrapRef}>
     | This draws one piece of the page while Auth is showing.

 105 |             <button
     | This draws one piece of the page while Auth is showing.

 106 |               type="button"
     | Inside Auth, this line runs as written: type="button". It happens in order, after the line above it and before the line below it.

 107 |               className="btn-google"
     | Inside Auth, this line runs as written: className="btn-google". It happens in order, after the line above it and before the line below it.

 108 |               disabled={googleLoading}
     | This ends Auth (opened on line 9).

 109 |               tabIndex={-1}
     | This ends Auth (opened on line 9).

 110 |               aria-hidden="true"
     | Inside Auth, this line runs as written: aria-hidden="true". It happens in order, after the line above it and before the line below it.

 111 |             >
     | Inside Auth, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 112 |               {googleLoading ? (
     | Inside Auth, this line runs as written: {googleLoading ? (. It happens in order, after the line above it and before the line below it.

 113 |                 <>
     | This draws one piece of the page while Auth is showing.

 114 |                   <span className="spinner" aria-hidden="true" />
     | This draws one piece of the page while Auth is showing.

 115 |                   Redirecting…
     | Inside Auth, this line runs as written: Redirecting…. It happens in order, after the line above it and before the line below it.

 116 |                 </>
     | This ends a drawing that Auth started just above.

 117 |               ) : (
     | This closes a box of instructions that opened above.

 118 |                 <>
     | This draws one piece of the page while Auth is showing.

 119 |                   <svg width="18" height="18" viewBox="0 0 18 18" fill="none" aria-hidden="true">
     | This draws one piece of the page while Auth is showing.

 120 |                     <path d="M17.64 9.2c0-.637-.057-1.251-.164-1.84H9v3.481h4.844c-.209 1.125-.843 2.078-1.796 2.717v2.258h2.908c1.702-1.567 2.684-3.874 2.684-6.615z" fill="#4285F4"/>
     | This draws one piece of the page while Auth is showing.

 121 |                     <path d="M9 18c2.43 0 4.467-.806 5.956-2.184l-2.908-2.258c-.806.54-1.837.86-3.048.86-2.344 0-4.328-1.584-5.036-3.711H.957v2.332C2.438 15.983 5.482 18 9 18z" fill="#34A853"/>
     | This draws one piece of the page while Auth is showing.

 122 |                     <path d="M3.964 10.707A5.41 5.41 0 0 1 3.682 9c0-.593.102-1.17.282-1.707V4.961H.957A8.996 8.996 0 0 0 0 9c0 1.452.348 2.827.957 4.039l3.007-2.332z" fill="#FBBC05"/>
     | This draws one piece of the page while Auth is showing.

 123 |                     <path d="M9 3.58c1.321 0 2.508.454 3.44 1.345l2.582-2.58C13.463.891 11.426 0 9 0 5.482 0 2.438 2.017.957 4.961L3.964 6.293C4.672 4.166 6.656 3.58 9 3.58z" fill="#EA4335"/>
     | This draws one piece of the page while Auth is showing.

 124 |                   </svg>
     | This ends a drawing that Auth started just above.

 125 |                   Continue with Google
     | Inside Auth, this line runs as written: Continue with Google. It happens in order, after the line above it and before the line below it.

 126 |                 </>
     | This ends a drawing that Auth started just above.

 127 |               )}
     | This ends Auth (opened on line 9).

 128 |             </button>
     | This ends a drawing that Auth started just above.

 129 |             {/* Google renders its real, clickable button here on top of the
     | Inside Auth, this line runs as written: {/* Google renders its real, clickable button here on top of the. It happens in order, after the line above it and before the line below it.

 130 |                 styled one above (see .google-btn-overlay) so clicks open
     | Inside Auth, this line runs as written: styled one above (see .google-btn-overlay) so clicks open. It happens in order, after the line above it and before the line below it.

 131 |                 Google's own popup/redirect flow directly, instead of going
     | Inside Auth, this line runs as written: Google's own popup/redirect flow directly, instead of going. It happens in order, after the line above it and before the line below it.

 132 |                 through the silent, less reliable One Tap prompt. */}
     | This ends Auth (opened on line 9).

 133 |             <div className="google-btn-overlay" ref={googleButtonBoxRef} />
     | This draws one piece of the page while Auth is showing.

 134 |           </div>
     | This ends a drawing that Auth started just above.

 135 |         ) : (
     | This closes a box of instructions that opened above.

 136 |           <button type="button" className="btn-google" disabled>
     | This draws one piece of the page while Auth is showing.

 137 |             Google Sign-In is not configured
     | Inside Auth, this line runs as written: Google Sign-In is not configured. It happens in order, after the line above it and before the line below it.

 138 |           </button>
     | This ends a drawing that Auth started just above.

 139 |         )}
     | This ends Auth (opened on line 9).

 140 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 141 |         <p className="auth-legal">
     | This draws one piece of the page while Auth is showing.

 142 |           By continuing you agree to our{" "}
     | This ends Auth (opened on line 9).

 143 |           <a href="/terms" className="text-link">Terms of Service</a> and{" "}
     | This draws one piece of the page while Auth is showing.

 144 |           <a href="/privacy" className="text-link">Privacy Policy</a>.
     | This draws one piece of the page while Auth is showing.

 145 |         </p>
     | This ends a drawing that Auth started just above.

 146 |       </div>
     | This ends a drawing that Auth started just above.

 147 |     </div>
     | This ends a drawing that Auth started just above.

 148 |   );
     | This closes a box of instructions that opened above.

 149 | }
     | This ends Auth (opened on line 9).

