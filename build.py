import base64,pathlib
d=pathlib.Path(__file__).parent
SITE_URL='https://cehastana.vercel.app'
OG_IMG='https://cdn.jsdelivr.net/gh/qazaqboss/cehastana@main/og-share.jpg'  # картинка с CDN GitHub, не зависит от Vercel  # поменяйте, если проект в Vercel назван иначе
t=(d/'src/template.html').read_text()
b=base64.b64encode((d/'src/site.jpg').read_bytes()).decode()
page=t.replace('__SITE__',b)
(d/'artifact').mkdir(exist_ok=True)
(d/'artifact/index.html').write_text(page)  # версия для Artifact
title='Цех 21×80 м · Astana Baza'
desc='Металлокаркас с мостовым краном 10 т: 3D-модель КМД, генплан, смета. Каркас с доставкой до Астаны — 27,5 млн ₸.'
head=f'''<!doctype html>
<html lang="ru"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{SITE_URL}/">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{OG_IMG}">
<meta property="og:image:secure_url" content="{OG_IMG}">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:alt" content="Цех 21×80 м — металлокаркас, 27,5 млн ₸ с доставкой до Астаны">
<meta property="og:site_name" content="Astana Baza">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="ru_RU">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{OG_IMG}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<style>:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>
'''
title_end=page.index('</title>')+len('</title>')
style_end=page.index('</script>',page.index('importmap'))+len('</script>')
full=head+page[:style_end]+'\n</head><body>\n'+page[style_end:]+'\n</body></html>\n'
(d/'index.html').write_text(full)  # сайт для Vercel (корень репозитория)
