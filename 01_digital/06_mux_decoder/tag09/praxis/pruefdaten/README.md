# Erwartete Werte zum Vergleichen

Die CSV-Dateien enthalten vollständige Solltabellen, keine Messergebnisse deiner Schaltungen. Trennzeichen ist ein Komma; alle Signalwerte stehen als einzelne 0 oder 1 in eigenen Spalten. Sie lassen sich als Text oder Tabelle lesen. Ein direkter Import ist abhängig vom Simulator und dessen Testformat; die Dateien sind nicht als universelles Importformat gedacht.

| Datei | Eingabespalten | Ausgabespalten | Zeilen ohne Kopfzeile |
| --- | --- | --- | --- |
| `mux4_soll.csv` | S1, S0, D0, D1, D2, D3 | Y | 64 |
| `decoder3_soll.csv` | A2, A1, A0 | Y7 bis Y0 | 8 |
| `priority8_soll.csv` | I7 bis I0 | Q2, Q1, Q0, NONE | 256 |
| `majority3_soll.csv` | A, B, C | Y | 8 |

## So vergleichst du

1. Erzeuge die Wahrheitstabelle deiner Schaltung oder führe passende Testvektoren im Simulator aus.
2. Ordne die Spalten anhand der Signalnamen zu. Eine andere Spaltenreihenfolge ist kein Fehler, aber die Zuordnung muss stimmen.
3. Vergleiche für dieselbe Eingabe jedes Ausgangsbit mit der Solltabelle.
4. Dokumentiere die tatsächlich geprüfte Zeilenzahl und alle Abweichungen. Bei nur einzelnen Handtests ist die vollständige Prüfung noch offen.

Decoder: genau eine Ausgangs-1 pro Zeile. Encoder: höchster aktiver Index gewinnt, nicht die Anzahl der Einsen. Bei acht Nullen ist Q=000 und NONE=1; bei nur I0=1 ist Q ebenfalls 000, aber NONE=0.
