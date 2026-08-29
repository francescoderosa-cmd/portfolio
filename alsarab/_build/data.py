# -*- coding: utf-8 -*-
"""Content for the Al Sarab site.

REAL = taken from alsarabdance.com (school facts, team, genres, contact).
PLACEHOLDER = invented to fill a module that exists in the reference layout.
Everything placeholder is flagged in the site's top banner.
"""

SITE = dict(
    name="Al Sarab",
    full="Al Sarab Alternative Dance School",
    arabic="السراب",
    city="Byblos",
    country="Lebanon",
    address_1="Center Al Haref",
    address_2="Byblos (Jbeil), Lebanon",
    email="alsarab.dance@gmail.com",
    phone="+961 71 049 801",
    phone_raw="+96171049801",
    phone2="+961 3 181 820",
    phone2_raw="+9613181820",
    hours="Monday &middot; Wednesday &middot; Friday: 4PM &ndash; 9PM",
    hours_short="Mon &middot; Wed &middot; Fri, 4&ndash;9PM",
    maps="https://maps.google.com/?q=Center+Al+Haref+Byblos+Lebanon",
    instagram="https://www.instagram.com/alsarabdanceschool/",
    facebook="https://www.facebook.com/Al-Sarab-alternative-dance-school-111858192203998",
    youtube="https://www.youtube.com/channel/UCjxqdibEFW-hZXMG_28hM1g",
    company="https://www.alsarabdancecompany.com",
    licence="213/2009",
    founded="January 1991",
    founder="Dr. Nadra Majeed Assaf",
    term="2025 / 2026",
    term_dates="22 September &ndash; 20 June",
    updated="21 August 2026",
)

FOOTER_ABOUT = (
    "Al Sarab Alternative Dance School is a curriculum-based dance school at Center Al Haref "
    "in Byblos, Lebanon. A place where technique, discipline and belonging meet. We teach Modern, "
    "Contemporary, Classical Ballet, Jazz, Raqs Sharqi and Acro, from creative movement at three "
    "years old to pre-professional levels. Registered with the Lebanese Ministry of Education under "
    "licence 213/2009 and a member of the National Dance Education Organization (USA). We also open "
    "our studios for rehearsals, workshops and private group sessions."
)

# ---------------------------------------------------------------- studios
STUDIOS = ["j1", "j2", "k1"]
STUDIO = {
    "j1": dict(slug="studio-1", name="Studio 1", loc="Jbeil", img="studio-1",
               size="90 m&sup2;", cap="24 dancers", floor="Sprung floor, marley surface",
               kit="Mirror wall, barres, sound system, air conditioning",
               blurb="The main teaching studio at Center Al Haref. Full mirror wall, "
                     "portable barres and a sprung floor &mdash; the room where most levels train."),
    "j2": dict(slug="studio-2", name="Studio 2", loc="Jbeil", img="studio-2",
               size="60 m&sup2;", cap="16 dancers", floor="Sprung floor, marley surface",
               kit="Mirror wall, barres, sound system, acro mats",
               blurb="The smaller Jbeil room, used for junior groups, acro and small-group "
                     "rehearsal. Mats and crash pads are stored here."),
    "k1": dict(slug="studio-koura", name="Studio", loc="Koura", img="studio-3",
               size="70 m&sup2;", cap="20 dancers", floor="Sprung floor, marley surface",
               kit="Mirror wall, sound system, changing area",
               blurb="The northern branch. The same curriculum, the same assessment, "
                     "taught closer to home for families in Koura and Bishmizzine."),
}

BRANCHES = [
    ("Jbeil", "Center Al Haref, Byblos &mdash; main studio"),
    ("Bishmizzine", "North Lebanon"),
    ("Koura", "North Lebanon"),
    ("La Collina", "Mount Lebanon"),
    ("Rabieh", "Metn"),
]

# ---------------------------------------------------------------- levels
LEVELS = [
    ("Open", "No level requirement. Anyone can join, whatever their background."),
    ("Beginner", "First year in the genre. Technique is built from zero."),
    ("Continuation", "A second or third year. Vocabulary is known, depth is the work."),
    ("Intermediate", "Confident technique. Longer combinations, faster changes."),
    ("Advanced", "Pre-professional. Repertoire, composition and performance."),
]
AGES = [
    ("3&ndash;5 yrs", "Creative movement. 40-minute classes."),
    ("6&ndash;8 yrs", "Foundation levels. Technique introduced through play."),
    ("9&ndash;12 yrs", "Graded levels with written objectives and assessment."),
    ("13&ndash;16 yrs", "Youth levels. Repertoire and performance work."),
    ("Adults", "Open and beginner classes for anyone 17 and over."),
]

# ---------------------------------------------------------------- genres
GENRES = [
    dict(slug="modern", name="Modern", img="modern",
         tagline="Where the school began",
         tags=["Beginner-friendly", "Technique", "Kids &amp; youth", "Adults"],
         short="Release, contraction, floorwork and weight. Modern is the spine of the Al Sarab "
               "curriculum &mdash; every student passes through it, whatever else they dance.",
         long=("Al Sarab opened in 1991 as a Modern Dance school, and Modern is still the genre "
               "every level touches. Classes work from the floor upward: breath, weight, release "
               "and contraction, then travelling phrases that ask a dancer to fall and recover "
               "without losing control.<br><br>"
               "The syllabus is graded. Foundation classes introduce the vocabulary through play; "
               "from Level 1 the work is written down, assessed, and carried forward year to year. "
               "Adult Modern runs as an open class &mdash; the same material, no assessment."),
         expect=["Warm-up on the floor, then centre and travelling",
                 "Barefoot &mdash; no shoes needed",
                 "Written objectives and an end-of-year evaluation from Level 1",
                 "Feeds directly into the Showcase Unit and the recital"]),
    dict(slug="contemporary", name="Contemporary", img="contemporary",
         tagline="Composition and a voice",
         tags=["Technique", "Performance", "Kids &amp; youth", "Adults"],
         short="For dancers who already have technique. Improvisation, partnering and "
               "choreographic composition &mdash; students make work, not only perform it.",
         long=("Contemporary at Al Sarab sits on top of Modern. It assumes the vocabulary is there "
               "and spends its time on what a dancer does with it: improvisation scores, contact "
               "and partnering, and composition.<br><br>"
               "Students in the upper levels are expected to make short works of their own and "
               "defend the choices in them. It is the part of the curriculum closest to how the "
               "Al Sarab Dance Company works."),
         expect=["Entry from Intermediate Modern or by placement",
                 "Improvisation and composition tasks, not only set phrases",
                 "Partnering and contact work in the youth and adult levels",
                 "Student-made pieces shown at the Winter Platform"]),
    dict(slug="classical-ballet", name="Classical Ballet", img="ballet",
         tagline="Technique and line",
         tags=["Beginner-friendly", "Technique", "Kids &amp; youth", "Adults"],
         short="Barre, centre and allegro in a graded syllabus. Placement, turnout and musicality "
               "built slowly, from pre-ballet at six to pointe work in the upper levels.",
         long=("Ballet is taught as the technical reference for the rest of the school. The class "
               "shape does not change &mdash; barre, centre, adage, allegro &mdash; and the "
               "progression is deliberately slow, because placement built badly has to be unbuilt.<br><br>"
               "Pre-ballet starts at six. Pointe work is introduced only when strength and "
               "alignment are assessed as ready, never by age alone. Adult ballet runs as an open "
               "class for returning and first-time dancers."),
         expect=["Ballet shoes required; pointe only when assessed as ready",
                 "Hair up, fitted practice clothes",
                 "Graded syllabus with an end-of-year evaluation",
                 "Adult open class, no experience needed"]),
    dict(slug="jazz", name="Jazz", img="jazz",
         tagline="Rhythm and attack",
         tags=["Beginner-friendly", "High energy", "Performance", "Kids &amp; youth"],
         short="Sharp lines, syncopation and performance quality. Jazz classes build stamina and "
               "stage presence, and feed straight into the end-of-year recital.",
         long=("Jazz is the school's performance engine. Classes are built on isolation work, "
               "syncopation and attack, with combinations that change quickly and demand that a "
               "dancer look up and out rather than down at the floor.<br><br>"
               "Most of the recital repertoire is made in Jazz classes, so the term follows a "
               "rhythm: technique through the autumn, repertoire from the new year, performance "
               "in June."),
         expect=["Jazz shoes or bare feet depending on level",
                 "High-energy warm-up; stamina is part of the work",
                 "Repertoire building from January",
                 "Recital Unit rehearsals on Saturdays for upper levels"]),
    dict(slug="raqs-sharqi", name="Raqs Sharqi", img="raqs",
         tagline="Oriental dance, taught as technique",
         tags=["Beginner-friendly", "Arabic repertoire", "Adults", "Kids &amp; youth"],
         short="The Arab world's own vocabulary, taught with the same rigour as any other "
               "technique: isolations, layering, rhythm reading and the classical repertoire.",
         long=("Raqs Sharqi is taught here as a technique with a syllabus, not as a party skill. "
               "Classes work through isolations, layering, travelling steps and &mdash; the part "
               "most schools skip &mdash; rhythm reading, so a dancer can name what she is hearing "
               "before she dances to it.<br><br>"
               "The genre is directed by Dr. Nadra Assaf, who teaches the upper levels herself. "
               "Adult classes are the most common entry point into the school."),
         expect=["Hip scarf provided for the first class",
                 "Rhythm reading as part of the syllabus",
                 "Classical Egyptian repertoire in the upper levels",
                 "Taught by the school's founding director"]),
    dict(slug="acro", name="Acro", img="acro",
         tagline="Strength and control",
         tags=["Strength", "High energy", "Kids &amp; youth", "Beginner-friendly"],
         short="Balance, flexibility and tumbling taught in a dance context, with spotting and "
               "clear progressions. Runs alongside Modern for junior and youth levels.",
         long=("Acro is dance-context tumbling: balances, limbering, and progressions that are "
               "spotted every step of the way. Nothing is attempted before the conditioning that "
               "supports it, which is why the class always opens with strength work.<br><br>"
               "It is taken alongside Modern rather than instead of it &mdash; the two are "
               "timetabled so a student can do both in the same afternoon."),
         expect=["Mats and crash pads; every skill is spotted",
                 "Conditioning block at the start of every class",
                 "Progressions written down and assessed",
                 "Timetabled to pair with Modern on the same day"]),
]
GENRE_BY_NAME = {g["name"]: g for g in GENRES}

STYLE_FILTERS = ["Beginner-friendly", "Technique", "High energy", "Strength",
                 "Performance", "Arabic repertoire", "Kids &amp; youth", "Adults"]

# ---------------------------------------------------------------- teachers
def _t(slug, name, role, tagline, styles, lead=False):
    return dict(slug=slug, name=name, role=role, tagline=tagline, styles=styles, lead=lead)

TEACHERS = [
    _t("nadra-assaf", "Dr. Nadra Assaf",
       "Founding &amp; Artistic Director &middot; Financial Manager &middot; Curriculum Coordinator",
       "Founded the school in 1991 and still teaches the upper Raqs Sharqi levels",
       ["Raqs Sharqi"], True),
    _t("jimmy-bechara", "Jimmy Bechara",
       "Operations Director &middot; Showcase Unit Lead",
       "Runs the building, the timetable and the Showcase Unit",
       ["Modern", "Acro", "Contemporary"], True),
    _t("myriam-barakat", "Myriam Barakat",
       "Teacher Coordinator &middot; Wardrobe Manager",
       "Coordinates the teaching team and every costume that goes on stage",
       ["Modern", "Acro"], True),
    _t("sarah-fadel", "Sarah Fadel",
       "Assessment Officer &middot; End-of-Year Unit Lead",
       "Keeps the written assessment that makes the curriculum a curriculum",
       ["Modern", "Jazz", "Contemporary"], True),
    _t("rana-balbont", "Rana Balbont",
       "End-of-Year Recital Unit Lead",
       "Leads the recital and the graded ballet syllabus",
       ["Classical Ballet"], True),
    _t("laetita-hakim", "Laetita Hakim",
       "Social Media Manager &middot; Dance Instructor",
       "Teaches Modern and runs everything you see from the school online",
       ["Modern"], True),
    _t("tia-semaan", "Tia Semaan", "Dance Instructor", "Creative movement and junior levels", ["Modern"]),
    _t("dia-chahine", "Dia Chahine", "Dance Instructor", "Junior and youth levels", ["Modern", "Jazz"]),
    _t("diva-chahine", "Diva Chahine", "Dance Instructor", "Junior and youth levels", ["Modern", "Jazz"]),
    _t("angelina-el-hachem", "Angelina El Hachem", "Dance Instructor", "Acro and conditioning", ["Acro"]),
    _t("cyrine-nacouzy", "Cyrine Nacouzy", "Dance Instructor", "Foundation levels, Koura branch", ["Modern"]),
    _t("yvana-makdessi", "Yvana Makdessi", "Dance Instructor", "Creative movement and foundation levels", ["Modern"]),
    _t("rita-khalil", "Rita Khalil", "Dance Instructor", "Ballet, Koura branch", ["Classical Ballet"]),
    _t("lenny-raphael", "Lenny Raphael", "Dance Instructor", "Youth levels", ["Jazz", "Contemporary"]),
    _t("marita-mrad", "Marita Mrad", "Dance Instructor", "Jazz foundation and junior levels", ["Jazz"]),
    _t("gaitana-kafrouny", "Gaitana Kafrouny", "Dance Instructor", "Junior levels", ["Modern", "Acro"]),
]
TEACHER_BY_NAME = {t["name"]: t for t in TEACHERS}

BIO_PLACEHOLDER = (
    "Profile to come. Al Sarab will supply a short biography for every member of the teaching "
    "team &mdash; training, performance background and what they want a student to leave the room "
    "with. This block shows how it will sit on the page."
)

NADRA_BIO = (
    "Dr. Nadra Majeed Assaf founded Al Sarab Alternative Dance School and Al Sarab Dance Company "
    "in January 1991. For more than thirty years she has built the school around embodied pedagogy "
    "&mdash; dance taught as an academic discipline &mdash; in Lebanon and across the Middle East."
)

# ---------------------------------------------------------------- schedule
PRICE = "Fees on request"

def _c(day, studio, start, end, name, genre, level, age, teacher):
    return dict(day=day, studio=studio, start=start, end=end, name=name, genre=genre,
                level=level, age=age, teacher=teacher, price=PRICE,
                slug=GENRE_BY_NAME[genre]["slug"])

CLASSES = [
    # Monday
    _c("MON", "j1", "16:00", "16:40", "Creative Movement", "Modern", "Open", "3&ndash;5 yrs", "Myriam Barakat"),
    _c("MON", "j2", "16:00", "16:55", "Pre-Ballet", "Classical Ballet", "Beginner", "6&ndash;8 yrs", "Rana Balbont"),
    _c("MON", "k1", "16:00", "16:55", "Modern Foundation", "Modern", "Beginner", "6&ndash;8 yrs", "Cyrine Nacouzy"),
    _c("MON", "j1", "17:00", "17:55", "Modern Level 1", "Modern", "Beginner", "9&ndash;12 yrs", "Jimmy Bechara"),
    _c("MON", "j2", "17:00", "17:55", "Ballet Level 2", "Classical Ballet", "Continuation", "9&ndash;12 yrs", "Rana Balbont"),
    _c("MON", "k1", "17:00", "17:55", "Jazz Level 1", "Jazz", "Beginner", "9&ndash;12 yrs", "Marita Mrad"),
    _c("MON", "j1", "18:00", "18:55", "Acro Level 1", "Acro", "Beginner", "9&ndash;12 yrs", "Myriam Barakat"),
    _c("MON", "j2", "18:00", "18:55", "Ballet Level 3", "Classical Ballet", "Advanced", "13&ndash;16 yrs", "Rana Balbont"),
    _c("MON", "j1", "19:00", "19:55", "Modern Level 3", "Modern", "Advanced", "13&ndash;16 yrs", "Jimmy Bechara"),
    _c("MON", "k1", "19:00", "19:55", "Raqs Sharqi &mdash; Adults", "Raqs Sharqi", "Open", "Adults", "Dr. Nadra Assaf"),
    _c("MON", "j2", "20:00", "20:55", "Contemporary &mdash; Youth", "Contemporary", "Intermediate", "13&ndash;16 yrs", "Sarah Fadel"),
    # Wednesday
    _c("WED", "j1", "16:00", "16:40", "Creative Movement", "Modern", "Open", "3&ndash;5 yrs", "Tia Semaan"),
    _c("WED", "j2", "16:00", "16:55", "Acro Foundation", "Acro", "Beginner", "6&ndash;8 yrs", "Angelina El Hachem"),
    _c("WED", "k1", "16:00", "16:55", "Pre-Ballet", "Classical Ballet", "Beginner", "6&ndash;8 yrs", "Rita Khalil"),
    _c("WED", "j1", "17:00", "17:55", "Jazz Level 2", "Jazz", "Continuation", "9&ndash;12 yrs", "Sarah Fadel"),
    _c("WED", "j2", "17:00", "17:55", "Modern Level 2", "Modern", "Continuation", "9&ndash;12 yrs", "Jimmy Bechara"),
    _c("WED", "k1", "17:00", "17:55", "Modern Level 1", "Modern", "Beginner", "9&ndash;12 yrs", "Cyrine Nacouzy"),
    _c("WED", "j1", "18:00", "18:55", "Ballet Level 1", "Classical Ballet", "Beginner", "9&ndash;12 yrs", "Rana Balbont"),
    _c("WED", "j2", "18:00", "18:55", "Acro Level 2", "Acro", "Intermediate", "13&ndash;16 yrs", "Myriam Barakat"),
    _c("WED", "j1", "19:00", "19:55", "Contemporary &mdash; Advanced", "Contemporary", "Advanced", "16+ yrs", "Jimmy Bechara"),
    _c("WED", "k1", "19:00", "19:55", "Jazz &mdash; Adults", "Jazz", "Open", "Adults", "Lenny Raphael"),
    # Friday
    _c("FRI", "j1", "16:00", "16:40", "Creative Movement", "Modern", "Open", "3&ndash;5 yrs", "Yvana Makdessi"),
    _c("FRI", "j2", "16:00", "16:55", "Jazz Foundation", "Jazz", "Beginner", "6&ndash;8 yrs", "Marita Mrad"),
    _c("FRI", "k1", "16:00", "16:55", "Modern Foundation", "Modern", "Beginner", "6&ndash;8 yrs", "Gaitana Kafrouny"),
    _c("FRI", "j1", "17:00", "17:55", "Raqs Sharqi Level 1", "Raqs Sharqi", "Beginner", "9&ndash;12 yrs", "Dr. Nadra Assaf"),
    _c("FRI", "j2", "17:00", "17:55", "Modern Level 2", "Modern", "Continuation", "9&ndash;12 yrs", "Laetita Hakim"),
    _c("FRI", "k1", "17:00", "17:55", "Acro Level 1", "Acro", "Beginner", "9&ndash;12 yrs", "Angelina El Hachem"),
    _c("FRI", "j1", "18:00", "18:55", "Raqs Sharqi Level 2", "Raqs Sharqi", "Intermediate", "13&ndash;16 yrs", "Dr. Nadra Assaf"),
    _c("FRI", "j2", "18:00", "18:55", "Showcase Unit &mdash; Rehearsal", "Contemporary", "Advanced", "13+ yrs", "Jimmy Bechara"),
    _c("FRI", "j1", "19:00", "19:55", "Modern &mdash; Adults", "Modern", "Open", "Adults", "Jimmy Bechara"),
    _c("FRI", "k1", "19:00", "19:55", "Ballet &mdash; Adults", "Classical Ballet", "Open", "Adults", "Rita Khalil"),
    # Saturday
    _c("SAT", "j1", "10:00", "10:40", "Creative Movement", "Modern", "Open", "3&ndash;5 yrs", "Tia Semaan"),
    _c("SAT", "j2", "10:00", "10:40", "Pre-Ballet", "Classical Ballet", "Beginner", "3&ndash;5 yrs", "Rana Balbont"),
    _c("SAT", "k1", "10:00", "10:55", "Modern Foundation", "Modern", "Beginner", "6&ndash;8 yrs", "Cyrine Nacouzy"),
    _c("SAT", "j1", "11:00", "11:55", "Acro Foundation", "Acro", "Beginner", "6&ndash;8 yrs", "Myriam Barakat"),
    _c("SAT", "j2", "11:00", "11:55", "Jazz Level 1", "Jazz", "Beginner", "9&ndash;12 yrs", "Marita Mrad"),
    _c("SAT", "k1", "11:00", "11:55", "Ballet Level 1", "Classical Ballet", "Beginner", "9&ndash;12 yrs", "Rita Khalil"),
    _c("SAT", "j1", "12:00", "12:55", "Contemporary &mdash; Youth", "Contemporary", "Intermediate", "13&ndash;16 yrs", "Sarah Fadel"),
    _c("SAT", "j2", "12:00", "12:55", "Recital Unit &mdash; Rehearsal", "Jazz", "Advanced", "13+ yrs", "Sarah Fadel"),
    _c("SAT", "k1", "12:00", "12:55", "Raqs Sharqi &mdash; Adults", "Raqs Sharqi", "Open", "Adults", "Dr. Nadra Assaf"),
]

DAY_ORDER = [("MON", "Mondays"), ("TUE", "Tuesdays"), ("WED", "Wednesdays"), ("THU", "Thursdays"),
             ("FRI", "Fridays"), ("SAT", "Saturdays"), ("SUN", "Sundays")]

# ---------------------------------------------------------------- events
EVENTS = [
    dict(slug="open-studios-week", cat="Open Day", when="upcoming", free=True,
         date="Monday, 22 September 2025", short_date="22 Sep 2025",
         time="4:00PM &ndash; 9:00PM", place="Center Al Haref, Byblos",
         img="ev-showcase", title="Open Studios Week",
         teaser="The first week of term is open. Every class can be watched or joined once, "
                "free, with no registration.",
         body=["Every September the school opens its first week. Any class on the timetable can "
               "be watched from the side of the room, or joined once, at no cost and with no "
               "registration &mdash; for the child who is not sure, and for the parent who wants "
               "to see how a class is actually run before committing to a year.",
               "Placement advice is given on the spot. If a student joins a class that turns out "
               "to be the wrong level, we will say so and suggest the right one."],
         howto=["Come to Center Al Haref during opening hours on any day of the week",
                "Tell reception which class you would like to try",
                "Bring comfortable clothes &mdash; shoes are not needed for most genres"]),
    dict(slug="winter-platform", cat="Showcase", when="upcoming", free=False,
         date="Saturday, 14 February 2026", short_date="14 Feb 2026",
         time="6:00PM", place="Studio 1, Center Al Haref, Byblos",
         img="ev-recital", title="Winter Platform &mdash; Showcase Unit",
         teaser="A smaller, closer evening: works in progress from the Showcase Unit, shown to "
                "families in the studio where they were made.",
         body=["The Winter Platform is deliberately unpolished. The Showcase Unit shows what it "
               "has been building since September &mdash; sometimes a finished piece, more often "
               "a section, occasionally an idea that is not working yet and is shown anyway.",
               "It is held in Studio 1 rather than a theatre. Families sit on the floor along the "
               "mirror wall, and the dancers talk about the work afterwards."],
         howto=["Open to families of enrolled students",
                "Seating is limited to the studio's capacity &mdash; reserve at reception",
                "Doors at 5:30PM"]),
    dict(slug="end-of-year-recital", cat="Recital", when="upcoming", free=False,
         date="Saturday, 20 June 2026", short_date="20 Jun 2026",
         time="7:00PM", place="Venue to be confirmed, Byblos",
         img="ev-metro", title="End-of-Year Recital 2026",
         teaser="Every level on stage, from the three-year-olds' first entrance to the "
                "pre-professional pieces. The year's assessment made public.",
         body=["The recital is the point of the year. Every level performs, in order, from "
               "creative movement to the advanced repertoire &mdash; which means a parent watching "
               "their five-year-old also watches what that child could be at sixteen.",
               "Repertoire is built from January in Jazz, Modern and Contemporary classes. The "
               "Recital Unit rehearses on Saturdays from the new year."],
         howto=["Tickets through the school from May",
                "Costume fittings are arranged through the wardrobe manager during the spring term",
                "Call times are published two weeks before"]),
    dict(slug="asds-goes-to-the-moon", cat="Archive", when="past", free=False,
         date="2019", short_date="2019",
         time="Evening", place="Metro Al Madina, Beirut",
         img="hero", title="ASDS Goes to the Moon",
         teaser="The school's full production at Metro Al Madina in Beirut. The photographs "
                "across this site are from that stage.",
         body=["Al Sarab took the whole school to Metro Al Madina in Beirut for a full-length "
               "production. Every photograph you see on this site was taken that night.",
               "It remains the reference point for what the school is aiming at: not a recital "
               "in a school hall, but a production, in a theatre, held to a theatre's standard."],
         howto=[]),
    dict(slug="ndeo-workshop", cat="Workshop", when="past", free=False,
         date="Spring 2025", short_date="Spring 2025",
         time="Weekend intensive", place="Center Al Haref, Byblos",
         img="ev-showcase", title="Guest Choreographer Intensive",
         teaser="A weekend intensive with a visiting choreographer, open to Intermediate and "
                "Advanced levels across all genres.",
         body=["Placeholder entry. Al Sarab runs guest workshops through the year; this card shows "
               "how a past workshop sits in the archive.",
               "Replace this text with the real workshop, the choreographer's name and the "
               "repertoire taught."],
         howto=[]),
    dict(slug="recital-2025", cat="Recital", when="past", free=False,
         date="June 2025", short_date="Jun 2025",
         time="Evening", place="Byblos",
         img="ev-recital", title="End-of-Year Recital 2025",
         teaser="Last year's recital &mdash; every level, one evening, the full curriculum shown "
                "in order.",
         body=["Placeholder entry for the previous year's recital, kept in the archive so families "
               "can look back.",
               "Photographs and the running order would sit here."],
         howto=[]),
]

# ---------------------------------------------------------------- news
NEWS = [
    dict(slug="thirty-five-years", cat="Studio News", date="12 August 2026", short_date="12 Aug 2026",
         read="3 min read", img="news-1",
         title="Thirty-five years, one idea: any and every body",
         teaser="Al Sarab opened in January 1991 with one studio and one genre. Here is what has "
                "changed, and the one thing that has not.",
         body=[("h", "One studio, one genre"),
               ("p", "Dr. Nadra Majeed Assaf opened Al Sarab Alternative Dance School in January "
                     "1991, alongside Al Sarab Dance Company. The school taught Modern Dance, and "
                     "for its first years that was the whole offer."),
               ("p", "Modern is still where every student starts, whatever they end up dancing. "
                     "It is the genre the rest of the curriculum is measured against."),
               ("h", "Six genres, one curriculum"),
               ("p", "Over the past fifteen years the programme has widened into six movement "
                     "disciplines: Modern, Contemporary, Classical Ballet, Jazz, Raqs Sharqi and "
                     "Acro. They are not six separate schools sharing a building &mdash; they are "
                     "one written curriculum, so a student who moves between genres does not "
                     "repeat a year of training twice."),
               ("h", "What being curriculum-based actually costs"),
               ("p", "It is easier to run a dance school without written objectives. Being "
                     "curriculum-based means an assessment officer, written level objectives, and "
                     "an end-of-year evaluation for every student &mdash; the work behind the "
                     "Ministry of Education licence 213/2009 and the NDEO membership."),
               ("h", "What has not changed"),
               ("p", "The mission has been the same sentence since 1991: open opportunities in "
                     "the society for any and every body to dance. Everything else &mdash; the "
                     "genres, the branches, the timetable &mdash; has moved around it.")]),
    dict(slug="which-genre-suits-you", cat="Guide", date="30 July 2026", short_date="30 Jul 2026",
         read="4 min read", img="news-2",
         title="Beginner's guide: which genre is right for you?",
         teaser="Modern, Ballet, Jazz, Raqs Sharqi, Contemporary or Acro? A short guide for anyone "
                "who wants to start but does not know where.",
         body=[("p", "There is no wrong first class, but there is a first class that will suit you "
                     "better. Here is how we place people when they call."),
               ("h", "If you have never danced"),
               ("p", "Modern or Raqs Sharqi. Both start from zero without assuming any vocabulary, "
                     "and neither requires shoes or equipment for the first term."),
               ("h", "If you want technique above all"),
               ("p", "Classical Ballet. It is the slowest to feel rewarding and the fastest to "
                     "change how you stand, walk and hold weight."),
               ("h", "If you want to perform"),
               ("p", "Jazz. Most of the recital repertoire is built in Jazz classes, and the "
                     "performance quality is trained from the first lesson."),
               ("h", "If you already have training"),
               ("p", "Contemporary. It assumes vocabulary and spends its time on improvisation, "
                     "partnering and composition."),
               ("h", "If you are seven and cannot sit still"),
               ("p", "Acro, alongside Modern. They are timetabled on the same afternoon for "
                     "exactly this reason.")]),
    dict(slug="the-2025-2026-timetable", cat="Studio News", date="20 June 2026", short_date="20 Jun 2026",
         read="2 min read", img="news-3",
         title="The 2025/2026 timetable is here",
         teaser="Classes across Jbeil and Koura, Monday to Saturday, from creative movement at "
                "three to adult open classes.",
         body=[("p", "The timetable for the coming academic year is published. Classes run in "
                     "Jbeil on Monday, Wednesday and Friday afternoons, in Koura on the same days, "
                     "and there is a full junior programme in Jbeil on Saturday mornings."),
               ("h", "What is new"),
               ("ul", ["Raqs Sharqi adult class added on Saturday mornings in Koura",
                       "Acro moved to pair with Modern on the same afternoon",
                       "Showcase Unit rehearsal moved to Friday evenings"]),
               ("h", "Placement"),
               ("p", "Placement is by age and by level, not by age alone. If you are not sure "
                     "where a student belongs, book a trial class and we will place them after it.")]),
    dict(slug="what-to-bring-first-class", cat="Guide", date="2 June 2026", short_date="2 Jun 2026",
         read="2 min read", img="news-2",
         title="What to bring to your first class",
         teaser="Short answer: less than you think. Here is the list, genre by genre.",
         body=[("p", "Placeholder article. This card and page show how a short practical guide "
                     "sits in the news section."),
               ("p", "The real version would list, per genre, what to wear and what the school "
                     "provides for a first class.")]),
    dict(slug="inside-the-recital", cat="Studio News", date="10 May 2026", short_date="10 May 2026",
         read="3 min read", img="ev-recital",
         title="Inside the recital: six months of work in one evening",
         teaser="How repertoire is built from January, and what the Recital Unit actually does on "
                "Saturday mornings.",
         body=[("p", "Placeholder article. The real version would follow the recital from the "
                     "January repertoire block to the June call sheet."),
               ("p", "Photographs from rehearsal would sit through the body of the piece.")]),
    dict(slug="teaching-at-al-sarab", cat="Studio News", date="18 March 2026", short_date="18 Mar 2026",
         read="2 min read", img="news-1",
         title="Teaching at Al Sarab: what we look for",
         teaser="We hire dancers who can teach, not only dancers. What that means in practice.",
         body=[("p", "Placeholder article. The real version would describe the school's teaching "
                     "standard and how new instructors are brought into the curriculum."),
               ("p", "It would end with the application route.")]),
]

# ---------------------------------------------------------------- faq
FAQ = [
    ("Classes &amp; Schedule", "How the week runs, and what a term looks like.", [
        ("How do I register for a course?",
         "Call +961 71 049 801 or send us a message. We book a trial class in the level we think "
         "fits, and confirm the year place after it."),
        ("Can I try a class before committing?",
         "Yes. Every new student is booked into a trial class first &mdash; it is how we place "
         "people. During Open Studios Week in September, any class can be tried at no cost."),
        ("How long is a class?",
         "Creative movement is 40 minutes. Every other class is 55 minutes."),
        ("Which genres do you teach?",
         "Modern, Contemporary, Classical Ballet, Jazz, Raqs Sharqi and Acro &mdash; taught inside "
         "one written curriculum."),
        ("How long is a term?",
         "The academic year runs from late September to the end of June, following the school "
         "calendar."),
        ("What happens if my child misses a class?",
         "Placeholder answer. The school's make-up policy would be stated here."),
        ("Can we join mid-year?",
         "Placeholder answer. Mid-year entry is usually possible in foundation levels and depends "
         "on the genre and the level."),
        ("What is the difference between Beginner and Continuation?",
         "Beginner is a first year in a genre and builds technique from zero. Continuation is a "
         "second or third year: the vocabulary is known and the work goes deeper."),
        ("How big are the classes?",
         "Placeholder answer. Group sizes per level would be stated here."),
        ("Do parents stay in the room?",
         "Placeholder answer. The policy for creative movement and foundation levels would be "
         "stated here."),
    ]),
    ("Getting Started", "For anyone who has never taken a dance class.", [
        ("Do I need any dance experience?",
         "No. Beginner and Open levels start from zero at every age, including adults."),
        ("What should I wear?",
         "Comfortable clothes you can move in, hair tied back. Ballet needs ballet shoes; most "
         "other genres are barefoot."),
        ("What do I need to bring?",
         "Water and the clothes you will dance in. A hip scarf is provided for a first Raqs Sharqi "
         "class."),
        ("How do you decide which level my child joins?",
         "By age and by level, after a trial class. Age alone does not place a student."),
        ("Is there an age limit for adults?",
         "No. Adult Open classes run in Modern, Ballet, Jazz and Raqs Sharqi."),
        ("Which genre should I start with?",
         "See our <a href=\"news/which-genre-suits-you.html\">beginner's guide</a>, or call us and "
         "describe what you are after."),
    ]),
    ("Fees &amp; Registration", "What it costs and how payment works.", [
        ("How much does a course cost?",
         "Fees depend on the genre, the level and the number of classes per week. They are given "
         "at registration &mdash; call or write and we will send the current sheet."),
        ("How do I pay?",
         "Placeholder answer. Accepted payment methods would be listed here."),
        ("Can fees be paid in instalments?",
         "Placeholder answer. Any instalment plan would be described here."),
        ("Is there a sibling or family reduction?",
         "Placeholder answer."),
        ("What is the cancellation policy?",
         "Placeholder answer."),
        ("Do you offer gift certificates?",
         "Placeholder answer."),
    ]),
    ("Location &amp; Access", "Finding us, and what is in the building.", [
        ("Where is the school?",
         "The main studio is at Center Al Haref, Byblos (Jbeil). There are also branches in "
         "Bishmizzine, Koura, La Collina and Rabieh."),
        ("When is reception open?",
         "Monday, Wednesday and Friday, 4PM to 9PM."),
        ("Is there parking?",
         "Placeholder answer."),
        ("Are the studios accessible?",
         "Placeholder answer. Step-free access and facilities would be described here."),
        ("Are there changing rooms?",
         "Placeholder answer."),
    ]),
    ("Performances", "The recital, the platform, and what families need to know.", [
        ("Does every student perform?",
         "Yes. Every level appears in the End-of-Year Recital in June."),
        ("How are costumes handled?",
         "Through the wardrobe manager, with fittings during the spring term."),
        ("Is performing compulsory?",
         "Placeholder answer."),
        ("Can we buy photographs or video?",
         "Placeholder answer."),
    ]),
    ("Private &amp; Group Sessions", "Birthdays, groups and one-off bookings.", [
        ("Can we book a private group session?",
         "Yes &mdash; see <a href=\"hire-us.html#request\">Hire Us</a> for the formats and "
         "how to enquire."),
        ("What is the minimum group size?",
         "Six people."),
        ("Which genres can we choose?",
         "Raqs Sharqi, Jazz, Modern or Acro, depending on the group."),
        ("How far ahead should we book?",
         "Placeholder answer."),
    ]),
    ("Studio Rental", "Renting a room for rehearsal or a workshop.", [
        ("Can I rent a studio?",
         "Yes, when it is not timetabled. See <a href=\"hire-us.html#studio-booking\">studio booking</a>."),
        ("What is included?",
         "Mirror wall, sprung floor, sound system and air conditioning. Studio 2 also has acro mats."),
        ("What is the minimum booking?",
         "Two hours."),
        ("Can I book a recurring slot?",
         "Placeholder answer."),
    ]),
    ("Other", "Everything else.", [
        ("How do I apply to teach at Al Sarab?",
         "Write to alsarab.dance@gmail.com with your training and teaching experience."),
        ("What makes Al Sarab different from other schools?",
         "It is curriculum-based: written level objectives, an assessment officer and an "
         "end-of-year evaluation, under Ministry of Education licence 213/2009 and NDEO membership."),
        ("Is Al Sarab Dance Company the same as the school?",
         "They share a founder and a home but are separate. The school teaches; the company "
         "performs and tours."),
        ("Do you run classes in schools or for companies?",
         "See <a href=\"hire-us.html#choreography\">Hire Us</a>."),
    ]),
]

# ---------------------------------------------------------------- hire us (one page, four services)
# Each service is a section on hire-us.html with its own "Request info" button.
# Nobody books online: every button opens an enquiry so the school can set price and date.
HIRE_SERVICES = [
    dict(slug="weddings", name="Weddings", img="perf-wedding",
         tagline="We dance at your wedding",
         blurb="A choreographed set danced by Al Sarab at your wedding &mdash; an entrance, a "
               "zaffe, a Raqs Sharqi number, or a full sequence built into the run of the evening. "
               "Nobody in the room has to dance: we perform, you watch.",
         points=["15 to 40 minutes, 4 to 10 dancers",
                 "Choreography built around your run of show",
                 "Music and costume agreed in advance",
                 "Floor plan checked before the date",
                 "We travel across Lebanon"],
         cta="Request info about a wedding"),
    dict(slug="videos", name="Videos", img="contemporary",
         tagline="Dance made for the camera",
         blurb="Choreography created and filmed for a screen rather than a stage &mdash; music "
               "videos, brand films, campaign content, or a piece of your own you want captured "
               "properly. Shot in our studios or on location.",
         points=["Concept and choreography developed with you",
                 "Dancers cast from the school and the company",
                 "Shot in Studio 1 or on location",
                 "Rehearsal and shoot days quoted separately",
                 "Filming crew arranged, or work with yours"],
         cta="Request info about a video"),
    dict(slug="choreography", name="Choreography", img="modern",
         tagline="A piece made for your project",
         blurb="Commissioned choreography for a theatre production, a school show, a competition "
               "piece or a company of your own. Created by Al Sarab and taught to your dancers, "
               "or performed by ours.",
         points=["Original work, or restaging of existing repertoire",
                 "Taught to your dancers or danced by ours",
                 "Creation period agreed with you",
                 "Rehearsal direction through to opening",
                 "Notation and video handover on request"],
         cta="Request info about a commission"),
    dict(slug="studio-booking", name="Studio booking", img="studio-1",
         tagline="Rent one of our rooms",
         blurb="Three professional dance studios at Center Al Haref in Byblos and one in Koura, "
               "available when they are not timetabled. Sprung floors, mirror walls, sound "
               "systems and air conditioning.",
         points=["Studio 1 &middot; Jbeil &mdash; 90 m&sup2;, up to 24 dancers",
                 "Studio 2 &middot; Jbeil &mdash; 60 m&sup2;, up to 16 dancers, acro mats",
                 "Studio &middot; Koura &mdash; 70 m&sup2;, up to 20 dancers",
                 "Two-hour minimum booking",
                 "Rehearsals, workshops, auditions, filming"],
         cta="Request info about a studio"),
]

HIRE_FAQ = [
    ("How do I get a price?",
     "Send an enquiry from any of the sections above. Every booking is different &mdash; the "
     "length, the number of dancers, the travel and the creation time all change the fee &mdash; "
     "so we quote each one individually and come back within 1 to 2 working days."),
    ("How far in advance should I ask?",
     "As early as you can for anything that needs new choreography: a wedding in high season, a "
     "commission, a shoot. A studio booking can usually be arranged in the same week. "
     "Placeholder: confirm the real lead times."),
    ("Do you travel outside Byblos?",
     "Yes, across Lebanon. Travel is included in the quote. Placeholder: confirm whether there is "
     "a distance limit."),
    ("Can we come and learn a dance ourselves instead?",
     "Yes &mdash; a private group session for a birthday, a hen party or a team day. Ask through "
     "the form and say that is what you want."),
    ("Who actually performs?",
     "Placeholder &mdash; to confirm with the school whether bookings are danced by Al Sarab Dance "
     "Company, which tours separately, or by ensembles drawn from the school."),
]

# ---------------------------------------------------------------- merchandising
# Reserve online, pay and collect at the school. No online payment anywhere on this page.
MERCH_NOTE = ("You cannot buy online. Reserve what you want in your name and it is held at "
              "reception for you to try, pay for and collect at the school.")

MERCH_SIZES_ADULT = ["XS", "S", "M", "L", "XL", "XXL"]
MERCH_SIZES_KIDS = ["4&ndash;6", "6&ndash;8", "8&ndash;10", "10&ndash;12", "12&ndash;14"]

MERCH = [
    dict(slug="hoodie", name="Al Sarab hoodie", cat="Outerwear", icon="hoodie",
         blurb="Heavyweight hoodie with the Al Sarab mark on the chest and the Arabic wordmark "
               "across the back. The one everybody wears to and from class.",
         sizes="adult", colours=["Lilac", "Black", "Sand"]),
    dict(slug="tshirt", name="Logo T-shirt", cat="Tops", icon="tshirt",
         blurb="Cotton T-shirt with the school mark. Cut loose enough to warm up in and to pull "
               "over a leotard.",
         sizes="both", colours=["White", "Black", "Lilac"]),
    dict(slug="joggers", name="Joggers", cat="Bottoms", icon="joggers",
         blurb="Tapered joggers with a cuffed ankle, in the same weight as the hoodie. Worn over "
               "practice clothes between classes.",
         sizes="adult", colours=["Black", "Grey"]),
    dict(slug="leggings", name="Training leggings", cat="Bottoms", icon="leggings",
         blurb="High-waisted leggings for Modern, Contemporary and Jazz. Opaque, with a wide "
               "waistband that stays put through floorwork.",
         sizes="both", colours=["Black", "Deep lilac"]),
    dict(slug="leotard", name="Ballet leotard", cat="Uniform", icon="leotard",
         blurb="The graded-syllabus leotard for Classical Ballet levels. Level colours are set by "
               "the syllabus &mdash; reception will tell you which one your level wears.",
         sizes="kids", colours=["By level"]),
    dict(slug="warmup-jacket", name="Warm-up jacket", cat="Outerwear", icon="jacket",
         blurb="Zip-through jacket for recital call times and cold studios in winter. Worn by the "
               "Recital Unit and the Showcase Unit.",
         sizes="both", colours=["Black"]),
    dict(slug="dance-bag", name="Dance bag", cat="Accessories", icon="bag",
         blurb="Holdall with a separate shoe compartment, big enough for a costume and a change "
               "of clothes on recital day.",
         sizes="one", colours=["Black", "Lilac"]),
    dict(slug="tote", name="Cotton tote", cat="Accessories", icon="tote",
         blurb="Canvas tote with the Arabic wordmark. For the ones who only ever bring shoes and "
               "a water bottle.",
         sizes="one", colours=["Natural", "Black"]),
    dict(slug="bottle", name="Water bottle", cat="Accessories", icon="bottle",
         blurb="Insulated steel bottle, 750ml, with the school mark. Reception refills it for free "
               "on class days.",
         sizes="one", colours=["Lilac", "Steel"]),
    dict(slug="socks", name="Grip socks", cat="Accessories", icon="socks",
         blurb="Grip socks for Modern and Contemporary floorwork, and for anyone still deciding "
               "whether to go barefoot.",
         sizes="one", colours=["Black"]),
]

# ---------------------------------------------------------------- summer camp
CAMP = dict(
    year="2027",
    label="Summer Camp 2027",
    dates="Dates to be announced &mdash; expected July 2027",
    ages="6 to 16 years",
    place="Center Al Haref, Byblos, with outdoor sessions nearby",
    daily="9:00AM &ndash; 3:00PM, Monday to Friday",
    length="Two weeks, or one week",
    intro=("Two weeks of dance in the summer, for dancers who train with us all year and for "
           "anyone who wants to try. Mornings are technique, afternoons are making things &mdash; "
           "and the last day is a showing for families."),
    activities=[
        ("Technique every morning", "Modern, Ballet and Jazz taught as a graded block, in the "
         "same curriculum as the school year. Levels are set on the first morning."),
        ("Choreography lab", "Campers make their own short pieces in small groups, with a teacher "
         "attached to each group. It is the part they remember."),
        ("Acro and conditioning", "Spotted tumbling, balances and strength work on mats, for "
         "everyone regardless of level."),
        ("Raqs Sharqi and rhythm", "Isolations, layering and rhythm reading &mdash; the Arabic "
         "repertoire taught as a technique, not as a party trick."),
        ("Outdoors and away from the mirror", "Afternoons out of the studio: games, improvisation "
         "in the open air, and a day trip in the second week."),
        ("Showing on the last day", "Everything made during the camp, shown to families. No "
         "tickets, no costumes bought &mdash; just the work."),
    ],
    reserve_note=("Places for Summer 2027 can be reserved now. Reserving costs nothing and holds a "
                  "name on the list &mdash; we contact you with dates, fees and the full programme "
                  "as soon as they are set."),
    last=dict(
        label="Summer Camp 2026",
        when="July 2026",
        summary=("The 2026 camp ran for two weeks in Byblos across all six genres. Mornings were "
                 "technique, afternoons were the choreography lab, and the final Friday was a "
                 "showing for families in Studio 1."),
        stats=[("Campers", "Placeholder"), ("Weeks", "Two"), ("Teachers", "Placeholder"),
               ("Pieces made", "Placeholder")],
        gallery=["acro", "jazz", "contemporary", "raqs", "news-2", "ev-showcase"],
    ),
)

CAMP_FAQ = [
    ("Does my child need dance experience?",
     "No. Levels are set on the first morning and beginners are placed together. Campers who train "
     "with us all year continue in their own level."),
    ("What should they bring?",
     "Clothes they can move in, a water bottle, lunch and a change of clothes for the afternoon. "
     "Ballet shoes only if they already have them."),
    ("How much does it cost?",
     "Fees for 2027 are not set yet. Reserve a place and we will send them as soon as they are, "
     "with no obligation."),
    ("Can they come for one week instead of two?",
     "Yes. Say so when you reserve and we will hold a one-week place."),
    ("Is there transport?",
     "Placeholder &mdash; confirm whether pick-up is offered and from where."),
    ("What happens on the last day?",
     "A showing in Studio 1 of everything made during the camp. Families are invited; there is "
     "nothing to buy and nothing to prepare."),
]

# ---------------------------------------------------------------- performances for hire
# NOTE FOR REVIEW: it is not yet settled whether the performers are Al Sarab Dance
# Company (which tours separately) or ensembles drawn from the school. The copy below
# is deliberately neutral — it says "Al Sarab" — and the Ensemble row in the facts box
# is flagged as unconfirmed. Settle this before the page goes anywhere public.
PERFORMANCE_FORMATS = [
    dict(name="Wedding", img="perf-wedding", featured=True,
         dur="15&ndash;40 min", size="4&ndash;10 dancers",
         genres="Raqs Sharqi, Jazz, Modern",
         blurb="An entrance, a set piece, or a full sequence built into the evening. "
               "The zaffe tradition and a choreographed Raqs Sharqi number are the two "
               "most-asked-for; both can be cut to the length your venue allows.",
         items=["Choreography built for your run of show",
                "Costume and music agreed in advance",
                "Site visit or floor plan check before the date",
                "Travel across Lebanon"]),
    dict(name="Private party", img="ev-showcase", featured=False,
         dur="10&ndash;25 min", size="3&ndash;6 dancers",
         genres="Raqs Sharqi, Jazz",
         blurb="A short, high-energy set for a birthday, an anniversary or a house "
               "celebration. Small enough to work in a room without a stage.",
         items=["Works without a stage or rig",
                "Repertoire from our existing pieces",
                "One set or two shorter appearances",
                "Music supplied or matched to your DJ"]),
    dict(name="Corporate &amp; gala", img="ev-recital", featured=False,
         dur="20&ndash;45 min", size="6&ndash;14 dancers",
         genres="Contemporary, Modern, Raqs Sharqi",
         blurb="A programmed piece for an opening, an award evening or a company "
               "celebration &mdash; closer to a concert set than to entertainment.",
         items=["Programmed as a sequence, not a single number",
                "Technical rider for lighting and sound",
                "Rehearsal in the venue where possible",
                "Bilingual introduction if needed"]),
    dict(name="Exclusive show", img="hero", featured=False,
         dur="45&ndash;70 min", size="10+ dancers",
         genres="Full repertoire",
         blurb="A full-length commissioned work, or an existing production restaged "
               "for your venue &mdash; as Al Sarab did at Metro Al Madina in Beirut.",
         items=["Original commission or restaging",
                "Creation period agreed with you",
                "Full technical and wardrobe production",
                "Photography and filming arranged"]),
]

PERF_FAQ = [
    ("How far in advance should we book?",
     "For a wedding in high season, as early as you can &mdash; choreography, costume and "
     "rehearsal all sit before the date. For a short party set, a few weeks is usually enough. "
     "Placeholder: confirm the real lead times."),
    ("Do you travel outside Byblos?",
     "Yes, across Lebanon. Travel is quoted with the booking. Placeholder: confirm whether there "
     "is a distance limit and how travel is charged."),
    ("Can the choreography be made for us specifically?",
     "Yes. Every wedding and gala booking is built around your run of show, your venue and the "
     "music you want. Existing repertoire is the faster and cheaper route if you prefer it."),
    ("What do you need from the venue?",
     "A flat, clean performance area and a way to play the music. Anything beyond that &mdash; "
     "lighting, a raised stage, a sound engineer &mdash; is agreed in the technical rider."),
    ("How much does it cost?",
     "Rates depend on the format, the number of dancers, the length and the travel. Every booking "
     "is quoted individually &mdash; send an enquiry and we will come back within 1 to 2 working days."),
    ("Is this the same thing as booking a class?",
     "No. Here Al Sarab comes to you and performs. If you want your group to learn a dance "
     "themselves, that is a private group session &mdash; ask through the Hire Us form."),
]

# ---------------------------------------------------------------- private sessions
PACKAGES = [
    dict(name="Classic", dur="60 min", price="On request", featured=False,
         items=["Private studio", "One instructor", "Warm-up and a short choreography",
                "Up to 10 people"]),
    dict(name="Extended", dur="90 min", price="On request", featured=True,
         items=["Private studio", "One instructor", "Warm-up, choreography and freestyle",
                "Choreography filmed", "Up to 15 people"]),
    dict(name="Full", dur="120 min", price="On request", featured=False,
         items=["Two studios", "Two instructors", "Full programme across two genres",
                "Choreography filmed", "Up to 25 people"]),
]
