# Tag 8: Karnaugh-Diagramme und Minimierung

Lernplan W02 T2, Lerntag 8. Literatur: Harris & Harris, *Digital Design and Computer Architecture, RISC-V Edition*, Kapitel 2.7, Buchseiten 73–81 (PDF-Seiten 97–105).

## Materialien

- [Zusammenfassung](zusammenfassungen/Tag08_Zusammenfassung.pdf): sieben Seiten mit ausgefüllten Beispielkarten, Randgruppen, Don't-Cares, POS und Algorithmus-Erklärung.
- `aufgaben/Tag08_Aufgaben.pdf` (lokal): Wiederholung, zehn eigene Übungskarten und Python-Aufgaben. Die Karten sind eigene Aufgaben im Buchthemenumfang, keine Kopien der Übungen 2.28–2.40.
- [Eigene Python-Startdatei](praxis/qm_lernversion.py): Quine-McCluskey in Teilaufgaben.
- [Einfach geschriebener Minimierer](praxis/qm_einfach.py): ausgeschriebene Schleifen und deutsche Kommentare. Beginne mit `combine`; die Beispiel-Eingaben stehen unten in der Datei. Start: `python3 qm_einfach.py` im Praxisordner. Gleiche Minimierung wie die Referenz, ohne deren Kommandozeilenoptionen.
- [Referenzprüfer](praxis/qm_referenz.py): funktionierender Minimierer für 1–4 Eingänge. Erst nach der Handlösung verwenden.
- [Aufgabendaten](praxis/faelle.json): dieselben zehn Funktionen wie im Aufgabenblatt.
- [auswertung.md](auswertung.md): Vorlage für Ergebnisse und offene Fragen.
- `quellen/` (lokal): LaTeX-Quellen.

## Reihenfolge

1. Zusammenfassung Seiten 1–3, dann Wiederholung und Karten 1–4.
2. Seiten 4–6, dann Karten 5–10 einschließlich Don't-Cares und POS-Zusatz.
3. Ergebnisse mit dem Referenzprüfer vergleichen. Gleichwertigkeit für alle festgelegten Zeilen prüfen.
4. Eigenen Minimierer schrittweise erarbeiten und die Auswertung ergänzen.

Der Kalender enthält Handaufgaben und einen eigenen Python-Minimierer. Der Programmierteil ist ein eigener größerer Lernblock; der Referenzprüfer ist eine Hilfe zur Kontrolle und ersetzt die eigene Umsetzung nicht.

## Starten

Keine zusätzlichen Pakete nötig:

```sh
cd "$HOME/Learning/Semiconductors : AI Hardware/ai-hardware-journey/01_digital/05_karnaugh/tag08/praxis"
python3 qm_referenz.py --fall 1
python3 qm_referenz.py --alle
python3 qm_lernversion.py
```

Der Referenzprüfer minimiert SOP nach Termzahl, dann Literalzahl. Er darf bei mehreren gleich guten Lösungen eine andere als deine auswählen. Die Textausgaben sind Logiknotation, kein direkt ausführbarer Python-Code.

## PDF-Neubau

Im Tag-8-Ordner, nach Sicherung eigener PDF-Anmerkungen:

```sh
tectonic --outdir zusammenfassungen quellen/Tag08_Zusammenfassung.tex
tectonic --outdir aufgaben quellen/Tag08_Aufgaben.tex
```

Aufgabenblätter und `.tex` bleiben lokal und sind von Git ausgeschlossen.
