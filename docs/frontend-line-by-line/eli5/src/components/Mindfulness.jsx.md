# `src/components/Mindfulness.jsx`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | /*import React, { useEffect, useRef, useState } from "react";
     | A note for people. The app skips this line.

   2 | import Affirmations from "./Affirmations";
     | A note for people. The app skips this line.

   3 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   4 | const MODES = {
     | A note for people. The app skips this line.

   5 |   belly: { label: "Belly breathing", steps: ["Breathe in", "Breathe out"], ms: 4000 },
     | A note for people. The app skips this line.

   6 |   box: { label: "Box breathing", steps: ["Inhale 4", "Hold 4", "Exhale 4", "Hold 4"], ms: 4000 },
     | A note for people. The app skips this line.

   7 |   guided: { label: "Guided Meditation (audio)", steps: ["Listen & relax"], ms: 60000 },
     | A note for people. The app skips this line.

   8 |   sleep: { label: "Sleep breathing", steps: ["Breathe in 4", "Breathe out 6"], ms: 5000 }
     | A note for people. The app skips this line.

   9 | };
     | A note for people. The app skips this line.

  10 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  11 | export default function Mindfulness(){
     | A note for people. The app skips this line.

  12 |   const [mode,setMode] = useState("belly");
     | A note for people. The app skips this line.

  13 |   const [running,setRunning] = useState(false);
     | A note for people. The app skips this line.

  14 |   const [step, setStep] = useState(0);
     | A note for people. The app skips this line.

  15 |   const timerRef = useRef();
     | A note for people. The app skips this line.

  16 |   const audioRef = useRef();
     | A note for people. The app skips this line.

  17 |   const affirmRef = useRef();
     | A note for people. The app skips this line.

  18 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  19 |   useEffect(()=>{
     | A note for people. The app skips this line.

  20 |     function onVisibility(){
     | A note for people. The app skips this line.

  21 |       if(document.visibilityState === 'hidden' && running){
     | A note for people. The app skips this line.

  22 |         setRunning(false);
     | A note for people. The app skips this line.

  23 |         if(affirmRef.current) affirmRef.current.messageForContext('tab-change');
     | A note for people. The app skips this line.

  24 |       }
     | A note for people. The app skips this line.

  25 |     }
     | A note for people. The app skips this line.

  26 |     document.addEventListener('visibilitychange', onVisibility);
     | A note for people. The app skips this line.

  27 |     return ()=> document.removeEventListener('visibilitychange', onVisibility);
     | A note for people. The app skips this line.

  28 |   }, [running]);
     | A note for people. The app skips this line.

  29 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  30 |   useEffect(()=>{
     | A note for people. The app skips this line.

  31 |     if(!running){ clearInterval(timerRef.current); if(audioRef.current) audioRef.current.pause(); return; }
     | A note for people. The app skips this line.

  32 |     const cfg = MODES[mode];
     | A note for people. The app skips this line.

  33 |     if(mode === 'guided'){ if(audioRef.current) audioRef.current.play(); }
     | A note for people. The app skips this line.

  34 |     timerRef.current = setInterval(()=>{
     | A note for people. The app skips this line.

  35 |       setStep(s => {
     | A note for people. The app skips this line.

  36 |         const next = s + 1;
     | A note for people. The app skips this line.

  37 |         if(next >= cfg.steps.length){
     | A note for people. The app skips this line.

  38 |           if(mode === 'guided'){ setRunning(false); if(affirmRef.current) affirmRef.current.messageForContext('task-complete'); return 0; }
     | A note for people. The app skips this line.

  39 |           return 0;
     | A note for people. The app skips this line.

  40 |         }
     | A note for people. The app skips this line.

  41 |         return next;
     | A note for people. The app skips this line.

  42 |       });
     | A note for people. The app skips this line.

  43 |     }, cfg.ms);
     | A note for people. The app skips this line.

  44 |     return ()=> clearInterval(timerRef.current);
     | A note for people. The app skips this line.

  45 |   }, [running, mode]);
     | A note for people. The app skips this line.

  46 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  47 |   return (
     | A note for people. The app skips this line.

  48 |     <div className="app">
     | A note for people. The app skips this line.

  49 |       <div className="page-header">
     | A note for people. The app skips this line.

  50 |         <h2>Mindfulness</h2>
     | A note for people. The app skips this line.

  51 |         <div className="small">Short practices to reset your attention.</div>
     | A note for people. The app skips this line.

  52 |       </div>
     | A note for people. The app skips this line.

  53 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  54 |       <div className="main-grid">
     | A note for people. The app skips this line.

  55 |         <div className="card">
     | A note for people. The app skips this line.

  56 |           <label className="small">Mode</label>
     | A note for people. The app skips this line.

  57 |           <select className="select" value={mode} onChange={e=>setMode(e.target.value)} style={{marginTop:8}}>
     | A note for people. The app skips this line.

  58 |             {Object.keys(MODES).map(k => <option key={k} value={k}>{MODES[k].label}</option>)}
     | A note for people. The app skips this line.

  59 |           </select>
     | A note for people. The app skips this line.

  60 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  61 |           <div className="mind-steps" style={{marginTop:18}}>
     | A note for people. The app skips this line.

  62 |             {MODES[mode].steps[step % MODES[mode].steps.length]}
     | A note for people. The app skips this line.

  63 |           </div>
     | A note for people. The app skips this line.

  64 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  65 |           {mode === 'guided' && <audio ref={audioRef} controls src="/guided-sample.mp3" />}
     | A note for people. The app skips this line.

  66 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  67 |           <div style={{marginTop:12}}>
     | A note for people. The app skips this line.

  68 |             <button className="btn" onClick={()=>setRunning(true)}>Start</button>
     | A note for people. The app skips this line.

  69 |             <button className="btn secondary" onClick={()=>setRunning(false)} style={{marginLeft:8}}>Stop</button>
     | A note for people. The app skips this line.

  70 |           </div>
     | A note for people. The app skips this line.

  71 |         </div>
     | A note for people. The app skips this line.

  72 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  73 |         <aside className="card">
     | A note for people. The app skips this line.

  74 |           <h4>Affirmation</h4>
     | A note for people. The app skips this line.

  75 |           <Affirmations ref={affirmRef} />
     | A note for people. The app skips this line.

  76 |         </aside>
     | A note for people. The app skips this line.

  77 |       </div>
     | A note for people. The app skips this line.

  78 |     </div>
     | A note for people. The app skips this line.

  79 |   );
     | A note for people. The app skips this line.

  80 | }*/
     | A note for people. The app skips this line.

  81 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  82 | /*import React, { useEffect, useRef, useState } from "react";
     | A note for people. The app skips this line.

  83 | import Affirmations from "./Affirmations";
     | A note for people. The app skips this line.

  84 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  85 | const MODES = {
     | A note for people. The app skips this line.

  86 |   meditation: { 
     | A note for people. The app skips this line.

  87 |     label: "Meditation ", 
     | A note for people. The app skips this line.

  88 |     audioSrc: "./audio/04_Meditation_for_Working_with_Difficulties.mp3"
     | A note for people. The app skips this line.

  89 |   },
     | A note for people. The app skips this line.

  90 |   grounding: { 
     | A note for people. The app skips this line.

  91 |     label: "Grounding", 
     | A note for people. The app skips this line.

  92 |     audioSrc: "./audio/Body-Scan-Meditation.mp3"
     | A note for people. The app skips this line.

  93 |   },
     | A note for people. The app skips this line.

  94 |   guided: { 
     | A note for people. The app skips this line.

  95 |     label: "Sleep meditation", 
     | A note for people. The app skips this line.

  96 |     audioSrc: "./audio/Body-Scan-Sleep.mp3"
     | A note for people. The app skips this line.

  97 |   }
     | A note for people. The app skips this line.

  98 |   
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  99 | };
     | A note for people. The app skips this line.

 100 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 101 | export default function Mindfulness(){
     | A note for people. The app skips this line.

 102 |   const [mode, setMode] = useState("meditation");
     | A note for people. The app skips this line.

 103 |   const [running, setRunning] = useState(false);
     | A note for people. The app skips this line.

 104 |   const [currentTime, setCurrentTime] = useState(0);
     | A note for people. The app skips this line.

 105 |   const [duration, setDuration] = useState(0);
     | A note for people. The app skips this line.

 106 |   const audioRef = useRef();
     | A note for people. The app skips this line.

 107 |   const affirmRef = useRef();
     | A note for people. The app skips this line.

 108 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 109 |   useEffect(()=>{
     | A note for people. The app skips this line.

 110 |     function onVisibility(){
     | A note for people. The app skips this line.

 111 |       if(document.visibilityState === 'hidden' && running){
     | A note for people. The app skips this line.

 112 |         setRunning(false);
     | A note for people. The app skips this line.

 113 |         if(affirmRef.current) affirmRef.current.messageForContext('tab-change');
     | A note for people. The app skips this line.

 114 |       }
     | A note for people. The app skips this line.

 115 |     }
     | A note for people. The app skips this line.

 116 |     document.addEventListener('visibilitychange', onVisibility);
     | A note for people. The app skips this line.

 117 |     return ()=> document.removeEventListener('visibilitychange', onVisibility);
     | A note for people. The app skips this line.

 118 |   }, [running]);
     | A note for people. The app skips this line.

 119 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 120 |   // Load audio duration when mode changes
     | A note written for people. The app does not run it.

 121 |   useEffect(() => {
     | A note for people. The app skips this line.

 122 |     const audio = audioRef.current;
     | A note for people. The app skips this line.

 123 |     if (!audio) return;
     | A note for people. The app skips this line.

 124 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 125 |     const handleLoadedMetadata = () => {
     | A note for people. The app skips this line.

 126 |       setDuration(audio.duration * 1000); // Convert to ms
     | A note for people. The app skips this line.

 127 |     };
     | A note for people. The app skips this line.

 128 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 129 |     audio.addEventListener('loadedmetadata', handleLoadedMetadata);
     | A note for people. The app skips this line.

 130 |     
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 131 |     // Trigger load
     | A note written for people. The app does not run it.

 132 |     audio.load();
     | A note for people. The app skips this line.

 133 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 134 |     return () => {
     | A note for people. The app skips this line.

 135 |       audio.removeEventListener('loadedmetadata', handleLoadedMetadata);
     | A note for people. The app skips this line.

 136 |     };
     | A note for people. The app skips this line.

 137 |   }, [mode]);
     | A note for people. The app skips this line.

 138 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 139 |   useEffect(()=>{
     | A note for people. The app skips this line.

 140 |     if(!running){ 
     | A note for people. The app skips this line.

 141 |       if(audioRef.current) {
     | A note for people. The app skips this line.

 142 |         audioRef.current.pause();
     | A note for people. The app skips this line.

 143 |         audioRef.current.currentTime = 0;
     | A note for people. The app skips this line.

 144 |       }
     | A note for people. The app skips this line.

 145 |       setCurrentTime(0);
     | A note for people. The app skips this line.

 146 |       return; 
     | A note for people. The app skips this line.

 147 |     }
     | A note for people. The app skips this line.

 148 |     
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 149 |     if(audioRef.current) {
     | A note for people. The app skips this line.

 150 |       audioRef.current.play();
     | A note for people. The app skips this line.

 151 |       
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 152 |       const handleAudioEnd = () => {
     | A note for people. The app skips this line.

 153 |         setRunning(false);
     | A note for people. The app skips this line.

 154 |         if(affirmRef.current) affirmRef.current.messageForContext('task-complete');
     | A note for people. The app skips this line.

 155 |       };
     | A note for people. The app skips this line.

 156 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 157 |       const handleTimeUpdate = () => {
     | A note for people. The app skips this line.

 158 |         setCurrentTime(audioRef.current.currentTime * 1000);
     | A note for people. The app skips this line.

 159 |       };
     | A note for people. The app skips this line.

 160 |       
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 161 |       audioRef.current.addEventListener('ended', handleAudioEnd);
     | A note for people. The app skips this line.

 162 |       audioRef.current.addEventListener('timeupdate', handleTimeUpdate);
     | A note for people. The app skips this line.

 163 |       
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 164 |       return () => {
     | A note for people. The app skips this line.

 165 |         if(audioRef.current) {
     | A note for people. The app skips this line.

 166 |           audioRef.current.removeEventListener('ended', handleAudioEnd);
     | A note for people. The app skips this line.

 167 |           audioRef.current.removeEventListener('timeupdate', handleTimeUpdate);
     | A note for people. The app skips this line.

 168 |         }
     | A note for people. The app skips this line.

 169 |       };
     | A note for people. The app skips this line.

 170 |     }
     | A note for people. The app skips this line.

 171 |   }, [running, mode]);
     | A note for people. The app skips this line.

 172 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 173 |   // Reset when mode changes
     | A note written for people. The app does not run it.

 174 |   useEffect(() => {
     | A note for people. The app skips this line.

 175 |     setRunning(false);
     | A note for people. The app skips this line.

 176 |     setCurrentTime(0);
     | A note for people. The app skips this line.

 177 |   }, [mode]);
     | A note for people. The app skips this line.

 178 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 179 |   const formatTime = (ms) => {
     | A note for people. The app skips this line.

 180 |     const seconds = Math.floor(ms / 1000);
     | A note for people. The app skips this line.

 181 |     const mins = Math.floor(seconds / 60);
     | A note for people. The app skips this line.

 182 |     const secs = seconds % 60;
     | A note for people. The app skips this line.

 183 |     return `${mins}:${secs.toString().padStart(2, '0')}`;
     | A note for people. The app skips this line.

 184 |   };
     | A note for people. The app skips this line.

 185 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 186 |   return (
     | A note for people. The app skips this line.

 187 |     <div className="app">
     | A note for people. The app skips this line.

 188 |       <div className="page-header">
     | A note for people. The app skips this line.

 189 |         <h2>Mindfulness</h2>
     | A note for people. The app skips this line.

 190 |         <div className="small">Audio-guided practices to reset your attention.</div>
     | A note for people. The app skips this line.

 191 |       </div>
     | A note for people. The app skips this line.

 192 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 193 |       <div className="main-grid">
     | A note for people. The app skips this line.

 194 |         <div className="card">
     | A note for people. The app skips this line.

 195 |           <label className="small">Mode</label>
     | A note for people. The app skips this line.

 196 |           <select 
     | A note for people. The app skips this line.

 197 |             className="select" 
     | A note for people. The app skips this line.

 198 |             value={mode} 
     | A note for people. The app skips this line.

 199 |             onChange={e=>setMode(e.target.value)} 
     | A note for people. The app skips this line.

 200 |             style={{marginTop:8}}
     | A note for people. The app skips this line.

 201 |             disabled={running}
     | A note for people. The app skips this line.

 202 |           >
     | A note for people. The app skips this line.

 203 |             {Object.keys(MODES).map(k => <option key={k} value={k}>{MODES[k].label}</option>)}
     | A note for people. The app skips this line.

 204 |           </select>
     | A note for people. The app skips this line.

 205 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 206 |           <div style={{
     | A note for people. The app skips this line.

 207 |             marginTop: 24,
     | A note for people. The app skips this line.

 208 |             padding: '3rem 1rem',
     | A note for people. The app skips this line.

 209 |             textAlign: 'center',
     | A note for people. The app skips this line.

 210 |             background: running ? 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)' : '#f7f7f7',
     | A note for people. The app skips this line.

 211 |             borderRadius: '12px',
     | A note for people. The app skips this line.

 212 |             transition: 'all 0.3s ease',
     | A note for people. The app skips this line.

 213 |             color: running ? 'white' : '#666'
     | A note for people. The app skips this line.

 214 |           }}>
     | A note for people. The app skips this line.

 215 |             <div style={{fontSize: '1.2rem', marginBottom: '0.5rem', opacity: 0.9}}>
     | A note for people. The app skips this line.

 216 |               {running ? 'Session in progress' : 'Ready to begin'}
     | A note for people. The app skips this line.

 217 |             </div>
     | A note for people. The app skips this line.

 218 |             <div style={{fontSize: '3rem', fontWeight: 'bold'}}>
     | A note for people. The app skips this line.

 219 |               {formatTime(currentTime)}
     | A note for people. The app skips this line.

 220 |             </div>
     | A note for people. The app skips this line.

 221 |             {duration > 0 && (
     | A note for people. The app skips this line.

 222 |               <div style={{fontSize: '0.9rem', marginTop: '0.5rem', opacity: 0.8}}>
     | A note for people. The app skips this line.

 223 |                 of {formatTime(duration)}
     | A note for people. The app skips this line.

 224 |               </div>
     | A note for people. The app skips this line.

 225 |             )}
     | A note for people. The app skips this line.

 226 |           </div>
     | A note for people. The app skips this line.

 227 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 228 |           <audio 
     | A note for people. The app skips this line.

 229 |             ref={audioRef} 
     | A note for people. The app skips this line.

 230 |             src={MODES[mode].audioSrc}
     | A note for people. The app skips this line.

 231 |             preload="metadata"
     | A note for people. The app skips this line.

 232 |             style={{display: 'none'}}
     | A note for people. The app skips this line.

 233 |           />
     | A note for people. The app skips this line.

 234 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 235 |           <div style={{marginTop:16}}>
     | A note for people. The app skips this line.

 236 |             <button className="btn" onClick={()=>setRunning(true)} disabled={running}>
     | A note for people. The app skips this line.

 237 |               Start
     | A note for people. The app skips this line.

 238 |             </button>
     | A note for people. The app skips this line.

 239 |             <button className="btn secondary" onClick={()=>setRunning(false)} style={{marginLeft:8}} disabled={!running}>
     | A note for people. The app skips this line.

 240 |               Stop
     | A note for people. The app skips this line.

 241 |             </button>
     | A note for people. The app skips this line.

 242 |           </div>
     | A note for people. The app skips this line.

 243 |         </div>
     | A note for people. The app skips this line.

 244 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 245 |         <aside className="card">
     | A note for people. The app skips this line.

 246 |           <h4>Affirmation</h4>
     | A note for people. The app skips this line.

 247 |           <Affirmations ref={affirmRef} />
     | A note for people. The app skips this line.

 248 |         </aside>
     | A note for people. The app skips this line.

 249 |       </div>
     | A note for people. The app skips this line.

 250 |     </div>
     | A note for people. The app skips this line.

 251 |   );
     | A note for people. The app skips this line.

 252 | }*/
     | A note for people. The app skips this line.

 253 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 254 | import React, { useEffect, useRef, useState } from "react";
     | Borrows React so this file can remember things and draw the screen.

 255 | import Affirmations from "./Affirmations";
     | This file borrows a tool another file already made.

 256 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 257 | const MODES = {
     | In FocusTimer, Pomodoro is 25/5 and Deep Work is 50/10. In Mindfulness the live MODES (the third copy, after line 252) are three mp3s. The earlier MODES are inside comments and never run.

 258 |   meditation: {
     | Inside the top of the file, this line runs as written: meditation: {. It happens in order, after the line above it and before the line below it.

 259 |     label: "Meditation",
     | Inside the top of the file, this line runs as written: label: "Meditation",. It happens in order, after the line above it and before the line below it.

 260 |     audioSrc: "/audio/04_Meditation_for_Working_with_Difficulties.mp3"
     | Inside the top of the file, this line runs as written: audioSrc: "/audio/04_Meditation_for_Working_with_Difficulties.mp3". It happens in order, after the line above it and before the line below it.

 261 |   },
     | This ends meditation: { (opened on line 258).

 262 |   grounding: {
     | Inside the top of the file, this line runs as written: grounding: {. It happens in order, after the line above it and before the line below it.

 263 |     label: "Grounding",
     | Inside the top of the file, this line runs as written: label: "Grounding",. It happens in order, after the line above it and before the line below it.

 264 |     audioSrc: "/audio/Body-Scan-Meditation.mp3"
     | Inside the top of the file, this line runs as written: audioSrc: "/audio/Body-Scan-Meditation.mp3". It happens in order, after the line above it and before the line below it.

 265 |   },
     | This ends grounding: { (opened on line 262).

 266 |   guided: {
     | Inside the top of the file, this line runs as written: guided: {. It happens in order, after the line above it and before the line below it.

 267 |     label: "Sleep meditation",
     | Inside the top of the file, this line runs as written: label: "Sleep meditation",. It happens in order, after the line above it and before the line below it.

 268 |     audioSrc: "/audio/Body-Scan-for-Sleep.mp3"
     | Inside the top of the file, this line runs as written: audioSrc: "/audio/Body-Scan-for-Sleep.mp3". It happens in order, after the line above it and before the line below it.

 269 |   }
     | This ends guided: { (opened on line 266).

 270 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 271 | };
     | This ends const MODES = { (opened on line 257).

 272 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 273 | export default function Mindfulness(){
     | This starts Mindfulness. The live function starts at the third Mindfulness in the file. The first two are inside a block comment. It plays one of three mp3s and stops if the tab is hidden.

 274 |   const [mode, setMode] = useState("meditation");
     | This gives a short name to a value so the rest of Mindfulness can use it.

 275 |   const [running, setRunning] = useState(false);
     | This gives a short name to a value so the rest of Mindfulness can use it.

 276 |   const [currentTime, setCurrentTime] = useState(0);
     | This gives a short name to a value so the rest of Mindfulness can use it.

 277 |   const [duration, setDuration] = useState(0);
     | This gives a short name to a value so the rest of Mindfulness can use it.

 278 |   const [audioError, setAudioError] = useState(null);
     | This gives a short name to a value so the rest of Mindfulness can use it.

 279 |   const audioRef = useRef();
     | This gives a short name to a value so the rest of Mindfulness can use it.

 280 |   const affirmRef = useRef();
     | This gives a short name to a value so the rest of Mindfulness can use it.

 281 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 282 |   useEffect(()=>{
     | This is an extra job that happens after the picture is drawn.

 283 |     function onVisibility(){
     | Inside onVisibility, this line runs as written: function onVisibility(){. It happens in order, after the line above it and before the line below it.

 284 |       if(document.visibilityState === 'hidden' && running){
     | Inside onVisibility, this line runs as written: if(document.visibilityState === 'hidden' && running){. It happens in order, after the line above it and before the line below it.

 285 |         setRunning(false);
     | Inside onVisibility, this line runs as written: setRunning(false);. It happens in order, after the line above it and before the line below it.

 286 |         if(affirmRef.current) affirmRef.current.messageForContext('tab-change');
     | Inside onVisibility, this line runs as written: if(affirmRef.current) affirmRef.current.messageForContext('tab-change');. It happens in order, after the line above it and before the line below it.

 287 |       }
     | This ends if(document.visibilityState === 'hidden' (opened on line 284).

 288 |     }
     | This ends onVisibility (opened on line 283).

 289 |     document.addEventListener('visibilitychange', onVisibility);
     | Inside Mindfulness, this line runs as written: document.addEventListener('visibilitychange', onVisibility);. It happens in order, after the line above it and before the line below it.

 290 |     return ()=> document.removeEventListener('visibilitychange', onVisibility);
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

 291 |   }, [running]);
     | This ends effect in Mindfulness (opened on line 282).

 292 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 293 |   // Load audio duration when mode changes
     | A note written for people. The app does not run it.

 294 |   useEffect(() => {
     | This is an extra job that happens after the picture is drawn.

 295 |     const audio = audioRef.current;
     | This gives a short name to a value so the rest of Mindfulness can use it.

 296 |     if (!audio) return;
     | This asks a yes-or-no question. The next bit runs only on yes.

 297 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 298 |     const handleLoadedMetadata = () => {
     | This gives a short name to a value so the rest of Mindfulness can use it.

 299 |       console.log('Audio loaded successfully, duration:', audio.duration);
     | Inside Mindfulness, this line runs as written: console.log('Audio loaded successfully, duration:', audio.duration);. It happens in order, after the line above it and before the line below it.

 300 |       setDuration(audio.duration * 1000);
     | Inside Mindfulness, this line runs as written: setDuration(audio.duration * 1000);. It happens in order, after the line above it and before the line below it.

 301 |       setAudioError(null);
     | Inside Mindfulness, this line runs as written: setAudioError(null);. It happens in order, after the line above it and before the line below it.

 302 |     };
     | This ends const handleLoadedMetadata = () => { (opened on line 298).

 303 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 304 |     const handleError = (e) => {
     | This gives a short name to a value so the rest of Mindfulness can use it.

 305 |       console.error('Audio load error:', e);
     | Inside Mindfulness, this line runs as written: console.error('Audio load error:', e);. It happens in order, after the line above it and before the line below it.

 306 |       console.error('Audio source:', audio.src);
     | Inside Mindfulness, this line runs as written: console.error('Audio source:', audio.src);. It happens in order, after the line above it and before the line below it.

 307 |       console.error('Current URL:', window.location.href);
     | Inside Mindfulness, this line runs as written: console.error('Current URL:', window.location.href);. It happens in order, after the line above it and before the line below it.

 308 |       setAudioError(`Cannot load audio file. Check if file exists at: ${audio.src}`);
     | This ends const handleError = (e) => { (opened on line 304).

 309 |       setRunning(false);
     | Inside Mindfulness, this line runs as written: setRunning(false);. It happens in order, after the line above it and before the line below it.

 310 |     };
     | This ends const handleError = (e) => { (opened on line 304).

 311 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 312 |     const handleCanPlay = () => {
     | This gives a short name to a value so the rest of Mindfulness can use it.

 313 |       console.log('Audio is ready to play');
     | Inside Mindfulness, this line runs as written: console.log('Audio is ready to play');. It happens in order, after the line above it and before the line below it.

 314 |     };
     | This ends const handleCanPlay = () => { (opened on line 312).

 315 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 316 |     audio.addEventListener('loadedmetadata', handleLoadedMetadata);
     | Inside Mindfulness, this line runs as written: audio.addEventListener('loadedmetadata', handleLoadedMetadata);. It happens in order, after the line above it and before the line below it.

 317 |     audio.addEventListener('error', handleError);
     | Inside Mindfulness, this line runs as written: audio.addEventListener('error', handleError);. It happens in order, after the line above it and before the line below it.

 318 |     audio.addEventListener('canplay', handleCanPlay);
     | Inside Mindfulness, this line runs as written: audio.addEventListener('canplay', handleCanPlay);. It happens in order, after the line above it and before the line below it.

 319 |     
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 320 |     // Reset and load
     | A note written for people. The app does not run it.

 321 |     audio.load();
     | Inside Mindfulness, this line runs as written: audio.load();. It happens in order, after the line above it and before the line below it.

 322 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 323 |     return () => {
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

 324 |       audio.removeEventListener('loadedmetadata', handleLoadedMetadata);
     | Inside Mindfulness, this line runs as written: audio.removeEventListener('loadedmetadata', handleLoadedMetadata);. It happens in order, after the line above it and before the line below it.

 325 |       audio.removeEventListener('error', handleError);
     | Inside Mindfulness, this line runs as written: audio.removeEventListener('error', handleError);. It happens in order, after the line above it and before the line below it.

 326 |       audio.removeEventListener('canplay', handleCanPlay);
     | Inside Mindfulness, this line runs as written: audio.removeEventListener('canplay', handleCanPlay);. It happens in order, after the line above it and before the line below it.

 327 |     };
     | This ends return () => { (opened on line 323).

 328 |   }, [mode]);
     | This ends effect in Mindfulness (opened on line 294).

 329 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 330 |   useEffect(()=>{
     | This is an extra job that happens after the picture is drawn.

 331 |     if(!running){ 
     | Inside Mindfulness, this line runs as written: if(!running){. It happens in order, after the line above it and before the line below it.

 332 |       if(audioRef.current) {
     | Inside Mindfulness, this line runs as written: if(audioRef.current) {. It happens in order, after the line above it and before the line below it.

 333 |         audioRef.current.pause();
     | Inside Mindfulness, this line runs as written: audioRef.current.pause();. It happens in order, after the line above it and before the line below it.

 334 |         audioRef.current.currentTime = 0;
     | Inside Mindfulness, this line runs as written: audioRef.current.currentTime = 0;. It happens in order, after the line above it and before the line below it.

 335 |       }
     | This ends if(audioRef.current) { (opened on line 332).

 336 |       setCurrentTime(0);
     | Inside Mindfulness, this line runs as written: setCurrentTime(0);. It happens in order, after the line above it and before the line below it.

 337 |       return; 
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

 338 |     }
     | This ends if(!running){ (opened on line 331).

 339 |     
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 340 |     const audio = audioRef.current;
     | This gives a short name to a value so the rest of Mindfulness can use it.

 341 |     if(audio) {
     | Inside Mindfulness, this line runs as written: if(audio) {. It happens in order, after the line above it and before the line below it.

 342 |       const playPromise = audio.play();
     | This gives a short name to a value so the rest of Mindfulness can use it.

 343 |       
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 344 |       if (playPromise !== undefined) {
     | This asks a yes-or-no question. The next bit runs only on yes.

 345 |         playPromise
     | Inside Mindfulness, this line runs as written: playPromise. It happens in order, after the line above it and before the line below it.

 346 |           .then(() => {
     | Inside Mindfulness, this line runs as written: .then(() => {. It happens in order, after the line above it and before the line below it.

 347 |             console.log('Audio playback started successfully');
     | Inside Mindfulness, this line runs as written: console.log('Audio playback started successfully');. It happens in order, after the line above it and before the line below it.

 348 |           })
     | This ends .then(() => { (opened on line 346).

 349 |           .catch(error => {
     | Inside Mindfulness, this line runs as written: .catch(error => {. It happens in order, after the line above it and before the line below it.

 350 |             console.error('Playback error:', error);
     | Inside Mindfulness, this line runs as written: console.error('Playback error:', error);. It happens in order, after the line above it and before the line below it.

 351 |             setAudioError('Playback failed: ' + error.message);
     | Inside Mindfulness, this line runs as written: setAudioError('Playback failed: ' + error.message);. It happens in order, after the line above it and before the line below it.

 352 |             setRunning(false);
     | Inside Mindfulness, this line runs as written: setRunning(false);. It happens in order, after the line above it and before the line below it.

 353 |           });
     | This ends .catch(error => { (opened on line 349).

 354 |       }
     | This ends if (playPromise !== undefined) { (opened on line 344).

 355 |       
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 356 |       const handleAudioEnd = () => {
     | This gives a short name to a value so the rest of Mindfulness can use it.

 357 |         console.log('Audio ended');
     | Inside Mindfulness, this line runs as written: console.log('Audio ended');. It happens in order, after the line above it and before the line below it.

 358 |         setRunning(false);
     | Inside Mindfulness, this line runs as written: setRunning(false);. It happens in order, after the line above it and before the line below it.

 359 |         if(affirmRef.current) affirmRef.current.messageForContext('task-complete');
     | Inside Mindfulness, this line runs as written: if(affirmRef.current) affirmRef.current.messageForContext('task-complete');. It happens in order, after the line above it and before the line below it.

 360 |       };
     | This ends const handleAudioEnd = () => { (opened on line 356).

 361 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 362 |       const handleTimeUpdate = () => {
     | This gives a short name to a value so the rest of Mindfulness can use it.

 363 |         setCurrentTime(audio.currentTime * 1000);
     | Inside Mindfulness, this line runs as written: setCurrentTime(audio.currentTime * 1000);. It happens in order, after the line above it and before the line below it.

 364 |       };
     | This ends const handleTimeUpdate = () => { (opened on line 362).

 365 |       
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 366 |       audio.addEventListener('ended', handleAudioEnd);
     | Inside Mindfulness, this line runs as written: audio.addEventListener('ended', handleAudioEnd);. It happens in order, after the line above it and before the line below it.

 367 |       audio.addEventListener('timeupdate', handleTimeUpdate);
     | Inside Mindfulness, this line runs as written: audio.addEventListener('timeupdate', handleTimeUpdate);. It happens in order, after the line above it and before the line below it.

 368 |       
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 369 |       return () => {
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

 370 |         if(audio) {
     | Inside Mindfulness, this line runs as written: if(audio) {. It happens in order, after the line above it and before the line below it.

 371 |           audio.removeEventListener('ended', handleAudioEnd);
     | Inside Mindfulness, this line runs as written: audio.removeEventListener('ended', handleAudioEnd);. It happens in order, after the line above it and before the line below it.

 372 |           audio.removeEventListener('timeupdate', handleTimeUpdate);
     | Inside Mindfulness, this line runs as written: audio.removeEventListener('timeupdate', handleTimeUpdate);. It happens in order, after the line above it and before the line below it.

 373 |         }
     | This ends if(audio) { (opened on line 370).

 374 |       };
     | This ends return () => { (opened on line 369).

 375 |     }
     | This ends if(audio) { (opened on line 341).

 376 |   }, [running, mode]);
     | This ends effect in Mindfulness (opened on line 330).

 377 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 378 |   // Reset when mode changes
     | A note written for people. The app does not run it.

 379 |   useEffect(() => {
     | This is an extra job that happens after the picture is drawn.

 380 |     setRunning(false);
     | Inside Mindfulness, this line runs as written: setRunning(false);. It happens in order, after the line above it and before the line below it.

 381 |     setCurrentTime(0);
     | Inside Mindfulness, this line runs as written: setCurrentTime(0);. It happens in order, after the line above it and before the line below it.

 382 |     setAudioError(null);
     | Inside Mindfulness, this line runs as written: setAudioError(null);. It happens in order, after the line above it and before the line below it.

 383 |   }, [mode]);
     | This ends effect in Mindfulness (opened on line 379).

 384 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 385 |   const formatTime = (ms) => {
     | This gives a short name to a value so the rest of Mindfulness can use it.

 386 |     const seconds = Math.floor(ms / 1000);
     | This gives a short name to a value so the rest of Mindfulness can use it.

 387 |     const mins = Math.floor(seconds / 60);
     | This gives a short name to a value so the rest of Mindfulness can use it.

 388 |     const secs = seconds % 60;
     | This gives a short name to a value so the rest of Mindfulness can use it.

 389 |     return `${mins}:${secs.toString().padStart(2, '0')}`;
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

 390 |   };
     | This ends const formatTime = (ms) => { (opened on line 385).

 391 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 392 |   const progressPct = duration > 0 ? (currentTime / duration) * 100 : 0;
     | This gives a short name to a value so the rest of Mindfulness can use it.

 393 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 394 |   return (
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

 395 |     <div>
     | This draws one piece of the page while Mindfulness is showing.

 396 |       <h1 className="page-title">Mindfulness</h1>
     | This draws one piece of the page while Mindfulness is showing.

 397 |       <p className="page-subtitle">Audio-guided practices to reset your attention</p>
     | This draws one piece of the page while Mindfulness is showing.

 398 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 399 |       <div className="grid-main">
     | This draws one piece of the page while Mindfulness is showing.

 400 |         <div className="card">
     | This draws one piece of the page while Mindfulness is showing.

 401 |           <div className="text-xs text-muted mb-1">Session type</div>
     | This draws one piece of the page while Mindfulness is showing.

 402 |           <select
     | This draws one piece of the page while Mindfulness is showing.

 403 |             className="select mb-4"
     | Inside Mindfulness, this line runs as written: className="select mb-4". It happens in order, after the line above it and before the line below it.

 404 |             value={mode}
     | This ends Mindfulness (opened on line 273).

 405 |             onChange={(e) => setMode(e.target.value)}
     | This ends Mindfulness (opened on line 273).

 406 |             disabled={running}
     | This ends Mindfulness (opened on line 273).

 407 |           >
     | Inside Mindfulness, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 408 |             {Object.keys(MODES).map((k) => (
     | Inside Mindfulness, this line runs as written: {Object.keys(MODES).map((k) => (. It happens in order, after the line above it and before the line below it.

 409 |               <option key={k} value={k}>{MODES[k].label}</option>
     | This draws one piece of the page while Mindfulness is showing.

 410 |             ))}
     | This ends Mindfulness (opened on line 273).

 411 |           </select>
     | This ends a drawing that Mindfulness started just above.

 412 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 413 |           {audioError && (
     | Inside Mindfulness, this line runs as written: {audioError && (. It happens in order, after the line above it and before the line below it.

 414 |             <div
     | This draws one piece of the page while Mindfulness is showing.

 415 |               style={{
     | Inside Mindfulness, this line runs as written: style={{. It happens in order, after the line above it and before the line below it.

 416 |                 padding: "10px 14px",
     | Inside Mindfulness, this line runs as written: padding: "10px 14px",. It happens in order, after the line above it and before the line below it.

 417 |                 background: "var(--red-dim)",
     | Inside Mindfulness, this line runs as written: background: "var(--red-dim)",. It happens in order, after the line above it and before the line below it.

 418 |                 color: "var(--red)",
     | Inside Mindfulness, this line runs as written: color: "var(--red)",. It happens in order, after the line above it and before the line below it.

 419 |                 borderRadius: "var(--radius-sm)",
     | Inside Mindfulness, this line runs as written: borderRadius: "var(--radius-sm)",. It happens in order, after the line above it and before the line below it.

 420 |                 fontSize: 13,
     | Inside Mindfulness, this line runs as written: fontSize: 13,. It happens in order, after the line above it and before the line below it.

 421 |                 marginBottom: 16,
     | Inside Mindfulness, this line runs as written: marginBottom: 16,. It happens in order, after the line above it and before the line below it.

 422 |               }}
     | This ends style={{ (opened on line 415).

 423 |             >
     | Inside Mindfulness, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 424 |               ⚠️ {audioError}
     | This ends Mindfulness (opened on line 273).

 425 |             </div>
     | This ends a drawing that Mindfulness started just above.

 426 |           )}
     | This ends Mindfulness (opened on line 273).

 427 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 428 |           <div className={`audio-player ${running ? "playing" : ""}`}>
     | This draws one piece of the page while Mindfulness is showing.

 429 |             <div className="audio-state-label">
     | This draws one piece of the page while Mindfulness is showing.

 430 |               {running ? "Session in progress" : "Ready to begin"}
     | This ends Mindfulness (opened on line 273).

 431 |             </div>
     | This ends a drawing that Mindfulness started just above.

 432 |             <div className="audio-time">{formatTime(currentTime)}</div>
     | This draws one piece of the page while Mindfulness is showing.

 433 |             {duration > 0 && (
     | Inside Mindfulness, this line runs as written: {duration > 0 && (. It happens in order, after the line above it and before the line below it.

 434 |               <div className="audio-duration">of {formatTime(duration)}</div>
     | This draws one piece of the page while Mindfulness is showing.

 435 |             )}
     | This ends Mindfulness (opened on line 273).

 436 |             <div className="audio-progress">
     | This draws one piece of the page while Mindfulness is showing.

 437 |               <div className="audio-progress-fill" style={{ width: `${progressPct}%` }} />
     | This draws one piece of the page while Mindfulness is showing.

 438 |             </div>
     | This ends a drawing that Mindfulness started just above.

 439 |           </div>
     | This ends a drawing that Mindfulness started just above.

 440 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 441 |           <audio ref={audioRef} src={MODES[mode].audioSrc} preload="metadata" />
     | This draws one piece of the page while Mindfulness is showing.

 442 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 443 |           <div className="flex gap-2 mt-4">
     | This draws one piece of the page while Mindfulness is showing.

 444 |             <button
     | This draws one piece of the page while Mindfulness is showing.

 445 |               className="btn btn-primary"
     | Inside Mindfulness, this line runs as written: className="btn btn-primary". It happens in order, after the line above it and before the line below it.

 446 |               onClick={() => setRunning(true)}
     | This decides what happens when you press.

 447 |               disabled={running || !!audioError}
     | This ends Mindfulness (opened on line 273).

 448 |             >
     | Inside Mindfulness, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 449 |               ▶ Start
     | Inside Mindfulness, this line runs as written: ▶ Start. It happens in order, after the line above it and before the line below it.

 450 |             </button>
     | This ends a drawing that Mindfulness started just above.

 451 |             <button
     | This draws one piece of the page while Mindfulness is showing.

 452 |               className="btn btn-ghost"
     | Inside Mindfulness, this line runs as written: className="btn btn-ghost". It happens in order, after the line above it and before the line below it.

 453 |               onClick={() => setRunning(false)}
     | This decides what happens when you press.

 454 |               disabled={!running}
     | This ends Mindfulness (opened on line 273).

 455 |             >
     | Inside Mindfulness, this line runs as written: >. It happens in order, after the line above it and before the line below it.

 456 |               ⏹ Stop
     | Inside Mindfulness, this line runs as written: ⏹ Stop. It happens in order, after the line above it and before the line below it.

 457 |             </button>
     | This ends a drawing that Mindfulness started just above.

 458 |           </div>
     | This ends a drawing that Mindfulness started just above.

 459 |         </div>
     | This ends a drawing that Mindfulness started just above.

 460 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 461 |         <aside className="stack">
     | This draws one piece of the page while Mindfulness is showing.

 462 |           <div className="card">
     | This draws one piece of the page while Mindfulness is showing.

 463 |             <div className="card-title">Affirmation</div>
     | This draws one piece of the page while Mindfulness is showing.

 464 |             <Affirmations ref={affirmRef} />
     | This draws one piece of the page while Mindfulness is showing.

 465 |           </div>
     | This ends a drawing that Mindfulness started just above.

 466 |         </aside>
     | This ends a drawing that Mindfulness started just above.

 467 |       </div>
     | This ends a drawing that Mindfulness started just above.

 468 |     </div>
     | This ends a drawing that Mindfulness started just above.

 469 |   );
     | This closes a box of instructions that opened above.

 470 | }
     | This ends Mindfulness (opened on line 273).

