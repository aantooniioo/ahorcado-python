class Hangman():
    def __init__(self):
        self.words = []

    def load_words(self, ruta):
        archivo = open(ruta, "r")

        # saltar la cabecera
        archivo.readline()

        for linea in archivo:
            palabra = linea.strip()
            self.words.append(palabra)

        archivo.close()