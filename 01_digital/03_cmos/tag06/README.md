# Tag 6: Vom Transistor zum Gatter

Grundlage: aktueller Kalender W01 T6, DDCA RISC-V Edition 1.7–1.9,
Buchseiten 25–35. Der sechsstündige Kalenderblock enthält Wiederholung,
Puffer und Wochenabschluss; die Aufgaben dürfen auf mehrere Sitzungen verteilt werden.

1. [Tag06_Zusammenfassung.pdf](zusammenfassungen/Tag06_Zusammenfassung.pdf) lesen: Erklärung, Schalterbilder und ngspice-Anleitung.
2. `aufgaben/Tag06_Aufgaben.pdf` (lokal) bearbeiten. Die praktischen Aufgaben folgen auf die Papieraufgaben.
3. Inverter-Beispiel ausführen, dann NAND selbst aufbauen und alle vier Zustände prüfen.

Die LaTeX-Quellen liegen in `quellen/`.
`inverter_beispiel.cir` ist das erklärte Startbeispiel. Level-1-Modelle und
Spannungsgrenzen sind Lehrbeispiele, keine charakterisierte Fertigungstechnologie.

## Ausführen

Im Terminal zuerst in diesen Ordner wechseln:

```sh
cd "$HOME/Learning/Semiconductors : AI Hardware/ai-hardware-journey/01_digital/03_cmos/tag06"
ngspice -b inverter_beispiel.cir
```

Die vorhandene SPICE-Umgebung wurde mit der Plot-Hilfe geprüft. Du kannst sie direkt nutzen:

```sh
source "$HOME/.venvs/ai-hardware-spice/bin/activate"
python plot.py inverter
```

Alternativ kannst du eine eigene Umgebung außerhalb des Projektpfads anlegen
(der Doppelpunkt im Projektpfad stört das Anlegen einer venv darin):

```sh
python3 -m venv "$HOME/.venvs/ai-hardware-day06"
source "$HOME/.venvs/ai-hardware-day06/bin/activate"
python -m pip install -r requirements.txt
python plot.py inverter
```

Die aktuelle NAND-Datei heißt `Aufgabe6.cir`:

```sh
ngspice -b Aufgabe6.cir
python plot.py nand
```

Die Dateien entstehen im aktuellen Arbeitsordner. `wr_singlescale` und
`wr_vecnames` müssen in beiden Netzlisten gesetzt sein: Die Plot-Hilfe erwartet
eine Kopfzeile und eine gemeinsame Sweep-/Zeitspalte, danach die Spannungen.

## Erwartete Ergebnisse

- Inverter: `inverter_dc.txt`, `inverter_kennlinie.png`, abgelesene Schaltschwelle VM.
- NAND: `Aufgabe6.cir`, `nand2_tran.txt`, `nand2_zeitverlauf.png`, vier geprüfte Tabellenzeilen.
- `auswertung.md`: kurze Erklärung und offene Fragen.

Die Plot-Hilfe zeichnet den Schnittpunkt Vout=Vin ein. Prüfe selbst, warum dieser
Punkt die Schaltschwelle VM beschreibt und nicht die Transistor-Schwellspannung Vt.

## PDFs neu bauen

```sh
tectonic --outdir zusammenfassungen quellen/Tag06_Zusammenfassung.tex
tectonic --outdir aufgaben quellen/Tag06_Aufgaben.tex
```

## Neue Erklärung und neues Aufgabenblatt

- [Tag06_Aufgabe6_7_Detailliert.pdf](zusammenfassungen/Tag06_Aufgabe6_7_Detailliert.pdf): acht Seiten zur NAND-Netzliste, PULSE, Zeitverläufen, Messwerten und Auswertung sowie zur freiwilligen Vertiefung.
- `aufgaben/Tag06_Aufgaben_Neu.pdf` (lokal): fünf Seiten mit dem gesamten Tag-6-Stoff, ohne Lösungen und mit kleineren Zwischenschritten.

Die bisherigen PDFs bleiben erhalten. Die neuen LaTeX-Quellen liegen in `quellen/` und lassen sich ebenfalls mit `tectonic` bauen.

## Materialien finden

### Zusammenfassungen und Lernhilfen

- [Tag06_Aufgabe6_7_Detailliert.pdf](<zusammenfassungen/Tag06_Aufgabe6_7_Detailliert.pdf>)
- [Tag06_Zusammenfassung.pdf](<zusammenfassungen/Tag06_Zusammenfassung.pdf>)

### Aufgabenblätter

- `aufgaben/Tag06_Aufgaben.pdf` (lokal)
- `aufgaben/Tag06_Aufgaben_Neu.pdf` (lokal)

### LaTeX-Quellen

- `quellen/Tag06_Aufgabe6_7_Detailliert.tex` (lokal)
- `quellen/Tag06_Aufgaben.tex` (lokal)
- `quellen/Tag06_Aufgaben_Neu.tex` (lokal)
- `quellen/Tag06_Zusammenfassung.tex` (lokal)

Die ausführbaren Python- bzw. SPICE-Dateien bleiben an ihren bisherigen Stellen. Terminalbefehle in bestehenden PDFs gelten damit weiterhin. Die PDFs wurden beim Sortieren nicht verändert; vorhandene Anmerkungen bleiben erhalten.
