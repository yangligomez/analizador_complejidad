"""
MAIN - Punto de Entrada de la Aplicación
Módulo principal que inicia la interfaz gráfica
del Analizador de Complejidad Asintótica.

"""

import tkinter as tk
import sys
import os

# Agregar las carpetas de módulos al path
sys.path.insert(0, os.path.dirname(__file__))

from interface.interfaz import ComplexityAnalyzerGUI


def main():
    root = tk.Tk()
    gui = ComplexityAnalyzerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
