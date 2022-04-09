#range()
from unittest import result


print("1. range(x) : x-1까지")
print("2. range(x, y) : x부터 y-1까지")
print("3. range(x, y, z) : x부터 y-1까지, 증감은 z값")
print("range()로 할 경우 출력은 리스트로 나온다")

#for 반복문 쓰는법
print('''
for 숫자 변수 in 범위:
    코드
''')

#예시
for i in range(5):
    print(str(i) + " = 반복 변수")
print()

for i in range(5, 10):
    print(str(i) + " = 반복 변수")
print()

for i in range(0, 10, 3):
    print(str(i) + " = 반복 변수")
print()


#리스트와 범위 조합하기
#예시
arr = [273, 32, 103, 57, 52]
for element in arr:
    print(element)

for i in range(len(arr)):
    print(f"{i}번째 반복: {arr[i]}")


#반대로 반복하기
#예시
for i in range(4, 0-1, -1):
    print(f"현재 반복 변수 : {i}")

#응용
marks = [90, 25, 67, 45, 80]

number = 0

for mark in marks:
    number = number +1
    if mark >= 60:
        print(f"{number}번 학생은 합격입니다.")
    else:
        print(f"{number}번 학생은 불합격입니다.")


#for문과 continue
#continue : 일부 코드 건너뛰어 실행하는 문구
for i in range(20):
    if i % 2 == 0:
        continue
    print(i)

marks2 = [90, 25, 67, 45, 80]

number2 = 0
for mark2 in marks2:
    number2 = number2 + 1
    if mark2 < 60:
        continue
    print(f"{number2}번 학생 축하합니다. 합격입니다.")

    #for와 range()를 이용한 구구단

    for i in range(2, 10):
        for j in range(1, 10):
            print(i * j, end=" ")


#리스트 안에 for문을 포함하는 경우

a = [1, 2, 3, 4]
result = []

for num in a:
    result.append(num*3)
print(result)
