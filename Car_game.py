import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 600
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Car Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Car class
class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 100))  # Car size
        self.image.fill(GREEN)  # Car color
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height - 120)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += self.speed

# Obstacle class
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))  # Obstacle size
        self.image.fill(RED)  # Obstacle color
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - 50)
        self.rect.y = -50
        self.speed = random.randint(4, 6)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > screen_height:
            self.rect.y = -50
            self.rect.x = random.randint(0, screen_width - 50)

# Setup groups
all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()

# Create car
car = Car()
all_sprites.add(car)

# Create obstacles
for i in range(5):
    obstacle = Obstacle()
    all_sprites.add(obstacle)
    obstacles.add(obstacle)

# Game loop
running = True
clock = pygame.time.Clock()
score = 0

while running:
    screen.fill(WHITE)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update sprites
    all_sprites.update()
    
    # Collision detection
    if pygame.sprite.spritecollide(car, obstacles, True):
        print("Game Over!")
        running = False
    
    # Draw everything
    all_sprites.draw(screen)
    
    # Score display
    score += 1
    font = pygame.font.SysFont(None, 36)
    text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(text, (10, 10))
    
    # Refresh the screen
    pygame.display.flip()

    # Set the speed of the game
    clock.tick(60)

# Quit Pygame
pygame.quit()
