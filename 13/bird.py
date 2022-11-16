from pico2d import *
import game_world
import game_framework

#1 : 이벤트 정의
RD, LD, RU, LU = range(4)
event_name = ['RD', 'LD', 'RU', 'LU']

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU
}

# Boy Run Speed
PIXEL_PER_METER = (10.0 / 0.1)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 6


#2 : 상태의 정의
class IDLE:
    @staticmethod
    def enter(self,event):
        print('ENTER IDLE')
        self.dir = 0
        self.timer = 1000

    @staticmethod
    def exit(self, event):
        print('EXIT IDLE')

    @staticmethod
    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8



    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_composite_draw(int(self.frame) * 100, 360, 153, 180,'','', self.x, self.y,153,180)
        else:
            self.image.clip_draw(int(self.frame) * 100, 200, 153, 180,3.141592 / 2,'',180, self.x, self.y,153,180)


class RUN:
    def enter(self, event):
        print('ENTER RUN')
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1

    def exit(self, event):
        print('EXIT RUN')
        self.face_dir = self.dir


    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time)%8
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        self.x = clamp(25, self.x, 1600-25)

    def draw(self):
        if self.dir == -1:
            self.image.clip_composite_draw(int(self.frame) * 100, 360, 153, 180,'','', self.x, self.y,153,180)
        elif self.dir == 1:
            self.image.clip_composite_draw(int(self.frame)*100, 100, 100, 100,0,180, self.x, self.y,self.w,self.h)




#3. 상태 변환 구현

next_state = {
    IDLE:  {RU: RUN,  LU: RUN,  RD: RUN,  LD: RUN},
    RUN:   {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE},

}




class Bird:

    def __init__(self):
        self.x, self.y = 100, 70
        self.w, self.h= 150,180
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('bird_animation.png')
        self.timer = 100

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            try:
                self.cur_state = next_state[self.cur_state][event]
            except KeyError:
                print(f'ERROR: State {self.cur_state.__name__}    Event {event_name[event]}')
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)


