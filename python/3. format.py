# '%s' & '문자열'
from ensurepip import version


name = 'maria'
print('I am %s.' % name)

#format 메서드
print('Hello, {0}'.format('World!'))
print('Hello, {0}'.format(100))

#f-string *파이썬 ver 3.6부터 사용 가능
language = 'Python'
version = 3.6
print(f'Hello, {language} {version}')

#------------------

#참고 : 그외 기능
#upper()
a = 'hello world'
print(a.upper())

#lower()
b = 'HELLO WORLD'
print(b.lower())

#문자열 구성 파악하는 함수, is####()
#참이면 True, 거짓이면 False를 출력
##문자열이 알파벳 또는 숫자로만 구성되어있는가
print("TrainA10".isalnum())

##문자열이 알파벳으로만 구성이 되었는가
print("10".isalpha())

##문자열이 식별자로 사용할 수 있는가
print("a".isidentifier())

##문자열이 숫자 형태인가.
a = '41'
print(a.isdigit())

##문자열이 정수 형태인가.
b = '42.16'
print(b.isdecimal())

##문자열이 공백으로 구성되었는가
c = "Love"
print(c.isspace())

##문자열이 소문자로만 구성이 되어있는가
d = 'lobo'
print(d.islower())

##문자열이 대문자로만 구성이 되어 있는가
print(d.isupper())


#--------------------

#문자열 찾기
#find() : 왼쪽부터 찾아서 처음 등장하는 위치를 찾습니다.
#rfind() : 오른쪽부터 찾아서 처음 등장하는 위치를 찾습니다.

hi = "안녕안녕하세요"
print(hi.find("안녕"))
print(hi.rfind("안녕"))

#문자열 in 연산자
##문자열이 연산자 안에 있는지 찾는 경우
print("안녕" in "안녕하세요")
print("잘자" in "안녕하세요")


#------------------

#특정 문자로 자를 때 : split()
##출력 시 리스트로 나옴
f = "10 20 30 40 50"
print(f.split(" "))