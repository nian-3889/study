//조건문 : 특정 조건 만족시 실행하는 명령어의 집합
//자바스크립트는 if, switch, 삼항연산자가 이에 해당한다

//문법
console.log(`
if문은 다음과 같은 형태로 씁니다.
if(조건식) {
    실행 식1
} else if(조건식) {
    실행 식2
} ... {
    실행식 ...
} else {
    실행식
}`)

//예시
let x = 60

if (x >= 100) {
    document.write("x의 값은 100이 넘습니다.")
} else {
    document.write("x의 값은 100을 넘지 않습니다.")
}

//무조건 false로 취급하는 값이 있다.
console.log(`
아래의 조건은 거짓으로 취급합니다.
- false
- undefined
- null
- 0
- NaN
- ""
*외우세요.
`)