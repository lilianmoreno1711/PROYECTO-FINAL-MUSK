# PROYECTO-FINAL-MUSK

# Análisis Avanzado de Clientes y Ventas

Proyecto final de análisis de clientes y ventas desarrollado en Python.

El proyecto carga información de clientes desde un archivo JSON y datos de ventas desde un archivo CSV. Posteriormente, cruza ambos conjuntos de datos, realiza diferentes cálculos y genera un reporte final en formato JSON.

## Funcionalidades

El proyecto realiza 10 cálculos relacionados con clientes y ventas:

- Total de clientes.
- Total de ventas.
- Ingresos totales.
- Ingresos por cliente.
- Número de ventas por cliente.
- Promedio de venta por cliente.
- Cliente con mayor gasto por país.
- Total de ventas por categoría.
- Cliente con más ventas dentro de una categoría.
- Clientes con un gasto superior a un umbral establecido.

También realiza un análisis de las ventas mensuales utilizando Pandas.

## Tecnologías utilizadas

- Python
- Pandas
- JSON
- CSV
- Programación Orientada a Objetos (POO)
- Programación funcional
- Bucles y condicionales
- Pytest
- Git
- GitHub Actions

## Estructura del proyecto

```text
PROYECTO-FINAL-MUSK/
│
├── data/
│   ├── clients.json
│   └── sales.csv
│
├── src/
│   ├── client.py
│   ├── sale.py
│   ├── client_collection.py
│   ├── sales_collection.py
│   ├── functional_utils.py
│   └── analyze.py
│
├── tests/
│   ├── test_clients.py
│   ├── test_sales.py
│   ├── test_collections.py
│   ├── test_calculations.py
│   └── test_10_calculos.py
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── requirements.txt
└── README.md