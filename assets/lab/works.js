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
  }
];
