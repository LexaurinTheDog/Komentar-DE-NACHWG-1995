from pathlib import Path
from lxml import etree as E
import json,re,hashlib
W=Path(__file__).parent
R=E.parse(str(W/'sources/official.xml'))
units=[];structure=[]
def render(e):
 if e is None:return ''
 s=e.text or ''
 for c in e:
  v=render(c)
  if c.tag in ('P','LA','DT','DD','TR','BR'):s+='\n\n'+v+'\n\n'
  else:s+=v
  s+=c.tail or ''
 return s
for n in R.findall('norm'):
 m=n.find('metadaten');en=m.findtext('enbez') or '';title=m.findtext('titel') or ''
 gl=m.find('gliederungseinheit')
 if gl is not None:
  level=len(gl.findtext('gliederungskennzahl') or '')//3
  structure=structure[:max(0,level-1)]+[(gl.findtext('gliederungsbez') or '')+' — '+(gl.findtext('gliederungstitel') or '')]
 if not (en.startswith('§') or en.startswith('Anlage')):continue
 text=re.sub(r'\n[ \t]*\n(?:\s*\n)+','\n\n',render(n.find('textdaten/text'))).strip()
 repealed='weggefallen' in title or 'aufgehoben' in title
 if not text and repealed:text=title
 num=int(re.search(r'\d+',en).group());milog='MILOG' in W.name
 chapter=(1 if num<=12 else 2 if num<=21 else 3) if milog else 1
 notes=[render(x).strip() for x in n.findall('textdaten/fussnoten') if render(x).strip()]
 units.append(dict(id='p'+str(num),label=en,title=title,text=text,chapter=chapter,structure=structure.copy(),notes=notes,repealed=repealed))
(W/'units.jsonl').write_text(''.join(json.dumps(u,ensure_ascii=False)+'\n' for u in units))
(W/'sources/canonical.md').write_text('\n\n'.join(u['label']+' '+u['title']+'\n\n'+u['text'] for u in units))
print(W.name,len(units))
