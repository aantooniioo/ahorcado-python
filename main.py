from hangman import Ahorcado

def main():
    print("Bienvenidos al juego del Ahorcado")

    #Creamos el objeto del juego (Ahorcado)
    juego = Ahorcado()

    #Cargamos las palabras desde el CSV (data/words.csv)
    juego.cargar_palabras("data/words.csv")

    #Mostramos cuántas palabras se han cargado    
    print("Numero de palabras:", len(juego.palabras))


if __name__ == "__main__":
    main()
