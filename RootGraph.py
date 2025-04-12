import tkinter as tk
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from tkinter import PhotoImage
from PIL import Image, ImageTk

def encontrarRaices():
    limpiarFrame()
    tk.Label(frameContenido, text="", font=("Arial", 12, "bold"), fg="#00008B", bg="lightblue").pack() #Espacio 

    tk.Label(frameContenido, text="RAÍCES DE UNA ECUACIÓN POLINÓMICA NO LINEAL", font=("Arial", 12, "bold"), fg="#00008B", bg="lightblue").pack() #Título
    tk.Label(frameContenido, text="", font=("Arial", 12, "bold"), fg="#00008B", bg="lightblue").pack() #espacio interlineal
    tk.Label(frameContenido, text="Ingrese la función f(x):", font=("Arial", 12, "bold"), fg="#00008B", bg="lightblue").pack()

    entry_function = tk.Entry(frameContenido, font=("Arial", 12, "bold"), fg="#00008B", bg="lightblue")
    entry_function.pack()

    def calcular():
        try:
            expr_str = entry_function.get()
            x = sp.symbols('x')
            expr = sp.sympify(expr_str)

            f_lambdified = sp.lambdify(x, expr, 'numpy')

            x_vals = np.linspace(-10, 10, 400)
            y_vals = f_lambdified(x_vals)

            roots = []
            for i in range(len(x_vals) - 1):
                if y_vals[i] * y_vals[i + 1] < 0:
                    root_approx = (x_vals[i] + x_vals[i + 1]) / 2
                    roots.append(root_approx)

            if roots:
                #root_label.config(text=f"Raíces encontradas: {', '.join(map(lambda r: f'{r:.4f}', roots))}")
                root_label.config(text=f"Raíces encontradas: {', '.join(map(lambda r: f'{r:.4f}', roots))}", font=("Arial", 12, "bold"))

            else:
                root_label.config(text="No se encontraron raíces en el intervalo.")

            funcionPlot(expr, roots)

        except Exception as e:
            root_label.config(text=f"Error: {e}")

    def limpiarVentana():
        entry_function.delete(0, tk.END)
        root_label.config(text="")
        info_label.config(text="")
        for widget in canvas_frame.winfo_children():
            widget.destroy()

    tk.Button(frameContenido, text="Encontrar Raíces", command=calcular, fg="white", bg="green", font=("Arial", 12, "bold"), height=2, width=20).pack(side="left", padx=10, pady=(10, 3))
    tk.Button(frameContenido, text="Limpiar Ventana", command=limpiarVentana, fg="white", bg="red", font=("Arial", 12, "bold"), height=2, width=20).pack(side="left", padx=10, pady=(10, 3))

def funcionPlot(expr, roots):
    x = sp.symbols('x')
    f_lambdified = sp.lambdify(x, expr, 'numpy')

    x_vals = np.linspace(-10, 10, 400)
    y_vals = f_lambdified(x_vals)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(x_vals, y_vals, label=f'f(x) = {expr}')
    
    ax.axhline(0, color='darkgray', linewidth=1.5)
    ax.axvline(0, color='darkgray', linewidth=1.5)

    ax.xaxis.label.set_color('blue')
    ax.yaxis.label.set_color('blue')
    ax.tick_params(axis='x', colors='blue')
    ax.tick_params(axis='y', colors='blue')

    for root in roots:
        ax.axvline(root, color='red', linestyle='--')
        ax.plot(root, 0, 'ro', markersize=8)

    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.grid(True, linestyle='--', linewidth=1)
    ax.legend()

    for widget in canvas_frame.winfo_children():
        widget.destroy()

    canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

def limpiarFrame():
    for widget in frameContenido.winfo_children():
        widget.destroy()

def mostrarPresentacion():
    # Limpiar entrada
    limpiarFrame()

    root_label.config(text="")
    info_label.config(text="")

    tk.Label(frameContenido, text="", font=("Arial", 12, "bold"), fg="#00008B", bg="lightblue").pack() 
    tk.Label(frameContenido, text="", font=("Arial", 12, "bold"), fg="#00008B", bg="lightblue").pack() 
    tk.Label(frameContenido, text="BIENVENIDOS A LA APLICACIÓN", font=("Comic Sans MS", 14, "bold"), fg="#00008B", bg="lightblue").pack() #Título
    tk.Label(frameContenido, text="RAÍCES DE UNA ECUACIÓN POLINÓMICA NO LINEAL", font=("Arial", 12, "bold"), fg="#00008B", bg="lightblue").pack() #Título
    tk.Label(frameContenido, text="", font=("Arial", 12, "bold"), fg="#00008B", bg="lightblue").pack() 
    tk.Label(frameContenido, text="", font=("Arial", 12, "bold"), fg="#00008B", bg="lightblue").pack()
    # Cargar la imagen
    try:
            # Leer la imagen mediante PIL.
            image = Image.open("Graph.png")  
            image = image.resize((400, 400))  
            image_tk = ImageTk.PhotoImage(image)
            image_label = tk.Label(frameContenido, image=image_tk, bg="#FFD700")
            image_label.image = image_tk  # Mantiene una referencia a la imagen
            image_label.pack(pady=20)# Mostrar imagen
            
    except Exception as e:
            print(f"Error al cargar la imagen: {e}")

    tk.Label(frameContenido, text="", font=("Arial", 12, "bold"), fg="#00008B", bg="lightblue").pack() 
    tk.Label(frameContenido, text="", font=("Arial", 12, "bold"), fg="#00008B", bg="lightblue").pack() 
    tk.Label(frameContenido, text="RootGraph", font=("Comic Sans MS", 20, "bold"), fg="#00008B", bg="lightblue").pack() 


def mostrarAyuda():
    limpiarFrame()
    tk.Label(frameContenido, text="\n\nINSTRUCCIONES DE USO:\n\n", bg="lightblue", font=("Comic Sans MS", 14,"bold"), fg="#00008B").pack(pady=20)
    tk.Label(frameContenido, text="\n1. Ingresar la función en el cuadro correspondiente\nEjemplos de Funciones validas\nx**3 - 2*x + 1\nsin(x) - x/2\n"
             f"2. Hacer un click en el boton Encontrar las raíces"
             f"\n3. Visualización gráfica\n4. Hacer un click en el botón Limpiar ventana",bg="lightblue", font=("Comic Sans MS", 14)).pack(pady=20)


def mostrarAcerca():
        limpiarFrame()
        tk.Label(frameContenido, text="\n\n\n\nCálculo de racíces de ecuciones no lineales.\nRootGraph v1.0", bg="lightblue", font=("Comic Sans MS", 14,"bold"), fg="#00008B").pack(pady=20)
        # Listado de contenidos para las etiquetas.
        textos = [
            "\nDesarrollado por: Leonel Coyla Idme",
            "Alfredo Mamani Canqui",
            "Elqui Yeye Pari Condori",
            "Juan Reynaldo Paredes Quispe",
            "José Pánfilo Tito Lipa",
          ]

        # Construir las etiquetas utilizando un bucle.
        for texto in textos:
            tk.Label(frameContenido, text=texto, bg="lightblue", font=("Comic Sans MS", 14)).pack(pady=4)

        label_Acerca_de = tk.Label(frameContenido, text= "\n\nLanzamiento : 11 de abril  2025", font=("Comic Sans MS", 14),fg="#003366",bg="lightblue")
        label_Acerca_de.pack(pady=(1,10))
        label_Acerca_de = tk.Label(frameContenido, text= "Contacto: lcoyla@unap.edu.pe", font=("Comic Sans MSl", 14),fg="#003366",bg="lightblue")
        label_Acerca_de.pack(pady=(1,10))

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Buscador de Raíces")
root.geometry("900x900")
root.config(bg="lightblue")  # Color de fondo para el fondo principal

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

menu_bar.add_command(label="Presentación", command=mostrarPresentacion)
menu_bar.add_command(label="Gráfico", command=encontrarRaices)
menu_bar.add_command(label="Ayuda", command=mostrarAyuda)
menu_bar.add_command(label="Acerca de", command=mostrarAcerca)

main_frame = tk.Frame(root, bg="lightblue")  # Fondo de color similar al de la raíz
main_frame.pack(pady=10)

frameContenido = tk.Frame(main_frame, bg="lightblue")  # Fondo de color similar al de la raíz
frameContenido.pack()

root_label = tk.Label(main_frame, text="", bg="lightblue")
root_label.pack()

info_label = tk.Label(main_frame, text="", fg="blue", bg="lightblue")
info_label.pack()

canvas_frame = tk.Frame(main_frame, bg="lightblue")  # Fondo de color similar al de la raíz
canvas_frame.pack()

root.mainloop()
