# Abschlussaufgabe: Ein belasteter RC-Tiefpass

Du kombinierst Spannungsteiler, Parallelwiderstände und RC-Zeitverhalten. Die Arbeitsdateien sind leer: `belasteter_rc.cir`, `plot.py`, `auswertung.md`. Ergebnisse kommen nach `results/`.

## 1. Schaltung

```text
in ---- R1 ---- out
                |
           +----+----+
           |         |
           C1        RL
           |         |
           +----0----+
```

R1 = 1 kΩ, C1 = 1 µF, RL zunächst 1 kΩ. R1 liegt zwischen in und out; C1 und RL liegen jeweils zwischen out und Masse.

Quelle:

```spice
V1 in 0 PULSE(0 5 1m 1u 1u 10m 20m)
```

## 2. Vorhersage

Was verändert RL gegenüber einem unbelasteten RC-Tiefpass? Vermute, ob Endspannung und Reaktionszeit größer, kleiner oder gleich werden. Schreibe vor der Simulation eine Begründung auf.

## 3. Endspannung durch Arbeitspunkt prüfen

Stelle die Quelle vorübergehend auf `DC 5` und führe `op` aus. Bestimme Uout und den Quellenstrom. Berechne Uout auch mit der Spannungsteilerformel. Im stationären Gleichstromzustand fließt kein Strom durch den idealen Kondensator.

Stelle die Quelle danach wieder auf PULSE zurück.

## 4. Zeitverlauf

Simuliere 25 ms mit maximal 10 µs Zeitschritt. Exportiere Eingang und Ausgang nach `results/last_1k.txt`. Plotte die Übersicht, das erste Aufladen und das erste Entladen.

## 5. Neue Denkaufgabe: Welcher Widerstand bestimmt tau?

Nicht einfach R1 verwenden: Beide Widerstände beeinflussen die Zeitkonstante.

Um den Widerstand aus Sicht des Kondensators zu bestimmen, ersetzt du die ideale Spannungsquelle gedanklich durch eine Verbindung mit 0 V (einen Kurzschluss). Entferne für diese Betrachtung den Kondensator gedanklich. Vom Ausgang nach Masse siehst du jetzt R1 und RL parallel.

Nur für diese Rechnung die Quelle gedanklich ersetzen; in der Simulation bleibt sie angeschlossen!

$$R_\mathrm{eff}=R_1\parallel R_L=\frac{R_1R_L}{R_1+R_L}$$

$$\tau=R_\mathrm{eff}C_1$$

Berechne die Zeitkonstante selbst.

## 6. Rechnung gegen Plot prüfen

Beim ersten Laden beträgt die 63,2-%-Marke 0,632 mal die Ausgangs-Endspannung aus Schritt 3, nicht automatisch 0,632 mal 5 V. Ziehe zum Bestimmen von tau den Beginn des Eingangssprungs ab.

Beim Entladen verwende 36,8 % des tatsächlichen Ausgangswerts zu Beginn des Entladens. Vergleiche beide abgelesenen Zeitkonstanten mit Schritt 5.

## 7. Zweite Last

Wiederhole mit RL = 3.3k; speichere getrennt als `results/last_3k3.txt`. Berechne Endspannung und Zeitkonstante erneut. Plotte die beiden Ausgangskurven gemeinsam. Optional: Teile jede Ausgangskurve durch ihren eigenen theoretischen Endwert und vergleiche die normierten Kurven.

## 8. Erklären

- Warum erreicht der Ausgang trotz konstanten 5 V Eingang keine 5 V?
- Warum kann ein zusätzlicher Lastwiderstand die Zeitkonstante verkleinern?
- Bedeutet eine kleinere Zeitkonstante automatisch eine höhere Ausgangsspannung?
- Was passiert gedanklich, wenn RL sehr groß wird (Verbraucher fast abgeklemmt)?

Fertig: zwei Lastfälle simuliert, Endspannungen und Zeitkonstanten rechnerisch sowie grafisch verglichen und vier Fragen beantwortet.

```sh
source "$HOME/.venvs/ai-hardware-spice/bin/activate"
ngspice -b belasteter_rc.cir
python plot.py
```
