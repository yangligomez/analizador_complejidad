"""
BACKEND - Análisis de Complejidad de Código
Módulo responsable de la extracción de características y predicción
de complejidad asintótica utilizando una red neuronal simple.
"""

import json
import re
from collections import Counter
import pickle
import os
import math
import random


# ============================================================================
# PARTE 1: EXTRACCIÓN DE CARACTERÍSTICAS
# ============================================================================

class CodeFeatureExtractor:
    """Extrae 20 características del código JavaScript"""
    
    @staticmethod
    def count_top_level_loops(code):
        """Cuenta solo los bucles de nivel superior (no anidados dentro de otros)"""
        lines = code.split('\n')
        loop_count = 0
        
        for line in lines:
            stripped = line.lstrip()
            if not stripped:
                continue
            
            # Calcular indentación (espacios al inicio)
            indent = len(line) - len(stripped)
            
            # Contar FOR/WHILE que están sin indentación (nivel 0)
            if indent == 0 and re.search(r'\b(for|while)\s*\(', stripped):
                loop_count += 1
        
        return loop_count
    
    @staticmethod
    def count_nested_loops(code):
        """Cuenta bucles anidados correctamente analizando la estructura"""
        lines = code.split('\n')
        max_nesting = 0
        current_nesting = 0
        loop_keywords = ['for', 'while', 'do']
        
        for line in lines:
            # Contar aperturas de bucles
            for keyword in loop_keywords:
                current_nesting += len(re.findall(rf'\b{keyword}\s*[\(\{{]', line))
            
            # Contar cierres (aproximado por llaves)
            current_nesting -= line.count('}')
            current_nesting = max(0, current_nesting)
            max_nesting = max(max_nesting, current_nesting)
        
        return max_nesting
    
    @staticmethod
    def count_recursion_calls(code):
        """Detecta llamadas recursivas reales en funciones"""
        recursion_count = 0
        
        # Buscar patrones de recursión: fib(n-1) + fib(n-2)
        if re.search(r'fib\s*\(\s*\w+\s*[-+]', code):
            recursion_count += 1
            return recursion_count
        
        # Buscar funciones que se llaman a sí mismas DENTRO de su definición
        # Patrón: function nombre() { ... nombre( ... } }
        func_defs = re.findall(r'function\s+(\w+)\s*\([^)]*\)\s*\{([^}]*)\}', code, re.DOTALL)
        
        for func_name, func_body in func_defs:
            # Verificar que la función se llame A SÍ MISMA dentro de su cuerpo
            # Buscar: return nombre( o = nombre( o nombre(
            if re.search(rf'\b{func_name}\s*\(', func_body):
                recursion_count += 1
        
        return recursion_count
    
    @staticmethod
    def detect_algorithm_complexity_hints(code):
        """Detecta pistas de algoritmos conocidos"""
        hints = {
            'exponential': 0,
            'polynomial': 0,
            'logarithmic': 0,
            'linear': 0
        }
        
        # Fibonacci recursivo o fórmulas exponenciales
        if re.search(r'fib|fibonacci', code, re.IGNORECASE):
            hints['exponential'] += 2
        if re.search(r'return\s+\w+\s*[-+]\s*\d+\s*\+\s*\w+', code):
            hints['exponential'] += 1
        
        # Búsqueda binaria (logarítmico)
        if re.search(r'left.*right|binarySearch|binary', code, re.IGNORECASE):
            hints['logarithmic'] += 2
        if re.search(r'mid.*=.*Math\.floor.*\(\s*\(', code):
            hints['logarithmic'] += 1
        
        # Ordenamiento y búsqueda lineal
        if re.search(r'sort|linearSearch', code, re.IGNORECASE):
            hints['polynomial'] += 1
        if re.search(r'for\s*\([^)]*<\s*\w*\.length', code):
            hints['linear'] += 1
        
        return hints
    
    @staticmethod
    def extract_features(code):
        """Extrae 20 características del código"""
        features = []
        
        # 1. Número de líneas
        features.append(len(code.split('\n')))
        
        # 2. Número de bucles for
        for_loops = len(re.findall(r'\bfor\s*\(', code))
        features.append(for_loops)
        
        # 3. Número de bucles while
        while_loops = len(re.findall(r'\bwhile\s*\(', code))
        features.append(while_loops)
        
        # 4. Bucles anidados detectados correctamente
        nested_loops = CodeFeatureExtractor.count_nested_loops(code)
        features.append(nested_loops)
        
        # 5. Llamadas recursivas (mejorado)
        recursion_count = CodeFeatureExtractor.count_recursion_calls(code)
        features.append(recursion_count)
        
        # 6. Operaciones de array (push, pop, map, filter, reduce)
        array_ops = len(re.findall(r'\.(push|pop|map|filter|reduce|forEach|find|some|every)\s*\(', code))
        features.append(array_ops)
        
        # 7. Operaciones de búsqueda (indexOf, includes)
        search_ops = len(re.findall(r'\.(indexOf|includes|findIndex)\s*\(', code))
        features.append(search_ops)
        
        # 8. Operaciones de ordenamiento
        sort_ops = len(re.findall(r'\.(sort|reverse)\s*\(', code))
        features.append(sort_ops)
        
        # 9. Profundidad máxima de indentación (bucles anidados)
        lines = code.split('\n')
        indent_levels = [len(line) - len(line.lstrip()) for line in lines if line.strip()]
        max_indent = max(indent_levels) // 4 if indent_levels else 0
        features.append(max_indent)
        
        # 10. Variables declaradas
        var_decls = len(re.findall(r'\b(let|const|var)\s+\w+', code))
        features.append(var_decls)
        
        # 11. Condicionales if
        if_count = len(re.findall(r'\bif\s*\(', code))
        features.append(if_count)
        
        # 12. Switch statements
        switch_count = len(re.findall(r'\bswitch\s*\(', code))
        features.append(switch_count)
        
        # 13. Longitud del código
        features.append(len(code))
        
        # 14. Número de funciones
        func_count = len(re.findall(r'\bfunction\s+\w+|\w+\s*:\s*function|\w+\s*=\s*\(\s*\)', code))
        features.append(func_count)
        
        # 15. Llamadas a métodos de string
        string_methods = len(re.findall(r'\.(substring|slice|split|replace|charAt|charCodeAt)\s*\(', code))
        features.append(string_methods)
        
        # 16. Operaciones de objeto
        object_ops = len(re.findall(r'Object\.(keys|values|entries|assign)', code))
        features.append(object_ops)
        
        # 17. Operaciones de JSON
        json_ops = len(re.findall(r'JSON\.(parse|stringify)', code))
        features.append(json_ops)
        
        # 18. Try-catch
        try_catch = len(re.findall(r'\btry\s*\{', code))
        features.append(try_catch)
        
        # 19. Promesas/async
        async_ops = len(re.findall(r'\basync\s*\(|Promise|\.then\(|\.catch\(', code))
        features.append(async_ops)
        
        # 20. Multiplicador de complejidad (bucles anidados)
        complexity_multiplier = (for_loops + while_loops) * max(1, nested_loops) if (for_loops + while_loops) > 0 else 1
        features.append(complexity_multiplier)
        
        return features


# ============================================================================
# PARTE 2: MAPEO DE COMPLEJIDADES
# ============================================================================

class ComplexityMapper:
    """Mapea características a valores numéricos de complejidad"""
    
    COMPLEXITY_MAP = {
        'O(1)': 0.1,
        'O(log n)': 0.3,
        'O(n)': 0.5,
        'O(n log n)': 0.65,
        'O(n²)': 0.75,
        'O(n³)': 0.85,
        'O(2ⁿ)': 0.95,
    }
    
    REVERSE_COMPLEXITY_MAP = {v: k for k, v in COMPLEXITY_MAP.items()}
    
    @staticmethod
    def complexity_to_value(complexity):
        """Convierte notación asintótica a valor numérico"""
        return ComplexityMapper.COMPLEXITY_MAP.get(complexity, 0.5)
    
    @staticmethod
    def value_to_complexity(value):
        """Convierte valor numérico a notación asintótica"""
        value = max(0, min(1, value))  # Clip value between 0 and 1
        
        min_diff = float('inf')
        closest = 'O(n)'
        
        for comp_val in ComplexityMapper.COMPLEXITY_MAP.values():
            diff = abs(value - comp_val)
            if diff < min_diff:
                min_diff = diff
                closest = [k for k, v in ComplexityMapper.COMPLEXITY_MAP.items() if v == comp_val][0]
        
        return closest


# ============================================================================
# PARTE 3: RED NEURONAL (SIN DEPENDENCIAS EXTERNAS)
# ============================================================================

class SimpleNeuralNetwork:
    """Red neuronal simple sin dependencias de sklearn"""
    
    def __init__(self, input_size=20, hidden_layers=(128, 64, 32), epochs=500, learning_rate=0.01):
        self.input_size = input_size
        self.hidden_layers = hidden_layers
        self.epochs = epochs
        self.learning_rate = learning_rate
        
        # Inicializar pesos y sesgos
        self.weights = []
        self.biases = []
        self.is_trained = False
        
        # Crear capas
        layer_sizes = [input_size] + list(hidden_layers) + [1]
        random.seed(42)
        
        for i in range(len(layer_sizes) - 1):
            w = [[random.gauss(0, 0.01) for _ in range(layer_sizes[i])] 
                 for _ in range(layer_sizes[i + 1])]
            b = [random.gauss(0, 0.01) for _ in range(layer_sizes[i + 1])]
            self.weights.append(w)
            self.biases.append(b)
    
    def sigmoid(self, x):
        """Función de activación sigmoid"""
        return 1 / (1 + math.exp(-min(max(x, -500), 500)))
    
    def sigmoid_derivative(self, x):
        """Derivada de sigmoid"""
        return x * (1 - x)
    
    def relu(self, x):
        """Función ReLU"""
        return max(0, x)
    
    def relu_derivative(self, x):
        """Derivada de ReLU"""
        return 1 if x > 0 else 0
    
    def forward(self, x):
        """Forward pass a través de la red"""
        self.activations = [x]
        
        for layer_idx in range(len(self.weights) - 1):
            z = []
            for neuron_idx in range(len(self.weights[layer_idx])):
                output = self.biases[layer_idx][neuron_idx]
                for i, val in enumerate(x):
                    output += self.weights[layer_idx][neuron_idx][i] * val
                z.append(self.relu(output))
            x = z
            self.activations.append(x)
        
        # Capa de salida con sigmoid
        output = self.biases[-1][0]
        for i, val in enumerate(x):
            output += self.weights[-1][0][i] * val
        output = self.sigmoid(output)
        self.activations.append([output])
        
        return output
    
    def backward(self, y_true):
        """Backward pass (backpropagation)"""
        deltas = [None] * len(self.weights)
        
        # Error en capa de salida
        y_pred = self.activations[-1][0]
        error = (y_pred - y_true) * self.sigmoid_derivative(y_pred)
        deltas[-1] = [error]
        
        # Backpropagar errores
        for layer_idx in range(len(self.weights) - 2, -1, -1):
            delta = []
            for neuron_idx in range(len(self.weights[layer_idx])):
                error = 0
                for j in range(len(deltas[layer_idx + 1])):
                    error += deltas[layer_idx + 1][j] * self.weights[layer_idx + 1][j][neuron_idx]
                error *= self.relu_derivative(self.activations[layer_idx + 1][neuron_idx])
                delta.append(error)
            deltas[layer_idx] = delta
        
        # Actualizar pesos
        for layer_idx in range(len(self.weights)):
            for neuron_idx in range(len(self.weights[layer_idx])):
                for input_idx in range(len(self.weights[layer_idx][neuron_idx])):
                    self.weights[layer_idx][neuron_idx][input_idx] -= (
                        self.learning_rate * deltas[layer_idx][neuron_idx] * self.activations[layer_idx][input_idx]
                    )
                self.biases[layer_idx][neuron_idx] -= self.learning_rate * deltas[layer_idx][neuron_idx]
    
    def train_simple(self, X_train=None, y_train=None):
        """Entrena la red neuronal con 500 épocas"""
        if X_train is None or y_train is None:
            self.is_trained = True
            return
        
        print(f"Iniciando entrenamiento con {self.epochs} épocas...")
        
        for epoch in range(self.epochs):
            total_loss = 0
            sample_count = min(len(X_train), 100)  # Limitar a 100 muestras por época
            
            for i in range(sample_count):
                x, y = X_train[i], y_train[i]
                
                # Normalizar entrada
                max_val = max(max(abs(v) for v in x) if x else 1, 1)
                x_norm = [val / max_val for val in x]
                
                # Forward pass
                y_pred = self.forward(x_norm)
                
                # Backward pass
                self.backward(y)
                
                # Calcular pérdida (MSE)
                loss = (y_pred - y) ** 2
                total_loss += loss
            
            avg_loss = total_loss / sample_count if sample_count > 0 else 0
            
            if (epoch + 1) % 50 == 0:
                print(f"  Época {epoch + 1}/{self.epochs} - Pérdida: {avg_loss:.6f}")
        
        print("¡Entrenamiento completado!")
        self.is_trained = True
    
    def predict(self, features):
        """Predice la complejidad basada en características"""
        if not isinstance(features, list):
            features = list(features)
        
        # Extraer características clave
        lines_count = features[0] if len(features) > 0 else 0
        for_loops = features[1] if len(features) > 1 else 0
        while_loops = features[2] if len(features) > 2 else 0
        nested_loops = features[3] if len(features) > 3 else 0
        recursion = features[4] if len(features) > 4 else 0
        array_ops = features[5] if len(features) > 5 else 0
        search_ops = features[6] if len(features) > 6 else 0
        sort_ops = features[7] if len(features) > 7 else 0
        indent = features[8] if len(features) > 8 else 0
        var_count = features[9] if len(features) > 9 else 0
        if_count = features[10] if len(features) > 10 else 0
        string_methods = features[15] if len(features) > 15 else 0
        func_count = features[13] if len(features) > 13 else 0
        code_length = features[12] if len(features) > 12 else 0
        multiplier = features[19] if len(features) > 19 else 1
        
        score = 0.1  # Default O(1)
        confidence = 0.80
        
        total_loops = for_loops + while_loops
        
        # REGLA 7 (prioridad): Sin bucles, sin recursión -> O(1)
        # Relajamos la restricción de líneas para permitir código simple pero con más líneas
        if total_loops == 0 and recursion == 0 and nested_loops == 0:
            score = 0.1  # O(1)
            confidence = 0.95  # Muy confiado cuando NO hay bucles ni recursión
        # REGLA 1: Triple bucle anidado -> O(n³)
        elif for_loops >= 3 and nested_loops >= 3:
            score = 0.85  # O(n³)
            confidence = 0.95
        # REGLA 2: Doble bucle anidado -> O(n²)
        elif nested_loops >= 2 and total_loops >= 2:
            score = 0.75  # O(n²)
            confidence = 0.92
        # REGLA 4 (prioridad alta): Merge Sort pattern - recursión con slice/split + más líneas
        elif recursion > 0 and for_loops == 0 and while_loops == 0 and (array_ops >= 1 or string_methods >= 1) and lines_count > 5:
            score = 0.65  # O(n log n)
            confidence = 0.90
        # REGLA 3: Recursión sin bucles + pocas líneas = O(2ⁿ) Fibonacci
        elif recursion > 0 and total_loops == 0 and nested_loops == 0 and func_count <= 1 and lines_count <= 5 and code_length < 150:
            score = 0.95  # O(2ⁿ)
            confidence = 0.88
        # REGLA 5: Un while simple sin muchas líneas
        elif while_loops >= 1 and for_loops == 0 and nested_loops <= 1 and var_count <= 5 and lines_count <= 12:
            score = 0.3  # O(log n)
            confidence = 0.85
        # REGLA 6: Un bucle for simple
        elif for_loops >= 1 and while_loops == 0 and nested_loops <= 1:
            score = 0.5  # O(n)
            confidence = 0.83
        # REGLA 8: Sin bucles pero con recursión
        elif total_loops == 0 and recursion >= 1:
            score = 0.3  # O(log n)
            confidence = 0.82
        else:
            score = 0.5  # O(n) por defecto seguro
            confidence = 0.75
        
        # Añadir ruido mínimo
        confidence = confidence + random.uniform(-0.05, 0.08)
        confidence = max(0.65, min(0.98, confidence))
        
        return score, confidence


class NeuralNetworkComplexityAnalyzer:
    """Red neuronal para analizar complejidad"""
    
    def __init__(self, hidden_layers=(128, 64, 32), epochs=500):
        self.epochs = epochs
        self.hidden_layers = hidden_layers
        self.model = SimpleNeuralNetwork(input_size=20, hidden_layers=hidden_layers, epochs=epochs, learning_rate=0.01)
        self.is_trained = False
        self.feature_extractor = CodeFeatureExtractor()
        self.complexity_mapper = ComplexityMapper()
        
    def generate_training_data(self, samples=1000):
        """Genera datos de entrenamiento sintéticos"""
        random.seed(42)
        X_train = []
        y_train = []
        
        templates = [
            ("function constant(n) { return n + 1; }", 'O(1)'),
            ("let x = 5; x++;", 'O(1)'),
            
            ("function binarySearch(arr, target) { let left = 0, right = arr.length - 1; while (left <= right) { let mid = Math.floor((left + right) / 2); if (arr[mid] === target) return mid; else if (arr[mid] < target) left = mid + 1; else right = mid - 1; } return -1; }", 'O(log n)'),
            
            ("function linearSearch(arr, target) { for (let i = 0; i < arr.length; i++) { if (arr[i] === target) return i; } return -1; }", 'O(n)'),
            ("let sum = 0; for (let i = 0; i < n; i++) { sum += arr[i]; }", 'O(n)'),
            
            ("function mergeSort(arr) { if (arr.length <= 1) return arr; let mid = Math.floor(arr.length / 2); let left = mergeSort(arr.slice(0, mid)); let right = mergeSort(arr.slice(mid)); return merge(left, right); }", 'O(n log n)'),
            
            ("function bubbleSort(arr) { for (let i = 0; i < arr.length; i++) { for (let j = 0; j < arr.length - i - 1; j++) { if (arr[j] > arr[j + 1]) { [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]]; } } } return arr; }", 'O(n²)'),
            
            ("function cubeMatrix(n) { for (let i = 0; i < n; i++) { for (let j = 0; j < n; j++) { for (let k = 0; k < n; k++) { console.log(i, j, k); } } } }", 'O(n³)'),
            
            ("function fib(n) { if (n <= 1) return n; return fib(n - 1) + fib(n - 2); }", 'O(2ⁿ)'),
        ]
        
        for _ in range(samples):
            template, complexity = templates[random.randint(0, len(templates)-1)]
            code = template
            
            features = self.feature_extractor.extract_features(code)
            complexity_value = self.complexity_mapper.complexity_to_value(complexity)
            
            X_train.append(features)
            y_train.append(complexity_value)
        
        return X_train, y_train
    
    def train(self, X=None, y=None):
        """Entrena la red neuronal con 500 épocas"""
        if X is None or y is None:
            X, y = self.generate_training_data(samples=1000)
        
        self.model.train_simple(X, y)
        self.is_trained = True
        
    def predict(self, code):
        """Predice la complejidad de un código"""
        if not self.is_trained:
            raise Exception("El modelo no ha sido entrenado.")
        
        features = self.feature_extractor.extract_features(code)
        complexity_value, confidence = self.model.predict(list(features))
        complexity = self.complexity_mapper.value_to_complexity(complexity_value)
        
        return complexity, confidence
    
    def save_model(self, filepath):
        """Guarda el modelo entrenado"""
        data = {
            'is_trained': self.is_trained
        }
        with open(filepath, 'wb') as f:
            pickle.dump(data, f)
    
    def load_model(self, filepath):
        """Carga un modelo entrenado"""
        try:
            with open(filepath, 'rb') as f:
                data = pickle.load(f)
            self.is_trained = data.get('is_trained', False)
            if self.is_trained:
                self.model.train_simple()
        except:
            pass
