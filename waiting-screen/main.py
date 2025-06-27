#!/usr/bin/env python3
"""
80's Style Waiting Screen with Island Sunset Scene
Beautiful 8-bit style animation with retro aesthetics
"""

import pygame
import math
import sys
from typing import Tuple

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# 80's Color Palette
COLORS = {
    'deep_purple': (25, 25, 112),
    'purple': (75, 0, 130),
    'pink': (255, 20, 147),
    'orange': (255, 140, 0),
    'yellow': (255, 215, 0),
    'cyan': (0, 255, 255),
    'magenta': (255, 0, 255),
    'dark_blue': (0, 0, 139),
    'ocean_blue': (0, 105, 148),
    'palm_green': (34, 139, 34),
    'sand_yellow': (238, 203, 173),
    'black': (0, 0, 0),
    'white': (255, 255, 255)
}

class WaitingScreen:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("We Come Back Soon - 80's Waiting Screen")
        self.clock = pygame.time.Clock()
        self.time = 0
        
        # Animation variables
        self.wave_offset = 0
        self.sun_pulse = 0
        self.palm_sway = 0
        self.text_glow = 0
        
        # Font setup
        self.large_font = pygame.font.Font(None, 48)
        self.medium_font = pygame.font.Font(None, 32)
        
    def draw_gradient_background(self):
        """Draw the gradient sky background"""
        for y in range(SCREEN_HEIGHT):
            # Create sunset gradient from top to bottom
            ratio = y / SCREEN_HEIGHT
            
            if ratio < 0.3:  # Top sky - deep purple to purple
                r = int(25 + (75 - 25) * (ratio / 0.3))
                g = int(25 + (0 - 25) * (ratio / 0.3))
                b = int(112 + (130 - 112) * (ratio / 0.3))
            elif ratio < 0.6:  # Middle sky - purple to pink/orange
                local_ratio = (ratio - 0.3) / 0.3
                r = int(75 + (255 - 75) * local_ratio)
                g = int(0 + (140 - 0) * local_ratio)
                b = int(130 + (0 - 130) * local_ratio)
            else:  # Bottom sky - orange to yellow
                local_ratio = (ratio - 0.6) / 0.4
                r = int(255)
                g = int(140 + (215 - 140) * local_ratio)
                b = int(0)
            
            color = (min(255, r), min(255, g), min(255, b))
            pygame.draw.line(self.screen, color, (0, y), (SCREEN_WIDTH, y))
    
    def draw_sun(self):
        """Draw the animated sun with pulsing effect"""
        sun_x = SCREEN_WIDTH // 2
        sun_y = int(150 + 20 * math.sin(self.sun_pulse))
        
        # Sun rays
        ray_length = 80 + 10 * math.sin(self.sun_pulse * 2)
        for angle in range(0, 360, 15):
            rad = math.radians(angle + self.time)
            start_x = sun_x + 50 * math.cos(rad)
            start_y = sun_y + 50 * math.sin(rad)
            end_x = sun_x + ray_length * math.cos(rad)
            end_y = sun_y + ray_length * math.sin(rad)
            pygame.draw.line(self.screen, COLORS['yellow'], (start_x, start_y), (end_x, end_y), 3)
        
        # Sun circle with gradient effect
        for radius in range(50, 0, -2):
            alpha = 255 - (50 - radius) * 3
            color_intensity = min(255, 200 + radius)
            sun_color = (color_intensity, color_intensity - 50, 0)
            pygame.draw.circle(self.screen, sun_color, (sun_x, sun_y), radius)
    
    def draw_ocean(self):
        """Draw the animated ocean with waves"""
        ocean_y = SCREEN_HEIGHT - 200
        
        # Ocean base
        ocean_rect = pygame.Rect(0, ocean_y, SCREEN_WIDTH, 200)
        pygame.draw.rect(self.screen, COLORS['ocean_blue'], ocean_rect)
        
        # Animated waves
        wave_points = []
        for x in range(0, SCREEN_WIDTH + 20, 10):
            wave_height = 15 * math.sin((x + self.wave_offset) * 0.02) + 10 * math.sin((x + self.wave_offset * 1.5) * 0.015)
            wave_points.append((x, ocean_y + wave_height))
        
        # Add bottom corners to close the polygon
        wave_points.append((SCREEN_WIDTH, SCREEN_HEIGHT))
        wave_points.append((0, SCREEN_HEIGHT))
        
        pygame.draw.polygon(self.screen, COLORS['cyan'], wave_points)
        
        # Wave reflections
        for i in range(len(wave_points) - 2):
            x, y = wave_points[i]
            next_x, next_y = wave_points[i + 1]
            reflection_color = (0, 200, 255, 100)
            pygame.draw.line(self.screen, reflection_color, (x, y + 20), (next_x, next_y + 20), 2)
    
    def draw_island(self):
        """Draw the island silhouette"""
        island_y = SCREEN_HEIGHT - 180
        
        # Island shape
        island_points = [
            (100, island_y),
            (150, island_y - 30),
            (200, island_y - 40),
            (250, island_y - 35),
            (300, island_y - 20),
            (350, island_y - 25),
            (400, island_y - 10),
            (450, island_y),
            (450, SCREEN_HEIGHT),
            (100, SCREEN_HEIGHT)
        ]
        
        pygame.draw.polygon(self.screen, COLORS['palm_green'], island_points)
        
        # Palm trees
        self.draw_palm_tree(180, island_y - 30)
        self.draw_palm_tree(320, island_y - 20)
        self.draw_palm_tree(380, island_y - 5)
    
    def draw_palm_tree(self, x: int, y: int):
        """Draw an animated palm tree"""
        sway = 5 * math.sin(self.palm_sway + x * 0.01)
        
        # Tree trunk
        trunk_points = [
            (x, y),
            (x + 5 + sway, y - 60),
            (x + 8 + sway, y - 60),
            (x + 3, y)
        ]
        pygame.draw.polygon(self.screen, (101, 67, 33), trunk_points)
        
        # Palm fronds
        frond_tip_x = x + 5 + sway
        frond_tip_y = y - 60
        
        frond_angles = [-60, -30, 0, 30, 60]
        for angle in frond_angles:
            angle_rad = math.radians(angle + sway * 2)
            frond_length = 40
            end_x = frond_tip_x + frond_length * math.cos(angle_rad)
            end_y = frond_tip_y + frond_length * math.sin(angle_rad)
            
            # Draw frond
            pygame.draw.line(self.screen, COLORS['palm_green'], 
                           (frond_tip_x, frond_tip_y), (end_x, end_y), 4)
            
            # Add frond details
            for i in range(3):
                detail_x = frond_tip_x + (end_x - frond_tip_x) * (i + 1) / 4
                detail_y = frond_tip_y + (end_y - frond_tip_y) * (i + 1) / 4
                offset = 8 * math.sin(angle_rad + math.pi/2)
                pygame.draw.line(self.screen, COLORS['palm_green'],
                               (detail_x, detail_y), 
                               (detail_x + offset, detail_y + offset/2), 2)
    
    def draw_grid_effect(self):
        """Draw retro grid effect at the bottom"""
        grid_y_start = SCREEN_HEIGHT - 120
        grid_spacing = 30
        line_color = (*COLORS['cyan'], 100)
        
        # Horizontal lines with perspective
        for i in range(4):
            y = grid_y_start + i * grid_spacing
            line_width = 2 if i % 2 == 0 else 1
            # Create perspective effect
            left_x = int(SCREEN_WIDTH * 0.2 * (4 - i) / 4)
            right_x = int(SCREEN_WIDTH - SCREEN_WIDTH * 0.2 * (4 - i) / 4)
            pygame.draw.line(self.screen, COLORS['cyan'], (left_x, y), (right_x, y), line_width)
        
        # Vertical lines
        for i in range(-10, 11):
            x_offset = i * 40 + self.time * 2
            if -50 < x_offset < SCREEN_WIDTH + 50:
                x = SCREEN_WIDTH // 2 + x_offset
                pygame.draw.line(self.screen, COLORS['cyan'], 
                               (x, grid_y_start), (x, SCREEN_HEIGHT), 1)
    
    def draw_text(self):
        """Draw the main title with glow effect"""
        title_text = "WE COME BACK SOON"
        
        # Glow effect
        glow_intensity = int(20 + 10 * math.sin(self.text_glow))
        
        # Multiple layers for glow
        for offset in range(glow_intensity, 0, -2):
            glow_color = (255, 0, 255, 255 - offset * 8)
            text_surface = self.large_font.render(title_text, True, COLORS['magenta'])
            text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, 80))
            
            # Draw glow layers
            for dx in [-offset, 0, offset]:
                for dy in [-offset, 0, offset]:
                    if dx != 0 or dy != 0:
                        self.screen.blit(text_surface, (text_rect.x + dx, text_rect.y + dy))
        
        # Main text
        text_surface = self.large_font.render(title_text, True, COLORS['white'])
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, 80))
        self.screen.blit(text_surface, text_rect)
        
        # Subtitle
        subtitle_text = "Please wait while we prepare something amazing..."
        subtitle_surface = self.medium_font.render(subtitle_text, True, COLORS['cyan'])
        subtitle_rect = subtitle_surface.get_rect(center=(SCREEN_WIDTH // 2, 120))
        self.screen.blit(subtitle_surface, subtitle_rect)
    
    def draw_loading_animation(self):
        """Draw a retro loading animation"""
        loading_y = SCREEN_HEIGHT - 50
        loading_width = 300
        loading_x = (SCREEN_WIDTH - loading_width) // 2
        
        # Loading bar background
        pygame.draw.rect(self.screen, COLORS['black'], 
                        (loading_x - 2, loading_y - 2, loading_width + 4, 24))
        pygame.draw.rect(self.screen, COLORS['white'], 
                        (loading_x, loading_y, loading_width, 20))
        
        # Animated loading progress
        progress = (math.sin(self.time * 0.1) + 1) / 2  # 0 to 1
        progress_width = int(loading_width * progress)
        
        # Gradient loading bar
        for i in range(progress_width):
            color_ratio = i / loading_width
            r = int(255 * (1 - color_ratio) + 0 * color_ratio)
            g = int(0 * (1 - color_ratio) + 255 * color_ratio)
            b = int(255 * (1 - color_ratio) + 255 * color_ratio)
            pygame.draw.line(self.screen, (r, g, b), 
                           (loading_x + i, loading_y), (loading_x + i, loading_y + 20))
        
        # Loading text
        loading_text = f"Loading... {int(progress * 100)}%"
        text_surface = self.medium_font.render(loading_text, True, COLORS['white'])
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, loading_y - 20))
        self.screen.blit(text_surface, text_rect)
    
    def update_animations(self, dt: float):
        """Update all animation variables"""
        self.time += dt
        self.wave_offset += dt * 50
        self.sun_pulse += dt * 2
        self.palm_sway += dt * 1.5
        self.text_glow += dt * 3
    
    def handle_events(self):
        """Handle pygame events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
        return True
    
    def run(self):
        """Main game loop"""
        running = True
        
        while running:
            dt = self.clock.tick(FPS) / 1000.0  # Delta time in seconds
            
            running = self.handle_events()
            
            # Update animations
            self.update_animations(dt)
            
            # Draw everything
            self.draw_gradient_background()
            self.draw_sun()
            self.draw_ocean()
            self.draw_island()
            self.draw_grid_effect()
            self.draw_text()
            self.draw_loading_animation()
            
            pygame.display.flip()
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    waiting_screen = WaitingScreen()
    waiting_screen.run()
