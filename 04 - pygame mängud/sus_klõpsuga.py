import pygame
import random

LAIUS = 640
KÕRGUS = 480
KIIRUS = 0.5

kell = pygame.time.Clock()
ekraan = pygame.display.set_mode((LAIUS, KÕRGUS))
pygame.init()

AMOGUS_PAREM = pygame.image.load("amogus.png")
AMOGUS_VASAK = pygame.transform.flip(AMOGUS_PAREM, True, False)

BEEBI = pygame.image.load("babby.png")

FONT = pygame.font.SysFont("Comic Sans MS", 24)

mäng_käib = True
amogus = AMOGUS_PAREM

skoor = 0

amogus_x = 50
amogus_y = 200
h_kiirus = 0
v_kiirus = 0

beebi_x = 300
beebi_y = 200


def beebi_juhuslik_punkt():
    x = random.randint(0, LAIUS - beebi_rect.w)
    y = random.randint(0, KÕRGUS - beebi_rect.h)
    return x, y


while mäng_käib:
    dt = kell.tick(60)
    
    for sisend in pygame.event.get():
        if sisend.type == pygame.QUIT:
            mäng_käib = False
        elif sisend.type == pygame.MOUSEBUTTONDOWN:
            klõpsu_asukoht = pygame.mouse.get_pos()
            print("Klõpsasid sellisesse punkti:", klõpsu_asukoht)
            if beebi_rect.collidepoint(klõpsu_asukoht):
                beebi_x, beebi_y = beebi_juhuslik_punkt()
                

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
    beebi_rect = ekraan.blit(BEEBI, (beebi_x, beebi_y))
    amogus_rect = ekraan.blit(amogus, (amogus_x, amogus_y))
    
    if amogus_rect.colliderect(beebi_rect):
        beebi_x, beebi_y = beebi_juhuslik_punkt()
        skoor += 1
        
    tekst = FONT.render(f"Skoor: {skoor}", True, (0, 0, 0))
    ekraan.blit(tekst, (40, 40))

    pygame.display.flip()  # salvestab joonistused

pygame.quit()
