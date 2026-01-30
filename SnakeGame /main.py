import pygame
import random
import sys

# ---------- Config ----------
CELL = 20                 # size of each grid cell (px)
GRID_W, GRID_H = 30, 20   # grid size (cells) => window = 600x400
W, H = GRID_W * CELL, GRID_H * CELL

FPS_START = 10            # starting speed
FPS_STEP = 0.2            # speed increase per food

# Colors (RGB)
BG = (18, 18, 18)
SNAKE = (0, 220, 120)
FOOD = (240, 80, 80)
GRID = (30, 30, 30)
TEXT = (235, 235, 235)

# ---------- Helpers ----------
def rand_food(excluded):
    """Pick a random cell not in excluded (snake body)."""
    while True:
        pos = (random.randrange(GRID_W), random.randrange(GRID_H))
        if pos not in excluded:
            return pos

def draw_cell(screen, pos, color):
    x, y = pos
    rect = pygame.Rect(x * CELL, y * CELL, CELL, CELL)
    pygame.draw.rect(screen, color, rect, border_radius=4)

def draw_grid(screen):
    for x in range(0, W, CELL):
        pygame.draw.line(screen, GRID, (x, 0), (x, H))
    for y in range(0, H, CELL):
        pygame.draw.line(screen, GRID, (0, y), (W, y))

def game_over_screen(screen, font, score):
    screen.fill(BG)
    msg1 = font.render("Game Over", True, TEXT)
    msg2 = font.render(f"Score: {score}", True, TEXT)
    msg3 = font.render("Press R to Restart or Q to Quit", True, TEXT)

    screen.blit(msg1, msg1.get_rect(center=(W // 2, H // 2 - 40)))
    screen.blit(msg2, msg2.get_rect(center=(W // 2, H // 2)))
    screen.blit(msg3, msg3.get_rect(center=(W // 2, H // 2 + 40)))
    pygame.display.flip()

def main():
    pygame.init()
    pygame.display.set_caption("Classic Snake (Python)")
    screen = pygame.display.set_mode((W, H))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("consolas", 26)

    def reset():
        snake = [(GRID_W // 2, GRID_H // 2)]
        direction = (1, 0)   # moving right
        pending_dir = direction
        food = rand_food(set(snake))
        score = 0
        fps = FPS_START
        return snake, direction, pending_dir, food, score, fps

    snake, direction, pending_dir, food, score, fps = reset()

    running = True
    alive = True

    while running:
        clock.tick(fps)

        # -------- Events --------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if alive:
                    # Prevent 180-degree turns
                    if event.key in (pygame.K_UP, pygame.K_w) and direction != (0, 1):
                        pending_dir = (0, -1)
                    elif event.key in (pygame.K_DOWN, pygame.K_s) and direction != (0, -1):
                        pending_dir = (0, 1)
                    elif event.key in (pygame.K_LEFT, pygame.K_a) and direction != (1, 0):
                        pending_dir = (-1, 0)
                    elif event.key in (pygame.K_RIGHT, pygame.K_d) and direction != (-1, 0):
                        pending_dir = (1, 0)
                else:
                    if event.key == pygame.K_r:
                        snake, direction, pending_dir, food, score, fps = reset()
                        alive = True
                    elif event.key in (pygame.K_q, pygame.K_ESCAPE):
                        running = False

        if not running:
            break

        if not alive:
            game_over_screen(screen, font, score)
            continue

        # -------- Update --------
        direction = pending_dir
        head_x, head_y = snake[0]
        dx, dy = direction
        new_head = (head_x + dx, head_y + dy)

        # Wall collision
        if not (0 <= new_head[0] < GRID_W and 0 <= new_head[1] < GRID_H):
            alive = False
            continue

        # Self collision
        if new_head in snake:
            alive = False
            continue

        snake.insert(0, new_head)

        # Eat food
        if new_head == food:
            score += 1
            fps = FPS_START + score * FPS_STEP
            food = rand_food(set(snake))
        else:
            snake.pop()  # move forward

        # -------- Draw --------
        screen.fill(BG)
        draw_grid(screen)

        draw_cell(screen, food, FOOD)
        for i, part in enumerate(snake):
            draw_cell(screen, part, SNAKE)

        score_surf = font.render(f"Score: {score}", True, TEXT)
        screen.blit(score_surf, (10, 10))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
