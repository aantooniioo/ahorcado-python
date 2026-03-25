from hangman import Hangman

def main():
    print("Bienvenidos al juego del Ahorcado")

    juego = Hangman()
    juego.load("data/words.csv")

    # Mostrar resumen
    juego.resumen_palabras()

    # Validación
    if juego.get_number_of_words() == 30:
        print("Palabras listas, ¡adelante!")
    else:
        print("Vaya, parece que no encontramos todas las palabras necesarias, no podemos dar comienzo al juego.")
        return

    # Pedir nombre
    usuario = input("Introduce tu nombre: ")

    print(f"Hola {usuario}, comienza la partida!")

    # Seleccionar palabra
    palabra = juego.get_random_word()

    print("Se ha seleccionado una palabra al azar")


if __name__ == "__main__":
    main()