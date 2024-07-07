import pygame
import random
import math

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Ball parameters
RADIUS = 20
NUM_CIRCLES = 5

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BALL_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]  # Example colors

# Circle class
class Circle:
    def __init__(self):
        self.x = random.randint(RADIUS, WIDTH - RADIUS)
        self.y = random.randint(RADIUS, HEIGHT - RADIUS)
        self.dx = random.uniform(-5, 5)
        self.dy = random.uniform(-5, 5)
        self.color = random.choice(BALL_COLORS)

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if not 0 < self.x < WIDTH:
            self.dx = -self.dx
        if not 0 < self.y < HEIGHT:
            self.dy = -self.dy

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), RADIUS)

    def collide(self, other):
        if math.hypot(self.x - other.x, self.y - other.y) < 2 * RADIUS:
            self.dx, other.dx = other.dx, self.dx
            self.dy, other.dy = other.dy, self.dy

# Initialize pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Circle Collisions")
clock = pygame.time.Clock()

# Create circles
circles = [Circle() for _ in range(NUM_CIRCLES)]
running = True

# Main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move circles and handle collisions
    [circle.move() for circle in circles]
    [circle.collide(other) for i, circle in enumerate(circles) for other in circles[i + 1:]]

    # Draw everything
    screen.fill(BLACK)  # Fill background color
    [circle.draw(screen) for circle in circles]

    pygame.display.flip()  # Update display
    clock.tick(60)  # Cap FPS

pygame.quit()
