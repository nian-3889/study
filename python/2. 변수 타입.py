#문자형(string)
#자세한 건 1. 변수와 문자열.py 참조
name = 'Nian'
print(type(name))

#숫자형. int와 float
x = 10 #int는 정수
y = 20.147 #float는 실수
z = 0.52273e2 #지수표현식. float에 해당
print(type(x))
print(type(y))
print(type(z))

#boolean. true와 false로 나뉨
a = True
b = False
print(type(a))
print(type(b))

#input()함수로 받은 데이터의 자료형
print(type(input())) #무조건 문자형(str)으로 나옴

#input()함수의 데이터 변환하고 싶다면?
number = input("숫자를 입력해주세요")
print(int(number))
print(float(number)) #실수를 정수로 변환할땐 에러나니 주의

#자바스크립트와 다르게 변환할 수 없는 자료형이 나올 땐 에러가 난다
#자바스크립트는 NaN이 있는데... 흐규규규...