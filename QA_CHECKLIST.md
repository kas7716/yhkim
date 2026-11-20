# QA Checklist: The Diana Dispatch (Portfolio)

MDIA 4590 Quality Assurance, Assignment 2
Tester and developer: Diana Kim (@kas7716)
Site: https://kas7716.github.io/yhkim/
Repository: https://github.com/kas7716/yhkim
Issue tracking: [GitHub Issues](https://github.com/kas7716/yhkim/issues)

## How bugs are managed

Bugs follow the status flow from Week 5:

1. A bug is submitted as a GitHub Issue with the `open` label, written in the Week 4 bug report format (Title, Status, Description, Steps to Reproduce, Expected Results, Actual Results, Configuration, Priority, Severity, Type, Assignee).
2. QA reviews it. If it does not meet the requirements of a bug, it gets the `rejected` label and is closed.
3. The bug is assigned to the developer (Diana) and fixed in a commit that references it (`Fixes #n`).
4. The developer comments on how it was fixed, adds the `retest` label and reassigns the issue to the instructor (QA).
5. QA retests with the Steps to Reproduce, removes `retest` and closes the issue.

Labels: `severity: high / medium / low`, `priority: high / medium / low`, `type: bug`, one `area:` label per checklist section, and the status labels `open`, `retest`, `rejected`.

Severity and priority use the Week 4 definitions. Severity: Low is a small visual issue with a workaround, Medium affects the workflow but has a workaround, High has no workaround or puts data at risk. Priority: Low has no timeline, Medium must be fixed before the next major release, High must be fixed before any code is deployed.

## Supported configurations

| Browser (latest stable) | Desktop | Mobile |
|---|---|---|
| Chrome (Blink) | macOS, Windows 11 | Android |
| Safari (WebKit) | macOS | iOS, iPadOS |
| Firefox (Gecko) | macOS, Windows 11 | |
| Edge (Blink) | Windows 11 | |

Breakpoints tested: 375, 768, 1024, 1440 px. Connections: WiFi and DevTools Slow 4G.
Tools: Chrome DevTools (Elements, Console, Network, Lighthouse, device toolbar), Safari Web Inspector, Firefox DevTools, WAVE, caniuse.com, WhatFont, Grammarly, View Source.

Result key: Pass, Fail (with issue number), N/A.

## 1. Portfolio requirements

| # | Task | Method | Result |
|---|---|---|---|
| 1.1 | Home page introduces who I am and what I do above the fold | Visual check at 1440 and 375 px | Pass |
| 1.2 | At least the required number of projects are listed, each linking to its own case study | Click every card in "In this edition" | Pass |
| 1.3 | Every case study has a brief, my role, tools, timeline and process images | Read each project page | Pass |
| 1.4 | About page has a photo, profile and experience | Read about.html | Pass |
| 1.5 | Contact options work: email opens a mail client, LinkedIn opens the right profile | Click each contact link | Pass |
| 1.6 | Resume is available to download from the site | Search every page for a resume link | Fail [#2](https://github.com/kas7716/yhkim/issues/2) |
| 1.7 | Every project page has a "Next story" link so there are no dead ends | Click "Next story" on all 7 pages | Pass |
| 1.8 | Custom 404 page exists and helps the visitor get back | Open a URL that does not exist, at root and one folder deep | Fail [#1](https://github.com/kas7716/yhkim/issues/1) |

## 2. Browser support and responsiveness

| # | Task | Method | Result |
|---|---|---|---|
| 2.1 | Layout matches the design in Chrome, Safari, Firefox and Edge | Open home, one project and about in each browser | Pass |
| 2.2 | No horizontal scroll at 375, 768, 1024 and 1440 px | DevTools device toolbar | Pass |
| 2.3 | Navigation bar and anchor links (#work, #letters, #contact) work on every page | Click each nav item | Pass |
| 2.4 | CSS features used are supported or fail gracefully (text-wrap, aspect-ratio, clamp, inset) | caniuse.com for each feature in dispatch.css | Pass |
| 2.5 | Custom fonts (Fraunces, Archivo, Nanum Pen Script) load in every browser | WhatFont, Network tab | Pass |
| 2.6 | Interactive pieces (cover reveal, draggable clippings, ticker) work with mouse and touch | Desktop browsers and DevTools touch emulation | Fail [#10](https://github.com/kas7716/yhkim/issues/10) |
| 2.7 | prefers-reduced-motion stops the ticker and animations | DevTools Rendering, emulate reduced motion | Pass |
| 2.8 | Video in ServeSmart plays inline on iOS Safari (muted, playsinline) | iOS Simulator or iPhone | Pass |
| 2.9 | Figma prototype embeds load, with a fallback link | Open First7 and K-Sip pages | Pass |

## 3. Code optimization

| # | Task | Method | Result |
|---|---|---|---|
| 3.1 | No console errors or warnings on any page | DevTools Console on all 10 pages | Pass |
| 3.2 | No broken internal links, images or anchors | Automated link check of every href and src | Pass |
| 3.3 | Images are sized for how they are displayed and compressed | Network tab, filter Img, compare file size with display size | Fail [#8](https://github.com/kas7716/yhkim/issues/8) |
| 3.4 | Images have width and height to prevent layout shift | Lighthouse Performance, CLS audit | Fail [#7](https://github.com/kas7716/yhkim/issues/7) |
| 3.5 | Images below the fold use loading="lazy" | View Source | Pass |
| 3.6 | Only files used by the site are deployed | Search the code for every file in assets/ | Fail [#9](https://github.com/kas7716/yhkim/issues/9) |
| 3.7 | Styles live in the stylesheet, not in inline style attributes | Search the generated HTML for style=" | Fail [#11](https://github.com/kas7716/yhkim/issues/11) |
| 3.8 | CSS and JS are cache busted when they change (?v= hash) | View Source after a change | Pass |
| 3.9 | Fonts are preloaded and use woff2 | View Source, Network tab | Pass |
| 3.10 | Scripts use defer or type="module" so they do not block rendering | View Source | Pass |

## 4. CMS support

The site has no third party CMS. Content is managed in one place, the CONTENT section of `tools/build.py`, and the guestbook uses Firebase Firestore.

| # | Task | Method | Result |
|---|---|---|---|
| 4.1 | Changing text in the CONTENT section and running the build updates every page | Edit one deck line, run `python3 tools/build.py`, compare | Pass |
| 4.2 | Adding an image path to a gallery entry shows it on the page with its caption as alt text | Add one test image, rebuild | Pass |
| 4.3 | README explains how to edit content and run the build | Read README.md | Pass |
| 4.4 | Guestbook letter can be sent, shows on the page and respects the 300 character limit | Send a test letter | Pass |
| 4.5 | Only the owner account can delete letters (enforced by firestore.rules) | Try Delete while signed out and signed in | Pass |
| 4.6 | Guestbook and counter stay hidden if Firebase fails to load | Block gstatic.com in DevTools Network request blocking | Pass |

## 5. Metadata and SEO

| # | Task | Method | Result |
|---|---|---|---|
| 5.1 | Every page has a unique, descriptive title | View Source on all pages | Pass |
| 5.2 | Every page has a unique meta description | View Source | Pass |
| 5.3 | html lang="en" and viewport meta are set | View Source | Pass |
| 5.4 | Favicon shows in the browser tab | Open the site in each browser | Pass |
| 5.5 | og:image matches each page | View Source, LinkedIn Post Inspector | Fail [#3](https://github.com/kas7716/yhkim/issues/3) |
| 5.6 | og:url matches each page | View Source | Fail [#4](https://github.com/kas7716/yhkim/issues/4) |
| 5.7 | Every page has a canonical link | View Source | Fail [#5](https://github.com/kas7716/yhkim/issues/5) |
| 5.8 | sitemap.xml and robots.txt exist | Open both URLs | Fail [#6](https://github.com/kas7716/yhkim/issues/6) |
| 5.9 | Heading order is logical, one h1 per page | WAVE structure panel | Pass |

## 6. Content accuracy and quality

| # | Task | Method | Result |
|---|---|---|---|
| 6.1 | No spelling or grammar errors | Grammarly on every page | Pass |
| 6.2 | Project names are the same everywhere (title, card, index, tab) | Compare home index, cards and page titles | Fail [#12](https://github.com/kas7716/yhkim/issues/12) |
| 6.3 | Dates, roles and company names match the resume | Compare about.html and project facts with the resume PDF | Pass |
| 6.4 | Every image has meaningful alt text, decorative images use alt="" | WAVE, View Source | Pass |
| 6.5 | No placeholder text ("photo to come", lorem ipsum) is left on live pages | Search the generated HTML | Pass |
| 6.6 | Image credits explain AI generated illustrations | Read captions on the home cover | Pass |
| 6.7 | External links (LinkedIn, Figma) open the correct page | Click each link | Pass |

## 7. Accessibility

| # | Task | Method | Result |
|---|---|---|---|
| 7.1 | WAVE shows no errors | WAVE on every page | Pass |
| 7.2 | Text contrast meets WCAG 2.2 AA (4.5:1) | WAVE contrast panel | Pass |
| 7.3 | Every interactive element is reachable and visible with the keyboard | Tab through each page | Pass |
| 7.4 | Skip to content link works | Tab once, press Enter | Pass |
| 7.5 | Moving content can be paused (WCAG 2.2.2) | Try to pause the ticker with mouse, keyboard and touch | Fail [#10](https://github.com/kas7716/yhkim/issues/10) |
| 7.6 | Screen reader reads the page in a sensible order | VoiceOver on macOS | Pass |

## 8. Configuration and deployment

| # | Task | Method | Result |
|---|---|---|---|
| 8.1 | Site loads over HTTPS on GitHub Pages | Open the live URL | Pass |
| 8.2 | Paths work under the /yhkim/ project folder | Open pages and a nested missing URL | Fail [#1](https://github.com/kas7716/yhkim/issues/1) |
| 8.3 | main branch only holds tested code; each fix is a small commit that references its issue | GitHub commit history | Pass |

## Bug summary

| Issue | Title | Area | Severity | Priority |
|---|---|---|---|---|
| [#1](https://github.com/kas7716/yhkim/issues/1) | 404 page loses its CSS, fonts and links on nested URLs | Configuration | Medium | High |
| [#2](https://github.com/kas7716/yhkim/issues/2) | Resume PDF is not linked anywhere on the site | Portfolio requirements | Medium | High |
| [#3](https://github.com/kas7716/yhkim/issues/3) | Every project page shares the home page og:image | Metadata | Low | Medium |
| [#4](https://github.com/kas7716/yhkim/issues/4) | og:url points to the home page on every page | Metadata | Low | Medium |
| [#5](https://github.com/kas7716/yhkim/issues/5) | No canonical link on any page | Metadata | Low | Low |
| [#6](https://github.com/kas7716/yhkim/issues/6) | sitemap.xml and robots.txt are missing | Metadata | Low | Low |
| [#7](https://github.com/kas7716/yhkim/issues/7) | Images have no width and height | Code optimization | Low | Medium |
| [#8](https://github.com/kas7716/yhkim/issues/8) | Home page thumbnails are oversized | Code optimization | Medium | Medium |
| [#9](https://github.com/kas7716/yhkim/issues/9) | Unused image files are deployed | Code optimization | Low | Low |
| [#10](https://github.com/kas7716/yhkim/issues/10) | News ticker cannot be paused on touch devices | Accessibility | Medium | Medium |
| [#11](https://github.com/kas7716/yhkim/issues/11) | Inline style attributes in the page templates | Code optimization | Low | Low |
| [#12](https://github.com/kas7716/yhkim/issues/12) | K-Sip project name is inconsistent | Content | Low | Low |

All 12 bugs were fixed, commented on and labelled `retest` for the instructor.
