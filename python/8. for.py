#range()
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