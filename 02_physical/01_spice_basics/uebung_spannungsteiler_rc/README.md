# Erste Simulationen mit ngspice

## Installation auf macOS

Homebrew vorausgesetzt: `brew install ngspice`. Mit `ngspice --version` prüfen.
Auf diesem Mac war ngspice 47 bereits installiert.

Python-Pakete in einer eigenen Umgebung installieren. Diese liegt außerhalb des
Repos, weil dessen übergeordneter Pfad einen Doppelpunkt enthält; Python erlaubt
an solchen Pfaden keine virtuelle Umgebung.

```sh
python3 -m venv "$HOME/.venvs/ai-hardware-spice"
source "$HOME/.venvs/ai-hardware-spice/bin/activate"
python -m pip install numpy matplotlib
```

## Simulationen wiederholen

```sh
cd "$HOME/Learning/Semiconductors : AI Hardware/ai-hardware-journey/02_physical/01_spice_basics/uebung_spannungsteiler_rc"
source "$HOME/.venvs/ai-hardware-spice/bin/activate"
ngspice -b divider.cir > results/divider.log 2>&1
ngspice -b rc.cir > results/rc.log 2>&1
python plot.py
open results/divider_dc.png results/rc_tran.png
```

Die Netzliste beschreibt Bauteile als `Name Knoten1 Knoten2 Wert`.
`0` bezeichnet Masse, `in` den Eingang und `out` den Ausgang.
Die erste Zeile ist immer der Titel. `k` bedeutet 1000, `u` ein Millionstel,
`m` ein Tausendstel. Achtung: Für Mega verwendet SPICE `Meg`, nicht `M`.

## Spannungsteiler verstehen

```text
in ── R1 (1 kΩ) ── out ── R2 (1 kΩ) ── 0
```

`V1 in 0 DC 5` legt 5 V zwischen Eingang und Masse an.
`.op` berechnet den stationären Arbeitspunkt. Erwartet:

- Ausgang: Vout = Vin × R2 / (R1 + R2) = 2,5 V.
- Strom durch beide Widerstände: 5 V / 2 kΩ = 2,5 mA.
- ngspice meldet i(V1) = −2,5 mA: Der positive Quellenstrom ist in den
  Pluspol hinein definiert; hier liefert die Quelle Energie.

`.dc V1 0 5 0.1` variiert die Quelle von 0 bis 5 V in Schritten von 0,1 V.
Der Plot zeigt eine Gerade mit Steigung 0,5.

Die `.control`-Sektion führt `op` und `dc` explizit aus und exportiert die
Sweep-Daten mit `wrdata`. Innerhalb dieser Sektion schreibt man die
Analysebefehle ohne Punkt; die `.op`- und `.dc`-Zeilen zeigen zusätzlich
am selben Beispiel die normale Netzlisten-Syntax.

## RC-Tiefpass verstehen

```text
in ── R1 (1 kΩ) ── out ── C1 (1 µF) ── 0
```

Der Ausgang wird über dem Kondensator gemessen. Er kann seine Spannung
nicht sprunghaft ändern und lädt sich über den Widerstand auf.

`PULSE(0 5 1m 1u 1u 20m 40m)` bedeutet: 0 V auf 5 V, Start nach 1 ms,
Anstiegs- und Abfallzeit je 1 µs, Pulsbreite 20 ms, Periode 40 ms.
Der Eingang bleibt deshalb bis zum Ende unserer Simulation auf 5 V.
Vor dem Sprung ist der Kondensator durch den Anfangsarbeitspunkt ungeladen.

`.tran 10u 7m 0 10u` simuliert bis 7 ms mit einer nominalen Ausgabe-Schrittweite
von 10 µs, Speicherung ab 0 und maximaler interner Schrittweite von 10 µs.
ngspice kann kleinere adaptive Schritte verwenden. `run` führt diese Analyse aus.

Theorie für einen idealen Sprung bei t0 = 1 ms:

```text
tau = R × C = 1000 Ω × 0,000001 F = 0,001 s = 1 ms
Vout(t) = 5 V × (1 − exp(−(t − t0)/tau)), für t >= t0
```

Zeitkonstante aus dem Plot ablesen:

1. Endspannung bestimmen: 5 V.
2. 63,2 % davon suchen: ungefähr 3,16 V.
3. Schnittpunkt mit der Ausgangskurve auf die Zeitachse projizieren: ca. 2 ms.
4. Zeitpunkt des Eingangssprungs abziehen: 2 ms − 1 ms = **1 ms**.

Das Skript interpoliert den Schnittpunkt zwischen den Simulationspunkten:
1,000496 ms, etwa 0,0496 % Abweichung zu RC. Die kleine Abweichung ist mit
der endlichen Anstiegszeit von 1 µs und numerischer Interpolation vereinbar.
Nach fünf Zeitkonstanten sind ungefähr 99,3 % der Endspannung erreicht.

`plot.py` liest die Textdaten mit NumPy und erzeugt beide PNGs mit matplotlib.
Es prüft außerdem die Spannungsteilerformel und eine RC-Abweichung unter 1 %.

## Selbst ausprobieren

Ändere R1 im Spannungsteiler auf 2k: Bei 5 V Eingang solltest du rund 1,667 V
sehen. Verdopple danach C1 im Tiefpass auf 2u: Die Zeitkonstante sollte 2 ms
betragen. Passe für einen vollständigen Ladeverlauf die Simulationsdauer an.
Für einen passenden Theorievergleich müssen auch R und C im Python-Skript
mit den Werten der Netzliste übereinstimmen.

Quelle: [Offizielles ngspice-Tutorial](https://ngspice.sourceforge.io/ngspice-control-language-tutorial.html).
