# -*- coding: utf-8 -*-
"""Pack the handover folder into a ZIP that extracts correctly everywhere.

Windows PowerShell 5.1's Compress-Archive writes entry names with backslashes,
which the ZIP spec does not allow (4.4.17.1: forward slashes only). Windows
opens those anyway, but cPanel's extractor and macOS Archive Utility can read
"website\\index.html" as one long filename and flatten the whole tree. This
writes the names correctly.

    py -3 makezip.py <source-dir> <output.zip>
"""

import os
import sys
import zipfile


def main():
    src = os.path.abspath(sys.argv[1])
    out = os.path.abspath(sys.argv[2])
    if os.path.exists(out):
        os.remove(out)

    count = 0
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for root, dirs, files in os.walk(src):
            dirs.sort()
            for name in sorted(files):
                path = os.path.join(root, name)
                arc = os.path.relpath(path, src).replace(os.sep, "/")
                z.write(path, arc)
                count += 1

    size = os.path.getsize(out) / (1024.0 * 1024.0)
    print("%d files -> %s (%.2f MB)" % (count, out, size))

    # read it back and prove the separators survived
    with zipfile.ZipFile(out) as z:
        names = z.namelist()
        bad = [n for n in names if "\\" in n]
        print("entries: %d, backslashes: %d" % (len(names), len(bad)))
        for probe in ("READ-ME-FIRST.html", "website/index.html",
                      "website/assets/site.css", "website/instructors/jimmy-bechara.html"):
            print("  %-44s %s" % (probe, "OK" if probe in names else "MISSING"))
        bad_zip = z.testzip()
        print("integrity: %s" % ("OK" if bad_zip is None else "CORRUPT: " + bad_zip))


if __name__ == "__main__":
    main()
