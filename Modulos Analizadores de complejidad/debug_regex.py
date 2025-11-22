"""
Debug: Verificar si los regex están detectando correctamente
"""

import re

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

print("=" * 60)
print("DEBUG: VERIFICANDO REGEX")
print("=" * 60)

# Test 1: Detectar variables de rango
print("\n1️⃣ Buscando variables de rango (left|right|inicio|fin|low|high|start|end)...")
pattern1 = r'(left|right|inicio|fin|low|high|start|end)'
match1 = re.search(pattern1, codigo_busqueda_binaria, re.IGNORECASE)
print(f"   Resultado: {match1}")
if match1:
    print(f"   ✅ Encontrado: '{match1.group()}'")

# Test 2: Detectar mid
print("\n2️⃣ Buscando 'mid', 'middle' o 'medio'...")
pattern2 = r'(mid|middle|medio)'
match2 = re.search(pattern2, codigo_busqueda_binaria, re.IGNORECASE)
print(f"   Resultado: {match2}")
if match2:
    print(f"   ✅ Encontrado: '{match2.group()}'")

# Test 3: Ambas condiciones
print("\n3️⃣ Verificando si AMBAS condiciones se cumplen...")
has_range_vars = bool(re.search(pattern1, codigo_busqueda_binaria, re.IGNORECASE))
has_mid = bool(re.search(pattern2, codigo_busqueda_binaria, re.IGNORECASE))
both_true = has_range_vars and has_mid
print(f"   ¿Tiene variables de rango? {has_range_vars}")
print(f"   ¿Tiene 'mid'? {has_mid}")
print(f"   ¿AMBAS? {both_true}")

if both_true:
    print("\n✅ Deberían detectar como O(log n)")
else:
    print("\n❌ No detecta como O(log n)")

print("\n" + "=" * 60)
