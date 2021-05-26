import pygame

LAIUS = 640
KÕRGUS = 480

kell = pygame.time.Clock()
ekraan = pygame.display.set_mode((LAIUS, KÕRGUS))
pygame.init()

amogus = pygame.image.load("amogus.png")

amogus_x = 50
amogus_y = 200
kiirus = 0.5

while True:
    dt = kell.tick(120)
    
    sisend = pygame.event.poll()
    if sisend.type == pygame.QUIT:
        break
    
    amogus_x += kiirus * dt

    if amogus_x + amogus.get_width() > LAIUS:
        kiirus = -0.5
        amogus = pygame.transform.flip(amogus, True, True)
    elif amogus_x < 0:
        kiirus = 0.5
        amogus = pygame.transform.flip(amogus, True, True)

    ekraan.fill((155, 89, 182))

    ekraan.blit(amogus, (amogus_x, amogus_y))

    pygame.display.flip()  # salvestab joonistused

pygame.quit()

# pygame.org/docs/ref/draw.html
