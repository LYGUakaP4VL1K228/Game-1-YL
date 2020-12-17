import pygame



if __name__ == '__main__':
    pygame.init()
    a, b = 1600, 900
    size = width, height = a, b
    screen = pygame.display.set_mode(size)

    playerR = pygame.image.load('персонаж.png')
    playerL = pygame.image.load('персонаж2.png')
    bg = pygame.image.load('фон1.png')
    player = playerR

    x = 50
    y = 50
    speed = 10

    pygame.display.flip()
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()

        y = 0
        if keys[pygame.K_LEFT]:
            x -= speed
            player = playerL
        elif keys[pygame.K_RIGHT]:
            x += speed
            player = playerR
        screen.blit(bg, (0, 0))

        screen.blit(player, (x, y))
        pygame.display.update()
    pygame.quit()