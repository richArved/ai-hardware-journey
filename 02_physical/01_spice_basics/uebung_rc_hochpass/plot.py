import os
import matplotlib.pyplot as plt
import numpy as np

# 1. Sicherstellen, dass der Ausgabeordner existiert
os.makedirs("results", exist_ok=True)

# 2. Simulationsdaten aus ngspice einlesen
# Falls deine Datei "hochpass_transient.txt" heißt, passe den Namen hier an:
dateipfad = "results/hochpass_tran.txt"
daten = np.loadtxt(dateipfad, skiprows=1)

# 3. Spalten extrahieren und Einheiten anpassen
zeit_s = daten[:, 0]  # Spalte 0: Zeit in Sekunden
vin = daten[:, 1]  # Spalte 1: Eingangsspannung in Volt
vout = daten[:, 2]  # Spalte 2: Ausgangsspannung in Volt (MIT Vorzeichen!)

# Umrechnung der Zeitachse in Millisekunden (1 s = 1000 ms)
zeit_ms = zeit_s * 1000.0

# =======================================================================
# DIAGRAMM 1: Uebersicht (gesamte 25 ms)
# =======================================================================
plt.figure(figsize=(10, 5))

# Eingang und Ausgang in unterschiedlichen Farben zeichnen
plt.plot(zeit_ms, vin, label="Eingang $V_{in}$", color="#1f77b4", linewidth=1.8)
plt.plot(
    zeit_ms, vout, label="Ausgang $V_{out}$", color="#d62728", linewidth=1.8
)

# Horizontale Nulllinie bei 0 V hervorheben
plt.axhline(
    0,
    color="black",
    linestyle="--",
    linewidth=1.2,
    alpha=0.8,
    label="0 V Referenz",
)

# Achsenbeschriftung und Titel
plt.title("RC-Hochpass: Übersicht über 25 ms", fontsize=13, fontweight="bold")
plt.xlabel("Zeit [ms]", fontsize=11)
plt.ylabel("Spannung [V]", fontsize=11)

# Gitter und Legende
plt.grid(True, linestyle=":", alpha=0.7)
plt.legend(loc="upper right", framealpha=0.95)

# Y-Achsenbereich so waehlen, dass die negativen -5 V Spitzen sichtbar sind
plt.ylim(-6, 6)
plt.xlim(0, 25)

plt.tight_layout()
plt.savefig("results/hochpass_uebersicht.png", dpi=300)
plt.close()
print("Gespeichert: results/hochpass_uebersicht.png")

# =======================================================================
# DIAGRAMM 2: Detailansicht (0,5 ms bis 5,0 ms)
# =======================================================================
# Datenbereich auf 0.5 ms bis 5.0 ms filtern
maske = (zeit_ms >= 0.5) & (zeit_ms <= 5.0)

plt.figure(figsize=(10, 5))

plt.plot(
    zeit_ms[maske],
    vin[maske],
    label="Eingang $V_{in}$",
    color="#1f77b4",
    linewidth=2.0,
)
plt.plot(
    zeit_ms[maske],
    vout[maske],
    label="Ausgang $V_{out}$",
    color="#d62728",
    linewidth=2.0,
)

# Nulllinie bei 0 V
plt.axhline(
    0,
    color="black",
    linestyle="--",
    linewidth=1.2,
    alpha=0.8,
    label="0 V Referenz",
)

# Achsenbeschriftung und Titel
plt.title(
    "RC-Hochpass: Detailansicht (0,5 ms bis 5,0 ms)",
    fontsize=13,
    fontweight="bold",
)
plt.xlabel("Zeit [ms]", fontsize=11)
plt.ylabel("Spannung [V]", fontsize=11)

# Gitter und Legende
plt.grid(True, linestyle=":", alpha=0.7)
plt.legend(loc="upper right", framealpha=0.95)

# Y-Achsenbereich fuer den ersten Entladevorgang anpassen
plt.ylim(-1, 6)
plt.xlim(0.5, 5.0)

plt.tight_layout()
plt.savefig("results/hochpass_detail.png", dpi=300)
plt.close()
print("Gespeichert: results/hochpass_detail.png")