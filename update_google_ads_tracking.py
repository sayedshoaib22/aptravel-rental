from pathlib import Path
import re

root = Path('.')
files = sorted(root.glob('**/*.html'))

google_tag = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-18269844622"></script>
<script>
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'AW-18269844622');
</script>
"""

event_snippet = """<script>
function gtag_report_conversion(url, target) {
  var callback = function () {
    if (typeof(url) != 'undefined') {
      if (target === '_blank') {
        window.open(url, '_blank');
      } else {
        window.location = url;
      }
    }
  };
  gtag('event', 'conversion', {
    'send_to': 'AW-18269844622/MMeUCKL__8UcEI7p3odE',
    'event_callback': callback
  });
  return false;
}
</script>
"""

conversion_keywords = re.compile(r'\b(Book|Quote|Contact|Enquiry|Request|Plan|Rent|Hire|Get|Now)\b', re.I)

modified_files = []

for path in files:
    text = path.read_text(encoding='utf-8')
    original = text
    modified = False

    if 'gtag_report_conversion' not in text:
        match = re.search(r'(<script\b[^>]*>.*?gtag\(\'config\'\s*,\s*\'AW-18269844622\'\).*?</script>)', text, flags=re.S)
        if match:
            replacement = match.group(1) + '\n' + event_snippet
            text = text.replace(match.group(1), replacement, 1)
            modified = True
        elif '</head>' in text:
            text = text.replace('</head>', google_tag + '\n' + event_snippet + '</head>', 1)
            modified = True

    def add_callback(match):
        full = match.group(0)
        attrs_before = match.group(1)
        href = match.group(2)
        attrs_after = match.group(3) or ''
        if re.search(r'onclick\s*=\s*"', full, re.I):
            return full
        target_search = re.search(r'target\s*=\s*"([^"]*)"', attrs_before + attrs_after, re.I)
        target = target_search.group(1) if target_search else ''
        safe_url = href.replace('"', '&quot;')
        call = f"gtag_report_conversion('{safe_url}'"
        if target.lower() == '_blank':
            call += ", '_blank'"
        call += ")"
        return full[:-1] + f' onclick="return {call}"' + '>'

    text_new = re.sub(r'<a([^>]*?)\s+href="(tel:[^"]+)"([^>]*)>', add_callback, text, flags=re.I)
    if text_new != text:
        text = text_new
        modified = True

    text_new = re.sub(r'<a([^>]*?)\s+href="(https://wa\.me/[^"]+)"([^>]*)>', add_callback, text, flags=re.I)
    if text_new != text:
        text = text_new
        modified = True

    def add_contact_onclick(match):
        full = match.group(0)
        attrs_before = match.group(1)
        href = match.group(2)
        attrs_after = match.group(3) or ''
        inner = match.group(4)
        if re.search(r'onclick\s*=\s*"', full, re.I):
            return full
        if re.search(r'\b(btn|svc-link|topbar-btn|btn-nav-call)\b', attrs_before + attrs_after, re.I) or conversion_keywords.search(inner):
            call = f"gtag_report_conversion('{href}')"
            return full[:-1] + f' onclick="return {call}"' + '>'
        return full

    text_new = re.sub(r'<a([^>]*?)\s+href="(/contact/)"([^>]*?)>(.*?)</a>', add_contact_onclick, text, flags=re.I|re.S)
    if text_new != text:
        text = text_new
        modified = True

    if modified and text != original:
        path.write_text(text, encoding='utf-8')
        modified_files.append(str(path))

if modified_files:
    print('Modified files:')
    for f in modified_files:
        print(f)
else:
    print('No files modified.')
