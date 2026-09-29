"""Einfaches Zeitmodell: Y = A*B + !A*C; Zusatzterm B*C.

B=C=1. A fällt bei 20 ns von 1 auf 0. Ein Listeneintrag ist 1 ns.
Feste Transportverzögerungen, keine Transistor- oder Analogsimulation.
Die Startwerte beschreiben eine bereits eingeschwungene Schaltung.
"""
from pathlib import Path


def und(a, b):
    if a == 1 and b == 1:
        return 1
    return 0


def oder(a, b):
    if a == 1 or b == 1:
        return 1
    return 0


def nicht(a):
    if a == 0:
        return 1
    return 0


def frueher(signal, zeit, verzoegerung):
    # Beispiel: bei t=25 mit 3 ns Verzögerung den Wert von t=22 lesen.
    index = zeit - verzoegerung
    if index < 0:
        return signal[0]  # Vor t=0 war die Schaltung schon stabil.
    return signal[index]


def simuliere(t_not=3, t_and=2, t_or=1):
    for wert in [t_not, t_and, t_or]:
        if type(wert) is not int or wert < 1:
            raise ValueError('Für dieses Modell ganze Verzögerungen ab 1 ns verwenden.')
    ende = 40 + t_not + t_and + t_or
    a = []
    for zeit in range(ende):
        if zeit < 20:
            a.append(1)
        else:
            a.append(0)

    not_a = [0]
    p = [1]     # P = A * B
    q = [0]     # Q = !A * C
    y = [1]
    y_sicher = [1]
    b = 1
    c = 1
    r = und(b, c)  # R bleibt 1: B und C ändern sich nicht.

    for zeit in range(1, ende):
        not_a.append(nicht(frueher(a, zeit, t_not)))
        p.append(und(frueher(a, zeit, t_and), b))
        q.append(und(frueher(not_a, zeit, t_and), c))
        alter_p = frueher(p, zeit, t_or)
        alter_q = frueher(q, zeit, t_or)
        y.append(oder(alter_p, alter_q))
        # Ein dreieingängiges OR mit derselben Verzögerung:
        # Das innere oder() ist hier nur eine logische Auswertung, kein Extra-Gatter.
        y_sicher.append(oder(oder(alter_p, alter_q), r))
    return a, not_a, p, q, y, y_sicher


if __name__ == '__main__':
    a, not_a, p, q, y, y_sicher = simuliere()
    breite = 0
    for wert in y:
        if wert == 0:
            breite = breite + 1
    print('Glitchbreite im festen Zeitmodell:', breite, 'ns')
    print('Korrigierter Ausgang durchgehend HIGH:', 0 not in y_sicher)

    # Eine Textdatei für das separate Zeichenprogramm speichern.
    ordner = Path(__file__).resolve().parent / 'results'
    ordner.mkdir(exist_ok=True)
    with (ordner / 'python_zeitverlauf.txt').open('w') as datei:
        datei.write('t_ns A not_A P Q Y Y_sicher\n')
        for zeit in range(len(a)):
            werte = [zeit, a[zeit], not_a[zeit], p[zeit], q[zeit], y[zeit], y_sicher[zeit]]
            for wert in werte:
                datei.write(str(wert) + ' ')
            datei.write('\n')
    print('Gespeichert:', ordner / 'python_zeitverlauf.txt')
