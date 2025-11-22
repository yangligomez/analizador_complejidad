# 🧠 Analizador de Complejidad Asintótica con Red Neuronal

Un analizador inteligente que utiliza una **red neuronal de 500 épocas** para detectar la notación asintótica (Big O) de algoritmos escritos en **JavaScript**.

## 📋 Características

✅ **Red Neuronal Avanzada**
- 500 épocas de entrenamiento
- Arquitectura: 128 → 64 → 32 neuronas
- Capas ocultas optimizadas para análisis de código
- Normalización de características con StandardScaler

✅ **Análisis Inteligente**
- Extrae 20 características diferentes del código
- Detecta bucles, recursión, operaciones de array
- Calcula indentación y complejidad anidada
- Identifica patrones de algoritmos comunes

✅ **Interfaz Gráfica Moderna**
- Editor de código con colores oscuros
- Barra de progreso de confianza
- Carga archivos JavaScript
- Explicaciones detalladas de cada complejidad

✅ **Soporta Todas las Complejidades Comunes**
- **O(1)** - Tiempo constante
- **O(log n)** - Búsqueda binaria
- **O(n)** - Lineal
- **O(n log n)** - Merge sort
- **O(n²)** - Bubble sort
- **O(n³)** - Matrices 3D
- **O(2ⁿ)** - Fibonacci recursivo

## 🚀 Instalación

### 1. Instalar Dependencias

```bash
python setup_requirements.py
```

O manualmente:

```bash
pip install numpy scikit-learn
```

### 2. Entrenar el Modelo (Primera ejecución)

La primera vez que ejecutes la interfaz gráfica, se entrenará automáticamente el modelo con 500 épocas. Esto puede tomar 1-2 minutos.

## 📖 Uso

### Opción 1: Interfaz Gráfica (Recomendado)

```bash
python gui_analyzer.py
```

**Pasos:**
1. Pega tu código JavaScript en el editor izquierdo
2. O carga un archivo .js usando el botón "📂 Cargar desde archivo"
3. Haz clic en "🔍 Analizar Complejidad"
4. Verás la notación O resultante y el porcentaje de confianza

### Opción 2: Uso por Línea de Comandos

```python
from neural_complexity_analyzer import NeuralNetworkComplexityAnalyzer

# Crear analizador
analyzer = NeuralNetworkComplexityAnalyzer(epochs=500)

# Entrenar (primera vez)
analyzer.train()

# Analizar código
code = """
function search(arr, target) {
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === target) return i;
    }
    return -1;
}
"""

complexity, confidence = analyzer.predict(code)
print(f"Complejidad: {complexity}")
print(f"Confianza: {confidence:.2%}")
```

## 📊 Arquitectura de la Red Neuronal

```
Entrada (20 características)
    ↓
Capa Oculta 1 (128 neuronas) - ReLU
    ↓
Capa Oculta 2 (64 neuronas) - ReLU
    ↓
Capa Oculta 3 (32 neuronas) - ReLU
    ↓
Salida (1 neurona) - Mapeo a complejidad
```

**Configuración:**
- **Épocas**: 500
- **Función de Activación**: ReLU
- **Optimizador**: Adam
- **Tasa de Aprendizaje**: 0.001
- **Regularización (Alpha)**: 0.0001

## 🔍 Características Analizadas

El modelo extrae automáticamente 20 características del código:

1. Número de líneas
2. Bucles `for`
3. Bucles `while`
4. Nivel de indentación
5. Definiciones de funciones
6. Operaciones de array (map, filter, etc.)
7. Búsquedas (indexOf, includes)
8. Ordenamientos (sort, reverse)
9. Profundidad máxima de anidación
10. Variables declaradas
11. Condicionales `if`
12. `switch` statements
13. Longitud total del código
14. Número de funciones
15. Métodos de string
16. Operaciones de objeto
17. Operaciones JSON
18. Try-catch blocks
19. Promesas/async
20. Factor multiplicador de bucles anidados

## 📁 Archivos Generados

- **`neural_complexity_analyzer.py`** - Motor de análisis y red neuronal
- **`gui_analyzer.py`** - Interfaz gráfica Tkinter
- **`setup_requirements.py`** - Script de instalación
- **`complexity_model.pkl`** - Modelo entrenado (se genera automáticamente)

## 🎯 Ejemplos

### Ejemplo 1: O(1)
```javascript
function getFirst(arr) {
    return arr[0];
}
```
**Resultado**: O(1) - Acceso directo, tiempo constante

### Ejemplo 2: O(n)
```javascript
function sum(arr) {
    let total = 0;
    for (let i = 0; i < arr.length; i++) {
        total += arr[i];
    }
    return total;
}
```
**Resultado**: O(n) - Un bucle sobre todos los elementos

### Ejemplo 3: O(n²)
```javascript
function bubbleSort(arr) {
    for (let i = 0; i < arr.length; i++) {
        for (let j = 0; j < arr.length - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                let temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
    return arr;
}
```
**Resultado**: O(n²) - Bucles anidados

### Ejemplo 4: O(2ⁿ)
```javascript
function fibonacci(n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}
```
**Resultado**: O(2ⁿ) - Recursión exponencial

## ⚙️ Personalización

### Cambiar la Arquitectura de la Red
```python
analyzer = NeuralNetworkComplexityAnalyzer(
    hidden_layers=(256, 128, 64, 32),  # Más capas
    epochs=1000  # Más épocas
)
```

### Entrenar con Datos Propios
```python
analyzer = NeuralNetworkComplexityAnalyzer()
analyzer.train(X_custom, y_custom)
```

## 📚 Teoría de Complejidad Asintótica

La **notación O grande** describe cómo el tiempo de ejecución crece con el tamaño de entrada:

| Notación | Nombre | Ejemplo |
|----------|--------|---------|
| O(1) | Constante | Acceso a array |
| O(log n) | Logarítmica | Búsqueda binaria |
| O(n) | Lineal | Búsqueda lineal |
| O(n log n) | Cuasilineal | Merge sort |
| O(n²) | Cuadrática | Bubble sort |
| O(n³) | Cúbica | Multiplicación de matrices |
| O(2ⁿ) | Exponencial | Fibonacci recursivo |

## 🔧 Troubleshooting

### Error: "ModuleNotFoundError: No module named 'sklearn'"
```bash
pip install scikit-learn
```

### El modelo tarda mucho en entrenar
Esto es normal la primera vez. Se entrena con 1000 muestras en 500 épocas. Espera 1-2 minutos.

### La predicción no es exacta
El modelo está basado en patrones. Para código muy específico o inusual, la predicción puede variar. Siempre verifica manualmente.

## 📝 Licencia

Este proyecto es educativo y está disponible para uso libre.

## 👨‍💻 Autor

Creado con ❤️ para análisis automático de complejidad de algoritmos

---

**¡Disfruta analizando la complejidad de tus algoritmos!** 🚀
