"""Plot the educational ngspice outputs; run from the day-6 folder."""
import argparse
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('kind', choices=['inverter', 'nand'])
args = parser.parse_args()
if args.kind == 'inverter':
    data = np.loadtxt('inverter_dc.txt', skiprows=1)
    vin, vout = data[:, 1], data[:, 2]
    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.plot(vin, vout, color='black', label='Inverter')
    ax.plot(vin, vin, '--', color='0.5', label='Vout = Vin')
    idx = np.argmin(abs(vout-vin))
    ax.plot(vin[idx], vout[idx], 'ko')
    ax.annotate(f'VM ≈ {vin[idx]:.2f} V', (vin[idx], vout[idx]),
                xytext=(15, 20), textcoords='offset points')
    ax.set(xlabel='Vin (V)', ylabel='Vout (V)', title='CMOS-Inverter: DC-Sweep')
    target = Path('inverter_kennlinie.png')
else:
    data = np.loadtxt('nand2_tran.txt', skiprows=1)
    fig, axes = plt.subplots(3, 1, figsize=(7, 6), sharex=True)
    for col, (ax, label) in enumerate(zip(axes, ['A', 'B', 'Y']), 1):
        ax.plot(data[:, 0]*1e6, data[:, col], color='black')
        ax.set(ylabel=f'{label} (V)', ylim=(-0.2, 3.5))
        ax.grid(alpha=0.25)
    axes[-1].set_xlabel('Zeit (µs)')
    axes[0].set_title('CMOS-NAND: Transientenanalyse')
    target = Path('nand2_zeitverlauf.png')
if args.kind == 'inverter':
    ax.grid(alpha=0.25)
    ax.legend()
fig.tight_layout()
fig.savefig(target, dpi=180)
print(f'Gespeichert: {target}')
