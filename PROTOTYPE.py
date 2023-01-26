# ver-00 PROTOTYPE
# 

import urllib.request
import requests

#%% with library urllib
url = "https://www.google.com"
encoding = 'ISO-8859-1'
with urllib.request.urlopen(url) as response:
    html = str(response.read(),encoding)
    
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response2:
    html2 = str(response2.read(), encoding)


#%% with library requests
resp = requests.get('https://www.google.com').text

