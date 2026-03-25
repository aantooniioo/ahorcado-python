class Hangman():
    def __init__(self):
        self.words = []

    def load(self, filename):
        archivo = open(filename, "r", encoding="utf-8")

        # saltar la cabecera
        archivo.readline()

        for linea in archivo:
            palabra = linea.strip()
            self.words.append(palabra)

        archivo.close()

    def get_number_of_words(self):
        return len(self.words)