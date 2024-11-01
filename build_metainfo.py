#!/usr/bin/env python3
import datetime
import json
import re
import yaml

import requests
from pkg_resources import packaging
from xml.sax.saxutils import escape

#from resolve_download import Version


pattern = re.compile(r'Version (\d+(\.\d+)?)(\s-\s(\d{1,2}\/\d{1,2}\/\d{4}))?(.*?(?=Version))', re.S)
list_pattern = re.compile(r'\s-\s*(.*)')

###
# Find the current tag
###
min_version = None
with open("org.paulpacifico.ShutterEncoder.yaml") as stream:
    result = yaml.safe_load(stream)
    modules = result['modules']
    module = next(module for module in modules if module['name'] == "shutter-encoder")
    tag = module['sources'][0]['tag']
    min_version = packaging.version.parse(tag)

###
# Enumerate the ChangeLog
###
response = requests.get('https://www.shutterencoder.com/changelog.txt')
releases = ""

matches = re.finditer(pattern, response.text)
for idx, match in enumerate(matches):
    version_text = match.group(1)
    date_text = match.group(4)
    changes_text = match.group(5).strip().replace("\r", "")
    changes_html = "<ul>\n"

    current_version = packaging.version.parse(version_text)
    if current_version > min_version:
        continue

    if date_text is None:
        continue

    date = datetime.datetime.strptime(date_text, "%d/%m/%Y")
    date_text = date.strftime("%Y-%m-%d")

    list_matches = re.finditer(list_pattern, changes_text)
    for idx, list_match in enumerate(list_matches):
        if list_match.group(1):
            li = escape(list_match.group(1))
            changes_html += "<li>" + li + "</li>\n"
    changes_html += "</ul>\n" 

    release = """
          <release version=\"""" + version_text + """\" date=\"""" + date_text + """\">
            <description>""" + changes_html + """</description>
          </release>"""

    releases += release

template = \
"""<?xml version="1.0" encoding="UTF-8"?>
<component type="desktop-application">
  <id>org.paulpacifico.ShutterEncoder</id>
  <metadata_license>FSFAP</metadata_license>
  <project_license>GPL-3.0-only</project_license>
  <name>Shutter Encoder</name>
  <summary>A converter designed by video editors</summary>

  <description>
    <p>
List of Functions:
– Without conversion:
Cut without re-encoding, Replace audio, Rewrap, Conform, Merge, Extract, Subtitling, Video inserts
– Sound conversions:
WAV, AIFF, FLAC, ALAC, MP3, AAC, AC3, OPUS, Vorbis, Dolby Digital Plus, Dolby TrueHD
– Editing codecs:
DNxHD, DNxHR, Apple ProRes, QT Animation, GoPro CineForm, Uncompressed
– Output codecs:
H.264, H.265, H.266, VP8, VP9, AV1
– Broadcast codecs:
XDCAM HD422, AVC-Intra 100, XAVC, HAP 
– Old codecs:
Theora, MPEG-2, MJPEG, Xvid, DV PAL, WMV, MPEG-1
– Archiving codec:
FFV1
– Images creation:
JPEG, Image
– Burn &amp; Rip:
DVD, Blu-ray, DVD RIP
– Analysis:
Loudness &amp; True Peak, Audio normalization, Cut detection, Black detection, Media offline detection, VMAF
– Download:
Web video
    </p>
  </description>

  <launchable type="desktop-id">org.paulpacifico.ShutterEncoder.desktop</launchable>

  <screenshots>
    <screenshot type="default">
      <caption>Player</caption>
      <image>https://www.shutterencoder.com/images/en/Player.png</image>
     </screenshot>
     <screenshot>
      <caption>Color</caption>
      <image>https://www.shutterencoder.com/images/en/Color.png</image>
     </screenshot>
     <screenshot>
      <caption>Crop</caption>
      <image>https://www.shutterencoder.com/images/en/Crop.png</image>
     </screenshot>
     <screenshot>
      <caption>Overlay</caption>
      <image>https://www.shutterencoder.com/images/en/Overlay.png</image>
     </screenshot>
     <screenshot>
      <caption>Burn Subtitles</caption>
      <image>https://www.shutterencoder.com/images/en/BurnSubtitles.png</image>
     </screenshot>
     <screenshot>
       <caption>Watermark</caption>
       <image>https://www.shutterencoder.com/images/en/Watermark.png</image>
     </screenshot>
   </screenshots>
 
  <url type="homepage">https://www.shutterencoder.com/</url>
  <project_group>Paul Pacifico</project_group>

   <provides>
    <binary>ShutterEncoder.jar</binary>
  </provides>

  <releases>    
    """ + releases + """
  </releases>
</component>
"""

with open(f"org.paulpacifico.ShutterEncoder.metainfo.xml", 'w') as f:
    f.write(template)

