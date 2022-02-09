 > This document is for clean code in Python
 >  > referenced in https://doorbw.tistory.com/231

 # *Docstring*
## *Docstring*은 코드에 포함된 문서

**코드를 코드 밖 특정 문서에 정리하는 것이 아닌 코드 내부에 문서화를 시키는 것**

특히나 *Python*같은 동적 타입의 언어는 코드 내부에 문서를 포함시키는 *docstring*이 매우 유용

파이썬에서 *docstring*은 함수나 클래스 모듈 등에 정의할 수 있으며 작성한 내용을 확인하기 위해서 해당 객체의 **\_\_doc__** 속성을 이용하면 된다.

```python
>>> print(str.__doc__)
```
결과
```
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.
```

작성한 내용과 같이 *str*객체의 *docstring*을 확인하니 str에 대한 상세한 설명과 사용방법 등이 출력된다.

# *Docstring* 사용하기
*Python*에서 *Docstring* 만들어서 사용하기
```python
class DocstringExampleClass():
    '''
    DocstringExampleClass
    Docstring을 이해하고 활용하기 위해 생성한 클래스
    해당 부분엔 클래스에 대한 설명을 기입한다.
    '''

    def docstrig_example_function():
        '''
        docstring_example_function
        Docstring을 이해하고 활용하기 위해 생성한 클래스 내부 함수
        해당 부분엔 함수에 대한 설명을 기입한다.
        print a fixed massage then
        Return 0 always
        '''
        print('docstring_example_function')
        return 0

def main():
    print('클래스 생성')
    dExmp = DocstringExampleClass()
    print('클래스 Docstring 확인')
    print(dExmp.__doc__)
    print()
    print('함수 Docstring 확인')
    print(dExmp.docstrig_example_function.__doc__)

if __name__ == '__main__':
    main()
```
결과
```
클래스 생성
클래스 Docstring 확인

    DocstringExampleClass
    Docstring을 이해하고 활용하기 위해 생성한 클래스
    해당 부분엔 클래스에 대한 설명을 기입한다.


함수 Docstring 확인

        docstring_example_function
        Docstring을 이해하고 활용하기 위해 생성한 클래스 내부 함수
        해당 부분엔 함수에 대한 설명을 기입한다.
        print a fixed massage then
        Return 0 always
```
위와 같이 간단한 클래스 하나와 함수 하나를 만들어 *Docstring*을 기입하였다.

***Docstring*은 코드와 같이 클래스, 함수 선언 바로 아래에 따옴표 3개를 사용한 str으로 정의할 수 있다.**

# 마무리
*Docstring*을 만드는 것은 같이 일하는 사람들의 이해를 도울 뿐 아니라 내가 사용하고 관리하기 더욱 편리해진다.

만들고 사용하는 것도 매우 간편하기 떄문에 꼭 사용하고, 반드시 수정사항이 있을 때 잠깐의 시간을 내어 *Docstring*을 수정한다면 좋은 코드로서 유지보수에 많은 이점이 올 것이다.