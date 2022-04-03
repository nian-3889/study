//이거는 모두 예시입니다.

//복합대입연산자, +=
let num = 10
document.write(`num += 10은 num = num + 10을 뜻하며, 그 값은 ${num += 10}이 됩니다.`)

//복합대입연산자, -=
num = 10
document.write(`num -= 10은 num = num - 10을 뜻하며, 그 값은 ${num -= 10}이 됩니다.`)

//복합대입연산자, *=
num = 10
document.write(`num *= 5은 num = num * 5을 뜻하며, 그 값은 ${num *= 5}이 됩니다.`)

//복합대입연산자, /=
num = 10
document.write(`num /= 5은 num = num / 5을 뜻하며, 그 값은 ${num /= 5}이 됩니다.`)

//복합대입연산자, %=
num = 10
document.write(`num %= 5은 num = num % 5을 뜻하며, 그 값은 ${num %= 5}이 됩니다.`)

//증감연산자, ++변수(--변수)
num = 10
document.write('증감연산자인 ++변수는 해당 문장을 실행하기 전에 값을 더합니다.')
document.write(num)
document.write(++num)
document.write(++num)
document.write(`++변수를 두 번 실행한 후의 num 값은 ${num}입니다.`)


//증감연산자, 변수++(변수--)
num = 10
document.write('증감연산자인 변수++는 해당 문장을 실행한 후에 값을 더합니다.')
document.write(num)
document.write(num++)
document.write(num++)
document.write(`변수++를 두 번 실행한 후의 num 값은 ${num}입니다.`)