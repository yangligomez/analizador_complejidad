"""
Script de prueba para O(n log n) - Merge Sort
"""

from Backend.backend import NeuralNetworkComplexityAnalyzer

# Inicializar analizador
print("=" * 70)
print("ANALIZADOR DE COMPLEJIDAD - PRUEBA O(n log n)")
print("=" * 70)
print("\n⏳ Entrenando modelo con 500 épocas...")
analyzer = NeuralNetworkComplexityAnalyzer()
analyzer.train()

# Merge Sort - O(n log n)
merge_sort = """function mergeSort(arr) {
  if (arr.length <= 1) return arr;
  
  let mid = Math.floor(arr.length / 2);
  let left = mergeSort(arr.slice(0, mid));
  let right = mergeSort(arr.slice(mid));
  
  return merge(left, right);
}

function merge(left, right) {
  let result = [];
  let i = 0, j = 0;
  
  while (i < left.length && j < right.length) {
    if (left[i] < right[j]) {
      result.push(left[i++]);
    } else {
      result.push(right[j++]);
    }
  }
  
  while (i < left.length) result.push(left[i++]);
  while (j < right.length) result.push(right[j++]);
  
  return result;
}"""

# Quick Sort - O(n log n) promedio
quick_sort = """function quickSort(arr) {
  if (arr.length <= 1) return arr;
  
  let pivot = arr[Math.floor(arr.length / 2)];
  let left = arr.filter(x => x < pivot);
  let middle = arr.filter(x => x === pivot);
  let right = arr.filter(x => x > pivot);
  
  return [...quickSort(left), ...middle, ...quickSort(right)];
}"""

# Heap Sort - O(n log n)
heap_sort = """function heapSort(arr) {
  let n = arr.length;
  
  for (let i = Math.floor(n / 2) - 1; i >= 0; i--) {
    heapify(arr, n, i);
  }
  
  for (let i = n - 1; i > 0; i--) {
    [arr[0], arr[i]] = [arr[i], arr[0]];
    heapify(arr, i, 0);
  }
  
  return arr;
}

function heapify(arr, n, i) {
  let largest = i;
  let left = 2 * i + 1;
  let right = 2 * i + 2;
  
  if (left < n && arr[left] > arr[largest]) largest = left;
  if (right < n && arr[right] > arr[largest]) largest = right;
  
  if (largest !== i) {
    [arr[i], arr[largest]] = [arr[largest], arr[i]];
    heapify(arr, n, largest);
  }
}"""

ejemplos = [
    ("Merge Sort", merge_sort),
    ("Quick Sort", quick_sort),
    ("Heap Sort", heap_sort),
]

print("\n" + "=" * 70)
print("RESULTADOS - ALGORITMOS O(n log n)")
print("=" * 70)

for nombre, codigo in ejemplos:
    complexity, confidence = analyzer.predict(codigo)
    print(f"\n✓ {nombre:20} → {complexity:10} ({confidence:.1%} confianza)")
    
    # Marcar si es correcto
    if complexity == "O(n log n)":
        print(f"  ✅ CORRECTO")
    else:
        print(f"  ⚠️  Se esperaba O(n log n), se detectó {complexity}")

print("\n" + "=" * 70)
