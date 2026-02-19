# Funciones aritméticas adicionales
import numpy as np

# Lectura de Datos y Manejo de Data Sets
import pandas as pd

# Datos
import yfinance as yf

# Gráficos
import matplotlib.pyplot as plt

# Descargamos la Data    
start_date = "2019-01-01"
end_date = "2021-01-01"

aapl_data = yf.download('AAPL', start=start_date, end=end_date)
aapl_data

# Elimina el nivel superior 'Ticker' en las columnas
aapl_data.columns = aapl_data.columns.droplevel(1)

# Calcular el precio de cierre anterior
aapl_data['Close t-1'] = aapl_data['Close'].shift(1)

# Retornos aritméticos
aapl_data['Returns'] = (aapl_data['Close'] - aapl_data['Close t-1'])/aapl_data['Close t-1']
aapl_data

# Retornos logarítmicos
aapl_data['Log Returns'] = np.log(aapl_data['Close']/aapl_data['Close t-1'])
aapl_data

# Graficar los Retornos Logarítmicos
plt.figure(figsize=(15,8))
plt.plot(aapl_data['Log Returns'], color='blue')
plt.title('Historic Returns of Apple')
plt.xlabel('Date')
plt.ylabel('Value')
plt.show

# Volatibilidad Diaria
vol_d = np.std(aapl_data['Log Returns'])
vol_d

# Volatiblidad Anual
vol_a = vol_d*np.sqrt(252)
