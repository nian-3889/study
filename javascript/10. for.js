//어떤 것을 반복적으로 시행할 때 쓰는 문법
//while은 11. while.js를 확인

//for문의 기본 구성은 아래와 같습니다.
document.write(`for([초기문];[조건문];[증감문])
                    실행문
                *변수명을 const로 할 경우, 에러가 나므로 주의`)

//예시
for(let i = 0; i < 10; i++) {
    console.log(i);
}

let x = 9
for (i = 1; i < x; i ++) {
    console.log(`${i} * ${x} = ${x * i}`)}


//이중 for문
document.write(`for ([초기값]; [조건문]; [증감문])
                    첫번째 for문 실행문 *생략 가능
                    for ([초기값]; [조건문]; [증감문]
                        두번째 for문 실행문`)

//예시
let num1 = prompt(Number(num1))
let num2 = prompt(Number(num2))

for (i = 1; i < num1; i++) {
    for (j = 1; j < num2; j++) {
        console.log(`${i} * ${j} = ${i * j}`)
    }
}



//for in문
document.write(`for(const key in 객체) {
                    반복문}`)

//예시
// const


//for of문