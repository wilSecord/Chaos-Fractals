import pygame
import random
import math

screen = pygame.display.set_mode((700, 700))

pygame.display.set_caption('Chaos Game')

pygame.display.flip()

running = True

white, black = (255, 255, 255), (0, 0, 0)

def new_point(f, s, mult):
    new = (0, 0)
    i_hat = mult * (s[0] - f[0])
    j_hat = mult * (s[1] - f[1])
    new = f[0] + round(i_hat), f[1] + round(j_hat)

    return new

def ngon_verts(n_verts, radius, position):
    tau = 6.28
    vert_list = [(round(math.cos(i / n_verts * tau) * radius + position[0]), round(math.sin(i / n_verts * tau) * radius + position[1])) for i in range(n_verts)]
    return vert_list

v_amnts = 10

verts = ngon_verts(v_amnts, 345, (350, 350))
a = random.choice(verts)

first_time = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not first_time:
        first_time = True
        for item in verts:
            screen.set_at(item, white)

    b = random.choice([item for item in verts if item != a])
    a = new_point(a, b, 0.75)
    screen.set_at(a, white)
    pygame.display.update()
