from pico2d import*

#2.이벤트 정의
#RD ,LD,RU,LU = 0,1,2,3
RD, LD, RU, LU, TIMER = range(5)

#키입력을 단순화 시켜서 이벤트로 해석
key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT) : RD,
    (SDL_KEYDOWN, SDLK_LEFT) : LD,
    (SDL_KEYUP, SDLK_RIGHT) : RU,
    (SDL_KEYUP, SDLK_LEFT) : LU
}


#1. 상태정의
class IDLE: #객체생성이 아니라 그루핑 용
    def enter(self, event): #상태에 들어갈 때 행하는 액션
        print('Enter Idle')
        self.dir = 0
        self.timer = 1000
        pass
    def exit(self): #상태를 나올 때 행하는 액션, 고개들기
        print('Exit Idle')
        pass
    def do(self): #상태에 있을 때 지속적으로 행하는 행위, 숨쉬기
        self.frame = (self.frame +1) % 8
        self.timer -= 1
        if self.timer == 0:
            self.add_event(TIMER)


    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)

        pass

class RUN: #객체생성이 아니라 그루핑 용
    @staticmethod #객체용이 아니라 그룹용이라고 알려줌
    def enter(self, event):
        print('Enter Run')

        #방향을 결정해야 하는데, 뭘 근거로? 어떤 키가 눌렸기 때문에?
        # 키 이벤트 정보가 필요. enter에는 self 뿐만아니라 enter도 받아야함
        if event == RD:
            self.dir +=1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -=1
        elif event == LU:
            self.dir +=1
        pass
    @staticmethod
    def exit(self):
        print('Exit Run')
        self.face_dir = self.dir
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame +1 %8)
        #x좌표 변경,달리기
        self.x += self .dir
        self.x = clamp(0,self.x,800) #교수님이 만들어논 함수 범위지정
        pass

    @staticmethod
    def draw(self):
        print('DRAW RUN')
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)


class SLEEP:
    def enter(self,event):
        print('Enter SLEEP')
        self.frame = 0
        pass
    def exit(self): #상태를 나올 때 행하는 액션, 고개들기
        pass
    def do(self): #상태에 있을 때 지속적으로 행하는 행위, 숨쉬기
        self.frame = (self.frame +1) % 8
        pass
    def draw(self):
        if self.face_dir == -1: #왼쪽을 보고 있다.
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100, -3.141592/2,'', self.x+25, self.y-25,100,100)
        else: #오른쪽 눕기
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100,3.141592/2,'', self.x+25, self.y-25,100,100)





#3. 상태변환 기술
next_state = {
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, TIMER: SLEEP},
    RUN: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE},
    SLEEP: {RU: RUN, LU: RUN, RD: RUN, LD: RUN}
}




class Boy:


        # if event.type == SDL_KEYDOWN:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             boy.dir -= 1
        #         case pico2d.SDLK_RIGHT:
        #             boy.dir += 1
        #
        # elif event.type == SDL_KEYUP:
        #      match event.key:
        #          case pico2d.SDLK_LEFT:
        #             boy.dir += 1
        #             boy.face_dir = -1
        #          case pico2d.SDLK_RIGHT:
        #             boy.dir -= 1
        #             boy.face_dir = 1


    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')
        self.timer =100
        self.event_q = [] #이벤트 큐 초기화
        self.cur_state = IDLE
        self.cur_state.enter(self, None) #초기 상태의 entry 액션 수행

    def update(self):
        # self.frame = (self.frame + 1) % 8
        # self.x += self.dir * 1
        # self.x = clamp(0, self.x, 800)
        self.cur_state.do(self) #현재상태의 do 액션수god
        #이벤트 확인해서, 이벤트가 있으면 이벤트 변환처리
        if self.event_q: #큐에 이벤트가 있으면 이벤트가 발생했으면
            event = self.event_q.pop()
            self.cur_state.exit(self) #현재상태를 나가고
            self.cur_state = next_state[self.cur_state][event] #다음 상태를 구한다
            self.cur_state.enter(self,event) #다음 상태의 entry 액션 수행


    def draw(self):
        self.cur_state.draw(self)

    def add_event(self, event):
        self.event_q.insert(0, event)

    def handle_event(self, event):
        if(event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.event_q.insert(0, key_event)
            self.add_event(TIMER)



