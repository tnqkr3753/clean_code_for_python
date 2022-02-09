 > This document is for clean code in Python
 >  > referenced in https://doorbw.tistory.com/234 

# 상속(*Inheritance*)
클래스에서 상속이란 물려주는 클래스(Parent Class, Super Class)의 내용들(속성과 메소드)을 물려받는 클래스(Child class, Sub Class)가 가지게 되는 것이다.

객체 지향적 프로그래밍에서 중요하고, 자주 사용하는 개념이다.

하지만 상속을 사용하면 부모클래스와 자식클래스간에 강력한 결합력이 발생하게 된다.

따라서 좋은 코드와 유지보수를 생각할 때 좋은 경우와 그렇지 않은 경우를 잘 선별해가며 활용할 수 있어야 한다.

새로 정의하고자 하는 자식클래스가 부모클래스의 기능을 그대로 물려받으면서 특정 기능을 바꾸거나, 추가적인 기능이 필요할 때 **상속**을 활용화면 될 것 같다.

# 상속 사용법
Python에선 다음과 같이 상속을 사용한다.
```python
class ParentClass:
    ~~

class ChildClass(ParentClass):
    ~~
```

이 때 자식클래스에서는 부모클래스의 속성과 메소드는 기재하지 않아도 기본적으로 포함된다.

```python
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
```
결과
```
동물이 4개의 다리로 움직입니다.
강아지가 밥을 먹습니다.
```

하지만 올바르지 않은 상속의 경우도 있다.
```python
import collections
from datetime import datetime

class TransactionalPolicy(collections.UserDict):
    '''잘못된 상속'''

    def change_in_policy(self, customer_id, **new_policy_data):
        self[customer_id].update(**new_policy_data)

def main():
    policy = TransactionalPolicy({
        "client1":{
            "fee": 1000.0,
            "expiration_date": datetime(2022,2,9),
        }
    })
    print(policy['client1'])
    policy.change_in_policy("client1",expiration_date=datetime(2022,2,15))
    print(policy['client1'])
    print()
    print(dir(policy))

if __name__=='__main__':
    main()
```
결과
```
{'fee': 1000.0, 'expiration_date': datetime.datetime(2022, 2, 9, 0, 0)}
{'fee': 1000.0, 'expiration_date': datetime.datetime(2022, 2, 15, 0, 0)}

['_MutableMapping__marker', '__abstractmethods__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__setitem__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '__weakref__', '_abc_impl', 'change_in_policy', 'clear', 'copy', 'data', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
```
policy객체를 볼 때 구현해놓은 change_in_policy 라는 함수 이외에도 pop이나 popitem, setdefault와 같이 dict객체의 함수를 가지고 있다.

해당 함수들은 public 메서드이기 때문에 의도하지 않은 사용이 있을 수도 있다.

이러한 경우엔 해당 자식클래스가 dict자료형을 상속받는 것은 올바르지 않다고 생각한다.

# 컴포지션(*Composition*)
