"""
Debug: Analizar características de Heap Sort
"""

from Backend.backend import CodeFeatureExtractor

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

extractor = CodeFeatureExtractor()
features = extractor.extract_features(heap_sort)

print("=" * 60)
print("ANÁLISIS DE CARACTERÍSTICAS - HEAP SORT")
print("=" * 60)
print(f"\nLíneas: {features[0]}")
print(f"FOR loops: {features[1]}")
print(f"WHILE loops: {features[2]}")
print(f"Anidación máxima: {features[3]}")
print(f"Recursión: {features[4]}")
print(f"Array ops: {features[5]}")
print(f"Variables: {features[9]}")
print(f"Functions: {features[13]}")

print("\n" + "=" * 60)
print("ANÁLISIS DE REGLAS:")
print("=" * 60)

total_loops = features[1] + features[2]
nested_loops = features[3]
recursion = features[4]
array_ops = features[5]
string_methods = features[15]

print(f"\ntotal_loops: {total_loops}")
print(f"nested_loops: {nested_loops}")
print(f"recursion: {recursion}")
print(f"array_ops: {array_ops}")

print(f"\nREGLA 4 (O(n log n))?")
print(f"  recursion > 0: {recursion > 0}")
print(f"  array_ops >= 1 or string_methods >= 1: {array_ops >= 1 or string_methods >= 1}")
print(f"  nested_loops <= 2: {nested_loops <= 2}")
print(f"  ¿CUMPLE? {recursion > 0 and (array_ops >= 1 or string_methods >= 1) and nested_loops <= 2}")

print(f"\nREGLA 6 (O(n))?")
print(f"  for_loops >= 1: {features[1] >= 1}")
print(f"  while_loops == 0: {features[2] == 0}")
print(f"  nested_loops <= 1: {nested_loops <= 1}")
print(f"  ¿CUMPLE? {features[1] >= 1 and features[2] == 0 and nested_loops <= 1}")
