#RUFFIN Evann 1G5
import winsound
from soundcopie import *
import pygame


winsound.PlaySound("assets//start.wav",winsound.SND_ASYNC)

pygame.mixer.init()

pygame.mixer.Channel(0).play(pygame.mixer.Sound("assets//chomp.wav"))
pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets//eat.wav"))


fenetre.mainloop()