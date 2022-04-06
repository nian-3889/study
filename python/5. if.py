#if문의 구성
print("""
if (조건문):
    (실행문)
elif (조건문):
    (실행문)
else:
    (실행문)
""")

#그래서 이 예제를
number = int(input())
if number % 2 == 0:
    print("짝수입니다")
if number % 2 == 1:
    print("홀수입니다")

##아래의 문장처럼 만들 수 있음
user_num = int(input())
if user_num % 2 == 0:
    print("짝수입니다")
else:
    print("홀수입니다")


#elif를 쓰는 예제--------------

#날짜/시간과 관련 기능 가져오기
from calendar import month
import datetime

now = datetime.datetime.now()
month = now.month

if 3 <= month <= 5:
    print("현재 봄입니다")
elif 6 <= month <= 8:
    print("현재는 여름입니다.")
elif 9 <= month <= 11:
    print("현재는 가을입니다.")
else:
    print("현재는 겨울입니다.")