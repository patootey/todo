import pygame
import requests

li = [1, 2, 3]

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


countries = requests.get("https://restcountries.com/v3.1/all")
countries = countries.json()


def search(key: str):
    for country in countries:

        for code in country["name"]:
            if code != "nativeName" and key.lower() in country["name"][code].lower():
                for name in country["currencies"]:
                    code = name
                return (
                    country["name"]["common"],
                    country["currencies"][code]["name"],
                    code,
                    country["currencies"][code]["symbol"],
                    country["flags"]["png"],
                )

            elif code == "nativeName":
                for symbol in country["name"][code]:
                    for z in country["name"][code][symbol]:
                        if key.lower() in country["name"][code][symbol][z].lower():
                            for name in country["currencies"]:
                                code = name
                            return (
                                country["name"]["common"],
                                country["currencies"][code]["name"],
                                code,
                                country["currencies"][code]["symbol"],
                                country["flags"]["png"],
                            )
        try:
            for code in country["currencies"]:
                if key.lower() == code.lower():
                    return (
                        country["name"]["common"],
                        country["currencies"][code]["name"],
                        code,
                        country["currencies"][code]["symbol"],
                        country["flags"]["png"],
                    )

                for symbol in country["currencies"][code]:
                    if key.lower() == country["currencies"][code][symbol].lower():
                        return (
                            country["name"]["common"],
                            country["currencies"][code]["name"],
                            code,
                            country["currencies"][code]["symbol"],
                            country["flags"]["png"],
                        )
        except:
            pass

    return f"Fant ikke landet '{key}'."
