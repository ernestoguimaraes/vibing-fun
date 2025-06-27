# 🐍✨ Glamorous Snake Game

A modern, visually stunning Snake game built with Python and Pygame featuring neon colors, particle effects, and smooth animations.

![Snake Game](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Pygame](https://img.shields.io/badge/Pygame-2.0+-green.svg)
![Status](https://img.shields.io/badge/Status-Ready%20to%20Play-brightgreen.svg)

## 🌟 Features

### ✨ Visual Effects
- **Neon color palette** with purple, magenta, gold, and cyan
- **Glowing effects** around snake and food
- **Particle explosions** when eating food or dying
- **Pulsing food** with dynamic animations
- **Snake trail** that fades behind the snake
- **Grid overlay** for a modern look

### 🎮 Gameplay
- Smooth snake movement with responsive controls
- Score tracking with persistent high scores
- Game over screen with restart functionality
- Progressive challenge as snake grows

### 🎯 Controls
- **Arrow Keys** or **WASD** - Move snake
- **Space** - Restart game (when game over)
- **Escape** - Quit game

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation & Running

#### Option 1: Using Virtual Environment (Recommended)
```bash
# Navigate to the game directory
cd snake-game

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the game
python main.py
```

#### Option 2: System-wide Installation
```bash
# Install pygame system-wide (if allowed)
pip install pygame>=2.0.0

# Run the game
python main.py
```

#### Option 3: Using pipx (Alternative)
```bash
# If you have pipx installed
pipx run --spec pygame python main.py
```

## 🎮 How to Play

1. **Start the Game**: Run `python main.py`
2. **Control the Snake**: Use arrow keys or WASD to move
3. **Eat Food**: Guide your snake to the glowing golden food
4. **Avoid Collisions**: Don't hit walls or your own body
5. **Beat High Scores**: Try to achieve the highest score possible
6. **Restart**: Press Space when game over, or Escape to quit

## 🎨 Game Elements

- **Snake Head**: Bright magenta circle with white eye
- **Snake Body**: Purple segments that fade as they get longer
- **Food**: Golden, pulsing circle with glow effects
- **Trail**: Fading light trail behind the snake
- **Particles**: Explosion effects for visual feedback

## 🔧 Customization

You can easily customize the game by modifying the constants in `main.py`:

```python
# Window size
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700

# Grid size (affects snake/food size)
GRID_SIZE = 20

# Colors
SNAKE_HEAD_COLOR = (255, 100, 255)  # Bright magenta
FOOD_COLOR = (255, 215, 0)          # Gold
BACKGROUND_COLOR = (15, 15, 35)     # Dark blue

# Game speed (lower = faster)
self.clock.tick(10)  # In the Game.run() method
```

## 📦 Dependencies

- **pygame**: Game development library for graphics and input handling

See `requirements.txt` for exact version requirements.

## 🐛 Troubleshooting

### Common Issues

1. **"externally-managed-environment" error**:
   - Use a virtual environment (see Option 1 above)
   - Or use `pip install --break-system-packages pygame` (not recommended)

2. **"No module named pygame"**:
   - Make sure pygame is installed: `pip install pygame`
   - Verify your virtual environment is activated

3. **Game window doesn't open**:
   - Ensure you have a display/GUI environment
   - Check if running in a headless environment

4. **Performance issues**:
   - Close other applications to free up resources
   - Adjust `GRID_SIZE` for better performance on older hardware

### System Requirements
- Python 3.7+
- Graphics display capability
- Keyboard input support
- At least 50MB free RAM

## 🎯 Game Tips

- **Strategy**: Plan your moves ahead to avoid trapping yourself
- **Speed**: The game runs at a fixed speed, focus on precision
- **High Scores**: Longer snakes = higher scores, but more challenge
- **Visual Cues**: Use the trail and glow effects to judge distances

## 🤝 Contributing

Feel free to fork this project and add your own features:
- Different food types with special effects
- Power-ups and special abilities
- Multiple difficulty levels
- Sound effects and music
- Leaderboard system

## 📄 License

This project is open source. Feel free to use, modify, and distribute.

## 🎉 Enjoy!

Have fun playing the Glamorous Snake Game! Try to beat your high score and enjoy the beautiful visual effects.

---
*Created with ❤️ and lots of neon colors*
