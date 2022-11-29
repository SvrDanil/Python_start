import pygame
import sys

def winner_check(mas,sign):
    zeroes = 0
    for row in mas :
        zeroes += row.count(0)
        if row.count(sign) == 3 :
            return sign
    for col in range (3):
        if mas[0][col] == sign and mas[1][col] == sign and mas [2][col] == sign:
            return sign
    if mas[0][0] == sign and mas[1][1] == sign and mas [2][2] == sign:
        return sign
    if mas[0][2] == sign and mas[1][1] == sign and mas [2][0] == sign:
        return sign
    if zeroes == 0:
        return 'None'
    return False
pygame.init()
size_block = 200
margin = 15
width  = size_block*3 + margin *4 
heigth = width + 20
size_window = (width,heigth)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption("Крестики - Нолики ")
black = (0 , 0 , 0)
red = (255 , 0 , 0)
green = (0 , 255 , 0)
blue = (0 , 0 , 255)
white = (255 , 255 , 255)
mas = [[0]* 3 for i in range (3)]
query = 0

turn_font = pygame.font.SysFont('comicsansms',14)

turn_x = turn_font.render("X turn",1,white)
turn_o = turn_font.render("O turn",1,white)
screen.blit(turn_x, [screen.get_width() / 2,screen.get_height()-25])

game_over = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (size_block + margin)
            row = y_mouse // (size_block + margin)
            if mas[row][col] == 0: 
                if query % 2 == 0:
                    mas[row][col] = 'X'
                    screen.fill(black)
                    screen.blit(turn_o, [screen.get_width() / 2,screen.get_height()-25])
                else:
                    mas[row][col] = 'O'
                    screen.fill(black)
                    screen.blit(turn_x, [screen.get_width() / 2,screen.get_height()-25])
                query +=1    
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            mas =[[0] *3 for i in range(3)]
            query = 0
            screen.fill(black)
    if not game_over:
        for row in range(3):
            for col in range(3):
                if mas [row][col] == 'X':
                    color = blue
                elif mas [row][col] == 'O':
                    color = green
                else :
                    color = white
                x = col * size_block + (col + 1) * margin
                y = row * size_block + (row+ 1) * margin
                pygame.draw.rect(screen, color, (x,y,size_block,size_block))
                if color == blue:
                    pygame.draw.line (screen, white, (x,y), (x + size_block, y + size_block), 3)
                    pygame.draw.line (screen, white, (x + size_block,y), (x, y + size_block), 3)
                elif color == green :
                    pygame.draw.circle (screen,white,(x + size_block//2, y + size_block//2), size_block//2-3,3)
    if (query - 1) % 2 == 0:
        game_over = winner_check(mas, 'X')
    else:
        game_over = winner_check(mas, 'O')
    
    if game_over:
        screen.fill(black)
        font = pygame.font.SysFont('comicsansms',80)
        font_continue = pygame.font.SysFont('comicsansms',30)
        text_winner = font.render(f'Winner :{game_over}',True,white)
        text_repeat = font_continue.render("Press SPACE to continue",1,white)
        text_rect = text_winner.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text_winner, [text_x,text_y])
        screen.blit(text_repeat,[text_x+20,text_y+100])


    pygame.display.update()