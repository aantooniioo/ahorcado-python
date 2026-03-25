from hangman import Hangman

def main():
    print("Bienvenidos al juego del Ahorcado")

    juego = Hangman()
    juego.load("data/words.csv")

    # Mostrar resumen
    juego.resumen_palabras()

    # Validación
    if juego.get_number_of_words() == 30:
        print("\nPalabras listas, ¡adelante!")
    else:
        print("\nVaya, parece que no encontramos todas las palabras necesarias, no podemos dar comienzo al juego.")
        return

    # Pedir nombre
    usuario = input("Introduce tu nombre: ")
    print(f"Hola {usuario}, comienza la partida!")

    # Palabras usadas
    palabras_usadas = []

    # Numero de rondas
    rondas = 3

    for ronda in range(1, rondas + 1):
        print(f"\n--- Ronda {ronda} ---")

        # Seleccionar palabra sin repetir
        while True:
            palabra = juego.get_random_word()
            if palabra not in palabras_usadas:
                palabras_usadas.append(palabra)
                break

        print("Se ha seleccionado una palabra al azar")

        # Mostrar palabra inicial
        juego.mostrar_palabra_oculta(palabra)

        # Lista de letras acertadas
        letras_acertadas = []

        # Contador de intentos
        intentos = 0

        # Limite de intentos
        max_intentos = 9

        while True:
            # Pedir letra
            letra = input("Introduce una letra: ").lower().strip()

            # Validar que solo se introduce una letra
            if len(letra) != 1:
                print("Introduce solo una letra")
                continue

            # Evitar repetir letras
            if letra in letras_acertadas:
                print("Ya has acertado esa letra")
                continue

            # Comprobar letra
            acierto = juego.comprobar_letra(palabra, letra)

            if acierto:
                letras_acertadas.append(letra)
            else:
                intentos += 1
                print(f"Intentos fallidos: {intentos}/{max_intentos}")

                # Dibujo del ahorcado
                juego.dibujar_ahorcado(intentos)

            # Mostrar progreso actualizado
            juego.mostrar_progreso(palabra, letras_acertadas)

            # Comprobar si se ha ganado
            ganado = True
            for l in palabra:
                if l not in letras_acertadas:
                    ganado = False
                    break

            if ganado:
                print("¡Has ganado esta ronda!")
                break

            # Comprobar si se ha perdido
            if intentos >= max_intentos:
                print("Has perdido esta ronda. La palabra era:", palabra)
                break


if __name__ == "__main__":
    main()