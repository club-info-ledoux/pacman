import random

MANUEL = False

# Décommentez cette ligne si vous voulez jouer le pacman
# MANUEL = True


def init(map: list[list[str]]) -> None:
    # initialisez les variables qui vous seront utiles
    pass

def play(map: list[list[str]]) -> str:


    
    # TODO : être intelligent
    return random.choices(["q", "d", "z", "s"])[0]  # = touche appuyée
