"""python3 pruefe_delay.py [--referenz] -- prueft nur das Zeitmodell."""
import argparse
import importlib
import math


def pruefe(modul):
    # Fest vorgegebene Erwartungswerte, einschliesslich Nicht-Zweierpotenzen.
    cases = [(1, 2.0, 1.0, 2.0, 2.0),
             (4, 2.0, 1.0, 8.0, 4.0),
             (12, 2.0, 1.0, 24.0, 6.0),
             (32, 2.0, 1.0, 64.0, 7.0),
             (64, 2.0, 1.0, 128.0, 8.0),
             (5, 0.3, 0.2, 1.5, 1.0)]
    for n, fa, stufe, ripple, cla in cases:
        for name, zeit, expected in [('delay_ripple', fa, ripple), ('delay_cla', stufe, cla)]:
            actual = getattr(modul, name)(n, zeit)
            if actual is None or not math.isclose(actual, expected, rel_tol=1e-9):
                raise AssertionError(f"{name}({n}, {zeit}): erwartet {expected}, erhalten {actual}")
    print('12 Funktionspruefungen bestanden. Keine Schaltungspruefung.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--referenz', action='store_true')
    args = parser.parse_args()
    try:
        pruefe(importlib.import_module('delay_referenz' if args.referenz else 'delay_lernen'))
    except (NotImplementedError, AssertionError) as error:
        raise SystemExit(str(error))
