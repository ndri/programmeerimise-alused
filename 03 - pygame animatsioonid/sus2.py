import pygame

LAIUS = 640
KÕRGUS = 480

kell = pygame.time.Clock()
ekraan = pygame.display.set_mode((LAIUS, KÕRGUS))
pygame.init()

amogus_parem = pygame.image.load("amogus.png")
amogus_vasak = pygame.transform.flip(amogus_parem, True, False)
amogus = amogus_parem

amogus_x = 50
amogus_y = 200

kiirus = 0.1
h_kiirus = kiirus
v_kiirus = kiirus


while True:
    dt = kell.tick(120)
    
    sisend = pygame.event.poll()
    if sisend.type == pygame.QUIT:
        break
    
    amogus_x += h_kiirus * dt
    amogus_y += v_kiirus * dt

    if amogus_x + amogus.get_width() > LAIUS:
        h_kiirus = -kiirus
        amogus = amogus_vasak
    elif amogus_x < 0:
        h_kiirus = kiirus
        amogus = amogus_parem
        
    if amogus_y + amogus.get_height() > KÕRGUS:
        v_kiirus = -kiirus
    elif amogus_y < 0:
        v_kiirus = kiirus

    ekraan.fill((155, 89, 182))
    ekraan.blit(amogus, (amogus_x, amogus_y))

    pygame.display.flip()  # salvestab joonistused

pygame.quit()

# pygame.org/docs/ref/draw.html
