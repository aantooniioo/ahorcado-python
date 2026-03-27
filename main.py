"""
Archivo principal del juego del ahorcado.

Se encarga de:
- Controlar el flujo del juego
- Gestionar rondas
- Interacción con el usuario
- Guardar datos en CSV
"""

from hangman import Hangman
import random
import uuid
from datetime import datetime
from typing import List

# Importar configuración
from config import (
    MAX_INTENTOS_FACIL,
    MAX_INTENTOS_NORMAL,
    MAX_INTENTOS_DIFICIL,
    PISTAS_FACIL,
    PISTAS_NORMAL,
    PISTAS_DIFICIL,
    NUM_RONDAS
)


def main() -> None:
    """
    Función principal que ejecuta el juego del ahorcado.
    """

    print("Bienvenidos al juego del Ahorcado")

    juego: Hangman = Hangman()
    juego.load("data/words.csv")

    # Mostrar resumen
    juego.resumen_palabras()

    # Validación de palabras
    if juego.get_number_of_words() == 30:
        print("\nPalabras listas, ¡adelante!")
    else:
        print("\nVaya, parece que no encontramos todas las palabras necesarias, no podemos dar comienzo al juego.")
        return

    # Pedir nombre
    usuario: str = input("Introduce tu nombre: ")
    print(f"Hola {usuario}, comienza la partida!")

    # Datos de partida
    game_id: str = str(uuid.uuid4())
    start_date: datetime = datetime.now()
    puntuacion: int = 0

    # Estadísticas
    total_intentos: int = 0
    total_aciertos: int = 0
    total_fallos: int = 0

    # Selección de dificultad
    print("\nSelecciona dificultad:")
    print("1. Facil (9 intentos)")
    print("2. Normal (7 intentos)")
    print("3. Dificil (5 intentos)")

    opcion: str = input("Elige opción: ")

    if opcion == "1":
        max_intentos: int = MAX_INTENTOS_FACIL
    elif opcion == "2":
        max_intentos = MAX_INTENTOS_NORMAL
    else:
        max_intentos = MAX_INTENTOS_DIFICIL

    palabras_usadas: List[str] = []
    rondas: int = NUM_RONDAS

    for ronda in range(1, rondas + 1):
        print(f"\n--- Ronda {ronda} ---")

        # Reiniciar pistas según dificultad
        if opcion == "1":
            pistas_restantes: int = PISTAS_FACIL
        elif opcion == "2":
            pistas_restantes = PISTAS_NORMAL
        else:
            pistas_restantes = PISTAS_DIFICIL

        # Seleccionar palabra no repetida
        while True:
            palabra: str = juego.get_random_word()
            if palabra not in palabras_usadas:
                palabras_usadas.append(palabra)
                break

        print("Se ha seleccionado una palabra al azar")

        juego.mostrar_palabra_oculta(palabra)

        letras_acertadas: List[str] = []
        letras_falladas: List[str] = []
        intentos: int = 0

        while True:
            letra: str = input("Introduce una letra o 'pista': ").lower().strip()

            # PISTA
            if letra == "pista":
                if pistas_restantes > 0:
                    pistas_restantes -= 1

                    letras_no: List[str] = []
                    for l in palabra:
                        if l not in letras_acertadas:
                            letras_no.append(l)

                    if len(letras_no) > 0:
                        pista: str = random.choice(letras_no)
                        print("Pista:", pista)

                    print("Pistas restantes:", pistas_restantes)
                else:
                    print("No tienes pistas")
                continue

            # Validaciones
            if len(letra) != 1:
                print("Introduce solo una letra")
                continue

            if letra in letras_acertadas or letra in letras_falladas:
                print("Ya has usado esa letra")
                continue

            # Comprobar letra
            acierto: bool = juego.comprobar_letra(palabra, letra)

            if acierto:
                letras_acertadas.append(letra)
            else:
                intentos += 1
                letras_falladas.append(letra)

                print(f"Intentos fallidos: {intentos}/{max_intentos}")
                print(f"Intentos restantes: {max_intentos - intentos}")

                juego.dibujar_ahorcado(intentos, max_intentos)

            # Mostrar estado
            juego.mostrar_progreso(palabra, letras_acertadas)
            print("Letras falladas:", " ".join(letras_falladas))

            # Comprobar victoria
            ganado: bool = True
            for l in palabra:
                if l not in letras_acertadas:
                    ganado = False
                    break

            if ganado:
                print("¡Has ganado esta ronda!")
                puntuacion += 1
            else:
                if intentos >= max_intentos:
                    print("Has perdido esta ronda. La palabra era:", palabra)

            # Fin de ronda
            if ganado or intentos >= max_intentos:
                total_intentos += intentos

                if ganado:
                    total_aciertos += 1
                else:
                    total_fallos += 1

                # Guardar ronda
                round_id: str = str(uuid.uuid4())
                with open("data/rounds_in_games.csv", "a", encoding="utf-8") as f:
                    f.write(f"{game_id},{palabra},{usuario},{round_id},{intentos},{ganado}\n")

                break

    # Fin de partida
    end_date: datetime = datetime.now()

    print(f"\nPartida finalizada. Tu puntuación es: {puntuacion}/{NUM_RONDAS}. Gracias por jugar, {usuario}.")

    # Medalla
    if puntuacion == NUM_RONDAS:
        medalla: str = "Excelente"
    elif puntuacion == 2:
        medalla = "Muy bien"
    elif puntuacion == 1:
        medalla = "Puedes mejorar"
    else:
        medalla = "Sigue practicando"

    print("Resultado:", medalla)

    # Resumen
    print("\nResumen de la partida:")
    print("Rondas ganadas:", total_aciertos)
    print("Rondas perdidas:", total_fallos)
    print("Intentos totales:", total_intentos)

    # Guardar partida
    with open("data/games.csv", "a", encoding="utf-8") as f:
        f.write(f"{game_id},{usuario},{start_date},{end_date},{puntuacion}\n")

    # Guardar resumen
    with open("data/resumen_partida.txt", "w", encoding="utf-8") as f:
        f.write("RESUMEN DE PARTIDA\n")
        f.write("-------------------\n")
        f.write(f"Jugador: {usuario}\n")
        f.write(f"Puntuación: {puntuacion}/{NUM_RONDAS}\n")
        f.write(f"Medalla: {medalla}\n")
        f.write(f"Rondas ganadas: {total_aciertos}\n")
        f.write(f"Rondas perdidas: {total_fallos}\n")
        f.write(f"Intentos totales: {total_intentos}\n")


if __name__ == "__main__":
    main()