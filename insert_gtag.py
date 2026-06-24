from pathlib import Path
snippet = """<!-- Google tag (gtag.js) -->
<script async src=\"https://www.googletagmanager.com/gtag/js?id=G-DKNLTK2M5F\"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-DKNLTK2M5F');
</script>
"""

root = Path('.')
updated = []
for path in root.rglob('*.html'):
    text = path.read_text(encoding='utf-8')
    if 'G-DKNLTK2M5F' in text:
        continue
    if '</head>' not in text:
        print(f'SKIP no </head> in {path}')
        continue
    new_text = text.replace('</head>', snippet + '</head>', 1)
    path.write_text(new_text, encoding='utf-8')
    updated.append(str(path))
print(f'UPDATED {len(updated)} files')
for p in updated:
    print(p)
