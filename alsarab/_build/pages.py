# -*- coding: utf-8 -*-
"""Page bodies, part 1: home, booking, schedule, genres, teachers."""

import json
from data import (SITE, STUDIOS, STUDIO, GENRES, GENRE_BY_NAME, STYLE_FILTERS, TEACHERS,
                  TEACHER_BY_NAME, BIO_PLACEHOLDER, NADRA_BIO, CLASSES, DAY_ORDER, LEVELS,
                  AGES, BRANCHES, PRICE)
from shell import (page, section, head_block, phero, phead, crumbs, btn, faq_items, ARROW)

# ---------------------------------------------------------------- shared bits
def img(base, name):
    return "%sassets/img/%s.jpg" % (base, name)


def schedule_data_js(base):
    rows = [dict(day=c["day"], studio=c["studio"], start=c["start"], end=c["end"], name=c["name"],
                 genre=c["genre"], level=c["level"], age=c["age"], teacher=c["teacher"],
                 price=c["price"], slug=c["slug"]) for c in CLASSES]
    studio_map = {k: dict(name=v["name"], loc=v["loc"]) for k, v in STUDIO.items()}
    return ("var BASE=%s;var STUDIOS=%s;var STUDIO=%s;var CLASSES=%s;"
            % (json.dumps(base), json.dumps(STUDIOS), json.dumps(studio_map), json.dumps(rows)))


def schedule_controls(term=True, teacher=True, beginner=True):
    genres = "".join('<option value="%s">%s</option>' % (g["name"], g["name"]) for g in GENRES)
    teachers = "".join('<option value="%s">%s</option>' % (t["name"], t["name"]) for t in TEACHERS)
    levels = "".join('<option value="%s">%s</option>' % (l, l) for l, _ in LEVELS)
    out = '<div class="controls rv">'
    if term:
        out += ('<div class="field"><label class="label" for="f-term">Academic year</label>'
                '<select id="f-term"><option>%s &mdash; %s</option></select></div>'
                % (SITE["term"], SITE["term_dates"]))
    out += ('<div class="field"><label class="label" for="f-genre">Dance genre</label>'
            '<select id="f-genre"><option value="">All genres</option>%s</select></div>' % genres)
    if teacher:
        out += ('<div class="field"><label class="label" for="f-teacher">Teacher</label>'
                '<select id="f-teacher"><option value="">All teachers</option>%s</select></div>' % teachers)
    out += ('<div class="field"><label class="label" for="f-level">Level</label>'
            '<select id="f-level"><option value="">All levels</option>%s</select></div>' % levels)
    out += ('<div class="field"><label class="label" for="f-loc">Location</label>'
            '<select id="f-loc"><option value="">All locations</option>'
            '<option value="Jbeil">Jbeil</option><option value="Koura">Koura</option></select></div>')
    if beginner:
        out += ('<div class="field check"><span class="label">&nbsp;</span>'
                '<label class="toggle" for="f-beg"><input type="checkbox" id="f-beg">'
                'Beginner-friendly</label></div>')
    out += '</div>'
    return out


def schedule_module(view_toggle=True):
    return ('<div class="tabs" id="days" data-tabs="days" role="tablist" aria-label="Day of the week"></div>'
            + ('<div style="display:flex;justify-content:flex-end;margin-bottom:16px">'
               '<div class="segmented" id="view">'
               '<button type="button" data-view="studio" aria-pressed="true">By studio</button>'
               '<button type="button" data-view="week" aria-pressed="false">One column</button>'
               '</div></div>' if view_toggle else "")
            + '<div class="grid-wrap"><div id="sched" data-day="MON"></div></div>')


def style_card(base, g, cls="style-card rv"):
    tags = "".join('<span class="tag">%s</span>' % t for t in g["tags"][:3])
    return ('<article class="%s" data-tags="%s"><div class="ph" style="background-image:url(%s)"></div>'
            '<div class="body"><div class="meta">%s</div><h3>%s</h3><p>%s</p>'
            '<div class="links"><a href="%sdance-styles/%s.html">Explore %s</a>'
            '<a href="%sclasses.html#schedule">See classes</a></div></div></article>'
            % (cls, "|".join(g["tags"]), img(base, g["img"]), tags, g["name"], g["short"],
               base, g["slug"], g["name"], base))


def person_card(base, t):
    initials = "".join(p[0] for p in t["name"].replace("Dr. ", "").split()[:2]).upper()
    bio = NADRA_BIO if t["slug"] == "nadra-assaf" else BIO_PLACEHOLDER
    return ('<article class="person-card rv"><div class="avatar" role="img" aria-label="Portrait of %s '
            'to come"><span>%s</span></div><div class="body"><p class="tagline">%s</p>'
            '<h3><a href="%sinstructors/%s.html">%s</a></h3><p>%s</p>'
            '<div class="foot"><a class="linkarrow" href="%sinstructors/%s.html">View profile%s</a>'
            '<span class="ig">Instagram &mdash; to come</span></div></div></article>'
            % (t["name"], initials, t["role"], base, t["slug"], t["name"], bio, base, t["slug"], ARROW))


def classes_for_teacher(name):
    return [c for c in CLASSES if c["teacher"] == name]


def classes_for_genre(genre):
    return [c for c in CLASSES if c["genre"] == genre]


def flat_table(base, rows, book=True):
    head = ('<thead><tr><th>Time</th><th>Class</th><th>Level</th><th>Age</th><th>Studio</th>'
            '<th>Teacher</th><th>Fee</th>' + ('<th></th>' if book else '') + '</tr></thead>')
    body = ""
    for c in sorted(rows, key=lambda x: (x["start"], STUDIO[x["studio"]]["name"])):
        body += ('<tr><td class="t">%s&ndash;%s</td>'
                 '<td class="n"><a href="%sdance-styles/%s.html">%s</a></td>'
                 '<td><span class="tag lv">%s</span></td><td>%s</td><td>%s &middot; %s</td>'
                 '<td><a href="%sinstructors/%s.html">%s</a></td><td>%s</td>'
                 % (c["start"], c["end"], base, c["slug"], c["name"], c["level"], c["age"],
                    STUDIO[c["studio"]]["name"], STUDIO[c["studio"]]["loc"], base,
                    TEACHER_BY_NAME[c["teacher"]]["slug"], c["teacher"], c["price"]))
        if book:
            body += '<td><a class="btn btn-primary btn-sm" href="%scontact.html">Book</a></td>' % base
        body += '</tr>'
    return '<div class="grid-wrap"><table class="flat">%s<tbody>%s</tbody></table></div>' % (head, body)


# ---------------------------------------------------------------- home
def home(base=""):
    genre_names = ", ".join(g["name"] for g in GENRES[:-1]) + " and " + GENRES[-1]["name"]

    hero = ('<header class="hero" id="top" aria-label="%s">'
            '<div class="hero-bg" style="background-image:url(%s)" role="img" '
            'aria-label="Al Sarab dancers on stage at Metro Al Madina, Beirut"></div>'
            '<div class="hero-in"><div class="container">'
            '<p class="label">Alternative Dance School &middot; Byblos, Lebanon &middot; Since 1991</p>'
            '<h1>Any and every<em>body can dance.</em></h1>'
            '<p>Al Sarab is one of the very few curriculum-based dance schools in Lebanon &mdash; '
            'accredited by the Lebanese Ministry of Education and a member of the National Dance '
            'Education Organization (USA). %s, for every age.</p>'
            '<div class="hero-cta">%s%s</div>'
            '<div class="hero-facts">'
            '<div><p class="label">Founded</p><strong>%s, by %s</strong></div>'
            '<div><p class="label">Ministry licence</p><strong>No. %s</strong></div>'
            '<div><p class="label">Branches</p><strong>Jbeil &middot; Koura &middot; Rabieh</strong></div>'
            '</div></div></div></header>'
            % (SITE["full"], img(base, "hero"), genre_names,
               btn(base, "classes.html", "Book your first class", "btn-light"),
               btn(base, "#schedule", "See the schedule", "btn-outline-light", arrow=False),
               SITE["founded"], SITE["founder"], SITE["licence"]))

    sched = section(
        head_block("Weekly schedule", "When are classes at Al Sarab?",
                   "Classes run Monday, Wednesday and Friday afternoons in Jbeil and Koura, with a "
                   "full junior programme on Saturday mornings. Most classes are 55 minutes. "
                   "Places are booked for the academic year.")
        + schedule_controls(teacher=False, beginner=True)
        + schedule_module(view_toggle=False)
        + '<p class="note">Sample timetable. The confirmed grid, fees and age placement are given at '
          'registration &mdash; <a href="%scontact.html">ask us for the current schedule</a>.</p>'
          '<div style="margin-top:26px">%s</div>' % (base, btn(base, "schedule.html", "View full schedule", "btn-ghost")),
        sid="schedule")

    lead = TEACHERS[0]
    teachers = section(
        head_block("Our teachers", "The people behind the movement",
                   "Sixteen instructors, choreographers and dance educators. Every class is taught "
                   "inside a written curriculum, with assessment, levels and end-of-year evaluation "
                   "&mdash; the reason families stay with Al Sarab for years.")
        + '<div class="feature rv"><div class="ph" style="background-image:url(%s)" role="img" '
          'aria-label="Al Sarab dancer on stage"></div><div class="body">'
          '<p class="label">Founding &amp; Artistic Director</p><h3>%s</h3>'
          '<p class="role">%s</p>'
          '<blockquote>&ldquo;Open opportunities in the society for any and every body to dance.&rdquo;</blockquote>'
          '<p>%s</p><div>%s</div></div></div>'
          % (img(base, "modern"), lead["name"], lead["role"], NADRA_BIO,
             btn(base, "instructors/nadra-assaf.html", "View profile", "btn-ghost"))
        + '<div class="cards g4" style="margin-top:32px">%s</div>'
          % "".join(person_card(base, t) for t in TEACHERS[1:5])
        + '<div style="margin-top:32px">%s</div>' % btn(base, "instructors.html", "All teachers", "btn-ghost"),
        sid="teachers")

    classes = section(
        head_block("Our classes", "Six genres, one curriculum",
                   "Al Sarab began with Modern Dance. Over the last fifteen years the programme has "
                   "widened into a full movement curriculum, with levels running from pre-school "
                   "creative movement to pre-professional training.")
        + '<div class="cards g3">%s</div>' % "".join(style_card(base, g) for g in GENRES)
        + '<div style="margin-top:32px">%s</div>' % btn(base, "dance-styles.html", "All dance genres", "btn-ghost"),
        sid="classes")

    from data import EVENTS, NEWS
    up = [e for e in EVENTS if e["when"] == "upcoming"][:3]
    events = section(
        head_block("Events &amp; performances", "What's happening at Al Sarab",
                   "Students perform. The school runs a showcase unit, an end-of-year recital, and "
                   "open workshops with guest choreographers &mdash; and its company has taken the "
                   "stage from Byblos to Beirut.")
        + '<div class="cards g3">%s</div>' % "".join(event_card(base, e) for e in up)
        + '<div style="margin-top:32px">%s</div>' % btn(base, "events.html", "All events", "btn-ghost"),
        sid="events")

    news = section(
        head_block("News &amp; stories", "From the studio",
                   "Guides, teacher interviews, student stories and news from the school.")
        + '<div class="cards g3">%s</div>' % "".join(news_card(base, n) for n in NEWS[:3])
        + '<div style="margin-top:32px">%s</div>' % btn(base, "news.html", "All news", "btn-ghost"),
        sid="news")

    about = section(
        head_block("About the school", "Thirty-five years of dance education in Lebanon")
        + '<div class="split">'
          '<div class="rv"><p>For over 30 years, Al Sarab Alternative Dance School has been a place '
          'committed to the embodied pedagogy of the dancers of Lebanon. The school opened in January '
          '1991 with a focus on Modern Dance; over the past fifteen years it has grown into a '
          'curriculum covering six movement disciplines.</p>'
          '<p>Al Sarab is a curriculum-based school registered with the Ministry of Education '
          '(Lebanon) under licence number 213/2009, and a member of the National Dance Education '
          'Organization (USA) &mdash; one of the very few schools in the country to hold both.</p>'
          '<div class="pull">Our mission is to open opportunities in the society for any and every '
          'body to dance.<cite>Dr. Nadra Majeed Assaf, Founding Director</cite></div>'
          '<p>The school\'s home is in Jbeil (Byblos), with branches that have carried the programme '
          'north to Koura and south towards Beirut. Its sister ensemble, Al Sarab Dance Company, '
          'tours separately &mdash; you can find them at <a href="%s" target="_blank" rel="noopener" '
          'style="color:var(--brand)">alsarabdancecompany.com</a>.</p>'
          '<div class="stamp"><span>Ministry of Education 213/2009</span><span>NDEO member (USA)</span>'
          '<span>Curriculum-based</span><span>Ages 3 to adult</span></div>'
          '<div style="margin-top:26px">%s</div></div>'
          '<div class="rv"><div style="border-radius:var(--radius);overflow:hidden;aspect-ratio:4/5;'
          'background:var(--deep) url(%s) center/cover" role="img" aria-label="Al Sarab dancers '
          'performing on stage"></div>'
          '<div class="rows" style="margin-top:30px">%s</div></div>'
          '</div>'
          % (SITE["company"], btn(base, "about.html", "More about the school", "btn-ghost"),
             img(base, "about"),
             "".join('<div class="row-item"><b>%s</b><span>%s</span></div>' % (n, d) for n, d in BRANCHES)),
        sid="about")

    from data import FAQ
    faq = section(
        head_block("FAQ", "Frequently asked questions",
                   "Everything families ask us before the first class &mdash; registration, ages, "
                   "levels and what to bring.")
        + '<div class="faq rv">%s</div>' % faq_items(FAQ[1][2][:6])
        + '<div style="margin-top:32px">%s</div>' % btn(base, "faq.html", "All questions", "btn-ghost"),
        sid="faq")

    contact = section(contact_block(base), sid="contact")

    return page("Al Sarab Dance School",
                "Curriculum-based dance school in Byblos, Lebanon. Modern, Contemporary, Classical "
                "Ballet, Jazz, Raqs Sharqi and Acro for every age, since 1991.",
                hero + sched + teachers + classes + events + news + about + faq + contact,
                base=base, active="index.html",
                extra_js="schedule.js", data_js=schedule_data_js(base))


# ---------------------------------------------------------------- shared cards
def event_card(base, e):
    tags = '<span class="tag hot">%s</span>' % e["cat"]
    if e["free"]:
        tags += '<span class="tag free">Free</span>'
    return ('<article class="card rv"><div class="ph" style="background-image:url(%s)"></div>'
            '<div class="body"><div class="meta">%s</div><h3>%s</h3><p>%s</p>'
            '<div class="foot"><span>%s</span><span>%s</span>'
            '<a class="linkarrow" href="%sevents/%s.html">View details%s</a></div></div></article>'
            % (img(base, e["img"]), tags, e["title"], e["teaser"], e["date"], e["place"],
               base, e["slug"], ARROW))


def news_card(base, n):
    return ('<article class="card rv"><div class="ph" style="background-image:url(%s)"></div>'
            '<div class="body"><div class="meta"><span class="tag hot">%s</span>'
            '<span class="tag">%s &middot; %s</span></div><h3>%s</h3><p>%s</p>'
            '<div class="foot"><a class="linkarrow" href="%snews/%s.html">Read article%s</a></div>'
            '</div></article>'
            % (img(base, n["img"]), n["cat"], n["short_date"], n["read"], n["title"], n["teaser"],
               base, n["slug"], ARROW))


def contact_block(base, heading="Visit us in Byblos"):
    return (head_block("Contact", heading,
                       "Reception answers on class days. For registration, timetables and fees, a "
                       "phone call is usually the fastest way.")
            + '<div class="split"><div class="rv"><div class="info">'
              '<div><p class="label">Address</p><p>%s<br>%s</p></div>'
              '<div><p class="label">Opening hours</p><p>%s</p></div>'
              '<div><p class="label">Phone</p><a href="tel:%s">%s</a><br><a href="tel:%s">%s</a></div>'
              '<div><p class="label">Email</p><a href="mailto:%s">%s</a></div></div>'
              '<div style="margin-top:26px">%s</div>'
              '<p class="label" style="color:var(--ink-2);margin:34px 0 14px">Follow the school</p>'
              '%s</div>%s</div>'
              % (SITE["address_1"], SITE["address_2"], SITE["hours"],
                 SITE["phone_raw"], SITE["phone"], SITE["phone2_raw"], SITE["phone2"],
                 SITE["email"], SITE["email"],
                 btn(base, SITE["maps"], "Open in Google Maps", "btn-ghost", arrow=False),
                 social_pills(), contact_form(base)))


def social_pills():
    from shell import IC_IG, IC_FB, IC_YT
    return ('<div class="social">'
            '<a href="%s" target="_blank" rel="noopener">%sInstagram</a>'
            '<a href="%s" target="_blank" rel="noopener">%sFacebook</a>'
            '<a href="%s" target="_blank" rel="noopener">%sYouTube</a></div>'
            % (SITE["instagram"], IC_IG, SITE["facebook"], IC_FB, SITE["youtube"], IC_YT))


def contact_form(base, subject="Class enquiry"):
    opts = ["Registration and placement", "Fees", "Private group session", "Studio rental",
            "Teaching application", "Something else"]
    return ('<form class="box rv" data-mailto="%s" data-subject="%s">'
            '<div><label class="label" for="c-name">Name</label>'
            '<input class="inp" id="c-name" name="name" required></div>'
            '<div><label class="label" for="c-mail">Email</label>'
            '<input class="inp" id="c-mail" name="email" type="email" required></div>'
            '<div><label class="label" for="c-subj">Subject</label>'
            '<select class="inp" id="c-subj" name="subject">%s</select></div>'
            '<div><label class="label" for="c-msg">Message</label>'
            '<textarea class="inp" id="c-msg" name="message" placeholder="Age of the student, genre '
            'you\'re interested in, preferred branch&hellip;" required></textarea></div>'
            '<button class="btn btn-primary" type="submit">Send message%s</button>'
            '<p class="form-note">This opens your mail app with the message ready to send to %s. '
            'We reply within 1 to 2 working days.</p></form>'
            % (SITE["email"], subject,
               "".join('<option>%s</option>' % o for o in opts), ARROW, SITE["email"]))


# ---------------------------------------------------------------- classes (booking)
def classes_page(base=""):
    levels = "".join('<div class="row-item"><b>%s</b><span>%s</span></div>' % (n, d) for n, d in LEVELS)
    ages = "".join('<div class="row-item"><b>%s</b><span>%s</span></div>' % (n, d) for n, d in AGES)

    body = (phero(base, "Classes", "Dance classes in Byblos &mdash; schedule and booking",
                  "Six genres across three studios in Jbeil and Koura. Book a place for the academic "
                  "year, or come for a trial class first. Every level is available to beginners and "
                  "no experience is needed to start.", "jazz",
                  btn(base, "#schedule", "See this week", "btn-light", arrow=False)
                  + btn(base, "pricing.html", "Fees", "btn-outline-light", arrow=False))
            + section(head_block("Levels &amp; ages", "How the levels work",
                                 "Placement is by age and by level, not by age alone. A trial class "
                                 "decides where a student starts.")
                      + '<div class="split"><div class="rv"><p class="label" style="color:var(--brand);'
                        'margin-bottom:14px">Levels</p><div class="rows">%s</div></div>'
                        '<div class="rv"><p class="label" style="color:var(--brand);margin-bottom:14px">'
                        'Age groups</p><div class="rows">%s</div></div></div>' % (levels, ages),
                      cls="section tight")
            + section(head_block("This week", "Classes at Al Sarab")
                      + schedule_controls()
                      + schedule_module()
                      + '<p class="note">Sample timetable &mdash; the confirmed grid is given at '
                        'registration. Last updated %s.</p>' % SITE["updated"],
                      sid="schedule")
            + section(head_block("Booking", "Three ways to join")
                      + '<div class="cards g3">'
                        '<div class="price-card rv"><h3>Academic year</h3>'
                        '<p class="amount">%s<small>%s &middot; %s</small></p>'
                        '<ul><li>A place in one class per week</li><li>Assessment and end-of-year '
                        'evaluation</li><li>Recital place included</li><li>Costume billed separately</li></ul>'
                        '%s</div>'
                        '<div class="price-card rv featured"><h3>Two or more classes</h3>'
                        '<p class="amount">%s<small>Per additional class</small></p>'
                        '<ul><li>Second and third genres at a reduced rate</li>'
                        '<li>Timetabled to pair on the same afternoon</li>'
                        '<li>One assessment record across genres</li><li>Sibling reduction available</li></ul>'
                        '%s</div>'
                        '<div class="price-card rv"><h3>Trial class</h3>'
                        '<p class="amount">Free<small>One class, before you commit</small></p>'
                        '<ul><li>Placement advice on the spot</li><li>No registration needed</li>'
                        '<li>Any genre, any branch</li><li>Free all week during Open Studios</li></ul>'
                        '%s</div></div>'
                        % (PRICE, SITE["term"], SITE["term_dates"],
                           btn(base, "contact.html", "Register", "btn-ghost"),
                           PRICE, btn(base, "contact.html", "Ask about rates", "btn-primary"),
                           btn(base, "contact.html", "Book a trial", "btn-ghost")))
            + section(head_block("Dance genres", "What you can study here")
                      + '<div class="cards g3">%s</div>' % "".join(style_card(base, g) for g in GENRES))
            + section(head_block("Questions", "Before you book")
                      + '<div class="faq rv">%s</div>' % faq_items([
                          ("How much does a course cost?",
                           "Fees depend on the genre, the level and the number of classes per week, "
                           "and are given at registration. Call +961 71 049 801 and we will send the "
                           "current sheet."),
                          ("Can I try before registering?",
                           "Yes. Every new student is booked into a trial class first &mdash; it is "
                           "how we place people."),
                          ("Do I need experience?",
                           "No. Beginner and Open levels start from zero at every age, including adults."),
                          ("Can I take more than one genre?",
                           "Yes, and the timetable is built for it &mdash; Acro pairs with Modern on "
                           "the same afternoon, for example."),
                      ])
                      + '<div style="margin-top:32px">%s</div>' % btn(base, "faq.html", "All questions", "btn-ghost"),
                      cls="section tight"))

    return page("Classes", "Dance classes in Byblos, Lebanon &mdash; schedule, levels and booking at "
                "Al Sarab Alternative Dance School.", body, base=base, active="classes.html",
                extra_js="schedule.js", data_js=schedule_data_js(base))


# ---------------------------------------------------------------- full schedule
def schedule_page(base=""):
    groups = ""
    for key, label in DAY_ORDER:
        rows = [c for c in CLASSES if c["day"] == key]
        groups += '<div class="daygroup rv"><h3 id="day-%s">%s</h3>%s</div>' % (
            key.lower(), label,
            flat_table(base, rows) if rows
            else '<p class="empty" style="border:1px solid var(--line);border-radius:var(--radius)">'
                 'No classes on %s.</p>' % label)

    levels = "".join('<div class="row-item"><b>%s</b><span>%s</span></div>' % (n, d) for n, d in LEVELS)
    ages = "".join('<div class="row-item"><b>%s</b><span>%s</span></div>' % (n, d) for n, d in AGES)

    body = (phead("Weekly schedule", "The full week at Al Sarab",
                  "%d classes a week across six genres and three studios in Jbeil and Koura. "
                  "Most classes are 55 minutes. Places are booked for the academic year %s."
                  % (len(CLASSES), SITE["term"]))
            + section('<div class="split"><div class="rv"><p class="label" style="color:var(--brand);'
                      'margin-bottom:14px">Levels</p><div class="rows">%s</div></div>'
                      '<div class="rv"><p class="label" style="color:var(--brand);margin-bottom:14px">'
                      'Age groups</p><div class="rows">%s</div></div></div>'
                      '<p class="note">Schedule last updated %s. For the interactive version with '
                      'filters, use <a href="%sclasses.html">classes &amp; booking</a>, or see '
                      '<a href="%stoday.html">what\'s on today</a>.</p>'
                      % (levels, ages, SITE["updated"], base, base), cls="section tight")
            + section(groups, cls="section tight")
            + section('<div class="offer rv"><div><h3>Machine-readable schedule</h3>'
                      '<p>A JSON and plain-text feed of the timetable would sit here, so the schedule '
                      'can be pulled into other systems. Placeholder module.</p></div>'
                      '<span class="tag ph">Placeholder</span></div>', cls="section tight"))

    return page("Schedule", "The full weekly dance class schedule at Al Sarab in Byblos, Lebanon.",
                body, base=base, active="schedule.html")


# ---------------------------------------------------------------- drop-in
def dropin_page(base=""):
    body = (phead("Drop-in", "Join a single class",
                  "Drop-in places are released when a class has room, so anyone can join a single "
                  "session without registering for the year. All levels welcome.")
            + section('<div class="grid-wrap rv"><p class="empty">'
                      '<strong style="display:block;font-family:Oswald,sans-serif;font-size:22px;'
                      'color:var(--ink);margin-bottom:10px">Drop-in places open when term starts</strong>'
                      'We add drop-in places once the academic year timetable is confirmed. '
                      'In the meantime, a trial class is free &mdash; call %s.</p></div>'
                      '<div style="margin-top:26px;display:flex;gap:12px;flex-wrap:wrap">%s%s</div>'
                      % (SITE["phone"], btn(base, "contact.html", "Book a trial class"),
                         btn(base, "schedule.html", "See the schedule", "btn-ghost")))
            + section(head_block("How it works", "Drop-in in three steps")
                      + '<div class="steps">'
                        '<div class="step rv"><span class="n">01</span><h3>Pick a class</h3>'
                        '<p>Choose any class on the timetable that matches your level and age group.</p></div>'
                        '<div class="step rv"><span class="n">02</span><h3>Call ahead</h3>'
                        '<p>Reception confirms there is room. Drop-in depends on the class not being full.</p></div>'
                        '<div class="step rv"><span class="n">03</span><h3>Come and dance</h3>'
                        '<p>Arrive ten minutes early. Bring water and clothes you can move in.</p></div>'
                        '<div class="step rv"><span class="n">04</span><h3>Decide after</h3>'
                        '<p>If it fits, the drop-in fee is credited against year registration.</p></div></div>',
                      cls="section tight"))
    return page("Drop-in", "Join a single dance class at Al Sarab without registering for the year.",
                body, base=base, active="drop-in.html")


# ---------------------------------------------------------------- today
def today_page(base=""):
    body = (phead("Today", "What's on today",
                  "The classes running right now at Center Al Haref and in Koura. Use the day tabs "
                  "to look at the rest of the week.")
            + section(schedule_controls(term=False, teacher=False)
                      + schedule_module()
                      + '<p class="note">Sample timetable. Reception confirms availability on the day '
                        '&mdash; <a href="tel:%s">%s</a>.</p>' % (SITE["phone_raw"], SITE["phone"]),
                      cls="section tight"))
    return page("Today", "Dance classes running today at Al Sarab in Byblos, Lebanon.",
                body, base=base, active="today.html",
                extra_js="schedule.js", data_js=schedule_data_js(base))


# ---------------------------------------------------------------- dance styles
def styles_index(base=""):
    chips = "".join('<button class="chip" type="button" aria-pressed="false" data-value="%s">%s</button>'
                    % (f, f) for f in STYLE_FILTERS)
    body = (phead("Dance genres", "Six genres, one curriculum",
                  "Whether you are stepping into a dance class for the first time or training for "
                  "the stage, there is a genre and a level that fits where you are right now.")
            + section('<div class="chips rv" data-filter-group="#style-grid" style="margin-bottom:34px">%s</div>'
                      '<div class="cards g3" id="style-grid">%s</div>'
                      '<p class="empty" data-filter-empty hidden>No genre matches that filter.</p>'
                      % (chips, "".join(style_card(base, g) for g in GENRES)), cls="section tight")
            + section('<div class="offer rv"><div><h3>Not sure where to start?</h3>'
                      '<p>Book a free trial class and we will place you after it.</p></div>%s</div>'
                      % btn(base, "contact.html", "Book a trial class"), cls="section tight"))
    return page("Dance genres", "The six dance genres taught at Al Sarab in Byblos, Lebanon.",
                body, base=base, active="dance-styles.html")


def style_detail(g, base="../"):
    rows = classes_for_genre(g["name"])
    teachers = sorted({c["teacher"] for c in rows})
    tcards = "".join(person_card(base, TEACHER_BY_NAME[t]) for t in teachers)
    expect = "".join('<li>%s</li>' % e for e in g["expect"])
    levels_here = sorted({c["level"] for c in rows})

    body = (phero(base, "Dance genre", g["name"], g["short"], g["img"],
                  btn(base, "contact.html", "Book a trial class", "btn-light")
                  + btn(base, "classes.html#schedule", "See the schedule", "btn-outline-light", arrow=False))
            + crumbs(base, [("Home", "index.html"), ("Dance genres", "dance-styles.html"), (g["name"], None)])
            + section('<div class="split"><div class="rv"><p class="label" style="color:var(--brand);'
                      'margin-bottom:16px">About</p><h2 style="font-size:34px;margin-bottom:20px">%s at '
                      'Al Sarab</h2><p style="font-size:17px">%s</p></div>'
                      '<div class="rv"><div class="facts">'
                      '<div class="r"><span class="k">Levels</span><span class="v">%s</span></div>'
                      '<div class="r"><span class="k">Ages</span><span class="v">%s</span></div>'
                      '<div class="r"><span class="k">Class length</span><span class="v">40&ndash;55 min</span></div>'
                      '<div class="r"><span class="k">Studios</span><span class="v">%s</span></div>'
                      '<div class="r"><span class="k">Fee</span><span class="v">%s</span></div></div>'
                      '<p class="label" style="color:var(--brand);margin:30px 0 14px">What to expect</p>'
                      '<ul class="ticks">%s</ul>'
                      '</div></div>'
                      % (g["name"], g["long"], ", ".join(levels_here) or "&mdash;",
                         "3 yrs to adult", "Jbeil &middot; Koura", PRICE, expect))
            + section(head_block("Timetable", "%s classes this week" % g["name"],
                                 "Every %s class on the current timetable, across both branches."
                                 % g["name"])
                      + flat_table(base, rows), sid="schedule")
            + section(head_block("Teachers", "Who teaches %s" % g["name"])
                      + '<div class="cards g4">%s</div>' % tcards, cls="section tight")
            + section('<div class="offer rv"><div><h3>Try %s</h3>'
                      '<p>A free trial class, then placement advice. Call %s or send a message.</p></div>%s</div>'
                      % (g["name"], SITE["phone"], btn(base, "contact.html", "Book a trial class")),
                      cls="section tight"))

    return page(g["name"], "%s classes at Al Sarab Alternative Dance School, Byblos, Lebanon."
                % g["name"], body, base=base, active="dance-styles.html")


# ---------------------------------------------------------------- teachers
def teachers_index(base=""):
    body = (phead("Teachers", "The people behind the movement",
                  "Our teachers are dancers, choreographers and dance educators. They teach inside a "
                  "written curriculum, with levels, assessment and an end-of-year evaluation &mdash; "
                  "and they are the reason students come back.")
            + section('<div class="cards g4">%s</div>' % "".join(person_card(base, t) for t in TEACHERS),
                      cls="section tight")
            + section('<div class="offer rv"><div><h3>Teach at Al Sarab</h3>'
                      '<p>We look for dancers who can teach, not only dancers. Write to us with your '
                      'training and teaching experience.</p></div>%s</div>'
                      % btn(base, "mailto:" + SITE["email"], "Get in touch", "btn-primary", arrow=False),
                      cls="section tight"))
    return page("Teachers", "The teaching team at Al Sarab Alternative Dance School, Byblos, Lebanon.",
                body, base=base, active="instructors.html")


def teacher_detail(t, base="../"):
    rows = classes_for_teacher(t["name"])
    bio = NADRA_BIO if t["slug"] == "nadra-assaf" else BIO_PLACEHOLDER
    initials = "".join(p[0] for p in t["name"].replace("Dr. ", "").split()[:2]).upper()
    styles = "".join('<a class="chip" style="text-decoration:none" href="%sdance-styles/%s.html">%s</a>'
                     % (base, GENRE_BY_NAME[s]["slug"], s) for s in t["styles"])

    body = (crumbs(base, [("Home", "index.html"), ("Teachers", "instructors.html"), (t["name"], None)])
            + '<section class="section tight"><div class="container">'
              '<div class="feature rv"><div class="avatar" style="aspect-ratio:auto;min-height:420px">'
              '<span style="font-size:72px">%s</span></div>'
              '<div class="body"><p class="label">%s</p><h1 style="font-size:40px">%s</h1>'
              '<p class="role">%s</p><p>%s</p>'
              '<p class="label" style="color:var(--brand);margin-top:10px">Genres taught</p>'
              '<div class="chips">%s</div></div></div></div></section>'
              % (initials, "Teaching team", t["name"], t["role"], bio, styles)
            + section(head_block("Background", "About %s" % t["name"])
                      + '<div class="rv" style="max-width:70ch"><p class="muted" style="font-size:17px">'
                        'Placeholder. A longer background &mdash; training, companies danced with, '
                        'teaching qualifications and approach &mdash; would sit here, in the school\'s '
                        'own words.</p></div>', cls="section tight")
            + section(head_block("Timetable", "Classes with %s" % t["name"])
                      + (flat_table(base, rows) if rows else
                         '<p class="empty" style="border:1px solid var(--line);border-radius:var(--radius)">'
                         'No classes on the current timetable.</p>'), cls="section tight")
            + section('<div class="offer rv"><div><h3>Book a class with %s</h3>'
                      '<p>Call %s or send a message and we will place you in the right level.</p></div>%s</div>'
                      % (t["name"], SITE["phone"], btn(base, "contact.html", "Book a trial class")),
                      cls="section tight"))

    return page(t["name"], "%s teaches at Al Sarab Alternative Dance School in Byblos, Lebanon."
                % t["name"], body, base=base, active="instructors.html")
