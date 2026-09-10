"""Aus dem Ordner loesung: ngspice -b ladezeiten.cir, dann python plot.py."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
p = Path(__file__).resolve().parent / 'results'
report = []
for variant, cb in [('grundaufgabe', 1e-6), ('zusatzversuch', 2e-6)]:
    t, vin, a, b = np.loadtxt(p / f'{variant}.txt', skiprows=1).T
    for name, limits in [('uebersicht', (0,45)), ('aufladen',(0.5,11)), ('entladen',(11,21))]:
        fig, ax = plt.subplots(figsize=(10,5), layout='constrained')
        ax.plot(t*1000, vin, label='Eingang', color='gray')
        ax.plot(t*1000, a, label='A: 1 kΩ, 1 µF')
        ax.plot(t*1000, b, label=f'B: 3,3 kΩ, {cb*1e6:g} µF')
        if name == 'aufladen':
            ax.axhline(5*(1-np.exp(-1)), ls=':', color='black', label='63,2 % von 5 V')
        if name == 'entladen':
            for values, color in [(a,'C0'), (b,'C1')]:
                ax.axhline(np.interp(.011002,t,values)/np.e, ls=':', color=color)
        ax.set(xlabel='Zeit (ms)', ylabel='Spannung (V)', xlim=limits, ylim=(-.2,5.4), title=f'{variant}: {name}')
        ax.grid(); ax.legend()
        fig.savefig(p / f'{variant}_{name}.png', dpi=160)
        plt.close(fig)
    for label, values, tau in [('A',a,.001),('B',b,3300*cb)]:
        rising = (t>=.001)&(t<=.011)
        cross = np.interp(5*(1-np.exp(-1)), values[rising], t[rising])
        # Nach Ende der endlichen fallenden Flanke messen, wenn Vin exakt null ist.
        start=.011002
        vstart=np.interp(start,t,values)
        falling=(t>=start)&(t<=.021)
        fallcross=np.interp(vstart/np.e,values[falling][::-1],t[falling][::-1])
        measured_rise=cross-.001
        measured_fall=fallcross-start
        assert abs(measured_rise/tau-1)<.01
        assert abs(measured_fall/tau-1)<.01
        report.append(f'{variant}, {label}: Theorie {tau*1000:.4f} ms; Laden {measured_rise*1000:.4f} ms; Entladen {measured_fall*1000:.4f} ms; Ustart {vstart:.6f} V; 36,8%-Pegel {vstart/np.e:.6f} V')
(p/'vergleich.txt').write_text('\n'.join(report)+'\n')
print('\n'.join(report))
