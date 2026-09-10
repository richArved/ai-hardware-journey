import os
import matplotlib.pyplot as plt
import numpy as np

# 1. Sicherstellen, dass der Ausgabeordner existiert
os.makedirs("results", exist_ok=True)

# 2. Simulationsdaten einlesen
dateipfad = "results/ladezeiten_tran.txt"
daten = np.loadtxt(dateipfad, skiprows=1)

# 3. Spalten extrahieren und Einheiten anpassen
zeit_ms = daten[:, 0] * 1000.0  # Zeit in ms
vin = daten[:, 1]  # Eingang
vout_a = daten[:, 2]  # Ausgang A (1 kOhm)
vout_b = daten[:, 3]  # Ausgang B (3.3 kOhm)

# =======================================================================
# DIAGRAMM 1: Uebersicht (0 bis 45 ms)
# =======================================================================
plt.figure(figsize=(10, 5))

plt.plot(zeit_ms, vin, label="Eingang $V_{in}$", color="#1f77b4", linewidth=1.5)
plt.plot(
    zeit_ms,
    vout_a,
    label="Ausgang A ($1\\,\\mathrm{k\\Omega}$)",
    color="#d62728",
    linewidth=1.8,
)
plt.plot(
    zeit_ms,
    vout_b,
    label="Ausgang B ($3{,}3\\,\\mathrm{k\\Omega}$)",
    color="#2ca02c",
    linewidth=1.8,
)

plt.axhline(0, color="black", linestyle="--", linewidth=1.0, alpha=0.6, label="0 V Referenz")

plt.title("RC-Ladezeiten: Übersicht (0 bis 45 ms)", fontsize=13, fontweight="bold")
plt.xlabel("Zeit [ms]", fontsize=11)
plt.ylabel("Spannung [V]", fontsize=11)
plt.grid(True, linestyle=":", alpha=0.7)
plt.legend(loc="upper right", framealpha=0.95)
plt.ylim(-0.5, 5.5)
plt.xlim(0, 45)

plt.tight_layout()
plt.savefig("results/uebersicht.png", dpi=300)
plt.close()
print("Gespeichert: results/uebersicht.png")

# =======================================================================
# DIAGRAMM 2: Erstes Aufladen (0,5 ms bis 11,0 ms)
# =======================================================================
maske_lade = (zeit_ms >= 0.5) & (zeit_ms <= 11.0)

plt.figure(figsize=(10, 5))

plt.plot(
    zeit_ms[maske_lade],
    vin[maske_lade],
    label="Eingang $V_{in}$",
    color="#1f77b4",
    linewidth=1.5,
)
plt.plot(
    zeit_ms[maske_lade],
    vout_a[maske_lade],
    label="Ausgang A ($1\\,\\mathrm{k\\Omega}$)",
    color="#d62728",
    linewidth=2.0,
)
plt.plot(
    zeit_ms[maske_lade],
    vout_b[maske_lade],
    label="Ausgang B ($3{,}3\\,\\mathrm{k\\Omega}$)",
    color="#2ca02c",
    linewidth=2.0,
)

plt.axhline(0, color="black", linestyle="--", linewidth=1.0, alpha=0.6)

plt.title("RC-Ladezeiten: Erstes Aufladen (0,5 bis 11 ms)", fontsize=13, fontweight="bold")
plt.xlabel("Zeit [ms]", fontsize=11)
plt.ylabel("Spannung [V]", fontsize=11)
plt.grid(True, linestyle=":", alpha=0.7)
plt.legend(loc="center right", framealpha=0.95)
plt.ylim(-0.5, 5.5)
plt.xlim(0.5, 11.0)

plt.tight_layout()
plt.savefig("results/aufladen.png", dpi=300)
plt.close()
print("Gespeichert: results/aufladen.png")

# =======================================================================
# DIAGRAMM 3: Erstes Entladen (11,0 ms bis 21,0 ms)
# =======================================================================
maske_entlade = (zeit_ms >= 11.0) & (zeit_ms <= 21.0)

plt.figure(figsize=(10, 5))

plt.plot(
    zeit_ms[maske_entlade],
    vin[maske_entlade],
    label="Eingang $V_{in}$",
    color="#1f77b4",
    linewidth=1.5,
)
plt.plot(
    zeit_ms[maske_entlade],
    vout_a[maske_entlade],
    label="Ausgang A ($1\\,\\mathrm{k\\Omega}$)",
    color="#d62728",
    linewidth=2.0,
)
plt.plot(
    zeit_ms[maske_entlade],
    vout_b[maske_entlade],
    label="Ausgang B ($3{,}3\\,\\mathrm{k\\Omega}$)",
    color="#2ca02c",
    linewidth=2.0,
)

plt.axhline(0, color="black", linestyle="--", linewidth=1.0, alpha=0.6)

plt.title("RC-Ladezeiten: Erstes Entladen (11 bis 21 ms)", fontsize=13, fontweight="bold")
plt.xlabel("Zeit [ms]", fontsize=11)
plt.ylabel("Spannung [V]", fontsize=11)
plt.grid(True, linestyle=":", alpha=0.7)
plt.legend(loc="upper right", framealpha=0.95)
plt.ylim(-0.5, 5.5)
plt.xlim(11.0, 21.0)

plt.tight_layout()
plt.savefig("results/entladen.png", dpi=300)
plt.close()
print("Gespeichert: results/entladen.png")