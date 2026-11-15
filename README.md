# The Diana Dispatch

Portfolio site of Diana (Yuhan) Kim. Static HTML, CSS and JavaScript, no build step required to serve.

To change content, edit the CONTENT section in `tools/build.py` and run `python3 tools/build.py`.

## Circulation counter and Letters to the editor

`js/letters.js` powers the readers count (footer) and the guestbook (front page, "Letters to the editor").
Data is stored in Firebase Firestore. Paste the project's web config into the `FIREBASE` object at the top of `js/letters.js`.
Until `projectId` is filled in, both widgets stay hidden.

- Security rules live in `firestore.rules`. Paste them into Firebase console, Firestore, Rules, then Publish.
- Counting: one reader is counted once per browser per day (Vancouver time) and once for the total.
- Open any page with `?owner` once to keep your own visits out of the count. Use `?owner=off` to undo.
- To delete a letter: open the site with `?owner`, press "Sign in with Google" in the Editor's desk line (only kas7716@gmail.com works), then use the Delete link under a letter. This is enforced by `firestore.rules`, not by the page.
