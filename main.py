from hangman import Hangman

def main():
    print("Bienvenidos al juego del Ahorcado")

    # Creamos el objeto del juego
    juego = Hangman()

    # Cargamos las palabras desde el CSV
    juego.load("data/words.csv")

    # Mostrar resumen
    juego.resumen_palabras()

    # Validación mínima
    if juego.get_number_of_words() == 30:
        print("\nPalabras listas, ¡adelante!")
    else:
        print("\nVaya, parece que no encontramos todas las palabras necesarias, no podemos dar comienzo al juego.")
        return

    # Mostrar número de palabras
    print("Numero de palabras:", juego.get_number_of_words())


if __name__ == "__main__":
    main()