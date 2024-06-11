import pygame
import requests

li = [1, 2, 3, 4, 5, 6, 7]

for list in li:
    print(list)


# Definer Sirkel-klassen
class Sirkel:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def tegn(self, skjerm):
        pygame.draw.circle(skjerm, self.color, (self.x, self.y), self.radius)
        pygame.draw.rect(skjerm, self.color, (self.x, self.y))


# Initialiser Pygame
pygame.init()

# Sett opp skjermen
bredde, hoyde = 800, 600
skjerm = pygame.display.set_mode((bredde, hoyde))
pygame.display.set_caption("Sirkel med Pygame")

# Opprett en sirkel
min_sirkel = Sirkel(400, 300, 50, (255, 0, 0))

# Hovedløkke
kjører = True
while kjører:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            kjører = False

    # Fyll skjermen med hvit farge
    skjerm.fill((255, 255, 255))

    # Tegn sirkelen
    min_sirkel.tegn(skjerm)

    # Oppdater skjermen
    pygame.display.flip()

# Avslutt Pygame
pygame.quit()
