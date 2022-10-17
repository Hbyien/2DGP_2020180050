import pico2d
import game_framework
import logo_state
import play_state
import item_state
import add_delete_boy


pico2d.open_canvas()
#game_framework.run(logo_state)
game_framework.run(play_state)

pico2d.clear_canvas()
