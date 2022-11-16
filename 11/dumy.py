# # class Star:#클래스의 역활 함수 또는 변수를 묶는다.
# #     x = 100
# #     def change():
# #         x= 200
# #         print('x is',x)
# #
# # print(Star.x)# Star 클래스 x는 클래스 변수
# # Star.change() #클래스 함수 호출 #클래스의 또다른 역활 함수나 변수를 묶음 이때 클래스는 그룹의 이름이 됨
# #
# # # star=Star() # 비혹 객체생성용이 아니더라도 객체는 만들어진다.
# # # star.change()
#
#
# class Player:
#     def __init__(self):
#         self.x = 100
#     def where(self):
#         print(self.x)
#
# player = Player()
# player.where()
#
# #Player.where() #클래스의 함수 호출
# Player.where(player) #self가 들어간것
# player.where() #객체 함수호출 Player.where(player)랑 똑같음


table = {
    'SLEEP' : {'HIT' : 'WAKE'},
    'WAKE' : {'TIME10' : 'SLEEP'}
}

cur_state = 'SLEEP'
print(table[cur_state]['HIT'])
print(table['WAKE']['TIME10'])