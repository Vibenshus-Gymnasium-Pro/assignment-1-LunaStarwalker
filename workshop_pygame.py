import pygame as pg

pg.init()

screen = pg.display.set_mode((1200, 800))

pg.display.set_caption("Workshop")

"""icon = pg.image.load("")
pg.display.set_icon(icon)"""

player_pos = pg.Vector2(screen.get_width() / 2, screen.get_height() / 2)

dt = 0

while True:

    pg.draw.circle(screen, (0, 255, 0), player_pos, 40)

    keys = pg.key.get_pressed()

    match keys:

        case pg.K_UP:
            player_pos.y -= 10

    pg.display.flip()

    for event in pg.event.get():
        if event.type == pg.quit():
            pg.quit()