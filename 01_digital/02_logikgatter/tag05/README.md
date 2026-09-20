# Tag 5: Logikgatter und Boolesche Algebra

Beginne mit [Tag05_Zusammenfassung.pdf](zusammenfassungen/Tag05_Zusammenfassung.pdf). Die acht Seiten enthalten eigene
Schaltungszeichnungen, Wahrheitstabellen, Formeln und den Praxisauftrag.
Die bearbeitbare LaTeX-Quelle liegt in `quellen/`.

## Grundlage im vorgesehenen Buch

Harris & Harris: Digital Design and Computer Architecture, RISC-V Edition.

- Abschnitt 1.5, Buchseiten 17–20: Logikgatter.
- Abschnitt 1.6, Buchseiten 20–24: elektrische Pegel, Störabstände und Kennlinien.
- Ergänzend 2.3, Buchseiten 58–63: Boolesche Algebra und De Morgan.
- Bezug 2.2 sowie 2.4–2.5.2: Gleichungen, Schaltpläne und Bubble Pushing.

Die Kapitelangabe im Jahresplan ist verkürzt: De Morgan und die Booleschen
Gesetze stehen in dieser Ausgabe in Kapitel 2.3, nicht in 1.6.

## Praxis

NOT, AND, OR und XOR aus NAND-Gattern in Logisim-Evolution bauen und alle
Eingangskombinationen prüfen. NOR dient als fünfter Aufbau für die im Plan
geforderte Anzahl. Zusätzlich beide De-Morgan-Gesetze schaltungstechnisch
vergleichen. Geplanter Dateiname: `tag05_nand.circ`.
Diese Zusammenfassung enthält noch keine fertige Logisim-Schaltung.

## PDF neu erzeugen

Aus diesem Ordner mit dem bereits installierten LaTeX-Compiler:

```sh
tectonic --outdir zusammenfassungen quellen/Tag05_Zusammenfassung.tex
```

## Materialien finden

### Zusammenfassungen und Lernhilfen

- [Tag05_Zusammenfassung.pdf](<zusammenfassungen/Tag05_Zusammenfassung.pdf>)
- `zusammenfassungen/abbildungen/Inverter_Kennlinie_Erklaerung.svg` (lokal)

### Aufgabenblätter

- `aufgaben/Tag05_Abschluss_Aufgaben.pdf` (lokal)
- `aufgaben/Tag05_Elektrische_Pegel_Aufgaben.pdf` (lokal)
- `aufgaben/Tag05_Logik_Festigung_Aufgaben.pdf` (lokal)

### Lösungen

- `loesungen/Tag05_Abschluss_Loesungen.pdf` (lokal)
- `loesungen/Tag05_Elektrische_Pegel_Loesungen.pdf` (lokal)

### Schaltungen

- [6a.dig](<praxis/digital/aufgabe06/6a.dig>)
- [6b.dig](<praxis/digital/aufgabe06/6b.dig>)
- [6c.dig](<praxis/digital/aufgabe06/6c.dig>)
- [DeMorgan1_NOR.circ](<praxis/logisim/DeMorgan1_NOR.circ>)
- [DeMorgan2_NAND.circ](<praxis/logisim/DeMorgan2_NAND.circ>)
- [NandToNOR.circ](<praxis/logisim/NandToNOR.circ>)
- [NandToXor.circ](<praxis/logisim/NandToXor.circ>)

### LaTeX-Quellen

- `quellen/Tag05_Abschluss_Aufgaben.tex` (lokal)
- `quellen/Tag05_Abschluss_Loesungen.tex` (lokal)
- `quellen/Tag05_Elektrische_Pegel_Aufgaben.tex` (lokal)
- `quellen/Tag05_Elektrische_Pegel_Loesungen.tex` (lokal)
- `quellen/Tag05_Logik_Festigung_Aufgaben.tex` (lokal)
- `quellen/Tag05_Zusammenfassung.tex` (lokal)

Die ausführbaren Python- bzw. SPICE-Dateien bleiben an ihren bisherigen Stellen. Terminalbefehle in bestehenden PDFs gelten damit weiterhin. Die PDFs wurden beim Sortieren nicht verändert; vorhandene Anmerkungen bleiben erhalten.
