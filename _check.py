from pathlib import Path
from lxml import etree as E
import json,re,sys,hashlib
sys.path.insert(0,'/Volumes/LaCie/open-commentary/_tools')
from build_repo import load_units,load_commentary
W=Path(__file__).parent;R=E.parse(str(W/'sources/official.xml'));U=load_units(W);C=load_commentary(W)
nodes=[n for n in R.findall('norm') if (n.findtext('metadaten/enbez') or '').startswith(('§','Anlage'))]
compact=lambda t:re.sub(r'\s','',t)
errors=[]
for n,u in zip(nodes,U):
 if n.findtext('metadaten/enbez')!=u['label']:errors.append('label:'+u['id'])
 t=n.find('textdaten/text');raw=''.join(t.itertext()) if t is not None else ''
 if raw and compact(raw)!=compact(u['text']):errors.append('text:'+u['id'])
 if u['id'] not in C:errors.append('missing:'+u['id'])
 if not u['text']:errors.append('empty:'+u['id'])
if len(nodes)!=len(U):errors.append('count mismatch')
if set(C)!=set(u['id'] for u in U):errors.append('commentary key mismatch')
meta=json.loads((W/'meta.json').read_text());repo=Path(meta['repo_dir'])
links=[]
for p in repo.glob('*.md'):
 for target in re.findall(r'\]\(([^)]+)\)',p.read_text()):
  if '://' not in target and not target.startswith('#') and not (repo/target.split('#')[0]).exists():links.append(str(p.name)+':'+target)
errors+=links
result=dict(ok=not errors,errors=errors,xml_statutory_units=len(nodes),parsed_units=len(U),commented_units=len(C),annexes=sum(u['label'].startswith('Anlage') for u in U),repealed=[u['id'] for u in U if u['repealed']],whitespace_independent_xml_equality=True if not errors else False,commentary_chars={k:len(v) for k,v in C.items()},source_files_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (W/'sources').iterdir() if p.is_file()})
(W/'completeness.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));print(json.dumps(result,ensure_ascii=False));sys.exit(bool(errors))
