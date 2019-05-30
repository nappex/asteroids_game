import os
import pyglet


HEIGHT = 800
WIDTH = 1100
resourcesPath = os.path.join(os.getcwd(), "models")

main_batch = pyglet.graphics.Batch()
backgroundOrder = pyglet.graphics.OrderedGroup(0)
foregroundOrder = pyglet.graphics.OrderedGroup(1)

# set the background
backgroundPath = os.path.join(resourcesPath, "backgrounds", "blue.png")
backgroundImgLoad = pyglet.image.load(backgroundPath)
background = pyglet.sprite.Sprite(backgroundImgLoad,
                                  batch=main_batch,
                                  group=backgroundOrder)
background.scale_x = WIDTH / background.width
background.scale_y = HEIGHT / background.height

objects = []

GAME_WINDOW = pyglet.window.Window(width=WIDTH, height=HEIGHT)


class Spaceship():
    def __init__(self):
        image = pyglet.image.load(os.path.join(resourcesPath,
                                               "PNG",
                                               "playerShip1_green.png"))
        image.anchor_x = image.width // 2
        image.anchor_y = image.height // 2
        self.sprite = pyglet.sprite.Sprite(image,
                                           WIDTH // 2,
                                           HEIGHT // 2,
                                           batch=main_batch,
                                           group=foregroundOrder)
        self.x = 0
        self.y = 0
        self.x_speed = 0
        self.y_speed = 0
        self.rotation = 0
        self.sprites = []

    def tick():
        pass


def draw_window():
    GAME_WINDOW.clear()
    main_batch.draw()


spaceship = Spaceship()

GAME_WINDOW.push_handlers(
        on_draw=draw_window,
                         )

if __name__ == "__main__":
    pyglet.app.run()
