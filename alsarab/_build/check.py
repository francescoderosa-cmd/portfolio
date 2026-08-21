# -*- coding: utf-8 -*-
"""Verify the built site: internal links, asset references, Liquid-unsafe text."""

import os
import re
import sys

OUT = os.path.abspath(sys.argv[1])

href_re = re.compile(r'(?:href|src)="([^"]+)"')
url_re = re.compile(r'url\((?:&quot;|")?([^)"&]+)')

bad_links, bad_assets, liquid, no_title, missing_alt = [], [], [], [], []
pages = []

for root, dirs, files in os.walk(OUT):
    for name in files:
        if not name.endswith(".html"):
            continue
        path = os.path.join(root, name)
        rel = os.path.relpath(path, OUT).replace("\\", "/")
        pages.append(rel)
        html = open(path, encoding="utf-8").read()
        folder = os.path.dirname(path)

        if "{{" in html or "{%" in html:
            liquid.append(rel)
        if "<title>" not in html:
            no_title.append(rel)

        for target in href_re.findall(html) + url_re.findall(html):
            if target.startswith(("http", "mailto:", "tel:", "#", "data:")):
                continue
            clean = target.split("#")[0].split("?")[0]
            if not clean:
                continue
            resolved = os.path.normpath(os.path.join(folder, clean))
            if not os.path.exists(resolved):
                (bad_assets if "assets/" in clean else bad_links).append((rel, target))

print("pages: %d" % len(pages))


def report(title, rows):
    if rows:
        print("\n%s (%d):" % (title, len(rows)))
        for r in rows[:25]:
            print("  ", r)
    else:
        print("%s: none" % title)


report("liquid-unsafe pages", liquid)
report("pages without <title>", no_title)
report("broken internal links", bad_links)
report("broken asset refs", bad_assets)

total = len(liquid) + len(no_title) + len(bad_links) + len(bad_assets)
print("\nRESULT: %s" % ("OK" if total == 0 else "%d problems" % total))
sys.exit(1 if total else 0)
