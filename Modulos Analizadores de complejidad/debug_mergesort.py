"""
Debug: Analizar características de Merge Sort
"""

from Backend.backend import CodeFeatureExtractor

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

extractor = CodeFeatureExtractor()
features = extractor.extract_features(merge_sort)

print("=" * 60)
print("ANÁLISIS DE CARACTERÍSTICAS - MERGE SORT")
print("=" * 60)
print(f"\nLíneas: {features[0]}")
print(f"FOR loops: {features[1]}")
print(f"WHILE loops: {features[2]}")
print(f"Anidación máxima: {features[3]}")
print(f"Recursión: {features[4]}")
print(f"Array ops: {features[5]}")
print(f"Search ops: {features[6]}")
print(f"Sort ops: {features[7]}")
print(f"Variables: {features[9]}")
print(f"Functions: {features[13]}")
print(f"String methods: {features[15]}")

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
print(f"  nested_loops <= 1: {nested_loops <= 1}")
print(f"  ¿CUMPLE? {recursion > 0 and (array_ops >= 1 or string_methods >= 1) and nested_loops <= 1}")

print(f"\nREGLA 2 (O(n²))?")
print(f"  nested_loops >= 2: {nested_loops >= 2}")
print(f"  total_loops >= 2: {total_loops >= 2}")
print(f"  ¿CUMPLE? {nested_loops >= 2 and total_loops >= 2}")
