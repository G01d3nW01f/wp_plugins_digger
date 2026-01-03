#!/usr/bin/python3

import re
import requests
from urllib.parse import urljoin
import sys


if len(sys.argv) != 2:
    print("[!]Require: argument <target URL>")
    sys.exit()

url = sys.argv[1]

response = requests.get(url)
#response.raise_for_status()

html = response.text

matches = re.findall(r'/wp-content/plugins/[^"\'<>\s]+', html)

for m in set(matches):
    print(urljoin(url,m))
