# 📊 ESTRUCTURA DEL PROYECTO - ANALIZADOR DE COMPLEJIDAD

## 🗂️ ORGANIZACIÓN VISUAL Y FUNCIONAL

```
RAÍZ DEL PROYECTO
│
├─────────────────────────────────────────────────────────────
│  📁 .venv/  (Entorno Virtual Python)
│  ├─ Scripts/python.exe  ⭐ (Intérprete de Python)
│  ├─ Lib/                (Librerías del proyecto)
│  └─ Include/            (Archivos de cabecera)
│
├─────────────────────────────────────────────────────────────
│  📁 Backend/  (LÓGICA Y PROCESAMIENTO)
│  │
│  ├─ backend.py  ⭐⭐⭐ (MOTOR PRINCIPAL - 533 líneas)
│  │  ├─ PARTE 1: Extracción de Características
│  │  │  └─ CodeFeatureExtractor (20 características)
│  │  │
│  │  ├─ PARTE 2: Mapeo de Complejidades
│  │  │  └─ ComplexityMapper (O(1) a O(2ⁿ))
│  │  │
│  │  ├─ PARTE 3: Red Neuronal
│  │  │  ├─ SimpleNeuralNetwork
│  │  │  │  ├─ forward() - Propagación hacia adelante
│  │  │  │  ├─ backward() - Backpropagation
│  │  │  │  ├─ sigmoid() - Función de activación
│  │  │  │  └─ train_simple() - Entrenamiento 500 épocas
│  │  │  │
│  │  │  └─ NeuralNetworkComplexityAnalyzer
│  │  │     ├─ generate_training_data()
│  │  │     ├─ train()
│  │  │     └─ predict()
│  │  │
│  │  └─ Lógica de Predicción (8 REGLAS)
│  │     ├─ REGLA 1: Triple bucle → O(n³)
│  │     ├─ REGLA 2: Doble bucle → O(n²)
│  │     ├─ REGLA 3: Recursión pura → O(2ⁿ)
│  │     ├─ REGLA 4: Merge sort → O(n log n)
│  │     ├─ REGLA 5: While simple → O(log n)
│  │     ├─ REGLA 6: For simple → O(n)
│  │     ├─ REGLA 7: Sin bucles → O(1) ⭐ (ARREGLADO)
│  │     └─ REGLA 8: Recursión sin bucles → O(log n)
│  │
│  └─ __init__.py  (Módulo Python)
│
├─────────────────────────────────────────────────────────────
│  📁 interface/  (INTERFAZ DE USUARIO)
│  │
│  ├─ interfaz.py  ⭐⭐ (GUI TKINTER - 580 líneas)
│  │  ├─ ComplexityAnalyzerGUI
│  │  │  ├─ setup_styles() - Estilos modernos
│  │  │  ├─ create_widgets() - Componentes UI
│  │  │  ├─ analyze_code() - Análisis en thread
│  │  │  └─ generate_explanation() - Reporte visual
│  │  │
│  │  └─ Componentes:
│  │     ├─ Área de entrada (ScrolledText)
│  │     ├─ Botón "Analizar Complejidad"
│  │     ├─ Display de complejidad (grande)
│  │     ├─ Barra de confianza
│  │     ├─ Panel de características
│  │     ├─ Factor dominante
│  │     ├─ Definición de complejidad
│  │     └─ Información adicional
│  │
│  └─ __init__.py  (Módulo Python)
│
├─────────────────────────────────────────────────────────────
│  📁 Documentacion/  (REFERENCIA Y GUÍAS)
│  │
│  ├─ README.md           (Descripción del proyecto)
│  └─ USAGE_GUIDE.md      (Guía de uso para el usuario)
│
├─────────────────────────────────────────────────────────────
│  📁 Presentacion/  (PARA PRESENTAR AL PROFESOR)
│  │
│  ├─ PRESENTACION.md          (Presentación formal)
│  └─ RESUMEN_EJECUTIVO.txt    (Resumen ejecutivo)
│
├─────────────────────────────────────────────────────────────
│  ⚙️ ARCHIVOS EJECUTABLES (RAÍZ)
│  │
│  ├─ main.py  ⭐⭐⭐ (PUNTO DE ENTRADA)
│  │  └─ Ejecutar para abrir la interfaz gráfica
│  │
│  ├─ train_500_epochs.py  ⭐⭐ (ENTRENAMIENTO)
│  │  └─ Ejecutar para entrenar la red neuronal
│  │     ├─ 500 épocas
│  │     ├─ Pérdida: 0.077211
│  │     └─ Tiempo: ~213 segundos
│  │
│  ├─ __init__.py          (Módulo Python)
│  └─ complexity_model.pkl (Modelo guardado)
│
└─────────────────────────────────────────────────────────────
```

---

## 🔄 FLUJO DE EJECUCIÓN (PASO A PASO)

### Opción 1: USAR LA INTERFAZ GRÁFICA

```
┌─────────────────────────────────────────┐
│  Usuario ejecuta: main.py               │
└─────────────────┬───────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│  main.py carga ComplexityAnalyzerGUI    │
│  desde interface/interfaz.py            │
└─────────────────┬───────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│  Se abre ventana Tkinter                │
│  - Área de entrada de código            │
│  - Botón "Analizar Complejidad"         │
│  - Área de resultados                   │
└─────────────────┬───────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│  Usuario pega código JavaScript         │
│  y hace clic en "Analizar"              │
└─────────────────┬───────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│  interfaz.py llama a:                   │
│  NeuralNetworkComplexityAnalyzer.      │
│  predict(code)                          │
└─────────────────┬───────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│  backend.py procesa:                    │
│  1. Extrae características (20)         │
│  2. Red neuronal predice               │
│  3. Aplica 8 reglas de lógica          │
│  4. Retorna complejidad + confianza    │
└─────────────────┬───────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│  interfaz.py muestra resultado:         │
│  - Complejidad (O(1), O(n), etc)       │
│  - Confianza (%)                        │
│  - Características encontradas          │
│  - Factor dominante                     │
│  - Definición                           │
└─────────────────────────────────────────┘
```

### Opción 2: ENTRENAR LA RED NEURONAL

```
┌─────────────────────────────────────────┐
│  Usuario ejecuta: train_500_epochs.py   │
└─────────────────┬───────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│  Crea analizador con 500 épocas         │
│  NeuralNetworkComplexityAnalyzer(       │
│      epochs=500                         │
│  )                                      │
└─────────────────┬───────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│  Genera 1000 muestras de entrenamiento  │
│  (código de ejemplo + complejidad real) │
└─────────────────┬───────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│  Red neuronal entrena 500 épocas:       │
│  Época 1: Forward → Backward            │
│  Época 2: Forward → Backward            │
│  ...                                    │
│  Época 500: Forward → Backward          │
│  (Pérdida converge a 0.077211)          │
└─────────────────┬───────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│  Prueba predicciones                    │
│  ✅ O(1) detectado                      │
│  ✅ O(n) detectado                      │
│  ✅ O(2ⁿ) detectado                     │
└─────────────────────────────────────────┘
```

---

## 📋 TABLA DE COMPONENTES FUNCIONALES

| Componente | Archivo | Líneas | Función |
|-----------|---------|--------|---------|
| **Entrada** | main.py | 26 | Punto de entrada |
| **GUI** | interface/interfaz.py | 580 | Interfaz visual |
| **Backend** | Backend/backend.py | 533 | Lógica de análisis |
| **Entrenamiento** | train_500_epochs.py | - | Script de prueba |
| **Documentación** | Documentacion/*.md | - | Guías y referencias |
| **Presentación** | Presentacion/*.md | - | Para profesor |

---

## ✅ ESTADO FUNCIONAL

| Componente | Estado | Notas |
|-----------|--------|-------|
| ✅ **Backend** | FUNCIONAL | Red neuronal 500 épocas |
| ✅ **Interface** | FUNCIONAL | GUI moderna con Tkinter |
| ✅ **main.py** | FUNCIONAL | Se ejecuta sin errores |
| ✅ **Predicción O(1)** | ARREGLADO | Ahora consistente |
| ✅ **Entrenamiento** | FUNCIONAL | Pérdida 0.077211 |
| ✅ **Documentación** | COMPLETA | Guías incluidas |

---

## 🚀 COMANDOS PARA EJECUTAR

### 1. Abrir la aplicación:
```powershell
& "C:/Users/IA Tech/Downloads/Modulos Analizadores de complejidad/.venv/Scripts/python.exe" main.py
```

### 2. Entrenar el modelo:
```powershell
& "C:/Users/IA Tech/Downloads/Modulos Analizadores de complejidad/.venv/Scripts/python.exe" train_500_epochs.py
```

### 3. Activar entorno virtual:
```powershell
& ".venv/Scripts/Activate.ps1"
```

---

## 🎯 CONCLUSIÓN

✅ **El proyecto está completamente funcional**

- ✅ 4 carpetas principales bien organizadas
- ✅ Cada carpeta tiene su función específica
- ✅ Flujo de ejecución claro y ordenado
- ✅ Red neuronal de 500 épocas implementada
- ✅ Bug de O(1) corregido
- ✅ Interfaz gráfica moderna
- ✅ Documentación completa

**Listo para presentar al profesor.** 🚀
