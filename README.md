# Proyecto 3 – Análisis y Diseño de Algoritmos

### Algoritmos Move-To-Front (MTF) e Improved Move-To-Front (IMTF)

Este proyecto implementa y analiza el algoritmo Move-To-Front (MTF) y su versión optimizada IMTF (Improved Move-To-Front). Ambos algoritmos están diseñados para autoorganizar listas en función de los patrones de acceso, buscando reducir el costo total de búsqueda.

---

## Contenido del Repositorio

Proyecto3-ADA/
├── mtf.py # Algoritmo MTF clásico y casos de prueba  
├── imtf.py # Algoritmo IMTF con mirada hacia adelante  
└── README.md # Documentación del proyecto

---

## Descripción del Proyecto

El objetivo del proyecto es comparar diferentes estrategias para listas autoorganizadas. Se evalúan los costos de acceso en diversas secuencias con:

- **MTF (Move-To-Front):** mueve al frente el elemento accedido.
- **IMTF (Improved MTF):** solo mueve al frente el elemento si aparece dentro de los siguientes `i-1` elementos.\*\*

Los casos evaluados incluyen:

- Secuencia ordenada
- Secuencia alternante
- Mejor caso posible
- Peor caso posible
- Repetición de un solo elemento

---

## 🧠 Archivos y su Funcionalidad

### `mtf.py`

Este archivo implementa:

- El algoritmo **MTF clásico**.
- Pruebas de todos los incisos descritos en el reporte (1 al 5).
- Cálculo del costo de acceso por posición y movimiento del elemento al frente.

### `imtf.py`

Este archivo contiene:

- El algoritmo IMTF, que optimiza el comportamiento del MTF.
- Revisión de la ventana de mirada hacia adelante para decidir si conviene reordenar.
- Comparaciones con las mismas secuencias del archivo `mtf.py`.

---

## Cómo ejecutar

### Requisitos

- Python 3.x

### Ejecución

Desde una terminal, navega al directorio del proyecto y ejecuta:

```bash
python mtf.py

python imtf.py
```

Cada script imprime:

- La configuración inicial y final de la lista
- Costos individuales por solicitud
- El costo total acumulado

Resultados esperados
Ambos algoritmos son ejecutados sobre las mismas secuencias para comparar su rendimiento. En general, IMTF logra una mejor eficiencia en escenarios donde los elementos no se repiten inmediatamente, evitando movimientos innecesarios.
