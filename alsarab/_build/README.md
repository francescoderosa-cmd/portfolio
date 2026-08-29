# Al Sarab — proposal site generator

Generates the 57-page static site served at `/alsarab/`.
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
| `pages2.py` | events, news, about, studios, fees, FAQ, contact, performances, rental, private, programmes, terms, portal, Arabic. |
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

Five top-level items. Two of them exist to keep apart things the visitor would
otherwise confuse:

- **Events** — what the school itself puts on: recitals, workshops, the archive.
- **Hire us** — what the school sells: `performances.html` (weddings, parties,
  galas, commissioned shows), private sessions, programmes, studio rental.

Before this split, the four commercial pages lived only in the footer and there was
nowhere to say that Al Sarab performs at other people's events.

Source photographs live in `assets/img/` and come from Al Sarab's own gallery
(the 2019 production at Metro Al Madina, Beirut).

## Structure

The layout, page set and module inventory follow usc.se as a working reference
for this draft. Colour, type and identity are meant to diverge before this goes
anywhere public.

## Open question for the client

`performances.html` ("Hire us") sells Al Sarab as performers for weddings, parties
and commissioned shows. **It is not settled whether the dancers are Al Sarab Dance
Company — which tours separately — or ensembles drawn from the school.** The copy
says "Al Sarab" throughout so it reads correctly either way, and the Ensemble row in
the page's facts box carries a visible "To confirm" chip. Settle this and the wording
tightens in one pass; see the note at the top of `PERFORMANCE_FORMATS` in `data.py`.
