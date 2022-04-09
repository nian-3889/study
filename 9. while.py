#while의 구조
from re import T


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