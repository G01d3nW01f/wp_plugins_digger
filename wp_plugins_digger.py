#!/usr/bin/python3

import re
import requests
from urllib.parse import urljoin
import sys

if len(sys.argv) != 2:
    print("[!] Require: argument <target URL>")
    sys.exit(1)

url = sys.argv[1]

response = requests.get(url)
html = response.text

# capture the plugin name
pattern = r'/wp-content/plugins/([^/]+)/'

matches = re.findall(pattern, html)

# delete the duplication
plugins = sorted(set(matches))

for plugin in plugins:
    plugin_path = f"/wp-content/plugins/{plugin}/"
    absolute_url = urljoin(url, plugin_path)

    print(absolute_url)
    print(f"  └ Plugin: {plugin}")
