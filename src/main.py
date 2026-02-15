import random

# Juego del Ahorcado
# Autor: Eliab Carrera
# Fecha: 15/02/2026

PALABRAS = ["python", "programacion", "teclado", "internet", "ahorcado"]

def elegir_palabra():
    return random.choice(PALABRAS)

def mostrar_palabra(palabra, letras_correctas):
    resultado = ""
    for letra in palabra:
        if letra in letras_correctas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado.strip()

def jugar():
    palabra = elegir_palabra()
    letras_correctas = set()
    letras_incorrectas = set()
    intentos = 6

    print("=== JUEGO DEL AHORCADO ===")

    while intentos > 0:
        print("\nPalabra:", mostrar_palabra(palabra, letras_correctas))
        print("Errores:", ", ".join(letras_incorrectas) if letras_incorrectas else "Ninguno")
        print("Intentos restantes:", intentos)

        letra = input("Ingresa una letra: ").lower()

        # Validación básica
        if len(letra) != 1 or not letra.isalpha():
            print("Ingresa solo una letra válida.")
            continue

        if letra in letras_correctas or letra in letras_incorrectas:
            print("Ya usaste esa letra.")
            continue

        if letra in palabra:
            letras_correctas.add(letra)
            print("¡Correcto!")
        else:
            letras_incorrectas.add(letra)
            intentos -= 1
            print("Incorrecto.")

        # Verificar si ganó
        gano = True
        for l in palabra:
            if l not in letras_correctas:
                gano = False
                break

        if gano:
            print("\n¡Ganaste!")
            print("La palabra era:", palabra)
            return

    print("\nPerdiste.")
    print("La palabra era:", palabra)

jugar()
