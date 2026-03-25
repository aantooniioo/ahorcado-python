from hangman import Hangman

def main():
    print("Bienvenidos al juego del Ahorcado")

    # Creamos el objeto del juego
    juego = Hangman()

    # Cargamos las palabras desde el CSV
    juego.load("data/words.csv")

    # Validación mínima
    if juego.get_number_of_words() < 30:
        print("Error: se necesitan al menos 30 palabras para jugar")
        return

    # Mostrar número de palabras
    print("Numero de palabras:", juego.get_number_of_words())


if __name__ == "__main__":
    main()