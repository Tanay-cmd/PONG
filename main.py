import pygame
import sys

#Game Inititalize
pygame.init()
clock = pygame.time.Clock()

# Game Setup
screen_width = 750
screen_height = 450
screen = pygame.display.set_mode((screen_width, screen_height))

player = pygame.Rect(0, screen_height/2, 10, 80)
opponent = pygame.Rect(screen_width - 10 ,screen_height/2, 10, 80)
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 10, 10)

player_speed = 10
opponent_speed = 10
ball_speed_x = 7
ball_speed_y = 7

player_score = 0
opponent_score = 0
def movements():
    global ball_speed_x, ball_speed_y

    ball.x += ball_speed_x
    ball.y += ball_speed_y                         
    if ball.midbottom[1] >= screen_height or ball.midbottom[1] <= 0:
        ball_speed_y *= -1
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1
   
def rival_movements():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        player.y -= player_speed
    elif keys[pygame.K_s]:
        player.y += player_speed

    # Constraints
    if player.y < 0:
        player.y = 0
    elif player.y > screen_height - player.height:
        player.y = screen_height - player.height
def player_movements():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        opponent.y -= opponent_speed
    elif keys[pygame.K_DOWN]:
        opponent.y += opponent_speed

    # Constraints
    if opponent.y < 0:
        opponent.y = 0
    elif opponent.y > screen_height - opponent.height:
        opponent.y = screen_height - opponent.height

score_font = pygame.font.Font(None, 32)

def score_system():
    global player_score, opponent_score
    if ball.x <= 0: 
        player_score += 1
        ball.x = screen_width/2 - 15
        ball.y = screen_height/2 - 15
    elif ball.x >= screen_width :
        opponent_score += 1
        ball.x = screen_width/2 - 15
        ball.y = screen_height/2 - 15

    player_score_text = score_font.render(f"{player_score}", False, (200,200,200))
    opponent_score_text = score_font.render(f"{opponent_score}", False, (200,200,200))
    screen.blit(player_score_text,(screen_width/4, 20))
    screen.blit(opponent_score_text,(3*screen_width/4 - 20, 20))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    
    movements()
    player_movements()
    rival_movements()
    
    screen.fill('grey12')
    pygame.draw.rect(screen, "white", player)
    pygame.draw.rect(screen, "white", opponent)
    pygame.draw.ellipse(screen, "white", ball)                     
    pygame.draw.aaline(screen, "white", (screen_width/2 ,0), (screen_width/2 ,screen_height))
    score_system()
    pygame.display.update()
    clock.tick(60)