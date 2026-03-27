"""
Clase Hangman.

Se encarga de:
- Cargar palabras desde un CSV
- Gestionar la lógica del juego
- Mostrar progreso de la palabra
- Dibujar el ahorcado
"""

import time
import random
from typing import List

from config import LOAD_DELAY, HANGMAN_STATES


class Hangman:
    def __init__(self) -> None:
        """
        Inicializa la clase Hangman.
        """
        self.words: List[str] = []
        self.load_delay: float = LOAD_DELAY
        self.estados: List[str] = HANGMAN_STATES

    def load(self, filename: str) -> None:
        """
        Carga palabras desde un archivo CSV.

        Filtra:
        - Palabras vacías
        - Palabras con menos de 5 letras
        - Palabras duplicadas
        """
        archivo = open(filename, "r", encoding="utf-8")

        archivo.readline()

        print("Cargando palabras", end="")

        for linea in archivo:
            palabra = linea.strip()

            print(".", end="", flush=True)
            time.sleep(self.load_delay)

            if palabra == "":
                continue

            if len(palabra) < 5:
                continue

            if palabra in self.words:
                continue

            self.words.append(palabra)

        archivo.close()
        print("\nCarga completada")

    def get_number_of_words(self) -> int:
        """
        Devuelve el número de palabras cargadas.
        """
        return len(self.words)

    def resumen_palabras(self) -> None:
        """
        Muestra estadísticas de las palabras cargadas.
        """
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

    def get_random_word(self) -> str:
        """
        Devuelve una palabra aleatoria.
        """
        return random.choice(self.words)

    def mostrar_palabra_oculta(self, palabra: str) -> None:
        """
        Muestra la palabra oculta.
        """
        resultado = ""

        for _ in palabra:
            resultado += "_ "

        print("Palabra:", resultado.strip())

    def comprobar_letra(self, palabra: str, letra: str) -> bool:
        """
        Comprueba si una letra está en la palabra.
        """
        if letra in palabra:
            print("¡Correcto!")
            return True
        else:
            print("Fallaste")
            return False

    def mostrar_progreso(self, palabra: str, letras_acertadas: List[str]) -> None:
        """
        Muestra el progreso de la palabra.
        """
        resultado = ""

        for letra in palabra:
            if letra in letras_acertadas:
                resultado += letra + " "
            else:
                resultado += "_ "

        print("Palabra:", resultado.strip())

    def dibujar_ahorcado(self, intentos: int, max_intentos: int) -> None:
        """
        Dibuja el estado del ahorcado.
        """
        total_estados = len(self.estados) - 1

        indice = max(1, int(intentos * total_estados / max_intentos))

        print(self.estados[indice])