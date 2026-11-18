import base64,pathlib
d=pathlib.Path(__file__).parent
t=(d/'src/template.html').read_text()
b=base64.b64encode((d/'src/site.jpg').read_bytes()).decode()
(d/'index.html').write_text(t.replace('__SITE__',b))
