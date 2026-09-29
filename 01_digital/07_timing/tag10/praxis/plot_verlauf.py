"""Zeichnet die Python- und, falls vorhanden, SPICE-Daten in Schwarz-Weiß.

Benötigt matplotlib. Erst timing_einfach.py ausführen.
Dateilesen und Zeichnen sind hier bewusst vom eigentlichen Lernmodell getrennt.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def zeichne(datei, ziel, spice):
    spalten = [[], [], [], [], [], [], []]
    with datei.open() as quelle:
        next(quelle)  # Erste Zeile enthält nur die Spaltennamen.
        for zeile in quelle:
            werte = zeile.split()
            if len(werte) != 7:
                raise ValueError('Erwartet: Zeit und sechs Signalspalten.')
            for index in range(7):
                spalten[index].append(float(werte[index]))
    if spice:
        for index in range(len(spalten[0])):
            spalten[0][index] = spalten[0][index] * 1e9  # Sekunden -> ns.

    fig, achsen = plt.subplots(6, 1, sharex=True, figsize=(9, 7))
    namen = ['A', 'NOT A', 'P', 'Q', 'Y vorher', 'Y mit BC']
    for index in range(6):
        achse = achsen[index]
        if spice:
            achse.plot(spalten[0], spalten[index+1], color='black')
            achse.axhline(0.5, color='gray', linestyle=':', linewidth=0.7)
        else:
            achse.step(spalten[0], spalten[index+1], where='post', color='black')
        achse.set_ylabel(namen[index])
        achse.set_ylim(-0.15, 1.15)
        achse.set_yticks([0, 1])
        achse.grid(axis='x', color='0.85')
    achsen[-1].set_xlabel('Zeit / ns')
    achsen[-1].set_xlim(15, 35)
    if spice:
        fig.suptitle('SPICE-RC-Lehrmodell: Spannungen in V, Schwelle 0,5 V')
    else:
        fig.suptitle('Python: feste Transportverzögerungen, logische Pegel')
    fig.tight_layout()
    fig.savefig(ziel, dpi=160)
    plt.close(fig)
    print('Gespeichert:', ziel)


if __name__ == '__main__':
    ordner = Path(__file__).resolve().parent / 'results'
    zeichne(ordner/'python_zeitverlauf.txt', ordner/'python_zeitverlauf.png', False)
    if (ordner/'spice_zeitverlauf.txt').exists():
        zeichne(ordner/'spice_zeitverlauf.txt', ordner/'spice_zeitverlauf.png', True)
