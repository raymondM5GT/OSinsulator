import pygame
from SnakeBasics import colors
from random import randint

SEGMENT_SIZE = 20

WINDOW_HEIGHT = 840
WINDOW_WIDTH = 800
WINDOW_DIMENSIONS = WINDOW_WIDTH, WINDOW_HEIGHT

KEY_MAP = {
    273: "Up",
    274: "Down",
    275: "Right",
    276: "Left"
}

pygame.init()
pygame.display.set_caption("Snake")
screen = pygame.display.set_mode(WINDOW_DIMENSIONS)
clock = pygame.time.Clock()


def draw_obj(SNAKE_POSITIONS, FOOD_POSITIONS):
    pygame.draw.rect(screen, colors.FOOD, [FOOD_POSITIONS, (SEGMENT_SIZE, SEGMENT_SIZE)])

    for x, y in SNAKE_POSITIONS:
        pygame.draw.rect(screen, colors.SNAKE, [x, y, SEGMENT_SIZE, SEGMENT_SIZE])


def set_food_position(SNAKE_POSITIONS):
    while True:
        x_position = randint(0, 39) * SEGMENT_SIZE
        y_position = randint(2, 41) * SEGMENT_SIZE
        FOOD_POSITIONS = (x_position, y_position)

        if FOOD_POSITIONS not in SNAKE_POSITIONS:
            return FOOD_POSITIONS


def move_snake(SNAKE_POSITIONS, direction):
    
    head_x_position, head_y_position = SNAKE_POSITIONS[0]

    if direction == "Left":
        new_head_position = (head_x_position - SEGMENT_SIZE, head_y_position)
    elif direction == "Right":
        new_head_position = (head_x_position + SEGMENT_SIZE, head_y_position)
    elif direction == "Down":
        new_head_position = (head_x_position, head_y_position + SEGMENT_SIZE)
    elif direction == "Up":
        new_head_position = (head_x_position, head_y_position - SEGMENT_SIZE)

    SNAKE_POSITIONS.insert(0, new_head_position)
    del SNAKE_POSITIONS[-1]


def on_key_press(event, current_direction):
    key = event.__dict__["key"]
    new_direction = KEY_MAP.get(key)

    all_directions = ("Up", "Down", "Left", "Right")
    opposite_directions = ({"Up", "Down"}, {"Left", "Right"})

    if (new_direction in all_directions and
            {new_direction, current_direction} not in opposite_directions):
        return new_direction

    return current_direction


def check_collisions_walls(SNAKE_POSITIONS):
    head_x_position, head_y_position = SNAKE_POSITIONS[0]

    return (head_x_position in (-20, WINDOW_WIDTH) or
            head_y_position in (20, WINDOW_HEIGHT) or
            (head_x_position, head_y_position) in SNAKE_POSITIONS[1:]
            )


def check_collisions_food(SNAKE_POSITIONS, FOOD_POSITIONS):
    if SNAKE_POSITIONS[0] == FOOD_POSITIONS:
        SNAKE_POSITIONS.append(SNAKE_POSITIONS[-1])

        return True


def game():
    Score = 0

    current_direction = "Right"
    SNAKE_POSITIONS = [(100, 100), (80, 100), (60, 100)]
    FOOD_POSITIONS = set_food_position(SNAKE_POSITIONS)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                current_direction = on_key_press(event, current_direction)

        screen.fill(colors.BG_color)
        draw_obj(SNAKE_POSITIONS, FOOD_POSITIONS)

        font = pygame.font.Font(None, 28)
        text = font.render(f"Score: {Score}", True, colors.TEXT)
        screen.blit(text, (10, 10))

        pygame.display.update()

        move_snake(SNAKE_POSITIONS, current_direction)

        if check_collisions_walls(SNAKE_POSITIONS):
            return

        if check_collisions_food(SNAKE_POSITIONS, FOOD_POSITIONS):
            FOOD_POSITIONS = set_food_position(SNAKE_POSITIONS)
            Score += 1

        clock.tick(5)


game()
