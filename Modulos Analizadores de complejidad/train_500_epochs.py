#!/usr/bin/env python3
"""
Script de entrenamiento con 500 épocas - Versión rápida
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from Backend.backend import NeuralNetworkComplexityAnalyzer
import time

print("=" * 70)
print("ENTRENAMIENTO DE RED NEURONAL CON 500 ÉPOCAS")
print("=" * 70)

# Inicializar con 500 épocas
analyzer = NeuralNetworkComplexityAnalyzer(epochs=500)

print(f"\n✓ Parámetros configurados:")
print(f"  - Épocas: {analyzer.model.epochs}")
print(f"  - Capas ocultas: {analyzer.model.hidden_layers}")
print(f"  - Learning rate: {analyzer.model.learning_rate}")
print(f"  - Tamaño entrada: {analyzer.model.input_size}")

# Generar datos de entrenamiento
print(f"\n📊 Generando datos de entrenamiento (1000 muestras)...")
X_train, y_train = analyzer.generate_training_data(samples=1000)
print(f"✓ Datos generados: {len(X_train)} muestras")

# Entrenar
print(f"\n🧠 Iniciando entrenamiento con 500 épocas...")
start_time = time.time()
analyzer.train(X_train, y_train)
elapsed = time.time() - start_time

print(f"\n✓ Entrenamiento completado en {elapsed:.2f} segundos")
print(f"✓ Modelo entrenado: {analyzer.is_trained}")

# Probar predicciones
print("\n" + "=" * 70)
print("PRUEBAS DE PREDICCIÓN")
print("=" * 70)

test_cases = [
    ("const x = 5; x++;", "O(1)"),
    ("for (let i = 0; i < n; i++) { console.log(i); }", "O(n)"),
]

for code, expected in test_cases:
    try:
        complexity, confidence = analyzer.predict(code)
        status = "✅" if complexity == expected else "⚠️ "
        print(f"\n{status} Código: {code[:50]}...")
        print(f"   Esperado: {expected} | Detectado: {complexity} ({confidence:.0%})")
    except Exception as e:
        print(f"❌ Error: {e}")

print("\n" + "=" * 70)
print("✅ Entrenamiento finalizado exitosamente")
print("=" * 70)
