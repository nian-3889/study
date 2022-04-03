//string : 문자열
//문자열은 따옴표('' 혹은 "")로 감싸야 함
let hi = '안녕하세요'
document.write(typeof(hi))

//Number : 숫자
//자바스크립트는 큰 숫자를 저장하는 BigInt라는 자료형을 지원함.
//그 수가 크거나 작은 경우 지수(e)표현으로 바꿀 수 있음.
//사칙연산은 연산자.js에서 확인요망
let num = 1
document.write(typeof(num))

//NaN : Not a Number
//자바스크립트에서 숫자가 아닌 값을 출력할 때 나오는 타입.
//숫자를 구분하기 위해 쓰는 변수는 isNaN(값)을 사용하면 된다.
let x = 4
let y = '4'
document.write(isNaN(x))
document.write(isNaN(y))

//boolean : 불리언 혹은 불 자료형. 쉽게 말하자면 참 거짓만 있는 형태.
//true(참)와 false(거짓)로 구성.
let eat = true
let sleep = false
document.write(typeof(eat))
document.write(typeof(sleep))