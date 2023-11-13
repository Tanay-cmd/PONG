import pygame
import sys

#Game Inititalize
pygame.init()
clock = pygame.time.Clock()

# Game Setup
screen_width = 750
screen_height = 450
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('PONG')

class Game:
    
    def __init__(self):
        self.player = pygame.Rect(0, screen_height/2, 10, 80)
        self.opponent = pygame.Rect(screen_width - 10 ,screen_height/2, 10, 80)
        self.ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 10, 10)

        self.player_speed = 10
        self.opponent_speed = 10
        self.ball_speed_x = 7
        self.ball_speed_y = 7

        self.player_score = 0
        self.opponent_score = 0

    def movements(self):
        

        self.ball.x += self.ball_speed_x
        self.ball.y += self.ball_speed_y                         
        if self.ball.midbottom[1] >= screen_height or self.ball.midbottom[1] <= 0:
            self.ball_speed_y *= -1
        if self.ball.colliderect(self.player) or self.ball.colliderect(self.opponent):
            self.ball_speed_x *= -1
    
    def rival_movements(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.player.y -= self.player_speed
        elif keys[pygame.K_s]:
            self.player.y += self.player_speed

        # Constraints
        if self.player.y < 0:
            self.player.y = 0
        elif self.player.y > screen_height - self.player.height:
            self.player.y = screen_height - self.player.height
    def player_movements(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.opponent.y -= self.opponent_speed
        elif keys[pygame.K_DOWN]:
            self.opponent.y += self.opponent_speed

        # Constraints
        if self.opponent.y < 0:
            self.opponent.y = 0
        elif self.opponent.y > screen_height - self.opponent.height:
            self.opponent.y = screen_height - self.opponent.height

    

    def score_system(self):
        score_font = pygame.font.Font(None, 32)
        self.player_score, self.opponent_score
        if self.ball.x <= 0: 
            self.player_score += 1
            self.ball.x = screen_width/2 - 15
            self.ball.y = screen_height/2 - 15
        elif self.ball.x >= screen_width :
            self.opponent_score += 1
            self.ball.x = screen_width/2 - 15
            self.ball.y = screen_height/2 - 15

        self.player_score_text = score_font.render(f"{self.player_score}", False, (200,200,200))
        self.opponent_score_text = score_font.render(f"{self.opponent_score}", False, (200,200,200))
        screen.blit(self.player_score_text,(screen_width/4, 20))
        screen.blit(self.opponent_score_text,(3*screen_width/4 - 20, 20))
    
    def update(self):
    
        self.movements()
        self.rival_movements()
        self.player_movements()
        screen.fill('grey12')
        pygame.draw.rect(screen, "white", self.player)
        pygame.draw.rect(screen, "white", self.opponent)
        pygame.draw.ellipse(screen, "white", self.ball)                     
        pygame.draw.aaline(screen, "white", (screen_width/2 ,0), (screen_width/2 ,screen_height))
        self.score_system()       
        

game = Game()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    game.update()

    
    

    pygame.display.update()
    clock.tick(60)
