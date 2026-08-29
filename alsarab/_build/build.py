# -*- coding: utf-8 -*-
"""Build the Al Sarab proposal site.

    py -3 build.py <output-dir>

Writes a complete static site: HTML pages, assets/site.css, assets/site.js,
assets/schedule.js and assets/img/*.jpg.
"""

import os
import shutil
import sys

import theme
import data
import pages
import pages2
import pages3

HERE = os.path.dirname(os.path.abspath(__file__))
IMG_SRC = os.path.abspath(os.path.join(HERE, "..", "img"))


def write(out, rel, html):
    path = os.path.join(out, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
    return rel


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "site")
    out = os.path.abspath(out)

    # clean everything we generate, leave anything else alone
    for rel in ("assets", "dance-styles", "instructors", "events", "news", "studios"):
        p = os.path.join(out, rel)
        if os.path.isdir(p):
            shutil.rmtree(p)
    for name in os.listdir(out) if os.path.isdir(out) else []:
        if name.endswith(".html"):
            os.remove(os.path.join(out, name))

    os.makedirs(os.path.join(out, "assets"), exist_ok=True)

    # ---- assets
    with open(os.path.join(out, "assets", "site.css"), "w", encoding="utf-8", newline="\n") as f:
        f.write(theme.CSS)
    with open(os.path.join(out, "assets", "site.js"), "w", encoding="utf-8", newline="\n") as f:
        f.write(theme.JS)
    with open(os.path.join(out, "assets", "schedule.js"), "w", encoding="utf-8", newline="\n") as f:
        f.write(theme.SCHEDULE_JS)
    with open(os.path.join(out, "assets", "merch.js"), "w", encoding="utf-8", newline="\n") as f:
        f.write(theme.MERCH_JS)

    dest_img = os.path.join(out, "assets", "img")
    os.makedirs(dest_img, exist_ok=True)
    for name in sorted(os.listdir(IMG_SRC)):
        if name.endswith(".jpg"):
            shutil.copy2(os.path.join(IMG_SRC, name), os.path.join(dest_img, name))

    made = []

    # ---- main nav: Home / School / Hire Us / Merchandising / Summer Camp / Contacts
    made.append(write(out, "index.html", pages.home()))
    made.append(write(out, "about.html", pages2.about_page()))          # School > History & info
    made.append(write(out, "instructors.html", pages.teachers_index()))  # School > The Teachers
    made.append(write(out, "classes.html", pages.classes_page()))        # School > Classes
    made.append(write(out, "portal.html", pages2.portal_page()))         # School > Portal
    made.append(write(out, "hire-us.html", pages3.hire_us_page()))
    made.append(write(out, "merchandising.html", pages3.merch_page()))
    made.append(write(out, "summer-camp.html", pages3.camp_page()))
    made.append(write(out, "contact.html", pages2.contact_page()))

    # ---- secondary: reachable from the footer, not in the main nav
    made.append(write(out, "events.html", pages2.events_index()))
    made.append(write(out, "news.html", pages2.news_index()))
    made.append(write(out, "pricing.html", pages2.pricing_page()))
    made.append(write(out, "faq.html", pages2.faq_page()))
    made.append(write(out, "terms.html", pages2.terms_page()))
    made.append(write(out, "ar.html", pages2.arabic_page()))

    # ---- detail pages
    for g in data.GENRES:
        made.append(write(out, "dance-styles/%s.html" % g["slug"], pages.style_detail(g)))
    for t in data.TEACHERS:
        made.append(write(out, "instructors/%s.html" % t["slug"], pages.teacher_detail(t)))
    for e in data.EVENTS:
        made.append(write(out, "events/%s.html" % e["slug"], pages2.event_detail(e)))
    for n in data.NEWS:
        made.append(write(out, "news/%s.html" % n["slug"], pages2.news_detail(n)))

    print("%d pages written to %s" % (len(made), out))
    for rel in made:
        print("  " + rel.replace("\\", "/"))


if __name__ == "__main__":
    main()
