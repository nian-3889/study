//MDN에서 함수란 "작업을 수행하거나 값을 계산하는 문장 집합 같은 자바스크립트 절차"

//함수를 정의(선언) 하려면 아래와 같은 키워드로 구성해야 함
document.write(`
    function 함수명(매개변수){
        실행문
    }`)

//예시
function square(number) {
    return number * number
}
square(4)

//아래와 같은 형태로도 함수가 정의가 가능함.
//이 방법은 익명 함수 표현이라고 함.
//변수 할당이 되지 않았으므로 변수명이 할당된 이후에만 실행이 가능하다.
document.write(`
    let(const) 변수명 = function () {
        실행문
    }
`)

//함수 표현식.
//익명 함수 표현식과 비슷함
document.write(`
    let(const) 변수명 = function 함수명() {
        실행문
    }
`)
//예시
let squareTwo = function(numberTwo) {
    return numberTwo * numberTwo
}
let x = squareTwo(4)

//화살표함수
document.write(`
    let(const) 변수명 = () => {
        실행문
    }
`)
//예시

let squereThree = (numberThree) => {
    return numberThree * numberThree
}
let y = squereThree(4)