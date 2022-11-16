from pico2d import *
import game_framework
import play_state
import title_state


# fill here
# running = True
image = None
count = 1


def enter():
    global image
    image = load_image('add_delete_boy.png')
    pass

def exit():
    global image
    del image
    pass

def update():
    play_state.update()
    pass

def draw():
    clear_canvas()
    play_state.draw_world()
    image.draw(400,300)
    update_canvas()
    pass

def handle_events():
    global count
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_state()
                case pico2d.SDLK_b:
                    game_framework.pop_state()
                case pico2d.SDLK_k:
                    if count ==1:
                        game_framework.pop_state()
                        pass
                    count -=1
                    play_state.add_boy(count)
                case pico2d.SDLK_j:
                    count += 1
                    play_state.add_boy(count)
                    game_framework.pop_state()







