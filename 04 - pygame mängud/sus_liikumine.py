import pygame

LAIUS = 640
KÕRGUS = 480
KIIRUS = 0.5

kell = pygame.time.Clock()
ekraan = pygame.display.set_mode((LAIUS, KÕRGUS))
pygame.init()

AMOGUS_PAREM = pygame.image.load("amogus.png")
AMOGUS_VASAK = pygame.transform.flip(AMOGUS_PAREM, True, False)

mäng_käib = True
amogus = AMOGUS_PAREM

amogus_x = 50
amogus_y = 200
h_kiirus = 0
v_kiirus = 0

while mäng_käib:
    dt = kell.tick(60)
    
    for sisend in pygame.event.get():
        if sisend.type == pygame.QUIT:
            mäng_käib = False

    h_kiirus = 0
    v_kiirus = 0

    vajutatud = pygame.key.get_pressed()
    if vajutatud[pygame.K_UP]:
        v_kiirus += -KIIRUS
    if vajutatud[pygame.K_DOWN]:
        v_kiirus += KIIRUS

        
    if vajutatud[pygame.K_LEFT]:
        h_kiirus += -KIIRUS
    if vajutatud[pygame.K_RIGHT]:
        h_kiirus += KIIRUS
        
    if h_kiirus and v_kiirus:
        h_kiirus /= 2**0.5
        v_kiirus /= 2**0.5
    
    amogus_x += h_kiirus * dt
    amogus_y += v_kiirus * dt

    ekraan.fill((155, 89, 182))
    ekraan.blit(amogus, (amogus_x, amogus_y))

    pygame.display.flip()  # salvestab joonistused

pygame.quit()
