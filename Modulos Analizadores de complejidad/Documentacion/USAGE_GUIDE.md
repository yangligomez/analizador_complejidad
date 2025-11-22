# 📚 Guía Completa de Uso - Analizador de Complejidad

## 🎯 Inicio Rápido

### Paso 1: Instalar Dependencias
```bash
python setup_requirements.py
```

### Paso 2: Ejecutar la Interfaz Gráfica
```bash
python gui_analyzer.py
```

### Paso 3: Analizar Código
1. Pega tu código JavaScript en el editor
2. Haz clic en "🔍 Analizar Complejidad"
3. Obtén el resultado instantáneamente

---

## 🚀 Características Principales

### 1. Red Neuronal Avanzada

**500 Épocas de Entrenamiento**
- Aprende patrones de complejidad
- Se adapta a diferentes estilos de código
- Mejora con el tiempo

**Arquitectura Optimizada**
```
Entrada → [128 neuronas] → [64 neuronas] → [32 neuronas] → Salida
          ↓                ↓                ↓
          ReLU             ReLU             ReLU
```

### 2. Análisis de 20 Características

El motor analiza automáticamente:
- **Estructuras de control**: for, while, if, switch
- **Operaciones de array**: map, filter, reduce, push, pop
- **Profundidad de anidación**: detecta bucles anidados
- **Patrones recursivos**: identifica llamadas recursivas
- **Complejidad del código**: longitud, indentación

### 3. Interfaz Moderna

- Editor de código con sintaxis oscura
- Barra de progreso de confianza
- Explicaciones detalladas
- Carga de archivos .js

---

## 📖 Complejidades Soportadas

### O(1) - Tiempo Constante
```javascript
// Acceso directo a elemento
function getElement(arr, index) {
    return arr[index];
}

// Operación simple
function increment(x) {
    return x + 1;
}
```
**Características**: Sin bucles, sin iteraciones

---

### O(log n) - Logarítmica
```javascript
// Búsqueda binaria
function binarySearch(arr, target) {
    let left = 0, right = arr.length - 1;
    while (left <= right) {
        let mid = Math.floor((left + right) / 2);
        if (arr[mid] === target) return mid;
        else if (arr[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
}
```
**Características**: Divide el problema a la mitad

---

### O(n) - Lineal
```javascript
// Búsqueda lineal
function findIndex(arr, value) {
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === value) return i;
    }
    return -1;
}

// Suma de elementos
function sum(arr) {
    let total = 0;
    for (let i = 0; i < arr.length; i++) {
        total += arr[i];
    }
    return total;
}
```
**Características**: Un bucle sobre todos los elementos

---

### O(n log n) - Cuasilineal
```javascript
// Merge Sort
function mergeSort(arr) {
    if (arr.length <= 1) return arr;
    
    let mid = Math.floor(arr.length / 2);
    let left = mergeSort(arr.slice(0, mid));
    let right = mergeSort(arr.slice(mid));
    
    return merge(left, right);
}

function merge(left, right) {
    let result = [];
    while (left.length && right.length) {
        if (left[0] <= right[0]) {
            result.push(left.shift());
        } else {
            result.push(right.shift());
        }
    }
    return result.concat(left).concat(right);
}
```
**Características**: Divide y conquista + fusión

---

### O(n²) - Cuadrática
```javascript
// Bubble Sort
function bubbleSort(arr) {
    for (let i = 0; i < arr.length; i++) {
        for (let j = 0; j < arr.length - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                // Intercambiar
                let temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
    return arr;
}

// Comparar pares
function comparePairs(arr) {
    for (let i = 0; i < arr.length; i++) {
        for (let j = i + 1; j < arr.length; j++) {
            console.log(arr[i], arr[j]);
        }
    }
}
```
**Características**: Dos bucles anidados

---

### O(n³) - Cúbica
```javascript
// Multiplicación de matrices
function multiplyMatrices(a, b) {
    let result = [];
    for (let i = 0; i < a.length; i++) {
        result[i] = [];
        for (let j = 0; j < b[0].length; j++) {
            result[i][j] = 0;
            for (let k = 0; k < b.length; k++) {
                result[i][j] += a[i][k] * b[k][j];
            }
        }
    }
    return result;
}
```
**Características**: Tres bucles anidados

---

### O(2ⁿ) - Exponencial
```javascript
// Fibonacci Recursivo
function fib(n) {
    if (n <= 1) return n;
    return fib(n - 1) + fib(n - 2);
}

// Generar subconjuntos
function generateSubsets(arr) {
    let result = [];
    for (let i = 0; i < Math.pow(2, arr.length); i++) {
        let subset = [];
        for (let j = 0; j < arr.length; j++) {
            if (i & (1 << j)) {
                subset.push(arr[j]);
            }
        }
        result.push(subset);
    }
    return result;
}
```
**Características**: Recursión exponencial, bucles potencia

---

## 🔧 Uso Avanzado

### Entrenar con Datos Personalizados

```python
from neural_complexity_analyzer import NeuralNetworkComplexityAnalyzer
import numpy as np

# Crear datos de entrenamiento personalizados
X_train = np.array([...])  # Características
y_train = np.array([...])  # Complejidades (0-1)

# Crear y entrenar analizador
analyzer = NeuralNetworkComplexityAnalyzer(epochs=500)
analyzer.train(X_train, y_train)

# Analizar nuevo código
code = "..."
complexity, confidence = analyzer.predict(code)
```

### Guardar y Cargar Modelos

```python
# Guardar modelo entrenado
analyzer.save_model("mi_modelo.pkl")

# Cargar modelo guardado
nuevo_analyzer = NeuralNetworkComplexityAnalyzer()
nuevo_analyzer.load_model("mi_modelo.pkl")
```

### Análisis por Línea de Comandos

```python
from neural_complexity_analyzer import NeuralNetworkComplexityAnalyzer

analyzer = NeuralNetworkComplexityAnalyzer(epochs=500)
analyzer.load_model("complexity_model.pkl")

# Analizar archivo
with open("mi_codigo.js", "r") as f:
    code = f.read()

complexity, confidence = analyzer.predict(code)
print(f"Complejidad: {complexity}")
print(f"Confianza: {confidence:.1%}")
```

---

## 📊 Interpretación de Resultados

### Confianza del Modelo

- **80-100%**: Predicción muy confiable
- **60-80%**: Predicción moderadamente confiable
- **40-60%**: Predicción poco confiable
- **<40%**: Puede ser código ambiguo o inusual

### Causas de Baja Confianza

1. **Código ambiguo**: Mezcla de patrones diferentes
2. **Código inusual**: No coincide con los patrones de entrenamiento
3. **Código incompleto**: Fragmentos sin contexto
4. **Lógica compleja**: Combinaciones poco comunes

---

## 💡 Consejos de Uso

### Para Mejores Resultados

✅ **Código completo**: Proporciona funciones enteras
✅ **Código limpio**: Bien formateado y legible
✅ **Código típico**: Usa patrones comunes de JavaScript
✅ **Verifica manualmente**: No confíes 100% en la IA

### Casos Problemáticos

❌ Fragmentos de código
❌ Código ofuscado o minificado
❌ Algoritmos muy específicos
❌ Mezcla de lenguajes

---

## 🐛 Solución de Problemas

### Problema: "ModuleNotFoundError: No module named 'sklearn'"

**Solución:**
```bash
pip install scikit-learn numpy
```

### Problema: El modelo tarda mucho en cargar

**Motivo**: Primera ejecución - se entrena con 500 épocas
**Solución**: Espera 1-2 minutos, se guardará automáticamente

### Problema: Predicciones incorrectas

**Prueba:**
1. Asegúrate de que sea código JavaScript válido
2. Verifica que sea un algoritmo típico
3. Intenta ejecutar `test_analyzer.py` para validar

### Problema: La interfaz gráfica no abre

**Solución:**
```bash
# Verifica que Tkinter esté instalado
python -m tkinter

# Si falla, instala:
# Windows: Incluido en Python
# Linux: sudo apt install python3-tk
# macOS: Incluido en Python
```

---

## 📁 Estructura de Archivos

```
.
├── neural_complexity_analyzer.py    # Motor de análisis
├── gui_analyzer.py                  # Interfaz gráfica
├── test_analyzer.py                 # Script de pruebas
├── setup_requirements.py             # Instalador de dependencias
├── requirements.txt                  # Lista de dependencias
├── README.md                        # Documentación principal
├── USAGE_GUIDE.md                   # Esta guía
└── complexity_model.pkl             # Modelo entrenado (auto-generado)
```

---

## 🎓 Teoría de Complejidad

### Definición Formal

La notación O grande describe el **límite superior asintótico** de una función:

$$f(n) = O(g(n))$$ si existe una constante $c > 0$ tal que:
$$f(n) \leq c \cdot g(n) \text{ para todo } n \geq n_0$$

### Comparación de Complejidades

```
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2ⁿ)
```

### Reglas Prácticas

1. **Bucles simples**: +1 exponente
2. **Bucles anidados**: multiplicar exponentes
3. **Operaciones secuenciales**: suma (toma la mayor)
4. **Recursión**: exponencial o logarítmica según el caso

---

## 📞 Ayuda Adicional

- **Documentación**: Ver README.md
- **Ejemplos**: Ver test_analyzer.py
- **Problemas**: Revisa la sección "Solución de Problemas"
- **Código Fuente**: Estudia neural_complexity_analyzer.py

---

**¡Ahora estás listo para analizar la complejidad de tus algoritmos!** 🚀
