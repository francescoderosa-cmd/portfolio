# -*- coding: utf-8 -*-
"""Page bodies, part 3: Hire Us, Merchandising, Summer Camp."""

from data import (SITE, GENRES, HIRE_SERVICES, HIRE_FAQ, MERCH, MERCH_NOTE,
                  MERCH_SIZES_ADULT, MERCH_SIZES_KIDS, CAMP, CAMP_FAQ)
from shell import page, section, head_block, phero, phead, btn, faq_items, ARROW
from pages import img

# ---------------------------------------------------------------- garment icons
# Line art stands in for product photography. Swap for real shots when they exist.
_ICONS = {
    "top": ('<path d="M22 18 34 12h20l12 6-6 12-6-3v33H34V27l-6 3z"/>'),
    "hood": ('<path d="M22 20 34 13h20l12 7-6 13-5-2.5V60H33V30.5L28 33z"/>'
             '<path d="M34 13c0 6 4.5 10 10 10s10-4 10-10"/>'),
    "bottoms": ('<path d="M28 12h32v10l-3 40H45l-1-26-1 26H31l-3-40z"/>'
                '<path d="M28 22h32"/>'),
    "bag": ('<path d="M16 26h56v34a4 4 0 0 1-4 4H20a4 4 0 0 1-4-4z"/>'
            '<path d="M32 26v-6a12 12 0 0 1 24 0v6"/><path d="M16 40h56"/>'),
    "bottle": ('<path d="M38 10h12v8l4 6v42a4 4 0 0 1-4 4H38a4 4 0 0 1-4-4V24l4-6z"/>'
               '<path d="M34 34h20"/>'),
    "socks": ('<path d="M30 12h16v26l12 12a10 10 0 0 1-14 14L28 48a10 10 0 0 1-2-6z"/>'
              '<path d="M30 24h16"/>'),
}
_ICON_FOR = {
    "hoodie": "hood", "jacket": "hood",
    "tshirt": "top", "leotard": "top",
    "joggers": "bottoms", "leggings": "bottoms",
    "bag": "bag", "tote": "bag",
    "bottle": "bottle", "socks": "socks",
}


def garment(icon):
    d = _ICONS[_ICON_FOR.get(icon, "top")]
    return ('<svg viewBox="0 0 88 76" fill="none" stroke="currentColor" stroke-width="2.4" '
            'stroke-linejoin="round" stroke-linecap="round" aria-hidden="true">%s</svg>' % d)


# ---------------------------------------------------------------- Hire Us
def hire_us_page(base=""):
    blocks = ""
    for i, s in enumerate(HIRE_SERVICES):
        points = "".join("<li>%s</li>" % p for p in s["points"])
        blocks += (
            '<article class="svc rv%s" id="%s">'
            '<div class="svc-ph" style="background-image:url(%s)" role="img" aria-label="%s"></div>'
            '<div class="svc-body"><p class="label">%s</p><h3>%s</h3><p class="svc-lead">%s</p>'
            '<ul class="ticks">%s</ul>'
            '<div class="svc-cta">%s<span class="muted" style="font-size:13px">'
            'The school comes back to you with dates and a quote.</span></div>'
            '</div></article>'
            % (" flip" if i % 2 else "", s["slug"], img(base, s["img"]), s["name"],
               s["tagline"], s["name"], s["blurb"], points,
               btn(base, "#request", s["cta"])))

    fields = [("q-name", "Your name", "text"), ("q-mail", "Email", "email"),
              ("q-phone", "Phone", "tel"), ("q-date", "Date you have in mind", "date")]
    inputs = "".join('<div><label class="label" for="%s">%s</label>'
                     '<input class="inp" id="%s" name="%s" type="%s"%s></div>'
                     % (i, l, i, l.lower().replace(" ", "_"), t,
                        " required" if i in ("q-name", "q-mail") else "")
                     for i, l, t in fields)

    body = (phero(base, "Hire Us", "What Al Sarab can do for you",
                  "Four things the school offers outside its own timetable. Nothing is bought "
                  "online: tell us what you need and we come back with dates and a quote, "
                  "usually within 1 to 2 working days.", "perf-wedding",
                  btn(base, "#request", "Request info", "btn-light", arrow=False))

            + section('<div class="jump rv">%s</div>'
                      % "".join('<a href="#%s">%s</a>' % (s["slug"], s["name"]) for s in HIRE_SERVICES),
                      cls="section tight")

            + '<section class="section tight"><div class="container"><div class="svc-list">%s</div></div></section>' % blocks

            + section(head_block("Request info", "Tell us what you need",
                                 "One form for all four services. Pick what it is about, add "
                                 "whatever detail you have, and we will come back with a quote "
                                 "and available dates.")
                      + '<div class="split"><form class="box rv" id="request-form" '
                        'data-mailto="%s" data-subject="Hire Us enquiry">'
                        '<div><label class="label" for="q-service">What is it about?</label>'
                        '<select class="inp" id="q-service" name="service">%s'
                        '<option>Something else</option></select></div>'
                        '%s'
                        '<div><label class="label" for="q-notes">Tell us more</label>'
                        '<textarea class="inp" id="q-notes" name="notes" placeholder="Where it is, '
                        'how many people, how long you need us, anything already decided&hellip;" '
                        'required></textarea></div>'
                        '<button class="btn btn-primary" type="submit">Send request%s</button>'
                        '<p class="form-note">This opens your mail app with everything filled in, '
                        'ready to send to %s. We are not able to take payment online &mdash; every '
                        'booking is quoted and confirmed by the school.</p></form>'
                        '<div class="rv"><h3 style="font-size:26px;margin-bottom:18px">Good to know</h3>'
                        '<div class="faq">%s</div></div></div>'
                        % (SITE["email"],
                           "".join('<option>%s</option>' % s["name"] for s in HIRE_SERVICES),
                           inputs, ARROW, SITE["email"], faq_items(HIRE_FAQ)),
                      sid="request")

            + section('<div class="offer rv"><div><h3>Looking for classes instead?</h3>'
                      '<p>The school teaches six genres in Jbeil and Koura, from three years old '
                      'to adult.</p></div>%s</div>'
                      % btn(base, "classes.html", "See the classes", "btn-ghost"), cls="section tight"))

    return page("Hire Us", "Hire Al Sarab for weddings, videos, choreography commissions and "
                "studio bookings in Lebanon.", body, base=base, active="hire-us.html")


# ---------------------------------------------------------------- Merchandising
def merch_page(base=""):
    cats = []
    for m in MERCH:
        if m["cat"] not in cats:
            cats.append(m["cat"])
    chips = "".join('<button class="chip" type="button" aria-pressed="false" data-value="%s">%s</button>'
                    % (c, c) for c in cats)

    cards = ""
    for m in MERCH:
        colours = "".join('<span class="tag">%s</span>' % c for c in m["colours"])
        cards += ('<article class="merch-card rv" data-tags="%s">'
                  '<div class="thumb">%s<span class="ph-note">Photo to come</span></div>'
                  '<div class="body"><p class="tagline">%s</p><h3>%s</h3><p>%s</p>'
                  '<div class="meta">%s</div>'
                  '<div class="foot"><span class="price">Available at reception</span>'
                  '<button class="btn btn-primary btn-sm" type="button" data-reserve="%s">'
                  'Reserve</button></div></div></article>'
                  % (m["cat"], garment(m["icon"]), m["cat"], m["name"], m["blurb"], colours, m["name"]))

    sizes = (['<option>One size</option>']
             + ['<option>Adult %s</option>' % s for s in MERCH_SIZES_ADULT]
             + ['<option>Kids %s</option>' % s for s in MERCH_SIZES_KIDS]
             + ['<option>By level (ballet)</option>'])

    fields = [("m-name", "Your name", "text"), ("m-mail", "Email", "email"),
              ("m-phone", "Phone", "tel")]
    inputs = "".join('<div><label class="label" for="%s">%s</label>'
                     '<input class="inp" id="%s" name="%s" type="%s"%s></div>'
                     % (i, l, i, l.lower().replace(" ", "_"), t,
                        " required" if i != "m-phone" else "")
                     for i, l, t in fields)

    body = (phead("Merchandising", "Al Sarab, off the studio floor",
                  "Hoodies, T-shirts, joggers and the pieces the levels wear. " + MERCH_NOTE)

            + section('<div class="offer rv" style="margin-bottom:34px"><div>'
                      '<h3>How reserving works</h3>'
                      '<p>Pick an item, choose a size, send the reservation. Reception puts your '
                      'name on it and holds it for you to try, pay for and collect at the school. '
                      'Nothing is charged here.</p></div>'
                      '<span class="tag todo">No online payment</span></div>'
                      '<div class="chips rv" data-filter-group="#merch-grid" style="margin-bottom:30px">'
                      '<button class="chip" type="button" aria-pressed="false" data-value="">All items</button>'
                      '%s</div>'
                      '<div class="cards g3" id="merch-grid">%s</div>'
                      '<p class="empty" data-filter-empty hidden>No item in that category.</p>'
                      % (chips, cards), cls="section tight")

            + section(head_block("Reserve", "Put your name on something",
                                 "Reserving is free and commits you to nothing. We hold the item "
                                 "at reception and tell you when it is ready to try on.")
                      + '<div class="split"><form class="box rv" id="reserve-form" '
                        'data-mailto="%s" data-subject="Merchandising reservation">'
                        '<div><label class="label" for="m-item">Item</label>'
                        '<select class="inp" id="m-item" name="item">%s</select></div>'
                        '<div class="two">'
                        '<div><label class="label" for="m-size">Size</label>'
                        '<select class="inp" id="m-size" name="size">%s</select></div>'
                        '<div><label class="label" for="m-qty">Quantity</label>'
                        '<select class="inp" id="m-qty" name="quantity">%s</select></div></div>'
                        '%s'
                        '<div><label class="label" for="m-notes">Anything else?</label>'
                        '<textarea class="inp" id="m-notes" name="notes" placeholder="Colour you '
                        'want, the student\'s name and level, when you can come in&hellip;"></textarea></div>'
                        '<button class="btn btn-primary" type="submit">Send reservation%s</button>'
                        '<p class="form-note">Opens your mail app, ready to send to %s. You pay at '
                        'the school when you collect.</p></form>'
                        '<div class="rv"><h3 style="font-size:26px;margin-bottom:18px">Good to know</h3>'
                        '<div class="faq">%s</div></div></div>'
                        % (SITE["email"],
                           "".join('<option>%s</option>' % m["name"] for m in MERCH),
                           "".join(sizes),
                           "".join('<option>%d</option>' % n for n in range(1, 6)),
                           inputs, ARROW, SITE["email"],
                           faq_items([
                               ("How long is it held for me?",
                                "Placeholder &mdash; confirm how long reception holds a reservation."),
                               ("Can I try before paying?",
                                "Yes. That is the point of reserving: the item is there in your "
                                "size when you come in."),
                               ("What if the size is wrong?",
                                "Reserve the size you think fits and try it at the school. Nothing "
                                "is paid until it does."),
                               ("Do you post items?",
                                "Placeholder &mdash; confirm whether delivery is possible."),
                           ])),
                      sid="reserve"))

    return page("Merchandising", "Al Sarab branded clothing and accessories. Reserve online, try "
                "and pay at the school.", body, base=base, active="merchandising.html",
                extra_js="merch.js")


# ---------------------------------------------------------------- Summer Camp
def camp_page(base=""):
    acts = "".join('<div class="pillar rv"><h3>%s</h3><p>%s</p></div>' % (t, d)
                   for t, d in CAMP["activities"])

    last = CAMP["last"]
    stats = "".join('<div class="row-item"><b>%s</b><span>%s</span></div>' % (k, v)
                    for k, v in last["stats"])
    gallery = "".join('<div class="shot" style="background-image:url(%s)" role="img" '
                      'aria-label="Al Sarab dancers"></div>' % img(base, g)
                      for g in last["gallery"])

    fields = [("c-name", "Parent or student name", "text"), ("c-mail", "Email", "email"),
              ("c-phone", "Phone", "tel"), ("c-age", "Age of the camper", "text")]
    inputs = "".join('<div><label class="label" for="%s">%s</label>'
                     '<input class="inp" id="%s" name="%s" type="%s"%s></div>'
                     % (i, l, i, l.lower().replace(" ", "_"), t,
                        " required" if i in ("c-name", "c-mail") else "")
                     for i, l, t in fields)

    body = (phero(base, "Summer Camp", CAMP["label"], CAMP["intro"], "acro",
                  btn(base, "#reserve", "Reserve a place", "btn-light", arrow=False)
                  + btn(base, "#last", "See last summer", "btn-outline-light", arrow=False))

            + section('<div class="split"><div class="rv">'
                      '<p class="label" style="color:var(--brand);margin-bottom:16px">Next camp</p>'
                      '<h2 style="font-size:34px;margin-bottom:20px">Summer %s</h2>'
                      '<p class="muted" style="font-size:17px">%s</p>'
                      '<p class="muted" style="margin-top:18px">%s</p>'
                      '<div style="margin-top:26px">%s</div></div>'
                      '<div class="rv"><div class="facts">'
                      '<div class="r"><span class="k">When</span><span class="v">%s</span></div>'
                      '<div class="r"><span class="k">Length</span><span class="v">%s</span></div>'
                      '<div class="r"><span class="k">Hours</span><span class="v">%s</span></div>'
                      '<div class="r"><span class="k">Ages</span><span class="v">%s</span></div>'
                      '<div class="r"><span class="k">Where</span><span class="v">%s</span></div>'
                      '</div></div></div>'
                      % (CAMP["year"], CAMP["intro"], CAMP["reserve_note"],
                         btn(base, "#reserve", "Reserve a place"),
                         CAMP["dates"], CAMP["length"], CAMP["daily"], CAMP["ages"], CAMP["place"]))

            + section(head_block("The programme", "What happens at camp",
                                 "Mornings are technique, afternoons are making things, and the "
                                 "last day is a showing for families.")
                      + '<div class="pillars">%s</div>' % acts)

            + section(head_block("Reserve", "Hold a place for Summer %s" % CAMP["year"],
                                 "Reserving is free and commits you to nothing. We contact you "
                                 "with dates, fees and the full programme as soon as they are set.")
                      + '<div class="split"><form class="box rv" data-mailto="%s" '
                        'data-subject="Summer Camp %s reservation">%s'
                        '<div><label class="label" for="c-length">One week or two?</label>'
                        '<select class="inp" id="c-length" name="length">'
                        '<option>Two weeks</option><option>One week</option>'
                        '<option>Not sure yet</option></select></div>'
                        '<div><label class="label" for="c-exp">Do they already dance?</label>'
                        '<select class="inp" id="c-exp" name="experience">'
                        '<option>Trains at Al Sarab</option><option>Dances elsewhere</option>'
                        '<option>Complete beginner</option></select></div>'
                        '<div><label class="label" for="c-notes">Anything we should know?</label>'
                        '<textarea class="inp" id="c-notes" name="notes" placeholder="Allergies, '
                        'siblings coming too, questions about the programme&hellip;"></textarea></div>'
                        '<button class="btn btn-primary" type="submit">Reserve a place%s</button>'
                        '<p class="form-note">Opens your mail app, ready to send to %s. No payment '
                        'is taken online and reserving costs nothing.</p></form>'
                        '<div class="rv"><h3 style="font-size:26px;margin-bottom:18px">Good to know</h3>'
                        '<div class="faq">%s</div></div></div>'
                        % (SITE["email"], CAMP["year"], inputs, ARROW, SITE["email"],
                           faq_items(CAMP_FAQ)),
                      sid="reserve")

            + section(head_block("Last summer", last["label"], last["summary"])
                      + '<div class="split" style="margin-bottom:34px">'
                        '<div class="rv"><div class="rows">%s</div></div>'
                        '<div class="rv"><p class="muted">Photographs from the 2026 camp would sit '
                        'in this gallery. The images below are from the school\'s own archive and '
                        'stand in for them.</p></div></div>'
                        '<div class="gallery rv">%s</div>' % (stats, gallery),
                      sid="last")

            + section('<div class="offer rv"><div><h3>Not sure yet?</h3>'
                      '<p>Come to a class during the year first &mdash; a trial is free.</p></div>%s</div>'
                      % btn(base, "classes.html#trial", "Book a trial class", "btn-ghost"),
                      cls="section tight"))

    return page("Summer Camp", "Al Sarab Summer Camp %s in Byblos, Lebanon. Reserve a place for "
                "next summer." % CAMP["year"], body, base=base, active="summer-camp.html")
