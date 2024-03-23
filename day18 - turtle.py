import turtle
import random
# import colorgram

timmy = turtle.Turtle()
window = turtle.Screen()
window.setup(700, 700)

# successively larger polygons
# timmy.penup()
# timmy.setposition(-50, 345)
# timmy.pendown()

# for _ in range(3, 11):
#     timmy.color(random.random(), random.random(), random.random())
#     sides = _
#     angles = 360 / sides
#     timmy.forward(100)
#     for x in range(1, sides):
#         timmy.right(angles)
#         timmy.forward(100)
#     timmy.right(angles)

#random walk
# DIRECTIONS = [0, 90, 180, -90]
# timmy.shapesize(2, 2)
# timmy.pensize(20)
# timmy.speed(8)

# for x in range(1000):
#     timmy.color(random.random(), random.random(), random.random())
#     timmy.setheading(random.choice(DIRECTIONS))
#     timmy.forward(50)

# circle spirograph
# timmy.speed('fastest')
# timmy.pensize(2)
# timmy.color(1, 0, 0)
# starting_color = [1, 0, 0]
# for _ in range(30):
#     starting_color[0] -= .03
#     starting_color[1] += .02
#     starting_color[2] += .03
#     timmy.color(starting_color[0], starting_color[1], starting_color[2])
#     timmy.circle(200)
#     timmy.right(6)
# for _ in range(30):
#     starting_color[0] += .03
#     starting_color[1] -= .02
#     starting_color[2] -= .03
#     timmy.color(starting_color[0], starting_color[1], starting_color[2])
#     timmy.circle(200)
#     timmy.right(6)

# extract = colorgram.extract("image.jpg", 40)
# for x in extract:
#     color_raw = x.rgb
#     color = (color_raw.r, color_raw.g, color_raw.b)
#     colors.append(color)
# print(colors)

# color-picked from Van Gogh's "Starry Night"
colors = [(69, 95, 135), (22, 31, 54), (126, 151, 176), (24, 33, 28),
          (37, 53, 114), (146, 166, 153), (35, 32, 24), (171, 172, 130),
          (94, 122, 172), (85, 102, 93), (101, 100, 70), (158, 151, 64),
          (202, 203, 147), (215, 215, 187), (197, 214, 200), (73, 78, 34),
          (113, 137, 125), (28, 24, 27), (105, 136, 145), (191, 207, 222),
          (52, 71, 60), (178, 200, 183), (169, 187, 222), (46, 70, 77),
          (93, 87, 91), (175, 198, 203), (158, 152, 156), (84, 55, 48),
          (213, 207, 211), (70, 59, 64), (132, 124, 129), (135, 125, 122),
          (195, 189, 195), (201, 188, 185)]

# Hirst dot painting
LEFT = -window.window_width() / 2
BOTTOM = -window.window_height() / 2
SPACING = 70

timmy.penup()
timmy.setposition(0.9 * BOTTOM, 0.9 * LEFT)
window.colormode(255)

def draw_dot():
    '''Draws each dot, selects color randomly.'''
    timmy.dot(30, random.choice(colors))
    timmy.forward(SPACING)

def full_line(height):
    '''Draws 10 dots, 'carriage returns' to next line.'''
    for _ in range(10):
        draw_dot()
    timmy.setpos(0.9 * LEFT, 0.9 * BOTTOM + height)

for x in range(10):
    full_line((x + 1) * SPACING)

screen = turtle.Screen()
screen.exitonclick()
