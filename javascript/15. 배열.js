//배열이란. 같은 타입의 데이터들을 하나의 변수에 할당하여 관리하기 위해 사용하는 데이터 타입

//배열 선언
const arr1 = new Array(1, 2, 3, 4, 5)
const arr2 = [1, 2, 3, 4, 5] //배열을 바로 만드는 방법
console.log(arr2)

//배열의 값은 인덱스를 통해서 접근한다.
//컴퓨터는 0부터 숫자를 센다
const rainbowColors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

console.log(rainbowColors[0])
console.log(rainbowColors[1])
console.log(rainbowColors[2])
console.log(rainbowColors[3])
console.log(rainbowColors[4])
console.log(rainbowColors[5])
console.log(rainbowColors[6])

//배열의 길이 : length라는 속성을 사용
console.log(rainbowColors.length)

//마지막 요소를 찾을 땐 이렇게 하면 됨
console.log(rainbowColors.length -1)

//요소 추가 : .push
rainbowColors.push('ultraviolet')
console.log(rainbowColors)

//요소 삭제 : .pop
rainbowColors.pop()
console.log(rainbowColors)


//객체 + for문
// for (let i = 0; i < rainbowColors.length; i++) {
//     console.log(rainbowColors[i])
// }

//간단하게 아래와 같이 사용 가능
for (const color of rainbowColors) {
    console.log(color)
}


//또 다른 예시

const priceList = [1000, 2000, 5000, 7000, 10000, 9000, 3000, 15000, 20000, 17000]
let sum = 0

for (const price of priceList) {
    sum += price
}

const avg = sum / priceList.length
console.log(`합계: ${sum}, 평균: ${avg}`)