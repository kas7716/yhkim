#!/usr/bin/env python3
"""Builds the static pages of The Diana Dispatch.

Edit the CONTENT section below, then run:  python3 tools/build.py
Output is plain HTML in the site root. No dependencies.

Pictures live in assets/img/. To fill a paste-up frame in a story gallery,
save the photo under assets/work/ and put its path in the third slot of the
gallery entry, for example ("Menu cover", "", "assets/work/banju-01.jpg").
"""
import html
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

# ───────────────────────── CONTENT ─────────────────────────
SITE = {
    "name": "The Diana Dispatch",
    "person": "Diana Kim",
    "email": "kas7716@gmail.com",
    "linkedin": "https://www.linkedin.com/in/yuhan-kim-8118813b3/",
    "description": "Portfolio of Diana (Yuhan) Kim, a Vancouver based designer working across graphic design, UI/UX and marketing.",
    "edition": "No. 2",
}

ILLUSTRATION = "Illustration made with Higgsfield. Photographs of the work arrive in the next edition."

TICKER = [
    ("Diana Kim is open to internship placements in Vancouver", "about.html#contact"),
    ("New in this edition: menus and posters for Banju", "banju.html"),
    ("Xbox Series X|S launch campaign", "xbox-launch-campaign.html"),
    ("Plant Box, a concept for first time plant owners", "plant-box.html"),
]

SCRAPS = [
    ("Graphic design", "ink", "", ""),
    ("UI/UX", "", "", ""),
    ("Marketing", "red", "", ""),
    ("Seoul to Vancouver", "serif", "", ""),
    ("Banju menus", "", "banju.html", "Read the story"),
    ("Open to internships", "ink", "about.html#contact", "Say hello"),
]

LEAD = [
    "I'm Diana, a designer in Vancouver. Before design school I spent four years in Seoul, launching products for Xbox and sourcing for a CJ ENM affiliate. I learned what a brief asks for, what a budget allows, and how quickly an audience decides whether to care.",
    "Now I study New Media Design and Web Development at BCIT, and I work across graphic design, UI/UX and marketing. This edition collects the work: menus and posters for a restaurant downtown, a console launch campaign, and a concept for people keeping their first plant alive.",
]

STORIES = [
    {
        "slug": "banju", "img": "assets/img/banju.jpg", "page": "A2",
        "title": "Banju menus and posters", "short": "Banju menus and posters",
        "kind": "Graphic design", "when": "Vancouver",
        "deck": "Menu and poster design for Banju, a Korean Japanese restaurant in downtown Vancouver.",
        "status": "Developing story!",
        "facts": [("Discipline", "Graphic design"), ("Client", "Banju, Vancouver"), ("Pieces", "Menus, posters"), ("Format", "Print")],
        "sections": [
            ("The assignment", [
                "A menu is the one piece of design every guest reads from start to finish. It has to sell the kitchen, answer questions before they are asked, and survive a busy Friday night.",
                "Banju is a Korean Japanese restaurant on Bute Street in downtown Vancouver. I designed its menus and the posters that promote them.",
            ], []),
            ("What I made", [], [
                ("Menus", "The restaurant's menu, designed to be read at the table."),
                ("Posters", "Promotional posters for the room and the window."),
            ]),
        ],
        "pull": "Designed to be held, seen and read.",
        "gallery": [("Menu cover", "", ""), ("Menu spread", "is-wide", ""), ("Poster", "", ""), ("Poster", "", ""), ("In the restaurant", "", "")],
    },
    {
        "slug": "xbox-launch-campaign", "img": "assets/img/xbox.jpg", "page": "B1",
        "title": "Xbox Series X|S launch campaign", "short": "Xbox launch campaign",
        "kind": "Graphic design", "when": "Korea, 2020",
        "deck": "A gift set, posters and banners for the launch of Xbox Series X and Series S in Korea, made while I was the product manager on the brand.",
        "status": "Developing story!",
        "facts": [("Discipline", "Graphic design"), ("Context", "Console launch, Korea"), ("Pieces", "Gift set, posters, banners"), ("Year", "2020")],
        "sections": [
            ("The assignment", [
                "Xbox Series X and Series S launched in Korea while I was the product manager for Xbox at a Microsoft distributor.",
                "A launch plan lives in spreadsheets. A launch itself lives in the things people see and hold, so alongside the planning I worked on the campaign's visual pieces.",
            ], []),
            ("What I made", [], [
                ("Gift set", "A boxed set prepared for the launch."),
                ("Posters", "Launch posters for the campaign."),
                ("Banners", "Banners carrying the campaign across channels."),
            ]),
        ],
        "pull": "Before the screen, there was the business brief.",
        "gallery": [("Gift set", "", ""), ("Launch poster", "", ""), ("Banner", "", ""), ("Campaign in place", "is-wide", ""), ("Detail", "", "")],
    },
    {
        "slug": "plant-box", "img": "assets/img/plant.jpg", "page": "C1",
        "title": "Plant Box", "short": "Plant Box",
        "kind": "UI/UX concept", "when": "BCIT",
        "deck": "A concept for a plant subscription box with a companion app, made for people keeping their first plant alive.",
        "status": "Concept in progress!",
        "facts": [("Discipline", "UI/UX and branding"), ("Type", "School concept"), ("My part", "Brand strategy, personas, interface"), ("Tools", "Figma, Illustrator")],
        "sections": [
            ("The idea", [
                "Plant Box pairs a monthly plant subscription with a companion app. The box delivers the plant. The app answers the question every beginner asks a week later: what is wrong with it?",
                "This is a concept project. It has no customers and claims no results.",
            ], []),
            ("What I am making", [], [
                ("Brand strategy", "Who the service is for and how it should sound."),
                ("Personas", "The beginner plant owners the concept is built around."),
                ("Interface", "App screens for care guidance and diagnosis."),
            ]),
        ],
        "pull": "Good care. Less guesswork.",
        "gallery": [("Persona", "is-half", ""), ("App flow", "is-half", ""), ("Screens", "is-wide", ""), ("Packaging", "", "")],
    },
]

HELD = [("K-Sip", "UI/UX"), ("Fruity Lab", "Brand identity")]

EXPERIENCE = [
    ("Now", "New Media Design and Web Development, BCIT", "Full time student in Vancouver, building this portfolio toward an internship."),
    ("2022 to 2023", "Project manager, BrandworksKorea", "Overseas sourcing team at a CJ ENM affiliate in Seoul."),
    ("2019 to 2022", "Product manager for Xbox", "At a Microsoft distributor in Korea, through the launch of Xbox Series X and Series S."),
]
# ─────────────────────── END CONTENT ───────────────────────

e = html.escape
SCRIBBLE = '<svg viewBox="0 0 100 10" preserveAspectRatio="none" aria-hidden="true"><path pathLength="1" d="M1 6 C 18 1, 30 9, 48 5 S 80 2, 99 6"/></svg>'
CIRCLE = '<svg viewBox="0 0 100 40" preserveAspectRatio="none" aria-hidden="true"><path pathLength="1" d="M8 22 C 6 6, 40 2, 62 3 S 98 10, 94 24 S 60 39, 36 37 S 2 34, 6 16"/></svg>'


def head(title, desc):
    full = f"{title} | {SITE['name']}" if title else f"{SITE['name']} | Portfolio of {SITE['person']}"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(full)}</title>
<meta name="description" content="{e(desc)}">
<meta name="author" content="{e(SITE['person'])}">
<meta property="og:type" content="website">
<meta property="og:title" content="{e(full)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="assets/img/cover.jpg">
<meta name="theme-color" content="#e9e5dc">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preload" href="fonts/fraunces-latin-full-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="fonts/archivo-latin-wdth-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="css/dispatch.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""


def ticker():
    group = "".join(f'<span class="ticker__item"><a href="{u}">{e(t)}</a></span>' for t, u in TICKER)
    return f"""<div class="ticker" aria-label="Latest">
  <div class="ticker__track"><div class="ticker__group">{group}</div><div class="ticker__group" aria-hidden="true">{group.replace('<a ', '<a tabindex="-1" ')}</div></div>
</div>
"""


def top(current, inner=True):
    def nav(label, href, key):
        cur = ' aria-current="page"' if key == current else ""
        return f'<a href="{href}"{cur}>{label}</a>'
    tag = "p" if inner else "h1"
    return ticker() + f"""<header class="wrap">
  <div class="masthead{' masthead--inner' if inner else ''}">
    <div class="ear"><strong>Weather</strong>Vancouver: rain, probably. Good day to stay in and read.</div>
    <{tag} style="margin:0"><a class="masthead__title" href="index.html">{e(SITE['name'])}</a></{tag}>
    <div class="ear ear--right"><strong>Price</strong>Free. Always was.<div class="barcode" aria-hidden="true"></div></div>
  </div>
  <div class="dateline"><span data-today>Vancouver edition</span><span>Design edition, {SITE['edition']}</span><span>Seoul to Vancouver</span><span>Written and designed by {e(SITE['person'])}</span></div>
</header>
<div class="bar">
  <div class="wrap bar__in">
    <a class="bar__name" href="index.html">{e(SITE['name'])}</a>
    <nav class="bar__nav" aria-label="Sections">
      {nav('Front page', 'index.html', 'home')}
      {nav('Work', 'index.html#work', 'work')}
      {nav('About', 'about.html', 'about')}
      {nav('Contact', 'about.html#contact', 'contact')}
    </nav>
  </div>
</div>
"""


def contact_actions():
    out = f'<a class="btn btn--fill" href="mailto:{SITE["email"]}">Email Diana</a>'
    if SITE["linkedin"]:
        out += f'<a class="btn" href="{SITE["linkedin"]}" rel="noopener">Connect on LinkedIn</a>'
    return out


def callout(title_html, extra="", anchor=""):
    return f"""  <section class="callout"{f' id="{anchor}"' if anchor else ''}>
    <img class="callout__bg" src="assets/img/press.jpg" alt="" loading="lazy">
    <div class="wrap callout__in{' contact' if extra else ''}">
      <div style="display:grid; gap:2rem"><h2 class="callout__title">{title_html}</h2><div class="actions">{contact_actions()}</div></div>
      {extra}
    </div>
  </section>
"""


def foot(matter=False):
    li = f'<a href="{SITE["linkedin"]}" rel="noopener">LinkedIn</a>' if SITE["linkedin"] else ""
    return f"""<footer class="footer">
  <div class="wrap footer__in">
    <span>{e(SITE['name'])}. Written, designed and printed by {e(SITE['person'])}, Vancouver.</span>
    <nav aria-label="Footer"><a href="index.html#work">Work</a><a href="about.html">About</a><a href="mailto:{SITE['email']}">Email</a>{li}</nav>
  </div>
</footer>
{'<script src="js/matter.min.js" defer></script>' if matter else ''}
<script src="js/main.js" defer></script>
</body>
</html>
"""


def page_home():
    scraps = ""
    for text, kind, href, small in SCRAPS:
        cls = "scrap" + (f" scrap--{kind}" if kind else "")
        sm = f"<small>{e(small)}</small>" if small else ""
        scraps += (f'<a class="{cls}" href="{href}">{sm}{e(text)}</a>' if href
                   else f'<span class="{cls}">{e(text)}</span>')
    inside = "".join(f'<li><a href="{s["slug"]}.html"><span>{e(s["short"])}</span><i></i><span>{s["page"]}</span></a></li>' for s in STORIES)
    inside += '<li><a href="about.html"><span>About the editor</span><i></i><span>Back page</span></a></li>'
    lead = "".join(f"<p>{e(p)}</p>" for p in LEAD)

    def card(s, cls):
        return f"""    <li class="story {cls}"><a class="story__link" href="{s['slug']}.html">
      <div class="pic"><img src="{s['img']}" alt="" loading="lazy"></div>
      <div><p class="kicker kicker--red">{e(s['kind'])}, {e(s['when'])}</p><h3 class="story__title"><span>{e(s['title'])}</span></h3><p class="story__deck">{e(s['deck'])}</p></div></a></li>
"""
    rows = card(STORIES[0], "story--feature") + card(STORIES[1], "story--left") + card(STORIES[2], "story--right")
    held = "".join(f"<span><b>{e(t)}</b> <span>{e(k)}</span></span>" for t, k in HELD)
    return head("", SITE["description"]) + top("home", inner=False) + f"""<main id="main">
  <section class="wrap front">
    <div class="lead">
      <p class="kicker kicker--red">Lead story</p>
      <h2 class="lead__head"><span class="line"><span>From a business</span></span><span class="line"><span>brief to a better</span></span><span class="line"><span><span class="underline">experience.{SCRIBBLE}</span></span></span></h2>
      <p class="byline kicker"><span>By {e(SITE['person'])}</span><span>Vancouver</span><span>Graphic design, UI/UX, marketing</span></p>
      <div class="story-text">{lead}</div>
      <nav class="inside" aria-label="Inside this edition"><p class="kicker">Inside this edition</p><ul>{inside}</ul></nav>
    </div>
    <div>
      <figure class="cover stage" data-stage>
        <div class="pic"><img src="assets/img/cover.jpg" alt="A person holding an open newspaper that hides their face. The paper reads: The Diana Dispatch, designer seeks internship."></div>
        <div class="cover__print" aria-hidden="true"><b>{e(SITE['name'])}</b><div class="cover__pages"><div><em>Extra</em><strong>Designer seeks internship.</strong><div class="greek"></div></div><div><div class="greek greek--tall"></div></div></div></div>
        <p class="cover__note pen" aria-hidden="true"><svg viewBox="0 0 60 40"><path d="M56 6 C 40 4, 18 10, 6 30 M6 30 l2 -11 M6 30 l11 -3"/></svg>that's me</p>
        <div class="scraps">{scraps}</div>
      </figure>
      <p class="credit stage__hint">The clippings are loose. Grab one and throw it. {ILLUSTRATION.split('.')[0]}.</p>
    </div>
  </section>

  <section class="section wrap" id="work">
    <div class="section__head"><h2 class="section__title">In this edition</h2><p class="kicker">Selected work</p></div>
    <ul class="stories">
{rows}      <li class="held"><span class="kicker kicker--red">Next edition</span>{held}</li>
    </ul>
  </section>

  <section class="wrap" aria-label="About Diana">
    <div class="columns" style="border-top: var(--thick)">
      <div class="column"><p class="kicker kicker--red">Then</p><h3>Before design</h3><p>I spent four years in Seoul as a product manager and project manager, launching products for Xbox and sourcing for a CJ ENM affiliate.</p></div>
      <div class="column"><p class="kicker kicker--red">Now</p><h3>In school, and in print</h3><p>I study New Media Design and Web Development at BCIT, and I design menus and posters for a restaurant downtown.</p></div>
      <div class="column"><p class="kicker kicker--red">Next</p><h3>An internship</h3><p>I am looking for a placement in Vancouver where design has to answer to a brief, a budget and a real audience.</p><p><a class="textlink" href="about.html">Read the full profile</a></p></div>
    </div>
  </section>

{callout(f'Something worth <span class="circled">keeping?{CIRCLE}</span>')}</main>
""" + foot(matter=True)


def frame(cap, cls, img):
    if img:
        return f'<figure class="frame has-img {cls}"><img src="{img}" alt="{e(cap)}" loading="lazy"></figure>'
    return f'<figure class="frame {cls}"><span class="pen">photo to come</span><span class="kicker">{e(cap)}</span></figure>'


def page_story(i):
    s = STORIES[i]
    nxt = STORIES[(i + 1) % len(STORIES)]
    body = ""
    for h, paras, items in s["sections"]:
        body += f"<h2>{e(h)}</h2>" + "".join(f"<p>{e(p)}</p>" for p in paras)
        if items:
            body += "<ul>" + "".join(f"<li><strong>{e(a)}</strong><span>{e(b)}</span></li>" for a, b in items) + "</ul>"
    facts = "".join(f"<div><dt>{e(a)}</dt><dd>{e(b)}</dd></div>" for a, b in s["facts"])
    gal = "".join(frame(cap, cls, img) for cap, cls, img in s["gallery"])
    return head(s["title"], s["deck"]) + top("work") + f"""<main id="main">
  <article class="wrap">
    <header class="article__head">
      <div><a class="article__section kicker kicker--red" href="index.html#work">{e(s['kind'])}, {e(s['when'])}</a>
      <h1 class="article__title">{e(s['title'])}</h1></div>
      <div><p class="article__deck">{e(s['deck'])}</p><span class="status pen">{e(s['status'])}</span></div>
    </header>
    <figure class="leadpic"><div class="pic"><img src="{s['img']}" alt=""></div><figcaption class="credit">{ILLUSTRATION}</figcaption></figure>
    <div class="article__body">
      <dl class="facts">{facts}</dl>
      <div class="prose">{body}</div>
    </div>
    <aside class="pull"><p>{e(s['pull'])}</p></aside>
    <div class="gallery">{gal}</div>
  </article>
  <nav class="next wrap" aria-label="Next story"><a href="{nxt['slug']}.html"><span class="kicker kicker--red">Next story</span><strong><span>{e(nxt['title'])}</span></strong></a></nav>
</main>
""" + foot()


def page_about():
    exp = "".join(f'<li><span class="when">{e(w)}</span><div><h3>{e(t)}</h3><p>{e(d)}</p></div></li>' for w, t, d in EXPERIENCE)
    li = f'<p><a href="{SITE["linkedin"]}" rel="noopener">LinkedIn</a></p>' if SITE["linkedin"] else ""
    card = f'<div class="card"><p class="kicker kicker--red">Clip and keep</p><h3>{e(SITE["person"])}</h3><p>Graphic design, UI/UX, marketing<br>Vancouver, BC</p><p><a href="mailto:{SITE["email"]}">{SITE["email"]}</a></p>{li}</div>'
    return head("About", "About Diana (Yuhan) Kim: designer in Vancouver with a marketing and product background from Seoul.") + top("about") + f"""<main id="main">
  <article class="wrap">
    <header class="article__head">
      <div><a class="article__section kicker kicker--red" href="index.html">The back page</a>
      <h1 class="article__title">A designer who started in the business brief.</h1></div>
      <div><p class="article__deck">I'm Yuhan Kim, and most people call me Diana. I moved from Seoul to Vancouver to turn years of launching and marketing products into designing them.</p></div>
    </header>
    <figure class="leadpic"><div class="pic"><img src="assets/img/desk.jpg" alt=""></div><figcaption class="credit">Illustration made with Higgsfield.</figcaption></figure>
    <div class="article__body">
      <dl class="facts"><div><dt>Based in</dt><dd>Vancouver, BC</dd></div><div><dt>From</dt><dd>Seoul</dd></div><div><dt>Studying</dt><dd>New Media Design and Web Development, BCIT</dd></div><div><dt>Looking for</dt><dd>An internship placement</dd></div></dl>
      <div class="prose">
        <h2>Profile</h2>
        <p>In Korea I worked on the business side of well known brands. I learned how a launch is planned, what a budget allows, and how quickly an audience decides whether to care.</p>
        <p>Design is where I want to use that. I work across graphic design, UI/UX and marketing, and I like projects where all three meet: a campaign that needs a poster, a product that needs a screen, a restaurant that needs a menu people enjoy reading.</p>
        <h2>Experience</h2>
        <ol class="timeline">{exp}</ol>
        <h2>What I do</h2>
        <ul>
          <li><strong>Graphic design</strong><span>Print, posters, menus, packaging, campaign pieces.</span></li>
          <li><strong>UI/UX</strong><span>Personas, flows, interface design in Figma.</span></li>
          <li><strong>Marketing</strong><span>Product launches, campaign planning, coordination across teams.</span></li>
        </ul>
      </div>
    </div>
  </article>
{callout("Let's start a conversation.", card, "contact")}</main>
""" + foot()


def page_404():
    return head("Page not found", "This page is not in this edition.") + top("") + """<main id="main" class="wrap notfound">
  <p class="kicker kicker--red">Correction</p>
  <h1 class="article__title">This page did not make the edition.</h1>
  <div class="actions"><a class="btn" href="index.html">Back to the front page</a></div>
</main>
""" + foot()


def main():
    out = {"index.html": page_home(), "about.html": page_about(), "404.html": page_404()}
    for i, s in enumerate(STORIES):
        out[s["slug"] + ".html"] = page_story(i)
    for name, text in out.items():
        (ROOT / name).write_text(text, encoding="utf-8")
        print("wrote", name, len(text))


if __name__ == "__main__":
    main()
