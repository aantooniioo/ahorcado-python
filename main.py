from hangman import Hangman

def main():
    print("Bienvenidos al juego del Ahorcado")

    #Creamos el objeto del juego (Ahorcado)
    juego = Hangman()

    #Cargamos las palabras desde el CSV (data/words.csv)
    juego.load_words("data/words.csv")

    #Mostramos cuántas palabras se han cargado    
    print("Numero de palabras:", len(juego.words))


if __name__ == "__main__":
    main()
