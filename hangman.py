import time
import random

class Hangman:
    def __init__(self):
        self.words = []

    def load(self, filename):
        archivo = open(filename, "r", encoding="utf-8")

        # Saltar cabecera
        archivo.readline()

        print("Cargando palabras", end="")

        for linea in archivo:
            palabra = linea.strip()

            # Animación (puntitos)
            print(".", end="", flush=True)
            time.sleep(0.05)

            # Evitar palabras vacías
            if palabra == "":
                continue

            # Evitar palabras con menos de 5 letras
            if len(palabra) < 5:
                continue

            # Evitar duplicados
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

    def get_random_word(self):
        return random.choice(self.words)
    
    def mostrar_palabra_oculta(self, palabra):
        resultado = ""

        # Mejor visual
        for letra in palabra:
            resultado += "_ "

        print("Palabra:", resultado.strip())

    def comprobar_letra(self,palabra, letra):
        if letra in palabra:
            print("¡Correcto!")
            return True
        else:
            print("Fallaste")
            return False
        
    def mostrar_progreso(self, palabra, letras_acertadas):
        resultado = ""

        for letra in palabra:
            if letra in letras_acertadas:
                resultado += letra + " "
            else:
                # MODIFICADO
                resultado += "_ "

        print("Palabra:", resultado.strip())

    # Ahora escalado según dificultad
    def dibujar_ahorcado(self, intentos, max_intentos):
        estados = [
            """
            
            
            
            
            -----
            """,
            """
            |
            |
            |
            |
            -----
            """,
            """
            ---------
            |
            |
            |
            -----
            """,
            """
            ---------
            |       |
            |
            |
            -----
            """,
            """
            ---------
            |       |
            |       O
            |
            -----
            """,
            """
            ---------
            |       |
            |       O
            |       |
            -----
            """,
            """
            ---------
            |       |
            |       O
            |      \\|
            -----
            """,
            """
            ---------
            |       |
            |       O
            |      \\|/
            -----
            """,
            """
            ---------
            |       |
            |       O
            |      \\|/
            |      /
            -----
            """,
            """
            ---------
            |       |
            |       O
            |      \\|/
            |      / \\
            -----
            """
        ]

        total_estados = len(estados) - 1

        # Escalado proporcional
        indice = int(intentos * total_estados / max_intentos)

        print(estados[indice])