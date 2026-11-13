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
    ("First7, an app for your first week in Canada", "first7.html"),
    ("Xbox Series X|S launch campaign", "xbox-launch-campaign.html"),
    ("Rootly, a plant brand for nervous beginners", "rootly.html"),
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
        "slug": "banju", "img": "assets/work/banju/card.jpg", "thumb": "assets/img/banju.jpg", "lead": "assets/work/banju/lead.jpg", "color": True, "page": "A2",
        "credit": "The Banju main menu: cover, signature page and the hot pot spread.",
        "title": "Banju menus and posters", "short": "Banju menus and posters",
        "kind": "Graphic design", "when": "Vancouver, 2026",
        "deck": "A new main menu, lunch and night menus, a sandwich board and two event posters for Banju, a Korean Japanese restaurant in downtown Vancouver.",
        "status": "",
        "facts": [("Discipline", "Graphic design, print"), ("Client", "Banju, Vancouver"), ("Pieces", "Main, lunch and night menus, sandwich board, two posters"), ("Timeline", "May to October 2026"), ("Tools", "InDesign, Illustrator, Photoshop")],
        "sections": [
            ("The brief", [
                "Banju asked me for a new main menu, a lunch menu, a night menu, a sandwich board for the sidewalk, and posters for two events: the World Cup and Halloween.",
                "The old menu was made in Canva before the restaurant renewed its dishes. It listed the food, but it did not feel designed.",
            ], []),
            ("The problem", [
                "I work at Banju, so I see guests order every day. Many of them are not Korean, and the dish names alone did not tell them what they would get. I often watched guests look dishes up on Google at the table.",
                "Banju also has a very long menu. Showing every dish with a photo was not possible, so the real work was deciding which dishes deserved one.",
            ], []),
            ("My approach", [], [
                ("Choose the signature dishes", "I picked the dishes that best represent Banju and gave them the large photos. Everything else is listed with a short English description."),
                ("One concept per section", "I split the menu by category, such as signature dishes, bibimbap and noodles, grill and wok, anju, and sushi and sashimi, and gave each page its own layout. Dark stone backgrounds, serif headings and one price style keep the pages reading as one book."),
                ("Shoot, edit and write", "I photographed and edited the food myself. The owners gave me descriptions in Korean, and I translated them into English, checking terms with research and AI tools so they stay consistent."),
            ]),
            ("The hot pot spread", [
                "Several signature dishes arrive at the table on a gas burner. I placed them across two facing pages so the pans run down both outer edges, with the flame showing under each one.",
                "Keeping the spread clean while still making it obvious that these dishes come with a burner took more rounds of revision than any other page.",
            ], []),
            ("Revisions", [
                "Banju has three owners, and dishes were added and removed throughout the project. Agreeing on the final menu took time, and I was studying full time at BCIT, so the work ran from May to October 2026.",
                "The main menu has 16 pages today. Banju is still renewing its sides, drinks and alcohol, so two more pages are planned, for 18 in total.",
            ], []),
            ("Printing", [
                "I built the print pieces in InDesign, with Illustrator and Photoshop for graphics and photos. Most pieces are printed at legal size on 28 lb paper. I made test prints at Staples before choosing the paper and size.",
            ], []),
            ("Posters and sandwich board", [
                "The World Cup Night and Halloween posters promoted special event days. They went up outside and inside the restaurant and on social media. The sandwich board brings the signature dishes out to the sidewalk.",
            ], []),
            ("The result", [
                "The menus are in use at Banju today. Before, most guests ordered from the QR code menu. Since the printed menus arrived, I have seen many more guests reading the physical menu.",
            ], []),
        ],
        "pull": "The real work was deciding which dishes deserved a photo.",
        "gallery": [
            "## The main menu",
            ("Cover", "is-third", "assets/work/banju/main-01.jpg"),
            ("Appetizers", "is-third", "assets/work/banju/main-02.jpg"),
            ("Signature dishes", "is-third", "assets/work/banju/main-03.jpg"),
            ("The hot pot spread. Dishes served on a gas burner run down both outer edges.", "is-full", "assets/work/banju/main-hotpot-spread.jpg"),
            ("Signature sashimi set", "is-third", "assets/work/banju/main-06.jpg"),
            ("Bibimbap and noodles", "is-third", "assets/work/banju/main-07.jpg"),
            ("Nigiri", "is-third", "assets/work/banju/main-15.jpg"),
            ("Anju, dishes to share with drinks", "is-full", "assets/work/banju/main-anju-spread.jpg"),
            "## Lunch and night",
            ("Lunch menu, two pages", "is-full", "assets/work/banju/lunch-spread.jpg"),
            ("Night menu", "is-half", "assets/work/banju/night.jpg"),
            ("Sandwich board", "is-half", "assets/work/banju/a-board.jpg"),
            "## Event posters",
            ("World Cup Night", "is-half", "assets/work/banju/poster-world-cup.jpg"),
            ("Halloween: Bloody Good Night", "is-half", "assets/work/banju/poster-halloween.jpg"),
        ],
    },
    {
        "slug": "first7", "img": "assets/work/first7/lead.jpg", "lead": "assets/work/first7/lead.jpg", "thumb": "assets/img/first7.jpg", "color": True, "page": "A3",
        "credit": "First7 screens: home, 7 day checklist, a task page, Overwhelmed Mode and progress.",
        "link": ("Open the prototype", "https://proto-comet-93806396.figma.site"),
        "embed": "https://proto-comet-93806396.figma.site",
        "title": "First7", "short": "First7",
        "kind": "UI/UX", "when": "BCIT",
        "deck": "A mobile app that helps international students and newcomers get through their first seven days in Canada, one day at a time.",
        "status": "",
        "facts": [("Discipline", "UI/UX design, brand"), ("Course", "UI/UX Strategy 2, BCIT"), ("Team", "Diana Kim, Gigi, Daisy"), ("My role", "Designer: all design deliverables"), ("Tools", "Figma, Illustrator")],
        "sections": [
            ("The problem", [
                "International students and newcomers arrive tired, jet lagged and often reading in a second language. Everything is urgent at once: a SIM card, transit, a bank account, groceries, a health card, emergency contacts.",
                "Not knowing the order is the real stress.",
            ], []),
            ("My role", [
                "I was the designer on a team of three with Gigi and Daisy. We did the research together, and I ran a survey with people in my own network. I made all of the design deliverables: the wireframes, the Figma prototype, the design system and components, the logo and brand style guide, and the presentation slides.",
            ], []),
            ("The idea", [
                "First7 turns an overwhelming pile into a sequence: one day, a few tasks, visible progress. After choosing a city and a profile (international student, newcomer or temporary worker), the user gets a seven day plan. Day 1 is getting connected, then transit, banking and SIN, ID and health coverage, school and city resources, community support, and a review of next steps.",
            ], []),
            ("Design decisions", [], [
                ("The 7 day track", "The one element the product is remembered by. Seven nodes, always: filled is done, ringed is today, hollow is ahead. It sits once at the top of the screen."),
                ("Overwhelmed Mode", "When it is all too much, the plan shrinks to three things for today: get connected, get around, stay safe."),
                ("Plain words", "\"Open a bank account\", not \"Financial onboarding\". Every screen answers two questions: what do I do today, and how long will it take?"),
                ("A friend, not a portal", "The brand should feel like a friend who already lives here: warm, calm and specific. The logo is a 7 drawn as a route, with a dot marking day one."),
            ]),
            ("Accessibility", [
                "I wrote accessibility rules into the style guide. Every colour is checked against WCAG 2.1 AA, status is never shown by colour alone, touch targets are at least 44 by 44, layouts survive 200 percent text size, motion respects reduced motion settings, and copy is plain English with no abbreviations that assume local knowledge.",
            ], []),
        ],
        "pull": "Not knowing the order is the real stress.",
        "gallery": [
            "## Try the prototype",
            ("embed",),
            "## Getting started",
            ("phones", [("Splash", "assets/work/first7/screen-01-splash.png"), ("Welcome", "assets/work/first7/screen-02-welcome.png"), ("Choose a city", "assets/work/first7/screen-03-choose-city.png"), ("Choose a profile", "assets/work/first7/screen-04-choose-profile.png")]),
            "## Seven days, one at a time",
            ("phones", [("Home dashboard", "assets/work/first7/screen-05-home-dashboard.png"), ("7 day checklist", "assets/work/first7/screen-06-7-day-checklist.png"), ("Task: SIM card", "assets/work/first7/screen-07-task-sim-card.png"), ("Task: transit", "assets/work/first7/screen-08-task-transit.png"), ("Task: bank account", "assets/work/first7/screen-09-task-bank-account.png"), ("Task: SIN and ID", "assets/work/first7/screen-10-task-sin-id.png"), ("Healthcare basics", "assets/work/first7/screen-11-healthcare-basics.png"), ("Apps and community hub", "assets/work/first7/screen-12-apps-community-hub.png")]),
            "## When it is too much",
            ("phones", [("Overwhelmed Mode", "assets/work/first7/screen-15-overwhelmed-mode.png"), ("Emergency information", "assets/work/first7/screen-14-emergency-info.png"), ("Progress summary", "assets/work/first7/screen-16-progress-summary.png"), ("Profile", "assets/work/first7/screen-13-profile.png")]),
            "## Design system",
            ("Brand foundation, logo and colour", "is-third", "assets/work/first7/style-guide-1.jpg"),
            ("Type, spacing, the 7 day track and components", "is-third", "assets/work/first7/style-guide-2.jpg"),
            ("Icons, accessibility rules and the system in use", "is-third", "assets/work/first7/style-guide-3.jpg"),
            ("Logo kit", "is-half", "assets/work/first7/logo-kit.jpg"),
            ("Figma components", "is-half", "assets/work/first7/components.png"),
        ],
    },
    {
        "slug": "rootly", "img": "assets/work/rootly/lead.jpg", "lead": "assets/work/rootly/lead.jpg", "thumb": "assets/img/plant.jpg", "color": True, "page": "B1",
        "credit": "Rootly brand style guide: logo system and brand pattern.",
        "title": "Rootly", "short": "Rootly",
        "kind": "Brand identity", "when": "BCIT",
        "deck": "A brand identity for a plant subscription box and companion app, made for young adults who want plants but are afraid of killing them.",
        "status": "",
        "facts": [("Discipline", "Brand identity"), ("Course", "MDIA 2166 Illustration for New Media, BCIT"), ("Team", "Solo: research, strategy, identity, logo, layout"), ("Client", "My instructor, in the client role"), ("Tools", "Illustrator")],
        "sections": [
            ("The problem", [
                "Young adults want plants but feel intimidated. They do not know where to start, and many have already lost a plant or two.",
                "Rootly is a subscription box with a companion app: curated plants plus step by step care guidance. The audience is 20 to 28, often living alone, wellness minded, on TikTok and Instagram, and into slow living and sustainability.",
            ], []),
            ("Research", [
                "I compared The Sill, Bloomscape and Leon & George on audience, price, subscription, app, beginner focus, care guidance, community and tone. Some offer subscription boxes, but none combine delivery with a companion app for beginners. That gap became Rootly's position: not just a plant, but a full support system for first time plant parents.",
            ], []),
            ("Two directions", [], [
                ("Soft Roots", "Organic, calm and earthy. Forest green, sage, linen and terracotta, with Lora and Inter. Its line: \"Grow slowly.\""),
                ("Bold Bloom", "Bold, playful and energetic. Deep green, lime pop, cream, coral pop and black, with Sergio Trendy and Nunito Sans. Its line: \"Don't kill it.\""),
            ]),
            ("The client's choice", [
                "My instructor, acting as the client, chose Bold Bloom. Its high contrast and humour fit a Gen Z audience better than the quiet, earthy option.",
                "Switching direction meant redesigning the logo and the whole palette, not just recolouring them.",
            ], []),
            ("The logo", [
                "I explored three concepts: a serif wordmark, a script wordmark, and a leaf icon with a tagline. The client chose the icon with tagline. The leaf on a stem sits next to a bold serif wordmark, with \"Grow with confidence\" set in lime.",
                "I built the leaf from ellipses, refined it with the pen tool, and combined shapes with Pathfinder. The final logo comes in four versions: horizontal, vertical, dark background and icon, exported as SVG and PNG for web, iOS and Android.",
            ], []),
            ("The system", [
                "The style guide covers logo rules, colour pairings, typography rules, a rounded grid brand pattern saved as an Illustrator pattern swatch, and how the brand applies to the app. The pattern tile size took several rounds before it read boldly at full scale.",
            ], []),
        ],
        "pull": "Don't kill it.",
        "gallery": [
            "## Research",
            ("Competitive analysis: The Sill, Bloomscape, Leon & George and Rootly", "is-full", "assets/work/rootly/proposal-competitive.jpg"),
            "## Two directions",
            ("Idea A: Soft Roots", "is-half", "assets/work/rootly/proposal-soft-roots.jpg"),
            ("Idea B: Bold Bloom, chosen by the client", "is-half", "assets/work/rootly/proposal-bold-bloom.jpg"),
            "## Logo",
            ("Three logo concepts. Option C, icon and tagline, was chosen.", "is-full", "assets/work/rootly/proposal-logo-concepts.jpg"),
            "## Style guide",
            ("Logo system", "is-half", "assets/work/rootly/style-logo.jpg"),
            ("Colour", "is-half", "assets/work/rootly/style-colour.jpg"),
            ("Typography", "is-half", "assets/work/rootly/style-typography.jpg"),
            ("Brand pattern", "is-half", "assets/work/rootly/style-pattern.jpg"),
            ("The brand in the app", "is-full", "assets/work/rootly/style-app.jpg"),
        ],
    },
    {
        "slug": "servesmart", "img": "assets/work/servesmart/lead.jpg", "lead": "assets/work/servesmart/lead.jpg", "color": True, "page": "B2",
        "credit": "ServeSmart running in the iOS simulator: menu, dish detail, ingredient guide, reference and saved dishes.",
        "title": "ServeSmart", "short": "ServeSmart",
        "kind": "Mobile app", "when": "BCIT, 2026",
        "deck": "A menu study app for restaurant servers, built in React Native after my own shifts at Banju.",
        "status": "",
        "facts": [("Discipline", "Mobile app design and development"), ("Course", "MDIA 4295 App Development Strategy 2, BCIT"), ("Team", "Solo"), ("Built with", "React Native, Expo, React Navigation, AsyncStorage, Wikipedia API")],
        "sections": [
            ("Why I made it", [
                "Working at Banju made me want a way to review ingredients and possible changes before a shift, especially when I have to explain dishes in English.",
                "ServeSmart is a study app for servers. It starts with four real menu items: Vegetable Hot Stone Bowl Bibimbap, Seafood Soft Tofu Soup, Steamed Clams with Wine & Butter, and Mushroom Bulgogi.",
            ], []),
            ("What it does", [], [
                ("Banju Menu", "Browse the dishes and search by keyword."),
                ("Menu Detail", "Read ingredients, changes a guest can ask for, and allergy checks. Save a dish to study later."),
                ("Ingredient Guide", "Look up an English ingredient word through the Wikipedia API."),
                ("Ingredient Reference", "Read a short introduction with its source and licence."),
                ("My Study", "Review the dishes saved on the device."),
            ]),
            ("Being careful with allergies", [
                "A study app for servers must not overpromise. The app lists what to check for egg, soy, milk, crustaceans and molluscs, and keeps sulphite and gluten concerns separate from food allergy.",
                "It also says plainly that removing one ingredient does not make a dish safe, because sauces or shared preparation may still contain it. Details I could not confirm with the kitchen are marked as unconfirmed.",
            ], []),
            ("How it works", [
                "The menu search uses local data. Two API requests happen in two different views: one finds the ingredient page, the other loads its introduction. Both show a loading state and clear messages when nothing is found or a request fails.",
                "Saved dishes are stored on the device with AsyncStorage. The save button changes after a successful write, and duplicates are prevented.",
            ], []),
            ("The second version: Study Notes", [
                "For the next assignment I built ServeSmart Study Notes, a local notes app for the same servers. Users create, edit, review and delete study notes, filter by status, and sort by priority or title.",
                "I ran checks on creating, editing, deleting, filtering, sorting and saved data after a reload in the web preview. Native device layout is not verified yet.",
            ], []),
        ],
        "pull": "Removing one ingredient does not make a dish safe.",
        "gallery": [
            "## The app",
            ("phones", [("Banju Menu", "assets/work/servesmart/screen-menu.png"), ("Menu Detail", "assets/work/servesmart/screen-detail.png"), ("Changes and allergy checks", "assets/work/servesmart/screen-allergy.png"), ("Ingredient Guide", "assets/work/servesmart/screen-guide.png")]),
            ("phones", [("Ingredient Reference", "assets/work/servesmart/screen-reference.png"), ("My Study", "assets/work/servesmart/screen-study.png")]),
            "## Demo",
            ("video", "assets/work/servesmart/demo.mp4", "The first minute of the demo recording, running in the iOS simulator."),
            "## Wireframes",
            ("Menu search and dish detail", "is-half", "assets/work/servesmart/wire-a-1.jpg"),
            ("Two API requests in two views", "is-half", "assets/work/servesmart/wire-a-2.jpg"),
            ("Saved items and the navigation map", "is-full", "assets/work/servesmart/wire-a-3.jpg"),
            "## Study Notes",
            ("Study Notes: filtering reviewed notes", "is-half", "assets/work/servesmart/notes-60.jpg"),
            ("Study Notes: deleting a note", "is-half", "assets/work/servesmart/notes-100.jpg"),
            ("Study Notes wireframes: list and empty state", "is-half", "assets/work/servesmart/wire-b-1.jpg"),
            ("Study Notes wireframes: add and edit form", "is-half", "assets/work/servesmart/wire-b-2.jpg"),
        ],
    },
    {
        "slug": "k-sip", "img": "assets/work/ksip/lead.jpg", "lead": "assets/work/ksip/lead.jpg", "color": True, "page": "B3",
        "credit": "K-Sip hi-fi prototype: landing page, product list, product detail and age verification.",
        "title": "K-Sip to Taste Together", "short": "K-Sip and Taste Together",
        "kind": "UI/UX and business model", "when": "BCIT, 2026",
        "deck": "A Korean spirits marketplace I designed and tested, and the party kit business it grew into.",
        "status": "",
        "facts": [("Discipline", "UI/UX design, usability testing, business model"), ("Courses", "MDIA 2540 UI/UX Strategy 1, Enterprise, MDIA 4150 Online Store, BCIT"), ("Team", "Solo"), ("Tools", "Figma, Maze")],
        "sections": [
            ("The problem", [
                "Korean traditional liquor is hard to buy if you do not read Korean. Existing platforms are built for the Korean market and use terms that mean little to someone outside it.",
                "K-Sip is a curated marketplace for people in Canada who want to explore Korean spirits. It describes soju, makgeolli and baekseju the way people already know wine: body, dryness, sweetness. It also suggests food pairings.",
            ], []),
            ("Persona and scenario", [
                "Soohyun, a Korean Canadian graphic designer in Vancouver, is hosting dinner for her colleagues. She wants to serve a Korean spirit with steak but cannot explain the flavours in English. She picks \"Steak\", finds an oak aged soju, reads \"Woody, Smooth\", and adds it to her cart.",
            ], []),
            ("Design", [
                "I mapped the user flow, drew lo-fi wireframes for four screens, and built a hi-fi prototype in Figma. The style guide uses a near black background, an electric lime accent and flavour profile bars, so each bottle reads at a glance.",
            ], []),
            ("Testing with Maze", [], [
                ("Task", "Find a Korean spirit that pairs well with steak and add it to the cart."),
                ("Success", "All 7 participants completed the task. 100 percent success, 0 percent drop off, 29.4 seconds on average."),
                ("Satisfaction", "4.8 out of 5 for \"How easy was it to find a product that matched your needs?\""),
                ("Misclicks", "A 42.5 percent misclick rate, which needed a closer look."),
            ]),
            ("What the misclicks meant", [
                "The heatmap showed people tapping product cards that did nothing. Only the first card had prototype interactions, so every other tap counted as a misclick. The problem was my prototype, not the layout.",
                "I linked every product card to its detail screen after the test. I also noted two limits for the next round: the food pairing filter was not interactive, and testers never reached the age verification step.",
            ], []),
            ("From K-Sip to Taste Together", [
                "In my Enterprise course I developed the idea into a business model, and in MDIA 4150 I reshaped it into Taste Together: an online store for people who host home parties with friends from different cultures.",
                "The host sends one party link. Each guest takes a short taste quiz, and the site suggests a menu and party kits for the whole group, including low and no alcohol options. Selling liquor in BC needs a licence, so the store sells mixer kits, snack boxes and meal kits, and leaves alcohol to licensed stores.",
                "This is a concept. The competitor scores and costs in the plan are planning assumptions, not survey or sales data.",
            ], []),
        ],
        "pull": "The problem was my prototype, not the layout.",
        "gallery": [
            "## K-Sip prototype",
            ("Hi-fi screens: landing page, product list, product detail, age verification", "is-full", "assets/work/ksip/screens.jpg"),
            ("User flow", "is-half", "assets/work/ksip/user-flow.jpg"),
            ("Lo-fi wireframes", "is-half", "assets/work/ksip/wireframes.jpg"),
            ("Style guide: colour, type and components", "is-full", "assets/work/ksip/style-guide.jpg"),
            "## Usability test",
            ("Task results from 7 participants", "is-half", "assets/work/ksip/results.jpg"),
            ("Satisfaction: 4.8 out of 5", "is-half", "assets/work/ksip/satisfaction.jpg"),
            ("Misclick heatmap on the product list", "is-full", "assets/work/ksip/heatmap.jpg"),
            "## Taste Together",
            ("Lean canvas. Figures are planning assumptions.", "is-half", "assets/work/ksip/lean-canvas.jpg"),
            ("Perceptual map. Scores are my own estimates, not survey results.", "is-half", "assets/work/ksip/perceptual-map.jpg"),
        ],
    },
    {
        "slug": "fruity-lab", "img": "assets/work/fruitylab/lead.jpg", "lead": "assets/work/fruitylab/lead.jpg", "color": True, "page": "B4",
        "credit": "Fruity Lab style guide: logo lockups and the mood based colour system.",
        "title": "Fruity Lab", "short": "Fruity Lab",
        "kind": "Brand identity", "when": "BCIT",
        "deck": "A branding package for a creative brand that turns three moods into three fruits, each with its own palette.",
        "status": "",
        "facts": [("Discipline", "Brand identity"), ("Type", "School project, BCIT"), ("Team", "Solo"), ("Pieces", "Logo system, colour system, typography, applications")],
        "sections": [
            ("The idea", [
                "Fruity Lab is a creative brand that shows contrasting moods through minimal, fruit inspired design. It runs on three moods, and each one has a fruit: Tomato for energy, Fig for emotion, Cherry for clarity.",
            ], []),
            ("Three moods", [], [
                ("Tomato", "Bold, contrast, experimental."),
                ("Fig", "Warm, organic, soft."),
                ("Cherry", "Minimal, modern, balanced."),
            ]),
            ("Colour", [
                "Instead of one brand colour, Fruity Lab has a palette for each mood. I sampled the colours from a moodboard for each mood, then refined them with contrast and accessibility checks.",
            ], []),
            ("The logo", [
                "I sketched fruit forms by hand and looked for a shape that could hold both halves of the name. The final mark is a fruit that is also a laboratory flask, with a leaf on top. It works in horizontal and vertical lockups.",
            ], []),
            ("Type and applications", [
                "Montserrat sets the headlines, Playfair Display the subheads and Poppins the body text. I applied the identity to a shop sign, a sweatshirt, business cards and pins.",
            ], []),
        ],
        "pull": "A palette for each mood instead of one brand colour.",
        "gallery": [
            "## Logo",
            ("Fruit form experiments", "is-half", "assets/work/fruitylab/logo-sketches.jpg"),
            ("From first concept to final mark", "is-half", "assets/work/fruitylab/logo-system.jpg"),
            ("Logo lockups", "is-full", "assets/work/fruitylab/logo-lockups.jpg"),
            "## System",
            ("Colour system: energy, emotion and clarity palettes", "is-half", "assets/work/fruitylab/colour-system.jpg"),
            ("Typography system", "is-half", "assets/work/fruitylab/typography.jpg"),
            "## Applications",
            ("Shop sign", "is-half", "assets/work/fruitylab/sign.jpg"),
            ("Sweatshirt", "is-half", "assets/work/fruitylab/sweatshirt.jpg"),
            ("Business cards", "is-half", "assets/work/fruitylab/cards.jpg"),
            ("Pins", "is-half", "assets/work/fruitylab/pins.jpg"),
        ],
    },
    {
        "slug": "xbox-launch-campaign", "img": "assets/img/xbox.jpg", "page": "C1",
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
]

HELD = []

EXPERIENCE = [
    ("Now", "New Media Design and Web Development, BCIT", "Full time student in Vancouver, building this portfolio toward an internship."),
    ("2022 to 2023", "Project manager, BrandworksKorea", "Overseas sourcing team at a CJ ENM affiliate in Seoul."),
    ("2019 to 2022", "Product manager for Xbox", "At a Microsoft distributor in Korea, through the launch of Xbox Series X and Series S."),
]
# ─────────────────────── END CONTENT ───────────────────────

e = html.escape


def asset_v(path):
    import hashlib
    return hashlib.md5((ROOT / path).read_bytes()).hexdigest()[:8]
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
<link rel="stylesheet" href="css/dispatch.css?v={asset_v("css/dispatch.css")}">
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
<script src="js/main.js?v={asset_v("js/main.js")}" defer></script>
</body>
</html>
"""


def thumb_ok(s):
    return bool(s.get('thumb')) and (ROOT / s['thumb']).exists()


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
      <div class="pic{' pic--color' if s.get('color') and not thumb_ok(s) else ''}"><img src="{s['thumb'] if thumb_ok(s) else s['img']}" alt="" loading="lazy"></div>
      <div><p class="kicker kicker--red">{e(s['kind'])}, {e(s['when'])}</p><h3 class="story__title"><span>{e(s['title'])}</span></h3><p class="story__deck">{e(s['deck'])}</p></div></a></li>
"""
    rows = card(STORIES[0], "story--feature") + card(STORIES[1], "story--left") + card(STORIES[2], "story--right")
    held = "".join(f'<span><a class="textlink" href="{x["slug"]}.html"><b>{e(x["short"])}</b></a> <span>{e(x["kind"])}</span></span>' for x in STORIES[3:])
    held += "".join(f"<span><b>{e(t)}</b> <span>{e(k)}</span></span>" for t, k in HELD)
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
        <div class="pic"><img src="assets/img/cover-printed.jpg" alt="A person holds open a newspaper called The Diana Dispatch. The headline reads: Designer seeks internship."></div>
        <canvas class="reveal" data-src="assets/img/reveal.webp" aria-hidden="true"></canvas>
        <svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false"><filter id="goo"><feGaussianBlur stdDeviation="14"/><feColorMatrix values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 24 -10"/></filter></svg>
        <p class="cover__note pen" aria-hidden="true"><svg viewBox="0 0 60 40"><path d="M56 6 C 40 4, 18 10, 6 30 M6 30 l2 -11 M6 30 l11 -3"/></svg>that's me</p>
        <div class="scraps">{scraps}</div>
      </figure>
      <p class="credit stage__hint">Move your cursor over the newspaper to see who is behind it. The clippings are loose too: grab one and throw it. Photo illustration made with Higgsfield.</p>
    </div>
  </section>

  <section class="section wrap" id="work">
    <div class="section__head"><h2 class="section__title">In this edition</h2><p class="kicker">Selected work</p></div>
    <ul class="stories">
{rows}      <li class="held"><span class="kicker kicker--red">Also in this edition</span>{held}</li>
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
    gal = ""
    for g in s["gallery"]:
        if isinstance(g, tuple) and g[0] == "video":
            gal += f'<div class="proto"><video src="{g[1]}" controls muted playsinline preload="metadata" class="demo"></video><p class="credit">{e(g[2])}</p></div>'
            continue
        if isinstance(g, tuple) and g[0] == "embed":
            gal += f'<div class="proto"><iframe src="{e(s["embed"])}" title="{e(s["title"])} prototype in Figma" loading="lazy" allowfullscreen></iframe><p class="credit">Tap through the live prototype. If it does not load, <a href="{e(s["link"][1])}" rel="noopener">open it in a new tab</a>.</p></div>'
            continue
        if isinstance(g, tuple) and g[0] == "phones":
            gal += '<div class="phones">' + "".join(f'<figure class="phone"><a href="{img}" aria-label="Open {e(cap)} full size"><img src="{img}" alt="{e(cap)}" loading="lazy" width="390" height="844"></a><figcaption class="credit">{e(cap)}</figcaption></figure>' for cap, img in g[1]) + '</div>'
            continue
        if isinstance(g, str):
            gal += f'<h2 class="gallery__title">{e(g[3:])}</h2>'
        elif g[2].startswith("assets/work/"):
            cap, cls, img = g
            gal += f'<figure class="work {cls}"><a href="{img}" aria-label="Open {e(cap)} full size"><img src="{img}" alt="{e(cap)}" loading="lazy"></a><figcaption class="credit">{e(cap)}</figcaption></figure>'
        else:
            gal += frame(*g)
    color = " pic--color" if s.get("color") else ""
    status = f'<span class="status pen">{e(s["status"])}</span>' if s.get("status") else ""
    link = f'<p style="margin-top:1rem"><a class="btn" href="{s["link"][1]}" rel="noopener">{e(s["link"][0])}</a></p>' if s.get("link") else ""
    return head(s["title"], s["deck"]) + top("work") + f"""<main id="main">
  <article class="wrap">
    <header class="article__head">
      <div><a class="article__section kicker kicker--red" href="index.html#work">{e(s['kind'])}, {e(s['when'])}</a>
      <h1 class="article__title">{e(s['title'])}</h1></div>
      <div><p class="article__deck">{e(s['deck'])}</p>{status}{link}</div>
    </header>
    <figure class="leadpic"><div class="pic{color}"><img src="{s.get('lead', s['img'])}" alt="{e(s.get('credit', ''))}"></div><figcaption class="credit">{e(s.get('credit', ILLUSTRATION))}</figcaption></figure>
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
