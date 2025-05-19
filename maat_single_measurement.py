# Maat-Based Quantum Measurement (Single Run)
# --------------------------------------------
# This script simulates a single quantum measurement of a spin system (|↑⟩ and |↓⟩)
# using the Maat value instead of standard quantum probabilities.
# Maat = (Harmony * Balance * Creativity * Connection * Respect) / EnergyFluctuation
# See model description in README_EN.md under "📊 The Maat Model"
# Author: Christof Krieg (2025)


import numpy as np
import matplotlib.pyplot as plt

# Parameter
alpha = 1/np.sqrt(2)  # Amplitude für |↑⟩
beta = 1/np.sqrt(2)   # Amplitude für |↓⟩
B = 1.0               # Magnetfeld
mu = 1.0              # Magnetisches Moment
kT = 1.0              # Temperatur
E_up = -mu * B        # Energie von |↑⟩
E_down = mu * B       # Energie von |↓⟩
E_ref = abs(E_up)     # Referenzenergie
N = 1000              # Anzahl Messungen

# Maat-Komponenten
def calculate_maat(E, alpha, beta, is_up=True):
    # Harmonie: Konstante Ordnung (vereinfacht)
    harmony = 1.0
    # Balance: exp(-ΔE/kT)
    delta_E = abs(E - E_up)  # Abstand zur minimalen Energie
    balance = np.exp(-delta_E / kT)
    # Schöpfungskraft: |α|² oder |β|²
    creation = abs(alpha)**2 if is_up else abs(beta)**2
    # Verbundenheit: Vereinfacht, |↑⟩ bevorzugt
    connection = 1.0 if is_up else 0.9
    # Respekt: 1 / (1 + ΔE/E_ref)
    respect = 1 / (1 + delta_E / E_ref)
    # Energiefluktuation: Konstante (vereinfacht)
    fluctuation = 0.1
    # Maat-Wert
    maat = (harmony * balance * creation * connection * respect) / fluctuation
    return maat

# Maat-Werte berechnen
maat_up = calculate_maat(E_up, alpha, beta, is_up=True)
maat_down = calculate_maat(E_down, alpha, beta, is_up=False)

# Normalisierte Wahrscheinlichkeiten
total_maat = maat_up + maat_down
p_up_maat = maat_up / total_maat
p_down_maat = maat_down / total_maat

# Simulation der Messungen
measurements = np.random.choice(['up', 'down'], size=N, p=[p_up_maat, p_down_maat])
up_count = np.sum(measurements == 'up')
down_count = np.sum(measurements == 'down')

# Ergebnisse
print(f"Maat-Wert |↑⟩: {maat_up:.3f}")
print(f"Maat-Wert |↓⟩: {maat_down:.3f}")
print(f"Messungen: |↑⟩ = {up_count} ({up_count/N:.2%}), |↓⟩ = {down_count} ({down_count/N:.2%})")
print(f"Standard-Quantenmechanik: |↑⟩ = {abs(alpha)**2:.2%}, |↓⟩ = {abs(beta)**2:.2%}")

# Plot
plt.bar(['|↑⟩', '|↓⟩'], [up_count/N, down_count/N], label='Maat-Werte')
plt.axhline(abs(alpha)**2, color='r', linestyle='--', label='Standard QM')
plt.ylabel('Häufigkeit')
plt.legend()
plt.show()
