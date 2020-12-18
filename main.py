import pygame


a, b = 1600, 900
size = width, height = a, b
screen = pygame.display.set_mode(size)


class ACT1:
    if __name__ == '__main__':
        pygame.init()

        playerR = pygame.image.load('персонаж.png')
        playerL = pygame.image.load('персонаж2.png')
        background = pygame.image.load('fon3.png')
        background_x = 0
        player = playerR

        x = 50
        y = 50
        speed = 10

        pygame.display.flip()
        clock = pygame.time.Clock()
        running = True
        while running:
            screen.fill((0, 0, 0))
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            move = pygame.key.get_pressed()
            y = 0

            if move[pygame.K_LEFT] and x >= 1:
                x -= speed
                player = playerL
                if background_x != 0:
                    background_x += speed
            elif move[pygame.K_RIGHT] and x <= 1300:
                if x != 1599:
                    x += speed
                player = playerR
                if background_x <= 3200:
                    background_x -= speed
            screen.blit(background, (background_x, 0))
            screen.blit(player, (x, y))
            pygame.display.update()
        pygame.quit()