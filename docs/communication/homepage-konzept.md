# Homepage-Konzept – pysv.org

Konzept zur Überarbeitung der Startseite des Python Software Verband e.V.
Quelle der Texte: `content/contents.lr` (DE) / `content/contents+en.lr` (EN).
Template: `templates/page.html` (rendert Hero → Blog-USPs per Skript → Details).

---

## 1. Diagnose des Status quo

Was die aktuelle Homepage tut:

- Hero erklärt die Vereinsstruktur (Zusammenschluss, Beiträge, Förderprogramm) — also das *Wie*, nicht das *Warum*.
- Zwischen Hero und Details werden per Lektor-Query Blog-Teaser eingespielt (`highlighted` zuerst, dann der Rest) — das ist der visuell stärkste Bereich, aber er erzählt keine Verbandsgeschichte, sondern listet Konferenzen.
- Die „Aufgaben"-Sektion ist ein Zweizeiler.
- Keine Sektion adressiert Sponsoren, andere Verbände oder politische Akteure direkt.
- Begriffe wie *KI*, *Open Source*, *Forschung*, *Ökosystem*, *Diversität*, *Community-Kultur* tauchen nicht auf.
- PyCon DE wird zwar als Blog-USP angeteasert, aber nicht inhaltlich positioniert als das, was sie ist.

Konsequenz: Ein Sponsor, ein Verband oder ein politischer Akteur, der hier landet, bekommt einen organisatorischen Vereinsabriss. Was wir tun, wofür wir stehen, und warum man uns ernst nehmen sollte, fehlt.

---

## 2. Strategische Positionierung (das Dach über allem)

Vier Botschaften, die auf jeder Section spürbar sein müssen:

1. **Wir tragen die Leitkonferenz für angewandte KI mit Open Source im deutschsprachigen Raum.**
   PyCon DE & PyData wird konsequent in genau diesen Worten geframed — nicht als „Python-Konferenz", sondern als der Ort, an dem KI mit offenen Werkzeugen praktisch wird. Das ist unsere stärkste politische, mediale und wirtschaftliche Karte.
2. **Wir tragen die führende Konferenz für wissenschaftliches Python in Europa mit.**
   EuroSciPy ist der Schwerpunkt Forschung & Wissenschaft — von Klimamodellen über Astrophysik bis zu Biomedizin. Wir sind Mit-Träger, Sponsor und Teil des Programmkomitees. Das ergänzt die PyCon DE & PyData, statt sie zu doppeln.
3. **Python ist das gemeinsame Werkzeug von Forschung, Industrie und Verwaltung.**
   Vom CERN-Datensatz über die Bilanzpipeline der Mittelständler bis zur Klima-Simulation der Behörde — Python ist die Brücke. Cross-Pollination zwischen Domänen ist kein Nebeneffekt, sondern unser Kerngeschäft.
4. **Wir sind ein seriöser Träger mit einer ungewöhnlich offenen, hilfsbereiten Kultur — und alles davon ist ehrenamtlich getragen.**
   Eingetragener Verein, gemeinnützig, mit Sitz in Heidelberg, Förderprogramm, Mitgliederversammlung, Vorstand — und gleichzeitig die Community, in der Junior-Entwickler:innen mit CTOs am Sprint-Tisch sitzen. Die Programmkomitees, das Orga-Team der PyCon DE, die Barcamp-Veranstalter:innen, der Vorstand — alle arbeiten ehrenamtlich. Das ist nicht selbstverständlich. Es ist die Grundlage von allem, was wir tun.

Diese vier Aussagen sind das Fundament. Jede Section dient mindestens einer davon.

---

## 3. Stakeholder-Mapping

Die Homepage hat vier gleichzeitige Leser:innen. Statt sie zu trennen (eigene Landingpages), bedienen wir sie über *Sektionen*, die jeweils eine Person stärker abholen, ohne die anderen zu verlieren.

### A. Community-Mitglied
- *Kommt von:* Konferenz, Meetup, Empfehlung.
- *Sucht:* „Was machen die eigentlich neben der PyCon DE? Sollte ich Mitglied werden? Kann ich Förderung bekommen?"
- *Sprache:* Du-nah, konkret, beispielbasiert. Wir benennen die Dinge, die in der Community zählen: Sprints, Meetups, Reisekosten, Diversity-Tickets, User Groups.
- *Proof Points:* Geförderte Projekte mit Namen (Django Girls, Jugend Hackt, PyData BBQ …), Förderprogramm-Zahl (~15.000 €/Jahr), Mitgliederversammlung.
- *Primary CTA:* „Mitglied werden" / „Förderung beantragen".

### B. Sponsor
- *Kommt von:* PyCon-DE-Sponsoring-Pitch, LinkedIn, Recruiting-Recherche.
- *Sucht:* „Wer ist der Träger? Ist das ein professioneller Counterpart? Reichweite? Gemeinnützig?"
- *Sprache:* Sachlich, faktenstark, mit Zahlen. Reichweite, Audience-Profil, Wiedererkennung im Markt.
- *Proof Points:* Anzahl Teilnehmende PyCon DE & PyData, Programmpunkte, Tracks (KI, Data, Open Source), e.V. & gemeinnützig, Standorte/Historie.
- *Primary CTA:* „PyCon-DE-Sponsoring" / „Kontakt für Partnerschaften".

### C. Andere Verbände / Institutionen
- *Kommt von:* Recherche zu Open-Source-Vertretung in DE, KI-Diskurs, Bildungspolitik.
- *Sucht:* „Wer spricht für die deutschsprachige Python-Community? Mit wem können wir gemeinsame Sache machen?"
- *Sprache:* Institutionell, mit klarer Selbstverortung. Wir sind *die* Stimme des deutschsprachigen Python-Ökosystems.
- *Proof Points:* e.V., Satzung, Vorstand, Sitz Heidelberg, jährliche Mitgliederversammlung, EuroSciPy-Mitorganisation, internationale Vernetzung (EuroPython, PSF).
- *Primary CTA:* „Kontakt für Kooperationen" / Vorstand erreichbar.

### D. Politik / politische Akteur:innen
- *Kommt von:* Anhörung, Briefing, Verbändekonsultation, KI-/Digital-/Bildungsthemen.
- *Sucht:* „Ist das ein anschlussfähiger Gesprächspartner zu Open Source, KI-Souveränität, Digitalbildung?"
- *Sprache:* Politik-Anschluss-Vokabular ohne Lobby-Sprech. Begriffe wie *digitale Souveränität*, *Open-Source-Resilienz*, *MINT-Bildung*, *Fachkräfte*, *Forschungstransfer*.
- *Proof Points:* Python in Forschung & Verwaltung (BfS, DWD, DLR, RKI, statistische Ämter — beispielhaft nennen, falls belegbar), gemeinnützig, neutraler Träger, jährliche Konferenz mit X Teilnehmenden, Förderung von Nachwuchs.
- *Primary CTA:* „Kontakt für politische Gesprächspartner:innen" / Positionspapiere/Pressekontakt.

---

## 4. Seitenarchitektur (Section-Reihenfolge)

Bestehende Render-Reihenfolge: **Hero → Blog-USPs (Skript) → Details.**
Neue Reihenfolge (alle Sections auf einer Seite, modular nach unten gestapelt):

```
1. Hero — Mission in einem Satz + zwei Sätze + zwei CTAs
2. Stakeholder-Doors — vier Mini-Kacheln (Community / Sponsoren / Verbände / Politik)
3. Featured-Blogs (Skript, bestehend) — PyCon DE 2027 + MV 2025 + EuroSciPy + PyCon DE 2026
4. Unsere Konferenzen & Barcamps — drei Formate: PyCon DE & PyData (angewandte KI/Open Source), EuroSciPy (Wissenschaft), Barcamps (Community-getragen)
5. Ehrenamtlich getragen — eigener Akzent zur Trägerschaft (Programmkomitees, Orga, Vorstand)
6. Was wir fördern — Förderprogramm in Klartext + Beispiele
7. Das Python-Ökosystem — Forschung bis Business, Cross-Pollination, Werkzeuglandschaft
8. Community-Kultur — offen, divers, hilfsbereit, professionell
9. Der Verband in Zahlen — Proof-Strip (Jahre aktiv, geförderte Projekte, Konferenz-Reichweite, Mitglieder, Ehrenamtsstunden)
10. Mitmachen — drei klare Pfade (Mitglied / Sponsor / Förderung beantragen) + Kontakt
```

Wichtig: Die Featured-Blogs (3) bleiben dort, wo sie heute sind — sie sind der erste „Beweis", dass etwas passiert. Alle Sections danach sind statische `details`-Inhalte (bzw. — siehe Abschnitt 7 — neue Modellfelder, falls wir das sauber bauen wollen).

---

## 5. Textkonzept pro Section (DE, Vorschlag)

Jede Section: **Zweck → Headline → Body → CTA → visueller Anker.**

### 5.1 Hero

- *Zweck:* In drei Sekunden klar machen, wer wir sind und wofür wir stehen. Mission > Vereinsstruktur.
- *Headline (H1):* **Python Software Verband**
- *Sub-Headline:* *Die Stimme der deutschsprachigen Python-Community — von Forschung bis Industrie, von Open Source bis angewandter KI.*
- *Body (2–3 Sätze):*
  > Wir fördern Python und Open Source im deutschsprachigen Raum — als gemeinnütziger Verein, als Träger der PyCon DE & PyData (Deutschlands führende Konferenz für angewandte KI mit Open Source), als Mit-Träger der EuroSciPy (Europas zentrale Konferenz für wissenschaftliches Python) und als Förderer der Barcamps, Meetups und Sprints der Community. All das wird ehrenamtlich getragen: von Programmkomitees, Orga-Teams und einem gewählten Vorstand. Hinter dem Verband steht eine Community, die ungewöhnlich offen, divers und hilfsbereit ist — und ein Ökosystem, das in fast jeder Branche und jeder Forschungsdisziplin zuhause ist.
- *CTAs:* `Mitglied werden` (primär) · `Förderung beantragen` (sekundär) · `Sponsoring & Partner` (tertiär, dezenter Link)
- *Visueller Anker:* Großes, ruhiges Headerbild — kein Stock-Code. Empfehlung: Foto aus der PyCon DE (gefüllter Saal von hinten, oder Sprint-Tisch). Alternativ ein vektorisiertes Motiv aus dem Logo-Farbraum (`--primary-color: #400811`, `--highlight-color: #FA4233`).

### 5.2 Stakeholder-Doors (neu)

- *Zweck:* Jede:r der vier Personas erkennt sich in der ersten Bildschirmhöhe. „Ich bin gemeint."
- *Headline (H2):* **Sie kommen aus …**
- *Mini-Kacheln (je 1 Zeile + Link):*
  - **… der Community.** Meetups, Sprints, Förderung für eure Events. → *Was wir fördern*
  - **… einem Unternehmen.** Sponsoring der PyCon DE, Mitgliedschaft, Recruiting-Reichweite. → *Für Sponsoren*
  - **… einem Verband oder einer Institution.** Kooperationen rund um Open Source und Digitalisierung. → *Kontakt Vorstand*
  - **… der Politik oder Verwaltung.** Open Source als Standortfaktor, KI-Souveränität, MINT-Bildung. → *Pressekontakt & Positionen*
- *Visueller Anker:* Vier gleich große Karten, je ein Icon (Sprechblase / Handshake / Säulen / Bundesadler-frei: stilisiertes Gebäude). Kein Foto — bewusst nüchtern.

### 5.3 Featured-Blogs *(bleibt wie aktuell, Skript-gerendert)*

- *Zweck:* Aktualität, Beweis, dass etwas passiert.
- Keine Textänderung nötig — die Blog-Teaser sind solide. Hinweis: `teaser_text` in den jeweiligen Blog-Einträgen kuratieren, damit PyCon-DE-Einträge die KI-/Open-Source-Sprache verwenden (siehe 5.4).

### 5.4 Unsere Konferenzen & Barcamps (neu, eigene Sektion)

- *Zweck:* Die drei Formate, mit denen wir die Community jährlich zusammenbringen, sauber voneinander abgrenzen — und PyCon DE konsequent als KI-/Open-Source-Leitkonferenz, EuroSciPy als Wissenschafts-Anker, Barcamps als Community-Format positionieren.
- *Headline (H2):* **Unsere Konferenzen & Barcamps**
- *Lead (1 Absatz):*
  > Wir bringen die Python-Community in drei Formaten zusammen — vom Großevent mit mehreren tausend Teilnehmenden bis zum Wochenend-Barcamp mit 25 Leuten. Alle drei Formate werden ehrenamtlich getragen, vom Verband finanziert oder ko-finanziert und sind offen für die gesamte Community.

#### 5.4 a) PyCon DE & PyData — angewandte KI mit Open Source

- *Sub-Headline (H3):* **Deutschlands führende Konferenz für angewandte KI mit Open Source**
- *Body:*
  > Einmal im Jahr trifft sich die deutschsprachige Python-Community zu Deutschlands wichtigster Konferenz zur Anwendung von Künstlicher Intelligenz auf Basis von Open Source. Drei Konferenztage, ein Sprint- und Community-Tag, ein Masterclass-Tag. Hier kommen die Menschen zusammen, die KI nicht nur diskutieren, sondern bauen: ML-Engineers, Data Scientists, Forschende, CTOs, Studierende. Quer durch Branchen — von der DAX-Konzern-IT über Mittelstand und Verwaltung bis zur universitären Forschung. Die PyCon DE & PyData ist die einzige Veranstaltung dieser Größenordnung im deutschsprachigen Raum, die Open Source und angewandte KI konsequent zusammen denkt.
- *Fakt-Kacheln:*
  - **130+ Programmpunkte** je Edition
  - **Hauptthemen:** KI, Data, Open-Source-Tools, MLOps
  - **Reichweite:** mehrere tausend Teilnehmende pro Jahr (zuletzt Darmstadt 2026, als nächstes Heidelberg 2027)
- *CTA:* `Programm der nächsten Edition` (Link auf Blog-Eintrag PyCon DE 2027) · `Sponsoring-Möglichkeiten` (Mailto / Sponsoring-PDF)
- *Visueller Anker:* Foto aus dem Plenum.

#### 5.4 b) EuroSciPy — wissenschaftliches Python in Europa

- *Sub-Headline (H3):* **Europas zentrale Konferenz für wissenschaftliches Python — mitgetragen vom PySV**
- *Body:*
  > Die EuroSciPy ist die jährliche europäische Konferenz für Python in der Forschung und in den Wissenschaften. Klimamodelle, Astrophysik, Biomedizin, Geowissenschaften, numerische Simulation, Hochleistungsrechnen: Wo immer in Europa wissenschaftliche Daten mit Python verarbeitet werden, ist die EuroSciPy der jährliche Treffpunkt. Der Python Software Verband ist Mit-Träger der Konferenzreihe und Teil des Programmkomitees. Die nächste Edition findet 2026 in Krakau statt.
- *Fakt-Kacheln:*
  - **Schwerpunkt:** Forschung & Wissenschaft, NumPy/SciPy-Ökosystem
  - **Format:** 6 Tage, Talks · Workshops · Sprints
  - **Reichweite:** ~200 Teilnehmende, ~40 Speaker:innen, 16 Workshops (Edition 2026)
- *CTA:* `EuroSciPy 2026 — Krakau` (Link Blog-Eintrag).
- *Visueller Anker:* Foto Wissenschafts-Setting oder Konferenzbild Krakau.

#### 5.4 c) Barcamps — Community-getragen, niedrigschwellig, regional

- *Sub-Headline (H3):* **Barcamps & PythonCamps — wo Python-Begeisterung lokal stattfindet**
- *Body:*
  > Neben den großen Konferenzen leben wir das Barcamp-Format: kleinere, regionale Wochenend-Veranstaltungen, deren Programm von den Teilnehmenden selbst gestaltet wird. PythonCamp Köln, PythonCamp auf Rügen, Python BarCamp Karlsruhe, PyCamp Leipzig — überall im deutschsprachigen Raum. Wer auf einer PyCon DE überfordert ist, findet hier den einfachen Einstieg in die Community; wer schon mittendrin ist, findet hier die offenen Diskussionen abseits der großen Bühne.
  >
  > Diese Barcamps werden vollständig von Ehrenamtlichen organisiert. Der Verband finanziert sie mit, sorgt für Versicherungsschutz und sichtbares Sponsoring — die inhaltliche Hoheit liegt bei den Veranstalter:innen vor Ort.
- *Fakt-Kacheln:*
  - **Größenordnung:** 25–80 Teilnehmende je Camp
  - **Format:** offenes Sessions-Board, kein vorgegebenes Programm
  - **Frequenz:** mehrere Camps pro Jahr im deutschsprachigen Raum
- *CTA:* `Aktuelle Barcamps in den Events` (Link auf `/events`) · `Ein Barcamp anmelden / fördern lassen` (Link auf `/grants`).
- *Visueller Anker:* Foto-Mini-Galerie: Sessions-Board / Aussenshot / Gruppenfoto.

### 5.5 Ehrenamtlich getragen (neu, eigene kleine Sektion)

- *Zweck:* Diese Aussage darf nicht in einer Aufzählung versanden. Sie ist die Grundlage unserer Glaubwürdigkeit gegenüber Politik (Bürgerschaftlichkeit), Sponsoren (Mittel kommen an, nicht in Gehälter) und Verbänden (echte Community, kein Beratungsbüro).
- *Headline (H2):* **Alles ehrenamtlich getragen**
- *Body (kurz, 2 Absätze):*
  > Die PyCon DE & PyData, die EuroSciPy, die Barcamps, das Förderprogramm, der Vorstand — all das ist ehrenamtliche Arbeit. Mehrere hundert Menschen organisieren, kuratieren, reviewen Vorträge, schleppen Hardware, betreuen Helpdesks und beantworten E-Mails, ohne dafür bezahlt zu werden. Sponsoring- und Mitgliedsbeiträge fließen in Veranstaltungen, Förderung und Infrastruktur — nicht in Gehälter.
  >
  > Das ist kein Detail, das in einer Fußnote stehen sollte. Es ist der Grund, warum eine PyCon DE 30–50 % günstiger ist als vergleichbare kommerzielle KI-Konferenzen, warum der Förderbescheid in Wochen statt Monaten kommt und warum auf einer PyCon DE Junior-Entwickler:innen und CTOs am selben Tisch sitzen.
- *Visueller Anker:* Eine große Zahl: **„hunderte ehrenamtlich Aktive pro Jahr"** (Zahl mit Vorstand verifizieren) — oder eine Foto-Wand „Faces of PySV": Helfer:innen-T-Shirts, Orga-Team-Aufnahmen, Sprint-Mentor:innen. Ehrenamtlich heißt: Gesichter.

### 5.6 Was wir fördern (neu, ersetzt den heutigen „Aufgaben"-Zweizeiler)

- *Zweck:* Konkret machen, was *„fördern"* bedeutet, mit Beispielen, die Glaubwürdigkeit erzeugen.
- *Headline (H2):* **Was wir fördern**
- *Intro:*
  > Mit den Beiträgen unserer Mitglieder und den Erträgen unserer Konferenzen unterstützen wir die Python-Community im deutschsprachigen Raum — finanziell, organisatorisch und sichtbar.
- *Drei-Spalten-Block:*
  - **Konferenzen, Barcamps & Community-Events.** PyCon DE & PyData (Träger), EuroSciPy (Mit-Träger), PythonCamps und Barcamps in Köln, Rügen, Karlsruhe, Leipzig, Meetup-Reihen. Wir tragen, organisieren mit oder fördern pauschal — und übernehmen Versicherungsschutz für ehrenamtliche Veranstalter:innen.
  - **Open-Source-Entwicklung.** Sprints, konkrete Features, Wartungsarbeit an Bibliotheken — bis zu 800 € je Vorhaben.
  - **Bildung & Nachwuchs.** Django Girls, Jugend Hackt, Workshops, Diversity-Tickets. Niedrigschwellig, formloser Antrag.
- *Beispielzeile:* „Zuletzt gefördert: Django Girls Berlin · PyData BBQ Heidelberg · GeoPython Basel · Jugend Hackt · Zope-Sprint."
- *CTA:* `Förderung beantragen` (Mailto an grants@python-verband.org) · `Förderprogramm im Detail`
- *Visueller Anker:* Kennzahl groß: **„~15.000 € jährliches Förderbudget"** + Mini-Galerie aus 3–4 Event-Fotos.

### 5.7 Das Python-Ökosystem (neu)

- *Zweck:* Klarmachen, dass „Python" nicht eine Sprache unter vielen ist, sondern ein domänenübergreifendes Werkzeug-Ökosystem — Argument für Politik und Verbände.
- *Headline (H2):* **Ein Ökosystem, das Forschung, Industrie und Verwaltung verbindet**
- *Body:*
  > Python ist die meistgenutzte Programmiersprache der Welt — und im deutschsprachigen Raum die gemeinsame Sprache von Forschungsinstituten, Konzernen, Mittelstand, Behörden und Bildungseinrichtungen. Rund um Python existiert ein Ökosystem aus hunderttausenden Open-Source-Bibliotheken: NumPy, pandas, scikit-learn, PyTorch, FastAPI, Django, Jupyter — die Werkzeuge hinter moderner Datenarbeit, wissenschaftlichem Rechnen, Webdiensten und KI-Anwendungen.
  >
  > Genau deshalb funktioniert unsere Community so gut: Eine Klimaforscherin, eine Bank-Quant-Analystin und eine Backend-Entwicklerin arbeiten mit denselben Tools. Cross-Pollination zwischen Domänen ist kein Nebeneffekt — sie ist der Grund, warum Python-Wissen so schnell überall ankommt.
- *Visueller Anker:* Domain-Strip mit kleinen Etiketten: **Wissenschaft · Data Science · KI/ML · Web · DevOps · Bildung · Verwaltung · Finanzen · Bio/Med · Geo · Industrie**. Ggf. als horizontale Pille-Reihe in `--highlight-color-pale`.

### 5.8 Community-Kultur (neu)

- *Zweck:* Den weichen, aber entscheidenden Faktor erklären — und zugleich zugänglich wirken.
- *Headline (H2):* **Die Kultur hinter dem Verband**
- *Body (kurz, drei Absätze):*
  > **Hilfsbereit.** Wer das erste Mal auf einer PyCon DE ist, wird in der Mittagspause an einen Tisch eingeladen. Wer eine Bibliothek pflegt, bekommt auf der Mailingliste Antworten von den Maintainer:innen. Das ist keine Folklore — das ist eine bewusst gepflegte Kultur.
  >
  > **Offen und divers.** Wir leben einen [Code of Conduct](/coc), der nicht dekorativ ist. Wir fördern gezielt Initiativen wie Django Girls und Diversity-Tickets, weil eine breitere Community eine bessere Community ist — auch fachlich.
  >
  > **Professionell und ehrenamtlich.** Hinter dieser Offenheit steht harte Arbeit: gewählter Vorstand, jährliche Mitgliederversammlung, transparente Finanzen, eingetragener Verein — und mehrere hundert Ehrenamtliche, die Programmkomitees, Konferenz-Orga und Barcamp-Veranstaltungen tragen. Wir sind freundlich. Wir sind nicht naiv.
- *Visueller Anker:* Foto-Trio: Sprint-Tisch / Hauptsaal / Hallway-Track. Bildunterschriften mit echten Event-Namen.

### 5.9 Der Verband in Zahlen (neu, Proof-Strip)

- *Zweck:* Für Sponsoren, Verbände und Politik in einer Sekunde Seriosität & Größenordnung zeigen.
- *Format:* Horizontaler Strip, 5–7 große Zahlen mit kurzer Bezeichnung. Beispiele (Zahlen final mit Vorstand verifizieren):
  - **seit 200X** als e.V. aktiv
  - **~15.000 €** jährliches Förderbudget
  - **130+** Programmpunkte je PyCon DE
  - **mehrere tausend** Teilnehmende pro PyCon DE & PyData
  - **~200** Teilnehmende EuroSciPy / Jahr
  - **mehrere Barcamps** pro Jahr im deutschsprachigen Raum
  - **100 % ehrenamtlich** organisiert (Programmkomitees, Orga, Vorstand)
  - **gemeinnützig** anerkannt, Sitz Heidelberg
- *Visueller Anker:* Schlichter Zahlen-Strip in Verbandsfarben, keine Icons.

### 5.10 Mitmachen (CTA-Block, ersetzt das heutige „Mitglied werden" am Ende)

- *Zweck:* Drei klare Pfade, ein Kontakt-Anker.
- *Headline (H2):* **Mitmachen**
- *Drei Karten:*
  - **Mitglied werden.** Ab 60 € im Jahr (Einzelpersonen) bzw. 600 € (Unternehmen). Stimmrecht, Sichtbarkeit, aktive Förderung. → `/membership`
  - **PyCon DE sponsern.** Erreichen Sie die deutschsprachige KI- und Python-Community direkt. → Mailto Sponsoring + Sponsoring-Deck (PDF, falls vorhanden).
  - **Förderung beantragen.** Formlos per E-Mail, schnelle Vorstandsentscheidung. → `/grants`
- *Schluss-Zeile:*
  > Sie kommen aus Politik, Verwaltung oder einem anderen Verband? Wir freuen uns über Gespräche — Kontakt: [info@pysv.org](mailto:info@pysv.org).
- *Visueller Anker:* Drei gleichwertige Karten, primäre/sekundäre/tertiäre Hierarchie nur über Button-Farben.

---

## 6. Tonalität / Voice in 6 Regeln

1. **Klartext vor Fachjargon.** „KI", „Open Source", „Förderung" — nicht „kuratierte Ökosystem-Maßnahmen".
2. **„Wir" statt „Der Verband".** Persönlich, aber nicht anbiedernd.
3. **Konkret vor abstrakt.** Eine Zahl, ein Eigenname, ein Beispiel ist mehr wert als drei Adjektive.
4. **Höflich-direkt.** Wir sprechen Sponsoren und Politik in der Sie-Form an, die Community-Sektionen dürfen Du verwenden, wenn der Kontext es trägt — sonst Sie. Konsistenz pro Section.
5. **„Pythonista" ist erlaubt.** Identitäts-positiver Community-Begriff, kein Nerd-Jargon.
6. **Keine Phrasen.** Worte wie „leidenschaftlich", „passionate", „synergetisch", „state-of-the-art" streichen, bevor sie ins Wireframe kommen.

---

## 7. Umsetzung in der Codebase

Die heutige Architektur erlaubt nur **`hero`** + **`details`** als Markdown-Felder (siehe `models/page.ini`). Dazwischen werden Blog-USPs gerendert. Zwei Optionen:

### Option A — schnell, minimal-invasiv

Alles, was nach den Blog-USPs kommt, in `details` schreiben. Vorteil: keine Template-Änderung. Nachteil: alle Sektionen teilen sich denselben Markdown-Block, visuelle Hierarchie nur über H2/H3 und CSS.

→ Stakeholder-Doors (5.2) ginge per HTML in den `hero`-Markdown (Lektor erlaubt Roh-HTML).
→ PyCon-DE-Sektion, Förderung, Ökosystem, Kultur, Zahlen, CTAs als H2-Blöcke in `details`.

### Option B — sauber, mittelfristig

`models/page.ini` um neue, semantische Felder erweitern und im Template einzeln rendern:

```ini
[fields.stakeholder_doors]   ; HTML/Markdown — vier Personas
[fields.conferences_section] ; Markdown — Lead + drei Unterblöcke (PyCon, EuroSciPy, Barcamps)
[fields.volunteers_section]  ; Markdown — Ehrenamt-Akzent
[fields.grants_section]      ; Markdown
[fields.ecosystem_section]   ; Markdown
[fields.culture_section]     ; Markdown
[fields.numbers_strip]       ; flow oder repeated record — inkl. Ehrenamtsstat
[fields.cta_section]         ; Markdown
```

`templates/page.html` rendert sie nach dem Blog-USP-Block in der oben festgelegten Reihenfolge. Jedes Feld bekommt einen `<section class="…">` mit klarer CSS-Klasse, damit die visuellen Anker (Karten, Zahlen-Strip, Domain-Pillen) gezielt gestylt werden können.

**Empfehlung:** Option B. Sie zwingt zur sauberen Trennung, macht die Pflege durch Vorstand/Redaktion einfacher und erlaubt es, einzelne Sections auf der englischen Variante (`contents+en.lr`) zu spiegeln oder bewusst zu kürzen.

### CSS-Erweiterungen (kurz)

Wiederverwenden, was da ist (`--primary-color`, `--highlight-color`, USP-Karten-Layout). Zusätzlich nötig:

- `.stakeholder-doors` — 4-Karten-Grid, dezent.
- `.conferences-block` — Lead + drei Sub-Sektionen (`.conf-pycon`, `.conf-euroscipy`, `.conf-barcamps`) mit jeweils Fakt-Kacheln.
- `.volunteers-accent` — eigene, knappe Akzent-Sektion (z. B. mit großem Zitat / großer Zahl).
- `.ecosystem-domains` — Pillen-Reihe.
- `.numbers-strip` — horizontale Zahlen-Reihe, große Typo, inkl. Ehrenamt-Stat.
- `.cta-cards` — 3-Karten-Grid mit primär/sekundär/tertiär-Buttons.

### Englische Variante

`content/contents+en.lr` mit übersetzten Inhalten spiegeln. Politik-Sektion und Verbands-Kooperationen können auf EN kürzer ausfallen (Zielgruppe lebt überwiegend im deutschsprachigen Raum). PyCon-DE- und Ökosystem-Sektion vollständig übersetzen — sie sind die internationale Visitenkarte.

---

## 8. Was vor der Umsetzung noch zu klären ist

1. **Zahlen verifizieren** (Gründungsjahr, exakte Teilnehmenden-Zahlen letzte PyCon DE & PyData, EuroSciPy-Reichweite, Anzahl ehrenamtlich Aktiver pro Jahr, Förderbudget aktuell, Anzahl Mitglieder — Vorstand fragen). Siehe MV-Erinnerung: keine P&L-Zahlen, aber Reichweite/Förderbudget/Ehrenamtsstatistik sind ok.
   - **Barcamp-Inventar:** Liste der aktiven Barcamp-Reihen (Köln/Rügen/Karlsruhe/Leipzig — kommen weitere dazu?) abstimmen, damit die Sektion aktuell bleibt.
2. **Sponsoring-Asset:** Gibt es ein aktuelles Sponsoring-PDF, das wir verlinken können? Wenn nein → kurzes One-Pager-Folgeprojekt.
3. **Politik-Kontakt:** Soll `info@pysv.org` ausreichen oder eine eigene Adresse (z. B. `presse@pysv.org`)? Empfehlung: dedizierte Adresse.
4. **Logo-Strip (Sponsoren/Partner):** Mit welchen Sponsoring-Logos der letzten PyCon dürfen wir auf der Homepage werben (vertragliche Lage prüfen)?
5. **Foto-Material:** Brauchen wir freigegebene Fotos aus PyCon DE 2026 (Darmstadt) als visuelle Anker — wer im Verband hat Zugriff?

---

## 9. Empfohlene Reihenfolge der Umsetzung

1. **Texte final schreiben** (auf Basis dieses Konzepts, mit Vorstand abgestimmt).
2. **Option B implementieren:** Modell erweitern, Template anpassen, CSS-Klassen ergänzen.
3. **Bildmaterial einbinden** (Heldenbild, Foto-Trio, Sponsoring-Logo-Strip).
4. **EN-Variante spiegeln**, Politik-Section auf DE belassen oder bewusst englisch nachziehen.
5. **Review** mit je einer Person aus jeder Zielgruppe (Community / Sponsor / Verband / Politik) — bevor live.
