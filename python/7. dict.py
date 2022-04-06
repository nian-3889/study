#딕셔너리(dictionary) : 키를 기반으로 값을 저장하는 것
print("""사용법:
변수 : {
    키 : 값,
    키 : 값,
    ...
    키 : 값,
}
""")
dict_a = {
    "name": "어벤져스 엔드게임",
    "type": "히어로 무비",
}
print(dict_a)

#딕셔너리 요소에 접근하기.
print(dict_a["name"])
print(dict_a["type"])

##예시 --------------------------

#딕셔너리 선언
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

#출력
print("name: {0}".format(dictionary["name"]))
print("type: {0}".format(dictionary["type"]))
print("ingredient: {0}".format(dictionary["ingredient"]))
print("origin: {0}".format(dictionary["origin"]))

#값을 변경
dictionary["name"] = "8D 건조 망고"
print("name: {0}".format(dictionary["name"]))


#---------------------------------

## 딕셔너리 값 추가(제거)하기

#추가하기
dictionary["price"] = 5000
print(dictionary)

#제거하기 *값까지 지워버림
del dictionary["ingredient"]
print(dictionary)

##예시

#변수 만들기
dict_b = {}
print(f"요소 추가 이전 : {dict_b}")

#값 추가하기
dict_b["name"] = "이름"
dict_b["head"] = "머리"
dict_b["body"] = "몸"
print(dict_b)

#값 제거하기 
del dict_b["body"]

print(dict_b)