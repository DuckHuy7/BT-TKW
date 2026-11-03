"""Check local links; optionally compare the deployed HTML/CSS/JS byte for byte."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import urllib.request,hashlib,json,sys
root=Path(__file__).resolve().parents[1]
class Check(HTMLParser):
 def __init__(self):
  super().__init__();self.ids=set();self.links=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.add(a['id'])
  for k in ['src','href']:
   if a.get(k):self.links.append(a[k])
c=Check();c.feed((root/'index.html').read_text())
for link in c.links:
 u=urlsplit(link)
 if u.scheme or u.netloc:continue
 if u.path:assert (root/unquote(u.path)).is_file(),f'Missing file: {link}'
 elif u.fragment:assert u.fragment in c.ids,f'Missing anchor: {link}'
print('PASS: local resources and fragment links')
if '--online' in sys.argv:
 results=[]
 for name in ['index.html','style.css','script.js']:
  with urllib.request.urlopen('https://duckhuy7.github.io/BT-TKW/'+name,timeout=30) as r:
   data=r.read();status=r.status
  local=(root/name).read_bytes()
  results.append({'file':name,'http_status':status,'matches_local':data==local,'sha256':hashlib.sha256(data).hexdigest()})
 print(json.dumps(results,indent=2))
 assert all(x['http_status']==200 and x['matches_local'] for x in results),'Deployment differs from local. Wait for the correct workflow to finish.'
