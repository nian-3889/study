//비교연산자, <
//오른쪽이 더 크다.
let x = 5
let y = 6
console.log(x < y)
document.write(`${y}는 ${x}보다 큽니다.`)

//비교연산자, >
//왼쪽이 더 크다.
x = 7
y = 4
console.log(x > y)
document.write(`${x}는 ${y}보다 큽니다.`)

//비교연산자, >=
//왼쪽이 크거나 같다.
x = 5
y = 4
let z = 7
console.log(x >= y)
console.log(x >= z)
document.write(`${x}가 ${y}보다 크거나 같으므로 true를 출력합니다.`)
document.write(`${x}가 ${z}보다 크거나 같지 않으므로 false를 출력합니다.`)

//비교연산자, <=
//오른쪽이 크거나 같다.
x = 5
y = 4
z = 7
console.log(x <= y)
console.log(x <= z)
document.write(`${y}가 ${x}보다 크거나 같지 않으므로 false를 출력합니다.`)
document.write(`${z}가 ${x}보다 크거나 같으므로 true를 출력합니다.`)

//비교연산자, ==
//두 값이 같은지 비교한다.
//===와 차이점은 타입까지 판단하지 않는다.
x = 4
y = 3
z = "4"
console.log(x == y)
console.log(x == z)
document.write(`${x}와 ${y}는 다르므로 false를 출력합니다.`)
document.write(`${x}와 ${z}는 자료형이 달라도 값이 똑같기 때문에 true를 출력합니다.`)


//비교연산자, !=
//둘이 다를 때 의미
//==처럼 타입까지 판단하지 않는다.
x = 5
y = 4
z = "5"
console.log(x != y)
console.log(x != z)
document.write(`${x}와 ${y}는 서로 다르므로 true를 출력합니다.`)
document.write(`${x}와 ${z}는 자료형이 달라도 값이 같기 때문에 false를 출력합니다.`)


//비교연산자, ===
//==와 다른 경우 타입까지 따진다.
//같은지 다른지 따질 때 
x = 5
y = 5
z = "5"
console.log(x === y)
console.log(x === z)
document.write(`${x}와 ${y}는 데이터와 자료형이 모두 같으므로 true를 출력합니다.`)
document.write(`${x}와 ${z}는 데이터는 같지만 자료형이 다르므로 false를 출력합니다.`)


//비교연산, &&
//논리곱 연산자라 하며, and로 이해하면 된다.
//둘 다 참(혹은 거짓)일 때 참(혹은 거짓)을 반환한다.
console.log(true && true)
console.log(true && false)
console.log(false && false)
console.log(false && true)
document.write("&&는 둘 다 참일 때 참을 표시합니다.")
document.write("&&는 둘 중 하나라도 거짓이면 거짓을 표시합니다.")



//비교연산, || *shift + \
//논리합 연산자라 하며, or로 이해하면 된다.
//둘 중 하나라도 참이면 참을 반환한다.
console.log(true || true)
console.log(true || false)
console.log(false || true)
console.log(false || false)
document.write("||는 둘 중 하나만 참일 때 참을 표시합니다.")
document.write("|는 shift + \를 누르면 이용할 수 있습니다.")