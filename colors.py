from collections import namedtuple

color = namedtuple("color", ["red", "green", "blue"])
BG_color = color(red=60, green=144, blue=80)
SNAKE = color(red=255, green=200, blue=100)
FOOD = color(red=200, green=188, blue=69)
TEXT = color(red=255, green=95, blue=165)

