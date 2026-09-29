# Tag 10: Zeitverhalten, Glitches und Hazards

**Status: vorbereitet, noch nicht bearbeitet. Tag 9 bleibt offen.**

Grundlage: Harris & Harris, *Digital Design and Computer Architecture, RISC-V Edition*, Kapitel 2.9, Buchseiten 86–93 (PDF 110–117). Der aktuelle Jahresplan verlangt einen sichtbaren Glitch und seine Beseitigung durch einen zusätzlichen redundanten Implikanten.

## Unterlagen

- [Zusammenfassung](zusammenfassungen/Tag10_Zusammenfassung.pdf): sechs Seiten mit Delay-Begriffen, Pfaden, K-Map, Python-Erklärung und tatsächlichen Referenzwellenformen.
- `aufgaben/Tag10_Aufgaben.pdf` (lokal): fünf Seiten mit Handrechnungen, kleinen Python-Übungen und eigenem ngspice-Lauf.
- [Einfaches Python-Zeitmodell](praxis/timing_einfach.py): feste Transportverzögerungen, deutsche Kommentare.
- [ngspice-Lehrschaltung](praxis/hazard_rc.cir): unkorrigierter und korrigierter Ausgang in einem Versuch.
- [Python-Plotprogramm](praxis/plot_verlauf.py): erzeugt schwarz-weiße PNGs aus beiden Datenquellen.
- [Ergebnisse und Herkunft](praxis/results/README.md): vorbereitende Referenzläufe, keine erledigten Nutzeraufgaben.
- [auswertung.md](auswertung.md): englische Vorlage mit offenen Prüfungen.

## Lernreihenfolge

1. Zusammenfassung Seiten 1–2 und Aufgaben 1–2: Zeitgrenzen und Pfade.
2. Seiten 3–4 und Aufgaben 3–4: Glitch vorhersagen, K-Map und Zusatzterm.
3. Seite 5 und Aufgabe 5: Python schrittweise lesen, ausführen und ändern.
4. Seite 6 und Aufgabe 6: eigener ngspice-Lauf, Wellenform und Auswertung.

Ein kompletter selbst geschriebener Simulator ist nicht verlangt. Python gehört dazu: zuerst die drei einfachen Logikfunktionen, dann `frueher`, danach die zeitliche Schleife. Das Plotprogramm ist ein Hilfsmittel; seine Bibliotheksdetails musst du heute nicht auswendig können.

## Starten

Öffne ein Terminal im Tagesordner. Für die Logiksimulation reicht Python ohne Zusatzpakete. Zum Zeichnen brauchst du matplotlib. Eine lokale Umgebung hält das getrennt von anderen Lerntagen:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install matplotlib
cd praxis
python timing_einfach.py
ngspice -b -o results/spice_run.log hazard_rc.cir
python plot_verlauf.py
```

Die ersten drei Befehle zur Einrichtung sind nur einmal nötig; später genügt das Aktivieren der Umgebung. ngspice muss installiert sein. Die Netzliste erwartet, dass du dich im Praxisordner befindest und `results/` existiert.

Vor Änderungen vorhandene Ergebnisse sichern: Wiederholte Läufe überschreiben Dateien gleichen Namens. Für eigene Varianten kannst du eine Kopie des Praxisordners anlegen. Die mitgelieferten Diagramme stehen außerdem in der Zusammenfassungs-PDF.

## Modellannahmen

- `Y = A*B + !A*C`; korrigiert mit dem Zusatz `B*C`.
- Nur A fällt; B und C bleiben 1. Der Anfangszustand ist bereits eingeschwungen.
- Python: 1 ns pro Listeneintrag, NOT/AND/OR standardmäßig 3/2/1 ns, feste Transportverzögerung. Bei t=20 fällt A; Y ist im Intervall [23,26) ns LOW.
- SPICE: Verhaltensquellen mit RC-Flanken, 0/1-V-Pegel und 0,5-V-Schwelle. Das ist **keine CMOS-Transistornetzliste**. Die Ergebnisse sind nicht mit physikalisch charakterisierten Gate-Delays gleichzusetzen.
- Die beiden Modelle zeigen denselben Mechanismus, ihre Impulsbreiten müssen nicht übereinstimmen.
- Die Zusatzgruppe behandelt den statischen 1-Hazard beim einzelnen Eingangswechsel. Keine allgemeine Garantie bei beliebigen gleichzeitig wechselnden Eingängen.

## PDFs erneut erzeugen

Im Tagesordner, nach Sicherung eigener PDF-Anmerkungen:

```sh
tectonic --outdir zusammenfassungen quellen/Tag10_Zusammenfassung.tex
tectonic --outdir aufgaben quellen/Tag10_Aufgaben.tex
```

Die Diagramme müssen zuvor in `praxis/results/` erzeugt worden sein. Aufgaben-PDF und LaTeX-Quellen bleiben entsprechend deiner Git-Regel lokal.
