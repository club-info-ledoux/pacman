import random
import tkinter

MANUEL = False

# Décommentez cette ligne si vous voulez jouer le fantome
# MANUEL = True


def init(map: list[list[str]]) -> None:
    # initialisez les variables qui vous seront utiles
    pass

def play(map: list[list[str]], couleur: str) -> str:


    # TODO : être intelligent
    return random.choices(["q", "d", "z", "s"])[0]  # = touche appuyée
