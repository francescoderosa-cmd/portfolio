# -*- coding: utf-8 -*-
"""Page bodies, part 2: events, news, about, FAQ, contact, portal, terms, Arabic."""

from data import (SITE, STUDIOS, STUDIO, GENRES, TEACHERS, EVENTS, NEWS, FAQ, BRANCHES,
                  PACKAGES, LEVELS)
from shell import (page, section, head_block, phero, phead, crumbs, btn, faq_items,
                   share_block, app_cta, ARROW)
from pages import img, event_card, news_card, person_card, contact_block, contact_form, social_pills


# ---------------------------------------------------------------- events
def events_index(base=""):
    up = [e for e in EVENTS if e["when"] == "upcoming"]
    past = [e for e in EVENTS if e["when"] == "past"]
    body = (phead("Events", "Workshops &middot; Showcases &middot; Recitals",
                  "We run guest workshops through the year, a winter platform for work in progress, "
                  "and an end-of-year recital where every level performs.")
            + section('<div class="tabs rv" data-tabs="ev" role="tablist">'
                      '<button class="tab" role="tab" data-panel="up" aria-selected="true">Upcoming</button>'
                      '<button class="tab" role="tab" data-panel="past" aria-selected="false">Past events</button>'
                      '</div>'
                      '<div data-panel-for="ev" data-panel="up"><div class="cards g3">%s</div></div>'
                      '<div data-panel-for="ev" data-panel="past" hidden><div class="cards g3">%s</div></div>'
                      % ("".join(event_card(base, e) for e in up),
                         "".join(event_card(base, e) for e in past)), cls="section tight")
            + section('<div class="offer rv"><div><h3>Never miss an event</h3>'
                      '<p>Follow the school on Instagram, or write to us and we will add you to the '
                      'family mailing list.</p></div>%s</div>'
                      % btn(base, SITE["instagram"], "Follow on Instagram", "btn-primary", arrow=False),
                      cls="section tight"))
    return page("Events", "Workshops, showcases and recitals at Al Sarab in Byblos, Lebanon.",
                body, base=base, active="events.html")


def event_detail(e, base="../"):
    howto = "".join("<li>%s</li>" % h for h in e["howto"])
    others = [x for x in EVENTS if x["slug"] != e["slug"] and x["when"] == "upcoming"][:3]
    tags = '<span class="tag hot">%s</span>' % e["cat"]
    if e["free"]:
        tags += '<span class="tag free">Free</span>'

    body = (phero(base, e["cat"], e["title"], e["teaser"], e["img"],
                  btn(base, "contact.html", "Ask about this event", "btn-light"))
            + crumbs(base, [("Home", "index.html"), ("Events", "events.html"), (e["title"], None)])
            + section('<div class="split"><div class="rv">'
                      '<div class="chips" style="margin-bottom:22px">%s</div>'
                      '%s%s</div>'
                      '<div class="rv"><div class="facts">'
                      '<div class="r"><span class="k">Date</span><span class="v">%s</span></div>'
                      '<div class="r"><span class="k">Time</span><span class="v">%s</span></div>'
                      '<div class="r"><span class="k">Where</span><span class="v">%s</span></div>'
                      '<div class="r"><span class="k">Admission</span><span class="v">%s</span></div></div>'
                      '<div style="margin-top:22px;display:flex;flex-direction:column;gap:12px">%s%s</div>'
                      '</div></div>'
                      % (tags,
                         "".join('<p style="margin-bottom:20px;color:var(--ink-2);font-size:17px">%s</p>' % p
                                 for p in e["body"]),
                         ('<h2 style="font-size:26px;margin:34px 0 14px">How to take part</h2>'
                          '<ul class="ticks">%s</ul>' % howto) if howto else "",
                         e["date"], e["time"], e["place"], "Free" if e["free"] else "See below",
                         btn(base, "contact.html", "Contact the school"),
                         btn(base, SITE["maps"], "Open in Google Maps", "btn-ghost", arrow=False)))
            + section(share_block(), cls="section tight")
            + (section(head_block("More", "Upcoming events")
                       + '<div class="cards g3">%s</div>' % "".join(event_card(base, x) for x in others),
                       cls="section tight") if others else ""))

    return page(e["title"], e["teaser"], body, base=base, active="events.html")


# ---------------------------------------------------------------- news
def news_index(base=""):
    body = (phead("News &amp; stories", "From the studio",
                  "Guides, teacher interviews, student stories and news from Al Sarab.")
            + section('<div class="cards g3">%s</div>' % "".join(news_card(base, n) for n in NEWS),
                      cls="section tight"))
    return page("News &amp; stories", "News, guides and stories from Al Sarab in Byblos, Lebanon.",
                body, base=base, active="news.html")


def news_detail(n, base="../"):
    parts = ""
    for kind, val in n["body"]:
        if kind == "h":
            parts += "<h2>%s</h2>" % val
        elif kind == "p":
            parts += "<p>%s</p>" % val
        elif kind == "ul":
            parts += "<ul>%s</ul>" % "".join("<li>%s</li>" % x for x in val)

    others = [x for x in NEWS if x["slug"] != n["slug"]][:3]

    body = ('<header class="phero" style="min-height:44vh"><div class="ph" '
            'style="background-image:url(%s)"></div><div class="container">'
            '<p class="label">%s</p><h1>%s</h1></div></header>'
            % (img(base, n["img"]), n["cat"], n["title"])
            + crumbs(base, [("Home", "index.html"), ("News", "news.html"), (n["cat"], None)])
            + '<section class="section tight"><div class="container"><div class="article rv">'
              '<div class="meta"><span class="tag hot">%s</span><span>%s</span><span>&middot;</span>'
              '<span>%s</span></div>'
              '<div class="body">%s</div>'
              '<div class="ctabox"><div><h3>Ready to try it?</h3>'
              '<p>A free trial class, then placement advice.</p></div>%s</div>'
              '%s</div></div></section>'
              % (n["cat"], n["date"], n["read"], parts,
                 btn(base, "contact.html", "Book a trial class"), share_block())
            + section(head_block("Keep reading", "Related stories")
                      + '<div class="cards g3">%s</div>' % "".join(news_card(base, x) for x in others),
                      cls="section tight"))

    return page(n["title"], n["teaser"], body, base=base, active="news.html")


# ---------------------------------------------------------------- about
def about_page(base=""):
    team = "".join(person_card(base, t) for t in TEACHERS[:8])
    body = (phero(base, "About", "Dance is for every body",
                  "Al Sarab Alternative Dance School has taught in Lebanon since January 1991. "
                  "One curriculum, six genres, five branches, and one sentence that has not changed "
                  "in thirty-five years.", "about")
            + section(head_block("What we stand for", "Three things that do not move")
                      + '<div class="pillars">'
                        '<div class="pillar rv"><h3>Any and every body</h3><p>The mission has been the '
                        'same sentence since 1991: open opportunities in the society for any and every '
                        'body to dance. Every decision about levels, fees and placement is measured '
                        'against it.</p></div>'
                        '<div class="pillar rv"><h3>Written, not assumed</h3><p>Being curriculum-based '
                        'means written level objectives, an assessment officer and an end-of-year '
                        'evaluation for every student. Progress is recorded, not guessed at.</p></div>'
                        '<div class="pillar rv"><h3>Taught by dancers who teach</h3><p>Our team are '
                        'performers, but they are hired to teach. Pedagogy is the qualification that '
                        'matters here.</p></div></div>')
            + section(head_block("Our home", "Center Al Haref, Byblos")
                      + '<div class="split"><div class="rv">'
                        '<p>The school\'s home is in Jbeil, a few minutes from the old port of Byblos. '
                        'Two studios sit in Center Al Haref: a large teaching room with a full mirror '
                        'wall and portable barres, and a smaller room for junior groups, acro and '
                        'rehearsal.</p>'
                        '<p>Branches have carried the programme north to Koura and Bishmizzine and '
                        'south towards Beirut, at La Collina and Rabieh &mdash; the same curriculum, '
                        'the same assessment, taught closer to home.</p>'
                        '<div style="margin-top:24px;display:flex;gap:12px;flex-wrap:wrap">%s%s</div></div>'
                        '<div class="rv"><div class="rows">%s</div></div></div>'
                        % (btn(base, "hire-us.html#studio-booking", "See the studios", "btn-ghost"),
                           btn(base, SITE["maps"], "Open in Google Maps", "btn-ghost", arrow=False),
                           "".join('<div class="row-item"><b>%s</b><span>%s</span></div>' % (n, d)
                                   for n, d in BRANCHES)))
            + section(head_block("The story", "From one genre to a curriculum")
                      + '<div class="split"><div class="rv">'
                        '<p>Dr. Nadra Majeed Assaf founded Al Sarab Alternative Dance School and Al '
                        'Sarab Dance Company in January 1991. The school taught Modern Dance, and for '
                        'its first years that was the whole offer.</p>'
                        '<p>Over the past fifteen years the programme widened into six movement '
                        'disciplines &mdash; Modern, Contemporary, Classical Ballet, Jazz, Raqs Sharqi '
                        'and Acro &mdash; held together by a single written curriculum rather than run '
                        'as six separate schools sharing a building.</p>'
                        '<div class="pull">For over 30 years, Al Sarab has been a place committed to '
                        'the embodied pedagogy of the dancers of Lebanon.<cite>Al Sarab Alternative '
                        'Dance School</cite></div>'
                        '<p>Today the school is registered with the Ministry of Education (Lebanon) '
                        'under licence 213/2009 and is a member of the National Dance Education '
                        'Organization (USA) &mdash; one of very few schools in the country to hold '
                        'both. Its sister ensemble, Al Sarab Dance Company, tours separately.</p>'
                        '<div class="stamp"><span>Founded January 1991</span>'
                        '<span>Ministry licence 213/2009</span><span>NDEO member (USA)</span>'
                        '<span>Six genres</span><span>Five branches</span></div></div>'
                        '<div class="rv"><div style="border-radius:var(--radius);overflow:hidden;'
                        'aspect-ratio:4/5;background:var(--deep) url(%s) center/cover" role="img" '
                        'aria-label="Al Sarab dancers on stage"></div></div></div>' % img(base, "contemporary"))
            + section(head_block("The team", "Who teaches here")
                      + '<div class="cards g4">%s</div>' % team
                      + '<div style="margin-top:32px">%s</div>'
                      % btn(base, "instructors.html", "Meet all teachers", "btn-ghost"), cls="section tight"))
    return page("About", "Al Sarab Alternative Dance School has taught dance in Lebanon since 1991.",
                body, base=base, active="about.html")


# ---------------------------------------------------------------- studios
def studios_index(base=""):
    cards = ""
    for k in STUDIOS:
        s = STUDIO[k]
        cards += ('<article class="card rv"><div class="ph" style="background-image:url(%s)"></div>'
                  '<div class="body"><div class="meta"><span class="tag">%s</span>'
                  '<span class="tag todo">Specs placeholder</span></div>'
                  '<h3>%s &middot; %s</h3><p>%s</p>'
                  '<div class="foot"><span>%s &mdash; %s</span>'
                  '<a class="linkarrow" href="%sstudios/%s.html">Explore studio%s</a></div></div></article>'
                  % (img(base, s["img"]), s["loc"], s["name"], s["loc"], s["blurb"],
                     s["size"], s["cap"], base, s["slug"], ARROW))

    body = (phead("Studios", "Three rooms, one curriculum",
                  "Al Sarab teaches in two studios at Center Al Haref in Byblos and one in Koura. "
                  "All have sprung floors, mirror walls and a sound system.")
            + section('<div class="cards g3">%s</div>' % cards, cls="section tight")
            + section('<div class="offer rv"><div><h3>Rent a studio</h3>'
                      '<p>Book a room for rehearsal, a workshop or a production, when it is not '
                      'timetabled.</p></div>%s</div>'
                      % btn(base, "studio-rental.html", "Studio rental"), cls="section tight"))
    return page("Studios", "The three dance studios of Al Sarab in Byblos and Koura, Lebanon.",
                body, base=base, active="studios.html")


def studio_detail(key, base="../"):
    s = STUDIO[key]
    rows = [c for c in __import__("data").CLASSES if c["studio"] == key]
    from pages import flat_table
    body = (phero(base, "Studio", "%s &middot; %s" % (s["name"], s["loc"]), s["blurb"], s["img"],
                  btn(base, "studio-rental.html", "Enquire about renting", "btn-light"))
            + crumbs(base, [("Home", "index.html"), ("Studios", "studios.html"), (s["name"], None)])
            + section('<div class="split"><div class="rv">'
                      '<h2 style="font-size:32px;margin-bottom:18px">The room</h2>'
                      '<p class="muted" style="font-size:17px">%s</p>'
                      '<p class="muted" style="margin-top:18px">Specifications on this page are '
                      'placeholders for review &mdash; Al Sarab will confirm the real dimensions, '
                      'capacity and equipment.</p></div>'
                      '<div class="rv"><div class="facts">'
                      '<div class="r"><span class="k">Size</span><span class="v">%s</span></div>'
                      '<div class="r"><span class="k">Capacity</span><span class="v">%s</span></div>'
                      '<div class="r"><span class="k">Floor</span><span class="v">%s</span></div>'
                      '<div class="r"><span class="k">Equipment</span><span class="v">%s</span></div>'
                      '<div class="r"><span class="k">Branch</span><span class="v">%s</span></div>'
                      '</div></div></div>'
                      % (s["blurb"], s["size"], s["cap"], s["floor"], s["kit"], s["loc"]))
            + section(head_block("Timetable", "Classes in this studio")
                      + flat_table(base, rows), cls="section tight"))
    return page("%s, %s" % (s["name"], s["loc"]),
                "%s at Al Sarab in %s, Lebanon." % (s["name"], s["loc"]),
                body, base=base, active="studios.html")


# ---------------------------------------------------------------- faq
def faq_page(base=""):
    def anchor(title):
        return "faq-" + title.lower().replace("&amp;", "").replace(" ", "-").replace("--", "-").strip("-")

    jump = "".join('<a href="#%s">%s</a>' % (anchor(t), t) for t, _, _ in FAQ)
    groups = ""
    for title, sub, items in FAQ:
        groups += ('<div class="faq-group rv"><h2 id="%s">%s</h2><p class="muted">%s</p>'
                   '<div class="faq">%s</div></div>' % (anchor(title), title, sub, faq_items(items)))

    body = (phead("FAQ", "Frequently asked questions",
                  "Everything families ask before the first class &mdash; registration, ages, levels, "
                  "fees and finding us.")
            + section('<div class="jump rv">%s</div>%s' % (jump, groups), cls="section tight")
            + section('<div class="offer rv"><div><h3>Still not answered?</h3>'
                      '<p>Call %s on a class day, or send us a message.</p></div>%s</div>'
                      % (SITE["phone"], btn(base, "contact.html", "Contact the school")),
                      cls="section tight"))
    return page("FAQ", "Frequently asked questions about classes, fees and registration at Al Sarab.",
                body, base=base, active="faq.html")


# ---------------------------------------------------------------- contact
def contact_page(base=""):
    body = (phead("Contact", "We would love to hear from you",
                  "Reception answers on class days. For registration, timetables and fees, a phone "
                  "call is usually the fastest way.")
            + section(contact_block(base, "Visit us in Byblos"), cls="section tight")
            + section(head_block("Branches", "Where else we teach")
                      + '<div class="rows rv">%s</div>'
                      % "".join('<div class="row-item"><b>%s</b><span>%s</span></div>' % (n, d)
                                for n, d in BRANCHES), cls="section tight"))
    return page("Contact", "Contact Al Sarab Alternative Dance School in Byblos, Lebanon.",
                body, base=base, active="contact.html")


# ---------------------------------------------------------------- studio rental
def rental_page(base=""):
    cards = ""
    for k in STUDIOS:
        s = STUDIO[k]
        cards += ('<div class="price-card rv"><h3>%s &middot; %s</h3>'
                  '<p class="amount">%s<small>%s &middot; %s</small></p>'
                  '<ul><li>%s</li><li>%s</li><li>Two-hour minimum</li>'
                  '<li>Half-day and full-day rates available</li></ul>%s</div>'
                  % (s["name"], s["loc"], "On request", s["size"], s["cap"], s["floor"], s["kit"],
                     btn(base, "#enquiry", "Enquire", "btn-ghost", arrow=False)))

    fields = [("r-name", "Your name", "text"), ("r-mail", "Email", "email"),
              ("r-date", "Preferred date", "date"), ("r-hours", "Hours needed", "text")]
    inputs = "".join('<div><label class="label" for="%s">%s</label>'
                     '<input class="inp" id="%s" name="%s" type="%s" required></div>'
                     % (i, l, i, l.lower().replace(" ", "_"), t) for i, l, t in fields)

    body = (phero(base, "Studio rental", "Rent a studio in Byblos",
                  "Three professional dance studios with sprung floors, mirror walls and sound "
                  "systems &mdash; available for rehearsal, workshops, auditions and productions "
                  "when they are not timetabled.", "studio-1",
                  btn(base, "#enquiry", "Send an enquiry", "btn-light", arrow=False))
            + section(head_block("The rooms", "What you can book",
                                 "Rates are quoted per booking. Specifications on this page are "
                                 "placeholders for review.")
                      + '<div class="cards g3">%s</div>' % cards, cls="section tight")
            + section(head_block("Enquiry", "Tell us what you need")
                      + '<div class="split"><form class="box rv" data-mailto="%s" '
                        'data-subject="Studio rental enquiry">%s'
                        '<div><label class="label" for="r-studio">Studio</label>'
                        '<select class="inp" id="r-studio" name="studio">%s</select></div>'
                        '<div><label class="label" for="r-use">Purpose of hire</label>'
                        '<select class="inp" id="r-use" name="purpose"><option>Rehearsal</option>'
                        '<option>Workshop</option><option>Audition</option><option>Filming</option>'
                        '<option>Other</option></select></div>'
                        '<div><label class="label" for="r-notes">Anything else?</label>'
                        '<textarea class="inp" id="r-notes" name="notes"></textarea></div>'
                        '<button class="btn btn-primary" type="submit">Send enquiry%s</button>'
                        '<p class="form-note">Opens your mail app. We reply within 1 to 2 working days.</p>'
                        '</form>'
                        '<div class="rv"><h3 style="font-size:26px;margin-bottom:18px">Good to know</h3>'
                        '<div class="faq">%s</div></div></div>'
                        % (SITE["email"], inputs,
                           "".join('<option>%s &middot; %s</option>' % (STUDIO[k]["name"], STUDIO[k]["loc"])
                                   for k in STUDIOS), ARROW,
                           faq_items(FAQ[6][2])), sid="enquiry", cls="section tight"))
    return page("Studio rental", "Rent a dance studio at Al Sarab in Byblos or Koura, Lebanon.",
                body, base=base, active="studio-rental.html")


# ---------------------------------------------------------------- performances for hire
def performances_page(base=""):
    from data import PERFORMANCE_FORMATS, PERF_FAQ

    cards = ""
    for f in PERFORMANCE_FORMATS:
        items = "".join("<li>%s</li>" % i for i in f["items"])
        cards += ('<article class="card rv%s"><div class="ph" style="background-image:url(%s)"></div>'
                  '<div class="body"><div class="meta"><span class="tag hot">%s</span>'
                  '<span class="tag">%s</span><span class="tag">%s</span></div>'
                  '<h3>%s</h3><p>%s</p>'
                  '<ul class="ticks" style="margin-top:4px">%s</ul>'
                  '<div class="foot"><span>Repertoire: %s</span>'
                  '<a class="linkarrow" href="#enquiry">Enquire about this%s</a></div></div></article>'
                  % (" featured" if f["featured"] else "", img(base, f["img"]), f["name"],
                     f["dur"], f["size"], f["name"], f["blurb"], items, f["genres"], ARROW))

    genre_chips = "".join('<a class="chip" style="text-decoration:none" href="%sdance-styles/%s.html">%s</a>'
                          % (base, g["slug"], g["name"]) for g in GENRES)

    fields = [("h-name", "Your name", "text"), ("h-mail", "Email", "email"),
              ("h-date", "Event date", "date"), ("h-place", "Venue or city", "text"),
              ("h-guests", "Guests expected", "text"), ("h-length", "Set length wanted", "text")]
    inputs = "".join('<div><label class="label" for="%s">%s</label>'
                     '<input class="inp" id="%s" name="%s" type="%s"%s></div>'
                     % (i, l, i, l.lower().replace(" ", "_"), t,
                        " required" if i in ("h-name", "h-mail") else "")
                     for i, l, t in fields)

    body = (phero(base, "Hire us", "Al Sarab at your event",
                  "Weddings, private parties, galas and commissioned shows. Al Sarab has been "
                  "putting dancers on stage in Lebanon since 1991 &mdash; including a full "
                  "production at Metro Al Madina in Beirut. The same dancers can perform at "
                  "your event.", "performances",
                  btn(base, "#enquiry", "Send an enquiry", "btn-light", arrow=False)
                  + btn(base, "#formats", "See the formats", "btn-outline-light", arrow=False))

            + section('<div class="split"><div class="rv">'
                      '<p class="label" style="color:var(--brand);margin-bottom:16px">What this is</p>'
                      '<h2 style="font-size:34px;margin-bottom:20px">We come to you and perform</h2>'
                      '<p class="muted" style="font-size:17px">This is the performance side of the '
                      'school: a choreographed set danced by Al Sarab at your wedding, your party or '
                      'your event. It is not a class &mdash; nobody in the room has to dance.</p>'
                      '<p class="muted" style="margin-top:16px">If what you actually want is your own '
                      'group learning a routine together, that is a '
                      '<a href="%sprivate-events.html" style="color:var(--brand)">private session</a> '
                      'instead. If you want the room, not the dancers, see '
                      '<a href="%sstudio-rental.html" style="color:var(--brand)">studio rental</a>.</p>'
                      '</div>'
                      '<div class="rv"><div class="facts">'
                      '<div class="r"><span class="k">Formats</span><span class="v">Wedding, party, gala, full show</span></div>'
                      '<div class="r"><span class="k">Set length</span><span class="v">10&ndash;70 min</span></div>'
                      '<div class="r"><span class="k">Dancers</span><span class="v">3 to 14+</span></div>'
                      '<div class="r"><span class="k">Travel</span><span class="v">Across Lebanon</span></div>'
                      '<div class="r"><span class="k">Ensemble</span>'
                      '<span class="v"><span class="tag todo">To confirm</span></span></div>'
                      '<div class="r"><span class="k">Fee</span><span class="v">Quoted per booking</span></div>'
                      '</div></div></div>' % (base, base), cls="section tight")

            + section(head_block("Formats", "Four ways to book us",
                                 "Every booking is quoted individually &mdash; the format sets the "
                                 "shape, then the length, the number of dancers and the travel set "
                                 "the fee.")
                      + '<div class="cards g2">%s</div>' % cards, sid="formats")

            + section(head_block("Repertoire", "What we can dance",
                                 "Raqs Sharqi is the most-asked-for at weddings, and the one Al Sarab "
                                 "teaches as a full technique rather than a party skill. Any genre "
                                 "in the curriculum can be programmed.")
                      + '<div class="chips rv">%s</div>' % genre_chips, cls="section tight")

            + section(head_block("How it works", "From enquiry to the night")
                      + '<div class="steps">'
                        '<div class="step rv"><span class="n">01</span><h3>Tell us the event</h3>'
                        '<p>Date, venue, how many guests, and roughly how long you want us on.</p></div>'
                        '<div class="step rv"><span class="n">02</span><h3>We propose and quote</h3>'
                        '<p>A format, a repertoire suggestion and a fee, within 1 to 2 working days.</p></div>'
                        '<div class="step rv"><span class="n">03</span><h3>We build it</h3>'
                        '<p>Choreography, music and costume agreed with you, then rehearsed. We check '
                        'the floor plan before the date.</p></div>'
                        '<div class="step rv"><span class="n">04</span><h3>We perform</h3>'
                        '<p>We arrive with everything we need and fit into your run of show.</p></div>'
                        '</div>', cls="section tight")

            + section(head_block("Enquiry", "Tell us about your event")
                      + '<div class="split"><form class="box rv" data-mailto="%s" '
                        'data-subject="Performance booking enquiry">%s'
                        '<div><label class="label" for="h-type">Type of event</label>'
                        '<select class="inp" id="h-type" name="event_type">%s'
                        '<option>Something else</option></select></div>'
                        '<div><label class="label" for="h-genre">Genre you have in mind</label>'
                        '<select class="inp" id="h-genre" name="genre">'
                        '<option>No preference &mdash; advise us</option>%s</select></div>'
                        '<div><label class="label" for="h-notes">Anything else we should know?</label>'
                        '<textarea class="inp" id="h-notes" name="notes" placeholder="Run of show, '
                        'music you want, whether there is a stage&hellip;"></textarea></div>'
                        '<button class="btn btn-primary" type="submit">Send enquiry%s</button>'
                        '<p class="form-note">Opens your mail app with everything filled in, ready to '
                        'send to %s. We reply within 1 to 2 working days.</p></form>'
                        '<div class="rv"><h3 style="font-size:26px;margin-bottom:18px">Good to know</h3>'
                        '<div class="faq">%s</div></div></div>'
                        % (SITE["email"], inputs,
                           "".join('<option>%s</option>' % f["name"] for f in PERFORMANCE_FORMATS),
                           "".join('<option>%s</option>' % g["name"] for g in GENRES),
                           ARROW, SITE["email"], faq_items(PERF_FAQ)),
                      sid="enquiry", cls="section tight")

            + section('<div class="offer rv"><div><h3>Looking for the school instead?</h3>'
                      '<p>Classes run Monday, Wednesday and Friday in Jbeil and Koura, from three '
                      'years old to adult.</p></div>%s</div>'
                      % btn(base, "classes.html", "See the classes", "btn-ghost"), cls="section tight"))

    return page("Performances", "Hire Al Sarab to perform at your wedding, party, gala or private "
                "show in Lebanon.", body, base=base, active="performances.html")


# ---------------------------------------------------------------- private events
def private_page(base=""):
    cards = ""
    for p in PACKAGES:
        items = "".join("<li>%s</li>" % i for i in p["items"])
        cards += ('<div class="price-card rv%s"><h3>%s</h3>'
                  '<p class="amount">%s<small>%s</small></p><ul>%s</ul>%s</div>'
                  % (" featured" if p["featured"] else "", p["name"], p["price"], p["dur"], items,
                     btn(base, "#enquiry", "Enquire", "btn-ghost" if not p["featured"] else "btn-primary",
                         arrow=False)))

    fields = [("p-name", "Your name", "text"), ("p-mail", "Email", "email"),
              ("p-date", "Preferred date", "date"), ("p-size", "Group size", "text")]
    inputs = "".join('<div><label class="label" for="%s">%s</label>'
                     '<input class="inp" id="%s" name="%s" type="%s" required></div>'
                     % (i, l, i, l.lower().replace(" ", "_"), t) for i, l, t in fields)

    body = (phero(base, "Private sessions", "A private class for your group",
                  "A closed session at Center Al Haref, built around your group. Birthdays, "
                  "hen parties, school groups, team days &mdash; 60 to 120 minutes, no experience "
                  "needed. Minimum six people.", "raqs",
                  btn(base, "#enquiry", "Send an enquiry", "btn-light", arrow=False))
            + section(head_block("Formats", "Three ways to run it",
                                 "Rates are quoted per group and given on enquiry. Genres available: "
                                 "Raqs Sharqi, Jazz, Modern or Acro.")
                      + '<div class="cards g3">%s</div>' % cards, cls="section tight")
            + section(head_block("How it works", "From enquiry to the day")
                      + '<div class="steps">'
                        '<div class="step rv"><span class="n">01</span><h3>Tell us the group</h3>'
                        '<p>Size, ages, the date you have in mind and the genre you like the sound of.</p></div>'
                        '<div class="step rv"><span class="n">02</span><h3>We quote</h3>'
                        '<p>A rate for the format, the room and the teacher, within 1 to 2 working days.</p></div>'
                        '<div class="step rv"><span class="n">03</span><h3>We build the session</h3>'
                        '<p>A warm-up, a short choreography and, in the longer formats, freestyle.</p></div>'
                        '<div class="step rv"><span class="n">04</span><h3>You dance</h3>'
                        '<p>Come as you are. We film the choreography in the Extended and Full formats.</p></div>'
                        '</div>', cls="section tight")
            + section(head_block("Enquiry", "Book your session")
                      + '<div class="split"><form class="box rv" data-mailto="%s" '
                        'data-subject="Private session enquiry">%s'
                        '<div><label class="label" for="p-genre">Dance genre</label>'
                        '<select class="inp" id="p-genre" name="genre">%s</select></div>'
                        '<div><label class="label" for="p-pack">Format</label>'
                        '<select class="inp" id="p-pack" name="package">%s</select></div>'
                        '<div><label class="label" for="p-notes">Anything else we should know?</label>'
                        '<textarea class="inp" id="p-notes" name="notes"></textarea></div>'
                        '<button class="btn btn-primary" type="submit">Send enquiry%s</button>'
                        '<p class="form-note">Opens your mail app. We reply within 1 to 2 working days.</p>'
                        '</form>'
                        '<div class="rv"><h3 style="font-size:26px;margin-bottom:18px">Good to know</h3>'
                        '<div class="faq">%s</div></div></div>'
                        % (SITE["email"], inputs,
                           "".join('<option>%s</option>' % g["name"] for g in GENRES),
                           "".join('<option>%s &middot; %s</option>' % (p["name"], p["dur"]) for p in PACKAGES),
                           ARROW, faq_items(FAQ[5][2])), sid="enquiry", cls="section tight"))
    return page("Private sessions", "Private group dance sessions at Al Sarab in Byblos, Lebanon.",
                body, base=base, active="private-events.html")


# ---------------------------------------------------------------- programmes
def programmes_page(base=""):
    body = (phead("Programmes", "Dance in schools, groups and companies",
                  "Al Sarab takes its curriculum outside its own studios &mdash; into schools, "
                  "community groups and company team days. This page is a placeholder for the real "
                  "programme offer.")
            + section(head_block("How it works", "Four steps")
                      + '<div class="steps">'
                        '<div class="step rv"><span class="n">01</span><h3>Tell us the group</h3>'
                        '<p>Age range, number of participants, how many sessions and where.</p></div>'
                        '<div class="step rv"><span class="n">02</span><h3>We design the block</h3>'
                        '<p>A written plan with objectives, drawn from the school curriculum.</p></div>'
                        '<div class="step rv"><span class="n">03</span><h3>We teach it</h3>'
                        '<p>At your site or in our studios, by the same teaching team.</p></div>'
                        '<div class="step rv"><span class="n">04</span><h3>You get a report</h3>'
                        '<p>A written evaluation at the end of the block, as for our own students.</p></div>'
                        '</div>', cls="section tight")
            + section(head_block("Questions", "About programmes")
                      + '<div class="faq rv">%s</div>' % faq_items([
                          ("Which age groups can you work with?",
                           "Placeholder answer. From creative movement at three to adult groups."),
                          ("Do you travel to us?",
                           "Placeholder answer. Travel within Lebanon would be described here."),
                          ("How long is a block?",
                           "Placeholder answer. Typical block lengths would be listed here."),
                          ("How is it priced?",
                           "Placeholder answer. Rates are quoted per programme."),
                          ("Can it end in a performance?",
                           "Placeholder answer."),
                          ("Who teaches it?",
                           "The same teaching team that teaches the school curriculum."),
                      ]), cls="section tight")
            + section('<div class="offer rv"><div><h3>Ready to start?</h3>'
                      '<p>Tell us about the group and we will come back with a plan.</p></div>%s</div>'
                      % btn(base, "contact.html", "Contact the school"), cls="section tight"))
    return page("Programmes", "Dance programmes for schools, groups and companies with Al Sarab.",
                body, base=base, active="corporate-programmes.html")


# ---------------------------------------------------------------- small pages
def terms_page(base=""):
    body = (phead("Terms", "Terms and conditions",
                  "Placeholder. Registration terms, payment and cancellation conditions, photography "
                  "consent and studio rules would be published here.")
            + section('<div class="article rv"><div class="body">'
                      '<h2>Registration</h2><p>Placeholder text.</p>'
                      '<h2>Fees and payment</h2><p>Placeholder text.</p>'
                      '<h2>Cancellation</h2><p>Placeholder text.</p>'
                      '<h2>Photography and filming</h2><p>Placeholder text.</p>'
                      '<h2>Studio rules</h2><p>Placeholder text.</p>'
                      '<h2>Privacy</h2><p>Placeholder text.</p>'
                      '</div></div>', cls="section tight"))
    return page("Terms", "Terms and conditions for Al Sarab Alternative Dance School.",
                body, base=base, active="terms.html")


def portal_page(base=""):
    body = (phero(base, "School &middot; Portal", SITE["portal_name"],
                  "The web app for enrolled students and their families &mdash; assessment "
                  "records, recital call sheets, costume information and school notices, in one "
                  "place. Sign in with the details reception gives you at registration.",
                  "studio-2",
                  app_cta(base))
            + section('<div class="split"><div class="rv">'
                      '<h2 style="font-size:32px;margin-bottom:18px">What is in it</h2>'
                      '<p class="muted" style="font-size:17px">The app is where the written side of '
                      'the curriculum lives. Everything a family would otherwise have to ask '
                      'reception for is in there, kept up to date by the teaching team.</p>'
                      '<p class="muted" style="margin-top:18px">Access is for enrolled students and '
                      'their parents. If you have not received your sign-in details, ask at '
                      'reception on a class day.</p>'
                      '<div style="margin-top:26px">%s</div></div>'
                      '<div class="rv"><div class="rows">'
                      '<div class="row-item"><b>Assessment</b><span>Level objectives, end-of-year '
                      'evaluation, progress across genres</span></div>'
                      '<div class="row-item"><b>Recital</b><span>Call sheets, costume fittings, '
                      'rehearsal dates</span></div>'
                      '<div class="row-item"><b>Timetable</b><span>Your own classes, changes and '
                      'closures</span></div>'
                      '<div class="row-item"><b>Notices</b><span>Messages from the school to your '
                      'family</span></div>'
                      '</div></div></div>' % app_cta(base))
            + section('<div class="offer rv"><div><h3>Not enrolled yet?</h3>'
                      '<p>The app is for registered families. Start with a free trial class.</p>'
                      '</div>%s</div>'
                      % btn(base, "classes.html#trial", "Book a trial class"), cls="section tight"))
    return page("Student &amp; parent portal",
                "The Al Sarab web app for enrolled students and their families.",
                body, base=base, active="portal.html")


def arabic_page(base=""):
    body = (phead("العربية", "The Arabic version is in preparation",
                  "This proposal is built in English first. The Arabic version would mirror it "
                  "completely &mdash; same structure, same modules, right-to-left layout, with "
                  "Arabic typography throughout.")
            + section('<div class="split"><div class="rv">'
                      '<h2 style="font-size:30px;margin-bottom:18px">What an RTL version changes</h2>'
                      '<p class="muted">The layout mirrors: navigation, cards, the schedule grid and '
                      'every table read right to left. Numerals, times and the timetable stay legible '
                      'in both directions.</p>'
                      '<p class="muted" style="margin-top:16px">Typography changes too. The Arabic '
                      'wordmark already sits in the logo; the body face would pair with an Arabic '
                      'family chosen to match its weight and rhythm.</p></div>'
                      '<div class="rv"><div class="facts">'
                      '<div class="r"><span class="k">Direction</span><span class="v">RTL</span></div>'
                      '<div class="r"><span class="k">Scope</span><span class="v">Every page</span></div>'
                      '<div class="r"><span class="k">Status</span><span class="v">Placeholder</span></div>'
                      '</div></div></div>', cls="section tight")
            + section('<div class="offer rv"><div><h3>Back to English</h3>'
                      '<p>The full proposal is on the English pages.</p></div>%s</div>'
                      % btn(base, "index.html", "Go to the homepage"), cls="section tight"))
    return page("العربية", "Arabic version of the Al Sarab site, in preparation.",
                body, base=base, active="ar.html")
