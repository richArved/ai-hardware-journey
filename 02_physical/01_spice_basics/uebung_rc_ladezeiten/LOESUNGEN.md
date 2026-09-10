# Musterlösung: Zwei RC-Ladezeiten

Deine Dateien bleiben erhalten. Deine aktuelle Netzliste verwendet bereits C2 = 2 µF (Zusatzversuch). Die Grundaufgabe verwendet C2 = 1 µF. Die getrennte Musterlösung in `loesung/` simuliert beide Fälle und erzeugt die Vergleichsplots.

## 1. Schaltung

```spice
V1 in 0 PULSE(0 5 1m 1u 1u 10m 20m)
R1 in out_a 1k
C1 out_a 0 1u
R2 in out_b 3.3k
C2 out_b 0 1u
```

Beide Zweige liegen parallel an derselben idealen Quelle. Die Ausgangsknoten dürfen nicht verbunden werden. Deine Verdrahtung ist richtig.

## 2. Vorhersagen

1. A lädt schneller, weil sein Produkt RC kleiner ist.
2. A entlädt schneller, aus demselben Grund.
3. Bei dauerhaftem Eingang von 5 V nähern sich beide Ausgänge 5 V. Im stationären Zustand fließt kein Kondensatorstrom und damit fällt über den jeweiligen Widerständen keine Spannung ab.
4. Es entstehen hier keine negativen Ausgangspulse. Der Ausgang liegt direkt über dem jeweiligen Kondensator gegen Masse. Seine Spannung ist stetig und bewegt sich bei diesem passiven RC-Aufbau zwischen 0 und 5 V.

Deine Vorhersagen stimmen. Präzisierung: Beim Entladen fließt der Strom im geschlossenen Kreis über Widerstand und Quelle; Masse ist kein Stromabfluss ins Nichts.

## 3. Arbeitspunkt und Simulation

Am Anfang ist die PULSE-Quelle auf 0 V. Daher ergibt `op`: Eingang = 0 V, Ausgang A = 0 V, Ausgang B = 0 V.

```spice
.control
set wr_singlescale
set wr_vecnames
op
print v(in) v(out_a) v(out_b)
tran 10u 45m 0 10u
wrdata results/ladezeiten_tran.txt v(in) v(out_a) v(out_b)
quit
.endc
.end
```

Die letzte `10u`-Angabe begrenzt den maximalen internen Zeitschritt. In deiner Datei fehlt diese ausdrückliche Begrenzung noch; die Analyse selbst ist vorhanden. `plot` innerhalb von ngspice ist für den Export und die Python-Diagramme nicht erforderlich.

## 4. Python und Diagramme

Die Spalten sind Zeit in Sekunden, Eingang, Ausgang A, Ausgang B. `skiprows=1` überspringt die Kopfzeile; Multiplikation der Zeit mit 1000 ergibt Millisekunden. Deine Zuordnung ist richtig.

Erwartung: A steigt und fällt schneller. B erreicht nach der ersten hohen Phase den Endwert weniger vollständig. Beide Ausgänge bleiben nichtnegativ; die Eingangsspannung wechselt zwischen 0 und 5 V. Bei weiteren Perioden kann B mit einer Restspannung starten.

Lauffähiger Vergleichscode: `loesung/plot.py`. Sechs fertige Diagramme liegen in `loesung/results/` (drei pro Variante). Die Legenden nennen R und C, sodass der Zusatzversuch erkennbar ist.

## 5. Theoretische Zeitkonstanten

$$\tau_A=R_1C_1=1000\,\Omega\cdot1\,\mu\mathrm{F}=1\,\mathrm{ms}$$

$$\tau_B=R_2C_2=3300\,\Omega\cdot1\,\mu\mathrm{F}=3{,}3\,\mathrm{ms}$$

B hat in der Grundaufgabe die 3,3-fache Zeitkonstante von A.

Zusatzversuch:

$$\tau_{B,\,2\mu F}=3300\,\Omega\cdot2\,\mu\mathrm{F}=6{,}6\,\mathrm{ms}$$

Verdoppelung der Kapazität verdoppelt die Zeitkonstante. A bleibt unverändert, weil die ideale Spannungsquelle ihren Eingang unabhängig von der Belastung auf dem vorgegebenen Wert hält.

## 6. Aufladen auswerten

Für den ersten idealen Sprung bei t0 = 1 ms:

$$U(t)=5\,\mathrm{V}\left(1-e^{-(t-t_0)/\tau}\right)$$

$$U_{63{,}2\%}=5(1-e^{-1})\,\mathrm{V}\approx3{,}1606\,\mathrm{V}$$

| Zweig | Schnittpunkt auf Zeitachse, ungefähr | Abzüglich 1 ms: Zeitkonstante |
|---|---:|---:|
| A | 2 ms | 1 ms |
| B, 1 µF | 4,3 ms | 3,3 ms |
| B, 2 µF | 7,6 ms | 6,6 ms |

Mit der endlichen Anstiegszeit von 1 µs ergeben sich simuliert ungefähr 2,0005 / 4,3005 / 7,6005 ms als Schnittpunkte. Diese kleinen Abweichungen sind kein Schaltungsfehler.

Wichtig: Den 63,2-%-Pegel auf den theoretischen Endwert 5 V beziehen, nicht auf die nach 10 ms erreichte Spannung.

## 7. Entladen auswerten

Der Abfall beginnt wegen der vorherigen Anstiegszeit bei 11,001 ms und endet bei 11,002 ms. Für eine saubere numerische Messung verwendet die Musterlösung das Ende der Flanke als Start. Beim visuellen Ablesen reicht ungefähr 11 ms.

$$U(t)=U_\mathrm{Start}e^{-(t-t_\mathrm{Start})/\tau}$$

$$U(t_\mathrm{Start}+\tau)=U_\mathrm{Start}/e\approx0{,}368U_\mathrm{Start}$$

| Zweig | Startspannung bei 11,002 ms | 36,8-%-Pegel (genauer: 1/e) | Schnittpunkt ungefähr | Gemessene Zeitspanne |
|---|---:|---:|---:|---:|
| A | 4,997249 V | 1,838385 V | 12,002 ms | 1 ms |
| B, 1 µF | 4,757841 V | 1,750312 V | 14,302 ms | 3,3 ms |
| B, 2 µF | 3,900994 V | 1,435095 V | 17,602 ms | 6,6 ms |

Warum nicht immer 36,8 % von 5 V? Der langsamere Kondensator erreicht vor dem Abschalten keine vollen 5 V. Für eine exponentielle Abnahme muss die Marke relativ zum tatsächlichen Startwert berechnet werden. Eine zu hohe Marke würde zu früh erreicht und die Zeitkonstante zu klein geschätzt.

Die aktuelle Netzliste mit C2 = 2 µF muss mit der letzten Tabellenzeile verglichen werden. Vollständige numerische Ergebnisse stehen in `loesung/results/vergleich.txt`.

## 8. Verständnisfragen mit kurzen Erklärungen

### Warum beeinflusst der größere Widerstand Laden und Entladen?

Bei gleicher antreibender Spannung lässt ein größerer Widerstand weniger Strom fließen: I = U/R. Die Kondensatorspannung ändert sich dadurch langsamer, sowohl beim Zuführen als auch beim Abführen von Ladung. In beiden Richtungen bestimmt dasselbe RC-Produkt die Geschwindigkeit.

### Sind Lade- und Entladezeitkonstante desselben Zweigs gleich?

Ja, in dieser Schaltung. Beim Laden und Entladen wirken derselbe Widerstand und derselbe Kondensator. Eine andere Startspannung verändert die Höhe der Kurve, aber nicht ihre Zeitkonstante. Kleine Unterschiede beim Ablesen entstehen durch Auflösung, endliche Flanken und numerische Auswertung.

### Warum gibt es keine negativen Pulse wie beim Hochpass?

Hier misst du direkt die Kondensatorspannung gegen Masse. Sie kann nicht springen. Wenn der Eingang auf null fällt, bleibt der Kondensator zunächst positiv geladen und entlädt sich gegen null. Beim Hochpass liegt der Kondensator zwischen Eingang und Ausgang: Seine Spannungsdifferenz bleibt kurzzeitig erhalten, während der Eingang fällt. Deshalb kann dort der Ausgang unter null springen.

### Was wird jeweils gemessen?

Hier (Tiefpass): Uout = UC, die Spannung zwischen Kondensatoranschluss und Masse. Beim Hochpass: Uout = UR, die Spannung über dem Widerstand. Die dortige Kondensatorspannung lautet UC = Uin − Uout. Derselbe Bauteiltyp kann daher je nach Anordnung zu einem anders aussehenden Ausgangssignal führen.

## Wiederholen

Im Ordner `loesung` ausführen:

```sh
source "$HOME/.venvs/ai-hardware-spice/bin/activate"
ngspice -b ladezeiten.cir
python plot.py
```

Die Musterlösung verändert deine eigene Netzliste und deine Ergebnisse nicht.
