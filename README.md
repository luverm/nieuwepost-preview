# Nieuwe Post Vlissingen: preview aanpassingen homepage

Voorbeeldpagina met scroll- en animatie-aanpassingen voor de homepage van
[nieuwepostvlissingen.nl](https://development.nieuwepostvlissingen.nl/). Alleen bedoeld om te bekijken en te bespreken.
Afbeeldingen, stylesheet en scripts komen rechtstreeks van de dev-site; tracking (GTM, Facebook, Hotjar) is uit de preview gehaald.

## Bestanden

| Bestand | Wat |
|---|---|
| `index.html` | De homepage met alle aanpassingen (dit is wat GitHub Pages laat zien) |
| `bron/intro-slide-sectie.html` | Het blok onder de hero: fotopanelen schuiven van links en rechts over het rode vlak |
| `bron/site-extras.html` | Alle scroll-effecten in één blok, voor elke pagina |
| `lenis.min.js` | Lenis 1.3.29 (MIT) voor soepel scrollen |
| `fonts/` | Alleen voor de preview: open vervangers voor de fonts van de site (Young Serif, Saira Condensed, Font Awesome Free), met licenties |
| `backup/original.html` | De homepage zoals die was, als referentie |
| `tools/build_preview.py` | Bouwt `index.html` opnieuw uit de bestanden hierboven |

## Op de site zetten (MODX)

1. Upload `lenis.min.js` naar `/assets/components/theme/templates/js/lenis.min.js`.
2. Vervang op de homepage de sectie `introduction-text` door `bron/intro-slide-sectie.html`.
3. Plak `bron/site-extras.html` één keer vlak voor de afsluitende body-tag in de template.

## Wat zit er in site-extras

- Soepel scrollen (Lenis)
- Koppen die woord voor woord omhoog komen
- Foto's die binnen hun kader meebewegen, ook de hero
- Header die bij naar beneden scrollen verdwijnt en bij omhoog scrollen terugkomt, met kleiner logo
- Achtergrond die richting de footer naar bordeaux verloopt
- Rustiger inkomende blokken (bijgestelde AOS-animaties)
- Pijltje naar beneden in de hero en gele scrollbalk rechts

Bij "minder beweging" in de systeeminstellingen van de bezoeker staan de bewegende effecten uit.
