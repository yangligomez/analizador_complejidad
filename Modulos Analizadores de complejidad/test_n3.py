"""
Script de prueba para O(n³) - Triple bucle anidado
"""

from Backend.backend import NeuralNetworkComplexityAnalyzer

# Inicializar analizador
print("=" * 70)
print("ANALIZADOR DE COMPLEJIDAD - PRUEBA O(n³)")
print("=" * 70)
print("\n⏳ Entrenando modelo con 500 épocas...")
analyzer = NeuralNetworkComplexityAnalyzer()
analyzer.train()

# Ejemplos de O(n³)
ejemplos = [
    ("Matriz 3D - Triple bucle", """function procesarMatriz3D(matriz) {
  let n = matriz.length;
  
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      for (let k = 0; k < n; k++) {
        console.log(matriz[i][j][k]);
      }
    }
  }
}"""),
    
    ("Producto de matrices", """function productMatrices(A, B) {
  let n = A.length;
  let C = [];
  
  for (let i = 0; i < n; i++) {
    C[i] = [];
    for (let j = 0; j < n; j++) {
      C[i][j] = 0;
      for (let k = 0; k < n; k++) {
        C[i][j] += A[i][k] * B[k][j];
      }
    }
  }
  
  return C;
}"""),
    
    ("Búsqueda en 3D", """function busqueda3D(arr) {
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr[i].length; j++) {
      for (let k = 0; k < arr[i][j].length; k++) {
        if (arr[i][j][k] === 5) {
          return [i, j, k];
        }
      }
    }
  }
  return null;
}"""),
]

print("\n" + "=" * 70)
print("RESULTADOS - ALGORITMOS O(n³)")
print("=" * 70)

for nombre, codigo in ejemplos:
    complexity, confidence = analyzer.predict(codigo)
    print(f"\n✓ {nombre:25} → {complexity:10} ({confidence:.1%} confianza)")
    
    # Marcar si es correcto
    if complexity == "O(n³)":
        print(f"  ✅ CORRECTO")
    else:
        print(f"  ⚠️  Se esperaba O(n³), se detectó {complexity}")

print("\n" + "=" * 70)
