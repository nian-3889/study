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


#함수 안에서 선언한 변수의 효력은 함수 내에서만 미친다.
a = 1
def vartest(a):
    a = a + 1

vartest(a)
print(a)

#함수 안에서 함수 밖의 변수를 변경하는 법
##1. return 사용하기
b = 1
def vartest_b(b):
    b = b + 1
    return b

#b가 vartest_b 함수의 결괏값으로 바뀜.
b = vartest_b(b)
print(b)

#2. global 명령어 사용하기

c = 1
def vartest_c():
    global c
    c = c + 1

vartest_c()
print(c)


#lambda
#def와 동일한 기능을 함.
#간결하게 만들 때, def를 사용할 수 없을 때 사용

add = lambda a, b : a + b
result_add = add(3, 4)

print(result_add)