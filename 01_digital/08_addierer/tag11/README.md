# Tag 11: Addierer - Ripple-Carry, Lookahead und Prefix

**Status: abgeschlossen für die Lernziele von Tag 11. Die detaillierte Prefix-Hierarchie bleibt für Woche 9 offen. Ergebnisse und offene Lernpunkte stehen in [auswertung.md](auswertung.md).**

Grundlage: aktueller Jahresplan, Lerntag 11 / W02 T5, und Harris & Harris,
*Digital Design and Computer Architecture, RISC-V Edition*, Kapitel 5.2.1,
Buchseiten 237–244 / PDF-Seiten 260–267. Kernlektüre: Buchseiten 238–243.

## Unterlagen

- [Zusammenfassung](zusammenfassungen/Tag11_Zusammenfassung.pdf): sechs Seiten, eigene Schwarz-Weiß-Abbildungen, Formeln, Zeitmodelle und Python-Hinweise.
- Aufgaben: `aufgaben/Tag11_Aufgaben.pdf` (lokal), vier Seiten mit Platz für eigene Rechnungen.
- [Python-Starter](praxis/delay_lernen.py): nur zwei kleine Funktionen selbst ergänzen.
- [Referenz](praxis/delay_referenz.py): Hilfe zum späteren Vergleichen.
- [Funktionsprüfer](praxis/pruefe_delay.py) und [Plotprogramm](praxis/plot_delay.py).
- [Schaltungsprüfer](praxis/pruefe_schaltungen.py): Python erzeugt 8/512 Testfälle und lässt DEINE Digital-Datei simulieren.
- [Schaltungsordner](praxis/schaltungen/) und [Auswertung](auswertung.md).

## Reihenfolge

1. Falls passend, bis zu 15 Minuten Wiederholung aus `00_notes/wiederholung.md` im Repository.
2. Halb-/Volladdierer verstehen, Aufgaben 1–3 auf Papier.
3. Einen Volladdierer bauen und prüfen; vier Instanzen zum Ripple-Addierer verbinden und prüfen.
4. Generate/Propagate und den Unterschied zwischen Block-CLA und Prefix verstehen.
5. Zwei Python-Funktionen schreiben, prüfen und Plot erzeugen.
6. Eigene Nachweise in `auswertung.md` festhalten.

Der Kalender nennt 60 Minuten Theorie und 60 Minuten Praxis als Orientierung.
Kein eigener Prefix-Aufbau, kein neuer ngspice-Versuch und kein selbstgeschriebener Plotter nötig.
Python bleibt enthalten, aber die Bibliotheksdetails sind Referenzhilfe.

## Start im Tagesordner

Ohne Zusatzpakete:

```sh
cd praxis
python3 pruefe_delay.py
python3 pruefe_schaltungen.py schaltungen/volladdierer.dig
python3 pruefe_schaltungen.py schaltungen/ripple4.dig
```

Die Funktionsprüfung meldet zunächst die noch offenen Funktionen. Die Schaltungsprüfung
wartet auf deine gespeicherten Dateien. Java und Digital werden benötigt; der Standardpfad
ist `~/Downloads/Digital/Digital.jar`. Alternativ `--jar /pfad/zu/Digital.jar` angeben.

Für den Plot einmalig eine Umgebung im Tagesordner einrichten:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install matplotlib
cd praxis
python plot_delay.py
```

Die Befehlsblöcke starten jeweils im Tagesordner. Bist du schon in `praxis`, gehe vorher mit
`cd ..` zurück. Später genügt die Aktivierung der bestehenden Umgebung.
`python pruefe_delay.py --referenz` und `python plot_delay.py --referenz` verwenden ausdrücklich
die fertige Referenz, nicht deine Umsetzung.

## Wichtige Modellgrenze

Im Buch ist der CLA aus einer Kette fester Blöcke weiterhin O(N).
O(log N) gilt hier für hierarchisches Lookahead/Prefix. Der vom Kalender vorgegebene
Funktionsname `delay_cla` bleibt erhalten, bezeichnet aber ausdrücklich dieses hierarchische Modell.
Formeln: `n * t_fa` und `(ceil(log2(n)) + 2) * t_stufe`, gültig für positive ganze n und positive Zeiten.
Der Plot nutzt 2 ns pro Ripple-Stufe und 1 ns pro Prefix-Modellstufe, alle N von 4 bis 64.
Er vergleicht Annahmen, keine gemessene Hardware. Gatterpfade werden separat gezählt.

Die Quellen und Aufgaben bleiben gemäß Git-Regel lokal. Es wird nur die Zusammenfassungs-PDF veröffentlicht.
