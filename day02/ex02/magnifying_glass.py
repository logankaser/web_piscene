#!/usr/bin/env python3

import sys
import xml.etree.ElementTree as ET

if len(sys.argv) > 1:
    tree = ET.parse(sys.argv[1])
    for link in tree.iter("a"):
        if "title" in link.attrib:
            link.attrib["title"] = link.attrib["title"].upper()
        link.text = link.text.upper()
        for img in link.iter("img"):
            if "title" in img.attrib:
                img.attrib["title"] = img.attrib["title"].upper()
    print(ET.tostring(tree.getroot(), method="html", encoding="unicode"))
