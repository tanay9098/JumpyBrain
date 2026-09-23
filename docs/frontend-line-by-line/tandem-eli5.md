# How the files play together — simple version

The line-by-line versions live next to this note:

- `eli5/` is the simple one. Every line of code is written out, and under it is what that line does in plain words.
- `technical/` is the same lines, with the precise computer explanation.

## The school

The web page (`index.html`) is an empty room with a box called `root`. `main.jsx` walks in and builds the school inside that box. It turns on three helpers before any room appears:

1. The address watcher, so `/` is Today and `/todo` is Tasks.
2. The name tag (`UserContext`), so every room can ask who is logged in.
3. The hallway (`App`).

The hallway then turns on the energy sticker (`EnergyContext`) and draws the signs, the top bar, and whichever room matches the address.

## The pocket, the sticker, and the mail carrier

- The **name tag** is saved in the browser’s pocket (`localStorage`) so a refresh does not log you out. Signing in with Google fills it. Logout empties it. The same tag is whispered to the Chrome add-on if that add-on is installed.
- The **energy sticker** is a number from 1 to 5. Only the face buttons change it. Today, the task list, and the sidebar all look at the same sticker. The timer later reads the same number out of the pocket when it saves a session.
- The **mail carrier** (`api.ts`) takes every letter to the server. It always shows the secret pass from the pocket. If the server says the pass is old, the carrier quietly gets a new one and tries the letter again.

Rooms do not call each other. They share the name tag, the sticker, the shield notebook, and the mail carrier. A link only changes the address, and the hallway swaps the room.

## A few trips across rooms

**You sign in.** The Auth room sends Google’s proof to the server, stores your name and pass, and sends you to Today.

**You tap a face.** The sticker changes. Today asks the server for a new “what next” task. The task list sorts itself again for that energy.

**You add a task.** The task room sends it to the server and then asks for the list again. The calendar has its own copy of the list. It will see the new task the next time it asks. If the task has a due time, a little alarm is set on this computer to pop a message when that time comes.

**You start the timer.** The circle counts down. A poster (`FocusOverlay`) watches whether you leave the tab. A quick peek does nothing. If you stay away, a sound plays and a big card says come back. When the work circle finishes, the timer tells the server how long you went, how you felt, and how many times you wandered.

**You change the shield.** Switches and lists on the shield page wait a short moment, then save the whole list to the server. Today and the timer show the same status words, because they both ask one helper (`getShieldStatus`) what the list means right now. This website remembers the rules. The Chrome add-on or the phone app is what actually stops the websites.

**You plug in Gmail.** The connectors room asks the server for a Google address and sends you there. Google sends you back, and the page says you are connected.
