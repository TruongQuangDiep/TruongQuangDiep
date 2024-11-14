#Quân

import pandas as pd

# Leer los archivos CSV
df_details = pd.read_csv("Details.csv")
df_orders = pd.read_csv("Orders.csv")

# Unir los DataFrames en base a la columna "Order ID"
df_merged = pd.merge(df_details, df_orders, on="Order ID")
     

df_merged.head(30)
# Ordenar de menor a mayor la columna "Order ID"
df_sorted = df_merged.sort_values(by="Order ID")
     

df_sorted.head(30)
     
# Guardar los datos actualizados en un nuevo archivo CSV
df_sorted.to_csv("onlinesales_sorted.csv", index=False)
     

df_online_sales = pd.read_csv("onlinesales_sorted.csv")
     

df_online_sales

# Información general del DataFrame
print("\nInformación general del DataFrame:")
print(df_online_sales.info())
# Resumen estadístico del DataFrame
print("\nResumen estadístico del DataFrame:")
print(df_online_sales.describe())
# Análisis de variables categóricas
print("\nAnálisis de variables categóricas:")
print("Categoría:")
print(df_online_sales['Category'].value_counts())
print("\nSub-Categoría:")
print(df_online_sales['Sub-Category'].value_counts())
print("\nModo de Pago:")
print(df_online_sales['PaymentMode'].value_counts())
print("\nEstado:")
print(df_online_sales['State'].value_counts())
print("\nCiudad:")
print(df_online_sales['City'].value_counts())
# Número de estados
num_states = df_online_sales['State'].nunique()
print("Número de estados:", num_states)

# Número de ciudades
num_cities = df_online_sales['City'].nunique()
print("Número de ciudades:", num_cities)
# Visualización de datos
# Visualización de la distribución de las categorías
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
df_online_sales['Category'].value_counts().plot(kind='bar')
plt.title('Distribución de Categorías')
plt.xlabel('Categoría')
plt.ylabel('Cantidad')
plt.show()



#Thiên

# Visualización de la distribución de los modos de pago
plt.figure(figsize=(10, 6))
df_online_sales['PaymentMode'].value_counts().plot(kind='bar')
plt.title('Distribución de Modos de Pago')
plt.xlabel('Modo de Pago')
plt.ylabel('Cantidad')
plt.show()
# Visualización de la distribución de las ventas por estado
plt.figure(figsize=(12, 6))
df_online_sales['State'].value_counts().plot(kind='bar')
plt.title('Distribución de Ventas por Estado')
plt.xlabel('Estado')
plt.ylabel('Cantidad de Ventas')
plt.xticks(rotation=90)
plt.show()
import matplotlib.pyplot as plt

# Variables numéricas relevantes para el análisis
numeric_variables = ['Amount', 'Profit', 'Quantity']

# Calculando medidas estadísticas básicas
statistics = df_online_sales[numeric_variables].describe()
print("Medidas estadísticas básicas:")
print(statistics)

# Calcular el rango intercuartílico (IQR)
Q1 = df_online_sales[numeric_variables].quantile(0.25)
Q3 = df_online_sales[numeric_variables].quantile(0.75)
IQR = Q3 - Q1

# Calcular límites superior e inferior para detección de outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Visualización de boxplots para detectar outliers
plt.figure(figsize=(12, 6))
for i, var in enumerate(numeric_variables):
    plt.subplot(1, len(numeric_variables), i + 1)
    plt.boxplot(df_online_sales[var])
    plt.title(var)
plt.tight_layout()
plt.show()

# Identificar y contar outliers para cada variable numérica
outliers = ((df_online_sales[numeric_variables] < lower_bound) | (df_online_sales[numeric_variables] > upper_bound)).sum()
print("\nNúmero de outliers por variable:")
print(outliers)
# Análisis de tendencias temporales
# Convertir la columna de fecha a formato datetime
df_online_sales['Order Date'] = pd.to_datetime(df_online_sales['Order Date'], format='%d-%m-%Y')
# Crear una nueva columna con el mes de cada orden
df_online_sales['Order Month'] = df_online_sales['Order Date'].dt.to_period('M')







#Duy

# Agrupar los datos por mes y sumar las ventas para cada mes
monthly_sales = df_online_sales.groupby('Order Month')['Amount'].sum()

# Graficar las tendencias temporales
plt.figure(figsize=(10, 6))
monthly_sales.plot(marker='o', color='b', linestyle='-')
plt.title('Tendencias Temporales de Ventas')
plt.xlabel('Mes')
plt.ylabel('Ventas Totales')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt

# Histograma de la variable 'Amount'
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.hist(df_online_sales['Amount'], bins=20, color='skyblue', edgecolor='black')
plt.title('Histograma de Amount')
plt.xlabel('Amount')
plt.ylabel('Frecuencia')

# Gráfico de dispersión de 'Amount' vs. índice
plt.subplot(1, 2, 2)
plt.scatter(df_online_sales.index, df_online_sales['Amount'], color='salmon', alpha=0.7)
plt.title('Gráfico de dispersión de Amount vs. Índice')
plt.xlabel('Índice')
plt.ylabel('Amount')

plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt

# Histograma de la variable 'Profit'
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.hist(df_online_sales['Profit'], bins=20, color='lightgreen', edgecolor='black')
plt.title('Histograma de Profit')
plt.xlabel('Profit')
plt.ylabel('Frecuencia')

# Gráfico de dispersión de 'Profit' vs. índice
plt.subplot(1, 2, 2)
plt.scatter(df_online_sales.index, df_online_sales['Profit'], color='orange', alpha=0.7)
plt.title('Gráfico de dispersión de Profit vs. Índice')
plt.xlabel('Índice')
plt.ylabel('Profit')

plt.tight_layout()
plt.show()





#Điệp

import matplotlib.pyplot as plt

# Histograma de la variable 'Quantity'
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.hist(df_online_sales['Quantity'], bins=20, color='lightblue', edgecolor='black')
plt.title('Histograma de Quantity')
plt.xlabel('Quantity')
plt.ylabel('Frecuencia')

# Gráfico de dispersión de 'Quantity' vs. índice
plt.subplot(1, 2, 2)
plt.scatter(df_online_sales.index, df_online_sales['Quantity'], color='purple', alpha=0.7)
plt.title('Gráfico de dispersión de Quantity vs. Índice')
plt.xlabel('Índice')
plt.ylabel('Quantity')

plt.tight_layout()
plt.show()

# Rentabilidad por categoría de producto
category_profit = df_online_sales.groupby('Category')['Profit'].sum()  # Agrupamos por categoría y sumamos las ganancias
category_profit.plot(kind='bar', color='skyblue')  # Creamos un gráfico de barras para la rentabilidad por categoría
plt.title('Rentabilidad por Categoría de Producto')  # Agregamos un título al gráfico
plt.xlabel('Categoría')  # Etiqueta del eje x
plt.ylabel('Rentabilidad Total')  # Etiqueta del eje y
plt.xticks(rotation=45, ha='right')  # Rotamos las etiquetas del eje x para mejor visualización
plt.show()  # Mostramos el gráfico
# Rentabilidad por subcategoría
subcategory_profit = df_online_sales.groupby('Sub-Category')['Profit'].sum()  # Agrupamos por subcategoría y sumamos las ganancias
subcategory_profit.plot(kind='bar', color='lightgreen')  # Creamos un gráfico de barras para la rentabilidad por subcategoría
plt.title('Rentabilidad por Subcategoría de Producto')  # Agregamos un título al gráfico
plt.xlabel('Subcategoría')  # Etiqueta del eje x
plt.ylabel('Rentabilidad Total')  # Etiqueta del eje y
plt.xticks(rotation=45, ha='right')  # Rotamos las etiquetas del eje x para mejor visualización
plt.show()  # Mostramos el gráfico
# Rentabilidad por método de pago
payment_profit = df_online_sales.groupby('PaymentMode')['Profit'].sum()  # Agrupamos por método de pago y sumamos las ganancias
payment_profit.plot(kind='bar', color='salmon')  # Creamos un gráfico de barras para la rentabilidad por método de pago
plt.title('Rentabilidad por Método de Pago')  # Agregamos un título al gráfico
plt.xlabel('Método de Pago')  # Etiqueta del eje x
plt.ylabel('Rentabilidad Total')  # Etiqueta del eje y
plt.xticks(rotation=45, ha='right')  # Rotamos las etiquetas del eje x para mejor visualización
plt.show()  # Mostramos el gráfico
# Segmentación de clientes por ciudad
customer_segmentation = df_online_sales.groupby('City')

# Analizar el comportamiento de compra de cada segmento
for city, data in customer_segmentation:
    print(f"Comportamiento de compra en {city}:")
    print("Número de compras:", data.shape[0])  # Número de compras realizadas en la ciudad
    print("Gasto promedio por compra:", data['Amount'].mean())  # Gasto promedio por compra en la ciudad
    print("Productos más comprados:")
    print(data['Sub-Category'].value_counts().head(3))  # Subcategorías más compradas en la ciudad
    print()
# Generar grafico que  muestre ventas totales, rentabilidad total, ventas rea.izadas y clientes totales








#Phú

# Calcular las métricas
total_sales = df_online_sales['Amount'].sum()
total_profit = df_online_sales['Profit'].sum()
total_customers = df_online_sales['CustomerName'].nunique()
total_orders = len(df_online_sales)

# Crear el tablero con subgráficos
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Graficar las ventas totales
axes[0, 0].bar('Ventas Totales', total_sales, color='blue')
axes[0, 0].text('Ventas Totales', total_sales, str(total_sales), ha='center', va='bottom', fontsize=10)
axes[0, 0].set_ylabel('Cantidad')
axes[0, 0].set_title('Ventas Totales')

# Graficar la rentabilidad total
axes[0, 1].bar('Rentabilidad Total', total_profit, color='green')
axes[0, 1].text('Rentabilidad Total', total_profit, str(total_profit), ha='center', va='bottom', fontsize=10)
axes[0, 1].set_ylabel('Cantidad')
axes[0, 1].set_title('Rentabilidad Total')

# Graficar el número total de clientes
axes[1, 0].bar('Clientes Totales', total_customers, color='orange')
axes[1, 0].text('Clientes Totales', total_customers, str(total_customers), ha='center', va='bottom', fontsize=10)
axes[1, 0].set_ylabel('Cantidad')
axes[1, 0].set_title('Clientes Totales')

# Graficar el número total de ventas realizadas
axes[1, 1].bar('Ventas Realizadas', total_orders, color='red')
axes[1, 1].text('Ventas Realizadas', total_orders, str(total_orders), ha='center', va='bottom', fontsize=10)
axes[1, 1].set_ylabel('Cantidad')
axes[1, 1].set_title('Ventas Realizadas')

# Ajustar el espacio entre los subgráficos
plt.tight_layout()

# Mostrar el tablero
plt.show()
# Agrupar por ciudad y método de pago, contar el número de transacciones y encontrar el método de pago más común
city_payment_counts = df_online_sales.groupby(['City', 'PaymentMode']).size().reset_index(name='Count')
city_most_common_payment = city_payment_counts.loc[city_payment_counts.groupby('City')['Count'].idxmax()]

# Mostrar los resultados
print(city_most_common_payment)
# Filtrar el DataFrame para incluir solo transacciones con tarjeta de crédito
credit_card_transactions = df_online_sales[df_online_sales['PaymentMode'] == 'Credit Card']

# Contar el número de transacciones por ciudad
city_credit_card_counts = credit_card_transactions['City'].value_counts()

# Mostrar los resultados
print(city_credit_card_counts)
# Filtrar el DataFrame para incluir solo transacciones de la categoría "Clothing"
clothing_transactions = df_online_sales[df_online_sales['Category'] == 'Clothing']

# Contar el número de veces que se utilizó cada método de pago
payment_mode_counts = clothing_transactions['PaymentMode'].value_counts()

# Mostrar los resultados
print(payment_mode_counts)
import pandas as pd
import matplotlib.pyplot as plt

# Asegúrate de tener las fechas en formato de fecha, si no están, conviértelas usando pd.to_datetime()

# Agrupar por mes y categoría y contar las ventas
sales_by_month_category = df_online_sales.groupby([df_online_sales['Order Date'].dt.month, 'Category']).size().unstack()

# Gráfico de líneas para cada categoría
sales_by_month_category.plot(kind='line', marker='o', figsize=(10, 6))
plt.title('Cantidad de compras por categoría y mes')
plt.xlabel('Mes')
plt.ylabel('Cantidad de compras')
plt.xticks(range(1, 13), ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'])
plt.legend(title='Categoría')
plt.grid(True)
plt.show()
df_online_sales.head(10)