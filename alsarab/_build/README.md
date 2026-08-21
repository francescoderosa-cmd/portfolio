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
| `theme.py` | all CSS and JS. **The whole palette is the `:root` block at the top** — change those tokens and the identity changes across all 57 pages. |
| `data.py` | all content: school facts, teachers, genres, timetable, events, news, FAQ. Marked at the top with what is real (from alsarabdance.com) and what is placeholder. |
| `shell.py` | page chrome — head, promo banner, nav model, footer, shared fragments. |
| `pages.py` | home, booking, schedule, drop-in, today, genres, teachers. |
| `pages2.py` | events, news, about, studios, fees, FAQ, contact, rental, private, programmes, terms, portal, Arabic. |
| `build.py` | writes every page and copies `assets/img/`. |
| `check.py` | post-build verification. |

Source photographs live in `assets/img/` and come from Al Sarab's own gallery
(the 2019 production at Metro Al Madina, Beirut).

## Structure

The layout, page set and module inventory follow usc.se as a working reference
for this draft. Colour, type and identity are meant to diverge before this goes
anywhere public.
