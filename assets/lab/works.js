/* ══════════════════════════════════════════════════════════════════════
   THE LAB · works data
   To add a work: 1) drop optimized .webp images in assets/lab/
                  2) add an entry here (id must be unique, kebab-case)
                  3) add a matching <article> card in lab.html (copy one)
   type: "painting" | "green-lab" | "experiment"
   meta: free-form rows rendered as label/value in the detail panel.
   ba:   optional { before, after } pair, renders a drag comparison slider.
   Only fields that exist are rendered, everything is optional but
   id, type, title, cover, images.
   ══════════════════════════════════════════════════════════════════════ */
var WORKS = [
  {
    id: "side-table",
    type: "experiment",
    title: "Psychedelic side table",
    cover: "assets/lab/table-06.webp",
    images: [
      "assets/lab/table-06.webp",
      "assets/lab/table-04.webp",
      "assets/lab/table-03.webp",
      "assets/lab/table-05.webp",
      "assets/lab/table-01.webp"
    ],
    ba: { before: "assets/lab/table-01.webp", after: "assets/lab/table-04.webp" },
    meta: { base: "Store-bought green tray table", technique: "Hand-painted acrylic flow" },
    note: "A plain tray table as the starting point, repainted by hand with a psychedelic flow texture. Drag the handle in the first view to compare before and after."
  },
  {
    id: "star-hand",
    type: "painting",
    title: "Catch the star",
    cover: "assets/lab/starhand-01.webp",
    images: ["assets/lab/starhand-01.webp"],
    meta: { medium: "Acrylic on canvas" },
    note: "A hand reaching through waves of night sky to hold a star."
  },
  {
    id: "flow-studies",
    type: "painting",
    title: "Flow studies",
    cover: "assets/lab/waves-01.webp",
    images: ["assets/lab/waves-01.webp", "assets/lab/waves-02.webp"],
    meta: { medium: "Acrylic on canvas" },
    note: "Studies of the wave language that later spread onto furniture and other pieces."
  },
  {
    id: "eye-studies",
    type: "painting",
    title: "Eye studies",
    cover: "assets/lab/eyes-01.webp",
    images: ["assets/lab/eyes-01.webp", "assets/lab/eyes-02.webp"],
    meta: { medium: "Acrylic on canvas" },
    note: "Two canvases from the same series, eyes multiplying and dissolving into the flow."
  },
  {
    id: "third-eye",
    type: "painting",
    title: "Third eye",
    cover: "assets/lab/thirdeye-01.webp",
    images: ["assets/lab/thirdeye-01.webp", "assets/lab/thirdeye-02.webp"],
    meta: { medium: "Mixed media on raw canvas" },
    note: "Black hands reaching for an eye with a marbled iris, painted on raw canvas."
  },
  {
    id: "moss-frames",
    type: "green-lab",
    title: "Moss wall art",
    cover: "assets/lab/mosswall-01.webp",
    images: ["assets/lab/mosswall-01.webp", "assets/lab/mosswall-02.webp", "assets/lab/mosswall-03.webp"],
    meta: { format: "Framed botanical panels", contents: "Preserved moss, ferns, eucalyptus" },
    note: "Framed compositions of preserved moss and greens, zero-maintenance little forests. The last shot is a panel in the making."
  },
  {
    id: "jar-world",
    type: "green-lab",
    title: "Jar ecosystem",
    cover: "assets/lab/jar-02.webp",
    images: ["assets/lab/jar-02.webp", "assets/lab/jar-03.webp", "assets/lab/jar-04.webp", "assets/lab/jar-01.webp"],
    meta: { jar: "Closed jar, wooden lid", contents: "Moss, lava rock, creeping plants" },
    note: "A sealed little world built around a lava rock, photographed through the glass."
  },
  {
    id: "demijohn",
    type: "green-lab",
    title: "Demijohn forest",
    cover: "assets/lab/demijohn-02.webp",
    images: ["assets/lab/demijohn-02.webp", "assets/lab/demijohn-01.webp"],
    meta: { jar: "Glass demijohn", contents: "Maidenhair fern, fittonia, ivy, moss" },
    note: "The biggest build so far, a bottled forest living on its own microclimate."
  },
  {
    id: "dome",
    type: "green-lab",
    title: "Under the dome",
    cover: "assets/lab/dome-01.webp",
    images: ["assets/lab/dome-01.webp", "assets/lab/dome-02.webp", "assets/lab/dome-03.webp"],
    meta: { jar: "Glass dome", contents: "Ivy, bark, moss" },
    note: "A small sealed dome, built around a piece of bark."
  },

  /* ── early design work (university years and just after, via Behance) ── */
  {
    id: "qr-note",
    type: "design",
    title: "Qr-Note Agenda",
    cover: "assets/lab/qrnote-01.webp",
    images: ["assets/lab/qrnote-01.webp","assets/lab/qrnote-02.webp","assets/lab/qrnote-03.webp","assets/lab/qrnote-05.webp","assets/lab/qrnote-04.webp"],
    meta: { kind: "IED thesis project", year: "2011" },
    note: "Graduation thesis at IED: a paper agenda that bridges analog and digital through embroidered and printed QR codes."
  },
  {
    id: "mug-agency",
    type: "design",
    title: "MUG Agency",
    cover: "assets/lab/mug-03.webp",
    images: ["assets/lab/mug-03.webp","assets/lab/mug-01.webp","assets/lab/mug-02.webp"],
    meta: { kind: "Logo and identity" },
    note: "Logo and visual identity for a creative agency, a mug as the meeting point."
  },
  {
    id: "shut-up-munch",
    type: "design",
    title: "Shut Up Munch",
    cover: "assets/lab/munch-01.webp",
    images: ["assets/lab/munch-01.webp","assets/lab/munch-02.webp","assets/lab/munch-03.webp","assets/lab/munch-04.webp"],
    meta: { kind: "Naming and logo studies" },
    note: "Naming, logotype and mark studies for an entertainment project, three directions explored."
  },
  {
    id: "filas-report",
    type: "design",
    title: "Filas Annual Report",
    cover: "assets/lab/filas-01.webp",
    images: ["assets/lab/filas-01.webp","assets/lab/filas-02.webp","assets/lab/filas-03.webp","assets/lab/filas-04.webp"],
    meta: { kind: "Editorial design", year: "2013" },
    note: "Layout and art direction for the Filas 2013 annual report, geometric shapes as a navigation system."
  },
  {
    id: "casa-lavica",
    type: "design",
    title: "Casa Lavica",
    cover: "assets/lab/casalavica-02.webp",
    images: ["assets/lab/casalavica-02.webp","assets/lab/casalavica-01.webp"],
    meta: { kind: "Logo design" },
    note: "Logo for a living and recording studio, a lava stone drawn as a single line."
  },
  {
    id: "casa-oca",
    type: "design",
    title: "La Casa dell'Oca",
    cover: "assets/lab/bbrome-01.webp",
    images: ["assets/lab/bbrome-01.webp","assets/lab/bbrome-02.webp"],
    meta: { kind: "Brand identity" },
    note: "Identity and stationery for a bed and breakfast in Rome."
  },
  {
    id: "cuollo",
    type: "design",
    title: "Claudia Cuollo, psicologa",
    cover: "assets/lab/cuollo-01.webp",
    images: ["assets/lab/cuollo-01.webp"],
    meta: { kind: "Personal identity" },
    note: "A quiet personal mark for a psychologist's practice."
  },
  {
    id: "lubec",
    type: "design",
    title: "LuBeC, Lucca Beni Culturali",
    cover: "assets/lab/lubec-01.webp",
    images: ["assets/lab/lubec-01.webp"],
    meta: { kind: "Event graphic" },
    note: "Key visual for a cultural heritage event, Greek vases dissolving into QR mosaics."
  },
  {
    id: "type-posters",
    type: "design",
    title: "Type posters",
    cover: "assets/lab/poster-01.webp",
    images: ["assets/lab/poster-01.webp","assets/lab/poster-02.webp"],
    meta: { kind: "Typography studies" },
    note: "Poster studies celebrating classic typefaces, Gotham and Eurostile."
  },
  {
    id: "urban-strangers",
    type: "design",
    title: "Urban Strangers, Empty Bed",
    cover: "assets/lab/urban-01.webp",
    images: ["assets/lab/urban-01.webp"],
    meta: { kind: "Release banner", year: "2015" },
    note: "Launch banner for a single release on Casa Lavica Records."
  },
  {
    id: "pangea-app",
    type: "design",
    title: "Pangea e-commerce app",
    cover: "assets/lab/pangea-01.webp",
    images: ["assets/lab/pangea-01.webp"],
    meta: { kind: "App concept" },
    note: "Concept UI for a marketplace of world food and crafts."
  },
  {
    id: "esposito-app",
    type: "design",
    title: "Portfolio app, A. Esposito",
    cover: "assets/lab/espositoapp-01.webp",
    images: ["assets/lab/espositoapp-01.webp"],
    meta: { kind: "App concept" },
    note: "Portfolio app concept for photographer Alessandro Esposito."
  }
];
