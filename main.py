# main.py

import os
import numpy as np
import matplotlib.pyplot as plt

# Importamos el archivo de funciones que creaste
import Funciones as fn

# ---------------------------------------------------------
# PARTE 1: Prueba de las funciones matemáticas
# ---------------------------------------------------------
print("--- Probando funciones importadas ---")
print("Suma (5 + 3) =", fn.suma(5, 3))
print("Resta (10 - 4) =", fn.resta(10, 4))
print("Multiplicación (6 * 2) =", fn.multi(6, 2))
print("-----------------------------------")

# ---------------------------------------------------------
# PARTE 2: Creación de carpeta y generación de gráficas
# ---------------------------------------------------------
resultados = "resultados"

# Verificamos si la carpeta existe; si no, la creamos
if not os.path.exists(resultados):
    os.makedirs(resultados)
    print(f"Directorio '{resultados}/' creado exitosamente.")

# Generamos los datos para la gráfica
x = np.linspace(0, 10, 100)
y = x**2

# Configuramos la gráfica
plt.figure()
plt.plot(x, y, color='blue', linestyle='-', linewidth=2, label='y = x^2')
plt.title("Gráfica generada desde main.py")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.legend()
plt.grid(True)

# Definimos las rutas exactas donde se guardarán los archivos
ruta_png = os.path.join(resultados, "grafica_parabola.png")
ruta_eps = os.path.join(resultados, "grafica_parabola.eps")

# Guardamos las figuras ANTES de mostrarlas
plt.savefig(ruta_png, dpi=300)
plt.savefig(ruta_eps)

print(f"¡Éxito! Las imágenes se han guardado en la carpeta '{resultados}/'.")

# Opcional: mostrar la gráfica en pantalla al ejecutar
plt.show()