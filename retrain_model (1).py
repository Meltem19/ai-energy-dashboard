import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
import joblib
import os

# Veriyi yükle
try:
    df = pd.read_csv("data/Energy_consumption.csv")
except FileNotFoundError:
    print("Hata: 'data/Energy_consumption.csv' dosyası bulunamadı.")
    exit()

# Gerekli tarih ve zamana dayalı özellikleri oluştur
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df = df.sort_values('Timestamp')
df['Hour'] = df['Timestamp'].dt.hour
df['DayOfWeek'] = df['Timestamp'].dt.dayofweek
df['IsWeekend'] = df['DayOfWeek'].isin([5, 6]).astype(int)
df['EnergyConsumption_Lag1'] = df['EnergyConsumption'].shift(1)

# Kategorik verileri sayıya çevir
df['HVACUsage'] = df['HVACUsage'].map({'Off': 0, 'On': 1})
df['LightingUsage'] = df['LightingUsage'].map({'Off': 0, 'On': 1})
df['Holiday'] = df['Holiday'].map({'No': 0, 'Yes': 1})

df = df.dropna()  # Eksik verileri at

# Özellik ve hedef tanımı
features = [
    'Temperature', 'Humidity', 'SquareFootage', 'Occupancy',
    'HVACUsage', 'LightingUsage', 'RenewableEnergy',
    'DayOfWeek', 'Holiday', 'Hour', 'IsWeekend', 'EnergyConsumption_Lag1'
]
target = 'EnergyConsumption'

X = df[features]
y = df[target]

# Eğitim ve test ayrımı
split = int(0.8 * len(df))
X_train, X_test = X.iloc[:split], X.iloc[split:]
y_train, y_test = y.iloc[:split], y.iloc[split:]

# Modeli eğit
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Tahmin ve metrikler
y_pred = model.predict(X_test)
rmse = mean_squared_error(y_test, y_pred, squared=False)
mae = mean_absolute_error(y_test, y_pred)

# Tahminleri CSV olarak kaydet
pred_df = pd.DataFrame({
    'Actual_EnergyConsumption': y_test.values,
    'Predicted_EnergyConsumption': y_pred
})
os.makedirs("data", exist_ok=True)
pred_df.to_csv("data/energy_predictions_updated.csv", index=False)

# Modeli kaydet
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/energy_forecast_model.pkl")

print(f"Model başarıyla eğitildi. RMSE: {rmse:.2f}, MAE: {mae:.2f}")
