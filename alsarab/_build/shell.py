# -*- coding: utf-8 -*-
"""Page chrome: <head>, promo banner, nav, footer, and small HTML helpers."""

from data import SITE, FOOTER_ABOUT, TEACHERS, GENRES
import theme

# ---------------------------------------------------------------- nav model
NAV = [
    ("HOME", "index.html", None),
    ("SCHOOL", None, [
        ("History &amp; info", "about.html"),
        ("The Teachers", "instructors.html"),
        ("Classes", "classes.html"),
        ("Student &amp; parent portal", "portal.html"),
    ]),
    ("HIRE US", "hire-us.html", None),
    ("MERCHANDISING", "merchandising.html", None),
    ("SUMMER CAMP", "summer-camp.html", None),
    ("CONTACTS", "contact.html", None),
]

FOOTER_NAV = [
    ("School", [("History &amp; info", "about.html"), ("The Teachers", "instructors.html"),
                ("Classes &amp; calendar", "classes.html"),
                ("Book a trial", "classes.html#trial"),
                ("Student &amp; parent portal", "portal.html")]),
    ("Services", [("Hire us", "hire-us.html"), ("Weddings", "hire-us.html#weddings"),
                  ("Videos", "hire-us.html#videos"),
                  ("Choreography", "hire-us.html#choreography"),
                  ("Studio booking", "hire-us.html#studio-booking")]),
    ("More", [("Merchandising", "merchandising.html"), ("Summer Camp", "summer-camp.html"),
              ("Events", "events.html"), ("News &amp; stories", "news.html"),
              ("FAQ", "faq.html")]),
]

# ---------------------------------------------------------------- icons
IC_IG = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true">'
         '<rect x="2.5" y="2.5" width="19" height="19" rx="5.5"/><circle cx="12" cy="12" r="4.2"/>'
         '<circle cx="17.6" cy="6.4" r="1.1" fill="currentColor" stroke="none"/></svg>')
IC_FB = ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M13.5 21v-8h2.7l.4-3.1'
         'h-3.1V7.9c0-.9.25-1.5 1.55-1.5H16.7V3.6c-.3-.04-1.3-.13-2.47-.13-2.45 0-4.13 1.5-4.13 4.24V9.9'
         'H7.4V13h2.7v8z"/></svg>')
IC_YT = ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M22.2 7.2a2.7 2.7 0 0 '
         '0-1.9-1.9C18.6 4.8 12 4.8 12 4.8s-6.6 0-8.3.5A2.7 2.7 0 0 0 1.8 7.2C1.3 8.9 1.3 12 1.3 12s0 3.1'
         '.5 4.8a2.7 2.7 0 0 0 1.9 1.9c1.7.5 8.3.5 8.3.5s6.6 0 8.3-.5a2.7 2.7 0 0 0 1.9-1.9c.5-1.7.5-4.8'
         '.5-4.8s0-3.1-.5-4.8M9.9 15.2V8.8l5.5 3.2z"/></svg>')
ARROW = ('<svg class="arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
         'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14"/>'
         '<path d="m12 5 7 7-7 7"/></svg>')
CHEV = ('<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" '
        'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>')


def mark(stroke_var="--bg"):
    return ('<svg viewBox="0 0 48 48" aria-hidden="true"><circle cx="24" cy="24" r="22" fill="currentColor"/>'
            '<g fill="none" stroke="var(%s)" stroke-width="3" stroke-linecap="round">'
            '<path d="M9 19c5-4 11-4 16 0s11 4 16 0"/><path d="M9 27c5-4 11-4 16 0s11 4 16 0"/>'
            '<path d="M13 35c4-2.6 8-2.6 12 0"/></g></svg>' % stroke_var)


def brand(base, stroke="--bg"):
    return ('<a class="brand" href="%sindex.html" aria-label="%s &mdash; home">%s'
            '<span class="brand-tx"><span class="brand-ar">%s</span>'
            '<span class="brand-en">AL SARAB</span></span></a>'
            % (base, SITE["full"], mark(stroke), SITE["arabic"]))


def link(base, href):
    return href if href.startswith(("http", "mailto:", "tel:", "#")) else base + href


def app_cta(base, label="Open the app"):
    """CTA for the student & parent web app.

    SITE["portal_url"] is empty until the app is published. Rather than ship a
    button that goes nowhere, render it inert and say why. Both branches return a
    single inline-flex wrapper, so this drops into a flex row as one item.
    """
    if SITE["portal_url"]:
        inner = ('<a class="btn btn-primary" href="%s" target="_blank" rel="noopener">%s%s</a>'
                 % (SITE["portal_url"], label, ARROW))
    else:
        inner = ('<span class="btn btn-primary" aria-disabled="true">%s</span>'
                 '<span class="tag todo">Link to come</span>' % label)
    return '<span class="cta-wrap">%s</span>' % inner


# ---------------------------------------------------------------- chrome
def promo():
    return (
        '<div class="promo" id="promo"><div class="container">'
        '<p><b>Design proposal.</b> Structure, layout and modules only &mdash; timetable, fees, '
        'studio specifications and some copy are placeholders for review.</p>'
        '<button type="button" aria-label="Dismiss notice">&times;</button>'
        '</div></div>')


def nav(base, active):
    items = []
    for label, href, drop in NAV:
        if drop:
            inner = "".join('<a href="%s">%s</a>' % (base + h, t) for t, h in drop)
            cur = ' class="nav-item has-drop open-none"'
            items.append('<div class="nav-item has-drop"><button type="button" aria-expanded="false" '
                         'aria-haspopup="true">%s%s</button><div class="drop">%s</div></div>'
                         % (label, CHEV, inner))
        else:
            aria = ' aria-current="page"' if href == active else ""
            items.append('<div class="nav-item"><a href="%s"%s>%s</a></div>' % (base + href, aria, label))

    mob = []
    for label, href, drop in NAV:
        if drop:
            mob.append('<div class="grp"><p class="label">%s</p>%s</div>'
                       % (label, "".join('<a href="%s">%s</a>' % (base + h, t) for t, h in drop)))
        else:
            mob.append('<div class="grp"><a href="%s">%s</a></div>' % (base + href, label))

    social = ('<div class="nav-social">'
              '<a href="%s" target="_blank" rel="noopener" aria-label="Instagram">%s</a>'
              '<a href="%s" target="_blank" rel="noopener" aria-label="Facebook">%s</a>'
              '<a href="%s" target="_blank" rel="noopener" aria-label="YouTube">%s</a></div>'
              % (SITE["instagram"], IC_IG, SITE["facebook"], IC_FB, SITE["youtube"], IC_YT))

    return (
        '<nav class="nav" aria-label="Main navigation"><div class="nav-in"><div class="container nav-row">'
        + brand(base) +
        '<div class="nav-links label">' + "".join(items) + '</div>'
        '<div class="nav-right">' + social +
        '<a class="lang" href="%sar.html" hreflang="ar">AR</a>' % base +
        '<a class="btn btn-primary" href="%sclasses.html#trial">Book a trial</a>' % base +
        '<button class="burger" id="burger" aria-label="Open menu" aria-expanded="false" '
        'aria-controls="mobile"><span></span></button>'
        '</div></div>'
        '<div class="mobile" id="mobile"><div class="container">' + "".join(mob) +
        '<div class="foot">' + social +
        '<a class="lang" href="%sar.html">AR</a></div>' % base +
        '</div></div></div></nav>')


def footer(base):
    cols = ""
    for title, links in FOOTER_NAV:
        lis = "".join('<li><a href="%s">%s</a></li>' % (link(base, h), t) for t, h in links)
        cols += '<div><h4>%s</h4><ul>%s</ul></div>' % (title, lis)

    contact = ('<div><h4>Contact</h4><ul>'
               '<li><a href="%s" target="_blank" rel="noopener">%s<br>%s</a></li>'
               '<li><a href="mailto:%s">%s</a></li>'
               '<li><a href="tel:%s">%s</a></li>'
               '<li>%s</li></ul></div>'
               % (SITE["maps"], SITE["address_1"], SITE["address_2"],
                  SITE["email"], SITE["email"], SITE["phone_raw"], SITE["phone"], SITE["hours_short"]))

    fsocial = ('<div class="fsocial">'
               '<a href="%s" target="_blank" rel="noopener" aria-label="Instagram">%s</a>'
               '<a href="%s" target="_blank" rel="noopener" aria-label="Facebook">%s</a>'
               '<a href="%s" target="_blank" rel="noopener" aria-label="YouTube">%s</a></div>'
               % (SITE["instagram"], IC_IG, SITE["facebook"], IC_FB, SITE["youtube"], IC_YT))

    return ('<footer><div class="container"><div class="cols">'
            '<div>' + brand(base, "--deep") +
            '<p class="about">' + FOOTER_ABOUT + '</p>' + fsocial + '</div>'
            + cols + contact +
            '</div><div class="legal">'
            '<span>&copy; 2026 %s &middot; Ministry of Education licence %s</span>'
            '<span><a href="%sterms.html">Terms</a> &middot; Design proposal, not the live school site</span>'
            '</div></div></footer>' % (SITE["full"], SITE["licence"], base))


# ---------------------------------------------------------------- page shell
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
         'family=Oswald:wght@400;500;600;700&family=Montserrat:wght@400;500;600'
         '&family=Reem+Kufi:wght@400;600&display=swap">')

FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 48 48'%3E"
           "%3Ccircle cx='24' cy='24' r='22' fill='%235F4F9B'/%3E%3Cg fill='none' stroke='%23E7E2F1'"
           " stroke-width='3' stroke-linecap='round'%3E%3Cpath d='M9 19c5-4 11-4 16 0s11 4 16 0'/%3E"
           "%3Cpath d='M9 27c5-4 11-4 16 0s11 4 16 0'/%3E%3Cpath d='M13 35c4-2.6 8-2.6 12 0'/%3E"
           "%3C/g%3E%3C/svg%3E")


def page(title, desc, body, base="", active="", extra_js="", data_js=""):
    """Assemble one complete HTML document."""
    full_title = title if title.startswith(SITE["name"]) else "%s &mdash; %s" % (title, SITE["full"])
    return (
        "<!doctype html>\n<html lang=\"en\">\n<head>\n"
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        '<meta name="robots" content="noindex, nofollow">\n'
        '<title>' + full_title + '</title>\n'
        '<meta name="description" content="' + desc + '">\n'
        '<meta name="theme-color" content="#140E1E">\n'
        '<link rel="icon" href="' + FAVICON + '">\n'
        + FONTS + '\n'
        '<link rel="stylesheet" href="' + base + 'assets/site.css">\n'
        "</head>\n<body>\n"
        + promo()
        + nav(base, active)
        + body
        + footer(base)
        + (('<script>' + data_js + '</script>') if data_js else "")
        + '<script src="' + base + 'assets/site.js"></script>'
        + (('<script src="' + base + 'assets/' + extra_js + '"></script>') if extra_js else "")
        + "\n</body>\n</html>\n")


# ---------------------------------------------------------------- fragments
def crumbs(base, trail):
    parts = []
    for i, (label, href) in enumerate(trail):
        if href:
            parts.append('<a href="%s">%s</a>' % (base + href, label))
        else:
            parts.append('<span style="opacity:1;color:var(--ink)">%s</span>' % label)
        if i < len(trail) - 1:
            parts.append('<span>/</span>')
    return '<div class="container"><nav class="crumbs" aria-label="Breadcrumb">%s</nav></div>' % "".join(parts)


def phero(base, label, h1, intro, img, buttons=""):
    return ('<header class="phero"><div class="ph" style="background-image:url(%sassets/img/%s.jpg)"></div>'
            '<div class="container"><p class="label">%s</p><h1>%s</h1><p>%s</p>%s</div></header>'
            % (base, img, label, h1, intro, ('<div class="btnrow">%s</div>' % buttons) if buttons else ""))


def phead(label, h1, intro, extra=""):
    return ('<header class="phead"><div class="container"><p class="label">%s</p><h1>%s</h1>'
            '<p>%s</p>%s</div></header>' % (label, h1, intro, extra))


def section(inner, cls="section", sid=""):
    return '<section class="%s"%s><div class="container">%s</div></section>' % (
        cls, (' id="%s"' % sid) if sid else "", inner)


def head_block(label, h2, p="", cls="section-head rv"):
    return '<div class="%s"><p class="label">%s</p><h2>%s</h2>%s</div>' % (
        cls, label, h2, ('<p>%s</p>' % p) if p else "")


def btn(base, href, text, kind="btn-primary", arrow=True, small=False):
    return ('<a class="btn %s%s" href="%s">%s%s</a>'
            % (kind, " btn-sm" if small else "", link(base, href), text, ARROW if arrow else ""))


def faq_items(items, start=1):
    out = ""
    for i, (q, a) in enumerate(items, start):
        out += ('<details class="q"%s><summary><span class="num">%02d</span><span>%s</span>'
                '<span class="plus" aria-hidden="true">+</span></summary><div class="a">%s</div></details>'
                % (" open" if i == start else "", i, q, a))
    return out


def share_block():
    nets = [("x", "X"), ("facebook", "Facebook"), ("linkedin", "LinkedIn"), ("whatsapp", "WhatsApp")]
    ico = {
        "x": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.5 3h3l-6.6 7.6L21.8 21h-6l-4.7-6.1L5.6 21H2.5l7.1-8.1L2.2 3h6.2l4.3 5.6zm-1.1 16h1.7L7.7 4.8H5.9z"/></svg>',
        "facebook": IC_FB,
        "linkedin": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M4.98 3.5A2.5 2.5 0 1 1 5 8.5a2.5 2.5 0 0 1 0-5M3 9.5h4V21H3zm7 0h3.8v1.6h.05c.53-.95 1.83-1.95 3.77-1.95 4.03 0 4.78 2.5 4.78 5.76V21h-4v-5.2c0-1.24-.02-2.84-1.9-2.84-1.9 0-2.2 1.36-2.2 2.75V21h-4z"/></svg>',
        "whatsapp": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.6 15L2 22l5.2-1.35A10 10 0 1 0 12 2m0 18.2a8.2 8.2 0 0 1-4.2-1.15l-.3-.18-3.1.8.83-3-.2-.31A8.2 8.2 0 1 1 12 20.2m4.5-6.1c-.25-.13-1.46-.72-1.69-.8s-.39-.13-.55.12-.63.8-.78.96-.29.19-.54.06a6.7 6.7 0 0 1-3.35-2.93c-.25-.43.25-.4.72-1.33a.45.45 0 0 0 0-.43c-.06-.12-.55-1.33-.76-1.82s-.4-.42-.55-.43h-.47a.9.9 0 0 0-.65.3 2.75 2.75 0 0 0-.86 2.05 4.8 4.8 0 0 0 1 2.53 10.9 10.9 0 0 0 4.2 3.7c1.56.68 2.17.73 2.95.62a2.5 2.5 0 0 0 1.65-1.17 2.05 2.05 0 0 0 .14-1.16c-.06-.11-.22-.17-.47-.29"/></svg>',
    }
    links = "".join('<a data-net="%s" href="#" target="_blank" rel="noopener" aria-label="Share on %s">%s</a>'
                    % (n, t, ico[n]) for n, t in nets)
    return ('<div class="share" data-share><span class="label">Share</span>' + links +
            '<button type="button" data-copy aria-label="Copy link">'
            '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">'
            '<rect x="9" y="9" width="12" height="12" rx="2.5"/>'
            '<path d="M5.5 15H4.5A1.5 1.5 0 0 1 3 13.5v-9A1.5 1.5 0 0 1 4.5 3h9A1.5 1.5 0 0 1 15 4.5v1"/>'
            '</svg></button><span class="copied"></span></div>')
