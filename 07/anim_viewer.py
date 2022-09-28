from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('anim_viewer.png')

x = 0
frame = 0
bottom = 0

while (x < 800):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame*97, 280-bottom, 97, 70, x, 90)
    update_canvas()
    frame = (frame+1)%6
    if frame ==0:
        bottom=bottom+70
        if bottom > 280:
            bottom=0
            delay(0.5)
    x += 5
    delay(0.1)
    get_events()


close_canvas()

