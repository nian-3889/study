#리스트(list) : 목록
print('리스트의 사용법 : 변수명 = [요소, 요소, 요소]')

#리스트를 선택하는 법
#참조 : 컴퓨터는 0부터 숫자를 센다
list_a = [273, 32, 103, "문자열", True, False, [4, 5, 6]]
print(list_a[0])
print(list_a[1])
print(list_a[1:3])
print(list_a[::-1]) ##역순으로 출력

print(list_a[3])
print(list_a[3][0]) #이중으로 사용할 수 있음

print(list_a[-1]) #리스트 안에 리스트를 넣을 수 있음
print(list_a[-1][1]) #첫번째 : 리스트의 마지막 + 두번째 : 첫번째 리스트의 두번째


#리스트 연산자와 같이 활용하기--------------------

#리스트 선언
list_b = [1, 2, 3]
list_c = [4, 5, 6]

#출력
print("# 리스트")
print(f"list_b = {list_b}")
print(f"list_c = {list_c}")

#기본 연산자
print("#리스트 기본 연산자")
print(f"list_b + list_c = {list_b + list_c}")
print(f"list_b * 3 = {list_b * 3}")

#함수
print("#길이 구하기")
print(f"len(list_b) = {len(list_b)}")

#요소 추가하기 : 맨 끝에 집어넣기
print("list_c=[4, 5, 6] 에 요소 추가하기")
list_c.append(7)
list_c.append(8)
print(list_c)

#요소 추가하기 : 중간에 추가하기
#사용법 : 리스트명.insert(넣을 위치, 요소)
list_c.insert(0, 3)
print(list_c)

#요소 제거하기 : del
del list_c[0]
print(list_c)

#요소 제거하기 : pop
#위치값을 주지 않으면 맨 마지막 요소를 삭제
list_c.pop(1)
list_c.pop()
print(list_c)