"""
Script de prueba para validar la corrección de búsqueda binaria
"""

import sys
import os

# Agregar las carpetas de módulos al path
base_dir = os.path.dirname(__file__)
modulos_dir = os.path.join(base_dir, "Modulos Analizadores de complejidad")
sys.path.insert(0, modulos_dir)

from Backend.backend import NeuralNetworkComplexityAnalyzer

# Código de búsqueda binaria que fue reportado
codigo_busqueda_binaria = """function busquedaBinaria(arr, objetivo) {
  let inicio = 0;
  let fin = arr.length - 1;

  while (inicio <= fin) {
    let medio = Math.floor((inicio + fin) / 2);

    if (arr[medio] === objetivo) {
      return true;
    } else if (arr[medio] < objetivo) {
      inicio = medio + 1;
    } else {
      fin = medio - 1;
    }
  }

  return false;
}

// uso
console.log(busquedaBinaria([1, 3, 5, 7, 9, 12, 15], 7));"""

# Inicializar analizador
analyzer = NeuralNetworkComplexityAnalyzer()
analyzer.train()

# Analizar el código
complexity, confidence = analyzer.predict(codigo_busqueda_binaria)

print("=" * 50)
print("ANÁLISIS DE BÚSQUEDA BINARIA")
print("=" * 50)
print(f"\n🎯 COMPLEJIDAD DETECTADA: {complexity}")
print(f"📊 CONFIANZA: {confidence:.2%}")
print("\nResultado esperado: O(log n)")

if complexity == "O(log n)":
    print("✅ ¡CORRECTO! El algoritmo fue identificado correctamente como O(log n)")
else:
    print(f"❌ ERROR: Se detectó como {complexity} en lugar de O(log n)")
