"""
Reading a web page

    python -m pip install requests
"""

import requests

r = requests.get('http://www.wikipedia.org')
print(r.status_code)
print(r.text[:100])
