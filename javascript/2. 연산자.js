//산술 연산자
//여기서 나오는 document.write()는 파이썬의 print()와 동일하다.


//덧셈 : 일반 사칙연산과 같음
let x = 1
let y = 2
let z = x + y
document.write(z)

//문자와 문자를 더할 수 있다.
document.write('My ' + 'Home')

//문자와 숫자를 더할 경우, 숫자를 문자화하여 한다.
document.write('1' + 1)

//뺄셈 : 일반 사칙연산과 같음.
//let은 재할당이 가능하므로 let 안쓰고 변수 = 할당값 으로 지정
x = 5
y = 2
z = x - y
document.write(z)

//곱셈 : 일반 사칙연산과 같음.
//단, 기호는 *
x = 4
y = 2
z = x * y
document.write(z)

//나눗셈 : 일반 사칙연산과 같음.
//단, 기호는 /
x = 6
y = 3
z = x / y
document.write(z)

//나머지 : 나눗셈의 나머지만 구하는 것.
//기호는 %
x = 3
y = 2
z = x % y
document.write(z)