# `src/utils/focusShield.js`

The source line is on the left of `|`. The explanation of that line is underneath it.

   1 | // Shared data + pure helpers for the Focus Shield (website blocking / whitelisting) feature.
     | Comment inside the top of the file. Not executed. It documents the next code: Shared data + pure helpers for the Focus Shield (website blocking / whitelisting) feature.

   2 | // Kept framework-free so it can be reused by the dashboard card, the Focus Timer session
     | Comment inside the top of the file. Not executed. It documents the next code: Kept framework-free so it can be reused by the dashboard card, the Focus Timer session

   3 | // panel, and the dedicated management page without duplicating logic.
     | Comment inside the top of the file. Not executed. It documents the next code: panel, and the dedicated management page without duplicating logic.

   4 | 
     | Blank line in `src/utils/focusShield.js` (pure rules for the Focus Shield, shared by several screens), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

   5 | export const CATEGORIES = [
     | Named export from pure rules for the Focus Shield, shared by several screens: `export const CATEGORIES = [`.

   6 |   "Social Media",
     | In `the top of the file` (src/utils/focusShield.js): statement `"Social Media",`. It runs when the top of the file runs, in order, before the next line of the same function.

   7 |   "Entertainment",
     | In `the top of the file` (src/utils/focusShield.js): statement `"Entertainment",`. It runs when the top of the file runs, in order, before the next line of the same function.

   8 |   "Gaming",
     | In `the top of the file` (src/utils/focusShield.js): statement `"Gaming",`. It runs when the top of the file runs, in order, before the next line of the same function.

   9 |   "Shopping",
     | In `the top of the file` (src/utils/focusShield.js): statement `"Shopping",`. It runs when the top of the file runs, in order, before the next line of the same function.

  10 |   "Streaming",
     | In `the top of the file` (src/utils/focusShield.js): statement `"Streaming",`. It runs when the top of the file runs, in order, before the next line of the same function.

  11 |   "News",
     | In `the top of the file` (src/utils/focusShield.js): statement `"News",`. It runs when the top of the file runs, in order, before the next line of the same function.

  12 |   "Custom",
     | In `the top of the file` (src/utils/focusShield.js): statement `"Custom",`. It runs when the top of the file runs, in order, before the next line of the same function.

  13 | ];
     | In `the top of the file` (src/utils/focusShield.js): statement `];`. It runs when the top of the file runs, in order, before the next line of the same function.

  14 | 
     | Blank line in `src/utils/focusShield.js` (pure rules for the Focus Shield, shared by several screens), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  15 | // The exact "popular suggestions" set — each maps to one or more matching domains so a
     | Comment inside the top of the file. Not executed. It documents the next code: The exact "popular suggestions" set — each maps to one or more matching domains so a

  16 | // user's existing custom entry (e.g. "twitter.com") still gets recognized as the same site.
     | Comment inside the top of the file. Not executed. It documents the next code: user's existing custom entry (e.g. "twitter.com") still gets recognized as the same site.

  17 | export const POPULAR_SITES = [
     | Named export from pure rules for the Focus Shield, shared by several screens: `export const POPULAR_SITES = [`.

  18 |   { id: "youtube", label: "YouTube", domain: "youtube.com", category: "Entertainment", emoji: "▶️" },
     | In `the top of the file` (src/utils/focusShield.js): `{ id: "youtube", label: "YouTube", domain: "youtube.com", category: "Entertainment", emoji: "▶️" },` closes the nearest open block. Names declared inside that block end here.

  19 |   { id: "reddit", label: "Reddit", domain: "reddit.com", category: "Social Media", emoji: "👽" },
     | In `the top of the file` (src/utils/focusShield.js): `{ id: "reddit", label: "Reddit", domain: "reddit.com", category: "Social Media", emoji: "👽" },` closes the nearest open block. Names declared inside that block end here.

  20 |   { id: "instagram", label: "Instagram", domain: "instagram.com", category: "Social Media", emoji: "📸" },
     | In `the top of the file` (src/utils/focusShield.js): `{ id: "instagram", label: "Instagram", domain: "instagram.com", category: "Social Media", emoji: "📸" },` closes the nearest open block. Names declared inside that block end here.

  21 |   { id: "facebook", label: "Facebook", domain: "facebook.com", category: "Social Media", emoji: "📘" },
     | In `the top of the file` (src/utils/focusShield.js): `{ id: "facebook", label: "Facebook", domain: "facebook.com", category: "Social Media", emoji: "📘" },` closes the nearest open block. Names declared inside that block end here.

  22 |   { id: "twitter", label: "Twitter / X", domain: "x.com", altDomains: ["twitter.com"], category: "Social Media", emoji: "🐦" },
     | In `the top of the file` (src/utils/focusShield.js): `{ id: "twitter", label: "Twitter / X", domain: "x.com", altDomains: ["twitter.com"], category: "Social Media", emoji: "🐦" },` closes the nearest open block. Names declared inside that block end here.

  23 |   { id: "discord", label: "Discord", domain: "discord.com", category: "Gaming", emoji: "🎮" },
     | In `the top of the file` (src/utils/focusShield.js): `{ id: "discord", label: "Discord", domain: "discord.com", category: "Gaming", emoji: "🎮" },` closes the nearest open block. Names declared inside that block end here.

  24 |   { id: "netflix", label: "Netflix", domain: "netflix.com", category: "Streaming", emoji: "🎬" },
     | In `the top of the file` (src/utils/focusShield.js): `{ id: "netflix", label: "Netflix", domain: "netflix.com", category: "Streaming", emoji: "🎬" },` closes the nearest open block. Names declared inside that block end here.

  25 |   { id: "primevideo", label: "Prime Video", domain: "primevideo.com", category: "Streaming", emoji: "📺" },
     | In `the top of the file` (src/utils/focusShield.js): `{ id: "primevideo", label: "Prime Video", domain: "primevideo.com", category: "Streaming", emoji: "📺" },` closes the nearest open block. Names declared inside that block end here.

  26 |   { id: "twitch", label: "Twitch", domain: "twitch.tv", category: "Gaming", emoji: "🕹️" },
     | In `the top of the file` (src/utils/focusShield.js): `{ id: "twitch", label: "Twitch", domain: "twitch.tv", category: "Gaming", emoji: "🕹️" },` closes the nearest open block. Names declared inside that block end here.

  27 | ];
     | In `the top of the file` (src/utils/focusShield.js): statement `];`. It runs when the top of the file runs, in order, before the next line of the same function.

  28 | 
     | Blank line in `src/utils/focusShield.js` (pure rules for the Focus Shield, shared by several screens), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  29 | export const PRESETS = [
     | Named export from pure rules for the Focus Shield, shared by several screens: `export const PRESETS = [`.

  30 |   {
     | In `the top of the file` (src/utils/focusShield.js): statement `{`. It runs when the top of the file runs, in order, before the next line of the same function.

  31 |     id: "student",
     | In `the top of the file` (src/utils/focusShield.js): statement `id: "student",`. It runs when the top of the file runs, in order, before the next line of the same function.

  32 |     label: "Student",
     | In `the top of the file` (src/utils/focusShield.js): statement `label: "Student",`. It runs when the top of the file runs, in order, before the next line of the same function.

  33 |     emoji: "🎓",
     | In `the top of the file` (src/utils/focusShield.js): statement `emoji: "🎓",`. It runs when the top of the file runs, in order, before the next line of the same function.

  34 |     description: "Block the usual social & video distractions during study time.",
     | In `the top of the file` (src/utils/focusShield.js): statement `description: "Block the usual social & video distractions during study time.",`. It runs when the top of the file runs, in order, before the next line of the same function.

  35 |     domains: ["instagram.com", "tiktok.com", "youtube.com", "reddit.com", "twitch.tv"],
     | In `the top of the file` (src/utils/focusShield.js): statement `domains: ["instagram.com", "tiktok.com", "youtube.com", "reddit.com", "twitch.tv"],`. It runs when the top of the file runs, in order, before the next line of the same function.

  36 |   },
     | In `the top of the file` (src/utils/focusShield.js): `},` closes { (opened on line 30). Names declared inside that block end here.

  37 |   {
     | In `the top of the file` (src/utils/focusShield.js): statement `{`. It runs when the top of the file runs, in order, before the next line of the same function.

  38 |     id: "developer",
     | In `the top of the file` (src/utils/focusShield.js): statement `id: "developer",`. It runs when the top of the file runs, in order, before the next line of the same function.

  39 |     label: "Developer",
     | In `the top of the file` (src/utils/focusShield.js): statement `label: "Developer",`. It runs when the top of the file runs, in order, before the next line of the same function.

  40 |     emoji: "💻",
     | In `the top of the file` (src/utils/focusShield.js): statement `emoji: "💻",`. It runs when the top of the file runs, in order, before the next line of the same function.

  41 |     description: "Block feeds and video, keep docs & Stack Overflow reachable.",
     | In `the top of the file` (src/utils/focusShield.js): statement `description: "Block feeds and video, keep docs & Stack Overflow reachable.",`. It runs when the top of the file runs, in order, before the next line of the same function.

  42 |     domains: ["reddit.com", "x.com", "youtube.com", "instagram.com", "facebook.com"],
     | In `the top of the file` (src/utils/focusShield.js): statement `domains: ["reddit.com", "x.com", "youtube.com", "instagram.com", "facebook.com"],`. It runs when the top of the file runs, in order, before the next line of the same function.

  43 |   },
     | In `the top of the file` (src/utils/focusShield.js): `},` closes { (opened on line 37). Names declared inside that block end here.

  44 |   {
     | In `the top of the file` (src/utils/focusShield.js): statement `{`. It runs when the top of the file runs, in order, before the next line of the same function.

  45 |     id: "remote-worker",
     | In `the top of the file` (src/utils/focusShield.js): statement `id: "remote-worker",`. It runs when the top of the file runs, in order, before the next line of the same function.

  46 |     label: "Remote Worker",
     | In `the top of the file` (src/utils/focusShield.js): statement `label: "Remote Worker",`. It runs when the top of the file runs, in order, before the next line of the same function.

  47 |     emoji: "🏠",
     | In `the top of the file` (src/utils/focusShield.js): statement `emoji: "🏠",`. It runs when the top of the file runs, in order, before the next line of the same function.

  48 |     description: "Block social media, news and shopping during work hours.",
     | In `the top of the file` (src/utils/focusShield.js): statement `description: "Block social media, news and shopping during work hours.",`. It runs when the top of the file runs, in order, before the next line of the same function.

  49 |     domains: ["facebook.com", "instagram.com", "x.com", "reddit.com", "amazon.com", "cnn.com"],
     | In `the top of the file` (src/utils/focusShield.js): statement `domains: ["facebook.com", "instagram.com", "x.com", "reddit.com", "amazon.com", "cnn.com"],`. It runs when the top of the file runs, in order, before the next line of the same function.

  50 |   },
     | In `the top of the file` (src/utils/focusShield.js): `},` closes { (opened on line 44). Names declared inside that block end here.

  51 |   {
     | In `the top of the file` (src/utils/focusShield.js): statement `{`. It runs when the top of the file runs, in order, before the next line of the same function.

  52 |     id: "deep-work",
     | In `the top of the file` (src/utils/focusShield.js): statement `id: "deep-work",`. It runs when the top of the file runs, in order, before the next line of the same function.

  53 |     label: "Deep Work",
     | In `the top of the file` (src/utils/focusShield.js): statement `label: "Deep Work",`. It runs when the top of the file runs, in order, before the next line of the same function.

  54 |     emoji: "🧠",
     | In `the top of the file` (src/utils/focusShield.js): statement `emoji: "🧠",`. It runs when the top of the file runs, in order, before the next line of the same function.

  55 |     description: "Block everything that isn't essential — maximum focus.",
     | In `the top of the file` (src/utils/focusShield.js): statement `description: "Block everything that isn't essential — maximum focus.",`. It runs when the top of the file runs, in order, before the next line of the same function.

  56 |     domains: [
     | In `the top of the file` (src/utils/focusShield.js): statement `domains: [`. It runs when the top of the file runs, in order, before the next line of the same function.

  57 |       "youtube.com", "reddit.com", "instagram.com", "facebook.com", "x.com",
     | In `the top of the file` (src/utils/focusShield.js): statement `"youtube.com", "reddit.com", "instagram.com", "facebook.com", "x.com",`. It runs when the top of the file runs, in order, before the next line of the same function.

  58 |       "discord.com", "netflix.com", "twitch.tv", "tiktok.com",
     | In `the top of the file` (src/utils/focusShield.js): statement `"discord.com", "netflix.com", "twitch.tv", "tiktok.com",`. It runs when the top of the file runs, in order, before the next line of the same function.

  59 |     ],
     | In `the top of the file` (src/utils/focusShield.js): statement `],`. It runs when the top of the file runs, in order, before the next line of the same function.

  60 |   },
     | In `the top of the file` (src/utils/focusShield.js): `},` closes { (opened on line 51). Names declared inside that block end here.

  61 |   {
     | In `the top of the file` (src/utils/focusShield.js): statement `{`. It runs when the top of the file runs, in order, before the next line of the same function.

  62 |     id: "exam-mode",
     | In `the top of the file` (src/utils/focusShield.js): statement `id: "exam-mode",`. It runs when the top of the file runs, in order, before the next line of the same function.

  63 |     label: "Exam Mode",
     | In `the top of the file` (src/utils/focusShield.js): statement `label: "Exam Mode",`. It runs when the top of the file runs, in order, before the next line of the same function.

  64 |     emoji: "📝",
     | In `the top of the file` (src/utils/focusShield.js): statement `emoji: "📝",`. It runs when the top of the file runs, in order, before the next line of the same function.

  65 |     description: "The most aggressive preset — blocks every common distraction.",
     | In `the top of the file` (src/utils/focusShield.js): statement `description: "The most aggressive preset — blocks every common distraction.",`. It runs when the top of the file runs, in order, before the next line of the same function.

  66 |     domains: [
     | In `the top of the file` (src/utils/focusShield.js): statement `domains: [`. It runs when the top of the file runs, in order, before the next line of the same function.

  67 |       "youtube.com", "instagram.com", "tiktok.com", "facebook.com", "x.com",
     | In `the top of the file` (src/utils/focusShield.js): statement `"youtube.com", "instagram.com", "tiktok.com", "facebook.com", "x.com",`. It runs when the top of the file runs, in order, before the next line of the same function.

  68 |       "reddit.com", "discord.com", "twitch.tv", "netflix.com", "primevideo.com",
     | In `the top of the file` (src/utils/focusShield.js): statement `"reddit.com", "discord.com", "twitch.tv", "netflix.com", "primevideo.com",`. It runs when the top of the file runs, in order, before the next line of the same function.

  69 |     ],
     | In `the top of the file` (src/utils/focusShield.js): statement `],`. It runs when the top of the file runs, in order, before the next line of the same function.

  70 |   },
     | In `the top of the file` (src/utils/focusShield.js): `},` closes { (opened on line 61). Names declared inside that block end here.

  71 | ];
     | In `the top of the file` (src/utils/focusShield.js): statement `];`. It runs when the top of the file runs, in order, before the next line of the same function.

  72 | 
     | Blank line in `src/utils/focusShield.js` (pure rules for the Focus Shield, shared by several screens), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  73 | const DOMAIN_RE = /^(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,63}$/i;
     | In `the top of the file` (src/utils/focusShield.js): `DOMAIN_RE`: Hostname check used by isValidDomain after normalizeDomain strips protocol and path. The code is `const DOMAIN_RE = /^(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,63}$/i;`.

  74 | 
     | Blank line in `src/utils/focusShield.js` (pure rules for the Focus Shield, shared by several screens), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  75 | // Strips protocol/path/query and a leading "www." so "https://www.reddit.com/r/x" -> "reddit.com"
     | Comment inside the top of the file. Not executed. It documents the next code: Strips protocol/path/query and a leading "www." so "https://www.reddit.com/r/x" -> "reddit.com"

  76 | export function normalizeDomain(input) {
     | Named export from pure rules for the Focus Shield, shared by several screens: `export function normalizeDomain(input) {`.

  77 |   if (!input) return "";
     | In `normalizeDomain` (src/utils/focusShield.js): branch `if (!input) return "";`. Only one side runs.

  78 |   let d = input.trim().toLowerCase();
     | In `normalizeDomain` (src/utils/focusShield.js): `d` is assigned `input.trim().toLowerCase();`. Later lines in this function read that name.

  79 |   d = d.replace(/^[a-z]+:\/\//, "");
     | In `normalizeDomain` (src/utils/focusShield.js): statement `d = d.replace(/^[a-z]+:\/\//, "");`. It runs when normalizeDomain runs, in order, before the next line of the same function.

  80 |   d = d.split("/")[0].split("?")[0].split("#")[0];
     | In `normalizeDomain` (src/utils/focusShield.js): statement `d = d.split("/")[0].split("?")[0].split("#")[0];`. It runs when normalizeDomain runs, in order, before the next line of the same function.

  81 |   d = d.replace(/^www\./, "");
     | In `normalizeDomain` (src/utils/focusShield.js): statement `d = d.replace(/^www\./, "");`. It runs when normalizeDomain runs, in order, before the next line of the same function.

  82 |   return d;
     | In `normalizeDomain` (src/utils/focusShield.js): return `return d;`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  83 | }
     | In `normalizeDomain` (src/utils/focusShield.js): `}` closes normalizeDomain (opened on line 76). Names declared inside that block end here.

  84 | 
     | Blank line in `src/utils/focusShield.js` (pure rules for the Focus Shield, shared by several screens), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  85 | export function isValidDomain(input) {
     | Named export from pure rules for the Focus Shield, shared by several screens: `export function isValidDomain(input) {`.

  86 |   const d = normalizeDomain(input);
     | In `isValidDomain` (src/utils/focusShield.js): `d` is assigned `normalizeDomain(input);`. Later lines in this function read that name.

  87 |   return DOMAIN_RE.test(d);
     | In `isValidDomain` (src/utils/focusShield.js): return `return DOMAIN_RE.test(d);`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  88 | }
     | In `isValidDomain` (src/utils/focusShield.js): `}` closes isValidDomain (opened on line 85). Names declared inside that block end here.

  89 | 
     | Blank line in `src/utils/focusShield.js` (pure rules for the Focus Shield, shared by several screens), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  90 | export function categoryForDomain(domain) {
     | Named export from pure rules for the Focus Shield, shared by several screens: `export function categoryForDomain(domain) {`.

  91 |   const d = normalizeDomain(domain);
     | In `categoryForDomain` (src/utils/focusShield.js): `d` is assigned `normalizeDomain(domain);`. Later lines in this function read that name.

  92 |   const site = POPULAR_SITES.find(
     | In `categoryForDomain` (src/utils/focusShield.js): `site` is assigned `POPULAR_SITES.find(`. Later lines in this function read that name.

  93 |     (s) => s.domain === d || (s.altDomains || []).includes(d)
     | In `categoryForDomain` (src/utils/focusShield.js): statement `(s) => s.domain === d || (s.altDomains || []).includes(d)`. It runs when categoryForDomain runs, in order, before the next line of the same function.

  94 |   );
     | In `categoryForDomain` (src/utils/focusShield.js): statement `);`. It runs when categoryForDomain runs, in order, before the next line of the same function.

  95 |   return site?.category || "Custom";
     | In `categoryForDomain` (src/utils/focusShield.js): return `return site?.category || "Custom";`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

  96 | }
     | In `categoryForDomain` (src/utils/focusShield.js): `}` closes categoryForDomain (opened on line 90). Names declared inside that block end here.

  97 | 
     | Blank line in `src/utils/focusShield.js` (pure rules for the Focus Shield, shared by several screens), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

  98 | // True while "now" falls inside the recurring blocking window.
     | Comment inside the top of the file. Not executed. It documents the next code: True while "now" falls inside the recurring blocking window.

  99 | export function isScheduleActiveNow(schedule) {
     | Named export from pure rules for the Focus Shield, shared by several screens: `export function isScheduleActiveNow(schedule) {`.

 100 |   if (!schedule?.enabled) return false;
     | In `isScheduleActiveNow` (src/utils/focusShield.js): branch `if (!schedule?.enabled) return false;`. Only one side runs.

 101 |   const now = new Date();
     | In `isScheduleActiveNow` (src/utils/focusShield.js): `now` is assigned `new Date();`. Later lines in this function read that name.

 102 |   const day = now.getDay();
     | In `isScheduleActiveNow` (src/utils/focusShield.js): `day` is assigned `now.getDay();`. Later lines in this function read that name.

 103 |   if (!Array.isArray(schedule.days) || !schedule.days.includes(day)) return false;
     | In `isScheduleActiveNow` (src/utils/focusShield.js): branch `if (!Array.isArray(schedule.days) || !schedule.days.includes(day)) return false;`. Only one side runs.

 104 |   const [sh, sm] = (schedule.startTime || "09:00").split(":").map(Number);
     | In `isScheduleActiveNow` (src/utils/focusShield.js): `sh, sm` is assigned `(schedule.startTime || "09:00").split(":").map(Number);`. Later lines in this function read that name.

 105 |   const [eh, em] = (schedule.endTime || "17:00").split(":").map(Number);
     | In `isScheduleActiveNow` (src/utils/focusShield.js): `eh, em` is assigned `(schedule.endTime || "17:00").split(":").map(Number);`. Later lines in this function read that name.

 106 |   const nowMins = now.getHours() * 60 + now.getMinutes();
     | In `isScheduleActiveNow` (src/utils/focusShield.js): `nowMins` is assigned `now.getHours() * 60 + now.getMinutes();`. Later lines in this function read that name.

 107 |   return nowMins >= sh * 60 + sm && nowMins < eh * 60 + em;
     | In `isScheduleActiveNow` (src/utils/focusShield.js): return `return nowMins >= sh * 60 + sm && nowMins < eh * 60 + em;`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

 108 | }
     | In `isScheduleActiveNow` (src/utils/focusShield.js): `}` closes isScheduleActiveNow (opened on line 99). Names declared inside that block end here.

 109 | 
     | Blank line in `src/utils/focusShield.js` (pure rules for the Focus Shield, shared by several screens), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

 110 | export function isPaused(rules) {
     | Named export from pure rules for the Focus Shield, shared by several screens: `export function isPaused(rules) {`.

 111 |   return !!(rules?.pausedUntil && new Date(rules.pausedUntil).getTime() > Date.now());
     | In `isPaused` (src/utils/focusShield.js): return `return !!(rules?.pausedUntil && new Date(rules.pausedUntil).getTime() > Date.now());`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

 112 | }
     | In `isPaused` (src/utils/focusShield.js): `}` closes isPaused (opened on line 110). Names declared inside that block end here.

 113 | 
     | Blank line in `src/utils/focusShield.js` (pure rules for the Focus Shield, shared by several screens), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

 114 | export const PAUSE_PRESETS = [
     | Named export from pure rules for the Focus Shield, shared by several screens: `export const PAUSE_PRESETS = [`.

 115 |   { id: "15m", label: "15 minutes", minutes: 15 },
     | In `the top of the file` (src/utils/focusShield.js): `{ id: "15m", label: "15 minutes", minutes: 15 },` closes the nearest open block. Names declared inside that block end here.

 116 |   { id: "30m", label: "30 minutes", minutes: 30 },
     | In `the top of the file` (src/utils/focusShield.js): `{ id: "30m", label: "30 minutes", minutes: 30 },` closes the nearest open block. Names declared inside that block end here.

 117 |   { id: "1h", label: "1 hour", minutes: 60 },
     | In `the top of the file` (src/utils/focusShield.js): `{ id: "1h", label: "1 hour", minutes: 60 },` closes the nearest open block. Names declared inside that block end here.

 118 |   { id: "tomorrow", label: "Until tomorrow" },
     | In `the top of the file` (src/utils/focusShield.js): `{ id: "tomorrow", label: "Until tomorrow" },` closes the nearest open block. Names declared inside that block end here.

 119 | ];
     | In `the top of the file` (src/utils/focusShield.js): statement `];`. It runs when the top of the file runs, in order, before the next line of the same function.

 120 | 
     | Blank line in `src/utils/focusShield.js` (pure rules for the Focus Shield, shared by several screens), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

 121 | export function computePauseUntil(presetId, customMinutes) {
     | Named export from pure rules for the Focus Shield, shared by several screens: `export function computePauseUntil(presetId, customMinutes) {`.

 122 |   if (presetId === "tomorrow") {
     | In `computePauseUntil` (src/utils/focusShield.js): branch `if (presetId === "tomorrow") {`. Only one side runs.

 123 |     const d = new Date();
     | In `computePauseUntil` (src/utils/focusShield.js): `d` is assigned `new Date();`. Later lines in this function read that name.

 124 |     d.setDate(d.getDate() + 1);
     | In `computePauseUntil` (src/utils/focusShield.js): statement `d.setDate(d.getDate() + 1);`. It runs when computePauseUntil runs, in order, before the next line of the same function.

 125 |     d.setHours(8, 0, 0, 0);
     | In `computePauseUntil` (src/utils/focusShield.js): statement `d.setHours(8, 0, 0, 0);`. It runs when computePauseUntil runs, in order, before the next line of the same function.

 126 |     return d;
     | In `computePauseUntil` (src/utils/focusShield.js): return `return d;`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

 127 |   }
     | In `computePauseUntil` (src/utils/focusShield.js): `}` closes if (presetId === "tomorrow") { (opened on line 122). Names declared inside that block end here.

 128 |   const preset = PAUSE_PRESETS.find((p) => p.id === presetId);
     | In `computePauseUntil` (src/utils/focusShield.js): `preset` is assigned `PAUSE_PRESETS.find((p) => p.id === presetId);`. Later lines in this function read that name.

 129 |   const minutes = preset?.minutes ?? customMinutes ?? 15;
     | In `computePauseUntil` (src/utils/focusShield.js): `minutes` is assigned `preset?.minutes ?? customMinutes ?? 15;`. Later lines in this function read that name.

 130 |   return new Date(Date.now() + minutes * 60 * 1000);
     | In `computePauseUntil` (src/utils/focusShield.js): return `return new Date(Date.now() + minutes * 60 * 1000);`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

 131 | }
     | In `computePauseUntil` (src/utils/focusShield.js): `}` closes computePauseUntil (opened on line 121). Names declared inside that block end here.

 132 | 
     | Blank line in `src/utils/focusShield.js` (pure rules for the Focus Shield, shared by several screens), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

 133 | export function formatClockTime(date) {
     | Named export from pure rules for the Focus Shield, shared by several screens: `export function formatClockTime(date) {`.

 134 |   if (!date) return "";
     | In `formatClockTime` (src/utils/focusShield.js): branch `if (!date) return "";`. Only one side runs.

 135 |   const d = date instanceof Date ? date : new Date(date);
     | In `formatClockTime` (src/utils/focusShield.js): `d` is assigned `date instanceof Date ? date : new Date(date);`. Later lines in this function read that name.

 136 |   return d.toLocaleTimeString(undefined, { hour: "numeric", minute: "2-digit" });
     | In `formatClockTime` (src/utils/focusShield.js): return `return d.toLocaleTimeString(undefined, { hour: "numeric", minute: "2-digit" });`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

 137 | }
     | In `formatClockTime` (src/utils/focusShield.js): `}` closes formatClockTime (opened on line 133). Names declared inside that block end here.

 138 | 
     | Blank line in `src/utils/focusShield.js` (pure rules for the Focus Shield, shared by several screens), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

 139 | // The single source of truth for "what is the shield actually doing right now" — reused by
     | Comment inside the top of the file. Not executed. It documents the next code: The single source of truth for "what is the shield actually doing right now" — reused by

 140 | // the dashboard card, the Focus Timer session panel and the Focus Shield page header so the
     | Comment inside the top of the file. Not executed. It documents the next code: the dashboard card, the Focus Timer session panel and the Focus Shield page header so the

 141 | // status never disagrees between screens.
     | Comment inside the top of the file. Not executed. It documents the next code: status never disagrees between screens.

 142 | export function getShieldStatus(rules, sessionActive = false) {
     | Named export from pure rules for the Focus Shield, shared by several screens: `export function getShieldStatus(rules, sessionActive = false) {`.

 143 |   if (!rules?.isEnabled) {
     | In `getShieldStatus` (src/utils/focusShield.js): branch `if (!rules?.isEnabled) {`. Only one side runs.

 144 |     return {
     | In `getShieldStatus` (src/utils/focusShield.js): return `return {`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

 145 |       level: "off",
     | In `getShieldStatus` (src/utils/focusShield.js): statement `level: "off",`. It runs when getShieldStatus runs, in order, before the next line of the same function.

 146 |       label: "Off",
     | In `getShieldStatus` (src/utils/focusShield.js): statement `label: "Off",`. It runs when getShieldStatus runs, in order, before the next line of the same function.

 147 |       description: "Turn on Focus Shield to start guarding your focus.",
     | In `getShieldStatus` (src/utils/focusShield.js): statement `description: "Turn on Focus Shield to start guarding your focus.",`. It runs when getShieldStatus runs, in order, before the next line of the same function.

 148 |     };
     | In `getShieldStatus` (src/utils/focusShield.js): `};` closes return { (opened on line 144). Names declared inside that block end here.

 149 |   }
     | In `getShieldStatus` (src/utils/focusShield.js): `}` closes if (!rules?.isEnabled) { (opened on line 143). Names declared inside that block end here.

 150 |   if (isPaused(rules)) {
     | In `getShieldStatus` (src/utils/focusShield.js): branch `if (isPaused(rules)) {`. Only one side runs.

 151 |     return {
     | In `getShieldStatus` (src/utils/focusShield.js): return `return {`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

 152 |       level: "paused",
     | In `getShieldStatus` (src/utils/focusShield.js): statement `level: "paused",`. It runs when getShieldStatus runs, in order, before the next line of the same function.

 153 |       label: "Paused",
     | In `getShieldStatus` (src/utils/focusShield.js): statement `label: "Paused",`. It runs when getShieldStatus runs, in order, before the next line of the same function.

 154 |       description: `Resumes at ${formatClockTime(rules.pausedUntil)}`,
     | In `getShieldStatus` (src/utils/focusShield.js): `description: `Resumes at ${formatClockTime(rules.pausedUntil)}`,` closes return { (opened on line 151). Names declared inside that block end here.

 155 |     };
     | In `getShieldStatus` (src/utils/focusShield.js): `};` closes return { (opened on line 151). Names declared inside that block end here.

 156 |   }
     | In `getShieldStatus` (src/utils/focusShield.js): `}` closes if (isPaused(rules)) { (opened on line 150). Names declared inside that block end here.

 157 |   if (sessionActive) {
     | In `getShieldStatus` (src/utils/focusShield.js): branch `if (sessionActive) {`. Only one side runs.

 158 |     return {
     | In `getShieldStatus` (src/utils/focusShield.js): return `return {`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

 159 |       level: "active",
     | In `getShieldStatus` (src/utils/focusShield.js): statement `level: "active",`. It runs when getShieldStatus runs, in order, before the next line of the same function.

 160 |       label: "Blocking now",
     | In `getShieldStatus` (src/utils/focusShield.js): statement `label: "Blocking now",`. It runs when getShieldStatus runs, in order, before the next line of the same function.

 161 |       description: "Focus session in progress",
     | In `getShieldStatus` (src/utils/focusShield.js): statement `description: "Focus session in progress",`. It runs when getShieldStatus runs, in order, before the next line of the same function.

 162 |     };
     | In `getShieldStatus` (src/utils/focusShield.js): `};` closes return { (opened on line 158). Names declared inside that block end here.

 163 |   }
     | In `getShieldStatus` (src/utils/focusShield.js): `}` closes if (sessionActive) { (opened on line 157). Names declared inside that block end here.

 164 |   if (isScheduleActiveNow(rules.schedule)) {
     | In `getShieldStatus` (src/utils/focusShield.js): branch `if (isScheduleActiveNow(rules.schedule)) {`. Only one side runs.

 165 |     return {
     | In `getShieldStatus` (src/utils/focusShield.js): return `return {`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

 166 |       level: "active",
     | In `getShieldStatus` (src/utils/focusShield.js): statement `level: "active",`. It runs when getShieldStatus runs, in order, before the next line of the same function.

 167 |       label: "Blocking now",
     | In `getShieldStatus` (src/utils/focusShield.js): statement `label: "Blocking now",`. It runs when getShieldStatus runs, in order, before the next line of the same function.

 168 |       description: "Scheduled block window is active",
     | In `getShieldStatus` (src/utils/focusShield.js): statement `description: "Scheduled block window is active",`. It runs when getShieldStatus runs, in order, before the next line of the same function.

 169 |     };
     | In `getShieldStatus` (src/utils/focusShield.js): `};` closes return { (opened on line 165). Names declared inside that block end here.

 170 |   }
     | In `getShieldStatus` (src/utils/focusShield.js): `}` closes if (isScheduleActiveNow(rules.schedule)) (opened on line 164). Names declared inside that block end here.

 171 |   return {
     | In `getShieldStatus` (src/utils/focusShield.js): return `return {`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

 172 |     level: "armed",
     | In `getShieldStatus` (src/utils/focusShield.js): statement `level: "armed",`. It runs when getShieldStatus runs, in order, before the next line of the same function.

 173 |     label: "Armed",
     | In `getShieldStatus` (src/utils/focusShield.js): statement `label: "Armed",`. It runs when getShieldStatus runs, in order, before the next line of the same function.

 174 |     description: "Will block during your next focus session",
     | In `getShieldStatus` (src/utils/focusShield.js): statement `description: "Will block during your next focus session",`. It runs when getShieldStatus runs, in order, before the next line of the same function.

 175 |   };
     | In `getShieldStatus` (src/utils/focusShield.js): `};` closes return { (opened on line 171). Names declared inside that block end here.

 176 | }
     | In `getShieldStatus` (src/utils/focusShield.js): `}` closes getShieldStatus (opened on line 142). Names declared inside that block end here.

 177 | 
     | Blank line in `src/utils/focusShield.js` (pure rules for the Focus Shield, shared by several screens), inside the top of the file. The parser skips it. It separates the previous statement from the next so the function is readable.

 178 | // Adds domains to an existing entry list without creating duplicates.
     | Comment inside the top of the file. Not executed. It documents the next code: Adds domains to an existing entry list without creating duplicates.

 179 | export function mergeDomains(existing, domainsOrEntries) {
     | Named export from pure rules for the Focus Shield, shared by several screens: `export function mergeDomains(existing, domainsOrEntries) {`.

 180 |   const have = new Set(existing.map((e) => e.value));
     | In `mergeDomains` (src/utils/focusShield.js): `have` is assigned `new Set(existing.map((e) => e.value));`. Later lines in this function read that name.

 181 |   const additions = domainsOrEntries
     | In `mergeDomains` (src/utils/focusShield.js): `additions` is assigned `domainsOrEntries`. Later lines in this function read that name.

 182 |     .map((d) => (typeof d === "string" ? { value: normalizeDomain(d), label: "" } : d))
     | In `mergeDomains` (src/utils/focusShield.js): iteration `.map((d) => (typeof d === "string" ? { value: normalizeDomain(d), label: "" } : d))`.

 183 |     .filter((e) => e.value && !have.has(e.value));
     | In `mergeDomains` (src/utils/focusShield.js): iteration `.filter((e) => e.value && !have.has(e.value));`.

 184 |   additions.forEach((e) => have.add(e.value));
     | In `mergeDomains` (src/utils/focusShield.js): iteration `additions.forEach((e) => have.add(e.value));`.

 185 |   return [...existing, ...additions.map((e) => ({ enabled: true, ...e }))];
     | In `mergeDomains` (src/utils/focusShield.js): return `return [...existing, ...additions.map((e) => ({ enabled: true, ...e }))];`. Control goes back to the caller with this value. A JSX return is what React commits to the DOM.

 186 | }
     | In `mergeDomains` (src/utils/focusShield.js): `}` closes mergeDomains (opened on line 179). Names declared inside that block end here.

