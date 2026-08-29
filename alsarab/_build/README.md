# Al Sarab — proposal site generator

Generates the static site served at `/alsarab/` (49 pages).
The folder is named `_build/` so GitHub Pages (Jekyll) never publishes it.

## Rebuild

From this folder:

```
py -3 build.py ..
py -3 check.py ..
```

`build.py` deletes and rewrites only what it generates (`*.html` at the top level
plus `assets/`, `dance-styles/`, `instructors/`, `events/`, `news/`, `studios/`).
`check.py` re-walks the output and fails on broken internal links, missing assets,
pages without a `<title>`, or text that Jekyll would try to interpret.

## Files

| file | what's in it |
|---|---|
| `theme.py` | all CSS and JS. **The whole palette is the `:root` block at the top** — change those tokens and the identity changes across every page. |
| `data.py` | all content: school facts, teachers, genres, timetable, events, news, FAQ, performance formats. Marked at the top with what is real (from alsarabdance.com) and what is placeholder. |
| `shell.py` | page chrome — head, promo banner, nav model, footer, shared fragments. |
| `pages.py` | home, booking, schedule, drop-in, today, genres, teachers. |
| `pages2.py` | events, news, about, fees, FAQ, contact, terms, portal, Arabic. Also holds the retired page builders (studios, rental, private, programmes, performances) — no longer called from `build.py`, kept in case a section comes back. |
| `pages3.py` | Hire Us, Merchandising, Summer Camp. |
| `build.py` | writes every page and copies `assets/img/`. |
| `check.py` | post-build verification. |

## Palette

Lilac-led, taken from the mark in Al Sarab's own logo (`#B6A8D4`).

| token | light | dark | role |
|---|---|---|---|
| `--brand` | `#5F4F9B` | `#B6A8D4` | the identity. The logo lilac is too light to carry text on a light ground, so light mode uses the same hue pushed down; dark mode uses the logo value itself. |
| `--on-brand` | `#FBF9FF` | `#1B1430` | text on a brand-filled surface. Flips with the theme — without it, buttons drop to 2.1:1 in dark mode. |
| `--ember` | `#B4573C` | `#DE9174` | the one warm counter-note, pulled from the red costumes in the photography. Level chips only. |
| `--bg` `--bg-2` `--bg-3` | `#E7E2F1` `#DDD6EC` `#CEC5E4` | `#120D1C` `#1A1329` `#261C3C` | grounds. Lilac-tinted, not grey. |
| `--ink` `--ink-2` | `#241C38` `#5F5480` | `#EFE9FA` `#B0A4CE` | text. |
| `--deep` `--on-deep` | `#140E1E` `#F0EAFA` | same | hero scrims, promo bar, footer — fixed in both themes. |

Contrast checked in both themes: body text 12.8:1 / 16.1:1, secondary text 5.4:1 / 8.2:1,
brand on ground 5.4:1 / 8.7:1, button label on brand 6.5:1 / 8.0:1.

## Navigation

Six top-level items, agreed with the school:

| nav | page | contains |
|---|---|---|
| Home | `index.html` | hero, six launch modules into the rest of the site, then the standing sections |
| School ▾ | — | History & info (`about.html`), The Teachers (`instructors.html`), Classes (`classes.html`), Student & parent portal (`portal.html`) |
| Hire Us | `hire-us.html` | one page, four services: Weddings, Videos, Choreography, Studio booking |
| Merchandising | `merchandising.html` | reserve-only shop list |
| Summer Camp | `summer-camp.html` | next camp first, last camp below |
| Contacts | `contact.html` | phone, email, form |

**Classes is one page, not three.** It carries the programmes (the six genres),
the levels and ages, the class calendar (`#calendar`), the walk-in trial form
(`#trial`) and the fee cards. The old `schedule.html`, `today.html`,
`drop-in.html` and `dance-styles.html` were folded into it and are no longer built.

**Hire Us is one page, not four.** `performances.html`, `private-events.html`,
`corporate-programmes.html` and `studio-rental.html` were folded into it as the
four service blocks and are no longer built. Every service button goes to one
shared `#request` form — nothing is priced or paid online anywhere on the site.

### Pages kept but out of the main nav

`events.html` (+ 6 details), `news.html` (+ 6 details), `pricing.html`, `faq.html`,
`terms.html`, `ar.html`. They were not in the structure the school gave us, but
deleting them would throw away work, so they live in the footer under **More**
until someone decides. Say the word and one line in `build.py` drops each one.

Source photographs live in `assets/img/` and come from Al Sarab's own gallery
(the 2019 production at Metro Al Madina, Beirut).

## Structure

The layout, page set and module inventory follow usc.se as a working reference
for this draft. Colour, type and identity are meant to diverge before this goes
anywhere public.

## Open question for the client

`hire-us.html` sells Al Sarab as performers for weddings, videos and commissioned
choreography. **It is not settled whether the dancers are Al Sarab Dance Company —
which tours separately — or ensembles drawn from the school.** The copy says
"Al Sarab" throughout so it reads correctly either way, and the last item in the
page FAQ is flagged as a placeholder for exactly this. Settle it and the wording
tightens in one pass; see the note above `HIRE_SERVICES` in `data.py`.
