# Tag 9: Multiplexer, Decoder und Prioritätsencoder

Lerntag 9 / W02 T3 aus dem Jahresplan. Literatur: Harris & Harris, *Digital Design and Computer Architecture, RISC-V Edition*, Kapitel 2.8, Buchseiten 81–86 (PDF 105–110). Der Prioritätsencoder wird ergänzend anhand des Themas aus Aufgabe 2.36 erklärt, Buchseiten 100–101 (PDF 124–125).

## Python gehört dazu

Aktualisierung: Die Aussagen „kein Python-Code nötig“ bzw. „keine Python-Pflichtaufgabe“ in den vorhandenen PDFs sind durch deinen neuen Wunsch überholt. Nutze ergänzend [bausteine.py](praxis/bausteine.py). Die PDFs bleiben mit möglichen eigenen Anmerkungen erhalten.

Beginne nur mit `mux2`: Sage die Ausgabe voraus, ändere die Eingaben und führe die Datei aus. Danach lies `mux4`, anschließend Decoder und Encoder. Die Tests stehen getrennt in `pruefe_modelle`; du musst nicht alle Syntax auf einmal beherrschen.

Im Praxisordner starten:

```sh
python3 bausteine.py
```

Die Datei prüft Python-Modelle vollständig. Sie liest keine Simulator-Schaltungen ein. Vergleiche deren Wahrheitstabellen zusätzlich mit den Python-Ergebnissen; die CSV-Dateien bleiben als optionale Tabellen erhalten.

## Materialien

- [Zusammenfassung](zusammenfassungen/Tag09_Zusammenfassung.pdf): sieben Seiten mit Beispielen, Gleichungen, Tabellen und eigenen Schaltbildern.
- `aufgaben/Tag09_Aufgaben.pdf` (lokal): sechs Seiten mit Handaufgaben, geführtem Schaltungsbau und Prüfübersicht.
- [Schaltungsablage](praxis/schaltungen/README.md): Namen und Anschlusskonventionen für deine eigenen Designs.
- [Solltabellen](praxis/pruefdaten/README.md): erwartete Werte zum Vergleich mit deinen Schaltungen.
- [auswertung.md](auswertung.md): noch leere englische Reflexionsvorlage.
- `quellen/` (lokal): bearbeitbare LaTeX-Dateien.

## Reihenfolge

1. Zusammenfassung Seiten 1–2 und Aufgabe 1: 2:1-MUX verstehen.
2. Seite 3 und Aufgabe 2: 4:1-MUX aus Gattern bauen.
3. Seite 5 und Aufgabe 3: 3:8-Decoder bauen.
4. Seiten 6–7 und Aufgabe 4: 8:3-Prioritätsencoder in zwei Stufen bauen.
5. Seite 4 und Aufgabe 5: Majority3 mit einem 8:1-MUX umsetzen.
6. Alle geforderten Zeilen prüfen und die Auswertung ergänzen.

Der Kalender plant zwei Stunden. Das ist eine Orientierung, keine Zusage für die Verdrahtungsdauer. Arbeite in diesen Blöcken; halte fest, was geprüft ist und was noch offen ist. Die Handaufgaben und Schaltungen sind der Tagesinhalt. Python gehört auf deinen Wunsch wieder zur Übung: kurze Modelle und Tests passend zu den jeweiligen Bausteinen.

Die eigene QM-Lernversion von Tag 8, insbesondere `combine` und `covers`, sowie die Wiederholung von Quine–McCluskey bleiben für Samstag vorgemerkt. Fertiger Referenzcode zählt nicht als eigene Implementierung.

## Konventionen

- Alle Datenleitungen sind 1 Bit breit; alle Ein- und Ausgänge sind aktiv HIGH.
- MUX: `S1` bzw. `S2` ist das höchstwertige Auswahlbit, `S0` das niedrigste.
- Decoder: Adresse `A2 A1 A0`, Ausgangsreihenfolge `Y7` bis `Y0`, kein Enable.
- Encoder: `I7` hat höchste Priorität; Ausgabe `Q2 Q1 Q0`, zusätzlich `NONE`. Bei keinem aktiven Eingang gilt `Q=000, NONE=1`.
- Mehrfach dargestellte Eingangssignale bedeuten dieselbe verzweigte Leitung, keine unabhängigen Pins.

## Abschluss

Vier eigene Hauptschaltungen sind gespeichert: 4:1-MUX, 3:8-Decoder, 8:3-Prioritätsencoder und Majority3 mit 8:1-MUX. Prüfe jeweils 64, 8, 256 und 8 Eingabezeilen. Die bereitgestellten CSV-Dateien enthalten Sollwerte, keine bereits durchgeführten Prüfungen deiner Schaltungen.

## PDFs neu erstellen

Im Tag-9-Ordner, nach Sicherung eigener PDF-Anmerkungen:

```sh
tectonic --outdir zusammenfassungen quellen/Tag09_Zusammenfassung.tex
tectonic --outdir aufgaben quellen/Tag09_Aufgaben.tex
```

Aufgabenblatt und LaTeX-Quellen bleiben wie bisher lokal und sind von Git ausgeschlossen.
