import pygame

pygame.init()
win = pygame.display.set_mode((1550, 800))
nebo = pygame.image.load('./figs/небо1.jpeg')
nebo = pygame.transform.scale(nebo, (1550, 800))
stena = pygame.image.load('./figs/земля1.jpeg')
stena = pygame.transform.scale(stena, (1550, 200))
stup = pygame.image.load('./figs/земля1.jpeg')
stup = pygame.transform.scale(stena, (200, 50))
image_sprite = [pygame.image.load("./figs/мариостоит.png"), pygame.image.load("./figs/мраиоидет.png")]
x = 580
y = 530
count = 0
Rect1 = pygame.Rect(x, y, 50, 70)
Rect2 = pygame.Rect(0, 600, 1550, 100)
Rect3 = pygame.Rect(50, 300, 200, 1)
Rect4 = pygame.Rect(350, 400, 200, 1)
Rect5 = pygame.Rect(650, 500, 200, 1)
Rect6 = pygame.Rect(1250, 250, 200, 1)
clock = pygame.time.Clock()
angle = False
run = True
while run:
    for i in pygame.event.get():
        keys = pygame.key.get_pressed()
        if i.type == pygame.QUIT:
            run = False
    if Rect1.x > 1550:
        Rect1.x = -49
        Rect1.y -= 10
    if Rect1.x < -49:
        Rect1.x = 1549
        Rect1.y -= 15
    if count >= len(image_sprite):
        count = 0
    image = image_sprite[count]
    povorot = pygame.transform.flip(image, angle, False)
    if keys[pygame.K_LEFT]:
        Rect1.x -= 12
        count += 1
        angle = True
    if keys[pygame.K_RIGHT]:
        Rect1.x += 12
        count += 1
        angle = False
    if keys[pygame.K_SPACE]:
        if Rect1.y >= 530 and Rect1.y > 529 or Rect1.y == 335 and Rect1.x > 301 and Rect1.x < 549 \
                or Rect1.y == 435 and Rect1.x > 601 and Rect1.x < 849 \
                or Rect1.y == 235 and Rect1.x > 1 and Rect1.x < 249 \
                or Rect1.y == 185 and Rect1.x > 1201 and Rect1.x < 1449:
            Rect1.y -= 150
    if not Rect1.colliderect(Rect2) and not Rect1.colliderect(Rect3) and not Rect1.colliderect(
            Rect4) and not Rect1.colliderect(Rect5) and not Rect1.colliderect(Rect6):
        Rect1.y = Rect1.y + 5
    win.blit(nebo, [0, 0])
    win.blit(stena, Rect2)
    win.blit(povorot, Rect1)
    win.blit(stup, Rect3)
    win.blit(stup, Rect4)
    win.blit(stup, Rect5)
    win.blit(stup, Rect6)

    # ввод текста на экран
    font = pygame.font.Font(pygame.font.get_default_font(), 36)
    text_surface = font.render('Coordinates: {}, {}'.format(Rect1.x, Rect1.y), True, (255, 255, 0))
    win.blit(text_surface, dest=(475, 0))

    pygame.display.update()
    clock.tick(12)
pygame.quit()
