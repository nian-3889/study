#함수란 : 계속 재사용할 수 있게 만들어 놓은 로직
#함수 구조
from unittest import result


print('''
def 함수명(매개변수):
    수행할문장
    return 결과값
''')

#예시

#일반적인 함수
def add(a, b): #a, b는 매개변수(parameter)
    return a + b
c = add(3, 4) #3, 4는 인수(arguments)
print(c)

#입력값이 없는 함수
def func1():
    print('BlockDMask')
func1()

#결과값이 없는 함수
def add_two(a, b):
    print(f"{a}, {b}의 합은 {a+b}이다")
add_two(3, 4)

#참조 : return값이 없기 때문에 결과값이 None로 출력된다.
d = add_two(3, 4)
print(d)


#예제 : 구구단
#<for문으로 할 경우>
for i in range(1, 10):
    print(f'{2} * {i} = {2 * i}')

#<함수를 할 경우>
def gugudan(num):
    for i in range(1, 10):
        print(f'{num} x {i} = {num * i}')

gugudan(2)


#입력값이 몇개가 될지 모를땐 어찌할까?
# def 함수이름 (*매개변수):
#     수행할 문장
#     ...

#예시
def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

result = add_mul('add', 1,2,3,4,5)
print(result)

result_mul = add_mul('mul', 1, 2, 3, 4, 5)
print(result_mul)