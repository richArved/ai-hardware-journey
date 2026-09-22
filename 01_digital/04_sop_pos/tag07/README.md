# Tag 7: Wahrheitstabelle zu SOP und POS

Aktueller Lernplan: W02 T1, Lerntag 7. Literatur: Harris & Harris, *Digital Design and Computer Architecture, RISC-V Edition*, Abschnitte 2.1–2.3, Buchseiten 53–65. Ergänzend 2.4 für den Gatteraufbau. Karnaugh-Diagramme folgen an Tag 8.

## Lernmaterialien

- [Zusammenfassung](zusammenfassungen/Tag07_Zusammenfassung.pdf): acht Seiten mit durchgerechneten Beispielen, Diagrammen und Python-Hilfen.
- `aufgaben/Tag07_Aufgaben.pdf` (lokal): sechs Seiten, von einzelnen Tabellenzeilen bis zum eigenen Tool.
- `quellen/` (lokal): bearbeitbare LaTeX-Quellen.
- [Python-Tool](praxis/truthtable.py): kommentierte Umsetzung für kanonische SOP und POS.
- [Eigene Auswertung](auswertung.md): Ergebnisse, Prüfungen und offene Lernpunkte.

## Reihenfolge

1. Zusammenfassung Seiten 1–5 lesen und Aufgaben 1–4 bearbeiten.
2. De Morgan wiederholen und Aufgaben 5–6 bearbeiten.
3. Zusammenfassung Seiten 7–8 lesen und das Tool in Aufgaben 7–8 implementieren.
4. Majority3 und XOR3 vollständig prüfen, danach `auswertung.md` ergänzen.

Das Kalenderziel ist ein Tool, das die kanonische SOP und POS aus einer Liste erzeugt. Bei Majority3 enthält die SOP vier Minterme. Nimm die Zeitangaben des Kalenders als Orientierung; die Lernschritte lassen sich auf mehrere Abschnitte verteilen.

## Python starten

Keine zusätzlichen Bibliotheken nötig. Im Terminal:

```sh
cd "$HOME/Learning/Semiconductors : AI Hardware/ai-hardware-journey/01_digital/04_sop_pos/tag07/praxis"
python3 truthtable.py
```

Das Skript gibt die SOP und POS für Majority3 und XOR3 aus. Ausgabetexte verwenden `!`, `*`, `+` als Logiknotation; sie werden nicht als Python-Code ausgeführt.

## PDFs bei Bedarf neu bauen

Im Tag-7-Ordner:

```sh
tectonic --outdir zusammenfassungen quellen/Tag07_Zusammenfassung.tex
tectonic --outdir aufgaben quellen/Tag07_Aufgaben.tex
```

Bestehende PDF-Anmerkungen vor einem Neubau separat sichern. Aufgaben und `.tex` bleiben gemäß der Repository-Regel lokal; die Zusammenfassungs-PDF darf versioniert werden.
