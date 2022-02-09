#print(str.__doc__)

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