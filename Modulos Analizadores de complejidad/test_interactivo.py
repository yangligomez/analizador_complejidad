"""
Script interactivo para probar el analizador de complejidad
Ingresa código JavaScript y obtén el análisis de complejidad
"""

from Backend.backend import NeuralNetworkComplexityAnalyzer

# Inicializar analizador
print("=" * 70)
print("ANALIZADOR DE COMPLEJIDAD - VERSIÓN MEJORADA")
print("=" * 70)
print("\nEntrenando modelo con 500 épocas...")
analyzer = NeuralNetworkComplexityAnalyzer()
analyzer.train()

print("\n" + "=" * 70)
print("EJEMPLOS DE PRUEBA")
print("=" * 70)

# Ejemplos predefinidos
ejemplos = {
    "1": {
        "nombre": "Búsqueda Binaria",
        "codigo": """function busquedaBinaria(arr, objetivo) {
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
}"""
    },
    "2": {
        "nombre": "Búsqueda Lineal",
        "codigo": """function busquedaLineal(arr, objetivo) {
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === objetivo) {
      return i;
    }
  }
  return -1;
}"""
    },
    "3": {
        "nombre": "Ordenamiento Burbuja",
        "codigo": """function ordenamientoBurbuja(arr) {
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr.length - i - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
      }
    }
  }
  return arr;
}"""
    },
    "4": {
        "nombre": "Fibonacci Recursivo",
        "codigo": """function fib(n) {
  if (n <= 1) return n;
  return fib(n - 1) + fib(n - 2);
}"""
    },
    "5": {
        "nombre": "Operación Constante",
        "codigo": """function suma(a, b) {
  return a + b;
}"""
    },
    "6": {
        "nombre": "Merge Sort",
        "codigo": """function mergeSort(arr) {
  if (arr.length <= 1) return arr;
  let mid = Math.floor(arr.length / 2);
  let left = mergeSort(arr.slice(0, mid));
  let right = mergeSort(arr.slice(mid));
  return merge(left, right);
}"""
    }
}

# Mostrar opciones
print("\nOpciones disponibles:")
for key, value in ejemplos.items():
    print(f"  {key} - {value['nombre']}")
print("  0 - Salir")

# Procesar ejemplos
while True:
    print("\n" + "-" * 70)
    opcion = input("\nSelecciona un ejemplo (0-6) o ingresa código JavaScript: ").strip()
    
    if opcion == "0":
        print("\n¡Hasta luego!")
        break
    
    if opcion in ejemplos:
        codigo = ejemplos[opcion]['codigo']
        nombre = ejemplos[opcion]['nombre']
        print(f"\n📌 Analizando: {nombre}")
    else:
        codigo = opcion
        print("\n📌 Analizando código personalizado:")
    
    print("\n" + "Código:")
    print("-" * 70)
    print(codigo)
    print("-" * 70)
    
    # Realizar análisis
    try:
        complexity, confidence = analyzer.predict(codigo)
        
        print("\n" + "=" * 70)
        print("RESULTADOS")
        print("=" * 70)
        print(f"🎯 COMPLEJIDAD: {complexity}")
        print(f"📊 CONFIANZA: {confidence:.1%}")
        print("=" * 70)
        
    except Exception as e:
        print(f"\n❌ Error al analizar: {e}")
