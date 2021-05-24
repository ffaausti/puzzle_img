import pygame
import random
import sys
import easygui as g

# Initialization
pygame.init()
# Nazwa okna pygame
pygame.display.set_caption('Puzzle Game')
# Rozmiary okna
s = pygame.display.set_mode((1500, 720))

img_map = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

win_map = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]


def click_image(zmienna1, zmienna2, mapa):
    if zmienna2 - 1 >= 0 and mapa[zmienna2 - 1][zmienna1] == 8:
        mapa[zmienna2][zmienna1], mapa[zmienna2 - 1][zmienna1] = mapa[zmienna2 - 1][zmienna1], mapa[zmienna2][zmienna1]
    elif zmienna2 + 1 <= 2 and mapa[zmienna2 + 1][zmienna1] == 8:
        mapa[zmienna2][zmienna1], mapa[zmienna2 + 1][zmienna1] = mapa[zmienna2 + 1][zmienna1], mapa[zmienna2][zmienna1]
    elif zmienna1 - 1 >= 0 and mapa[zmienna2][zmienna1 - 1] == 8:
        mapa[zmienna2][zmienna1], mapa[zmienna2][zmienna1 - 1] = mapa[zmienna2][zmienna1 - 1], mapa[zmienna2][zmienna1]
    elif zmienna1 + 1 <= 2 and mapa[zmienna2][zmienna1 + 1] == 8:
        mapa[zmienna2][zmienna1], mapa[zmienna2][zmienna1 + 1] = mapa[zmienna2][zmienna1 + 1], mapa[zmienna2][zmienna1]
        

def random_image(mapa):
    for el in range(1000):
        zmienna1 = random.randint(0, 2)
        zmienna2 = random.randint(0, 2)
        click_image(zmienna1, zmienna2, mapa)

#nie wiem czy coś widać
# zdjęcie do układanki
img = pygame.image.load('kotzkapusta.jpg')

random_image(img_map)

s.fill((25, 35, 45))
s.blit(img, (800, 0))

for zmienna2 in range(3):
    for zmienna1 in range(3):
        el = img_map[zmienna2][zmienna1]
        if el == 8:          # 8No need to place pictures
            continue
        dz1 = (el % 3) * 239  # Game block image size setting
        dz2 = (int(el / 3)) * 240
        s.blit(img, (zmienna1 * 239, zmienna2 * 240), (dz1, dz2, 239, 240))

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN:
        if pygame.mouse.get_pressed() == (1, 0, 0):
            mouse_z1, mouse_z2 = pygame.mouse.get_pos()
            if mouse_z1 < 719 and mouse_z2 < 720:
                x = int(mouse_z1 / 239)
                y = int(mouse_z2 / 240)
                click_image(x, y, img_map)
                if img_map == win_map:
                    g.msgbox("Congratulations on completing the puzzle!")
