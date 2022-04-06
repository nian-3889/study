#boolean : 참과 거짓만이 가지고 있는 유형.
#대충 비교 연산자와 함께 스위치를 만들 때 사용
##무조건 첫 자는 대문자로 작성할 것
print(True)
print(False)


#----------------

#비교 연산자
print(10 == 100) #같다
print(10 != 20) #다르다
print(190 > 200) #오른쪽이 크다
print(180 >= 200) #오른쪽이 크거나 같다
print(190 < 200) #왼쪽이 크다
print(190 <= 200) #왼쪽이 크거나 같다

#대충 범위도 구할 수 있음
x = 25
print(10 < x < 30)
print(40 < x < 60)

#---------------------

#not : 참과 거짓을 바꿀때 사용
a = 10
under_20 = a < 20
print("under_20:", under_20)
print("not under_20:", not under_20)

#and : A값과 B값. 즉, A 와 B가 둘다 참이어야 참.
b = 40
print(b == 40 and b <= 80)
print(b != 20 and b > 90)

#or : A 또는 B. 즉, A와 B 한쪽이 참이면 참
c = 20
print(c != 21 or c < 10)
print(c == 10 or c < 10)