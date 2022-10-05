from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('run.png')

x = 0
frame = 0
while (x < 800):

    for x in range(0,400, 3):
        character.clip_draw(frame*80, 130, 80, 80, x, 90)
        update_canvas()
        frame = (frame+1)%8
        clear_canvas()
        grass.draw(400, 30)
        delay(0.05)
    get_events()


close_canvas()

