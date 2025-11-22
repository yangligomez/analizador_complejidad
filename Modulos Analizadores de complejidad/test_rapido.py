"""
Script de prueba rápida con múltiples ejemplos
"""

from Backend.backend import NeuralNetworkComplexityAnalyzer

# Inicializar analizador
print("=" * 70)
print("ANALIZADOR DE COMPLEJIDAD - PRUEBAS RÁPIDAS")
print("=" * 70)
print("\n⏳ Entrenando modelo con 500 épocas...")
analyzer = NeuralNetworkComplexityAnalyzer()
analyzer.train()

# Ejemplos para probar
ejemplos = [
    ("Búsqueda Binaria", """function busquedaBinaria(arr, objetivo) {
  let inicio = 0;
  let fin = arr.length - 1;
  while (inicio <= fin) {
    let medio = Math.floor((inicio + fin) / 2);
    if (arr[medio] === objetivo) return true;
    else if (arr[medio] < objetivo) inicio = medio + 1;
    else fin = medio - 1;
  }
  return false;
}"""),
    
    ("Búsqueda Lineal", """function busquedaLineal(arr, objetivo) {
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === objetivo) return i;
  }
  return -1;
}"""),
    
    ("Merge Sort (O(n log n))", """function mergeSort(arr) {
  if (arr.length <= 1) return arr;
  let mid = Math.floor(arr.length / 2);
  let left = mergeSort(arr.slice(0, mid));
  let right = mergeSort(arr.slice(mid));
  return merge(left, right);
}"""),
    
    ("Ordenamiento Burbuja", """function ordenamientoBurbuja(arr) {
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr.length - i - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
      }
    }
  }
  return arr;
}"""),
    
    ("Fibonacci Recursivo", """function fib(n) {
  if (n <= 1) return n;
  return fib(n - 1) + fib(n - 2);
}"""),
    
    ("Suma (Constante)", """function suma(a, b) {
  return a + b;
}"""),
]

print("\n" + "=" * 70)
print("RESULTADOS DE PRUEBAS")
print("=" * 70)

for nombre, codigo in ejemplos:
    complexity, confidence = analyzer.predict(codigo)
    print(f"\n✓ {nombre:25} → {complexity:10} ({confidence:.1%} confianza)")

print("\n" + "=" * 70)
