# Tag 4 – Zahlensysteme und Binärarithmetik

Grundlage: Woche 1, Tag 4 deines Jahresplans (10.09.2026).
Ziel: Binär, Hex und Dezimal umrechnen, Zweierkomplement verstehen und
vorzeichenbehafteten Overflow erkennen. Theorie: DDCA Kapitel 1.4 (48 Minuten).
Praxis: vier Funktionen implementieren und mit pytest prüfen (72 Minuten).

## Start

Im Terminal ausführen:

```sh
cd "$HOME/Learning/Semiconductors : AI Hardware/ai-hardware-journey/01_digital/01_zahlensysteme/tag04"
source "$HOME/.venvs/ai-hardware-day04/bin/activate"
python -m pytest -q
```

Die Python-Umgebung ist bereits eingerichtet. Am Anfang sind die Tests rot:
Die vier Funktionen werfen absichtlich `NotImplementedError`. Das ist dein
Ausgangspunkt, kein Installationsfehler. Ziel ist, alle Tests grün zu bekommen.

Öffne `hardware_numbers/numbers.py` und ersetze die vier Platzhalter.
Das Modul liegt in einem Paket, damit es Pythons Standardmodul `numbers`
nicht überschattet und dadurch andere Bibliotheken stört.

## Arbeitsauftrag

1. **Binärdarstellung (ca. 12 Minuten):** Implementiere `to_bin(value, bits)`.
   Eingabe ist eine nichtnegative Ganzzahl, Ausgabe genau `bits` Ziffern ohne
   `0b`, einschließlich führender Nullen. Beispiel: `to_bin(3, 4) == "0011"`.
2. **Hexdarstellung (ca. 10 Minuten):** Implementiere `to_hex(value, bits)`.
   Verwende Großbuchstaben, kein `0x` und genau aufgerundet `bits / 4` Stellen.
   Beispiel: `to_hex(3, 5) == "03"`. Die Zahl muss in die tatsächliche Bitbreite
   passen, auch wenn diese kein Vielfaches von vier ist.
3. **Zweierkomplement (ca. 18 Minuten):** Implementiere
   `from_twos_complement(raw, bits)`. `raw` ist ein nichtnegatives Bitmuster
   als Python-Integer; das Ergebnis ist seine signed Interpretation.
   Beispiel: `from_twos_complement(14, 4) == -2`.
4. **Addition (ca. 22 Minuten):** Implementiere
   `add_with_overflow_flag(a, b, bits)`. Eingaben sind signed Ganzzahlen.
   Gib `(signed_ergebnis, overflow_bool)` zurück. Das Ergebnis wird auf die
   Bitbreite begrenzt und wieder signed interpretiert.
   Beispiel: `add_with_overflow_flag(7, 2, 4) == (-7, True)`.
5. **Prüfen und erklären (ca. 10 Minuten):** Führe alle Tests aus und ergänze
   mindestens zwei eigene Fälle. Halte deine Erkenntnisse in `auswertung.md` fest.

Für alle Funktionen gilt: `bits >= 1`. Ungültige Bitbreiten und Werte außerhalb
des jeweiligen Eingabebereichs müssen `ValueError` auslösen. Du darfst
Integer-Eingaben voraussetzen; andere Typen sind nicht Teil der Aufgabe.
Beliebige Bitbreiten sind gefordert: auch 1, 5 oder 65 Bit.

Unsigned Bereich: `0` bis `2**bits - 1`.
Signed Bereich: `-2**(bits-1)` bis `2**(bits-1) - 1`.
Python-Integer laufen nicht von selbst wie ein begrenztes Hardwareregister über.
Signed Overflow und ein unsigned Übertrag sind verschiedene Eigenschaften.

## Schrittweise testen

```sh
python -m pytest -q -k to_bin
python -m pytest -q -k to_hex
python -m pytest -q -k from_twos_complement
python -m pytest -q -k add_with_overflow_flag
python -m pytest -q
```

Die letzte Ausführung prüft zusätzlich die ungültigen Eingaben.
Zum schnellen Stoppen beim ersten Fehler: `python -m pytest -xq`.
Die Tests enthalten erwartete Ergebnisse; versuche die Aufgaben zuerst selbst.

## Erfolgskontrolle

- Alle Tests sind grün, einschließlich deiner eigenen Fälle.
- Du kannst `0xB7` ohne Taschenrechner in Dezimal und Binär umrechnen.
- Du kannst denselben 8-Bit-Wert unsigned und signed interpretieren.
- Du kannst erklären, warum Carry und signed Overflow nicht dasselbe sind.

## Umgebung bei Bedarf neu anlegen

Die virtuelle Umgebung liegt außerhalb des Repos, weil dessen Pfad einen
Doppelpunkt enthält, den Python für venv-Verzeichnisse nicht erlaubt.

```sh
python3 -m venv "$HOME/.venvs/ai-hardware-day04"
"$HOME/.venvs/ai-hardware-day04/bin/python" -m pip install -r requirements.txt
```

## Materialien finden

### Zusammenfassungen und Lernhilfen

- [Tag04_Cheatsheet.pdf](<zusammenfassungen/Tag04_Cheatsheet.pdf>)

### Aufgabenblätter

- `aufgaben/Tag04_Abschlussarbeit.pdf` (lokal)
- `aufgaben/Tag04_Festigung_Aufgaben.pdf` (lokal)

### LaTeX-Quellen

- `quellen/Tag04_Abschlussarbeit.tex` (lokal)
- `quellen/Tag04_Cheatsheet.tex` (lokal)
- `quellen/Tag04_Festigung_Aufgaben.tex` (lokal)

Die ausführbaren Python- bzw. SPICE-Dateien bleiben an ihren bisherigen Stellen. Terminalbefehle in bestehenden PDFs gelten damit weiterhin. Die PDFs wurden beim Sortieren nicht verändert; vorhandene Anmerkungen bleiben erhalten.
