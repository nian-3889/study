#기본적인 자료형은 문자열, 숫자, boolean이 있음

#변수 만드는 방법
#변수 이름 = 변수값
x = 3
y = '2'
z = '알파벳'

#출력방법
#1. print(변수 이름)
print(x)
print(y)
print(z)

#2. print(숫자)
print(1)
print(20)
print(2e3)

#3. print('문자')
print('안녕하세요')
#따옴표를 붙여 쓸땐 이스케이프 문자(\") 등을 씀
print("\"안녕하세요\"라고 말했습니다.")
#이스케이프 문자가 싫으면 '''문장'''("""문장""").
print("""'안녕하세요.'
라고 말했습니다.
""")

#문자와 문자를 연결할 수 있음
#단, 문자와 숫자는 더할 수 없음.
print(y + z)

#문자열을 반복할 수 있음
print('안녕하세요'*3)

#문자열 중 일부만 선택할 수 있음
print('안녕하세요'[0])
print('안녕하세요'[1])
print('안녕하세요'[2])
print('안녕하세요'[3])
print('안녕하세요'[4])

#물론 거꾸로도 가능
print('안녕하세요'[-1])
print('안녕하세요'[-2])
print('안녕하세요'[-3])
print('안녕하세요'[-4])
print('안녕하세요'[-5])

#범위 지정도 가능
print('안녕하세요'[:2])
print(z[:2])

#문자열의 길이도 구할 수 있음
#자바스크립트는 변수명.length
print(len(z))


#사칙연산
a = 10
b = 5
print(a + b) #덧셈
print(a - b) #뺄셈
print(a * b) #곱셈
print(a ** b) #제곱
print(a / b) #나눗셈
print(a % b) #나머지

#복합대입연산자
number = 100
number += 10 #덧셈 후 대입
number -= 20 #뺄셈 후 대입
number *= 30 #곱셈 후 대입
number /= 40 #나눈 후 대입
number %= 50 #숫자의 나머지를 구한 후 대입
number **= 2 #숫자를 제곱 후 대입
print(number) #출력


#input : 사용자 입력
input('인사말을 입력하세요')
print(input())