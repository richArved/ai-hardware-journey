import matplotlib.pyplot as plt
import numpy as np

# Daten laden: Spalte 0 = Vin, Spalte 1 = Vled, Spalte 2 = -I(V1)
data = np.loadtxt("results/led_dc.txt")
vin = data[:, 0]
vled = data[:, 1]
# Falls der Strom negativ exportiert wurde, Vorzeichen korrigieren und in mA umrechnen:
current_ma = np.abs(data[:, 2]) * 1e3

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5))

# 1. Kennlinie: LED-Spannung über Versorgungsspannung
ax1.plot(vin, vled, color="#d62728", lw=2, label="$V_{\mathrm{led}}$")
ax1.axhline(2.18, color="gray", linestyle="--", alpha=0.7, label="Schwellenspannung (~2.18 V)")
ax1.set_title("LED-Spannung vs. Versorgungsspannung")
ax1.set_xlabel("Versorgungsspannung $V_{\mathrm{in}}$ [V]")
ax1.set_ylabel("Spannung an LED [V]")
ax1.grid(True, linestyle=":", alpha=0.6)
ax1.legend()

# 2. Kennlinie: Strom über Versorgungsspannung
ax2.plot(vin, current_ma, color="#1f77b4", lw=2, label="LED-Strom")
ax2.set_title("LED-Strom vs. Versorgungsspannung")
ax2.set_xlabel("Versorgungsspannung $V_{\mathrm{in}}$ [V]")
ax2.set_ylabel("Strom [mA]")
ax2.grid(True, linestyle=":", alpha=0.6)
ax2.legend()

plt.tight_layout()
plt.show()