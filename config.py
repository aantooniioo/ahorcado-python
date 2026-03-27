MAX_INTENTOS_FACIL = 9
MAX_INTENTOS_NORMAL = 7
MAX_INTENTOS_DIFICIL = 5

PISTAS_FACIL = 999
PISTAS_NORMAL = 2
PISTAS_DIFICIL = 0

NUM_RONDAS = 3

# Hangman
LOAD_DELAY = 0.05

HANGMAN_STATES = [
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