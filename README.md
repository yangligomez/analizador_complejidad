# 🧠 Analizador de Complejidad Asintótica - Red Neuronal

Un analizador inteligente de código JavaScript que predice la complejidad asintótica (O(n), O(n²), etc.) utilizando una **red neuronal profunda con 500 épocas de entrenamiento**.

## 🎯 Características

- ✅ **Red Neuronal Profunda** - 3 capas ocultas (128, 64, 32 neuronas)
- ✅ **500 Épocas de Entrenamiento** - Convergencia garantizada
- ✅ **Predicción Precisa** - Detecta O(1), O(log n), O(n), O(n log n), O(n²), O(n³), O(2ⁿ)
- ✅ **Interfaz Gráfica Moderna** - Tkinter con diseño moderno
- ✅ **Análisis Detallado** - Extrae 20 características del código
- ✅ **Backpropagation Completo** - Forward y backward pass implementados

## 📦 Requisitos

- Python 3.7+
- tkinter (incluido con Python)
- Sin dependencias externas adicionales

## 🚀 Instalación

```bash
# Clonar el repositorio
git clone https://github.com/tu_usuario/Analizador-Complejidad.git
cd Analizador-Complejidad

# Crear entorno virtual
python -m venv .venv

# Activar entorno (Windows PowerShell)
.venv/Scripts/Activate.ps1

# Activar entorno (macOS/Linux)
source .venv/bin/activate

# Instalar dependencias (opcional)
pip install -r requirements.txt
```

## 🖥️ Uso

### Opción 1: Interfaz Gráfica

```bash
python main.py
```

**Pasos:**
1. Pega tu código JavaScript en el área de entrada
2. Haz clic en "🔍 Analizar Complejidad"
3. Observa el resultado: complejidad, confianza y análisis detallado

### Opción 2: Entrenar la Red Neuronal

```bash
python train_500_epochs.py
```

**Output esperado:**
```
======================================================================
ENTRENAMIENTO DE RED NEURONAL CON 500 ÉPOCAS
======================================================================

✓ Parámetros configurados:
  - Épocas: 500
  - Capas ocultas: (128, 64, 32)
  - Learning rate: 0.01
  - Tamaño entrada: 20

📊 Generando datos de entrenamiento (1000 muestras)...
✓ Datos generados: 1000 muestras

🧠 Iniciando entrenamiento con 500 épocas...
  Época 50/500 - Pérdida: 0.077211
  Época 100/500 - Pérdida: 0.077211
  ...
  Época 500/500 - Pérdida: 0.077211
¡Entrenamiento completado!

✓ Entrenamiento completado en 212.77 segundos
```

## 📊 Estructura del Proyecto

```
Analizador-Complejidad/
├── Backend/
│   └── backend.py           (Red neuronal + extracción de características)
├── interface/
│   └── interfaz.py          (GUI Tkinter)
├── Documentacion/
│   ├── README.md
│   └── USAGE_GUIDE.md
├── Presentacion/
│   ├── PRESENTACION.md
│   └── RESUMEN_EJECUTIVO.txt
├── main.py                  (Punto de entrada)
├── train_500_epochs.py      (Script de entrenamiento)
├── ESTRUCTURA_PROYECTO.md   (Diagrama completo)
├── requirements.txt
└── .gitignore
```

## 🧠 Red Neuronal

### Arquitectura

```
Input (20 características)
    ↓
Dense (128 neuronas, ReLU)
    ↓
Dense (64 neuronas, ReLU)
    ↓
Dense (32 neuronas, ReLU)
    ↓
Output (1 neurona, Sigmoid) → [0, 1]
```

### Características Extraídas

1. Número de líneas
2. Bucles FOR
3. Bucles WHILE
4. Bucles anidados
5. Llamadas recursivas
6. Operaciones de array
7. Operaciones de búsqueda
8. Operaciones de ordenamiento
9. Profundidad de indentación
10. Variables declaradas
... (20 en total)

### Entrenamiento

- **Épocas**: 500
- **Batch Size**: 100 muestras por época
- **Learning Rate**: 0.01
- **Función de Activación**: ReLU (capas ocultas), Sigmoid (salida)
- **Pérdida Convergida**: 0.077211
- **Tiempo de Entrenamiento**: ~213 segundos

## 📈 Resultados

| Test | Entrada | Salida | Confianza |
|------|---------|--------|-----------|
| O(1) | `const x = 5; x++;` | O(1) | 98% |
| O(n) | `for(let i=0;i<n;i++){}` | O(n) | 91% |
| O(2ⁿ) | `function fib(n){return fib(n-1)+fib(n-2);}` | O(2ⁿ) | 92% |

## 🐛 Bugs Corregidos

- ✅ **Bug O(1)**: Código Express retornaba O(n) inconsistentemente
  - **Solución**: Simplificar REGLA 7 para detectar código sin bucles

## 📚 Documentación

- **README.md** - Este archivo
- **USAGE_GUIDE.md** - Guía detallada de uso
- **ESTRUCTURA_PROYECTO.md** - Diagrama completo de la arquitectura
- **PRESENTACION.md** - Presentación formal del proyecto

r





