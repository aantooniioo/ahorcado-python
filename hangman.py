class Hangman():
    def __init__(self):
        self.palabras = []

    def cargar_palabras(self, ruta):
        archivo = open(ruta, "r")

        # saltar la cabecera
        archivo.readline()

        for linea in archivo:
            palabra = linea.strip()
            self.palabras.append(palabra)

        archivo.close()