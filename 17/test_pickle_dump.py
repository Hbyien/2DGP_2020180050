import pickle

class NPC:
    def __init__(self,name,x,y):
        self.name, self.x, self.y= name,x,y
    def show(self):
        print(f'Name:{self.name}@({self.x},{self.y})')
yuri=NPC('Yuri',100,200)
print(yuri.__dict__)#모든 객체는 __dict__라는 내부 변수가 자동적으로 존재

yuri.name = 'tom'
yuri.x=100

yuri.__dict__.update({'name':'jeni','x':100,'y':100})