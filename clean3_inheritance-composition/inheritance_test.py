class Animal:
    '''Animal ParentClass

    Animal 부모클래스
    동물 클래스들은 해당 클래스를 상속받는다.

    '''
    leg : int

    def __init__(self, leg:int):
        self.leg = leg

    def move(self):
        print(f'동물이 {self.leg}개의 다리로 움직입니다.')

    def eat(self):
        pass

class Dog(Animal):
    '''Dog ChildClass

    Animal클래스를 상속받는 Dog클래스
    개의 다리 수를 설정하고, eat함수를 재정의한다.

    '''

    def __init__(self):
        super().__init__(4)

    def eat(self):
        print('개가 밥을 먹습니다.')

def main():
    d = Dog()
    d.move()
    d.eat()

if __name__=='__main__':
    main()