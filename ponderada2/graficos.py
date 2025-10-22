import pandas as pd
import matplotlib.pyplot as plt

# ==============================
# 1️⃣ Novos dados
# ==============================
data = [
    [57752, 5.00, 0.00],
    [58153, 5.00, 0.00],
    [58554, 5.00, 0.00],
    [58955, 5.00, 0.00],
    [59357, 5.00, 0.00],
    [59757, 5.00, 0.00],
    [60158, 5.00, 0.00],
    [60560, 5.00, 0.00],
    [60960, 5.00, 0.00],
    [61362, 5.00, 0.00],
    [61763, 5.00, 0.00],
    [62163, 5.00, 0.00],
    [62565, 5.00, 0.00],
    [62966, 4.99, 0.01],
    [63367, 5.00, 0.00],
    [63768, 5.00, 0.00],
    [64169, 5.00, 0.00]
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
