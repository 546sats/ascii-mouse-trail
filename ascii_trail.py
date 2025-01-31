from asciimatics.screen import Screen
import random

# Symbols used for trails and effects
symbols = ["@", "#", "$", "₿", "&", "*", "~", "^", "!", "░", "▒", "▓", "█"]

def interactive_mouse(screen):
    mouse_trails = []  # Store mouse trails as (x, y, symbol, color, lifetime)

    while True:
        # Capture mouse input
        event = screen.get_event()

        # Clear the screen for the current frame
        screen.clear()

        # Handle mouse input and add to trail
        if event and event.x is not None and event.y is not None:
            # Add a new trail point with a long lifetime
            mouse_trails.append((event.x, event.y, random.choice(symbols), random.randint(1, 7), 300))

            # Create a burst effect around the mouse position
            for _ in range(10):  # Increase for denser bursts
                x = event.x + random.randint(-3, 3)
                y = event.y + random.randint(-3, 3)
                if 0 <= x < screen.width and 0 <= y < screen.height:
                    screen.print_at(random.choice(symbols), x, y, random.randint(1, 7))

        # Update and draw mouse trails
        updated_trails = []
        for trail_x, trail_y, symbol, color, lifetime in mouse_trails:
            if lifetime > 0:
                screen.print_at(symbol, trail_x, trail_y, color)
                updated_trails.append((trail_x, trail_y, symbol, color, lifetime - 1))  # Reduce lifetime

        mouse_trails = updated_trails

        # Create random background effects
        for _ in range(50):  # Adjust for more/less density
            x = random.randint(0, screen.width - 1)
            y = random.randint(0, screen.height - 1)
            screen.print_at(random.choice(symbols), x, y, random.randint(1, 7))

        # Refresh the screen for the next frame
        screen.refresh()

# Run the interactive mouse tracker in fullscreen mode
Screen.wrapper(interactive_mouse)
