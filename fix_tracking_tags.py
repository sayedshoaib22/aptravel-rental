import glob
import re
from pathlib import Path

files = sorted(glob.glob('**/*.html', recursive=True))
updated = []

# Remove the stray onclick text that was accidentally inserted after an opening tag.
stray_pattern = re.compile(r'(?<=>)\s*onclick=("|\')(?:return gtag_report_conversion\([^\)]*\))\1>', re.S)

# Add tracking to anchors that still need it based on their href/target.
opening_pattern = re.compile(r'(<(?:a|button)\b[^>]*?)(/?>)', re.I)

for file in files:
    text = Path(file).read_text(encoding='utf-8')
    text = stray_pattern.sub('', text)

    def add_tracking(m):
        opening_tag = m.group(1)
        closing = m.group(2)
        if 'onclick=' in opening_tag.lower():
            return m.group(0)

        href_match = re.search(r'\bhref=("|\')(.*?)\1', opening_tag, re.I)
        if not href_match:
            return m.group(0)

        href = href_match.group(2)
        target_match = re.search(r'\btarget=("|\')(_blank)\1', opening_tag, re.I)
        target = target_match.group(2) if target_match else None
        if target:
            onclick = f' onclick="return gtag_report_conversion(\'{href}\', \'{target}\')"'
        else:
            onclick = f' onclick="return gtag_report_conversion(\'{href}\')"'
        return f'{opening_tag}{onclick}{closing}'

    new_text = opening_pattern.sub(add_tracking, text)
    if new_text != text:
        Path(file).write_text(new_text, encoding='utf-8')
        updated.append(file)

print('updated_files', len(updated))
for path in updated:
    print(path)
