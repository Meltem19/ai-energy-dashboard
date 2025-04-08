import pandas as pd
import matplotlib.pyplot as plt

# CSV dosyasını oku
try:
    df = pd.read_csv("data/energy_predictions_updated.csv")
except FileNotFoundError:
    print("Hata: 'data/energy_predictions_updated.csv' dosyası bulunamadı.")
    exit()

# Grafik çizimi
plt.figure(figsize=(12, 6))
plt.plot(df['Actual_EnergyConsumption'], label='Gerçek Tüketim', linewidth=2)
plt.plot(df['Predicted_EnergyConsumption'], label='Tahmin Edilen Tüketim', linestyle='--')
plt.title('Enerji Tüketimi: Gerçek vs Tahmin')
plt.xlabel('Zaman')
plt.ylabel('kWh')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
