import time

class Hangman:
    def __init__(self):
        self.words = []

    def load(self, filename):
        archivo = open(filename, "r", encoding="utf-8")

        # saltar cabecera
        archivo.readline()

        print("Cargando palabras", end="")

        for linea in archivo:
            palabra = linea.strip()

            # animación (puntitos)
            print(".", end="", flush=True)
            time.sleep(0.05)

            # evitar palabras vacías
            if palabra == "":
                continue

            # evitar palabras con menos de 5 letras
            if len(palabra) < 5:
                continue

            # evitar duplicados
            if palabra in self.words:
                continue

            self.words.append(palabra)

        archivo.close()
        print("\nCarga completada")

    def get_number_of_words(self):
        return len(self.words)

    def resumen_palabras(self):
        if len(self.words) == 0:
            return

        total_letras = 0
        palabra_mas_larga = self.words[0]

        for palabra in self.words:
            total_letras += len(palabra)

            if len(palabra) > len(palabra_mas_larga):
                palabra_mas_larga = palabra

        media = total_letras / len(self.words)

        print("\nResumen de palabras:")
        print("Numero total:", len(self.words))
        print("Longitud media:", round(media, 2))
        print("Palabra mas larga:", palabra_mas_larga)