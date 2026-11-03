

banco_a1 = [
    {
        "texto": "Completa la oración: 'She ___ from Spain.'",
        "opciones": "a) are   b) is",
        "correcta": "b"
    },
    {
        "texto": "Elige la forma correcta en pasado: 'Yesterday, we ___ to the cinema.'",
        "opciones": "a) went   b) goed",
        "correcta": "a"
    }
]
puntuacion = 0

for pregunta in banco_a1:
    print(pregunta["texto"])
    print(pregunta["opciones"])

    respuesta = input("Elige una respuesta (a/b): ").lower()
    if respuesta == pregunta["correcta"]:
        puntuacion += 1
        print("Correcto!")
    else:
        print("Incorrecto!")
print("Tu puntuacion final es: ", puntuacion)



...

print("¡Bienvenido al Test de Nivelación de Inglés!")
print("Vamos a descubrir tu nivel desde A1 hasta C2.")

puntuacion = 0

print("Pregunta 1: Completa la oración: 'She ___ from Spain.'")
print("a) are   b) is")
respuesta1 = input("Elige tu respuesta (a/b): ").lower()
if respuesta1 == "b":
    puntuacion += 1
    print("¡Correcto! Vas muy bien.")
else:
    print("Incorrecto. La respuesta era 'b) is'.")

print("Pregunta 2: Elige la forma correcta en pasado: 'Yesterday, we ___ to the cinema.'")
print("a) goed   b) went")
respuesta2 = input("Elige tu respuesta (a/b): ").lower()
if respuesta2 == "b":
    puntuacion += 1
    print("¡Correcto! Vas muy bien.")
else:
    print("Incorrecto. La respuesta era 'b) went'.")

print("Pregunta 3: Completa la oración. 'If I won the lottery, I ___ a big house.'")
print("a) would buy   b) will buy ")
respuesta3 = input("Elige tu respuesta (a/b): ").lower()
if respuesta3 == "a":
    puntuacion += 1
    print("¡Correcto! Vas muy bien.")
else:
    print("Incorrecto. La respuesta era 'a) would buy'.")

print("Pregunta 4: Selecciona la opción correcta: 'I am looking forward ___ you.'")
print("a) to seeing   b) to see ")
respuesta4 = input("Elige tu respuesta (a/b): ").lower()
if respuesta4 == "a":
    puntuacion += 1
    print("¡Correcto! Vas muy bien.")
else:
    print("Incorrecto. La respuesta era 'a) to seeing'.")


print("Pregunta 5: Completa la estructura avanzada: 'Not only ___ late, but he also forgot his passport.'")
print("a) he arrived   b) did he arrive")
respuesta5 = input("Elige tu respuesta (a/b): ").lower()
if respuesta5 == "b":
    puntuacion += 1
else:
    print("Incorrecto. La respuesta era 'b) did he arrive'.")


print("Pregunta 6: Expresa una deducción lógica en el pasado: 'She ___ the train; there's no other way she could be here so soon.'")
print("a) must have caught   b) should have caught")
respuesta6 = input("Elige tu respuesta (a/b): ").lower()
if respuesta6 == "a":
    puntuacion += 1
else:
    print("Incorrecto. La respuesta era 'a) must have caught'.")


if puntuacion == 6:
    print("¡Felicidades! Tienes un nivel C2 (Nativo/Bilingüe).")
elif puntuacion == 5:
    print("Tienes un nivel C1 (Avanzado).")
elif puntuacion == 4:
    print("Tienes un nivel B2 (Intermedio Alto).")
elif puntuacion == 3:
    print("Tienes un nivel B1 (Intermedio).")
elif puntuacion == 2:
    print("Tienes un nivel A2 (Básico Alto).")
elif puntuacion == 1:
    print("Tienes un nivel A1 (Básico).")
else:
    print("Necesitas estudiar más. Eres nivel Principiante absoluto.")


...

print("¡Bienvenido al Test de Nivelación de Inglés!\n")

# Evaluamos A1
print("--- NIVEL A1 ---")
puntos_a1 = hacer_test(banco_a1)

if puntos_a1 == 1:
    print("¡Excelente! Avanzas al Nivel A2.\n")

    # Evaluamos A2
    print("--- NIVEL A2 ---")
    puntos_a2 = hacer_test(banco_a2)

    if puntos_a2 == 1:
        print("¡Increíble! Avanzas al Nivel B1.\n")
        # Aquí conectarías el B1 siguiendo la misma lógica

        print("--- NIVEL B1 ---")
        puntos_b1 = hacer_test(banco_b1)

        if puntos_b1 == 1:
            print("¡bien hecho! Pasas al Nivel B1.\n")
    else:
        print("Test finalizado. Tu nivel sólido es A1 (en transición a A2).")
else:
    print("Test finalizado. Tu nivel sugerido para comenzar es A1.")

    return puntuacion

hacer_test(banco_c2)