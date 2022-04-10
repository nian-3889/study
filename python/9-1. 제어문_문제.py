#문제 출처 : https://wikidocs.net/42527

#문1 : 다음의 코드 결괏값은 무엇인가
a = "Life is too short, you need python"

if "wife" in a:
    #wife란 단어가 a 변수에 없어 통과
    print("wife")
elif "python" in a and "you" not in a:
    #python도 있고 you도 있다. 조건문에는 not in으로 되어있어 통과
    print("python")
elif "shirt" not in a:
    #shirt는 없기 때문에 참이다. 출력
    print("shirt")
elif "need" in a:
    #need가 있으나, shirt가 먼저 참이기 때문에 출력되지 않는다.
    print("need")
else:
    print("none")

#문2
from unittest import result

result =0
i = 1
while i < 1000:
    #3의 배수일 때만 합산
    if i % 3 == 0:
        result += i
    i += 1

print(result)


#문 3
start_num = 1
finish_num = int(input("숫자를 입력해주세요."))

while start_num < finish_num + 1:
    print(start_num * '*')
    start_num += 1

#문4
for i in range(1, 100):
    print(i)

#문5
class_a = [70, 60, 55, 75, 95, 90, 80, 85, 100]
total = 0

#클래스로 바로 더하면 오류나므로 별도의 변수에 대입한 후에 더해야 함
for score in class_a:
    total += score

average = total / len(class_a)
print(average)


