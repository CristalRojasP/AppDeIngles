import os
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
from preguntas import banco_a1

ventana = tk.Tk()
ventana.title("Sistema de Evaluación de Inglés")
ventana.geometry("400x350")

#creaciones de widgets
titulo = tk.Label(ventana, text="¡Bienvenido al Test de Nivelación!", font=("Arial", 14, "bold"))
titulo.pack(pady=15)

label_nombre = tk.Label(ventana, text="Nombre completo:")
label_nombre.pack(pady=2)

caja_nombre = tk.Entry(ventana, width=35)
caja_nombre.pack(pady=5)

label_correo = tk.Label(ventana, text="Correo electrónico:")
label_correo.pack(pady=2)

caja_correo = tk.Entry(ventana, width=35)
caja_correo.pack(pady=5)


# 3. LÓGICA DE NEGOCIO (FUNCIÓN DEL BOTÓN)
def iniciar_evaluacion():
    nombre = caja_nombre.get().title().strip()
    correo = caja_correo.get().lower().strip()

    # Validaciones de campos vacíos y formato
    if not nombre or not correo:
        messagebox.showwarning("Campos vacíos", "Por favor, completa tanto tu nombre como tu correo.")
        return

    if "@" not in correo or "." not in correo:
        messagebox.showerror("Correo inválido", "Ingresa un correo válido (ejemplo: usuario@gmail.com).")
        return

    # Verificación de Cooldown en el archivo
    correo_registrado = False
    if os.path.exists("resultados_examen.txt"):
        with open("resultados_examen.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                if correo in linea:
                    correo_registrado = True
                    partes = linea.split("|")
                    fragmento_fecha = partes[2]
                    fecha_str = fragmento_fecha.replace("Fecha:", "").strip()
                    fecha_examen = datetime.strptime(fecha_str, "%Y-%m-%d")
                    dias_transcurridos = (datetime.now() - fecha_examen).days

                    if dias_transcurridos < 90:
                        messagebox.showerror(f"\nLo siento, {nombre}. Ya tienes un registro reciente."
                        "Hiciste el examen hace {dias_transcurridos} días. Debes esperar a completar tu ciclo")

                        return

    # Si todo está correcto y es un usuario habilitado
    messagebox.showinfo("Acceso Permitido",
                        f"¡Hola {nombre}!\nTu correo fue verificado con éxito. Puedes iniciar tu examen.")
    ventana.withdraw()
    abrir_ventana_examen()

boton_inicar = tk.Button(ventana, text="Iniciar Test", command=iniciar_evaluacion, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
boton_inicar.pack(pady=20)


def abrir_ventana_examen():

    ventana_2 = tk.Toplevel()
    ventana_2.title("Sistema de Evaluación de Inglés")
    ventana_2.geometry("400x350")
    indice = 0
    pregunta_actual = banco_a1[indice]


    enunciado_actual = pregunta_actual["texto"]

    pregunta_label = tk.Label(ventana_2, text=enunciado_actual, font=("Arial", 12), wraplength=350, justify="center")
    pregunta_label.pack(pady=10)

    for opcion in pregunta_actual["opciones"]:
        # Creamos un botón por cada opción disponible en la pregunta
        boton_opcion = tk.Button(ventana_2, text=opcion, width=35, command=lambda op=opcion: evaluar_respuesta(op))
        boton_opcion.pack(pady=5)

#creaciones de widgets
    titulo = tk.Label(ventana_2, text="¡Bienvenido al Test de Nivelación!", font=("Arial", 14, "bold"))
titulo.pack(pady=15)



ventana.mainloop()