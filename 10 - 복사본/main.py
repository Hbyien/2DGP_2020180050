import pico2d
import play_state
import logo_state

start_state = logo_state #모듈을 변수로 취급

# start_state.enter()
pico2d.open_canvas()

states = [logo_state, play_state]
for state in states:
    state.enter()
    while state.running:
        state.handle_events()
        state.update()
        state.draw()
    state.exit()

# game main loop code
# while start_state.running:
#     start_state.handle_events()
#
#     start_state.update()
#     start_state.draw()
#
#     pico2d.delay(0.05)
# start_state.exit()



# finalization code
pico2d.close_canvas()