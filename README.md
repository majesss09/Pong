# Pong

A compact implementation of the classic Pong game written with Python's `turtle` module. This project demonstrates simple game loop mechanics, collision detection, and score handling using only the Python standard library.

## Features

- Simple two-player local gameplay (keyboard controls)
- Ball movement and bounce physics
- Scorekeeping and on-screen display
- Minimal dependencies — only Python 3 and `turtle`

## Requirements

- Python 3.x (includes the `turtle` module on standard CPython installs)

## Install & Run

1. Ensure you have Python 3 installed.
2. From the project root, run:

```bash
python main.py
```

The game window will open; use the keyboard controls below to play.

## Controls

- Left paddle: `w` (up), `s` (down)
- Right paddle: `Up Arrow` (up), `Down Arrow` (down)

Check `main.py` for exact key bindings if they were customized.

## Project Structure

- [main.py](main.py) — Game setup, screen, and main loop wiring.
- [ball.py](ball.py) — `Ball` behaviour: movement, bounce, and reset.
- [paddle.py](paddle.py) — `Paddle` class and input handling.
- [scoreboard.py](scoreboard.py) — Score display and update logic.

Each component is kept small and focused so you can inspect and learn from individual parts.

## How it works (brief)

- `main.py` creates the screen and instances of `Paddle`, `Ball`, and the scoreboard, then enters a timed loop to update positions and detect collisions.
- The `Ball` class handles edge bounces and paddle collisions. When a player misses, the ball resets and the scoreboard updates.

