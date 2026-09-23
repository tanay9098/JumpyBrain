# `src/utils/focusShield.js`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | // Shared data + pure helpers for the Focus Shield (website blocking / whitelisting) feature.
     | A note written for people. The app does not run it.

   2 | // Kept framework-free so it can be reused by the dashboard card, the Focus Timer session
     | A note written for people. The app does not run it.

   3 | // panel, and the dedicated management page without duplicating logic.
     | A note written for people. The app does not run it.

   4 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

   5 | export const CATEGORIES = [
     | This lets another file use this piece by its name.

   6 |   "Social Media",
     | Inside the top of the file, this line runs as written: "Social Media",. It happens in order, after the line above it and before the line below it.

   7 |   "Entertainment",
     | Inside the top of the file, this line runs as written: "Entertainment",. It happens in order, after the line above it and before the line below it.

   8 |   "Gaming",
     | Inside the top of the file, this line runs as written: "Gaming",. It happens in order, after the line above it and before the line below it.

   9 |   "Shopping",
     | Inside the top of the file, this line runs as written: "Shopping",. It happens in order, after the line above it and before the line below it.

  10 |   "Streaming",
     | Inside the top of the file, this line runs as written: "Streaming",. It happens in order, after the line above it and before the line below it.

  11 |   "News",
     | Inside the top of the file, this line runs as written: "News",. It happens in order, after the line above it and before the line below it.

  12 |   "Custom",
     | Inside the top of the file, this line runs as written: "Custom",. It happens in order, after the line above it and before the line below it.

  13 | ];
     | Inside the top of the file, this line runs as written: ];. It happens in order, after the line above it and before the line below it.

  14 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  15 | // The exact "popular suggestions" set — each maps to one or more matching domains so a
     | A note written for people. The app does not run it.

  16 | // user's existing custom entry (e.g. "twitter.com") still gets recognized as the same site.
     | A note written for people. The app does not run it.

  17 | export const POPULAR_SITES = [
     | This lets another file use this piece by its name.

  18 |   { id: "youtube", label: "YouTube", domain: "youtube.com", category: "Entertainment", emoji: "▶️" },
     | This ends the nearest open block.

  19 |   { id: "reddit", label: "Reddit", domain: "reddit.com", category: "Social Media", emoji: "👽" },
     | This ends the nearest open block.

  20 |   { id: "instagram", label: "Instagram", domain: "instagram.com", category: "Social Media", emoji: "📸" },
     | This ends the nearest open block.

  21 |   { id: "facebook", label: "Facebook", domain: "facebook.com", category: "Social Media", emoji: "📘" },
     | This ends the nearest open block.

  22 |   { id: "twitter", label: "Twitter / X", domain: "x.com", altDomains: ["twitter.com"], category: "Social Media", emoji: "🐦" },
     | This ends the nearest open block.

  23 |   { id: "discord", label: "Discord", domain: "discord.com", category: "Gaming", emoji: "🎮" },
     | This ends the nearest open block.

  24 |   { id: "netflix", label: "Netflix", domain: "netflix.com", category: "Streaming", emoji: "🎬" },
     | This ends the nearest open block.

  25 |   { id: "primevideo", label: "Prime Video", domain: "primevideo.com", category: "Streaming", emoji: "📺" },
     | This ends the nearest open block.

  26 |   { id: "twitch", label: "Twitch", domain: "twitch.tv", category: "Gaming", emoji: "🕹️" },
     | This ends the nearest open block.

  27 | ];
     | Inside the top of the file, this line runs as written: ];. It happens in order, after the line above it and before the line below it.

  28 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  29 | export const PRESETS = [
     | This lets another file use this piece by its name.

  30 |   {
     | Inside the top of the file, this line runs as written: {. It happens in order, after the line above it and before the line below it.

  31 |     id: "student",
     | Inside the top of the file, this line runs as written: id: "student",. It happens in order, after the line above it and before the line below it.

  32 |     label: "Student",
     | Inside the top of the file, this line runs as written: label: "Student",. It happens in order, after the line above it and before the line below it.

  33 |     emoji: "🎓",
     | Inside the top of the file, this line runs as written: emoji: "🎓",. It happens in order, after the line above it and before the line below it.

  34 |     description: "Block the usual social & video distractions during study time.",
     | Inside the top of the file, this line runs as written: description: "Block the usual social & video distractions during study time.",. It happens in order, after the line above it and before the line below it.

  35 |     domains: ["instagram.com", "tiktok.com", "youtube.com", "reddit.com", "twitch.tv"],
     | Inside the top of the file, this line runs as written: domains: ["instagram.com", "tiktok.com", "youtube.com", "reddit.com", "twitch.tv"],. It happens in order, after the line above it and before the line below it.

  36 |   },
     | This ends { (opened on line 30).

  37 |   {
     | Inside the top of the file, this line runs as written: {. It happens in order, after the line above it and before the line below it.

  38 |     id: "developer",
     | Inside the top of the file, this line runs as written: id: "developer",. It happens in order, after the line above it and before the line below it.

  39 |     label: "Developer",
     | Inside the top of the file, this line runs as written: label: "Developer",. It happens in order, after the line above it and before the line below it.

  40 |     emoji: "💻",
     | Inside the top of the file, this line runs as written: emoji: "💻",. It happens in order, after the line above it and before the line below it.

  41 |     description: "Block feeds and video, keep docs & Stack Overflow reachable.",
     | Inside the top of the file, this line runs as written: description: "Block feeds and video, keep docs & Stack Overflow reachable.",. It happens in order, after the line above it and before the line below it.

  42 |     domains: ["reddit.com", "x.com", "youtube.com", "instagram.com", "facebook.com"],
     | Inside the top of the file, this line runs as written: domains: ["reddit.com", "x.com", "youtube.com", "instagram.com", "facebook.com"],. It happens in order, after the line above it and before the line below it.

  43 |   },
     | This ends { (opened on line 37).

  44 |   {
     | Inside the top of the file, this line runs as written: {. It happens in order, after the line above it and before the line below it.

  45 |     id: "remote-worker",
     | Inside the top of the file, this line runs as written: id: "remote-worker",. It happens in order, after the line above it and before the line below it.

  46 |     label: "Remote Worker",
     | Inside the top of the file, this line runs as written: label: "Remote Worker",. It happens in order, after the line above it and before the line below it.

  47 |     emoji: "🏠",
     | Inside the top of the file, this line runs as written: emoji: "🏠",. It happens in order, after the line above it and before the line below it.

  48 |     description: "Block social media, news and shopping during work hours.",
     | Inside the top of the file, this line runs as written: description: "Block social media, news and shopping during work hours.",. It happens in order, after the line above it and before the line below it.

  49 |     domains: ["facebook.com", "instagram.com", "x.com", "reddit.com", "amazon.com", "cnn.com"],
     | Inside the top of the file, this line runs as written: domains: ["facebook.com", "instagram.com", "x.com", "reddit.com", "amazon.com", "cnn.com"],. It happens in order, after the line above it and before the line below it.

  50 |   },
     | This ends { (opened on line 44).

  51 |   {
     | Inside the top of the file, this line runs as written: {. It happens in order, after the line above it and before the line below it.

  52 |     id: "deep-work",
     | Inside the top of the file, this line runs as written: id: "deep-work",. It happens in order, after the line above it and before the line below it.

  53 |     label: "Deep Work",
     | Inside the top of the file, this line runs as written: label: "Deep Work",. It happens in order, after the line above it and before the line below it.

  54 |     emoji: "🧠",
     | Inside the top of the file, this line runs as written: emoji: "🧠",. It happens in order, after the line above it and before the line below it.

  55 |     description: "Block everything that isn't essential — maximum focus.",
     | Inside the top of the file, this line runs as written: description: "Block everything that isn't essential — maximum focus.",. It happens in order, after the line above it and before the line below it.

  56 |     domains: [
     | Inside the top of the file, this line runs as written: domains: [. It happens in order, after the line above it and before the line below it.

  57 |       "youtube.com", "reddit.com", "instagram.com", "facebook.com", "x.com",
     | Inside the top of the file, this line runs as written: "youtube.com", "reddit.com", "instagram.com", "facebook.com", "x.com",. It happens in order, after the line above it and before the line below it.

  58 |       "discord.com", "netflix.com", "twitch.tv", "tiktok.com",
     | Inside the top of the file, this line runs as written: "discord.com", "netflix.com", "twitch.tv", "tiktok.com",. It happens in order, after the line above it and before the line below it.

  59 |     ],
     | Inside the top of the file, this line runs as written: ],. It happens in order, after the line above it and before the line below it.

  60 |   },
     | This ends { (opened on line 51).

  61 |   {
     | Inside the top of the file, this line runs as written: {. It happens in order, after the line above it and before the line below it.

  62 |     id: "exam-mode",
     | Inside the top of the file, this line runs as written: id: "exam-mode",. It happens in order, after the line above it and before the line below it.

  63 |     label: "Exam Mode",
     | Inside the top of the file, this line runs as written: label: "Exam Mode",. It happens in order, after the line above it and before the line below it.

  64 |     emoji: "📝",
     | Inside the top of the file, this line runs as written: emoji: "📝",. It happens in order, after the line above it and before the line below it.

  65 |     description: "The most aggressive preset — blocks every common distraction.",
     | Inside the top of the file, this line runs as written: description: "The most aggressive preset — blocks every common distraction.",. It happens in order, after the line above it and before the line below it.

  66 |     domains: [
     | Inside the top of the file, this line runs as written: domains: [. It happens in order, after the line above it and before the line below it.

  67 |       "youtube.com", "instagram.com", "tiktok.com", "facebook.com", "x.com",
     | Inside the top of the file, this line runs as written: "youtube.com", "instagram.com", "tiktok.com", "facebook.com", "x.com",. It happens in order, after the line above it and before the line below it.

  68 |       "reddit.com", "discord.com", "twitch.tv", "netflix.com", "primevideo.com",
     | Inside the top of the file, this line runs as written: "reddit.com", "discord.com", "twitch.tv", "netflix.com", "primevideo.com",. It happens in order, after the line above it and before the line below it.

  69 |     ],
     | Inside the top of the file, this line runs as written: ],. It happens in order, after the line above it and before the line below it.

  70 |   },
     | This ends { (opened on line 61).

  71 | ];
     | Inside the top of the file, this line runs as written: ];. It happens in order, after the line above it and before the line below it.

  72 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  73 | const DOMAIN_RE = /^(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,63}$/i;
     | Hostname check used by isValidDomain after normalizeDomain strips protocol and path.

  74 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  75 | // Strips protocol/path/query and a leading "www." so "https://www.reddit.com/r/x" -> "reddit.com"
     | A note written for people. The app does not run it.

  76 | export function normalizeDomain(input) {
     | This lets another file use this piece by its name.

  77 |   if (!input) return "";
     | This asks a yes-or-no question. The next bit runs only on yes.

  78 |   let d = input.trim().toLowerCase();
     | This gives a short name to a value so the rest of normalizeDomain can use it.

  79 |   d = d.replace(/^[a-z]+:\/\//, "");
     | Inside normalizeDomain, this line runs as written: d = d.replace(/^[a-z]+:\/\//, "");. It happens in order, after the line above it and before the line below it.

  80 |   d = d.split("/")[0].split("?")[0].split("#")[0];
     | Inside normalizeDomain, this line runs as written: d = d.split("/")[0].split("?")[0].split("#")[0];. It happens in order, after the line above it and before the line below it.

  81 |   d = d.replace(/^www\./, "");
     | Inside normalizeDomain, this line runs as written: d = d.replace(/^www\./, "");. It happens in order, after the line above it and before the line below it.

  82 |   return d;
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  83 | }
     | This ends normalizeDomain (opened on line 76).

  84 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  85 | export function isValidDomain(input) {
     | This lets another file use this piece by its name.

  86 |   const d = normalizeDomain(input);
     | This gives a short name to a value so the rest of isValidDomain can use it.

  87 |   return DOMAIN_RE.test(d);
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  88 | }
     | This ends isValidDomain (opened on line 85).

  89 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  90 | export function categoryForDomain(domain) {
     | This lets another file use this piece by its name.

  91 |   const d = normalizeDomain(domain);
     | This gives a short name to a value so the rest of categoryForDomain can use it.

  92 |   const site = POPULAR_SITES.find(
     | This gives a short name to a value so the rest of categoryForDomain can use it.

  93 |     (s) => s.domain === d || (s.altDomains || []).includes(d)
     | Inside categoryForDomain, this line runs as written: (s) => s.domain === d || (s.altDomains || []).includes(d). It happens in order, after the line above it and before the line below it.

  94 |   );
     | This closes a box of instructions that opened above.

  95 |   return site?.category || "Custom";
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

  96 | }
     | This ends categoryForDomain (opened on line 90).

  97 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

  98 | // True while "now" falls inside the recurring blocking window.
     | A note written for people. The app does not run it.

  99 | export function isScheduleActiveNow(schedule) {
     | This lets another file use this piece by its name.

 100 |   if (!schedule?.enabled) return false;
     | This asks a yes-or-no question. The next bit runs only on yes.

 101 |   const now = new Date();
     | This gives a short name to a value so the rest of isScheduleActiveNow can use it.

 102 |   const day = now.getDay();
     | This gives a short name to a value so the rest of isScheduleActiveNow can use it.

 103 |   if (!Array.isArray(schedule.days) || !schedule.days.includes(day)) return false;
     | This asks a yes-or-no question. The next bit runs only on yes.

 104 |   const [sh, sm] = (schedule.startTime || "09:00").split(":").map(Number);
     | This gives a short name to a value so the rest of isScheduleActiveNow can use it.

 105 |   const [eh, em] = (schedule.endTime || "17:00").split(":").map(Number);
     | This gives a short name to a value so the rest of isScheduleActiveNow can use it.

 106 |   const nowMins = now.getHours() * 60 + now.getMinutes();
     | This gives a short name to a value so the rest of isScheduleActiveNow can use it.

 107 |   return nowMins >= sh * 60 + sm && nowMins < eh * 60 + em;
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

 108 | }
     | This ends isScheduleActiveNow (opened on line 99).

 109 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 110 | export function isPaused(rules) {
     | This lets another file use this piece by its name.

 111 |   return !!(rules?.pausedUntil && new Date(rules.pausedUntil).getTime() > Date.now());
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

 112 | }
     | This ends isPaused (opened on line 110).

 113 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 114 | export const PAUSE_PRESETS = [
     | This lets another file use this piece by its name.

 115 |   { id: "15m", label: "15 minutes", minutes: 15 },
     | This ends the nearest open block.

 116 |   { id: "30m", label: "30 minutes", minutes: 30 },
     | This ends the nearest open block.

 117 |   { id: "1h", label: "1 hour", minutes: 60 },
     | This ends the nearest open block.

 118 |   { id: "tomorrow", label: "Until tomorrow" },
     | This ends the nearest open block.

 119 | ];
     | Inside the top of the file, this line runs as written: ];. It happens in order, after the line above it and before the line below it.

 120 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 121 | export function computePauseUntil(presetId, customMinutes) {
     | This lets another file use this piece by its name.

 122 |   if (presetId === "tomorrow") {
     | This asks a yes-or-no question. The next bit runs only on yes.

 123 |     const d = new Date();
     | This gives a short name to a value so the rest of computePauseUntil can use it.

 124 |     d.setDate(d.getDate() + 1);
     | Inside computePauseUntil, this line runs as written: d.setDate(d.getDate() + 1);. It happens in order, after the line above it and before the line below it.

 125 |     d.setHours(8, 0, 0, 0);
     | Inside computePauseUntil, this line runs as written: d.setHours(8, 0, 0, 0);. It happens in order, after the line above it and before the line below it.

 126 |     return d;
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

 127 |   }
     | This ends if (presetId === "tomorrow") { (opened on line 122).

 128 |   const preset = PAUSE_PRESETS.find((p) => p.id === presetId);
     | This gives a short name to a value so the rest of computePauseUntil can use it.

 129 |   const minutes = preset?.minutes ?? customMinutes ?? 15;
     | This gives a short name to a value so the rest of computePauseUntil can use it.

 130 |   return new Date(Date.now() + minutes * 60 * 1000);
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

 131 | }
     | This ends computePauseUntil (opened on line 121).

 132 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 133 | export function formatClockTime(date) {
     | This lets another file use this piece by its name.

 134 |   if (!date) return "";
     | This asks a yes-or-no question. The next bit runs only on yes.

 135 |   const d = date instanceof Date ? date : new Date(date);
     | This gives a short name to a value so the rest of formatClockTime can use it.

 136 |   return d.toLocaleTimeString(undefined, { hour: "numeric", minute: "2-digit" });
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

 137 | }
     | This ends formatClockTime (opened on line 133).

 138 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 139 | // The single source of truth for "what is the shield actually doing right now" — reused by
     | A note written for people. The app does not run it.

 140 | // the dashboard card, the Focus Timer session panel and the Focus Shield page header so the
     | A note written for people. The app does not run it.

 141 | // status never disagrees between screens.
     | A note written for people. The app does not run it.

 142 | export function getShieldStatus(rules, sessionActive = false) {
     | This lets another file use this piece by its name.

 143 |   if (!rules?.isEnabled) {
     | This asks a yes-or-no question. The next bit runs only on yes.

 144 |     return {
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

 145 |       level: "off",
     | Inside getShieldStatus, this line runs as written: level: "off",. It happens in order, after the line above it and before the line below it.

 146 |       label: "Off",
     | Inside getShieldStatus, this line runs as written: label: "Off",. It happens in order, after the line above it and before the line below it.

 147 |       description: "Turn on Focus Shield to start guarding your focus.",
     | Inside getShieldStatus, this line runs as written: description: "Turn on Focus Shield to start guarding your focus.",. It happens in order, after the line above it and before the line below it.

 148 |     };
     | This ends return { (opened on line 144).

 149 |   }
     | This ends if (!rules?.isEnabled) { (opened on line 143).

 150 |   if (isPaused(rules)) {
     | This asks a yes-or-no question. The next bit runs only on yes.

 151 |     return {
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

 152 |       level: "paused",
     | Inside getShieldStatus, this line runs as written: level: "paused",. It happens in order, after the line above it and before the line below it.

 153 |       label: "Paused",
     | Inside getShieldStatus, this line runs as written: label: "Paused",. It happens in order, after the line above it and before the line below it.

 154 |       description: `Resumes at ${formatClockTime(rules.pausedUntil)}`,
     | This ends return { (opened on line 151).

 155 |     };
     | This ends return { (opened on line 151).

 156 |   }
     | This ends if (isPaused(rules)) { (opened on line 150).

 157 |   if (sessionActive) {
     | This asks a yes-or-no question. The next bit runs only on yes.

 158 |     return {
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

 159 |       level: "active",
     | Inside getShieldStatus, this line runs as written: level: "active",. It happens in order, after the line above it and before the line below it.

 160 |       label: "Blocking now",
     | Inside getShieldStatus, this line runs as written: label: "Blocking now",. It happens in order, after the line above it and before the line below it.

 161 |       description: "Focus session in progress",
     | Inside getShieldStatus, this line runs as written: description: "Focus session in progress",. It happens in order, after the line above it and before the line below it.

 162 |     };
     | This ends return { (opened on line 158).

 163 |   }
     | This ends if (sessionActive) { (opened on line 157).

 164 |   if (isScheduleActiveNow(rules.schedule)) {
     | This asks a yes-or-no question. The next bit runs only on yes.

 165 |     return {
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

 166 |       level: "active",
     | Inside getShieldStatus, this line runs as written: level: "active",. It happens in order, after the line above it and before the line below it.

 167 |       label: "Blocking now",
     | Inside getShieldStatus, this line runs as written: label: "Blocking now",. It happens in order, after the line above it and before the line below it.

 168 |       description: "Scheduled block window is active",
     | Inside getShieldStatus, this line runs as written: description: "Scheduled block window is active",. It happens in order, after the line above it and before the line below it.

 169 |     };
     | This ends return { (opened on line 165).

 170 |   }
     | This ends if (isScheduleActiveNow(rules.schedule)) (opened on line 164).

 171 |   return {
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

 172 |     level: "armed",
     | Inside getShieldStatus, this line runs as written: level: "armed",. It happens in order, after the line above it and before the line below it.

 173 |     label: "Armed",
     | Inside getShieldStatus, this line runs as written: label: "Armed",. It happens in order, after the line above it and before the line below it.

 174 |     description: "Will block during your next focus session",
     | Inside getShieldStatus, this line runs as written: description: "Will block during your next focus session",. It happens in order, after the line above it and before the line below it.

 175 |   };
     | This ends return { (opened on line 171).

 176 | }
     | This ends getShieldStatus (opened on line 142).

 177 | 
     | A blank line inside the current job. The app skips it. It is only space so the writing is not cramped.

 178 | // Adds domains to an existing entry list without creating duplicates.
     | A note written for people. The app does not run it.

 179 | export function mergeDomains(existing, domainsOrEntries) {
     | This lets another file use this piece by its name.

 180 |   const have = new Set(existing.map((e) => e.value));
     | This gives a short name to a value so the rest of mergeDomains can use it.

 181 |   const additions = domainsOrEntries
     | This gives a short name to a value so the rest of mergeDomains can use it.

 182 |     .map((d) => (typeof d === "string" ? { value: normalizeDomain(d), label: "" } : d))
     | This ends mergeDomains (opened on line 179).

 183 |     .filter((e) => e.value && !have.has(e.value));
     | Inside mergeDomains, this line runs as written: .filter((e) => e.value && !have.has(e.value));. It happens in order, after the line above it and before the line below it.

 184 |   additions.forEach((e) => have.add(e.value));
     | Inside mergeDomains, this line runs as written: additions.forEach((e) => have.add(e.value));. It happens in order, after the line above it and before the line below it.

 185 |   return [...existing, ...additions.map((e) => ({ enabled: true, ...e }))];
     | This is the answer the function gives back. If it looks like a picture tag, that picture is what you see.

 186 | }
     | This ends mergeDomains (opened on line 179).

