# `src/components/Mindfulness.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | /*import React, { useEffect, useRef, useState } from "react";
     | Comment inside the top of the file. Not executed. Text: /*import React, { useEffect, useRef, useState } from "react";

   2 | import Affirmations from "./Affirmations";
     | Comment inside the top of the file. Not executed. Text: import Affirmations from "./Affirmations";

   3 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   4 | const MODES = {
     | Comment inside the top of the file. Not executed. Text: const MODES = {

   5 |   belly: { label: "Belly breathing", steps: ["Breathe in", "Breathe out"], ms: 4000 },
     | Comment inside the top of the file. Not executed. Text: belly: { label: "Belly breathing", steps: ["Breathe in", "Breathe out"], ms: 4000 },

   6 |   box: { label: "Box breathing", steps: ["Inhale 4", "Hold 4", "Exhale 4", "Hold 4"], ms: 4000 },
     | Comment inside the top of the file. Not executed. Text: box: { label: "Box breathing", steps: ["Inhale 4", "Hold 4", "Exhale 4", "Hold 4"], ms: 4000 },

   7 |   guided: { label: "Guided Meditation (audio)", steps: ["Listen & relax"], ms: 60000 },
     | Comment inside the top of the file. Not executed. Text: guided: { label: "Guided Meditation (audio)", steps: ["Listen & relax"], ms: 60000 },

   8 |   sleep: { label: "Sleep breathing", steps: ["Breathe in 4", "Breathe out 6"], ms: 5000 }
     | Comment inside the top of the file. Not executed. Text: sleep: { label: "Sleep breathing", steps: ["Breathe in 4", "Breathe out 6"], ms: 5000 }

   9 | };
     | Comment inside the top of the file. Not executed. Text: };

  10 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  11 | export default function Mindfulness(){
     | Comment inside Mindfulness. Not executed. Text: export default function Mindfulness(){

  12 |   const [mode,setMode] = useState("belly");
     | Comment inside Mindfulness. Not executed. Text: const [mode,setMode] = useState("belly");

  13 |   const [running,setRunning] = useState(false);
     | Comment inside Mindfulness. Not executed. Text: const [running,setRunning] = useState(false);

  14 |   const [step, setStep] = useState(0);
     | Comment inside Mindfulness. Not executed. Text: const [step, setStep] = useState(0);

  15 |   const timerRef = useRef();
     | Comment inside Mindfulness. Not executed. Text: const timerRef = useRef();

  16 |   const audioRef = useRef();
     | Comment inside Mindfulness. Not executed. Text: const audioRef = useRef();

  17 |   const affirmRef = useRef();
     | Comment inside Mindfulness. Not executed. Text: const affirmRef = useRef();

  18 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

  19 |   useEffect(()=>{
     | Comment inside Mindfulness. Not executed. Text: useEffect(()=>{

  20 |     function onVisibility(){
     | Comment inside onVisibility. Not executed. Text: function onVisibility(){

  21 |       if(document.visibilityState === 'hidden' && running){
     | Comment inside onVisibility. Not executed. Text: if(document.visibilityState === 'hidden' && running){

  22 |         setRunning(false);
     | Comment inside onVisibility. Not executed. Text: setRunning(false);

  23 |         if(affirmRef.current) affirmRef.current.messageForContext('tab-change');
     | Comment inside onVisibility. Not executed. Text: if(affirmRef.current) affirmRef.current.messageForContext('tab-change');

  24 |       }
     | Comment inside onVisibility. Not executed. Text: }

  25 |     }
     | Comment inside onVisibility. Not executed. Text: }

  26 |     document.addEventListener('visibilitychange', onVisibility);
     | Comment inside Mindfulness. Not executed. Text: document.addEventListener('visibilitychange', onVisibility);

  27 |     return ()=> document.removeEventListener('visibilitychange', onVisibility);
     | Comment inside Mindfulness. Not executed. Text: return ()=> document.removeEventListener('visibilitychange', onVisibility);

  28 |   }, [running]);
     | Comment inside Mindfulness. Not executed. Text: }, [running]);

  29 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

  30 |   useEffect(()=>{
     | Comment inside Mindfulness. Not executed. Text: useEffect(()=>{

  31 |     if(!running){ clearInterval(timerRef.current); if(audioRef.current) audioRef.current.pause(); return; }
     | Comment inside Mindfulness. Not executed. Text: if(!running){ clearInterval(timerRef.current); if(audioRef.current) audioRef.current.pause(); return; }

  32 |     const cfg = MODES[mode];
     | Comment inside Mindfulness. Not executed. Text: const cfg = MODES[mode];

  33 |     if(mode === 'guided'){ if(audioRef.current) audioRef.current.play(); }
     | Comment inside Mindfulness. Not executed. Text: if(mode === 'guided'){ if(audioRef.current) audioRef.current.play(); }

  34 |     timerRef.current = setInterval(()=>{
     | Comment inside Mindfulness. Not executed. Text: timerRef.current = setInterval(()=>{

  35 |       setStep(s => {
     | Comment inside Mindfulness. Not executed. Text: setStep(s => {

  36 |         const next = s + 1;
     | Comment inside Mindfulness. Not executed. Text: const next = s + 1;

  37 |         if(next >= cfg.steps.length){
     | Comment inside Mindfulness. Not executed. Text: if(next >= cfg.steps.length){

  38 |           if(mode === 'guided'){ setRunning(false); if(affirmRef.current) affirmRef.current.messageForContext('task-complete'); return 0; }
     | Comment inside Mindfulness. Not executed. Text: if(mode === 'guided'){ setRunning(false); if(affirmRef.current) affirmRef.current.messageForContext('task-complete'); return 0; }

  39 |           return 0;
     | Comment inside Mindfulness. Not executed. Text: return 0;

  40 |         }
     | Comment inside Mindfulness. Not executed. Text: }

  41 |         return next;
     | Comment inside Mindfulness. Not executed. Text: return next;

  42 |       });
     | Comment inside Mindfulness. Not executed. Text: });

  43 |     }, cfg.ms);
     | Comment inside Mindfulness. Not executed. Text: }, cfg.ms);

  44 |     return ()=> clearInterval(timerRef.current);
     | Comment inside Mindfulness. Not executed. Text: return ()=> clearInterval(timerRef.current);

  45 |   }, [running, mode]);
     | Comment inside Mindfulness. Not executed. Text: }, [running, mode]);

  46 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

  47 |   return (
     | Comment inside Mindfulness. Not executed. Text: return (

  48 |     <div className="app">
     | Comment inside Mindfulness. Not executed. Text: <div className="app">

  49 |       <div className="page-header">
     | Comment inside Mindfulness. Not executed. Text: <div className="page-header">

  50 |         <h2>Mindfulness</h2>
     | Comment inside Mindfulness. Not executed. Text: <h2>Mindfulness</h2>

  51 |         <div className="small">Short practices to reset your attention.</div>
     | Comment inside Mindfulness. Not executed. Text: <div className="small">Short practices to reset your attention.</div>

  52 |       </div>
     | Comment inside Mindfulness. Not executed. Text: </div>

  53 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

  54 |       <div className="main-grid">
     | Comment inside Mindfulness. Not executed. Text: <div className="main-grid">

  55 |         <div className="card">
     | Comment inside Mindfulness. Not executed. Text: <div className="card">

  56 |           <label className="small">Mode</label>
     | Comment inside Mindfulness. Not executed. Text: <label className="small">Mode</label>

  57 |           <select className="select" value={mode} onChange={e=>setMode(e.target.value)} style={{marginTop:8}}>
     | Comment inside Mindfulness. Not executed. Text: <select className="select" value={mode} onChange={e=>setMode(e.target.value)} style={{marginTop:8}}>

  58 |             {Object.keys(MODES).map(k => <option key={k} value={k}>{MODES[k].label}</option>)}
     | Comment inside Mindfulness. Not executed. Text: {Object.keys(MODES).map(k => <option key={k} value={k}>{MODES[k].label}</option>)}

  59 |           </select>
     | Comment inside Mindfulness. Not executed. Text: </select>

  60 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

  61 |           <div className="mind-steps" style={{marginTop:18}}>
     | Comment inside Mindfulness. Not executed. Text: <div className="mind-steps" style={{marginTop:18}}>

  62 |             {MODES[mode].steps[step % MODES[mode].steps.length]}
     | Comment inside Mindfulness. Not executed. Text: {MODES[mode].steps[step % MODES[mode].steps.length]}

  63 |           </div>
     | Comment inside Mindfulness. Not executed. Text: </div>

  64 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

  65 |           {mode === 'guided' && <audio ref={audioRef} controls src="/guided-sample.mp3" />}
     | Comment inside Mindfulness. Not executed. Text: {mode === 'guided' && <audio ref={audioRef} controls src="/guided-sample.mp3" />}

  66 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

  67 |           <div style={{marginTop:12}}>
     | Comment inside Mindfulness. Not executed. Text: <div style={{marginTop:12}}>

  68 |             <button className="btn" onClick={()=>setRunning(true)}>Start</button>
     | Comment inside Mindfulness. Not executed. Text: <button className="btn" onClick={()=>setRunning(true)}>Start</button>

  69 |             <button className="btn secondary" onClick={()=>setRunning(false)} style={{marginLeft:8}}>Stop</button>
     | Comment inside Mindfulness. Not executed. Text: <button className="btn secondary" onClick={()=>setRunning(false)} style={{marginLeft:8}}>Stop</button>

  70 |           </div>
     | Comment inside Mindfulness. Not executed. Text: </div>

  71 |         </div>
     | Comment inside Mindfulness. Not executed. Text: </div>

  72 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

  73 |         <aside className="card">
     | Comment inside Mindfulness. Not executed. Text: <aside className="card">

  74 |           <h4>Affirmation</h4>
     | Comment inside Mindfulness. Not executed. Text: <h4>Affirmation</h4>

  75 |           <Affirmations ref={affirmRef} />
     | Comment inside Mindfulness. Not executed. Text: <Affirmations ref={affirmRef} />

  76 |         </aside>
     | Comment inside Mindfulness. Not executed. Text: </aside>

  77 |       </div>
     | Comment inside Mindfulness. Not executed. Text: </div>

  78 |     </div>
     | Comment inside Mindfulness. Not executed. Text: </div>

  79 |   );
     | Comment inside Mindfulness. Not executed. Text: );

  80 | }*/
     | Comment inside Mindfulness. Not executed. Text: }*/

  81 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  82 | /*import React, { useEffect, useRef, useState } from "react";
     | Comment inside the top of the file. Not executed. Text: /*import React, { useEffect, useRef, useState } from "react";

  83 | import Affirmations from "./Affirmations";
     | Comment inside the top of the file. Not executed. Text: import Affirmations from "./Affirmations";

  84 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  85 | const MODES = {
     | Comment inside the top of the file. Not executed. Text: const MODES = {

  86 |   meditation: { 
     | Comment inside the top of the file. Not executed. Text: meditation: {

  87 |     label: "Meditation ", 
     | Comment inside the top of the file. Not executed. Text: label: "Meditation ",

  88 |     audioSrc: "./audio/04_Meditation_for_Working_with_Difficulties.mp3"
     | Comment inside the top of the file. Not executed. Text: audioSrc: "./audio/04_Meditation_for_Working_with_Difficulties.mp3"

  89 |   },
     | Comment inside the top of the file. Not executed. Text: },

  90 |   grounding: { 
     | Comment inside the top of the file. Not executed. Text: grounding: {

  91 |     label: "Grounding", 
     | Comment inside the top of the file. Not executed. Text: label: "Grounding",

  92 |     audioSrc: "./audio/Body-Scan-Meditation.mp3"
     | Comment inside the top of the file. Not executed. Text: audioSrc: "./audio/Body-Scan-Meditation.mp3"

  93 |   },
     | Comment inside the top of the file. Not executed. Text: },

  94 |   guided: { 
     | Comment inside the top of the file. Not executed. Text: guided: {

  95 |     label: "Sleep meditation", 
     | Comment inside the top of the file. Not executed. Text: label: "Sleep meditation",

  96 |     audioSrc: "./audio/Body-Scan-Sleep.mp3"
     | Comment inside the top of the file. Not executed. Text: audioSrc: "./audio/Body-Scan-Sleep.mp3"

  97 |   }
     | Comment inside the top of the file. Not executed. Text: }

  98 |   
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  99 | };
     | Comment inside the top of the file. Not executed. Text: };

 100 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

 101 | export default function Mindfulness(){
     | Comment inside Mindfulness. Not executed. Text: export default function Mindfulness(){

 102 |   const [mode, setMode] = useState("meditation");
     | Comment inside Mindfulness. Not executed. Text: const [mode, setMode] = useState("meditation");

 103 |   const [running, setRunning] = useState(false);
     | Comment inside Mindfulness. Not executed. Text: const [running, setRunning] = useState(false);

 104 |   const [currentTime, setCurrentTime] = useState(0);
     | Comment inside Mindfulness. Not executed. Text: const [currentTime, setCurrentTime] = useState(0);

 105 |   const [duration, setDuration] = useState(0);
     | Comment inside Mindfulness. Not executed. Text: const [duration, setDuration] = useState(0);

 106 |   const audioRef = useRef();
     | Comment inside Mindfulness. Not executed. Text: const audioRef = useRef();

 107 |   const affirmRef = useRef();
     | Comment inside Mindfulness. Not executed. Text: const affirmRef = useRef();

 108 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

 109 |   useEffect(()=>{
     | Comment inside Mindfulness. Not executed. Text: useEffect(()=>{

 110 |     function onVisibility(){
     | Comment inside onVisibility. Not executed. Text: function onVisibility(){

 111 |       if(document.visibilityState === 'hidden' && running){
     | Comment inside onVisibility. Not executed. Text: if(document.visibilityState === 'hidden' && running){

 112 |         setRunning(false);
     | Comment inside onVisibility. Not executed. Text: setRunning(false);

 113 |         if(affirmRef.current) affirmRef.current.messageForContext('tab-change');
     | Comment inside onVisibility. Not executed. Text: if(affirmRef.current) affirmRef.current.messageForContext('tab-change');

 114 |       }
     | Comment inside onVisibility. Not executed. Text: }

 115 |     }
     | Comment inside onVisibility. Not executed. Text: }

 116 |     document.addEventListener('visibilitychange', onVisibility);
     | Comment inside Mindfulness. Not executed. Text: document.addEventListener('visibilitychange', onVisibility);

 117 |     return ()=> document.removeEventListener('visibilitychange', onVisibility);
     | Comment inside Mindfulness. Not executed. Text: return ()=> document.removeEventListener('visibilitychange', onVisibility);

 118 |   }, [running]);
     | Comment inside Mindfulness. Not executed. Text: }, [running]);

 119 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

 120 |   // Load audio duration when mode changes
     | Comment inside Mindfulness. Not executed. It documents the next code: Load audio duration when mode changes

 121 |   useEffect(() => {
     | Comment inside Mindfulness. Not executed. Text: useEffect(() => {

 122 |     const audio = audioRef.current;
     | Comment inside Mindfulness. Not executed. Text: const audio = audioRef.current;

 123 |     if (!audio) return;
     | Comment inside Mindfulness. Not executed. Text: if (!audio) return;

 124 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

 125 |     const handleLoadedMetadata = () => {
     | Comment inside Mindfulness. Not executed. Text: const handleLoadedMetadata = () => {

 126 |       setDuration(audio.duration * 1000); // Convert to ms
     | Comment inside Mindfulness. Not executed. Text: setDuration(audio.duration * 1000); // Convert to ms

 127 |     };
     | Comment inside Mindfulness. Not executed. Text: };

 128 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

 129 |     audio.addEventListener('loadedmetadata', handleLoadedMetadata);
     | Comment inside Mindfulness. Not executed. Text: audio.addEventListener('loadedmetadata', handleLoadedMetadata);

 130 |     
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

 131 |     // Trigger load
     | Comment inside Mindfulness. Not executed. It documents the next code: Trigger load

 132 |     audio.load();
     | Comment inside Mindfulness. Not executed. Text: audio.load();

 133 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

 134 |     return () => {
     | Comment inside Mindfulness. Not executed. Text: return () => {

 135 |       audio.removeEventListener('loadedmetadata', handleLoadedMetadata);
     | Comment inside Mindfulness. Not executed. Text: audio.removeEventListener('loadedmetadata', handleLoadedMetadata);

 136 |     };
     | Comment inside Mindfulness. Not executed. Text: };

 137 |   }, [mode]);
     | Comment inside Mindfulness. Not executed. Text: }, [mode]);

 138 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

 139 |   useEffect(()=>{
     | Comment inside Mindfulness. Not executed. Text: useEffect(()=>{

 140 |     if(!running){ 
     | Comment inside Mindfulness. Not executed. Text: if(!running){

 141 |       if(audioRef.current) {
     | Comment inside Mindfulness. Not executed. Text: if(audioRef.current) {

 142 |         audioRef.current.pause();
     | Comment inside Mindfulness. Not executed. Text: audioRef.current.pause();

 143 |         audioRef.current.currentTime = 0;
     | Comment inside Mindfulness. Not executed. Text: audioRef.current.currentTime = 0;

 144 |       }
     | Comment inside Mindfulness. Not executed. Text: }

 145 |       setCurrentTime(0);
     | Comment inside Mindfulness. Not executed. Text: setCurrentTime(0);

 146 |       return; 
     | Comment inside Mindfulness. Not executed. Text: return;

 147 |     }
     | Comment inside Mindfulness. Not executed. Text: }

 148 |     
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

 149 |     if(audioRef.current) {
     | Comment inside Mindfulness. Not executed. Text: if(audioRef.current) {

 150 |       audioRef.current.play();
     | Comment inside Mindfulness. Not executed. Text: audioRef.current.play();

 151 |       
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

 152 |       const handleAudioEnd = () => {
     | Comment inside Mindfulness. Not executed. Text: const handleAudioEnd = () => {

 153 |         setRunning(false);
     | Comment inside Mindfulness. Not executed. Text: setRunning(false);

 154 |         if(affirmRef.current) affirmRef.current.messageForContext('task-complete');
     | Comment inside Mindfulness. Not executed. Text: if(affirmRef.current) affirmRef.current.messageForContext('task-complete');

 155 |       };
     | Comment inside Mindfulness. Not executed. Text: };

 156 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

 157 |       const handleTimeUpdate = () => {
     | Comment inside Mindfulness. Not executed. Text: const handleTimeUpdate = () => {

 158 |         setCurrentTime(audioRef.current.currentTime * 1000);
     | Comment inside Mindfulness. Not executed. Text: setCurrentTime(audioRef.current.currentTime * 1000);

 159 |       };
     | Comment inside Mindfulness. Not executed. Text: };

 160 |       
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

 161 |       audioRef.current.addEventListener('ended', handleAudioEnd);
     | Comment inside Mindfulness. Not executed. Text: audioRef.current.addEventListener('ended', handleAudioEnd);

 162 |       audioRef.current.addEventListener('timeupdate', handleTimeUpdate);
     | Comment inside Mindfulness. Not executed. Text: audioRef.current.addEventListener('timeupdate', handleTimeUpdate);

 163 |       
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

 164 |       return () => {
     | Comment inside Mindfulness. Not executed. Text: return () => {

 165 |         if(audioRef.current) {
     | Comment inside Mindfulness. Not executed. Text: if(audioRef.current) {

 166 |           audioRef.current.removeEventListener('ended', handleAudioEnd);
     | Comment inside Mindfulness. Not executed. Text: audioRef.current.removeEventListener('ended', handleAudioEnd);

 167 |           audioRef.current.removeEventListener('timeupdate', handleTimeUpdate);
     | Comment inside Mindfulness. Not executed. Text: audioRef.current.removeEventListener('timeupdate', handleTimeUpdate);

 168 |         }
     | Comment inside Mindfulness. Not executed. Text: }

 169 |       };
     | Comment inside Mindfulness. Not executed. Text: };

 170 |     }
     | Comment inside Mindfulness. Not executed. Text: }

 171 |   }, [running, mode]);
     | Comment inside Mindfulness. Not executed. Text: }, [running, mode]);

 172 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

 173 |   // Reset when mode changes
     | Comment inside Mindfulness. Not executed. It documents the next code: Reset when mode changes

 174 |   useEffect(() => {
     | Comment inside Mindfulness. Not executed. Text: useEffect(() => {

 175 |     setRunning(false);
     | Comment inside Mindfulness. Not executed. Text: setRunning(false);

 176 |     setCurrentTime(0);
     | Comment inside Mindfulness. Not executed. Text: setCurrentTime(0);

 177 |   }, [mode]);
     | Comment inside Mindfulness. Not executed. Text: }, [mode]);

 178 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

 179 |   const formatTime = (ms) => {
     | Comment inside Mindfulness. Not executed. Text: const formatTime = (ms) => {

 180 |     const seconds = Math.floor(ms / 1000);
     | Comment inside Mindfulness. Not executed. Text: const seconds = Math.floor(ms / 1000);

 181 |     const mins = Math.floor(seconds / 60);
     | Comment inside Mindfulness. Not executed. Text: const mins = Math.floor(seconds / 60);

 182 |     const secs = seconds % 60;
     | Comment inside Mindfulness. Not executed. Text: const secs = seconds % 60;

 183 |     return `${mins}:${secs.toString().padStart(2, '0')}`;
     | Comment inside Mindfulness. Not executed. Text: return `${mins}:${secs.toString().padStart(2, '0')}`;

 184 |   };
     | Comment inside Mindfulness. Not executed. Text: };

 185 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

 186 |   return (
     | Comment inside Mindfulness. Not executed. Text: return (

 187 |     <div className="app">
     | Comment inside Mindfulness. Not executed. Text: <div className="app">

 188 |       <div className="page-header">
     | Comment inside Mindfulness. Not executed. Text: <div className="page-header">

 189 |         <h2>Mindfulness</h2>
     | Comment inside Mindfulness. Not executed. Text: <h2>Mindfulness</h2>

 190 |         <div className="small">Audio-guided practices to reset your attention.</div>
     | Comment inside Mindfulness. Not executed. Text: <div className="small">Audio-guided practices to reset your attention.</div>

 191 |       </div>
     | Comment inside Mindfulness. Not executed. Text: </div>

 192 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

 193 |       <div className="main-grid">
     | Comment inside Mindfulness. Not executed. Text: <div className="main-grid">

 194 |         <div className="card">
     | Comment inside Mindfulness. Not executed. Text: <div className="card">

 195 |           <label className="small">Mode</label>
     | Comment inside Mindfulness. Not executed. Text: <label className="small">Mode</label>

 196 |           <select 
     | Comment inside Mindfulness. Not executed. Text: <select

 197 |             className="select" 
     | Comment inside Mindfulness. Not executed. Text: className="select"

 198 |             value={mode} 
     | Comment inside Mindfulness. Not executed. Text: value={mode}

 199 |             onChange={e=>setMode(e.target.value)} 
     | Comment inside Mindfulness. Not executed. Text: onChange={e=>setMode(e.target.value)}

 200 |             style={{marginTop:8}}
     | Comment inside Mindfulness. Not executed. Text: style={{marginTop:8}}

 201 |             disabled={running}
     | Comment inside Mindfulness. Not executed. Text: disabled={running}

 202 |           >
     | Comment inside Mindfulness. Not executed. Text: >

 203 |             {Object.keys(MODES).map(k => <option key={k} value={k}>{MODES[k].label}</option>)}
     | Comment inside Mindfulness. Not executed. Text: {Object.keys(MODES).map(k => <option key={k} value={k}>{MODES[k].label}</option>)}

 204 |           </select>
     | Comment inside Mindfulness. Not executed. Text: </select>

 205 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

 206 |           <div style={{
     | Comment inside Mindfulness. Not executed. Text: <div style={{

 207 |             marginTop: 24,
     | Comment inside Mindfulness. Not executed. Text: marginTop: 24,

 208 |             padding: '3rem 1rem',
     | Comment inside Mindfulness. Not executed. Text: padding: '3rem 1rem',

 209 |             textAlign: 'center',
     | Comment inside Mindfulness. Not executed. Text: textAlign: 'center',

 210 |             background: running ? 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)' : '#f7f7f7',
     | Comment inside Mindfulness. Not executed. Text: background: running ? 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)' : '#f7f7f7',

 211 |             borderRadius: '12px',
     | Comment inside Mindfulness. Not executed. Text: borderRadius: '12px',

 212 |             transition: 'all 0.3s ease',
     | Comment inside Mindfulness. Not executed. Text: transition: 'all 0.3s ease',

 213 |             color: running ? 'white' : '#666'
     | Comment inside Mindfulness. Not executed. Text: color: running ? 'white' : '#666'

 214 |           }}>
     | Comment inside Mindfulness. Not executed. Text: }}>

 215 |             <div style={{fontSize: '1.2rem', marginBottom: '0.5rem', opacity: 0.9}}>
     | Comment inside Mindfulness. Not executed. Text: <div style={{fontSize: '1.2rem', marginBottom: '0.5rem', opacity: 0.9}}>

 216 |               {running ? 'Session in progress' : 'Ready to begin'}
     | Comment inside Mindfulness. Not executed. Text: {running ? 'Session in progress' : 'Ready to begin'}

 217 |             </div>
     | Comment inside Mindfulness. Not executed. Text: </div>

 218 |             <div style={{fontSize: '3rem', fontWeight: 'bold'}}>
     | Comment inside Mindfulness. Not executed. Text: <div style={{fontSize: '3rem', fontWeight: 'bold'}}>

 219 |               {formatTime(currentTime)}
     | Comment inside Mindfulness. Not executed. Text: {formatTime(currentTime)}

 220 |             </div>
     | Comment inside Mindfulness. Not executed. Text: </div>

 221 |             {duration > 0 && (
     | Comment inside Mindfulness. Not executed. Text: {duration > 0 && (

 222 |               <div style={{fontSize: '0.9rem', marginTop: '0.5rem', opacity: 0.8}}>
     | Comment inside Mindfulness. Not executed. Text: <div style={{fontSize: '0.9rem', marginTop: '0.5rem', opacity: 0.8}}>

 223 |                 of {formatTime(duration)}
     | Comment inside Mindfulness. Not executed. Text: of {formatTime(duration)}

 224 |               </div>
     | Comment inside Mindfulness. Not executed. Text: </div>

 225 |             )}
     | Comment inside Mindfulness. Not executed. Text: )}

 226 |           </div>
     | Comment inside Mindfulness. Not executed. Text: </div>

 227 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

 228 |           <audio 
     | Comment inside Mindfulness. Not executed. Text: <audio

 229 |             ref={audioRef} 
     | Comment inside Mindfulness. Not executed. Text: ref={audioRef}

 230 |             src={MODES[mode].audioSrc}
     | Comment inside Mindfulness. Not executed. Text: src={MODES[mode].audioSrc}

 231 |             preload="metadata"
     | Comment inside Mindfulness. Not executed. Text: preload="metadata"

 232 |             style={{display: 'none'}}
     | Comment inside Mindfulness. Not executed. Text: style={{display: 'none'}}

 233 |           />
     | Comment inside Mindfulness. Not executed. Text: />

 234 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

 235 |           <div style={{marginTop:16}}>
     | Comment inside Mindfulness. Not executed. Text: <div style={{marginTop:16}}>

 236 |             <button className="btn" onClick={()=>setRunning(true)} disabled={running}>
     | Comment inside Mindfulness. Not executed. Text: <button className="btn" onClick={()=>setRunning(true)} disabled={running}>

 237 |               Start
     | Comment inside Mindfulness. Not executed. Text: Start

 238 |             </button>
     | Comment inside Mindfulness. Not executed. Text: </button>

 239 |             <button className="btn secondary" onClick={()=>setRunning(false)} style={{marginLeft:8}} disabled={!running}>
     | Comment inside Mindfulness. Not executed. Text: <button className="btn secondary" onClick={()=>setRunning(false)} style={{marginLeft:8}} disabled={!running}>

 240 |               Stop
     | Comment inside Mindfulness. Not executed. Text: Stop

 241 |             </button>
     | Comment inside Mindfulness. Not executed. Text: </button>

 242 |           </div>
     | Comment inside Mindfulness. Not executed. Text: </div>

 243 |         </div>
     | Comment inside Mindfulness. Not executed. Text: </div>

 244 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

 245 |         <aside className="card">
     | Comment inside Mindfulness. Not executed. Text: <aside className="card">

 246 |           <h4>Affirmation</h4>
     | Comment inside Mindfulness. Not executed. Text: <h4>Affirmation</h4>

 247 |           <Affirmations ref={affirmRef} />
     | Comment inside Mindfulness. Not executed. Text: <Affirmations ref={affirmRef} />

 248 |         </aside>
     | Comment inside Mindfulness. Not executed. Text: </aside>

 249 |       </div>
     | Comment inside Mindfulness. Not executed. Text: </div>

 250 |     </div>
     | Comment inside Mindfulness. Not executed. Text: </div>

 251 |   );
     | Comment inside Mindfulness. Not executed. Text: );

 252 | }*/
     | Comment inside Mindfulness. Not executed. Text: }*/

 253 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

 254 | import React, { useEffect, useRef, useState } from "react";
     | Import for the audio breathing page; the top of the file is old commented code: `import React, { useEffect, useRef, useState } from "react";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

 255 | import Affirmations from "./Affirmations";
     | Import for the audio breathing page; the top of the file is old commented code: `import Affirmations from "./Affirmations";`. The names become local bindings. A side-effect import (one with no names, such as a CSS file) runs that module for its effect.

 256 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

 257 | const MODES = {
     | In `the top of the file` (src/components/Mindfulness.jsx): `MODES`: In FocusTimer, Pomodoro is 25/5 and Deep Work is 50/10. In Mindfulness the live MODES (the third copy, after line 252) are three mp3s. The earlier MODES are inside comments and never run. The code is `const MODES = {`.

 258 |   meditation: {
     | In `the top of the file` (src/components/Mindfulness.jsx): statement `meditation: {`. It runs when the top of the file runs, in order, before the next line of the same function.

 259 |     label: "Meditation",
     | In `the top of the file` (src/components/Mindfulness.jsx): statement `label: "Meditation",`. It runs when the top of the file runs, in order, before the next line of the same function.

 260 |     audioSrc: "/audio/04_Meditation_for_Working_with_Difficulties.mp3"
     | In `the top of the file` (src/components/Mindfulness.jsx): statement `audioSrc: "/audio/04_Meditation_for_Working_with_Difficulties.mp3"`. It runs when the top of the file runs, in order, before the next line of the same function.

 261 |   },
     | In `the top of the file` (src/components/Mindfulness.jsx): `},` closes meditation: { (opened on line 258). Names declared inside that block end here.

 262 |   grounding: {
     | In `the top of the file` (src/components/Mindfulness.jsx): statement `grounding: {`. It runs when the top of the file runs, in order, before the next line of the same function.

 263 |     label: "Grounding",
     | In `the top of the file` (src/components/Mindfulness.jsx): statement `label: "Grounding",`. It runs when the top of the file runs, in order, before the next line of the same function.

 264 |     audioSrc: "/audio/Body-Scan-Meditation.mp3"
     | In `the top of the file` (src/components/Mindfulness.jsx): statement `audioSrc: "/audio/Body-Scan-Meditation.mp3"`. It runs when the top of the file runs, in order, before the next line of the same function.

 265 |   },
     | In `the top of the file` (src/components/Mindfulness.jsx): `},` closes grounding: { (opened on line 262). Names declared inside that block end here.

 266 |   guided: {
     | In `the top of the file` (src/components/Mindfulness.jsx): statement `guided: {`. It runs when the top of the file runs, in order, before the next line of the same function.

 267 |     label: "Sleep meditation",
     | In `the top of the file` (src/components/Mindfulness.jsx): statement `label: "Sleep meditation",`. It runs when the top of the file runs, in order, before the next line of the same function.

 268 |     audioSrc: "/audio/Body-Scan-for-Sleep.mp3"
     | In `the top of the file` (src/components/Mindfulness.jsx): statement `audioSrc: "/audio/Body-Scan-for-Sleep.mp3"`. It runs when the top of the file runs, in order, before the next line of the same function.

 269 |   }
     | In `the top of the file` (src/components/Mindfulness.jsx): `}` closes guided: { (opened on line 266). Names declared inside that block end here.

 270 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

 271 | };
     | In `the top of the file` (src/components/Mindfulness.jsx): `};` closes const MODES = { (opened on line 257). Names declared inside that block end here.

 272 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

 273 | export default function Mindfulness(){
     | Defines `Mindfulness` in the audio breathing page; the top of the file is old commented code. The live function starts at the third Mindfulness in the file. The first two are inside a block comment. It plays one of three mp3s and stops if the tab is hidden.

 274 |   const [mode, setMode] = useState("meditation");
     | In `Mindfulness` (src/components/Mindfulness.jsx): React state `mode, setMode`. The value survives re-renders. Calling the setter re-renders this component. `const [mode, setMode] = useState("meditation");`

 275 |   const [running, setRunning] = useState(false);
     | In `Mindfulness` (src/components/Mindfulness.jsx): React state `running, setRunning`. The value survives re-renders. Calling the setter re-renders this component. `const [running, setRunning] = useState(false);`

 276 |   const [currentTime, setCurrentTime] = useState(0);
     | In `Mindfulness` (src/components/Mindfulness.jsx): React state `currentTime, setCurrentTime`. The value survives re-renders. Calling the setter re-renders this component. `const [currentTime, setCurrentTime] = useState(0);`

 277 |   const [duration, setDuration] = useState(0);
     | In `Mindfulness` (src/components/Mindfulness.jsx): React state `duration, setDuration`. The value survives re-renders. Calling the setter re-renders this component. `const [duration, setDuration] = useState(0);`

 278 |   const [audioError, setAudioError] = useState(null);
     | In `Mindfulness` (src/components/Mindfulness.jsx): React state `audioError, setAudioError`. The value survives re-renders. Calling the setter re-renders this component. `const [audioError, setAudioError] = useState(null);`

 279 |   const audioRef = useRef();
     | In `Mindfulness` (src/components/Mindfulness.jsx): A ref `audioRef`. `.current` survives re-renders and writing it does not re-render. `const audioRef = useRef();`

 280 |   const affirmRef = useRef();
     | In `Mindfulness` (src/components/Mindfulness.jsx): A ref `affirmRef`. `.current` survives re-renders and writing it does not re-render. `const affirmRef = useRef();`

 281 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

 282 |   useEffect(()=>{
     | In `Mindfulness` (src/components/Mindfulness.jsx): opens or continues an effect — `useEffect(()=>{`. The effect body runs after paint, and its cleanup runs before the next effect and on unmount.

 283 |     function onVisibility(){
     | In `onVisibility` (src/components/Mindfulness.jsx): statement `function onVisibility(){`. It runs when onVisibility runs, in order, before the next line of the same function.

 284 |       if(document.visibilityState === 'hidden' && running){
     | In `onVisibility` (src/components/Mindfulness.jsx): branch `if(document.visibilityState === 'hidden' && running){`. Only one side runs.

 285 |         setRunning(false);
     | In `onVisibility` (src/components/Mindfulness.jsx): statement `setRunning(false);`. It runs when onVisibility runs, in order, before the next line of the same function.

 286 |         if(affirmRef.current) affirmRef.current.messageForContext('tab-change');
     | In `onVisibility` (src/components/Mindfulness.jsx): branch `if(affirmRef.current) affirmRef.current.messageForContext('tab-change');`. Only one side runs.

 287 |       }
     | In `onVisibility` (src/components/Mindfulness.jsx): `}` closes if(document.visibilityState === 'hidden' (opened on line 284). Names declared inside that block end here.

 288 |     }
     | In `onVisibility` (src/components/Mindfulness.jsx): `}` closes onVisibility (opened on line 283). Names declared inside that block end here.

 289 |     document.addEventListener('visibilitychange', onVisibility);
     | In `Mindfulness` (src/components/Mindfulness.jsx): The browser fires this when the tab is hidden or shown. FocusOverlay uses it for the 800ms nudge. Mindfulness uses it to stop audio.

 290 |     return ()=> document.removeEventListener('visibilitychange', onVisibility);
     | In `Mindfulness` (src/components/Mindfulness.jsx): return `return ()=> document.removeEventListener('visibilitychange', onVisibility);`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

 291 |   }, [running]);
     | In `Mindfulness` (src/components/Mindfulness.jsx): `}, [running]);` closes effect in Mindfulness (opened on line 282). Names declared inside that block end here.

 292 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

 293 |   // Load audio duration when mode changes
     | Comment inside Mindfulness. Not executed. It documents the next code: Load audio duration when mode changes

 294 |   useEffect(() => {
     | In `Mindfulness` (src/components/Mindfulness.jsx): opens or continues an effect — `useEffect(() => {`. The effect body runs after paint, and its cleanup runs before the next effect and on unmount.

 295 |     const audio = audioRef.current;
     | In `Mindfulness` (src/components/Mindfulness.jsx): `audio` is assigned `audioRef.current;`. Later lines in this function read that name.

 296 |     if (!audio) return;
     | In `Mindfulness` (src/components/Mindfulness.jsx): branch `if (!audio) return;`. Only one side runs.

 297 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

 298 |     const handleLoadedMetadata = () => {
     | In `Mindfulness` (src/components/Mindfulness.jsx): `handleLoadedMetadata` is assigned `() => {`. Later lines in this function read that name.

 299 |       console.log('Audio loaded successfully, duration:', audio.duration);
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `console.log('Audio loaded successfully, duration:', audio.duration);`. It runs when Mindfulness runs, in order, before the next line of the same function.

 300 |       setDuration(audio.duration * 1000);
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `setDuration(audio.duration * 1000);`. It runs when Mindfulness runs, in order, before the next line of the same function.

 301 |       setAudioError(null);
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `setAudioError(null);`. It runs when Mindfulness runs, in order, before the next line of the same function.

 302 |     };
     | In `Mindfulness` (src/components/Mindfulness.jsx): `};` closes const handleLoadedMetadata = () => { (opened on line 298). Names declared inside that block end here.

 303 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

 304 |     const handleError = (e) => {
     | In `Mindfulness` (src/components/Mindfulness.jsx): `handleError` is assigned `(e) => {`. Later lines in this function read that name.

 305 |       console.error('Audio load error:', e);
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `console.error('Audio load error:', e);`. It runs when Mindfulness runs, in order, before the next line of the same function.

 306 |       console.error('Audio source:', audio.src);
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `console.error('Audio source:', audio.src);`. It runs when Mindfulness runs, in order, before the next line of the same function.

 307 |       console.error('Current URL:', window.location.href);
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `console.error('Current URL:', window.location.href);`. It runs when Mindfulness runs, in order, before the next line of the same function.

 308 |       setAudioError(`Cannot load audio file. Check if file exists at: ${audio.src}`);
     | In `Mindfulness` (src/components/Mindfulness.jsx): `setAudioError(`Cannot load audio file. Check if file exists at: ${audio.src}`);` closes const handleError = (e) => { (opened on line 304). Names declared inside that block end here.

 309 |       setRunning(false);
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `setRunning(false);`. It runs when Mindfulness runs, in order, before the next line of the same function.

 310 |     };
     | In `Mindfulness` (src/components/Mindfulness.jsx): `};` closes const handleError = (e) => { (opened on line 304). Names declared inside that block end here.

 311 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

 312 |     const handleCanPlay = () => {
     | In `Mindfulness` (src/components/Mindfulness.jsx): `handleCanPlay` is assigned `() => {`. Later lines in this function read that name.

 313 |       console.log('Audio is ready to play');
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `console.log('Audio is ready to play');`. It runs when Mindfulness runs, in order, before the next line of the same function.

 314 |     };
     | In `Mindfulness` (src/components/Mindfulness.jsx): `};` closes const handleCanPlay = () => { (opened on line 312). Names declared inside that block end here.

 315 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

 316 |     audio.addEventListener('loadedmetadata', handleLoadedMetadata);
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `audio.addEventListener('loadedmetadata', handleLoadedMetadata);`. It runs when Mindfulness runs, in order, before the next line of the same function.

 317 |     audio.addEventListener('error', handleError);
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `audio.addEventListener('error', handleError);`. It runs when Mindfulness runs, in order, before the next line of the same function.

 318 |     audio.addEventListener('canplay', handleCanPlay);
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `audio.addEventListener('canplay', handleCanPlay);`. It runs when Mindfulness runs, in order, before the next line of the same function.

 319 |     
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

 320 |     // Reset and load
     | Comment inside Mindfulness. Not executed. It documents the next code: Reset and load

 321 |     audio.load();
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `audio.load();`. It runs when Mindfulness runs, in order, before the next line of the same function.

 322 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

 323 |     return () => {
     | In `Mindfulness` (src/components/Mindfulness.jsx): return `return () => {`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

 324 |       audio.removeEventListener('loadedmetadata', handleLoadedMetadata);
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `audio.removeEventListener('loadedmetadata', handleLoadedMetadata);`. It runs when Mindfulness runs, in order, before the next line of the same function.

 325 |       audio.removeEventListener('error', handleError);
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `audio.removeEventListener('error', handleError);`. It runs when Mindfulness runs, in order, before the next line of the same function.

 326 |       audio.removeEventListener('canplay', handleCanPlay);
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `audio.removeEventListener('canplay', handleCanPlay);`. It runs when Mindfulness runs, in order, before the next line of the same function.

 327 |     };
     | In `Mindfulness` (src/components/Mindfulness.jsx): `};` closes return () => { (opened on line 323). Names declared inside that block end here.

 328 |   }, [mode]);
     | In `Mindfulness` (src/components/Mindfulness.jsx): `}, [mode]);` closes effect in Mindfulness (opened on line 294). Names declared inside that block end here.

 329 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

 330 |   useEffect(()=>{
     | In `Mindfulness` (src/components/Mindfulness.jsx): opens or continues an effect — `useEffect(()=>{`. The effect body runs after paint, and its cleanup runs before the next effect and on unmount.

 331 |     if(!running){ 
     | In `Mindfulness` (src/components/Mindfulness.jsx): branch `if(!running){`. Only one side runs.

 332 |       if(audioRef.current) {
     | In `Mindfulness` (src/components/Mindfulness.jsx): branch `if(audioRef.current) {`. Only one side runs.

 333 |         audioRef.current.pause();
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `audioRef.current.pause();`. It runs when Mindfulness runs, in order, before the next line of the same function.

 334 |         audioRef.current.currentTime = 0;
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `audioRef.current.currentTime = 0;`. It runs when Mindfulness runs, in order, before the next line of the same function.

 335 |       }
     | In `Mindfulness` (src/components/Mindfulness.jsx): `}` closes if(audioRef.current) { (opened on line 332). Names declared inside that block end here.

 336 |       setCurrentTime(0);
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `setCurrentTime(0);`. It runs when Mindfulness runs, in order, before the next line of the same function.

 337 |       return; 
     | In `Mindfulness` (src/components/Mindfulness.jsx): return `return;`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

 338 |     }
     | In `Mindfulness` (src/components/Mindfulness.jsx): `}` closes if(!running){ (opened on line 331). Names declared inside that block end here.

 339 |     
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

 340 |     const audio = audioRef.current;
     | In `Mindfulness` (src/components/Mindfulness.jsx): `audio` is assigned `audioRef.current;`. Later lines in this function read that name.

 341 |     if(audio) {
     | In `Mindfulness` (src/components/Mindfulness.jsx): branch `if(audio) {`. Only one side runs.

 342 |       const playPromise = audio.play();
     | In `Mindfulness` (src/components/Mindfulness.jsx): `playPromise` is assigned `audio.play();`. Later lines in this function read that name.

 343 |       
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

 344 |       if (playPromise !== undefined) {
     | In `Mindfulness` (src/components/Mindfulness.jsx): branch `if (playPromise !== undefined) {`. Only one side runs.

 345 |         playPromise
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `playPromise`. It runs when Mindfulness runs, in order, before the next line of the same function.

 346 |           .then(() => {
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `.then(() => {`. It runs when Mindfulness runs, in order, before the next line of the same function.

 347 |             console.log('Audio playback started successfully');
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `console.log('Audio playback started successfully');`. It runs when Mindfulness runs, in order, before the next line of the same function.

 348 |           })
     | In `Mindfulness` (src/components/Mindfulness.jsx): `})` closes .then(() => { (opened on line 346). Names declared inside that block end here.

 349 |           .catch(error => {
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `.catch(error => {`. It runs when Mindfulness runs, in order, before the next line of the same function.

 350 |             console.error('Playback error:', error);
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `console.error('Playback error:', error);`. It runs when Mindfulness runs, in order, before the next line of the same function.

 351 |             setAudioError('Playback failed: ' + error.message);
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `setAudioError('Playback failed: ' + error.message);`. It runs when Mindfulness runs, in order, before the next line of the same function.

 352 |             setRunning(false);
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `setRunning(false);`. It runs when Mindfulness runs, in order, before the next line of the same function.

 353 |           });
     | In `Mindfulness` (src/components/Mindfulness.jsx): `});` closes .catch(error => { (opened on line 349). Names declared inside that block end here.

 354 |       }
     | In `Mindfulness` (src/components/Mindfulness.jsx): `}` closes if (playPromise !== undefined) { (opened on line 344). Names declared inside that block end here.

 355 |       
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

 356 |       const handleAudioEnd = () => {
     | In `Mindfulness` (src/components/Mindfulness.jsx): `handleAudioEnd` is assigned `() => {`. Later lines in this function read that name.

 357 |         console.log('Audio ended');
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `console.log('Audio ended');`. It runs when Mindfulness runs, in order, before the next line of the same function.

 358 |         setRunning(false);
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `setRunning(false);`. It runs when Mindfulness runs, in order, before the next line of the same function.

 359 |         if(affirmRef.current) affirmRef.current.messageForContext('task-complete');
     | In `Mindfulness` (src/components/Mindfulness.jsx): branch `if(affirmRef.current) affirmRef.current.messageForContext('task-complete');`. Only one side runs.

 360 |       };
     | In `Mindfulness` (src/components/Mindfulness.jsx): `};` closes const handleAudioEnd = () => { (opened on line 356). Names declared inside that block end here.

 361 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

 362 |       const handleTimeUpdate = () => {
     | In `Mindfulness` (src/components/Mindfulness.jsx): `handleTimeUpdate` is assigned `() => {`. Later lines in this function read that name.

 363 |         setCurrentTime(audio.currentTime * 1000);
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `setCurrentTime(audio.currentTime * 1000);`. It runs when Mindfulness runs, in order, before the next line of the same function.

 364 |       };
     | In `Mindfulness` (src/components/Mindfulness.jsx): `};` closes const handleTimeUpdate = () => { (opened on line 362). Names declared inside that block end here.

 365 |       
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

 366 |       audio.addEventListener('ended', handleAudioEnd);
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `audio.addEventListener('ended', handleAudioEnd);`. It runs when Mindfulness runs, in order, before the next line of the same function.

 367 |       audio.addEventListener('timeupdate', handleTimeUpdate);
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `audio.addEventListener('timeupdate', handleTimeUpdate);`. It runs when Mindfulness runs, in order, before the next line of the same function.

 368 |       
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

 369 |       return () => {
     | In `Mindfulness` (src/components/Mindfulness.jsx): return `return () => {`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

 370 |         if(audio) {
     | In `Mindfulness` (src/components/Mindfulness.jsx): branch `if(audio) {`. Only one side runs.

 371 |           audio.removeEventListener('ended', handleAudioEnd);
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `audio.removeEventListener('ended', handleAudioEnd);`. It runs when Mindfulness runs, in order, before the next line of the same function.

 372 |           audio.removeEventListener('timeupdate', handleTimeUpdate);
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `audio.removeEventListener('timeupdate', handleTimeUpdate);`. It runs when Mindfulness runs, in order, before the next line of the same function.

 373 |         }
     | In `Mindfulness` (src/components/Mindfulness.jsx): `}` closes if(audio) { (opened on line 370). Names declared inside that block end here.

 374 |       };
     | In `Mindfulness` (src/components/Mindfulness.jsx): `};` closes return () => { (opened on line 369). Names declared inside that block end here.

 375 |     }
     | In `Mindfulness` (src/components/Mindfulness.jsx): `}` closes if(audio) { (opened on line 341). Names declared inside that block end here.

 376 |   }, [running, mode]);
     | In `Mindfulness` (src/components/Mindfulness.jsx): `}, [running, mode]);` closes effect in Mindfulness (opened on line 330). Names declared inside that block end here.

 377 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

 378 |   // Reset when mode changes
     | Comment inside Mindfulness. Not executed. It documents the next code: Reset when mode changes

 379 |   useEffect(() => {
     | In `Mindfulness` (src/components/Mindfulness.jsx): opens or continues an effect — `useEffect(() => {`. The effect body runs after paint, and its cleanup runs before the next effect and on unmount.

 380 |     setRunning(false);
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `setRunning(false);`. It runs when Mindfulness runs, in order, before the next line of the same function.

 381 |     setCurrentTime(0);
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `setCurrentTime(0);`. It runs when Mindfulness runs, in order, before the next line of the same function.

 382 |     setAudioError(null);
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `setAudioError(null);`. It runs when Mindfulness runs, in order, before the next line of the same function.

 383 |   }, [mode]);
     | In `Mindfulness` (src/components/Mindfulness.jsx): `}, [mode]);` closes effect in Mindfulness (opened on line 379). Names declared inside that block end here.

 384 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

 385 |   const formatTime = (ms) => {
     | In `Mindfulness` (src/components/Mindfulness.jsx): `formatTime` is assigned `(ms) => {`. Later lines in this function read that name.

 386 |     const seconds = Math.floor(ms / 1000);
     | In `Mindfulness` (src/components/Mindfulness.jsx): `seconds` is assigned `Math.floor(ms / 1000);`. Later lines in this function read that name.

 387 |     const mins = Math.floor(seconds / 60);
     | In `Mindfulness` (src/components/Mindfulness.jsx): `mins` is assigned `Math.floor(seconds / 60);`. Later lines in this function read that name.

 388 |     const secs = seconds % 60;
     | In `Mindfulness` (src/components/Mindfulness.jsx): `secs` is assigned `seconds % 60;`. Later lines in this function read that name.

 389 |     return `${mins}:${secs.toString().padStart(2, '0')}`;
     | In `Mindfulness` (src/components/Mindfulness.jsx): return `return `${mins}:${secs.toString().padStart(2, '0')}`;`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

 390 |   };
     | In `Mindfulness` (src/components/Mindfulness.jsx): `};` closes const formatTime = (ms) => { (opened on line 385). Names declared inside that block end here.

 391 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

 392 |   const progressPct = duration > 0 ? (currentTime / duration) * 100 : 0;
     | In `Mindfulness` (src/components/Mindfulness.jsx): `progressPct` is assigned `duration > 0 ? (currentTime / duration) * 100 : 0;`. Later lines in this function read that name.

 393 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

 394 |   return (
     | In `Mindfulness` (src/components/Mindfulness.jsx): return `return (`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

 395 |     <div>
     | In `Mindfulness` (src/components/Mindfulness.jsx): Opens it. A box that groups the elements inside it. Source: `<div>`

 396 |       <h1 className="page-title">Mindfulness</h1>
     | In `Mindfulness` (src/components/Mindfulness.jsx): Opens it. The page title. Source: `<h1 className="page-title">Mindfulness</h1>`

 397 |       <p className="page-subtitle">Audio-guided practices to reset your attention</p>
     | In `Mindfulness` (src/components/Mindfulness.jsx): Opens it. A paragraph. Source: `<p className="page-subtitle">Audio-guided practices to reset your attention</p>`

 398 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

 399 |       <div className="grid-main">
     | In `Mindfulness` (src/components/Mindfulness.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="grid-main">`

 400 |         <div className="card">
     | In `Mindfulness` (src/components/Mindfulness.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="card">`

 401 |           <div className="text-xs text-muted mb-1">Session type</div>
     | In `Mindfulness` (src/components/Mindfulness.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="text-xs text-muted mb-1">Session type</div>`

 402 |           <select
     | In `Mindfulness` (src/components/Mindfulness.jsx): Opens it. A dropdown. onChange writes the chosen value into state. Source: `<select`

 403 |             className="select mb-4"
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `className="select mb-4"`. It runs when Mindfulness runs, in order, before the next line of the same function.

 404 |             value={mode}
     | In `Mindfulness` (src/components/Mindfulness.jsx): `value={mode}` closes Mindfulness (opened on line 273). Names declared inside that block end here.

 405 |             onChange={(e) => setMode(e.target.value)}
     | In `Mindfulness` (src/components/Mindfulness.jsx): event prop `onChange={(e) => setMode(e.target.value)}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 406 |             disabled={running}
     | In `Mindfulness` (src/components/Mindfulness.jsx): `disabled={running}` closes Mindfulness (opened on line 273). Names declared inside that block end here.

 407 |           >
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `>`. It runs when Mindfulness runs, in order, before the next line of the same function.

 408 |             {Object.keys(MODES).map((k) => (
     | In `Mindfulness` (src/components/Mindfulness.jsx): iteration `{Object.keys(MODES).map((k) => (`.

 409 |               <option key={k} value={k}>{MODES[k].label}</option>
     | In `Mindfulness` (src/components/Mindfulness.jsx): JSX `<option>`. React will create this node when the parent renders.. value is controlled by React state, so the DOM shows that state Source: `<option key={k} value={k}>{MODES[k].label}</option>`

 410 |             ))}
     | In `Mindfulness` (src/components/Mindfulness.jsx): `))}` closes Mindfulness (opened on line 273). Names declared inside that block end here.

 411 |           </select>
     | In `Mindfulness` (src/components/Mindfulness.jsx): Closes it. A dropdown. onChange writes the chosen value into state. Source: `</select>`

 412 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

 413 |           {audioError && (
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `{audioError && (`. It runs when Mindfulness runs, in order, before the next line of the same function.

 414 |             <div
     | In `Mindfulness` (src/components/Mindfulness.jsx): Opens it. A box that groups the elements inside it. Source: `<div`

 415 |               style={{
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `style={{`. It runs when Mindfulness runs, in order, before the next line of the same function.

 416 |                 padding: "10px 14px",
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `padding: "10px 14px",`. It runs when Mindfulness runs, in order, before the next line of the same function.

 417 |                 background: "var(--red-dim)",
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `background: "var(--red-dim)",`. It runs when Mindfulness runs, in order, before the next line of the same function.

 418 |                 color: "var(--red)",
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `color: "var(--red)",`. It runs when Mindfulness runs, in order, before the next line of the same function.

 419 |                 borderRadius: "var(--radius-sm)",
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `borderRadius: "var(--radius-sm)",`. It runs when Mindfulness runs, in order, before the next line of the same function.

 420 |                 fontSize: 13,
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `fontSize: 13,`. It runs when Mindfulness runs, in order, before the next line of the same function.

 421 |                 marginBottom: 16,
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `marginBottom: 16,`. It runs when Mindfulness runs, in order, before the next line of the same function.

 422 |               }}
     | In `Mindfulness` (src/components/Mindfulness.jsx): `}}` closes style={{ (opened on line 415). Names declared inside that block end here.

 423 |             >
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `>`. It runs when Mindfulness runs, in order, before the next line of the same function.

 424 |               ⚠️ {audioError}
     | In `Mindfulness` (src/components/Mindfulness.jsx): `⚠️ {audioError}` closes Mindfulness (opened on line 273). Names declared inside that block end here.

 425 |             </div>
     | In `Mindfulness` (src/components/Mindfulness.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 426 |           )}
     | In `Mindfulness` (src/components/Mindfulness.jsx): `)}` closes Mindfulness (opened on line 273). Names declared inside that block end here.

 427 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

 428 |           <div className={`audio-player ${running ? "playing" : ""}`}>
     | In `Mindfulness` (src/components/Mindfulness.jsx): Opens it. A box that groups the elements inside it. Source: `<div className={`audio-player ${running ? "playing" : ""}`}>`

 429 |             <div className="audio-state-label">
     | In `Mindfulness` (src/components/Mindfulness.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="audio-state-label">`

 430 |               {running ? "Session in progress" : "Ready to begin"}
     | In `Mindfulness` (src/components/Mindfulness.jsx): `{running ? "Session in progress" : "Ready to begin"}` closes Mindfulness (opened on line 273). Names declared inside that block end here.

 431 |             </div>
     | In `Mindfulness` (src/components/Mindfulness.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 432 |             <div className="audio-time">{formatTime(currentTime)}</div>
     | In `Mindfulness` (src/components/Mindfulness.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="audio-time">{formatTime(currentTime)}</div>`

 433 |             {duration > 0 && (
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `{duration > 0 && (`. It runs when Mindfulness runs, in order, before the next line of the same function.

 434 |               <div className="audio-duration">of {formatTime(duration)}</div>
     | In `Mindfulness` (src/components/Mindfulness.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="audio-duration">of {formatTime(duration)}</div>`

 435 |             )}
     | In `Mindfulness` (src/components/Mindfulness.jsx): `)}` closes Mindfulness (opened on line 273). Names declared inside that block end here.

 436 |             <div className="audio-progress">
     | In `Mindfulness` (src/components/Mindfulness.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="audio-progress">`

 437 |               <div className="audio-progress-fill" style={{ width: `${progressPct}%` }} />
     | In `Mindfulness` (src/components/Mindfulness.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="audio-progress-fill" style={{ width: `${progressPct}%` }} />`

 438 |             </div>
     | In `Mindfulness` (src/components/Mindfulness.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 439 |           </div>
     | In `Mindfulness` (src/components/Mindfulness.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 440 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

 441 |           <audio ref={audioRef} src={MODES[mode].audioSrc} preload="metadata" />
     | In `Mindfulness` (src/components/Mindfulness.jsx): Opens it. The hidden audio element Mindfulness plays. Source: `<audio ref={audioRef} src={MODES[mode].audioSrc} preload="metadata" />`

 442 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

 443 |           <div className="flex gap-2 mt-4">
     | In `Mindfulness` (src/components/Mindfulness.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="flex gap-2 mt-4">`

 444 |             <button
     | In `Mindfulness` (src/components/Mindfulness.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button`

 445 |               className="btn btn-primary"
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `className="btn btn-primary"`. It runs when Mindfulness runs, in order, before the next line of the same function.

 446 |               onClick={() => setRunning(true)}
     | In `Mindfulness` (src/components/Mindfulness.jsx): event prop `onClick={() => setRunning(true)}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 447 |               disabled={running || !!audioError}
     | In `Mindfulness` (src/components/Mindfulness.jsx): `disabled={running || !!audioError}` closes Mindfulness (opened on line 273). Names declared inside that block end here.

 448 |             >
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `>`. It runs when Mindfulness runs, in order, before the next line of the same function.

 449 |               ▶ Start
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `▶ Start`. It runs when Mindfulness runs, in order, before the next line of the same function.

 450 |             </button>
     | In `Mindfulness` (src/components/Mindfulness.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

 451 |             <button
     | In `Mindfulness` (src/components/Mindfulness.jsx): Opens it. A button. If it has onClick, that function runs on press. Source: `<button`

 452 |               className="btn btn-ghost"
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `className="btn btn-ghost"`. It runs when Mindfulness runs, in order, before the next line of the same function.

 453 |               onClick={() => setRunning(false)}
     | In `Mindfulness` (src/components/Mindfulness.jsx): event prop `onClick={() => setRunning(false)}`. React registers the listener. The arrow function runs later, on that event, with the state from the render that created it unless it reads a ref.

 454 |               disabled={!running}
     | In `Mindfulness` (src/components/Mindfulness.jsx): `disabled={!running}` closes Mindfulness (opened on line 273). Names declared inside that block end here.

 455 |             >
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `>`. It runs when Mindfulness runs, in order, before the next line of the same function.

 456 |               ⏹ Stop
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `⏹ Stop`. It runs when Mindfulness runs, in order, before the next line of the same function.

 457 |             </button>
     | In `Mindfulness` (src/components/Mindfulness.jsx): Closes it. A button. If it has onClick, that function runs on press. Source: `</button>`

 458 |           </div>
     | In `Mindfulness` (src/components/Mindfulness.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 459 |         </div>
     | In `Mindfulness` (src/components/Mindfulness.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 460 | 
     | Blank line in `src/components/Mindfulness.jsx` (the audio breathing page; the top of the file is old commented code), inside Mindfulness. The parser skips it. It separates the previous statement from the next so the function is readable.

 461 |         <aside className="stack">
     | In `Mindfulness` (src/components/Mindfulness.jsx): Opens it. A side column. Source: `<aside className="stack">`

 462 |           <div className="card">
     | In `Mindfulness` (src/components/Mindfulness.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="card">`

 463 |             <div className="card-title">Affirmation</div>
     | In `Mindfulness` (src/components/Mindfulness.jsx): Opens it. A box that groups the elements inside it. Source: `<div className="card-title">Affirmation</div>`

 464 |             <Affirmations ref={affirmRef} />
     | In `Mindfulness` (src/components/Mindfulness.jsx): Opens it. The sentence box. The parent holds a ref and asks it for a line. Source: `<Affirmations ref={affirmRef} />`

 465 |           </div>
     | In `Mindfulness` (src/components/Mindfulness.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 466 |         </aside>
     | In `Mindfulness` (src/components/Mindfulness.jsx): Closes it. A side column. Source: `</aside>`

 467 |       </div>
     | In `Mindfulness` (src/components/Mindfulness.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 468 |     </div>
     | In `Mindfulness` (src/components/Mindfulness.jsx): Closes it. A box that groups the elements inside it. Source: `</div>`

 469 |   );
     | In `Mindfulness` (src/components/Mindfulness.jsx): statement `);`. It runs when Mindfulness runs, in order, before the next line of the same function.

 470 | }
     | In `Mindfulness` (src/components/Mindfulness.jsx): `}` closes Mindfulness (opened on line 273). Names declared inside that block end here.

