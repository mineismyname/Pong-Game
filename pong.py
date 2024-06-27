import os
import pygame
import random
from pygame.locals import *
pygame.init()
pygame.mixer.init()
pygame.mixer.get_num_channels()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
## Load the sound as WAV (convert MP3 to WAV if necessary)
collide = pygame.mixer.Sound('./sounds/collide.mp3')  # Use a valid path
collide2 = pygame.mixer.Sound('./sounds/collide2.mp3')  # Use a valid path
collide3 = pygame.mixer.Sound('./sounds/collide3.mp3')  # Use a valid path
slowdown = pygame.mixer.Sound('./sounds/slowdown.mp3')  # Use a valid path
music = pygame.mixer.Sound('./sounds/music.mp3') # Use a valid path
exciting_music = pygame.mixer.Sound('./sounds/exciting music.mp3') # Use a valid path
silence = pygame.mixer.Sound('./sounds/silence.wav') # Use a valid path
deathfight = pygame.mixer.Sound('./sounds/deathfight.mp3') # Use a valid path
reverse = pygame.mixer.Sound ('./sounds/reverse.mp3') #Use a valid path
boost = pygame.mixer.Sound ('./sounds/boost.mp3') #Use a valid path
winscore = 25

collide_channel = pygame.mixer.Channel(0)
collide2_channel = pygame.mixer.Channel(1)
collide3_channel = pygame.mixer.Channel(2)
slowdown_channel = pygame.mixer.Channel(3)
music_channel = pygame.mixer.Channel(4)
silence_channel = pygame.mixer.Channel(5)
exciting_music_channel = pygame.mixer.Channel(6)
deathfight_channel = pygame.mixer.Channel(7)
reverse_channel = pygame.mixer.Channel(5)
music_channel.play(music, loops=-1)
exciting_music_channel.play(exciting_music, loops=-1)
deathfight_channel.play(deathfight, loops=-1)
music_channel.set_volume(0.3)
exciting_music_channel.set_volume(0.0)
deathfight_channel.set_volume(0.0)
boost_channel = pygame.mixer.Channel(5)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
max_ball_speed = 10
max_paddle_speed = 7
controls = 1
player1shield = "off"
player2shield = "off"
p1_shield_used = "no"
p2_shield_used = "no"
waitimer = 0
hi_frame_rate = 'off'
boosted = False
class Circle(pygame.sprite.Sprite):
    def __init__(self, color, radius, x, y, direction, speed=3):
        super(Circle, self).__init__()
        self.color = color
        self.radius = radius
        self.x = x
        self.y = y
        self.direction = direction
        self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
        self.speed = speed

    def update(self):
        if self.speed < max_ball_speed:
            self.speed += 0.004
        else:
            if not boosted:
                self.speed = max_ball_speed - 0.001
        self.rect.x += self.direction[0] * self.speed
        self.rect.y += self.direction[1] * self.speed

    def check_boundary_collision(self, height):
        if self.rect.top <= 0 or self.rect.bottom >= height:
            self.direction[1] = -self.direction[1]
            collide2_channel.play(collide2)
    def switch(self, height):
            self.direction[1] = -self.direction[1]
            reverse_channel.play(reverse)

    def check_paddle_collision(self, paddle):
        if self.rect.colliderect(paddle.rect):
            collide_channel.play(collide)
            self.direction[0] = -self.direction[0]
    def bounce_back(self):
        collide_channel.play(collide)
        self.direction[0] = -self.direction[0]
class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y, player, speed, score):
        super(Paddle, self).__init__()
        self.surf = pygame.Surface((width, height))
        self.surf.fill(color)
        self.rect = self.surf.get_rect(center=(x, y))
        self.player = player
        self.speed = speed
        self.score = score

    def update(self, keys, height):
        if self.speed < max_paddle_speed:
            self.speed += 0.002
        else:
            self.speed = max_paddle_speed -0.001
        if controls == 1:
            if self.player == 1:
                if keys[pygame.K_w] and self.rect.top > 0:
                    self.rect.y -= self.speed
                if keys[pygame.K_s] and self.rect.bottom < height:
                    self.rect.y += self.speed
            if self.player == 2:
                if keys[pygame.K_UP] and self.rect.top > 0:
                    self.rect.y -= self.speed
                if keys[pygame.K_DOWN] and self.rect.bottom < height:
                    self.rect.y += self.speed
        if controls == -1:
            if self.player == 1:
                if keys[pygame.K_w] and self.rect.bottom < height:
                    self.rect.y -= self.speed * controls
                if keys[pygame.K_s] and self.rect.top > 0:
                    self.rect.y += self.speed * controls
            if self.player == 2:
                if keys[pygame.K_UP] and self.rect.bottom < height:
                    self.rect.y -= self.speed * controls
                if keys[pygame.K_DOWN] and self.rect.top > 0:
                    self.rect.y += self.speed * controls
ball_direction = [random.choice([-1, 1]), random.choice([-1, 1])]
ball_position = [HEIGHT // 2, WIDTH // 2]
cooldown = 0
ball1 = Circle(WHITE, 25, WIDTH // 2, HEIGHT // 2, ball_direction, 3)
cooldown_active = False
player1 = Paddle(RED, 20, 100, 50, HEIGHT // 2, 1, 2, 0)
player2 = Paddle(YELLOW, 20, 100, WIDTH - 50, HEIGHT // 2, 2, 2, 0)
def slow_down():
    slowdown_channel.play(slowdown)
    silence_channel.play(silence)
    global cooldown
    global cooldown_active
    if not cooldown_active:
        cooldown_active = True
        ball1.speed = 1
        if pygame.time.get_ticks() > cooldown:
            
            cooldown_active = False      
player1uses = 0
player2uses = 0
switchstatus = "Player one or two can make an action"
fontcolor = WHITE
game_on = True
winner = None
mostrecentpress = None
while game_on:
    keys = pygame.key.get_pressed()      
    if keys[pygame.K_d] or keys[pygame.K_LEFT]:
        if keys[pygame.K_d]:
                if mostrecentpress == "d":
                    timer = 1
                    nokeypressed = True
        if keys[pygame.K_LEFT]:
            if mostrecentpress == "left":
                timer = 1
                nokeypressed = True
        while timer < 1:
            if keys[pygame.K_d] or keys[pygame.K_LEFT]:
                if keys[pygame.K_d]:
                    mostrecentpress = "d"
                if keys[pygame.K_LEFT]:
                    mostrecentpress = "left"
                if keys[pygame.K_d]:
                    mostrecentpress = "d"
                    switchstatus = "It is player two's turn to act"
                    fontcolor = YELLOW
                if keys[pygame.K_LEFT]:
                    mostrecentpress = "left"   
                    switchstatus = "It is player one's turn to act" 
                    fontcolor = RED
                timer += 0.001
                nokeypressed = False
            else:
                nokeypressed = True
                timer = 1
            if timer >= 1 and nokeypressed == False:
                controls = random.choice([-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1])
                ball1.switch(HEIGHT)        
    else:
        timer = 0
        nokeypressed = True
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                game_on = False
        elif event.type == pygame.QUIT:
            game_on = False
    if keys[pygame.K_a] and cooldown_active == False and player1uses == 0:
        slow_down()
        player1uses += 1
    if keys[pygame.K_RIGHT] and cooldown_active == False and player2uses == 0:
        slow_down()
        player2uses += 1
    if keys[pygame.K_x]:
        pygame.quit()
    player1.update(keys, HEIGHT)
    player2.update(keys, HEIGHT)
    if player1.score >= 10 or player2.score >= 10 and player1.score < 24 and player2.score < 24:
        exciting_music_channel.set_volume(0.3)
        music_channel.set_volume(0.0)
        max_ball_speed = 13
        max_paddle_speed = 9
    if player1.score > 23 or player2.score > 23:
        exciting_music_channel.set_volume(0.0)
        deathfight_channel.set_volume(0.5)
        max_ball_speed = 16
        max_paddle_speed = 11
    ball1.update()
    ball1.check_boundary_collision(HEIGHT)
    ball1.check_paddle_collision(player1)
    ball1.check_paddle_collision(player2)
    # point scoring ----------------------------------------------------------------------------------------------------------------------------------------------------------



    if ball1.rect.left <= 0 or ball1.rect.right >= WIDTH:
        if ball1.rect.left <= 0:

            if player1shield == "on":
                ball1.bounce_back()
                ball1.rect.center = (30, ball1.rect.y + 16.5)
                player1shield  = "off"
            else:
                player2.score += 1
                player2.speed += 1
                collide3_channel.play(collide3)
                ball1.rect.center = (WIDTH // 2, HEIGHT // 2)
                ball1.direction = [random.choice([-1, 1]), random.choice([-1, 1])]
                boosted = False
                ball1.speed *= 0.4

            if player2.score == winscore:
                winner = "player 2"
                game_on = False
        else:
            if player2shield == "on":
                ball1.bounce_back()
                ball1.rect.center = (770, ball1.rect.y + 16.5)
                player2shield  = "off"
            else:
                player1.score += 1
                player1.speed += 1
                collide3_channel.play(collide3)
                ball1.rect.center = (WIDTH // 2, HEIGHT // 2)
                ball1.direction = [random.choice([-1, 1]), random.choice([-1, 1])]
                boosted = False
                ball1.speed *= 0.4

            if player1.score >= winscore:
                winner = "player 1"
                game_on = False




    if player1.score < 24 and player2.score < 24:
        screen.fill((0, 0, 0))
    else:
        screen.fill((59, 8, 8))
    pygame.draw.circle(screen, ball1.color, ball1.rect.center, ball1.radius)
    screen.blit(player1.surf, player1.rect)
    screen.blit(player2.surf, player2.rect)


    font = pygame.font.SysFont("Callibri", 32)
    switchfont = pygame.font.SysFont("Callibri", 25)
    score1 = font.render(str(player1.score), True, WHITE)
    score2 = font.render(str(player2.score), True, WHITE)
    switch = switchfont.render(str(switchstatus), True, fontcolor)
    text_width = switch.get_width()
    text_height = switch.get_height()
    x = WIDTH // 2 - text_width // 2
    y = 40
    screen.blit(score1, (200, 40))
    screen.blit(score2, (600, 40))
    screen.blit(switch, (x, y))
    pygame.display.flip()
    if hi_frame_rate == 'off':
        clock.tick(60)
    else:
        clock.tick(150)
    if keys[pygame.K_p]:
        hi_frame_rate = 'on'
    if keys[pygame.K_SPACE]:
        nokeypressed = False
        while timer < 1:
            if keys[pygame.K_SPACE]:
                timer += 0.00001
            else:
                nokeypressed = True
                timer = 1
        if timer >= 1 and nokeypressed == False:
            if player1.score != 24 and player2.score != 24:
                player1.score += 1
                player2.score += 1
    if keys[pygame.K_b]:
        nokeypressed = False
        while timer < 1:
            if keys[pygame.K_b]:
                timer += 0.00001
            else:
                nokeypressed = True
                timer = 1
        if timer >= 1 and nokeypressed == False:
            winscore = 9999999999999999999999999999999999999999
    if keys[pygame.K_PAGEDOWN] and p2_shield_used == "no":
        player2shield = "on"
        p2_shield_used = "yes"
    if keys[pygame.K_q] and p1_shield_used == "no":
        player1shield = "on"
        p1_shield_used = "yes"
    if keys[pygame.K_e]:
        if mostrecentpress != "d":
            ball1.speed += 3
            mostrecentpress = "d"
            switchstatus = "It is player two's turn to act"
            fontcolor = YELLOW
            boosted = True
            boost_channel.play(boost)
    if keys[pygame.K_PAGEUP]:
        if mostrecentpress != "left":
            ball1.speed += 3
            mostrecentpress = "left"
            switchstatus = "It is player one's turn to act"
            fontcolor = RED
            boosted = True
            boost_channel.play(boost)



if winner:
    screen.fill((0, 0, 0))
    winnertext = font.render(f'{winner} wins!', True, WHITE)
    screen.blit(winnertext, (WIDTH // 2 - winnertext.get_width() // 2, HEIGHT // 2 - winnertext.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(5000)

pygame.display.flip()
pygame.quit()