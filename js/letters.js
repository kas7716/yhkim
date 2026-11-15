/* The Diana Dispatch: circulation counter and letters to the editor.
   Data lives in Firebase Firestore (free Spark plan). The web config below is public by design;
   what keeps the data safe is firestore.rules in the repository root.
   Until projectId is filled in, nothing is loaded and both widgets stay hidden. */

const FIREBASE = {
  apiKey: "AIzaSyANEfOvrpDFSnEh0r02tNTFQsS821kBCTA",
  authDomain: "diana-dispatch.firebaseapp.com",
  projectId: "diana-dispatch",
  appId: "1:642508723118:web:7668484fe4d80e851eee3f"
};

const SDK = "https://www.gstatic.com/firebasejs/11.0.2/";
const TZ = "America/Vancouver";      /* one edition day for everybody */
const MAX_NAME = 30;
const MAX_MSG = 300;
const COOLDOWN_MS = 60 * 1000;
const SHOW = 40;                      /* letters printed on the page */

const $ = (sel, root) => (root || document).querySelector(sel);

const store = {
  get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
  set(k, v) { try { localStorage.setItem(k, v); } catch (e) { /* private mode: fine */ } }
};

function editionDay() {
  return new Intl.DateTimeFormat("en-CA", { timeZone: TZ, year: "numeric", month: "2-digit", day: "2-digit" }).format(new Date());
}
function fmtDate(d) {
  return new Intl.DateTimeFormat("en-CA", { timeZone: TZ, year: "numeric", month: "short", day: "numeric" }).format(d);
}
function fmtNum(n) { return Number(n || 0).toLocaleString("en-CA"); }

/* Visiting any page with ?owner keeps your own visits out of the count. ?owner=off turns it back on. */
(function ownerSwitch() {
  const m = /[?&]owner(?:=([^&]*))?/.exec(location.search);
  if (!m) return;
  store.set("dd-owner", m[1] === "off" ? "0" : "1");
})();

if (FIREBASE.projectId) start().catch(function (err) { console.warn("Dispatch counter offline:", err); });

async function start() {
  const [{ initializeApp }, fs] = await Promise.all([
    import(SDK + "firebase-app.js"),
    import(SDK + "firebase-firestore.js")
  ]);
  const db = fs.getFirestore(initializeApp(FIREBASE));
  circulation(db, fs);
  letters(db, fs);
}

/* ---------- Circulation: readers today and readers to date ---------- */
async function circulation(db, fs) {
  const box = $("[data-circulation]");
  if (!box) return;
  const today = editionDay();
  const dayRef = fs.doc(db, "stats", "day-" + today);
  const totalRef = fs.doc(db, "stats", "total");
  const bump = (ref) => fs.setDoc(ref, { count: fs.increment(1) }, { merge: true });

  /* A reader is counted once per browser per day, and once ever for the total. */
  if (store.get("dd-owner") !== "1") {
    if (store.get("dd-day") !== today) {
      store.set("dd-day", today);
      try { await bump(dayRef); } catch (e) { store.set("dd-day", ""); }
    }
    if (store.get("dd-first") !== "1") {
      store.set("dd-first", "1");
      try { await bump(totalRef); } catch (e) { store.set("dd-first", ""); }
    }
  }
  try {
    const [d, t] = await Promise.all([fs.getDoc(dayRef), fs.getDoc(totalRef)]);
    $("[data-readers='today']", box).textContent = fmtNum(d.exists() ? d.data().count : 0);
    $("[data-readers='total']", box).textContent = fmtNum(t.exists() ? t.data().count : 0);
    box.hidden = false;
  } catch (e) { /* leave it hidden */ }
}

/* ---------- Letters to the editor ---------- */
function letters(db, fs) {
  const section = $("#letters");
  if (!section) return;
  const list = $("[data-letters]", section);
  const form = $("#letter-form", section);
  const status = $("[data-status]", form);
  const msgEl = form.elements.message;
  const nameEl = form.elements.name;
  const countEl = $("[data-count]", form);
  const col = fs.collection(db, "letters");

  function say(text, kind) {
    status.textContent = text;
    status.dataset.kind = kind || "";
  }

  function letterEl(l) {
    const li = document.createElement("li");
    li.className = "letter";
    const p = document.createElement("p");
    p.className = "letter__body";
    p.textContent = l.message;
    const by = document.createElement("p");
    by.className = "letter__by kicker";
    const who = document.createElement("span");
    who.textContent = l.name;
    const when = document.createElement("time");
    when.textContent = fmtDate(l.date);
    by.append(who, when);
    li.append(p, by);
    return li;
  }

  function empty() {
    const li = document.createElement("li");
    li.className = "letter letter--empty";
    li.dataset.empty = "";
    li.innerHTML = '<p class="pen">No letters yet. Be the first to write to the editor.</p>';
    return li;
  }

  async function load() {
    try {
      const snap = await fs.getDocs(fs.query(col, fs.orderBy("createdAt", "desc"), fs.limit(SHOW)));
      list.replaceChildren();
      snap.forEach(function (doc) {
        const d = doc.data();
        const date = d.createdAt && d.createdAt.toDate ? d.createdAt.toDate() : new Date();
        list.append(letterEl({ name: d.name, message: d.message, date: date }));
      });
      if (!list.children.length) list.append(empty());
      section.hidden = false;
    } catch (e) {
      /* If letters cannot load, keep the section out of the page rather than show a broken one. */
    }
  }

  msgEl.addEventListener("input", function () { countEl.textContent = msgEl.value.length + " / " + MAX_MSG; });

  form.addEventListener("submit", async function (ev) {
    ev.preventDefault();
    if (form.elements.website.value) return;                     /* honeypot */
    const name = nameEl.value.trim().slice(0, MAX_NAME);
    const message = msgEl.value.trim().slice(0, MAX_MSG);
    if (!message) { say("Your letter is empty. Write a line or two first.", "error"); msgEl.focus(); return; }
    if (!name) { say("Please sign your letter with a name or initials.", "error"); nameEl.focus(); return; }
    const wait = COOLDOWN_MS - (Date.now() - Number(store.get("dd-last") || 0));
    if (wait > 0) { say("One letter at a time, please. Try again in " + Math.ceil(wait / 1000) + " seconds.", "error"); return; }

    const btn = $("button[type=submit]", form);
    btn.disabled = true;
    say("Sending to the press room...", "");
    try {
      await fs.addDoc(col, { name: name, message: message, createdAt: fs.serverTimestamp() });
      store.set("dd-last", String(Date.now()));
      const placeholder = $("[data-empty]", list);
      if (placeholder) placeholder.remove();
      list.prepend(letterEl({ name: name, message: message, date: new Date() }));
      form.reset();
      countEl.textContent = "0 / " + MAX_MSG;
      say("Letter received. Thank you for writing.", "ok");
    } catch (e) {
      say("The press room is closed right now. Please try again later.", "error");
    } finally {
      btn.disabled = false;
    }
  });

  load();
}
