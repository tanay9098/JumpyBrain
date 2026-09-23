# `src/components/FocusOverlay.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import React, { useEffect, useRef, useState } from "react";
     | Borrows React so this file can remember things and draw the screen.

   2 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   3 | import { tabAlertSound } from "../utils/sound";
     | This file borrows a tool another file already made.

   4 | import { notify } from "../utils/notify";
     | This file borrows a tool another file already made.

   5 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   6 | // ── 3-State Focus FSM ────────────────────────────────────────────────────
     | A note written for people. The app does not run it.

   7 | // idle      → no session running
     | A note written for people. The app does not run it.

   8 | // focused   → session active, tab visible
     | A note written for people. The app does not run it.

   9 | // distracted → tab hidden, 800ms debounce timer started
     | A note written for people. The app does not run it.

  10 | // alert     → 800ms elapsed, show nudge overlay
     | A note written for people. The app does not run it.

  11 | //
     | A note written for people. The app does not run it.

  12 | // Transitions:
     | A note written for people. The app does not run it.

  13 | //   idle      → focused   : FocusTimer calls setFocusActive(true)
     | A note written for people. The app does not run it.

  14 | //   focused   → distracted: visibilitychange hidden
     | A note written for people. The app does not run it.

  15 | //   distracted → focused  : visibilitychange visible (cancel debounce)
     | A note written for people. The app does not run it.

  16 | //   distracted → alert    : 800ms timeout fires
     | A note written for people. The app does not run it.

  17 | //   alert     → focused   : user clicks "I'm back"
     | A note written for people. The app does not run it.

  18 | //   focused   → idle      : FocusTimer calls setFocusActive(false)
     | A note written for people. The app does not run it.

  19 | //   alert     → idle      : user clicks "End session"
     | A note written for people. The app does not run it.

  20 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  21 | const STATES = { IDLE: "idle", FOCUSED: "focused", DISTRACTED: "distracted", ALERT: "alert" };
     | Focus overlay state machine: idle, focused, distracted (left the tab, waiting 800ms), alert (show the nudge).

  22 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  23 | // Global bridge — FocusTimer calls this to start/stop a session
     | A note written for people. The app does not run it.

  24 | let _bridge = null;
     | This gives a short name to a value so the rest of the top of the file can use it.

  25 | export function setFocusActive(active, taskName = "") {
     | This lets another file use this piece by its name.

  26 |   if (_bridge) _bridge(active, taskName);
     | This asks a yes-or-no question. The next bit runs only on yes.

  27 | }
     | This ends setFocusActive (opened on line 25).

  28 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  29 | // Distraction counter accessible to FocusTimer on session complete
     | A note written for people. The app does not run it.

  30 | let _distractionCount = 0;
     | This gives a short name to a value so the rest of the top of the file can use it.

  31 | let _distractionCountRef = { current: 0 };
     | This gives a short name to a value so the rest of the top of the file can use it.

  32 | export function getDistractionCount() { return _distractionCountRef.current; }
     | This lets another file use this piece by its name.

  33 | export function resetDistractionCount() { _distractionCountRef.current = 0; }
     | This lets another file use this piece by its name.

  34 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  35 | export default function FocusOverlay() {
     | This starts FocusOverlay. Mounted once in App, beside the routes. Watches document visibility only while a session is focused.

  36 |   const [state, setStateRaw] = useState(STATES.IDLE);
     | This gives a short name to a value so the rest of FocusOverlay can use it.

  37 |   const [taskName, setTaskName] = useState("");
     | This gives a short name to a value so the rest of FocusOverlay can use it.

  38 |   const [distractionCount, setDistractionCount] = useState(0);
     | How many times the 800ms timer fired during this focus session. Posted with the session so the shield page can show 'distractions today'.

  39 |   const stateRef = useRef(STATES.IDLE);
     | This gives a short name to a value so the rest of FocusOverlay can use it.

  40 |   const taskNameRef = useRef("");
     | This gives a short name to a value so the rest of FocusOverlay can use it.

  41 |   const debounceRef = useRef(null);
     | This gives a short name to a value so the rest of FocusOverlay can use it.

  42 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  43 |   function setState(s) {
     | This starts setState. Writes both the ref (so the visibility listener is not stale) and React state (so the alert card appears).

  44 |     stateRef.current = s;
     | Inside setState, this line runs as written: stateRef.current = s;. It happens in order, after the line above it and before the line below it.

  45 |     setStateRaw(s);
     | Inside setState, this line runs as written: setStateRaw(s);. It happens in order, after the line above it and before the line below it.

  46 |   }
     | This ends setState (opened on line 43).

  47 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  48 |   // Register bridge
     | A note written for people. The app does not run it.

  49 |   useEffect(() => {
     | This is an extra job that happens after the picture is drawn.

  50 |     _bridge = (active, name) => {
     | Inside FocusOverlay, this line runs as written: _bridge = (active, name) => {. It happens in order, after the line above it and before the line below it.

  51 |       if (active) {
     | This asks a yes-or-no question. The next bit runs only on yes.

  52 |         setState(STATES.FOCUSED);
     | Inside FocusOverlay, this line runs as written: setState(STATES.FOCUSED);. It happens in order, after the line above it and before the line below it.

  53 |         setTaskName(name);
     | Inside FocusOverlay, this line runs as written: setTaskName(name);. It happens in order, after the line above it and before the line below it.

  54 |         taskNameRef.current = name;
     | Inside FocusOverlay, this line runs as written: taskNameRef.current = name;. It happens in order, after the line above it and before the line below it.

  55 |         setDistractionCount(0);
     | Inside FocusOverlay, this line runs as written: setDistractionCount(0);. It happens in order, after the line above it and before the line below it.

  56 |         _distractionCountRef.current = 0;
     | Inside FocusOverlay, this line runs as written: _distractionCountRef.current = 0;. It happens in order, after the line above it and before the line below it.

  57 |       } else {
     | This ends if (active) { (opened on line 51).

  58 |         clearTimeout(debounceRef.current);
     | Inside FocusOverlay, this line runs as written: clearTimeout(debounceRef.current);. It happens in order, after the line above it and before the line below it.

  59 |         setState(STATES.IDLE);
     | Inside FocusOverlay, this line runs as written: setState(STATES.IDLE);. It happens in order, after the line above it and before the line below it.

  60 |         setTaskName("");
     | Inside FocusOverlay, this line runs as written: setTaskName("");. It happens in order, after the line above it and before the line below it.

  61 |       }
     | This ends } else { (opened on line 57).

  62 |     };
     | This ends _bridge = (active, name) => { (opened on line 50).

  63 |     return () => { _bridge = null; };
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  64 |   }, []);
     | This ends effect in FocusOverlay (opened on line 49).

  65 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  66 |   // Page Visibility FSM — single persistent listener using stateRef
     | A note written for people. The app does not run it.

  67 |   useEffect(() => {
     | This is an extra job that happens after the picture is drawn.

  68 |     function onVisibility() {
     | Inside onVisibility, this line runs as written: function onVisibility() {. It happens in order, after the line above it and before the line below it.

  69 |       if (document.visibilityState === "hidden") {
     | This asks a yes-or-no question. The next bit runs only on yes.

  70 |         if (stateRef.current === STATES.FOCUSED) {
     | This asks a yes-or-no question. The next bit runs only on yes.

  71 |           setState(STATES.DISTRACTED);
     | Inside onVisibility, this line runs as written: setState(STATES.DISTRACTED);. It happens in order, after the line above it and before the line below it.

  72 |           debounceRef.current = setTimeout(() => {
     | Inside onVisibility, this line runs as written: debounceRef.current = setTimeout(() => {. It happens in order, after the line above it and before the line below it.

  73 |             if (stateRef.current === STATES.DISTRACTED) {
     | This asks a yes-or-no question. The next bit runs only on yes.

  74 |               setState(STATES.ALERT);
     | Inside onVisibility, this line runs as written: setState(STATES.ALERT);. It happens in order, after the line above it and before the line below it.

  75 |               tabAlertSound.play();
     | Inside onVisibility, this line runs as written: tabAlertSound.play();. It happens in order, after the line above it and before the line below it.

  76 |               notify(
     | Inside onVisibility, this line runs as written: notify(. It happens in order, after the line above it and before the line below it.

  77 |                 "Hey, where'd you go?",
     | Inside onVisibility, this line runs as written: "Hey, where'd you go?",. It happens in order, after the line above it and before the line below it.

  78 |                 taskNameRef.current
     | Inside onVisibility, this line runs as written: taskNameRef.current. It happens in order, after the line above it and before the line below it.

  79 |                   ? `You were working on "${taskNameRef.current}". Come back and finish strong.`
     | This ends if (stateRef.current === STATES.DISTRACT (opened on line 73).

  80 |                   : "You switched away during a focus session. Come back and finish strong."
     | Inside onVisibility, this line runs as written: : "You switched away during a focus session. Come back and finish strong.". It happens in order, after the line above it and before the line below it.

  81 |               );
     | This closes a box of instructions that opened above.

  82 |               // Track distraction count for ML
     | A note written for people. The app does not run it.

  83 |               setDistractionCount((c) => {
     | Inside onVisibility, this line runs as written: setDistractionCount((c) => {. It happens in order, after the line above it and before the line below it.

  84 |                 const next = c + 1;
     | This gives a short name to a value so the rest of onVisibility can use it.

  85 |                 _distractionCountRef.current = next;
     | Inside onVisibility, this line runs as written: _distractionCountRef.current = next;. It happens in order, after the line above it and before the line below it.

  86 |                 return next;
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  87 |               });
     | This ends setDistractionCount((c) => { (opened on line 83).

  88 |             }
     | This ends if (stateRef.current === STATES.DISTRACT (opened on line 73).

  89 |           }, 800);
     | This ends debounceRef.current = setTimeout(() => { (opened on line 72).

  90 |         }
     | This ends if (stateRef.current === STATES.FOCUSED) (opened on line 70).

  91 |       } else {
     | This ends if (document.visibilityState === "hidden (opened on line 69).

  92 |         // Tab came back
     | A note written for people. The app does not run it.

  93 |         if (stateRef.current === STATES.DISTRACTED) {
     | This asks a yes-or-no question. The next bit runs only on yes.

  94 |           clearTimeout(debounceRef.current);
     | Inside onVisibility, this line runs as written: clearTimeout(debounceRef.current);. It happens in order, after the line above it and before the line below it.

  95 |           setState(STATES.FOCUSED);
     | Inside onVisibility, this line runs as written: setState(STATES.FOCUSED);. It happens in order, after the line above it and before the line below it.

  96 |         }
     | This ends if (stateRef.current === STATES.DISTRACT (opened on line 93).

  97 |       }
     | This ends } else { (opened on line 91).

  98 |     }
     | This ends onVisibility (opened on line 68).

  99 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 100 |     document.addEventListener("visibilitychange", onVisibility);
     | Inside FocusOverlay, this line runs as written: document.addEventListener("visibilitychange", onVisibility);. It happens in order, after the line above it and before the line below it.

 101 |     return () => {
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

 102 |       document.removeEventListener("visibilitychange", onVisibility);
     | Inside FocusOverlay, this line runs as written: document.removeEventListener("visibilitychange", onVisibility);. It happens in order, after the line above it and before the line below it.

 103 |       clearTimeout(debounceRef.current);
     | Inside FocusOverlay, this line runs as written: clearTimeout(debounceRef.current);. It happens in order, after the line above it and before the line below it.

 104 |     };
     | This ends return () => { (opened on line 101).

 105 |   }, []); // mount once — uses stateRef to avoid stale closures
     | This ends effect in FocusOverlay (opened on line 67).

 106 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 107 |   function onImBack() {
     | This starts onImBack. Alert → focused. The countdown keeps running; this only dismisses the card.

 108 |     setState(STATES.FOCUSED);
     | Inside onImBack, this line runs as written: setState(STATES.FOCUSED);. It happens in order, after the line above it and before the line below it.

 109 |   }
     | This ends onImBack (opened on line 107).

 110 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 111 |   function onEndSession() {
     | This starts onEndSession. Alert → idle and clears the debounce. It does not by itself stop FocusTimer's interval.

 112 |     clearTimeout(debounceRef.current);
     | Inside onEndSession, this line runs as written: clearTimeout(debounceRef.current);. It happens in order, after the line above it and before the line below it.

 113 |     setState(STATES.IDLE);
     | Inside onEndSession, this line runs as written: setState(STATES.IDLE);. It happens in order, after the line above it and before the line below it.

 114 |     setTaskName("");
     | Inside onEndSession, this line runs as written: setTaskName("");. It happens in order, after the line above it and before the line below it.

 115 |   }
     | This ends onEndSession (opened on line 111).

 116 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 117 |   if (state !== STATES.ALERT) return null;
     | This asks a yes-or-no question. The next bit runs only on yes.

 118 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 119 |   return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

 120 |     <div className="focus-overlay">
     | This draws one piece of the page while FocusOverlay is showing.

 121 |       <div className="focus-overlay-card">
     | This draws one piece of the page while FocusOverlay is showing.

 122 |         <div className="focus-overlay-icon">🧘</div>
     | This draws one piece of the page while FocusOverlay is showing.

 123 |         <div className="focus-overlay-title">Hey, where'd you go?</div>
     | This draws one piece of the page while FocusOverlay is showing.

 124 |         <div className="focus-overlay-text">
     | This draws one piece of the page while FocusOverlay is showing.

 125 |           {taskName
     | Inside FocusOverlay, this line runs as written: {taskName. It happens in order, after the line above it and before the line below it.

 126 |             ? <>You were working on <strong>"{taskName}"</strong>.<br /></>
     | This ends FocusOverlay (opened on line 35).

 127 |             : null}
     | This ends FocusOverlay (opened on line 35).

 128 |           Take a slow breath and come back.
     | Inside FocusOverlay, this line runs as written: Take a slow breath and come back.. It happens in order, after the line above it and before the line below it.

 129 |           <br />
     | This draws one piece of the page while FocusOverlay is showing.

 130 |           <span style={{ fontSize: 12, opacity: 0.7 }}>Try 30 seconds of belly breathing.</span>
     | This draws one piece of the page while FocusOverlay is showing.

 131 |         </div>
     | This ends a drawing that FocusOverlay started just above.

 132 |         <div style={{ display: "flex", gap: 10, justifyContent: "center" }}>
     | This draws one piece of the page while FocusOverlay is showing.

 133 |           <button className="btn btn-primary" onClick={onImBack}>
     | This draws one piece of the page while FocusOverlay is showing.

 134 |             I'm back ✓
     | Inside FocusOverlay, this line runs as written: I'm back ✓. It happens in order, after the line above it and before the line below it.

 135 |           </button>
     | This ends a drawing that FocusOverlay started just above.

 136 |           <button className="btn btn-ghost" onClick={onEndSession}>
     | This draws one piece of the page while FocusOverlay is showing.

 137 |             End session
     | Inside FocusOverlay, this line runs as written: End session. It happens in order, after the line above it and before the line below it.

 138 |           </button>
     | This ends a drawing that FocusOverlay started just above.

 139 |         </div>
     | This ends a drawing that FocusOverlay started just above.

 140 |       </div>
     | This ends a drawing that FocusOverlay started just above.

 141 |     </div>
     | This ends a drawing that FocusOverlay started just above.

 142 |   );
     | This closes a box of instructions that opened above.

 143 | }
     | This ends FocusOverlay (opened on line 35).

