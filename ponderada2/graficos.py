import pandas as pd
import matplotlib.pyplot as plt

# ==============================
# 1️⃣ Definindo os dados
# ==============================
data = [
    [5, 4.43, 0.57],
    [1607, 4.26, 0.74],
    [2010, 4.09, 0.91],
    [2412, 3.93, 1.07],
    [2813, 3.77, 1.23],
    [3216, 3.63, 1.37],
    [3618, 3.48, 1.52],
    [4021, 3.34, 1.66],
    [4423, 3.21, 1.79],
    [4825, 3.08, 1.92],
    [5227, 2.97, 2.03],
    [5629, 2.85, 2.15],
    [6032, 2.74, 2.26],
    [6434, 2.63, 2.37],
    [6836, 2.52, 2.48],
    [7238, 2.42, 2.58],
    [7641, 2.33, 2.67],
    [8043, 2.24, 2.76],
    [8445, 2.15, 2.85],
    [8847, 2.06, 2.94],
    [9249, 1.98, 3.02],
    [9652, 1.91, 3.09],
    [0, 5.00, 0.00],
    [401, 4.80, 0.20],
    [803, 4.61, 0.39],
    [1205, 4.43, 0.57],
    [1607, 4.26, 0.74],
    [2010, 4.09, 0.91],
    [2412, 3.93, 1.07],
    [2813, 3.77, 1.23],
    [3216, 3.63, 1.37],
    [3618, 3.48, 1.52],
    [4021, 3.34, 1.66],
    [4423, 3.21, 1.79],
    [4825, 3.08, 1.92],
    [5227, 2.97, 2.03],
    [5629, 2.85, 2.15],
    [6032, 2.74, 2.26],
    [6434, 2.63, 2.37],
    [6836, 2.52, 2.48],
    [7238, 2.42, 2.58],
    [7641, 2.33, 2.67],
    [8043, 2.24, 2.76],
    [8445, 2.15, 2.85],
    [8847, 2.06, 2.94],
    [9249, 1.98, 3.02],
    [9652, 1.91, 3.09],
    [10054, 1.83, 3.17],
    [10457, 1.76, 3.24],
    [10859, 1.69, 3.31],
    [11260, 1.62, 3.38],
    [11663, 1.56, 3.44],
    [12065, 1.50, 3.50],
    [12468, 1.44, 3.56],
    [12870, 1.38, 3.62],
    [13273, 1.32, 3.68],
    [13675, 1.28, 3.72],
    [14077, 1.22, 3.78],
    [14480, 1.17, 3.83],
    [14882, 1.13, 3.87],
    [15285, 1.09, 3.91],
    [15686, 1.04, 3.96]
]

# Cria o DataFrame
df = pd.DataFrame(data, columns=["Tempo (ms)", "Vc (V)", "Vr (V)"])

# ==============================
# 2️⃣ Gráfico 1 - Vc vs Tempo
# ==============================
plt.figure(figsize=(8, 5))
plt.plot(df["Tempo (ms)"], df["Vc (V)"], color="blue", linewidth=2)
plt.title("Gráfico 1 - Tensão no Capacitor (Vc) vs Tempo")
plt.xlabel("Tempo (ms)")
plt.ylabel("Tensão no Capacitor (V)")
plt.grid(True)
plt.show()

# ==============================
# 3️⃣ Gráfico 2 - Vr vs Tempo
# ==============================
plt.figure(figsize=(8, 5))
plt.plot(df["Tempo (ms)"], df["Vr (V)"], color="red", linewidth=2)
plt.title("Gráfico 2 - Tensão no Resistor (Vr) vs Tempo")
plt.xlabel("Tempo (ms)")
plt.ylabel("Tensão no Resistor (V)")
plt.grid(True)
plt.show()

# ==============================
# 4️⃣ Gráfico 3 - Comparativo Vc e Vr
# ==============================
plt.figure(figsize=(8, 5))
plt.plot(df["Tempo (ms)"], df["Vc (V)"], label="Vc (V)", color="blue", linewidth=2)
plt.plot(df["Tempo (ms)"], df["Vr (V)"], label="Vr (V)", color="red", linewidth=2)
plt.title("Gráfico 3 - Comparativo: Vc e Vr ao longo do tempo")
plt.xlabel("Tempo (ms)")
plt.ylabel("Tensão (V)")
plt.legend()
plt.grid(True)
plt.show()
