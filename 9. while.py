#while의 구조
#유의사항 : 무한루프에 빠질 경우 Ctrl + c로 빠져나가자.

print('''
while 조건문:
    수행할 문장
    수행할 문장
    ...
    조건 증감식
''')

#예제
tree_hit = 0

while tree_hit < 10:
    tree_hit = tree_hit + 1
    print(f"나무를 {tree_hit}번 찍었습니다.")
    if tree_hit == 10:
        print("나무 넘어갑니다.")

coffee = 10
while True:
    money = int(input("돈을 넣어주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee -1
    elif money > 300:
        print(f"거스름돈 {money -300}원을 주고 커피를 줍니다.")
        coffee = coffee -1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print(f"남은 커피의 양은 {coffee}개 입니다.")
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
