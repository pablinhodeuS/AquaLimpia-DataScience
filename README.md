# Proyecto de Ciencia de Datos — AquaLimpia S.A.

## Análisis de Desempeño de Plantas de Tratamiento de Aguas Residuales

---

## Descripción del Proyecto

Este proyecto desarrolla un análisis exploratorio de datos aplicado al monitoreo operacional y ambiental de plantas de tratamiento de aguas residuales pertenecientes a AquaLimpia S.A.

El objetivo principal es identificar patrones de desempeño, evaluar el cumplimiento normativo asociado a la DBO del efluente tratado y generar información útil para distintas áreas de la organización mediante Python y herramientas de análisis de datos.

---

## Objetivos

- Analizar el comportamiento operacional de las plantas de tratamiento.
- Evaluar el cumplimiento normativo de los efluentes.
- Calcular la eficiencia de remoción de DBO.
- Detectar alertas operativas.
- Generar reportes automatizados para distintas áreas.
- Construir un dashboard exploratorio reproducible.

---

## Dataset Utilizado

Archivo:

```text
dataset_set_A_aguas_residuales.xlsx
```

El dataset contiene información operacional y ambiental de tres plantas de tratamiento durante el período julio–octubre 2025.

### Variables principales

| Variable | Descripción |
|---|---|
| fecha_registro | Fecha del registro |
| planta | Planta de tratamiento |
| caudal_entrada_m3_d | Caudal de entrada |
| DBO_entrada_mg_L | DBO de entrada |
| DBO_salida_mg_L | DBO de salida |
| energia_aeracion_kWh | Consumo energético |
| lodos_generados_kg_d | Lodos generados |
| cumplimiento_norma | Cumplimiento normativo |

---

## Tecnologías Utilizadas

- Python 3
- Pandas
- NumPy
- Matplotlib
- Seaborn
- OpenPyXL

---

## Estructura del Proyecto

```text
AquaLimpia-DataScience/
├── README.md
├── LICENSE
├── .gitignore
├── dataset_set_A_aguas_residuales.xlsx
├── scripts/
│   └── funciones_analisis.py
├── reportes/
│   ├── reporte_area_operaciones.xlsx
│   ├── reporte_gestion_ambiental.xlsx
│   └── dashboard_aqualimpia.png
```

---

## Funcionalidades del Proyecto

El script desarrollado permite:

- Cargar y procesar datos desde Excel.
- Calcular eficiencia de remoción de DBO.
- Detectar alertas operativas.
- Generar reportes automatizados en Excel.
- Construir dashboard exploratorio.
- Comparar desempeño entre plantas.

---

## Indicadores Analizados

### Eficiencia de remoción de DBO

```python
((DBO_entrada_mg_L - DBO_salida_mg_L) / DBO_entrada_mg_L) * 100
```

### Indicadores principales

- DBO de salida promedio
- Eficiencia promedio
- Cumplimiento normativo
- Consumo energético
- Relación caudal/eficiencia
- Alertas operativas

---

## Resultados Principales

| Planta | DBO Salida | Eficiencia | Cumplimiento |
|---|---|---|---|
| Planta Centro | 35.90 mg/L | 87.51% | 23% |
| Planta Norte | 36.56 mg/L | 86.65% | 17% |
| Planta Sur | 36.06 mg/L | 87.10% | 30% |

### Hallazgos relevantes

- La tasa global de cumplimiento fue de 22.5%.
- La Planta Norte presentó el menor desempeño.
- Se detectaron múltiples alertas operativas.
- Los niveles promedio de DBO superan el límite normativo de 30 mg/L.

---

## Dashboard Exploratorio

El proyecto genera automáticamente un dashboard con:

- DBO promedio por planta
- Cumplimiento normativo
- Distribución de eficiencia
- Relación caudal vs eficiencia

Archivo generado:

```text
reportes/dashboard_aqualimpia.png
```

---

## Reportes Generados

### Área de Operaciones

Archivo:

```text
reportes/reporte_area_operaciones.xlsx
```

Incluye:
- Fecha
- Planta
- Caudal
- DBO entrada/salida
- Eficiencia
- Energía
- Lodos
- Alertas

### Área de Gestión Ambiental

Archivo:

```text
reportes/reporte_gestion_ambiental.xlsx
```

Incluye:
- Fecha
- Planta
- DBO salida
- Eficiencia
- Cumplimiento normativo

---

## Calidad de los Datos

### Resultados del análisis

| Indicador | Resultado |
|---|---|
| Valores nulos | 0 |
| Duplicados | 0 |
| Registros analizados | 200 |

### Limitaciones

- Período acotado de análisis.
- No existen variables meteorológicas.
- No se incorpora tipo de afluente.
- No se consideran mantenciones operacionales.

---

## Ejecución del Proyecto

### Instalar librerías

```bash
pip install pandas numpy matplotlib seaborn openpyxl
```

### Ejecutar script

```bash
python scripts/funciones_analisis.py
```

---

## Consideraciones Éticas

- Los resultados se utilizan como apoyo a la toma de decisiones.
- El análisis no reemplaza evaluaciones técnicas especializadas.
- Se busca transparencia y reproducibilidad del análisis.

---

## Autor

Pablo Matías Cancino Orellana  
Proyecto académico — Ciencia de Datos  
Instituto Profesional IACC — 2026

---

## Referencias

- McKinney, W. (2022). *Python para análisis de datos*. O'Reilly Media.
- IACC. (2026). *Aplicación práctica y reflexión ética*. Ciencia de Datos.
- Pandas Development Team. https://pandas.pydata.org/
- Seaborn Documentation. https://seaborn.pydata.org/
