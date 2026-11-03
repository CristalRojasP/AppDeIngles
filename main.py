import os

from datetime import datetime, timedelta
from preguntas import banco_a1, banco_a2, banco_b1, banco_b2, banco_c1, banco_c2

nombre_usuario = input("¡Hola! Ingresa tu nombre:").title()
# Pedir correo con validación básica
while True:
    correo = input("Ingresa tu correo electrónico (ej. usuario@gmail.com): ").lower().strip()
    if "@" in correo and "." in correo:
        break # Correo válido, salimos del bucle
    else:
        print(" Error: Formato de correo inválido. Asegúrate de incluir '@' y un dominio (ejemplo: correo@gmail.com).\n")

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
                    print(f"\nLo siento, {nombre_usuario}. Ya tienes un registro reciente.")
                    print(
                        f"Hiciste el examen hace {dias_transcurridos} días. Debes esperar a completar tu ciclo de 90 días.")
                    exit()  # Esta función de Python detiene y cierra el programa de inmediato
                else:
                    print("\nTu último examen fue hace más de 90 días. Puedes realizarlo nuevamente.")


if not correo_registrado:
    print("\n¡Correo verificado! Eres un usuario nuevo en el sistema. Iniciando test de nivelación...\n")

#ZONA 2: EJECUCIÓN

def hacer_test(banco_nivel):
    puntuacion = 0
    errores = 0
    for pregunta in banco_nivel:
        print(pregunta["texto"])
        print(pregunta["opciones"])
        respuesta = input("Elige tu respuesta (a/b): ").lower()

        if respuesta == pregunta["correcta"]:
            puntuacion += 1
            print("¡Correcto!\n")  # El \n da un salto de línea para que se vea más limpio
        else:
            print("Incorrecto!\n")
            errores += 1

        if errores == 2:
            print("Has acumulado 2 errores. No es posible alcanzar la puntuación mínima.\n")
            break

    return puntuacion

#ZONA 3

print("¡Bienvenido al Test de Nivelación de Inglés!\n")

# --- ESCALÓN 1: A1 ---
print("--- NIVEL A1 ---")
puntos_a1 = hacer_test(banco_a1)

if puntos_a1 >= 4:
    print("¡Excelente " + nombre_usuario + "! Avanzas al Nivel A2.\n")

    # --- ESCALÓN 2: A2 (Nota cómo esto está DENTRO del if anterior) ---
    print("--- NIVEL A2 ---")
    puntos_a2 = hacer_test(banco_a2)

    if puntos_a2 >= 4:
        print("¡Increíble " + nombre_usuario + "! Avanzas al Nivel B1.\n")

        # --- ESCALÓN 3: B1 ---
        print("--- NIVEL B1 ---")
        puntos_b1 = hacer_test(banco_b1)

        if puntos_b1 >= 4:
            print("¡Muy bien " + nombre_usuario + "! Avanzas al Nivel B2.\n")

            #---ESCALÓN 4: B2---
            print("--- NIVEL B2 ---")
            puntos_b2 = hacer_test(banco_b2)

            if puntos_b2 >= 4:
                print("¡Bien hecho " + nombre_usuario + "! Avanzas al Nivel C1.\n")

                #---ESCALÓN 5: C1---
                print("--- NIVEL C1 ---")
                puntos_c1 = hacer_test(banco_c1)

                if puntos_c1 >= 4:
                    print("¡Correcto " + nombre_usuario + "! Avanzas al Nivel C2.\n")

                    #---ESCALÓN 6: C2---
                    print("--- NIVEL C2 ---")
                    puntos_c2 = hacer_test(banco_c2)

                    if puntos_c2 >= 4:
                        print("¡Lo hiciste muy bien " + nombre_usuario + "! Haz obtenido un nivel C2\n")
                        nivel_final = "C2"


                    else:
                        print("Test finalizado " + nombre_usuario + ". Obtuviste", puntos_c2,"puntos en este nivel. Tu nivel sólido es C1")
                        nivel_final = "C1"


                else:
                    print("Test finalizado " + nombre_usuario + ". Obtuviste", puntos_c1,"puntos en este nivel. Tu nivel sólido es B2")
                    nivel_final = "B2"

            else:
                print("Test finalizado " + nombre_usuario + ". Obtuviste", puntos_b2,"puntos en este nivel. Tu nivel sólido es B1")
                nivel_final = "B1"

        else:
           print("Test finalizado " + nombre_usuario + ". Obtuviste", puntos_b1,"puntos en este nivel. Tu nivel sólido es A2.")
           nivel_final = "A2"

    else:
        print("Test finalizado " +  nombre_usuario + ". Obtuviste", puntos_a2,"puntos en este nivel. Tu nivel sólido es A1.")
        nivel_final = "A1"

else:
    print("Test finalizado " + nombre_usuario + ". Obtuviste", puntos_a1,"puntos en este nivel. Tu nivel sugerido para comenzar es A1.")
    nivel_final = "0"

# Guardar resultados con fecha
fecha_actual = datetime.now().strftime("%Y-%m-%d")

with open("resultados_examen.txt", "a", encoding="utf-8") as archivo:
    archivo.write(f"[{correo}] Nombre: {nombre_usuario} | Nivel: {nivel_final} | Fecha: {fecha_actual}\n")