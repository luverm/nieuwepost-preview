# Overdracht: scroll- en animatie-aanpassingen homepage Nieuwe Post

Voor: Cees van Wageningen
Van: Lucas Vermaire
Datum: 27 november 2026

## In het kort

Voorstel voor een rustigere, soepelere homepage van nieuwepostvlissingen.nl, geïnspireerd op het scrollgedrag van rivarotterdam.nl en binnen de huisstijl van Nieuwe Post. Er is niets op de dev- of live-site aangepast; alles staat klaar om in MODX te zetten.

- Preview: https://luverm.github.io/nieuwepost-preview/
- Bestanden en versiegeschiedenis: https://github.com/luverm/nieuwepost-preview

## De bestanden

| Bestand | Wat het is | Waar het heen moet |
|---|---|---|
| `bron/site-extras.html` | Alle scroll-effecten in één blok (CSS + JS) | Eén keer vlak voor de afsluitende body-tag in de template |
| `bron/intro-slide-sectie.html` | Nieuw blok onder de hero: fotopanelen schuiven van links en rechts over het bordeaux vlak | Op de homepage, in plaats van de huidige sectie onder de hero |
| `lenis.min.js` | Lenis 1.3.29 (MIT) voor soepel scrollen | `/assets/components/theme/templates/js/lenis.min.js` |
| `backup/original.html` | De homepage zoals die op 27 november op de dev-site stond | Alleen ter referentie |

`index.html`, de map `fonts/` en `tools/` zijn alleen voor de GitHub-preview en hoeven niet op de site.

## Stappen in MODX

1. Upload `lenis.min.js` naar `/assets/components/theme/templates/js/`.
2. Plak de inhoud van `bron/site-extras.html` één keer vlak voor de afsluitende body-tag in de template. Het werkt dan op elke pagina.
3. Vervang op de homepage de sectie direct onder de hero door `bron/intro-slide-sectie.html`.
   Let op: op de dev-site staat daar inmiddels een `hero-blurred-text`-sectie met de kop "Nieuwe Post... historisch verankerd". Mijn blok gebruikt nog de oude kop "Wonen waar tijdloos design en erfgoed samenkomen". Kies welke kop het moet zijn en pas die aan in het blok.

## Wat er in site-extras zit

- **Soepel scrollen (Lenis):** lerp 0.085, ankerlinks werken mee.
- **Koppen woord voor woord:** geldt voor `h2.written-title` en de kop in `.big-image-section`. De eigen AOS-animatie van die koppen wordt uitgezet, anders dubbelt het effect.
- **Beeld-parallax:** de hero-foto en de foto's bij de woningtypes, updates, Café-blok en quote bewegen rustig mee binnen hun kader. Foto's bovenin een kaart (`card-img-top`) krijgen een eigen kader, zodat ze niet over de titel schuiven.
- **Header:** verdwijnt bij naar beneden scrollen, komt terug bij omhoog scrollen, met een kleiner logo. Blijft staan als het mobiele menu open is.
- **Rustiger AOS-animaties:** langer en zachter, met kleinere verschuivingen.
- **Footer statisch:** de eigen AOS-animatie van de footer staat uit.
- **Gele scrollbalk:** smalle okerkleurige balk rechts die volloopt met het scrollen.
- **Hero-fix:** `section.intro` krijgt `overflow: clip`, zodat de hero niet intern kan verschuiven. Zonder deze regel kon er een lege strook onder de hero-foto ontstaan.

Bezoekers die in hun systeem "minder beweging" hebben ingesteld, krijgen geen Lenis, geen parallax en geen woordanimatie.

## Huisstijl

Alles volgt de huisstijl van Nieuwe Post (voorstel "Historie" uit het huisstijlboek):

- Kleuren: bordeaux `#40000f`, mauve `#7a4f50`, lichtoranje `#fcb562`, oker `#cd841f`, zand `#f5e4d1`
- Letters: Or Lemmen voor koppen, Saira Light voor tekst
- Beeldelement: boogvormen

## Goed om te weten

- **Fonts in de preview:** de preview gebruikt Young Serif in plaats van Or Lemmen en Font Awesome Free in plaats van Pro. De dev-site staat niet toe dat github.io zijn fonts gebruikt, en de betaalde fonts mogen niet in een openbare repository. Op de echte site laden gewoon de echte fonts.
  Wil je de preview met de echte fonts zien, dan kan dat met één regel in de `.htaccess` van de dev-site:

  ```apache
  <FilesMatch "\.(otf|ttf|woff2?)$">
      Header set Access-Control-Allow-Origin "https://luverm.github.io"
  </FilesMatch>
  ```

- **Tracking:** in de preview zijn Google Tag Manager, Facebook en Hotjar weggehaald, zodat bezoeken niet meetellen. In de bestanden voor de site is daar niets aan veranderd.
- **Testen na plaatsen:** let vooral op de plattegrond (plotmap), de sliders (Swiper) en het mobiele menu in combinatie met Lenis. In de preview werkte dat goed, maar het is niet op de echte server getest.
- **Terugdraaien:** haal het blok uit de template en zet de oude sectie terug uit `backup/original.html`. In de GitHub-geschiedenis staat elke stap als losse commit.
