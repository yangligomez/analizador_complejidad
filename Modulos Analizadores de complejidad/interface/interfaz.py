"""
INTERFAZ - Interfaz Gráfica de Usuario
Módulo responsable de la presentación visual y la interacción
con el usuario en la aplicación de análisis de complejidad.
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import threading
import re
import random
import sys
import os

# Agregar la ruta de Backend al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from Backend.backend import (
    CodeFeatureExtractor,
    ComplexityMapper,
    NeuralNetworkComplexityAnalyzer
)
import os


# ============================================================================
# INTERFAZ GRÁFICA MODERNA
# ============================================================================

class ComplexityAnalyzerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Analizador de Complejidad - Red Neuronal")
        self.root.geometry("1400x900")
        self.root.configure(bg='#0a0e27')
        
        # Colores modernos
        self.primary_bg = '#0a0e27'      # Azul muy oscuro
        self.secondary_bg = '#1a1f3a'    # Azul oscuro
        self.card_bg = '#232d4a'         # Azul gris
        self.accent_color = '#00d4ff'    # Cian brillante
        self.accent_purple = '#b366ff'   # Púrpura
        self.success_color = '#00ff88'   # Verde brillante
        self.error_color = '#ff3333'     # Rojo
        self.fg_color = '#e0e0e0'        # Gris claro
        
        self.analyzer = None
        self.is_model_loaded = False
        self.analysis_in_progress = False
        self.last_code_analyzed = None
        self.last_confidence = 0
        
        self.create_widgets()
        self.setup_styles()
        self.initialize_model()
        
        # Configurar cierre de la ventana
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
    def setup_styles(self):
        """Configura estilos modernos de ttk"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Colores de fondo
        style.configure('TFrame', background=self.primary_bg)
        style.configure('Card.TFrame', background=self.card_bg)
        style.configure('TLabel', background=self.primary_bg, foreground=self.fg_color)
        
        # Botones
        style.configure('TButton', font=('Segoe UI', 10, 'bold'), padding=12)
        style.map('TButton',
                  background=[('active', self.accent_purple)],
                  foreground=[('active', '#ffffff')])
        
        # Botones especiales
        style.configure('Accent.TButton', background=self.accent_color, foreground='#000000')
        style.map('Accent.TButton',
                  background=[('active', self.accent_purple)])
        
        # Labels especiales
        style.configure('Header.TLabel', background=self.primary_bg, foreground=self.accent_color, 
                       font=('Segoe UI', 18, 'bold'))
        style.configure('Subheader.TLabel', background=self.primary_bg, foreground=self.fg_color, 
                       font=('Segoe UI', 11, 'bold'))
        style.configure('Status.TLabel', background=self.primary_bg, foreground=self.success_color,
                       font=('Segoe UI', 9))
        
        # LabelFrames
        style.configure('Card.TLabelframe', background=self.card_bg, foreground=self.accent_color,
                       borderwidth=1, relief='flat', padding=15)
        style.configure('Card.TLabelframe.Label', background=self.card_bg, foreground=self.accent_color,
                       font=('Segoe UI', 11, 'bold'))
        
    def create_widgets(self):
        """Crea los widgets con diseño moderno"""
        
        # ===================== HEADER SUPERIOR =====================
        header_frame = tk.Frame(self.root, bg=self.primary_bg, height=80)
        header_frame.pack(fill=tk.X, padx=0, pady=0)
        header_frame.pack_propagate(False)
        
        # Línea decorativa superior
        top_line = tk.Frame(header_frame, bg=self.accent_color, height=3)
        top_line.pack(fill=tk.X, side=tk.TOP)
        
        # Contenido del header
        header_content = tk.Frame(header_frame, bg=self.primary_bg)
        header_content.pack(fill=tk.BOTH, expand=True, padx=20, pady=15)
        
        # Título principal
        title = tk.Label(header_content, text="🧠  ANALIZADOR DE COMPLEJIDAD", 
                        font=('Segoe UI', 20, 'bold'), bg=self.primary_bg, fg=self.accent_color)
        title.pack(side=tk.LEFT, anchor=tk.W)
        
        # Subtítulo
        subtitle = tk.Label(header_content, text="Red Neuronal con 500 Épocas", 
                           font=('Segoe UI', 10), bg=self.primary_bg, fg=self.fg_color)
        subtitle.pack(side=tk.LEFT, anchor=tk.W, padx=(5, 0))
        
        # Estado (derecha)
        self.status_label = tk.Label(header_content, text="⏳ Cargando modelo...", 
                                     font=('Segoe UI', 10, 'bold'), bg=self.primary_bg, 
                                     fg=self.accent_purple)
        self.status_label.pack(side=tk.RIGHT, anchor=tk.E)
        
        # ===================== CONTENEDOR PRINCIPAL =====================
        main_container = tk.Frame(self.root, bg=self.primary_bg)
        main_container.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # ===================== PANEL IZQUIERDO (Código) =====================
        left_panel = tk.Frame(main_container, bg=self.card_bg, relief=tk.FLAT, highlightthickness=1, 
                             highlightbackground=self.accent_color)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        # Header del panel izquierdo
        left_header = tk.Frame(left_panel, bg=self.accent_color, height=40)
        left_header.pack(fill=tk.X, padx=0, pady=0)
        left_header.pack_propagate(False)
        
        left_title = tk.Label(left_header, text="📝  CÓDIGO JAVASCRIPT", 
                             font=('Segoe UI', 11, 'bold'), bg=self.accent_color, fg='#000000')
        left_title.pack(side=tk.LEFT, padx=15, pady=10)
        
        # Botones de acción
        button_frame = tk.Frame(left_panel, bg=self.card_bg)
        button_frame.pack(fill=tk.X, padx=12, pady=12)
        
        load_btn = tk.Button(button_frame, text="📂 Cargar Archivo", command=self.load_file,
                            bg=self.accent_color, fg='#000000', font=('Segoe UI', 9, 'bold'),
                            relief=tk.FLAT, padx=12, pady=8, cursor='hand2')
        load_btn.pack(side=tk.LEFT, padx=5)
        
        clear_btn = tk.Button(button_frame, text="🗑️ Limpiar", command=self.clear_code,
                             bg=self.error_color, fg='#ffffff', font=('Segoe UI', 9, 'bold'),
                             relief=tk.FLAT, padx=12, pady=8, cursor='hand2')
        clear_btn.pack(side=tk.LEFT, padx=5)
        
        # Editor de código
        editor_frame = tk.Frame(left_panel, bg=self.card_bg)
        editor_frame.pack(fill=tk.BOTH, expand=True, padx=12, pady=(0, 12))
        
        self.code_text = scrolledtext.ScrolledText(
            editor_frame, height=25, width=50, bg='#0d1221', fg='#d4d4d4',
            font=('Consolas', 10), wrap=tk.WORD, insertbackground=self.accent_color,
            relief=tk.FLAT, borderwidth=0, selectbackground=self.accent_purple,
            selectforeground='#ffffff'
        )
        self.code_text.pack(fill=tk.BOTH, expand=True)
        self.code_text.insert(tk.END, "// Pega aquí tu código JavaScript")
        self.code_text.bind('<FocusIn>', self.on_code_focus_in)
        self.code_text.bind('<FocusOut>', self.on_code_focus_out)
        self.code_text.bind('<KeyRelease>', self.on_code_change)
        
        # ===================== PANEL DERECHO (Análisis) =====================
        right_panel = tk.Frame(main_container, bg=self.primary_bg)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # ========== Card de Análisis ==========
        analysis_card = tk.Frame(right_panel, bg=self.card_bg, relief=tk.FLAT, highlightthickness=1,
                                highlightbackground=self.accent_color)
        analysis_card.pack(fill=tk.X, pady=(0, 12))
        
        # Header de análisis
        analysis_header = tk.Frame(analysis_card, bg=self.accent_color, height=40)
        analysis_header.pack(fill=tk.X)
        analysis_header.pack_propagate(False)
        
        analysis_title = tk.Label(analysis_header, text="📊  RESULTADOS", 
                                 font=('Segoe UI', 11, 'bold'), bg=self.accent_color, fg='#000000')
        analysis_title.pack(side=tk.LEFT, padx=15, pady=10)
        
        # Botón Analizar
        self.analyze_btn = tk.Button(analysis_card, text="🔍 ANALIZAR COMPLEJIDAD", 
                                    command=self.analyze_code, bg=self.success_color, 
                                    fg='#000000', font=('Segoe UI', 10, 'bold'),
                                    relief=tk.FLAT, padx=15, pady=12, cursor='hand2')
        self.analyze_btn.pack(fill=tk.X, padx=15, pady=15)
        
        # Resultado principal
        result_container = tk.Frame(analysis_card, bg=self.card_bg)
        result_container.pack(fill=tk.BOTH, padx=15, pady=10)
        
        result_label = tk.Label(result_container, text="Complejidad Detectada:", 
                               font=('Segoe UI', 9, 'bold'), bg=self.card_bg, fg=self.fg_color)
        result_label.pack(anchor=tk.W)
        
        result_display = tk.Frame(result_container, bg=self.secondary_bg, relief=tk.FLAT,
                                 highlightthickness=1, highlightbackground=self.accent_color)
        result_display.pack(fill=tk.X, pady=(8, 0))
        
        self.complexity_result = tk.Label(result_display, text="O(?)", 
                                         font=('Segoe UI', 48, 'bold'),
                                         bg=self.secondary_bg, fg=self.accent_color)
        self.complexity_result.pack(pady=20)
        
        # Confianza
        confidence_frame = tk.Frame(analysis_card, bg=self.card_bg)
        confidence_frame.pack(fill=tk.X, padx=15, pady=10)
        
        confidence_label = tk.Label(confidence_frame, text="Nivel de Confianza:", 
                                   font=('Segoe UI', 9, 'bold'), bg=self.card_bg, fg=self.fg_color)
        confidence_label.pack(anchor=tk.W)
        
        self.confidence_var = tk.DoubleVar(value=0)
        self.confidence_bar = ttk.Progressbar(confidence_frame, variable=self.confidence_var, 
                                             length=200, mode='determinate', maximum=100)
        self.confidence_bar.pack(fill=tk.X, pady=(5, 0))
        
        self.confidence_text = tk.Label(confidence_frame, text="0%", 
                                       font=('Segoe UI', 9), bg=self.card_bg, fg=self.accent_color)
        self.confidence_text.pack(anchor=tk.E, pady=(3, 0))
        
        # ========== Card de Explicación ==========
        explanation_card = tk.Frame(right_panel, bg=self.card_bg, relief=tk.FLAT, highlightthickness=1,
                                   highlightbackground=self.accent_color)
        explanation_card.pack(fill=tk.BOTH, expand=True)
        
        # Header de explicación
        explanation_header = tk.Frame(explanation_card, bg=self.accent_purple, height=40)
        explanation_header.pack(fill=tk.X)
        explanation_header.pack_propagate(False)
        
        explanation_title = tk.Label(explanation_header, text="📖  EXPLICACIÓN", 
                                    font=('Segoe UI', 11, 'bold'), bg=self.accent_purple, fg='#ffffff')
        explanation_title.pack(side=tk.LEFT, padx=15, pady=10)
        
        # Texto de explicación
        explanation_container = tk.Frame(explanation_card, bg=self.card_bg)
        explanation_container.pack(fill=tk.BOTH, expand=True, padx=0, pady=0)
        
        self.explanation_text = scrolledtext.ScrolledText(
            explanation_container, height=20, width=40, bg='#0d1221', fg='#d4d4d4',
            font=('Segoe UI', 9), wrap=tk.WORD, relief=tk.FLAT, borderwidth=0,
            selectbackground=self.accent_purple, selectforeground='#ffffff'
        )
        self.explanation_text.pack(fill=tk.BOTH, expand=True, padx=0, pady=0)
        
        # Contenido inicial de la explicación
        info_text = {
            'O(1)': 'Tiempo constante. No depende del tamaño de entrada.',
            'O(log n)': 'Búsqueda binaria. Divide el problema a la mitad.',
            'O(n)': 'Tiempo lineal. Itera sobre todos los elementos.',
            'O(n log n)': 'Ordenamiento eficiente (merge sort, quick sort).',
            'O(n²)': 'Bucles anidados. Bubble sort, insertion sort.',
            'O(n³)': 'Tres bucles anidados. Operaciones con matrices.',
            'O(2ⁿ)': 'Exponencial. Muy ineficiente (Fibonacci recursivo).',
        }
        
        self.explanation_text.insert(tk.END, "GUÍA DE COMPLEJIDADES\n")
        self.explanation_text.insert(tk.END, "=" * 40 + "\n\n")
        for complexity, explanation in info_text.items():
            self.explanation_text.insert(tk.END, f"{complexity}\n{explanation}\n\n")
        
        self.explanation_text.config(state=tk.DISABLED)
        
    def initialize_model(self):
        """Inicializa el modelo en un thread separado"""
        def load_model_thread():
            try:
                self.status_label.config(text="⏳ Cargando modelo entrenado...")
                self.root.update()
                
                if os.path.exists("complexity_model.pkl"):
                    self.analyzer = NeuralNetworkComplexityAnalyzer(epochs=500)
                    self.analyzer.load_model("complexity_model.pkl")
                    self.is_model_loaded = True
                    self.status_label.config(text="✅ Modelo cargado (archivo guardado)", 
                                           fg=self.success_color)
                else:
                    self.status_label.config(text="⏳ Entrenando modelo (500 épocas)...")
                    self.root.update()
                    
                    self.analyzer = NeuralNetworkComplexityAnalyzer(epochs=500)
                    self.analyzer.train()
                    self.analyzer.save_model("complexity_model.pkl")
                    self.is_model_loaded = True
                    self.status_label.config(text="✅ Modelo entrenado y listo", 
                                           fg=self.success_color)
                    
            except Exception as e:
                self.status_label.config(text=f"❌ Error al inicializar", fg=self.error_color)
                messagebox.showerror("Error", f"Error al inicializar: {str(e)}")
        
        thread = threading.Thread(target=load_model_thread, daemon=True)
        thread.start()
    
    def on_closing(self):
        """Maneja el cierre de la aplicación con un mensaje bacano"""
        goodbye_messages = [
            "🚀 ¡Gracias por usar el ANALIZADOR DE COMPLEJIDAD!\n\n"
            "Has hecho un GRAN TRABAJO analizando algoritmos hoy.\n"
            "Recuerda: ¡Un buen algoritmo es un algoritmo EFICIENTE! ⚡\n\n"
            "¡Hasta pronto, CODIFICADOR! 🎯",
            
            "🎊 ¡MISIÓN CUMPLIDA!\n\n"
            "Espero que hayas aprendido mucho sobre complejidad asintótica.\n"
            "Sigue optimizando tu código y hazlo IMPARABLE 💪\n\n"
            "¡Vuelve pronto! 👨‍💻",
            
            "⚡ ¡ANÁLISIS COMPLETADO!\n\n"
            "Tu viaje a través de la COMPLEJIDAD ASINTÓTICA ha sido ÉPICO.\n"
            "Que tus algoritmos siempre sean O(n) o mejor 🏆\n\n"
            "¡Hasta la próxima, CAMPEÓN! 🌟",
            
            "🧠 ¡POWER DOWN! 🔌\n\n"
            "Has conquistado el mundo de los algoritmos hoy.\n"
            "Que la eficiencia te acompañe siempre en tu código.\n\n"
            "¡Que la Red Neuronal no te olvide! 🤖💙",
        ]
        
        goodbye_message = random.choice(goodbye_messages)
        
        if messagebox.askokcancel("¡Hasta Luego!", goodbye_message + "\n\n¿Deseas CERRAR la aplicación?"):
            self.root.destroy()
    
    def on_code_focus_in(self, event):
        """Al hacer focus en el área de código"""
        if self.code_text.get(1.0, tk.END).strip() == "// Pega aquí tu código JavaScript":
            self.code_text.delete(1.0, tk.END)
            self.code_text.config(fg='#d4d4d4')
    
    def on_code_focus_out(self, event):
        """Al perder focus del área de código"""
        if not self.code_text.get(1.0, tk.END).strip():
            self.code_text.insert(tk.END, "// Pega aquí tu código JavaScript")
            self.code_text.config(fg='#808080')
    
    def on_code_change(self, event=None):
        """Se llama cuando hay cambios en el código"""
        if not self.analysis_in_progress:
            self.analyze_btn.config(state=tk.NORMAL, text="🔍 Analizar Complejidad")
    
    def load_file(self):
        """Carga un archivo JavaScript"""
        file_path = filedialog.askopenfilename(
            title="Selecciona un archivo JavaScript",
            filetypes=[("JavaScript files", "*.js"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    code = f.read()
                
                # Validar que sea JavaScript
                if not self.is_javascript_code(code):
                    messagebox.showerror(
                        "Error - Archivo No Válido",
                        "❌ EL ARCHIVO NO CONTIENE CÓDIGO JAVASCRIPT\n\n"
                        "Por favor, carga un archivo JavaScript (.js) válido.\n\n"
                        "Este analizador SOLO funciona con código JavaScript."
                    )
                    return
                
                self.code_text.delete(1.0, tk.END)
                self.code_text.insert(1.0, code)
                self.code_text.config(fg='#d4d4d4')
                self.analyze_btn.config(state=tk.NORMAL, text="🔍 Analizar Complejidad")
                messagebox.showinfo("Éxito", "✓ Archivo JavaScript cargado correctamente")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo abrir el archivo: {str(e)}")
    
    def clear_code(self):
        """Limpia el área de código y la información anterior"""
        self.code_text.delete(1.0, tk.END)
        self.code_text.insert(tk.END, "// Pega aquí tu código JavaScript")
        self.code_text.config(fg='#808080')
        
        self.complexity_result.config(text="O(?)")
        self.confidence_var.set(0)
        self.confidence_text.config(text="0%")
        self.explanation_text.config(state=tk.NORMAL)
        self.explanation_text.delete(1.0, tk.END)
        
        # Restaurar la guía inicial
        info_text = {
            'O(1)': 'Tiempo constante. No depende del tamaño de entrada.',
            'O(log n)': 'Búsqueda binaria. Divide el problema a la mitad.',
            'O(n)': 'Tiempo lineal. Itera sobre todos los elementos.',
            'O(n log n)': 'Ordenamiento eficiente (merge sort, quick sort).',
            'O(n²)': 'Bucles anidados. Bubble sort, insertion sort.',
            'O(n³)': 'Tres bucles anidados. Operaciones con matrices.',
            'O(2ⁿ)': 'Exponencial. Muy ineficiente (Fibonacci recursivo).',
        }
        self.explanation_text.insert(tk.END, "GUÍA DE COMPLEJIDADES\n")
        self.explanation_text.insert(tk.END, "=" * 40 + "\n\n")
        for complexity, explanation in info_text.items():
            self.explanation_text.insert(tk.END, f"{complexity}\n{explanation}\n\n")
        
        self.explanation_text.config(state=tk.DISABLED)
        self.last_code_analyzed = None
        self.last_confidence = 0
        self.analyze_btn.config(state=tk.NORMAL)
    
    def is_javascript_code(self, code: str) -> bool:
        """Verifica si el código es JavaScript válido"""
        if not code or not code.strip():
            return False
        
        code_lower = code.lower()
        
        # RECHAZAR: Detectar otros lenguajes PRIMERO
        # Python
        if 'def ' in code or '__name__' in code or 'self.' in code:
            return False
        if re.search(r'\bdef\s+\w+\s*\(', code):
            return False
        
        # Java
        if 'public class' in code or 'public static' in code or 'System.out' in code:
            return False
        if '@Override' in code or '@Deprecated' in code or 'import java' in code:
            return False
        
        # C/C++
        if '#include' in code or 'std::' in code or 'cout' in code or 'cin' in code:
            return False
        if 'int main' in code or 'printf' in code or 'scanf' in code:
            return False
        
        # ACEPTAR: Verificar que tenga estructura JavaScript
        js_patterns = [
            r'\bfunction\s+\w+\s*\(',
            r'\bconst\s+\w+\s*=',
            r'\blet\s+\w+\s*=',
            r'\bvar\s+\w+\s*=',
            r'=>',
            r'\bfor\s*\(',
            r'\bwhile\s*\(',
            r'\bif\s*\(',
            r'\breturn\s+',
            r'\.map\s*\(',
            r'\.filter\s*\(',
            r'\.forEach\s*\(',
        ]
        
        matches = sum(1 for pattern in js_patterns if re.search(pattern, code))
        return matches >= 2
    
    def analyze_code(self):
        """Analiza el código JavaScript"""
        if not self.is_model_loaded:
            messagebox.showwarning("Advertencia", "⏳ El modelo aún se está cargando. Espera un momento.")
            return
        
        if self.analysis_in_progress:
            messagebox.showinfo("Info", "⚙️ Ya hay un análisis en curso.")
            return
        
        code = self.code_text.get(1.0, tk.END).strip()
        
        if not code or code == "// Pega aquí tu código JavaScript":
            messagebox.showwarning(
                "Código Vacío",
                "⚠️ Por favor, ingresa código JavaScript primero.\n\n"
                "Pega tu código en el área de texto de la izquierda."
            )
            return
        
        # Validar que sea JavaScript
        if not self.is_javascript_code(code):
            messagebox.showerror(
                "❌ Error - Lenguaje No Soportado",
                "❌ ESTE CÓDIGO NO ES JAVASCRIPT\n\n"
                "Este analizador SOLO funciona con código JavaScript.\n\n"
                "Por favor, proporciona SOLO código JavaScript."
            )
            return
        
        # Prevenir análisis concurrentes
        self.analysis_in_progress = True
        self.analyze_btn.config(state=tk.DISABLED, text="⏳ ANALIZANDO...")
        
        def analyze_thread():
            try:
                complexity, confidence = self.analyzer.predict(code)
                confidence_percent = int(confidence * 100)
                
                self.complexity_result.config(text=complexity)
                self.confidence_var.set(confidence_percent)
                self.confidence_text.config(text=f"{confidence_percent}%")
                
                explanation = self.generate_explanation(code, complexity)
                self.explanation_text.config(state=tk.NORMAL)
                self.explanation_text.delete(1.0, tk.END)
                self.explanation_text.insert(tk.END, explanation)
                self.explanation_text.config(state=tk.DISABLED)
                
                self.last_code_analyzed = code
                self.last_confidence = confidence_percent
                
            except Exception as e:
                messagebox.showerror("Error", f"Error durante el análisis: {str(e)}")
            finally:
                self.analysis_in_progress = False
                self.analyze_btn.config(state=tk.NORMAL, text="🔍 ANALIZAR COMPLEJIDAD")
        
        thread = threading.Thread(target=analyze_thread, daemon=True)
        thread.start()
    
    def generate_explanation(self, code, complexity):
        """Genera una explicación detallada del análisis"""
        explanation = f"┌─ ANÁLISIS COMPLETADO ─────────────────┐\n\n"
        explanation += f"🎯 COMPLEJIDAD: {complexity}\n\n"
        
        # Análisis detallado de características
        for_loops = len(re.findall(r'\bfor\s*\(', code))
        while_loops = len(re.findall(r'\bwhile\s*\(', code))
        nested_loops = CodeFeatureExtractor.count_nested_loops(code)
        recursion = CodeFeatureExtractor.count_recursion_calls(code)
        array_methods = len(re.findall(r'\.(push|pop|map|filter|reduce|forEach|find|some|every)\s*\(', code))
        search_methods = len(re.findall(r'\.(indexOf|includes|findIndex)\s*\(', code))
        sort_methods = len(re.findall(r'\.(sort|reverse)\s*\(', code))
        functions = len(re.findall(r'\bfunction\s+\w+|const\s+\w+\s*=\s*\(', code))
        
        explanation += "📊 CARACTERÍSTICAS:\n"
        explanation += f"  FOR: {for_loops} | WHILE: {while_loops}\n"
        explanation += f"  Máx Anidación: {nested_loops} | Recursión: {'Sí ✓' if recursion > 0 else 'No'}\n"
        explanation += f"  Array: {array_methods} | Búsquedas: {search_methods}\n\n"
        
        # Nota aclaratoria si hay múltiples FOR
        if for_loops > nested_loops + 1:
            explanation += f"💡 NOTA: Hay {for_loops} FOR totales pero solo {nested_loops} nivel(es) de anidación.\n"
            explanation += f"   Algunos bucles son independientes entre sí.\n\n"
        
        # Factor dominante
        explanation += "🔑 FACTOR DOMINANTE:\n"
        
        if for_loops + while_loops == 0:
            explanation += "  • Sin bucles → O(1)\n"
        elif nested_loops >= 3:
            explanation += f"  • {nested_loops} niveles anidados → O(n³)\n"
        elif nested_loops >= 2:
            explanation += f"  • {nested_loops} niveles anidados → O(n²)\n"
        elif for_loops + while_loops >= 2:
            explanation += f"  • Múltiples bucles (no anidados) → O(n)\n"
        else:
            explanation += f"  • Un bucle → O(n)\n"
        
        if recursion > 0 and nested_loops == 0:
            explanation += f"  • Recursión detectada → puede ser O(2ⁿ)\n"
        
        explanation += "\n"
        
        interpretations = {
            'O(1)': '⚡ CONSTANTE\nMuy rápido. No depende del tamaño.',
            'O(log n)': '🔍 LOGARÍTMICO\nBúsqueda binaria. Muy eficiente.',
            'O(n)': '📈 LINEAL\nUna pasada sobre datos.',
            'O(n log n)': '✨ CUASILINEAL\nMerge sort, Quick sort.',
            'O(n²)': '⚠️  CUADRÁTICO\nBucles anidados. Lento.',
            'O(n³)': '❌ CÚBICO\nMuy lento. Tres bucles.',
            'O(2ⁿ)': '💥 EXPONENCIAL\nMuy ineficiente. Evitar.',
        }
        
        explanation += "ℹ️  DEFINICIÓN:\n"
        explanation += f"  {interpretations.get(complexity, 'Complejidad desconocida')}\n"
        
        return explanation
