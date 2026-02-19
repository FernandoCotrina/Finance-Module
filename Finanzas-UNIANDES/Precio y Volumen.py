#API DATOS
import yfinance as yf

#Manejo de Tablas de Datos
import pandas as pd

#Manejo de Gráficos
import matplotlib.pyplot as plt

# Descargar Datos
start_date = "2019-01-01"
end_date = "2021-01-01"

goog_data = yf.download('GOOG', start=start_date, end=end_date)
msft_data = yf.download('MSFT', start=start_date, end=end_date)

#Guardar en CSV
goog_data.to_csv('GOOG.csv')
msft_data.to_csv('MSFT.csv')

# Estadísticas Descriptivas
stats_goog = goog_data.describe()
stats_msft = msft_data.describe()


# Graficar el volumen diario de transacciones para MSFT
plt.figure(figsize=(12, 6))
plt.plot(msft_data.index, msft_data["Volume"], label="MSFT Volume", color="blue")
plt.title("Volume of Daily Transactions for Microsoft (MSFT)")
plt.xlabel("Date")
plt.ylabel("Volume")
plt.legend()
plt.grid(True)
plt.show()
