#!/usr/bin/env python3
"""
80's Style ASCII Waiting Screen
Terminal-based retro waiting screen with animated ASCII art
No external dependencies required
"""

import time
import os
import sys
import threading
from typing import List

class ASCIIWaitingScreen:
    def __init__(self):
        self.running = True
        self.frame = 0
        self.animation_speed = 0.3
        
        # Color codes for terminal
        self.colors = {
            'reset': '\033[0m',
            'bold': '\033[1m',
            'magenta': '\033[95m',
            'cyan': '\033[96m',
            'yellow': '\033[93m',
            'red': '\033[91m',
            'green': '\033[92m',
            'blue': '\033[94m',
            'bg_black': '\033[40m',
            'bg_blue': '\033[44m',
            'bg_magenta': '\033[45m'
        }
        
        # Island frames for animation
        self.island_frames = [
            self.get_island_frame_1(),
            self.get_island_frame_2(),
            self.get_island_frame_3(),
            self.get_island_frame_2()
        ]
        
        # Wave animations
        self.wave_patterns = [
            "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
            "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
            "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
            "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        ]
    
    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def get_island_frame_1(self) -> List[str]:
        """Return the first frame of the island animation"""
        return [
            "                    ☀️                     ",
            "                   ╱  ╲                   ",
            "              ╭─────────────╮              ",
            "           ╭──╯             ╰──╮           ",
            "        ╭──╯                   ╰──╮        ",
            "     ╭──╯         🌴    🌴       ╰──╮     ",
            "   ╭─╯               🌴             ╰─╮   ",
            " ╭─╯                               ╰─╮ ",
            "─╯                                   ╰─"
        ]
    
    def get_island_frame_2(self) -> List[str]:
        """Return the second frame of the island animation"""
        return [
            "                     ☀️                    ",
            "                    ╱  ╲                  ",
            "              ╭─────────────╮              ",
            "           ╭──╯             ╰──╮           ",
            "        ╭──╯                   ╰──╮        ",
            "     ╭──╯        🌴     🌴        ╰──╮     ",
            "   ╭─╯              🌴              ╰─╮   ",
            " ╭─╯                                 ╰─╮ ",
            "─╯                                     ╰─"
        ]
    
    def get_island_frame_3(self) -> List[str]:
        """Return the third frame of the island animation"""
        return [
            "                   ☀️                      ",
            "                  ╱  ╲                    ",
            "              ╭─────────────╮              ",
            "           ╭──╯             ╰──╮           ",
            "        ╭──╯                   ╰──╮        ",
            "     ╭──╯       🌴      🌴       ╰──╮     ",
            "   ╭─╯             🌴              ╰─╮   ",
            " ╭─╯                               ╰─╮ ",
            "─╯                                   ╰─"
        ]
    
    def get_title_art(self) -> List[str]:
        """Return the main title in ASCII art"""
        return [
            "██╗    ██╗███████╗     ██████╗ ██████╗ ███╗   ███╗███████╗",
            "██║    ██║██╔════╝    ██╔════╝██╔═══██╗████╗ ████║██╔════╝",
            "██║ █╗ ██║█████╗      ██║     ██║   ██║██╔████╔██║█████╗  ",
            "██║███╗██║██╔══╝      ██║     ██║   ██║██║╚██╔╝██║██╔══╝  ",
            "╚███╔███╔╝███████╗    ╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗",
            " ╚══╝╚══╝ ╚══════╝     ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝",
            "",
            "    ██████╗  █████╗  ██████╗██╗  ██╗    ███████╗ ██████╗  ██████╗ ███╗   ██╗",
            "    ██╔══██╗██╔══██╗██╔════╝██║ ██╔╝    ██╔════╝██╔═══██╗██╔═══██╗████╗  ██║",
            "    ██████╔╝███████║██║     █████╔╝     ███████╗██║   ██║██║   ██║██╔██╗ ██║",
            "    ██╔══██╗██╔══██║██║     ██╔═██╗     ╚════██║██║   ██║██║   ██║██║╚██╗██║",
            "    ██████╔╝██║  ██║╚██████╗██║  ██╗    ███████║╚██████╔╝╚██████╔╝██║ ╚████║",
            "    ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝"
        ]
    
    def get_loading_bar(self) -> str:
        """Generate animated loading bar"""
        progress = (self.frame % 40) / 40
        filled = int(progress * 50)
        bar = "█" * filled + "░" * (50 - filled)
        percentage = int(progress * 100)
        return f"[{bar}] {percentage}%"
    
    def get_retro_border(self, width: int) -> str:
        """Generate retro border"""
        return "═" * width
    
    def draw_frame(self):
        """Draw a single frame of the animation"""
        self.clear_screen()
        
        # Get current island frame
        current_island = self.island_frames[self.frame % len(self.island_frames)]
        current_waves = self.wave_patterns[self.frame % len(self.wave_patterns)]
        
        # Print the scene
        print(self.colors['bg_black'] + self.colors['bold'])
        
        # Title
        print(self.colors['magenta'] + self.colors['bold'])
        title_lines = self.get_title_art()
        for line in title_lines:
            print(f"    {line}")
        
        print(self.colors['reset'] + self.colors['cyan'])
        print("    ┌─────────────────────────────────────────────────────────────────┐")
        print("    │                                                                 │")
        
        # Sky gradient simulation with colors
        print(f"    │  {self.colors['yellow']}✦{self.colors['magenta']}✧{self.colors['cyan']}✦{self.colors['yellow']}✧" * 15 + f"{self.colors['cyan']}  │")
        print("    │                                                                 │")
        
        # Island scene
        for line in current_island:
            print(f"    │  {self.colors['yellow']}{line}{self.colors['cyan']}  │")
        
        # Ocean waves
        print(f"    │  {self.colors['blue']}{current_waves}{self.colors['cyan']}  │")
        print(f"    │  {self.colors['blue']}{'~' * 56}{self.colors['cyan']}  │")
        print(f"    │  {self.colors['blue']}{'~' * 56}{self.colors['cyan']}  │")
        
        # Retro grid effect
        grid_line = "│  " + self.colors['cyan'] + "╭─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────╮" + "  │"
        print(f"    {grid_line}")
        for i in range(3):
            offset = (self.frame + i) % 9
            grid_content = "│     " * 9 + "│"
            if offset < len(grid_content):
                grid_content = grid_content[:offset] + "█" + grid_content[offset+1:]
            print(f"    │  {self.colors['cyan']}{grid_content}{self.colors['cyan']}  │")
        
        print("    │                                                                 │")
        print("    └─────────────────────────────────────────────────────────────────┘")
        
        # Loading section
        print(self.colors['reset'] + self.colors['green'])
        print(f"    Please wait while we prepare something amazing...")
        print()
        print(f"    {self.get_loading_bar()}")
        print()
        
        # Instructions
        print(self.colors['yellow'])
        print("    Press Ctrl+C to exit")
        print(self.colors['reset'])
    
    def run(self):
        """Main animation loop"""
        print(self.colors['bold'] + self.colors['magenta'])
        print("Starting 80's Waiting Screen...")
        print(self.colors['reset'])
        time.sleep(1)
        
        try:
            while self.running:
                self.draw_frame()
                self.frame += 1
                time.sleep(self.animation_speed)
        except KeyboardInterrupt:
            self.clear_screen()
            print(self.colors['bold'] + self.colors['cyan'])
            print("Thank you for waiting! ✨")
            print("See you soon! 🌴🌅")
            print(self.colors['reset'])
            self.running = False

if __name__ == "__main__":
    waiting_screen = ASCIIWaitingScreen()
    waiting_screen.run()
