import pygame
import random
import math
from pygame import mixer

# Initialize pygame
pygame.init()

# Create screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Title and Icon
pygame.display.set_caption("Space Shooter")

# Player
player_img = pygame.Surface((64, 64), pygame.SRCALPHA)
pygame.draw.polygon(player_img, (0, 255, 0), [(32, 0), (0, 64), (64, 64)])
player_x = 370
player_y = 480
player_x_change = 0
player_speed = 5

# Enemy
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    # Create a red circular enemy
    temp_enemy_img = pygame.Surface((40, 40), pygame.SRCALPHA)
    pygame.draw.circle(temp_enemy_img, (255, 0, 0), (20, 20), 20)
    enemy_img.append(temp_enemy_img)
    enemy_x.append(random.randint(0, 736))
    enemy_y.append(random.randint(50, 150))
    enemy_x_change.append(3)
    enemy_y_change.append(40)

# Bullet
bullet_img = pygame.Surface((16, 16), pygame.SRCALPHA)
pygame.draw.circle(bullet_img, (255, 255, 0), (8, 8), 8)
bullet_x = 0
bullet_y = 480
bullet_x_change = 0
bullet_y_change = 10
bullet_state = "ready"  # Ready - can't see bullet, Fire - bullet is moving

# Score
score_value = 0
font = pygame.font.SysFont(None, 32)
text_x = 10
text_y = 10

# Game Over text
game_over_font = pygame.font.SysFont(None, 64)

# Sound
try:
    # Laser sound
    bullet_sound = mixer.Sound('laser.wav')
    # Explosion sound
    explosion_sound = mixer.Sound('explosion.wav')
    # Background music
    mixer.music.load('background.wav')
    mixer.music.play(-1)
    sound_available = True
except:
    sound_available = False

# Stars background
stars = []
for i in range(100):
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    radius = random.randint(1, 2)
    stars.append([x, y, radius])

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(player_img, (x, y))

def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 24, y + 10))

def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt((enemy_x - bullet_x) ** 2 + (enemy_y - bullet_y) ** 2)
    if distance < 27:  # 20 (enemy radius) + 8 (bullet radius) - 1
        return True
    return False

# Game Loop
running = True
game_over = False

while running:
    # RGB background
    screen.fill((0, 0, 0))
    
    # Draw stars
    for star in stars:
        pygame.draw.circle(screen, (255, 255, 255), (star[0], star[1]), star[2])
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        # Keystroke check
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -player_speed
            if event.key == pygame.K_RIGHT:
                player_x_change = player_speed
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                if sound_available:
                    bullet_sound.play()
                bullet_x = player_x
                fire_bullet(bullet_x, bullet_y)
            if event.key == pygame.K_r and game_over:
                # Reset game
                game_over = False
                score_value = 0
                player_x = 370
                for i in range(num_of_enemies):
                    enemy_x[i] = random.randint(0, 736)
                    enemy_y[i] = random.randint(50, 150)
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0
                
    # Player movement
    player_x += player_x_change
    
    # Boundary check for player
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:  # 800 - 64 (player width)
        player_x = 736
        
    # Enemy movement
    if not game_over:
        for i in range(num_of_enemies):
            # Game Over
            if enemy_y[i] > 440:
                for j in range(num_of_enemies):
                    enemy_y[j] = 2000  # Move enemies off screen
                game_over_text()
                game_over = True
                break
                
            enemy_x[i] += enemy_x_change[i]
            
            # Boundary check for enemy
            if enemy_x[i] <= 0:
                enemy_x_change[i] = 3
                enemy_y[i] += enemy_y_change[i]
            elif enemy_x[i] >= 760:  # 800 - 40 (enemy width)
                enemy_x_change[i] = -3
                enemy_y[i] += enemy_y_change[i]
                
            # Collision
            collision = is_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
            if collision and bullet_state == "fire":
                if sound_available:
                    explosion_sound.play()
                bullet_y = 480
                bullet_state = "ready"
                score_value += 1
                enemy_x[i] = random.randint(0, 736)
                enemy_y[i] = random.randint(50, 150)
                
            # Draw enemy
            enemy(enemy_x[i], enemy_y[i], i)
    
    # Bullet movement
    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = "ready"
        
    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change
        
    # Show info text
    if game_over:
        restart_text = font.render("Press R to restart", True, (255, 255, 255))
        screen.blit(restart_text, (320, 320))
        
    # Draw player
    player(player_x, player_y)
    
    # Show score
    show_score(text_x, text_y)
    
    # Update display
    pygame.display.update()

# Quit pygame
pygame.quit()
