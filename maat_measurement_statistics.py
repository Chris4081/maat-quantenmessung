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
B = 1.0
mu = 1.0
kT = 1.0
E_up = -mu * B
E_down = mu * B
E_ref = abs(E_up)
fluctuation = 0.1
N = 1000              # Messungen pro Durchlauf
repeats = 100         # Anzahl Wiederholungen

# Maat-Berechnung
def calculate_maat(E, alpha, beta, is_up=True):
    harmony = 1.0
    delta_E = abs(E - E_up)
    balance = np.exp(-delta_E / kT)
    creation = abs(alpha)**2 if is_up else abs(beta)**2
    connection = 1.0 if is_up else 0.9
    respect = 1 / (1 + delta_E / E_ref)
    maat = (harmony * balance * creation * connection * respect) / fluctuation
    return maat

# Wiederholte Messungssimulation
results_up = []
results_down = []

for i in range(repeats):
    maat_up = calculate_maat(E_up, alpha, beta, is_up=True)
    maat_down = calculate_maat(E_down, alpha, beta, is_up=False)
    total_maat = maat_up + maat_down
    p_up_maat = maat_up / total_maat
    p_down_maat = maat_down / total_maat

    measurements = np.random.choice(['up', 'down'], size=N, p=[p_up_maat, p_down_maat])
    up_count = np.sum(measurements == 'up')
    down_count = N - up_count

    results_up.append(up_count / N)
    results_down.append(down_count / N)

# Durchschnittswerte
mean_up = np.mean(results_up)
mean_down = np.mean(results_down)

# Ausgabe
print(f"Durchschnitt über {repeats} Wiederholungen mit je {N} Messungen:")
print(f"⟨|↑⟩⟩ = {mean_up:.2%}")
print(f"⟨|↓⟩⟩ = {mean_down:.2%}")
print(f"Standard-QM: |↑⟩ = {abs(alpha)**2:.2%}, |↓⟩ = {abs(beta)**2:.2%}")

# Plot
plt.hist(results_up, bins=20, alpha=0.7, label='|↑⟩ (Maat)')
plt.axvline(abs(alpha)**2, color='red', linestyle='--', label='|↑⟩ QM')
plt.xlabel('Häufigkeit |↑⟩')
plt.ylabel('Anzahl Wiederholungen')
plt.title('Verteilung der |↑⟩-Messungen über Wiederholungen')
plt.legend()
plt.show()
