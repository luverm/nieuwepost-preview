"""Bouwt index.html (de GitHub Pages-preview) uit backup/original.html + de blokken in bron/.

Gebruik: python3 tools/build_preview.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
P = 'https://luverm.github.io/nieuwepost-preview/'

src = (ROOT / 'backup/original.html').read_text(encoding='utf-8')
sec = (ROOT / 'bron/intro-slide-sectie.html').read_text(encoding='utf-8').rstrip('\n')
extras = (ROOT / 'bron/site-extras.html').read_text(encoding='utf-8')

# 1. Rode vlak vervangen door de inschuivende panelen
start = src.index('<section class="introduction-text')
end = src.index('</section>', start) + len('</section>')
s = src[:start] + sec + src[end:]

# 2. Tracking eruit, zodat bezoeken aan de preview niet meetellen bij de klant
s = re.sub(r'\s*<!-- Google Tag Manager -->.*?<!-- End Google Tag Manager -->', '', s, flags=re.S)
s = re.sub(r'\s*<!-- Google Tag Manager \(noscript\) -->.*?<!-- End Google Tag Manager \(noscript\) -->', '', s, flags=re.S)
s = re.sub(r'\s*<script type="text/plain" data-cli-class="cli-blocker-script"[^>]*></script>', '', s)

# 3. Zelfde bundle-versie als de dev-site
s = s.replace('bundle.js?v=1.21', 'bundle.js?v=1.23')

# 4. Saira Condensed (OFL) lokaal
font_css = f'''
    <!-- Alleen voor deze preview: Saira Condensed (OFL) lokaal, omdat de dev-site zijn fonts niet aan andere domeinen geeft -->
    <style>
        @font-face {{ font-family: SairaCondensed; src: url("{P}fonts/saira-condensed-latin-300-normal.woff2") format("woff2"); font-weight: 300; font-style: normal; font-display: swap; }}
        @font-face {{ font-family: SairaCondensed; src: url("{P}fonts/saira-condensed-latin-ext-300-normal.woff2") format("woff2"); font-weight: 300; font-style: normal; font-display: swap; unicode-range: U+0100-024F, U+1E00-1EFF; }}
    </style>
'''
s = s.replace('</head>', font_css + '</head>', 1)

# 5. Scroll-extra's + vervangende fonts vlak voor de afsluitende body-tag
extras = extras.replace('<script src="/assets/components/theme/templates/js/lenis.min.js"></script>',
                        f'<script src="{P}lenis.min.js"></script>')
fonts_js = f'''
<!-- Alleen voor deze preview: vervangende fonts, omdat de dev-site zijn fonts niet aan andere domeinen geeft.
     Koppen: Young Serif (OFL) in plaats van Or Lemmen. Icoontjes: Font Awesome Free in plaats van Pro.
     Op de echte site is dit niet nodig. -->
<script>
    (function () {{
        if (!('FontFace' in window)) return;
        var P = '{P}fonts/';
        [
            ['OrLemmen', 'young-serif-latin-400-normal.woff2', '700'],
            ['OrLemmen', 'young-serif-latin-ext-400-normal.woff2', '700', 'U+0100-024F, U+1E00-1EFF'],
            ['Font Awesome 6 Pro', 'fa-solid-900.woff2', '900'],
            ['Font Awesome 6 Brands', 'fa-brands-400.woff2', '400']
        ].forEach(function (f) {{
            var opts = {{ weight: f[2], style: 'normal', display: 'swap' }};
            if (f[3]) opts.unicodeRange = f[3];
            var face = new FontFace(f[0], 'url(' + P + f[1] + ') format("woff2")', opts);
            document.fonts.add(face);
            face.load().catch(function () {{}});
        }});
    }})();
</script>
'''
k = s.rindex('</body>')
s = s[:k] + extras + fonts_js + '\n' + s[k:]

(ROOT / 'index.html').write_text(s, encoding='utf-8')
print('index.html gebouwd')
