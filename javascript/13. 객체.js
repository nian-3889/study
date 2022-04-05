//객채란 실생활에서 우리사 인식할 수 있는 사물.
//자바스크리트에서 객체는 이름과 값으로 구성된 프로퍼티의 집합.

//생성법
let user_name = new Object(); //객체 생성자 문법
let name1 = {} //객체 리터럴 문법 *이 방법 많이 씀

//객체 리터럴 작성법
// : 를 기점으로 왼쪽에 이름, 오른쪽에 값이 있음
let cat = "나비"
let kitty = {
    name: "나비",
    family: "코리안 숏 헤어",
    age: 1,
    weight: 0.1
}
console.log(cat)
console.log(kitty.name)

//유의사항 : const 객체 값은 수정할 수 있다.

//대괄호 표기법 : 꼭 ""로 감싸야함
//정의
let user = {};

//set
user["like birds"] = true;

//get
console.log(user["like birds"]);

//delete
delete user["like birds"];



//in 연산자로 존재여부 확인하기.
//사용법 : key in object
//예시
let user_in = {};
console.log(user_in.noSuchProperty === undefined);
//*.noSuchProperty : 프로퍼티가 존재하지 않는지 확인하는 메서드

//for in 반목문
//사용법
document.write(`
    for (key in object) {
        실행문
    }
`)

//예시
let user_forIn = {
    name: "John",
    age: 30,
    isAdmin: true,
}

for (let key in user) {
    console.log(key);
    console.log(user[key]);
}