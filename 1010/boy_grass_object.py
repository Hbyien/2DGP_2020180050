from pico2d import *
import random

# 잔디 클래스, 잔디 클래스가 필요
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)
    pass

#소년을 만들려면, 소년 클래스가 필요.
class Boy:
    def __init__(self):
        self.x, self.y = random.randint(0, 400), 90
        self.frame = random.randint(0,7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame+1)%8
        self.x +=5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
    pass



# Game object class here

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()

# initialization code
grass = Grass() #잔디객체 생성
#boy = Boy()
team = [Boy() for i in range(11)]

running = True
while running:

    handle_events()

    #시물레이션
    for boy in team:
        boy.update()


    #랜더링 : 보여준다.
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    update_canvas()

    delay(0.05)

del boy
del grass

close_canvas()



# game main loop code

# finalization code