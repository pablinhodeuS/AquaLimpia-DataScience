import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# CONFIGURACIÓN DE DIRECTORIO

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE_DIR)

# CARGA DE DATOS

df = pd.read_excel("dataset_set_A_aguas_residuales.xlsx")

# Conversión de fecha
df["fecha_registro"] = pd.to_datetime(df["fecha_registro"])

# CREACIÓN DE CARPETA DE REPORTES

os.makedirs("reportes", exist_ok=True)

# CÁLCULO DE EFICIENCIA DBO

df["eficiencia_remocion_DBO_%"] = (
    (df["DBO_entrada_mg_L"] - df["DBO_salida_mg_L"])
    / df["DBO_entrada_mg_L"]
) * 100

# ALERTAS OPERATIVAS

df["alerta_operativa"] = np.where(
    df["eficiencia_remocion_DBO_%"] < 85,
    "ALERTA",
    "NORMAL"
)

# RESUMEN POR PLANTA

resumen = df.groupby("planta").agg({
    "DBO_salida_mg_L": "mean",
    "eficiencia_remocion_DBO_%": "mean",
    "cumplimiento_norma": "mean",
    "energia_aeracion_kWh": "mean"
}).round(2)

print("\nResumen por planta:\n")
print(resumen)

# REPORTE ÁREA OPERACIONES

reporte_operaciones = df[[
    "fecha_registro",
    "planta",
    "caudal_entrada_m3_d",
    "DBO_entrada_mg_L",
    "DBO_salida_mg_L",
    "eficiencia_remocion_DBO_%",
    "energia_aeracion_kWh",
    "lodos_generados_kg_d",
    "alerta_operativa"
]]

reporte_operaciones.to_excel(
    "reportes/reporte_area_operaciones.xlsx",
    index=False
)

# REPORTE GESTIÓN AMBIENTAL

reporte_ambiental = df[[
    "fecha_registro",
    "planta",
    "DBO_salida_mg_L",
    "eficiencia_remocion_DBO_%",
    "cumplimiento_norma"
]]

reporte_ambiental.to_excel(
    "reportes/reporte_gestion_ambiental.xlsx",
    index=False
)

# DASHBOARD EXPLORATORIO

plt.figure(figsize=(14, 8))

# Gráfico 1: DBO salida promedio

plt.subplot(2, 2, 1)

sns.barplot(
    data=df,
    x="planta",
    y="DBO_salida_mg_L"
)

plt.axhline(
    30,
    linestyle="--",
    color="red",
    label="Límite normativo"
)

plt.title("DBO salida promedio por planta")
plt.ylabel("DBO salida (mg/L)")
plt.legend()

# Gráfico 2: Cumplimiento normativo

plt.subplot(2, 2, 2)

cumplimiento = (
    df.groupby("planta")["cumplimiento_norma"]
    .mean() * 100
)

cumplimiento.plot(kind="bar")

plt.title("Cumplimiento normativo (%)")
plt.ylabel("Cumplimiento (%)")

# Gráfico 3: Eficiencia DBO-

plt.subplot(2, 2, 3)

sns.boxplot(
    data=df,
    x="planta",
    y="eficiencia_remocion_DBO_%"
)

plt.title("Distribución eficiencia DBO")
plt.ylabel("Eficiencia (%)")

# Gráfico 4: Caudal vs eficiencia

plt.subplot(2, 2, 4)

sns.scatterplot(
    data=df,
    x="caudal_entrada_m3_d",
    y="eficiencia_remocion_DBO_%",
    hue="planta"
)

plt.title("Caudal vs eficiencia")
plt.xlabel("Caudal entrada (m3/d)")
plt.ylabel("Eficiencia (%)")

# AJUSTES FINALES

plt.tight_layout()

# Guardar dashboard
plt.savefig(
    "reportes/dashboard_aqualimpia.png",
    dpi=300
)

# Mostrar gráficos
plt.show()

print("\nAnálisis finalizado correctamente.")
print("Los archivos fueron guardados en la carpeta 'reportes'.")
