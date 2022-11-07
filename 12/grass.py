from pico2d import *

class Grass1:
    def __init__(self):
        self.image = load_image('grass.png')

    def update(self):
        pass
    def draw(self):
        self.image.draw(400, 30)

class Grass2:
    def __init__(self):
        self.image = load_image('grass.png')

    def update(self):
        pass
    def draw(self):
        self.image.draw(400, 10)


