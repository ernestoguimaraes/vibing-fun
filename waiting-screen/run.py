#!/usr/bin/env python3
"""
80's Waiting Screen Launcher
Automatically chooses between pygame and ASCII versions
"""

import sys
import subprocess
import os

def check_pygame():
    """Check if pygame is available"""
    try:
        import pygame
        return True
    except ImportError:
        return False

def run_pygame_version():
    """Run the full pygame version"""
    print("🎮 Starting full graphics version...")
    os.system("python3 main.py")

def run_ascii_version():
    """Run the ASCII fallback version"""
    print("📺 Starting ASCII version...")
    os.system("python3 ascii_main.py")

def install_pygame():
    """Try to install pygame"""
    print("🔧 Pygame not found. Attempting to install...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame"])
        return True
    except:
        try:
            subprocess.check_call(["pip3", "install", "pygame"])
            return True
        except:
            return False

def main():
    print("🌴 80's Waiting Screen Launcher 🌅")
    print("=" * 40)
    
    if check_pygame():
        print("✅ Pygame found!")
        choice = input("Choose version:\n1. Full Graphics (pygame)\n2. ASCII Terminal\nEnter choice (1/2): ").strip()
        
        if choice == "1":
            run_pygame_version()
        else:
            run_ascii_version()
    else:
        print("❌ Pygame not found.")
        install_choice = input("Install pygame for full graphics? (y/n): ").strip().lower()
        
        if install_choice == 'y':
            if install_pygame():
                print("✅ Pygame installed successfully!")
                run_pygame_version()
            else:
                print("❌ Failed to install pygame. Using ASCII version...")
                run_ascii_version()
        else:
            print("📺 Using ASCII version...")
            run_ascii_version()

if __name__ == "__main__":
    main()
