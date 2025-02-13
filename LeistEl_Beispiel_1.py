import numpy as np
import matplotlib.pyplot as plt

# %% Parameter
a0 = 30  # Amplitude
fn = 50  # Frequenz in Hz
t = np.linspace(0, 0.02, 1001)  # Zeitvektor von 0 bis 20 ms

# %% Initialisierung des Signals
a = np.full_like(t, np.nan)  # NaN-Werte für ausgeblendete Bereiche
b = np.full_like(t, np.nan)  # NaN-Werte für ausgeblendete Bereiche

# %% Bedingungen für die Funktionen setzen
# a (Sinusfunktion) nur von 0s bis 0.005s und von 0.015s bis 0.02s sichtbar
idx_a1 = (t >= 0) & (t <= 0.005)
idx_a2 = (t >= 0.015) & (t <= 0.02)
a[idx_a1 | idx_a2] = a0 * np.sin(2 * np.pi * fn * t[idx_a1 | idx_a2])

# b (lineare Funktion) nur von 0.005s bis 0.015s sichtbar
idx_b = (t > 0.005) & (t < 0.015)
b[idx_b] = -6 * 10**3 * (t[idx_b] - 0.01)

# %% Plot Höhe reduziert
fig, ax = plt.subplots(figsize=(8, 3), num=1, clear=True, constrained_layout=True)

ax.plot(t, a, label='a (sinusförmig)', color='red')
ax.plot(t, b, label='b (linear)', color='red')
ax.grid(True)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Amplitude (V)')
ax.margins(x=0)
# ax.legend()

# Speichern als PDF
fig.savefig('TEST.pdf')

# Anzeigen des Plots
plt.show()
