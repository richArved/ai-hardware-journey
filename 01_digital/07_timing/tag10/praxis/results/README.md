# Vorbereitende Referenzläufe

Diese Dateien wurden beim Erstellen von Tag 10 durch Codex erzeugt und geprüft. Sie belegen die Funktionsfähigkeit der bereitgestellten Modelle. Sie sind **kein Nachweis, dass du die Aufgaben bereits selbst bearbeitet hast**.

| Datei | Herkunft |
| --- | --- |
| `python_zeitverlauf.txt` | `timing_einfach.py`, Standardparameter 3/2/1 ns |
| `python_zeitverlauf.png` | Python-Daten mit `plot_verlauf.py` gezeichnet |
| `spice_run.log` | ngspice 47, `hazard_rc.cir` |
| `spice_zeitverlauf.txt` | ngspice-Transientenanalyse mit maximal 0,02 ns Zeitschritt |
| `spice_zeitverlauf.png` | SPICE-Daten mit `plot_verlauf.py` gezeichnet |

Referenz: Python-Glitch 3 ns; ngspice-Glitch etwa 2,78 ns zwischen den 0,5-V-Durchgängen. Der korrigierte Ausgang bleibt im betrachteten Fenster HIGH (SPICE-Mindestwert 1 V zwischen 15 und 40 ns).

Vor eigenen Varianten Dateien sichern oder einen separaten Arbeitsordner verwenden. Eigene Beobachtungen und den tatsächlich verwendeten Stand in `auswertung.md` dokumentieren.
