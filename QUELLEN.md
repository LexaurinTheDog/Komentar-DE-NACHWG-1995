# Quellenkarten und Rechercheprotokoll

## Gesetz

- Quelle: https://www.gesetze-im-internet.de/nachwg/xml.zip
- Abrufdatum: 19.10.2026; genauer UTC-Zeitpunkt und Antwort-Header in [verification.json](sources/verification.json).
- Konsolidierungsstand: Zuletzt geändert durch Art. 50 G v. 23.10.2024 I Nr. 323.
- Original: [ZIP](sources/official.zip), [XML](sources/official.xml), [kanonische Extraktion](sources/canonical.md).
- SHA-256: XML `5892f4d805acad3095889b7d49ba2bfe982886366bbdfc8f6f84410c4c229ac6`.
- Bestehender Katalogtext: `/Volumes/LaCie/law-intake/eu/de/gesetze/gii-nachwg.md`; unverändert belassen.

## Tatsächliche Recherche

Am 19.10.2026 wurde mit Firecrawl die Abfrage `site.bundesarbeitsgericht.de Nachweisgesetz Schadensersatz Ausschlussfrist 8 AZR 105/10` ausgeführt. Die originale Antwort steht in [search.json](sources/search.json). Danach wurden die folgenden amtlichen BAG-Volltexte abgerufen und in HTML sowie Text gesichert. Trefferbeschreibungen allein wurden nicht zur Begründung verwendet. Die Suche ist thematisch begrenzt; nicht belegte Abwesenheit von Entscheidungen wird nicht behauptet. Für die übrigen Paragraphen wurde keine gesonderte umfassende Einzelnormsuche durchgeführt. Dort enthält diese Ausgabe keine eigenständige Rechtsprechungsautorität.

### BAG, 22.09.2022 – 8 AZR 4/21

- Amtlicher Volltext: https://www.bundesarbeitsgericht.de/entscheidung/8-azr-4-21/
- Zuordnung: § 2; Aussage: Schadensersatz wegen Nachweisverzugs nach alter Fassung; Kausalität und Grenzen der Vermutung aufklärungsgemäßen Verhaltens; Rn. 17 ff..
- Beleg: [HTML](sources/8-azr-4-21.html), [Text](sources/8-azr-4-21.txt), [Abruf und SHA-256](sources/8-azr-4-21.json).
- Grenze: fallbezogene Aussage; kein Beleg für sämtliche Voraussetzungen heutiger oder abweichender Sachverhalte.


## Unabhängige Nachprüfung am 19.10.2026

Die ursprünglichen Abrufzeitpunkte bleiben unverändert. [Neue tatsächliche Abrufe einschließlich HTTP-Ergebnis, Zeit und Hash](sources/second-pass-verification.json) bestätigen die unveränderte amtliche XML-Fassung. [Katalogabgleich](sources/review-intake-comparison.json). Eine XML-Buildzeit wird nicht als alleiniger Beweis der Wirksamkeit jedes historischen Rechtsstands behandelt.

Die sauberen BAG-Textlesefassungen wurden aus dem unveränderten Original-HTML neu erzeugt; das HTML ist die maßgebliche archivierte Antwort. Die Nachprüfung hat die drei verwendeten Entscheidungen überprüft, keine vollständige neue Einzelnormrecherche ausgeführt.

BAG 8 AZR 4/21: Rn. 17–19 zu Nachweisverzug, Grundvermutung und nötigem Kausalitätsvortrag; Rn. 20–22 zur fehlenden Anspruchskenntnis und zum konkreten Verhalten. Altfassung bis 31.07.2022; keine Aussage zur Textformreform.

Zusätzlich amtlich geprüft: [§ 10 OWiG](https://www.gesetze-im-internet.de/owig_1968/__10.html), [Original](sources/review-owig-10.html), [HTTP-Abruf und Hash](sources/review-owig-10.json). § 4 NachwG bedroht Fahrlässigkeit nicht ausdrücklich mit Geldbuße.

[Amtlicher Vorspann einschließlich allgemeiner Hinweise](sources/amtlicher-vorspann.txt); maschinell aus dem ersten XML-Normknoten gewonnen.
