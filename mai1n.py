import pygame
import sys
import os
from pygame.locals import *

import PREVIEW


class Person:
    def __init__(self, x, minX, maxX, speed, playerR, playerL, img_names2, img_names3):
        self.x = x
        self.minX = minX
        self.maxX = maxX
        self.speed = speed
        self.rotation = False  # False - right; True - left
        
        self.rightMoveSprites = list()
        self.currentRightSprite = 0
        self.leftMoveSprites = list()
        self.currentLeftSprite = 0
        
        self.defaultRSprite = pygame.image.load(playerR).convert_alpha()
        self.defaultLSprite = pygame.image.load(playerL).convert_alpha()
        
        self.PlayerSprite = self.defaultRSprite
        
        for img2 in img_names2:
            self.rightMoveSprites.append(pygame.image.load(img2).convert_alpha())
        for img3 in img_names3:
            self.leftMoveSprites.append(pygame.image.load(img3).convert_alpha())
            
    def stepRight(self):
        self.rotation = False
        self.x = min(self.x + self.speed, self.maxX)
        self.PlayerSprite = self.rightMoveSprites[self.currentRightSprite]
        self.currentRightSprite = (self.currentRightSprite + 1) % len(self.rightMoveSprites)
        self.currentLeftSprite = 0
        
    def stepLeft(self):
        self.rotation = True
        self.x = max(self.x - self.speed, self.minX)
        self.PlayerSprite = self.leftMoveSprites[self.currentLeftSprite]
        self.currentLeftSprite = (self.currentLeftSprite + 1) % len(self.leftMoveSprites)
        self.currentRightSprite = 0
        
    def setDefaultSprite(self):
        if self.rotation:
            self.PlayerSprite = self.defaultLSprite
        else:
            self.PlayerSprite = self.defaultRSprite
    
    def getPlayerSprite(self):
        return self.PlayerSprite
    
    def getX(self):
        return self.x
    
    def isPlayMusic(self):
        return ((self.currentRightSprite == 1 or self.currentRightSprite == 6) or (self.currentLeftSprite == 1 or self.currentLeftSprite == 6)) and \
               (self.PlayerSprite != self.defaultRSprite and self.PlayerSprite != self.defaultLSprite)


def ACT1_REFORGE():
    pygame.mixer.music.load('Звуки и музыка\дождь.mp3')
    s = pygame.mixer.Sound('Звуки и музыка\шаг.ogg')
    s.set_volume(0.1)
    pressspace = pygame.image.load('Спрайты\Элементы интерфейса\НАЖМИТЕ ПРОБЕЛ.png').convert_alpha()
    background = pygame.image.load('фон3.png').convert_alpha()
    key = pygame.transform.smoothscale(pygame.image.load('Ключ.png').convert_alpha(), (50, 50))
    img_names = ('0.png', '1.png', '2.png',
                 '3.png', '4.png', '5.png', '6.png', '7.png')
    
    if __name__ == '__main__':
        screen = pygame.display.set_mode(size)
        pygame.display.flip()
        pygame.mouse.set_visible(False)
        background_x = 0

        keyx = 600
        keyshow = False

        inventarkey = False

        textstart = True
        
        speed = 20
        c = 0

        mainPerson = Person(20, #начальная координата x
                            20, #минимальное значение x
                            1250, #максимальное значение x
                            speed, #скорость изменения x
                            'Спрайты\Персонаж\персонаж.png', #путь к изображению стоящего персонажа вмторящего в правую сторону
                            'Спрайты\Персонаж\персонаж2.png', #путь к изображению стоящего персонажа вмторящего в левую сторону
                            ('Спрайты\Персонаж\\right\пр1.png', 'Спрайты\Персонаж\\right\пр2.png', 'Спрайты\Персонаж\\right\пр3.png', 'Спрайты\Персонаж\\right\пр4.png',
                             'Спрайты\Персонаж\\right\пр5.png', 'Спрайты\Персонаж\\right\пр6.png', 'Спрайты\Персонаж\\right\пр7.png', 'Спрайты\Персонаж\\right\пр8.png', 
                             'Спрайты\Персонаж\\right\пр9.png', 'Спрайты\Персонаж\\right\пр10.png', 'Спрайты\Персонаж\\right\пр11.png', 'Спрайты\Персонаж\\right\пр12.png'), #изображения для анимации ходьбы в правую сторону
                            ("Спрайты\Персонаж\\left\ле1.png", "Спрайты\Персонаж\\left\ле2.png", "Спрайты\Персонаж\\left\ле3.png", "Спрайты\Персонаж\\left\ле4.png",
                             "Спрайты\Персонаж\\left\ле5.png", "Спрайты\Персонаж\\left\ле6.png", "Спрайты\Персонаж\\left\ле7.png", "Спрайты\Персонаж\\left\ле8.png",
                             "Спрайты\Персонаж\\left\ле9.png", "Спрайты\Персонаж\\left\ле10.png", "Спрайты\Персонаж\\left\ле11.png", "Спрайты\Персонаж\\left\ле12.png") #изображения для анимации ходьбы в левую сторону              
        ) # главный герой
        
        dedPerson = Person(2000, #начальная координата x
                            -10000, #минимальное значение x
                            10000, #максимальное значение x
                            speed, #скорость изменения x
                            'Спрайты\Гробовщик\Гробовщик.png', #путь к изображению стоящего персонажа вмторящего в правую сторону
                            'Спрайты\Гробовщик\ГробовщикЛ.png', #путь к изображению стоящего персонажа вмторящего в левую сторону
                            ('Спрайты\Гробовщик\Гробовщик.png', ), #изображения для анимации ходьбы в правую сторону
                            ("Спрайты\гробовщик\гр1.png", "Спрайты\гробовщик\гр2.png", "Спрайты\гробовщик\гр3.png", "Спрайты\гробовщик\гр4.png", 
                             "Спрайты\гробовщик\гр5.png", "Спрайты\гробовщик\гр6.png", "Спрайты\гробовщик\гр7.png", "Спрайты\гробовщик\гр8.png", 
                             "Спрайты\гробовщик\гр9.png", "Спрайты\гробовщик\гр10.png", "Спрайты\гробовщик\гр11.png", "Спрайты\гробовщик\гр12.png") #изображения для анимации ходьбы в левую сторону              
        ) # дед

        all_imgs = list()
        all_imgsGr = list()

        for img in img_names:
            fullname = os.path.join('Спрайты\Дождь', img)
            all_imgs.append(pygame.image.load(fullname).convert_alpha())
        clock = pygame.time.Clock()
        running = True
        grDead = False
        H = 0
        schetpi = 0
        pygame.mixer.music.play(-1)
        g = True
        image = pygame.image.load('черрный фон.jpg')
        x1 = 0
        x2 = 0
        while running:
            mainPerson.setDefaultSprite()
            clock.tick(12)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    main_menu()
                else:
                    pygame.display.flip()
            move = pygame.key.get_pressed()
            y = 0
            x = mainPerson.getX()
            if x != 640 or H == 1:
                if move[pygame.K_LEFT] and x > 20:
                    mainPerson.stepLeft()
                elif move[pygame.K_RIGHT] and x < 1250:
                    mainPerson.stepRight()
                elif move[pygame.K_RIGHT] and x >= 1250 and background_x != -1300:
                    background_x -= speed
                    keyx -= speed
                    mainPerson.stepRight()
                elif move[pygame.K_LEFT] and x <= 20 and background_x < 0:
                    background_x += speed
                    keyx += speed
                    mainPerson.stepLeft()
            elif schetpi > 0:
                grDead = True
                keyshow = True

            dedx = dedPerson.getX()

            if grDead:
                dedPerson.stepLeft()
                if dedx < -1000:
                    H = 1
                    grDead = False

            if move[pygame.K_SPACE] and x - background_x > 2150 and inventarkey:
                ACT1_5()
                pygame.quit()

            elif x == 640 and H != 1 and schetpi == 0:
                if dedx != 700:
                    dedPerson.stepLeft()
                else:
                    dedPerson.setDefaultSprite()
                    screen.fill((0, 0, 0))
                    pygame.display.update()
                    schetpi += 1
                    BATTLE_DED()

            c += 1
            if c == 8:
                c = 0
            if mainPerson.isPlayMusic():
                s.play()

            player = mainPerson.getPlayerSprite()
            playerDED = dedPerson.getPlayerSprite()

            screen.blit(background, (background_x, y))
            if keyshow:
                screen.blit(key, (keyx, 800))
            screen.blit(player, (x, 300))

            screen.blit(playerDED, (dedx, y))
            
            mouse_pos = pygame.mouse.get_pos()
            screen.blit(IMAGE, mouse_pos)
            screen.blit(all_imgs[c], (background_x, y))

            #маски
            mask = player.get_rect()
            mask.x = x
            mask.y = 300

            maskkey = key.get_rect()
            maskkey.x = keyx
            maskkey.y = 800

            if move[pygame.K_SPACE] and keyshow and mask.colliderect(maskkey):
                inventarkey = True
                keyshow = False

            if textstart:
                draw_text('попадите в дом', pygame.font.Font('20031 (1).otf', 20), (255, 255, 255), screen, 20, 20)
            if mask.colliderect(maskkey) and H == 1 and keyshow:
                screen.blit(pressspace, (0, 0))
            if x - background_x > 2150 and inventarkey:
                screen.blit(pressspace, (0, 0))

            if x1 != 920:
                x1 += 30
                x2 -= 30
                screen.blit(image, (x1, 0))
                screen.blit(image, (x2, 0))

            pygame.display.update()
        pygame.quit()

def ACT1_5():
    if __name__ == '__main__':
        screen = pygame.display.set_mode(size)
        pygame.display.flip()
        pygame.mouse.set_visible(False)
        playerR = pygame.image.load('Спрайты\Персонаж\персонаж.png').convert_alpha()
        playerL = pygame.image.load('Спрайты\Персонаж\персонаж2.png').convert_alpha()
        background = pygame.image.load('фон2.png').convert_alpha()
        background_x = 0
        x = 20
        speed = 20
        c = 0
        c1 = 0
        z1 = 0
        all_imgs2 = list()
        all_imgs3 = list()

        img_names2 = (
            'пр1.png', 'пр2.png', 'пр3.png', 'пр4.png', 'пр5.png', 'пр6.png', 'пр7.png',
            'пр8.png', 'пр9.png', 'пр10.png', 'пр11.png', 'пр12.png')
        img_names3 = ("ле1.png", "ле2.png", "ле3.png", "ле4.png", "ле5.png", "ле6.png", "ле7.png", "ле8.png", "ле9.png",
                      "ле10.png", "ле11.png", "ле12.png")
        for img2 in img_names2:
            fullname1 = os.path.join('Спрайты\Персонаж', 'right', img2)
            all_imgs2.append(pygame.image.load(fullname1))
        for img3 in img_names3:
            fullname2 = os.path.join('Спрайты\Персонаж', 'left', img3)
            all_imgs3.append(pygame.image.load(fullname2).convert_alpha())
        clock = pygame.time.Clock()
        running = True
        while running:
            player = playerR
            clock.tick(12)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    #main_menu()
                else:
                    pygame.display.flip()
            move = pygame.key.get_pressed()
            y = 0
            if move[pygame.K_LEFT] and x > 20:
                x -= speed
                player = all_imgs3[z1]
                z1 += 1
            elif move[pygame.K_RIGHT] and x <= 1250:
                x += speed
                player = all_imgs2[c1]
                c1 += 1
            elif move[pygame.K_RIGHT] and x >= 1250:
                player = all_imgs2[c1]

            if move[pygame.K_SPACE] and x < 100:
                ACT1_5_2()

            c += 1
            if c == 8:
                c = 0
            if c1 == 12:
                c1 = 0
            if z1 == 12:
                z1 = 0

            mouse_pos = pygame.mouse.get_pos()
            screen.blit(background, (background_x, y))
            screen.blit(player, (x, y))
            screen.blit(IMAGE, mouse_pos)
            pygame.display.update()
        pygame.quit()

def ACT1_5_2():
    if __name__ == '__main__':
        screen = pygame.display.set_mode(size)
        pygame.display.flip()
        pygame.mouse.set_visible(False)
        playerR = pygame.image.load('персонаж.png').convert_alpha()
        playerL = pygame.image.load('персонаж2.png').convert_alpha()
        background = pygame.image.load('фон3.png').convert_alpha()
        background_x = 0
        x = 20
        speed = 20
        c = 0
        c1 = 0
        z1 = 0
        all_imgs2 = list()
        all_imgs3 = list()
        img_names2 = (
            'пр1.png', 'пр2.png', 'пр3.png', 'пр4.png', 'пр5.png', 'пр6.png', 'пр7.png',
            'пр8.png', 'пр9.png', 'пр10.png', 'пр11.png', 'пр12.png', 'пр13.png', 'пр14.png', 'пр15.png', 'пр16.png',
            'пр17.png', 'пр18.png', 'пр19.png', 'пр20.png', 'пр21.png', 'пр22.png', 'пр23.png', 'пр24.png')
        img_names3 = ("ле1.png", "ле2.png", "ле3.png", "ле4.png", "ле5.png", "ле6.png", "ле7.png", "ле8.png", "ле9.png",
                      "ле10.png", "ле11.png", "ле12.png")
        for img2 in img_names2:
            all_imgs2.append(pygame.image.load(img2))
        for img3 in img_names3:
            all_imgs3.append(pygame.image.load(img3).convert_alpha())
        clock = pygame.time.Clock()
        running = True
        player = playerR
        while running:
            player = playerR
            screen.fill((0, 0, 0))
            clock.tick(12)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            move = pygame.key.get_pressed()
            y = 0
            if move[pygame.K_LEFT] and x > 20:
                x -= speed
                player = all_imgs3[z1]
                z1 += 1
            elif move[pygame.K_RIGHT] and x <= 1250:
                x += speed
                player = all_imgs2[c1]
                c1 += 1
            elif move[pygame.K_RIGHT] and x >= 1250 and background_x != -1300:
                background_x -= speed
                player = all_imgs2[c1]
                c1 += 1
            elif move[pygame.K_LEFT] and x <= 20 and background_x < 0:
                background_x += speed
                player = all_imgs3[z1]
                z1 += 1
            c += 1
            if c == 8:
                c = 0
            if c1 == 13:
                c1 = 0
            if z1 == 12:
                z1 = 0

            screen.blit(background, (background_x, y))
            screen.blit(player, (x, y))
            pygame.display.update()
        pygame.quit()
        pygame.quit()


IMAGE = pygame.image.load('курсор2.png')


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def main_menu():
    pygame.mixer.music.load('МЕЛОДИЯ.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.05)
    s = pygame.mixer.Sound('звук щелчка.ogg')

    m = 0
    ty = pygame.image.load('1туман.png').convert_alpha()
    tyx = -300
    menusp = (
        'меню.png', 'меню2.png', 'меню4.png', 'меню5.png', 'меню6.png', 'меню7.png', 'меню8.png')
    menu = list()
    for i in menusp:
        menu.append(pygame.image.load(i).convert_alpha())

    while True:
        if tyx == -4800:
            tyx = -300
        screen.fill((pygame.Color('Black')))
        screen.blit(background, (0, 0))
        draw_text('главное меню', pygame.font.Font('20031 (1).otf', 50), (255, 255, 255), screen, 20, 20)
        button_1 = pygame.Rect(94, 200, 395, 90)
        button_2 = pygame.Rect(94, 350, 395, 90)
        button_3 = pygame.Rect(94, 500, 395, 90)

        mx, my = pygame.mouse.get_pos()
        screen.blit(menu[m], (0, 0))
        screen.blit(ty, (tyx, 0))

        tyx -= 10

        screen.blit(but, (90, 195))
        screen.blit(but, (90, 345))
        screen.blit(but, (90, 495))

        draw_text('начать игру', pygame.font.Font('20031 (1).otf', 50), (255, 255, 255), screen, 120, 224)
        draw_text('продолжить игру', pygame.font.Font('20031 (1).otf', 38), (255, 255, 255), screen, 105, 376)
        draw_text('настройки', pygame.font.Font('20031 (1).otf', 50), (255, 255, 255), screen, 130, 520)

        x = -1600
        x1 = 1600
        if button_1.collidepoint((mx, my)):
            screen.blit(but1, (90, 195))
            draw_text('начать игру', pygame.font.Font('20031 (1).otf', 50), (255, 255, 255), screen, 120, 224)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    s.play()
                    g = True
                    image = pygame.image.load('черрный фон.jpg')
                    image2 = image
                    while g:
                        if x != 920:
                            x += 30
                            x1 -= 30
                            screen.blit(image, (x, 0))
                            screen.blit(image, (x1, 0))
                            pygame.display.flip()
                            pygame.display.update()
                            mainClock.tick(12)
                        else:
                            g = False
                    pygame.mixer.music.stop()
                    ACT1_REFORGE()
                    pygame.quit()
        if button_2.collidepoint((mx, my)):
            screen.blit(but1, (90, 345))
            draw_text('продолжить игру', pygame.font.Font('20031 (1).otf', 38), (255, 255, 255), screen, 105, 376)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        m += 1
        if m == 7:
            m = 0
        mouse_pos = pygame.mouse.get_pos()
        screen.blit(IMAGE, mouse_pos)
        pygame.display.flip()
        pygame.display.update()
        mainClock.tick(12)

def BATTLE_DED():
    global chis
    back = pygame.image.load('фонбитва.png').convert_alpha()
    ded1 = pygame.transform.smoothscale(pygame.image.load('битваГ1.png').convert_alpha(), (600, 600))
    ded2 = pygame.transform.smoothscale(pygame.image.load('битваГ2.png').convert_alpha(), (600, 600))
    ded3 = pygame.transform.smoothscale(pygame.image.load('битваГ3.png').convert_alpha(), (600, 600))
    deda = pygame.transform.smoothscale(pygame.image.load('битваГ4.png').convert_alpha(), (600, 600))
    deda2 = pygame.transform.smoothscale(pygame.image.load('битваГ5.png').convert_alpha(), (600, 600))
    dedl = pygame.transform.smoothscale(pygame.image.load('битваГ6.png').convert_alpha(), (600, 600))
    dedl2 = pygame.transform.smoothscale(pygame.image.load('битваГ7.png').convert_alpha(), (600, 600))
    dedl3 = pygame.transform.smoothscale(pygame.image.load('битваГ8.png').convert_alpha(), (600, 600))
    dedl4 = pygame.transform.smoothscale(pygame.image.load('битваГ9.png').convert_alpha(), (600, 600))
    dedl5 = pygame.transform.smoothscale(pygame.image.load('битваГ10.png').convert_alpha(), (600, 600))
    p1 = pygame.transform.smoothscale(pygame.image.load('БитваП1.png').convert_alpha(), (600, 600))
    p2 = pygame.transform.smoothscale(pygame.image.load('БитваП2.png').convert_alpha(), (600, 600))
    p3 = pygame.transform.smoothscale(pygame.image.load('БитваП3.png').convert_alpha(), (600, 600))

    battle = list()
    battle.append(p1)
    battle.append(p2)
    battle.append(p3)

    battle1 = list()
    battle1.append(ded1)
    battle1.append(ded2)
    battle1.append(ded3)

    anim = list()
    anim.append(deda)
    anim.append(deda2)
    anim.append(dedl)

    battlelopata = list()
    battlelopata.append(dedl)
    battlelopata.append(dedl2)
    battlelopata.append(dedl3)
    battlelopata.append(dedl4)
    battlelopata.append(dedl5)

    grob = (
        'Полоска здоровья.png', 'Полоска здоровья1.png', 'Полоска здоровья2.png', 'Полоска здоровья3.png',
        'Полоска здоровья4.png', 'Полоска здоровья5.png', 'Полоска здоровья6.png', 'Полоска здоровья7.png',
        'Полоска здоровья8.png')
    playerFight = list()
    for img in grob:
        playerFight.append(pygame.image.load(img).convert_alpha())

    grobovshik = list()
    grob3 = (
        'Полоска здоровья.png', 'Полоска здоровья11.png', 'Полоска здоровья22.png',
        'Полоска здоровья33.png',
        'Полоска здоровья44.png')

    for mgi in grob3:
        grobovshik.append(pygame.image.load(mgi).convert_alpha())
    j = 0
    g = 0
    kadrplayer = 0
    c = False
    c1 = False
    schetpi1 = 0
    schetpi = 0
    br = True
    anima = False
    dedSt1 = True
    dead = True
    screen.fill((0, 0, 0))
    pygame.display.update()
    while br:
        screen.fill((0, 0, 0))
        screen.blit(back, (0, 0))
        screen.blit(pygame.transform.scale(playerFight[g], (400, 50)), (300, 250))
        screen.blit(pygame.transform.scale(grobovshik[kadrplayer], (400, 50)), (840, 250))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE and c != True:
                    c = True
                    if kadrplayer == 4:
                        for i in range(1):
                            dedSt1 == False
                            dead == False
                            anima = True
                            br = False
                    else:
                        kadrplayer += 1
                if event.key == K_ESCAPE:
                    sys.exit()
        if anima:
            for i in range(2):
                screen.blit(anim[i], (450, 300))
                pygame.display.update()
        if c == True:
            screen.blit(battle[j], (450, 300))
            if j != 2:
                j += 1
            else:
                c = False
                screen.blit(battle[j], (450, 300))
                j = 0

        else:
            screen.blit(battle[0], (450, 300))

        if schetpi % 10 == 0:
            c1 = True
            if g == 8:
                PREVIEW.death()
                break
            else:
                g += 1

        if c1 == True and anima == False:
            screen.blit(battle1[schetpi1], (450, 300))
            if schetpi1 != 2 and anima == False:
                schetpi1 += 1
            else:
                c1 = False
                screen.blit(battle1[schetpi1], (450, 300))
                schetpi1 = 0
        else:
            screen.blit(battle1[0], (450, 300))
        pygame.display.update()
        mainClock.tick(10)
        schetpi += 1
    chis = 1

pygame.mixer.init()
pygame.mouse.set_visible(False)
a, b = 1600, 900
size = width, height = a, b
screen = pygame.display.set_mode(size)
mainClock = pygame.time.Clock()

font = pygame.font.SysFont(None, 20)

click = False
background = pygame.image.load('фон3.png')

but = pygame.transform.scale(pygame.image.load('кнопка.png').convert_alpha(), (400, 100))
but1 = pygame.transform.scale(pygame.image.load('кнопка1.png').convert_alpha(), (400, 100))
#PREVIEW.p()
main_menu()
