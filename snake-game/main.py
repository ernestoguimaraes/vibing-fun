import pygame
import random
import math
import sys
from enum import Enum
from typing import List, Tuple

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE

# Colors with glamorous palette
BACKGROUND_COLOR = (15, 15, 35)  # Dark blue
GRID_COLOR = (25, 25, 45)
SNAKE_HEAD_COLOR = (255, 100, 255)  # Bright magenta
SNAKE_BODY_COLOR = (200, 50, 200)   # Purple
SNAKE_GLOW_COLOR = (255, 150, 255)  # Light magenta
FOOD_COLOR = (255, 215, 0)          # Gold
FOOD_GLOW_COLOR = (255, 255, 100)   # Light yellow
TEXT_COLOR = (255, 255, 255)
ACCENT_COLOR = (0, 255, 255)        # Cyan

class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

class Particle:
    def __init__(self, x: float, y: float, color: Tuple[int, int, int]):
        self.x = x
        self.y = y
        self.vx = random.uniform(-2, 2)
        self.vy = random.uniform(-2, 2)
        self.life = 60
        self.max_life = 60
        self.color = color
        self.size = random.uniform(2, 5)

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.life -= 1
        self.vx *= 0.98
        self.vy *= 0.98

    def draw(self, screen: pygame.Surface):
        if self.life > 0:
            alpha = int(255 * (self.life / self.max_life))
            size = int(self.size * (self.life / self.max_life))
            if size > 0:
                color_with_alpha = (*self.color, alpha)
                temp_surface = pygame.Surface((size * 2, size * 2), pygame.SRCALPHA)
                pygame.draw.circle(temp_surface, color_with_alpha, (size, size), size)
                screen.blit(temp_surface, (self.x - size, self.y - size))

class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = Direction.RIGHT
        self.grow = False
        self.trail_positions = []

    def move(self):
        head = self.body[0]
        new_head = (
            head[0] + self.direction.value[0],
            head[1] + self.direction.value[1]
        )
        
        self.trail_positions.append((head[0] * GRID_SIZE + GRID_SIZE // 2, 
                                   head[1] * GRID_SIZE + GRID_SIZE // 2))
        if len(self.trail_positions) > 20:
            self.trail_positions.pop(0)
        
        self.body.insert(0, new_head)
        
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def change_direction(self, new_direction: Direction):
        opposite_directions = {
            Direction.UP: Direction.DOWN,
            Direction.DOWN: Direction.UP,
            Direction.LEFT: Direction.RIGHT,
            Direction.RIGHT: Direction.LEFT
        }
        
        if new_direction != opposite_directions.get(self.direction):
            self.direction = new_direction

    def check_collision(self) -> bool:
        head = self.body[0]
        
        # Wall collision
        if (head[0] < 0 or head[0] >= GRID_WIDTH or 
            head[1] < 0 or head[1] >= GRID_HEIGHT):
            return True
        
        # Self collision
        if head in self.body[1:]:
            return True
        
        return False

    def eat_food(self):
        self.grow = True

    def draw(self, screen: pygame.Surface, particles: List[Particle]):
        # Draw trail
        for i, pos in enumerate(self.trail_positions):
            alpha = int(50 * (i / len(self.trail_positions)))
            if alpha > 0:
                trail_surface = pygame.Surface((6, 6), pygame.SRCALPHA)
                pygame.draw.circle(trail_surface, (*SNAKE_GLOW_COLOR, alpha), (3, 3), 3)
                screen.blit(trail_surface, (pos[0] - 3, pos[1] - 3))

        # Draw snake body with glow effect
        for i, segment in enumerate(self.body):
            x = segment[0] * GRID_SIZE
            y = segment[1] * GRID_SIZE
            
            # Glow effect
            glow_surface = pygame.Surface((GRID_SIZE + 10, GRID_SIZE + 10), pygame.SRCALPHA)
            if i == 0:  # Head
                pygame.draw.circle(glow_surface, (*SNAKE_GLOW_COLOR, 50), 
                                 (GRID_SIZE // 2 + 5, GRID_SIZE // 2 + 5), GRID_SIZE // 2 + 5)
                screen.blit(glow_surface, (x - 5, y - 5))
                
                # Head with gradient
                pygame.draw.circle(screen, SNAKE_HEAD_COLOR, (x + GRID_SIZE // 2, y + GRID_SIZE // 2), GRID_SIZE // 2)
                pygame.draw.circle(screen, (255, 255, 255), (x + GRID_SIZE // 2 - 3, y + GRID_SIZE // 2 - 3), 3)
            else:  # Body
                body_color = tuple(int(c * (1 - i * 0.05)) for c in SNAKE_BODY_COLOR)
                pygame.draw.circle(glow_surface, (*SNAKE_GLOW_COLOR, 30), 
                                 (GRID_SIZE // 2 + 5, GRID_SIZE // 2 + 5), GRID_SIZE // 2 + 3)
                screen.blit(glow_surface, (x - 5, y - 5))
                pygame.draw.circle(screen, body_color, (x + GRID_SIZE // 2, y + GRID_SIZE // 2), GRID_SIZE // 2 - 1)

class Food:
    def __init__(self):
        self.position = self.generate_position()
        self.pulse = 0

    def generate_position(self) -> Tuple[int, int]:
        return (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

    def draw(self, screen: pygame.Surface):
        x = self.position[0] * GRID_SIZE
        y = self.position[1] * GRID_SIZE
        
        # Pulsing effect
        self.pulse += 0.2
        pulse_size = int(3 * math.sin(self.pulse))
        
        # Glow effect
        glow_surface = pygame.Surface((GRID_SIZE + 20, GRID_SIZE + 20), pygame.SRCALPHA)
        pygame.draw.circle(glow_surface, (*FOOD_GLOW_COLOR, 80), 
                         (GRID_SIZE // 2 + 10, GRID_SIZE // 2 + 10), GRID_SIZE // 2 + 10)
        screen.blit(glow_surface, (x - 10, y - 10))
        
        # Food with pulsing
        pygame.draw.circle(screen, FOOD_COLOR, 
                         (x + GRID_SIZE // 2, y + GRID_SIZE // 2), 
                         GRID_SIZE // 2 + pulse_size)
        pygame.draw.circle(screen, (255, 255, 255), 
                         (x + GRID_SIZE // 2 - 2, y + GRID_SIZE // 2 - 2), 2)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Glamorous Snake Game")
        self.clock = pygame.time.Clock()
        self.font_large = pygame.font.Font(None, 48)
        self.font_medium = pygame.font.Font(None, 36)
        self.font_small = pygame.font.Font(None, 24)
        
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.high_score = 0
        self.game_over = False
        self.particles = []
        
        # Ensure food doesn't spawn on snake
        while self.food.position in self.snake.body:
            self.food.position = self.food.generate_position()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if self.game_over:
                    if event.key == pygame.K_SPACE:
                        self.restart_game()
                    elif event.key == pygame.K_ESCAPE:
                        return False
                else:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.snake.change_direction(Direction.UP)
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.snake.change_direction(Direction.DOWN)
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.snake.change_direction(Direction.LEFT)
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.snake.change_direction(Direction.RIGHT)
        return True

    def update(self):
        if not self.game_over:
            self.snake.move()
            
            # Check food collision
            if self.snake.body[0] == self.food.position:
                self.snake.eat_food()
                self.score += 10
                
                # Create particles
                food_x = self.food.position[0] * GRID_SIZE + GRID_SIZE // 2
                food_y = self.food.position[1] * GRID_SIZE + GRID_SIZE // 2
                for _ in range(15):
                    self.particles.append(Particle(food_x, food_y, FOOD_COLOR))
                
                # Generate new food
                self.food.position = self.food.generate_position()
                while self.food.position in self.snake.body:
                    self.food.position = self.food.generate_position()
            
            # Check collisions
            if self.snake.check_collision():
                self.game_over = True
                if self.score > self.high_score:
                    self.high_score = self.score
                
                # Death particles
                head = self.snake.body[0]
                head_x = head[0] * GRID_SIZE + GRID_SIZE // 2
                head_y = head[1] * GRID_SIZE + GRID_SIZE // 2
                for _ in range(30):
                    self.particles.append(Particle(head_x, head_y, SNAKE_HEAD_COLOR))
        
        # Update particles
        self.particles = [p for p in self.particles if p.life > 0]
        for particle in self.particles:
            particle.update()

    def draw_grid(self):
        for x in range(0, WINDOW_WIDTH, GRID_SIZE):
            pygame.draw.line(self.screen, GRID_COLOR, (x, 0), (x, WINDOW_HEIGHT))
        for y in range(0, WINDOW_HEIGHT, GRID_SIZE):
            pygame.draw.line(self.screen, GRID_COLOR, (0, y), (WINDOW_WIDTH, y))

    def draw_ui(self):
        # Score
        score_text = self.font_medium.render(f"Score: {self.score}", True, TEXT_COLOR)
        self.screen.blit(score_text, (10, 10))
        
        # High Score
        high_score_text = self.font_small.render(f"High Score: {self.high_score}", True, ACCENT_COLOR)
        self.screen.blit(high_score_text, (10, 50))
        
        # Controls
        controls_text = self.font_small.render("Use Arrow Keys or WASD to move", True, (150, 150, 150))
        self.screen.blit(controls_text, (10, WINDOW_HEIGHT - 30))

    def draw_game_over(self):
        # Semi-transparent overlay
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))
        
        # Game Over text with glow
        game_over_text = self.font_large.render("GAME OVER", True, (255, 100, 100))
        glow_text = self.font_large.render("GAME OVER", True, (255, 200, 200))
        
        text_rect = game_over_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50))
        glow_rect = glow_text.get_rect(center=(WINDOW_WIDTH // 2 + 2, WINDOW_HEIGHT // 2 - 48))
        
        self.screen.blit(glow_text, glow_rect)
        self.screen.blit(game_over_text, text_rect)
        
        # Final score
        final_score_text = self.font_medium.render(f"Final Score: {self.score}", True, TEXT_COLOR)
        score_rect = final_score_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        self.screen.blit(final_score_text, score_rect)
        
        # Instructions
        restart_text = self.font_small.render("Press SPACE to restart or ESC to quit", True, ACCENT_COLOR)
        restart_rect = restart_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50))
        self.screen.blit(restart_text, restart_rect)

    def restart_game(self):
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.game_over = False
        self.particles = []
        
        while self.food.position in self.snake.body:
            self.food.position = self.food.generate_position()

    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.draw_grid()
        
        # Draw particles
        for particle in self.particles:
            particle.draw(self.screen)
        
        # Draw game objects
        self.food.draw(self.screen)
        self.snake.draw(self.screen, self.particles)
        
        # Draw UI
        self.draw_ui()
        
        if self.game_over:
            self.draw_game_over()
        
        pygame.display.flip()

    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(10)  # Snake speed
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()