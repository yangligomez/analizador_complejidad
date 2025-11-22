"""
Script de prueba para validar SOLO la lógica de detección de búsqueda binaria
Sin necesidad de entrenar 500 épocas
"""

from Backend.backend import CodeFeatureExtractor, SimpleNeuralNetwork, ComplexityMapper

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

print("=" * 60)
print("PRUEBA DE DETECCIÓN DE BÚSQUEDA BINARIA")
print("=" * 60)

# Paso 1: Extraer características
print("\n1️⃣ Extrayendo características del código...")
feature_extractor = CodeFeatureExtractor()
features = feature_extractor.extract_features(codigo_busqueda_binaria)

print(f"   Líneas de código: {features[0]}")
print(f"   Bucles FOR: {features[1]}")
print(f"   Bucles WHILE: {features[2]}")
print(f"   Anidación máxima: {features[3]}")
print(f"   Recursión: {features[4]}")
print(f"   Variables: {features[9]}")

# Paso 2: Crear modelo sin entrenar (solo para prueba de lógica)
print("\n2️⃣ Inicializando modelo para prueba de lógica...")
mapper = ComplexityMapper()
model = SimpleNeuralNetwork(input_size=20, hidden_layers=(128, 64, 32), epochs=500)
model.is_trained = True  # Marcar como entrenado para permitir predicción

# Paso 3: Predecir complejidad
print("\n3️⃣ Prediciendo complejidad basada en características y código...")
complexity_value, confidence = model.predict(features, codigo_busqueda_binaria)
complexity = mapper.value_to_complexity(complexity_value)

# Paso 4: Mostrar resultados
print("\n" + "=" * 60)
print("RESULTADOS")
print("=" * 60)
print(f"\n🎯 COMPLEJIDAD DETECTADA: {complexity}")
print(f"📊 CONFIANZA: {confidence:.2%}")
print(f"📈 VALOR NUMÉRICO: {complexity_value:.3f}")
print("\n✅ RESULTADO ESPERADO: O(log n)")

if complexity == "O(log n)":
    print("\n✅ ¡ÉXITO! El algoritmo fue identificado correctamente como O(log n)")
    print("   La detección de búsqueda binaria está funcionando correctamente.")
else:
    print(f"\n❌ ERROR: Se detectó como {complexity} en lugar de O(log n)")
    print("   Revisa los patrones de detección en detect_algorithm_complexity_hints()")

print("\n" + "=" * 60)
