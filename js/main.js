/* The Diana Dispatch: interactions. No build step. */
(function () {
  "use strict";
  var reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* Today's date in the dateline */
  var dateEl = document.querySelector("[data-today]");
  if (dateEl) {
    try {
      dateEl.textContent = new Intl.DateTimeFormat("en-CA", {
        weekday: "long", year: "numeric", month: "long", day: "numeric"
      }).format(new Date());
    } catch (e) { /* keep the fallback text */ }
  }

  /* Show the small title once the masthead has scrolled away */
  var masthead = document.querySelector(".masthead");
  var bar = document.querySelector(".bar");
  if (masthead && bar && "IntersectionObserver" in window) {
    new IntersectionObserver(function (entries) {
      bar.classList.toggle("is-stuck", !entries[0].isIntersecting);
    }, { threshold: 0 }).observe(masthead);
  }

  /* Work index: a plate follows the pointer */
  var peek = document.querySelector(".peek");
  if (peek && window.matchMedia("(hover: hover)").matches) {
    var px = 0, py = 0, tx = 0, ty = 0, raf = null;
    var cap = peek.querySelector(".plate__cap");
    var no = peek.querySelector(".plate__no");
    var img = peek.querySelector("img");
    var follow = function () {
      px += (tx - px) * 0.18; py += (ty - py) * 0.18;
      peek.style.left = px + "px"; peek.style.top = py + "px";
      raf = requestAnimationFrame(follow);
    };
    document.querySelectorAll("[data-peek]").forEach(function (row) {
      row.addEventListener("pointerenter", function (e) {
        peek.className = "peek plate plate--" + row.dataset.peek + " is-on";
        no.textContent = row.dataset.no || "";
        cap.textContent = row.dataset.cap || "";
        if (img) {
          if (row.dataset.img) { img.src = row.dataset.img; img.hidden = false; }
          else { img.hidden = true; img.removeAttribute("src"); }
        }
        tx = e.clientX; ty = e.clientY;
        if (!raf) { px = tx; py = ty; follow(); }
      });
      row.addEventListener("pointermove", function (e) { tx = e.clientX + 210; ty = e.clientY + 20; });
      row.addEventListener("pointerleave", function () {
        peek.classList.remove("is-on");
        cancelAnimationFrame(raf); raf = null;
      });
    });
  }

  /* Front page: loose clippings you can grab, drag and throw */
  var stage = document.querySelector("[data-stage]");
  if (!stage || !window.Matter || reduced) return;

  var M = window.Matter;
  var engine = M.Engine.create();
  engine.gravity.y = 1.1;
  stage.classList.add("is-live");

  var els = Array.prototype.slice.call(stage.querySelectorAll(".scrap"));
  var W = stage.clientWidth, H = stage.clientHeight;
  var items = els.map(function (el, i) {
    var w = el.offsetWidth, h = el.offsetHeight;
    var x = W * (0.18 + 0.64 * ((i * 0.37) % 1));
    var body = M.Bodies.rectangle(x, -80 - i * 130, w, h, {
      restitution: 0.32, friction: 0.5, frictionAir: 0.018,
      angle: (i % 2 ? 1 : -1) * (0.15 + (i % 3) * 0.12)
    });
    return { el: el, body: body, w: w, h: h };
  });

  var walls = [];
  function buildWalls() {
    W = stage.clientWidth; H = stage.clientHeight;
    M.Composite.remove(engine.world, walls);
    var t = 200, o = { isStatic: true };
    walls = [
      M.Bodies.rectangle(W / 2, H + t / 2, W + t * 2, t, o),
      M.Bodies.rectangle(-t / 2, H / 2 - 1500, t, H + 4000, o),
      M.Bodies.rectangle(W + t / 2, H / 2 - 1500, t, H + 4000, o),
      M.Bodies.rectangle(W / 2, -2600, W + t * 2, t, o)
    ];
    M.Composite.add(engine.world, walls);
    items.forEach(function (it) {
      var p = it.body.position;
      if (p.x > W - 10 || p.y > H + 50) M.Body.setPosition(it.body, { x: Math.min(p.x, W - it.w / 2 - 10), y: Math.min(p.y, H - it.h) });
    });
  }
  buildWalls();
  M.Composite.add(engine.world, items.map(function (it) { return it.body; }));

  var held = null;
  items.forEach(function (it) {
    var moved = 0, sx = 0, sy = 0;
    it.el.addEventListener("dragstart", function (e) { e.preventDefault(); });
    it.el.addEventListener("pointerdown", function (e) {
      if (e.button) return;
      if (e.pointerType === "mouse") e.preventDefault();
      var r = stage.getBoundingClientRect();
      held = { it: it, x: e.clientX - r.left, y: e.clientY - r.top,
               ox: e.clientX - r.left - it.body.position.x, oy: e.clientY - r.top - it.body.position.y };
      moved = 0; sx = e.clientX; sy = e.clientY;
      it.el.setPointerCapture(e.pointerId);
      it.el.classList.add("is-held");
      M.Sleeping && M.Sleeping.set(it.body, false);
    });
    it.el.addEventListener("pointermove", function (e) {
      if (!held || held.it !== it) return;
      var r = stage.getBoundingClientRect();
      held.x = e.clientX - r.left; held.y = e.clientY - r.top;
      moved = Math.max(moved, Math.abs(e.clientX - sx) + Math.abs(e.clientY - sy));
    });
    var drop = function () {
      if (held && held.it === it) held = null;
      it.el.classList.remove("is-held");
    };
    it.el.addEventListener("pointerup", drop);
    it.el.addEventListener("pointercancel", drop);
    it.el.addEventListener("click", function (e) { if (moved > 8) { e.preventDefault(); e.stopPropagation(); } }, true);
  });

  var running = false, last = 0;
  function frame(now) {
    if (!running) return;
    var dt = Math.min(now - last || 16.6, 33); last = now;
    if (held) {
      var b = held.it.body;
      var vx = (held.x - held.ox - b.position.x) * 0.28;
      var vy = (held.y - held.oy - b.position.y) * 0.28;
      var cap = 60;
      M.Body.setVelocity(b, { x: Math.max(-cap, Math.min(cap, vx)), y: Math.max(-cap, Math.min(cap, vy)) });
      M.Body.setAngularVelocity(b, b.angularVelocity * 0.85);
    }
    M.Engine.update(engine, dt);
    for (var i = 0; i < items.length; i++) {
      var it = items[i], p = it.body.position;
      it.el.style.transform = "translate(" + (p.x - it.w / 2).toFixed(1) + "px," + (p.y - it.h / 2).toFixed(1) + "px) rotate(" + it.body.angle.toFixed(3) + "rad)";
    }
    requestAnimationFrame(frame);
  }
  function start() { if (!running) { running = true; last = 0; requestAnimationFrame(frame); } }
  function stop() { running = false; }

  if ("IntersectionObserver" in window) {
    new IntersectionObserver(function (en) { en[0].isIntersecting ? start() : stop(); }).observe(stage);
  } else { start(); }

  var rt;
  window.addEventListener("resize", function () {
    clearTimeout(rt);
    rt = setTimeout(function () {
      items.forEach(function (it) {
        var w = it.el.offsetWidth, h = it.el.offsetHeight;
        if (Math.abs(w - it.w) > 2) { M.Body.scale(it.body, w / it.w, h / it.h); it.w = w; it.h = h; }
      });
      buildWalls();
    }, 150);
  });
})();
