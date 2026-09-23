# `src/components/FocusOverlay.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | import React, { useEffect, useRef, useState } from "react";
     | Import for the full-screen nudge when you leave a focus tab: `import React, { useEffect, useRef, useState } from "react";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   2 | 
     | Blank line in `src/components/FocusOverlay.jsx` (the full-screen nudge when you leave a focus tab), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   3 | import { tabAlertSound } from "../utils/sound";
     | Import for the full-screen nudge when you leave a focus tab: `import { tabAlertSound } from "../utils/sound";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   4 | import { notify } from "../utils/notify";
     | Import for the full-screen nudge when you leave a focus tab: `import { notify } from "../utils/notify";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

   5 | 
     | Blank line in `src/components/FocusOverlay.jsx` (the full-screen nudge when you leave a focus tab), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   6 | // ── 3-State Focus FSM ────────────────────────────────────────────────────
     | Comment inside the top of the file. Not executed. It documents the next code: ── 3-State Focus FSM ────────────────────────────────────────────────────

   7 | // idle      → no session running
     | Comment inside the top of the file. Not executed. It documents the next code: idle      → no session running

   8 | // focused   → session active, tab visible
     | Comment inside the top of the file. Not executed. It documents the next code: focused   → session active, tab visible

   9 | // distracted → tab hidden, 800ms debounce timer started
     | Comment inside the top of the file. Not executed. It documents the next code: distracted → tab hidden, 800ms debounce timer started

  10 | // alert     → 800ms elapsed, show nudge overlay
     | Comment inside the top of the file. Not executed. It documents the next code: alert     → 800ms elapsed, show nudge overlay

  11 | //
     | Comment inside the top of the file. Not executed. It documents the next code: 

  12 | // Transitions:
     | Comment inside the top of the file. Not executed. It documents the next code: Transitions:

  13 | //   idle      → focused   : FocusTimer calls setFocusActive(true)
     | Comment inside the top of the file. Not executed. It documents the next code: idle      → focused   : FocusTimer calls setFocusActive(true)

  14 | //   focused   → distracted: visibilitychange hidden
     | Comment inside the top of the file. Not executed. It documents the next code: focused   → distracted: visibilitychange hidden

  15 | //   distracted → focused  : visibilitychange visible (cancel debounce)
     | Comment inside the top of the file. Not executed. It documents the next code: distracted → focused  : visibilitychange visible (cancel debounce)

  16 | //   distracted → alert    : 800ms timeout fires
     | Comment inside the top of the file. Not executed. It documents the next code: distracted → alert    : 800ms timeout fires

  17 | //   alert     → focused   : user clicks "I'm back"
     | Comment inside the top of the file. Not executed. It documents the next code: alert     → focused   : user clicks "I'm back"

  18 | //   focused   → idle      : FocusTimer calls setFocusActive(false)
     | Comment inside the top of the file. Not executed. It documents the next code: focused   → idle      : FocusTimer calls setFocusActive(false)

  19 | //   alert     → idle      : user clicks "End session"
     | Comment inside the top of the file. Not executed. It documents the next code: alert     → idle      : user clicks "End session"

  20 | 
     | Blank line in `src/components/FocusOverlay.jsx` (the full-screen nudge when you leave a focus tab), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  21 | const STATES = { IDLE: "idle", FOCUSED: "focused", DISTRACTED: "distracted", ALERT: "alert" };
     | In `the top of the file` (src/components/FocusOverlay.jsx): `STATES`: Focus overlay state machine: idle, focused, distracted (left the tab, waiting 800ms), alert (show the nudge). The code is `const STATES = { IDLE: "idle", FOCUSED: "focused", DISTRACTED: "distracted", ALERT: "alert" };`.

  22 | 
     | Blank line in `src/components/FocusOverlay.jsx` (the full-screen nudge when you leave a focus tab), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  23 | // Global bridge — FocusTimer calls this to start/stop a session
     | Comment inside the top of the file. Not executed. It documents the next code: Global bridge — FocusTimer calls this to start/stop a session

  24 | let _bridge = null;
     | In `the top of the file` (src/components/FocusOverlay.jsx): `_bridge` is assigned `null;`. Later lines in this function read that name.

  25 | export function setFocusActive(active, taskName = "") {
     | Named export from the full-screen nudge when you leave a focus tab: `export function setFocusActive(active, taskName = "") {`.

  26 |   if (_bridge) _bridge(active, taskName);
     | In `setFocusActive` (src/components/FocusOverlay.jsx): branch `if (_bridge) _bridge(active, taskName);`. Only one side runs.

  27 | }
     | In `setFocusActive` (src/components/FocusOverlay.jsx): `}` closes setFocusActive (opened on line 25). Names declared inside that block end here.

  28 | 
     | Blank line in `src/components/FocusOverlay.jsx` (the full-screen nudge when you leave a focus tab), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  29 | // Distraction counter accessible to FocusTimer on session complete
     | Comment inside the top of the file. Not executed. It documents the next code: Distraction counter accessible to FocusTimer on session complete

  30 | let _distractionCount = 0;
     | In `the top of the file` (src/components/FocusOverlay.jsx): `_distractionCount` is assigned `0;`. Later lines in this function read that name.

  31 | let _distractionCountRef = { current: 0 };
     | In `the top of the file` (src/components/FocusOverlay.jsx): `_distractionCountRef` is assigned `{ current: 0 };`. Later lines in this function read that name.

  32 | export function getDistractionCount() { return _distractionCountRef.current; }
     | Named export from the full-screen nudge when you leave a focus tab: `export function getDistractionCount() { return _distractionCountRef.current; }`.

  33 | export function resetDistractionCount() { _distractionCountRef.current = 0; }
     | Named export from the full-screen nudge when you leave a focus tab: `export function resetDistractionCount() { _distractionCountRef.current = 0; }`.

  34 | 
     | Blank line in `src/components/FocusOverlay.jsx` (the full-screen nudge when you leave a focus tab), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  35 | export default function FocusOverlay() {
     | Defines `FocusOverlay` in the full-screen nudge when you leave a focus tab. Mounted once in App, beside the routes. Watches document visibility only while a session is focused.

  36 |   const [state, setStateRaw] = useState(STATES.IDLE);
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): React state `state, setStateRaw`. The value survives re-renders. Calling the setter re-renders this component. `const [state, setStateRaw] = useState(STATES.IDLE);`

  37 |   const [taskName, setTaskName] = useState("");
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): React state `taskName, setTaskName`. The value survives re-renders. Calling the setter re-renders this component. `const [taskName, setTaskName] = useState("");`

  38 |   const [distractionCount, setDistractionCount] = useState(0);
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): `distractionCount`: How many times the 800ms timer fired during this focus session. Posted with the session so the shield page can show 'distractions today'. The code is `const [distractionCount, setDistractionCount] = useState(0);`.

  39 |   const stateRef = useRef(STATES.IDLE);
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): A ref `stateRef`. `.current` survives re-renders and writing it does not re-render. `const stateRef = useRef(STATES.IDLE);`

  40 |   const taskNameRef = useRef("");
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): A ref `taskNameRef`. `.current` survives re-renders and writing it does not re-render. `const taskNameRef = useRef("");`

  41 |   const debounceRef = useRef(null);
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): A ref `debounceRef`. `.current` survives re-renders and writing it does not re-render. `const debounceRef = useRef(null);`

  42 | 
     | Blank line in `src/components/FocusOverlay.jsx` (the full-screen nudge when you leave a focus tab), inside FocusOverlay. The parser skips it. It separates the previous statement from the next so the function is readable.

  43 |   function setState(s) {
     | Defines `setState` in the full-screen nudge when you leave a focus tab. Writes both the ref (so the visibility listener is not stale) and React state (so the alert card appears).

  44 |     stateRef.current = s;
     | In `setState` (src/components/FocusOverlay.jsx): statement `stateRef.current = s;`. It runs when setState runs, in order, before the next line of the same function.

  45 |     setStateRaw(s);
     | In `setState` (src/components/FocusOverlay.jsx): statement `setStateRaw(s);`. It runs when setState runs, in order, before the next line of the same function.

  46 |   }
     | In `setState` (src/components/FocusOverlay.jsx): `}` closes setState (opened on line 43). Names declared inside that block end here.

  47 | 
     | Blank line in `src/components/FocusOverlay.jsx` (the full-screen nudge when you leave a focus tab), inside FocusOverlay. The parser skips it. It separates the previous statement from the next so the function is readable.

  48 |   // Register bridge
     | Comment inside FocusOverlay. Not executed. It documents the next code: Register bridge

  49 |   useEffect(() => {
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): opens or continues an effect — `useEffect(() => {`. The effect body runs after paint, and its cleanup runs before the next effect and on unmount.

  50 |     _bridge = (active, name) => {
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): statement `_bridge = (active, name) => {`. It runs when FocusOverlay runs, in order, before the next line of the same function.

  51 |       if (active) {
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): branch `if (active) {`. Only one side runs.

  52 |         setState(STATES.FOCUSED);
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): statement `setState(STATES.FOCUSED);`. It runs when FocusOverlay runs, in order, before the next line of the same function.

  53 |         setTaskName(name);
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): statement `setTaskName(name);`. It runs when FocusOverlay runs, in order, before the next line of the same function.

  54 |         taskNameRef.current = name;
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): statement `taskNameRef.current = name;`. It runs when FocusOverlay runs, in order, before the next line of the same function.

  55 |         setDistractionCount(0);
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): statement `setDistractionCount(0);`. It runs when FocusOverlay runs, in order, before the next line of the same function.

  56 |         _distractionCountRef.current = 0;
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): statement `_distractionCountRef.current = 0;`. It runs when FocusOverlay runs, in order, before the next line of the same function.

  57 |       } else {
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): branch `} else {`. Only one side runs.

  58 |         clearTimeout(debounceRef.current);
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): timer — `clearTimeout(debounceRef.current);`. The callback runs later on the event loop, not now.

  59 |         setState(STATES.IDLE);
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): statement `setState(STATES.IDLE);`. It runs when FocusOverlay runs, in order, before the next line of the same function.

  60 |         setTaskName("");
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): statement `setTaskName("");`. It runs when FocusOverlay runs, in order, before the next line of the same function.

  61 |       }
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): `}` closes } else { (opened on line 57). Names declared inside that block end here.

  62 |     };
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): `};` closes _bridge = (active, name) => { (opened on line 50). Names declared inside that block end here.

  63 |     return () => { _bridge = null; };
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): return `return () => { _bridge = null; };`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  64 |   }, []);
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): `}, []);` closes effect in FocusOverlay (opened on line 49). Names declared inside that block end here.

  65 | 
     | Blank line in `src/components/FocusOverlay.jsx` (the full-screen nudge when you leave a focus tab), inside FocusOverlay. The parser skips it. It separates the previous statement from the next so the function is readable.

  66 |   // Page Visibility FSM — single persistent listener using stateRef
     | Comment inside FocusOverlay. Not executed. It documents the next code: Page Visibility FSM — single persistent listener using stateRef

  67 |   useEffect(() => {
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): opens or continues an effect — `useEffect(() => {`. The effect body runs after paint, and its cleanup runs before the next effect and on unmount.

  68 |     function onVisibility() {
     | In `onVisibility` (src/components/FocusOverlay.jsx): statement `function onVisibility() {`. It runs when onVisibility runs, in order, before the next line of the same function.

  69 |       if (document.visibilityState === "hidden") {
     | In `onVisibility` (src/components/FocusOverlay.jsx): branch `if (document.visibilityState === "hidden") {`. Only one side runs.

  70 |         if (stateRef.current === STATES.FOCUSED) {
     | In `onVisibility` (src/components/FocusOverlay.jsx): branch `if (stateRef.current === STATES.FOCUSED) {`. Only one side runs.

  71 |           setState(STATES.DISTRACTED);
     | In `onVisibility` (src/components/FocusOverlay.jsx): statement `setState(STATES.DISTRACTED);`. It runs when onVisibility runs, in order, before the next line of the same function.

  72 |           debounceRef.current = setTimeout(() => {
     | In `onVisibility` (src/components/FocusOverlay.jsx): timer — `debounceRef.current = setTimeout(() => {`. The callback runs later on the event loop, not now.

  73 |             if (stateRef.current === STATES.DISTRACTED) {
     | In `onVisibility` (src/components/FocusOverlay.jsx): branch `if (stateRef.current === STATES.DISTRACTED) {`. Only one side runs.

  74 |               setState(STATES.ALERT);
     | In `onVisibility` (src/components/FocusOverlay.jsx): statement `setState(STATES.ALERT);`. It runs when onVisibility runs, in order, before the next line of the same function.

  75 |               tabAlertSound.play();
     | In `onVisibility` (src/components/FocusOverlay.jsx): statement `tabAlertSound.play();`. It runs when onVisibility runs, in order, before the next line of the same function.

  76 |               notify(
     | In `onVisibility` (src/components/FocusOverlay.jsx): statement `notify(`. It runs when onVisibility runs, in order, before the next line of the same function.

  77 |                 "Hey, where'd you go?",
     | In `onVisibility` (src/components/FocusOverlay.jsx): statement `"Hey, where'd you go?",`. It runs when onVisibility runs, in order, before the next line of the same function.

  78 |                 taskNameRef.current
     | In `onVisibility` (src/components/FocusOverlay.jsx): statement `taskNameRef.current`. It runs when onVisibility runs, in order, before the next line of the same function.

  79 |                   ? `You were working on "${taskNameRef.current}". Come back and finish strong.`
     | In `onVisibility` (src/components/FocusOverlay.jsx): `? `You were working on "${taskNameRef.current}". Come back and finish strong.`` closes if (stateRef.current === STATES.DISTRACT (opened on line 73). Names declared inside that block end here.

  80 |                   : "You switched away during a focus session. Come back and finish strong."
     | In `onVisibility` (src/components/FocusOverlay.jsx): statement `: "You switched away during a focus session. Come back and finish strong."`. It runs when onVisibility runs, in order, before the next line of the same function.

  81 |               );
     | In `onVisibility` (src/components/FocusOverlay.jsx): statement `);`. It runs when onVisibility runs, in order, before the next line of the same function.

  82 |               // Track distraction count for ML
     | Comment inside onVisibility. Not executed. It documents the next code: Track distraction count for ML

  83 |               setDistractionCount((c) => {
     | In `onVisibility` (src/components/FocusOverlay.jsx): statement `setDistractionCount((c) => {`. It runs when onVisibility runs, in order, before the next line of the same function.

  84 |                 const next = c + 1;
     | In `onVisibility` (src/components/FocusOverlay.jsx): `next` is assigned `c + 1;`. Later lines in this function read that name.

  85 |                 _distractionCountRef.current = next;
     | In `onVisibility` (src/components/FocusOverlay.jsx): statement `_distractionCountRef.current = next;`. It runs when onVisibility runs, in order, before the next line of the same function.

  86 |                 return next;
     | In `onVisibility` (src/components/FocusOverlay.jsx): return `return next;`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  87 |               });
     | In `onVisibility` (src/components/FocusOverlay.jsx): `});` closes setDistractionCount((c) => { (opened on line 83). Names declared inside that block end here.

  88 |             }
     | In `onVisibility` (src/components/FocusOverlay.jsx): `}` closes if (stateRef.current === STATES.DISTRACT (opened on line 73). Names declared inside that block end here.

  89 |           }, 800);
     | In `onVisibility` (src/components/FocusOverlay.jsx): `}, 800);` closes debounceRef.current = setTimeout(() => { (opened on line 72). Names declared inside that block end here.

  90 |         }
     | In `onVisibility` (src/components/FocusOverlay.jsx): `}` closes if (stateRef.current === STATES.FOCUSED) (opened on line 70). Names declared inside that block end here.

  91 |       } else {
     | In `onVisibility` (src/components/FocusOverlay.jsx): branch `} else {`. Only one side runs.

  92 |         // Tab came back
     | Comment inside onVisibility. Not executed. It documents the next code: Tab came back

  93 |         if (stateRef.current === STATES.DISTRACTED) {
     | In `onVisibility` (src/components/FocusOverlay.jsx): branch `if (stateRef.current === STATES.DISTRACTED) {`. Only one side runs.

  94 |           clearTimeout(debounceRef.current);
     | In `onVisibility` (src/components/FocusOverlay.jsx): timer — `clearTimeout(debounceRef.current);`. The callback runs later on the event loop, not now.

  95 |           setState(STATES.FOCUSED);
     | In `onVisibility` (src/components/FocusOverlay.jsx): statement `setState(STATES.FOCUSED);`. It runs when onVisibility runs, in order, before the next line of the same function.

  96 |         }
     | In `onVisibility` (src/components/FocusOverlay.jsx): `}` closes if (stateRef.current === STATES.DISTRACT (opened on line 93). Names declared inside that block end here.

  97 |       }
     | In `onVisibility` (src/components/FocusOverlay.jsx): `}` closes } else { (opened on line 91). Names declared inside that block end here.

  98 |     }
     | In `onVisibility` (src/components/FocusOverlay.jsx): `}` closes onVisibility (opened on line 68). Names declared inside that block end here.

  99 | 
     | Blank line in `src/components/FocusOverlay.jsx` (the full-screen nudge when you leave a focus tab), inside FocusOverlay. The parser skips it. It separates the previous statement from the next so the function is readable.

 100 |     document.addEventListener("visibilitychange", onVisibility);
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): The browser fires this when the tab is hidden or shown. FocusOverlay uses it for the 800ms nudge. Mindfulness uses it to stop audio.

 101 |     return () => {
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): return `return () => {`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

 102 |       document.removeEventListener("visibilitychange", onVisibility);
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): The browser fires this when the tab is hidden or shown. FocusOverlay uses it for the 800ms nudge. Mindfulness uses it to stop audio.

 103 |       clearTimeout(debounceRef.current);
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): timer — `clearTimeout(debounceRef.current);`. The callback runs later on the event loop, not now.

 104 |     };
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): `};` closes return () => { (opened on line 101). Names declared inside that block end here.

 105 |   }, []); // mount once — uses stateRef to avoid stale closures
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): `}, []); // mount once — uses stateRef to avoid stale closures` closes effect in FocusOverlay (opened on line 67). Names declared inside that block end here.

 106 | 
     | Blank line in `src/components/FocusOverlay.jsx` (the full-screen nudge when you leave a focus tab), inside FocusOverlay. The parser skips it. It separates the previous statement from the next so the function is readable.

 107 |   function onImBack() {
     | Defines `onImBack` in the full-screen nudge when you leave a focus tab. Alert → focused. The countdown keeps running; this only dismisses the card.

 108 |     setState(STATES.FOCUSED);
     | In `onImBack` (src/components/FocusOverlay.jsx): statement `setState(STATES.FOCUSED);`. It runs when onImBack runs, in order, before the next line of the same function.

 109 |   }
     | In `onImBack` (src/components/FocusOverlay.jsx): `}` closes onImBack (opened on line 107). Names declared inside that block end here.

 110 | 
     | Blank line in `src/components/FocusOverlay.jsx` (the full-screen nudge when you leave a focus tab), inside FocusOverlay. The parser skips it. It separates the previous statement from the next so the function is readable.

 111 |   function onEndSession() {
     | Defines `onEndSession` in the full-screen nudge when you leave a focus tab. Alert → idle and clears the debounce. It does not by itself stop FocusTimer's interval.

 112 |     clearTimeout(debounceRef.current);
     | In `onEndSession` (src/components/FocusOverlay.jsx): timer — `clearTimeout(debounceRef.current);`. The callback runs later on the event loop, not now.

 113 |     setState(STATES.IDLE);
     | In `onEndSession` (src/components/FocusOverlay.jsx): statement `setState(STATES.IDLE);`. It runs when onEndSession runs, in order, before the next line of the same function.

 114 |     setTaskName("");
     | In `onEndSession` (src/components/FocusOverlay.jsx): statement `setTaskName("");`. It runs when onEndSession runs, in order, before the next line of the same function.

 115 |   }
     | In `onEndSession` (src/components/FocusOverlay.jsx): `}` closes onEndSession (opened on line 111). Names declared inside that block end here.

 116 | 
     | Blank line in `src/components/FocusOverlay.jsx` (the full-screen nudge when you leave a focus tab), inside FocusOverlay. The parser skips it. It separates the previous statement from the next so the function is readable.

 117 |   if (state !== STATES.ALERT) return null;
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): branch `if (state !== STATES.ALERT) return null;`. Only one side runs.

 118 | 
     | Blank line in `src/components/FocusOverlay.jsx` (the full-screen nudge when you leave a focus tab), inside FocusOverlay. The parser skips it. It separates the previous statement from the next so the function is readable.

 119 |   return (
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

 120 |     <div className="focus-overlay">
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="focus-overlay">`

 121 |       <div className="focus-overlay-card">
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="focus-overlay-card">`

 122 |         <div className="focus-overlay-icon">🧘</div>
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="focus-overlay-icon">🧘</div>`

 123 |         <div className="focus-overlay-title">Hey, where'd you go?</div>
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="focus-overlay-title">Hey, where'd you go?</div>`

 124 |         <div className="focus-overlay-text">
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="focus-overlay-text">`

 125 |           {taskName
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): statement `{taskName`. It runs when FocusOverlay runs, in order, before the next line of the same function.

 126 |             ? <>You were working on <strong>"{taskName}"</strong>.<br /></>
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): `? <>You were working on <strong>"{taskName}"</strong>.<br /></>` closes FocusOverlay (opened on line 35). Names declared inside that block end here.

 127 |             : null}
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): `: null}` closes FocusOverlay (opened on line 35). Names declared inside that block end here.

 128 |           Take a slow breath and come back.
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): statement `Take a slow breath and come back.`. It runs when FocusOverlay runs, in order, before the next line of the same function.

 129 |           <br />
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): JSX `<br>`. React will create this node when the parent renders. Source: `<br />`

 130 |           <span style={{ fontSize: 12, opacity: 0.7 }}>Try 30 seconds of belly breathing.</span>
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): Opens it. An inline box. Source: `<span style={{ fontSize: 12, opacity: 0.7 }}>Try 30 seconds of belly breathing.</span>`

 131 |         </div>
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 132 |         <div style={{ display: "flex", gap: 10, justifyContent: "center" }}>
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): Opens it. A box that groups the elements inside it. Source: `<div style={{ display: "flex", gap: 10, justifyContent: "center" }}>`

 133 |           <button className="btn btn-primary" onClick={onImBack}>
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button className="btn btn-primary" onClick={onImBack}>`

 134 |             I'm back ✓
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): statement `I'm back ✓`. It runs when FocusOverlay runs, in order, before the next line of the same function.

 135 |           </button>
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

 136 |           <button className="btn btn-ghost" onClick={onEndSession}>
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button className="btn btn-ghost" onClick={onEndSession}>`

 137 |             End session
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): statement `End session`. It runs when FocusOverlay runs, in order, before the next line of the same function.

 138 |           </button>
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

 139 |         </div>
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 140 |       </div>
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 141 |     </div>
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 142 |   );
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): statement `);`. It runs when FocusOverlay runs, in order, before the next line of the same function.

 143 | }
     | In `FocusOverlay` (src/components/FocusOverlay.jsx): `}` closes FocusOverlay (opened on line 35). Names declared inside that block end here.

