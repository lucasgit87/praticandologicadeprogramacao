import pygame


pygame.mixer.init()
pygame.init()


pygame.mixer.music.load('mix_50s (audio-joiner.com).mp3')


pygame.mixer.music.play()


print("Tocando música... aperte ENTER para parar.")
input()
