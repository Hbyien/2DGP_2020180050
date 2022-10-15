from pico2d import *


TUK_WIDTH, TUK_HEIGHT = 800, 600



def handle_events():
    global running
    global dir
    global uir
    global bottom
    global x,y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                dir -= 1
                bottom =0
            elif event.key == SDLK_RIGHT:
                dir += 1
                bottom = 100
            elif event.key == SDLK_UP:
                uir +=1
            elif event.key == SDLK_DOWN:
                uir -=1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type ==SDL_KEYUP:
            if event.key ==SDLK_LEFT:
                dir +=1
            elif event.key == SDLK_RIGHT:
                dir -=1
            elif event.key == SDLK_UP:
                uir -=1
            elif event.key == SDLK_DOWN:
                uir+=1
    pass




open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')


running = True


x = TUK_WIDTH // 2
y = TUK_HEIGHT//2
frame = 0
dir = 0
uir = 0
bottom = 100

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    character.clip_draw(frame * 100, bottom, 100, 100, x, y)
    update_canvas()
    handle_events()

    frame = (frame + 1) %8

    x+= dir*5
    if(x==5):
        x+=5
    if(x==TUK_WIDTH-5):
        x-=5
    y += uir*5
    if (y == 5):
        y += 5
    if (y == TUK_HEIGHT - 5):
        y -= 5
    delay(0.01)


close_canvas()

