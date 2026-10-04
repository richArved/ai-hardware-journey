"""Fertiges Hilfsmittel. Standard: eigene Funktionen; --referenz: Referenzmodell."""
import argparse
import importlib
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--referenz', action='store_true')
    args = parser.parse_args()
    model = importlib.import_module('delay_referenz' if args.referenz else 'delay_lernen')
    widths = list(range(4, 65))
    try:
        ripple = [model.delay_ripple(n, 2.0) for n in widths]
        prefix = [model.delay_cla(n, 1.0) for n in widths]
    except NotImplementedError as error:
        raise SystemExit(str(error))
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        raise SystemExit('Matplotlib fehlt: python3 -m pip install matplotlib (in deiner venv).')
    fig, ax = plt.subplots(figsize=(8, 4.8))
    ax.plot(widths, ripple, 'k-', label='Ripple: N * 2 ns')
    ax.step(widths, prefix, where='pre', color='black', linestyle='--',
            label='Hierarchisches Lookahead/Prefix: (ceil(log2 N) + 2) * 1 ns')
    ax.set(xlabel='Bitbreite N', ylabel='Modellverzoegerung (ns)',
           title='Lehrmodelle: lineares und logarithmisches Wachstum')
    ax.set_xlim(4, 64)
    ax.grid(True, color='0.85')
    ax.legend(fontsize=8)
    fig.tight_layout()
    folder = Path(__file__).resolve().parent / 'results'
    folder.mkdir(exist_ok=True)
    filename = 'delay_referenz.png' if args.referenz else 'delay_eigene_funktionen.png'
    fig.savefig(folder / filename, dpi=180)
    print(folder / filename)


if __name__ == '__main__':
    main()
