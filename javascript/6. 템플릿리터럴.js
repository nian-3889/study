//템플릿 리터럴(Template Literal) : ES6부터 도입된 문자열 표기법.
//따옴표('' 혹은 "")가 아닌 백틱(``)으로 표현

//사용법 1. 줄바꿈
//기존에는 \n을 써야만 했다.
let write = `
안녕히 계세요 여러분!
전 이 세상의 모든 굴레와 속박을 벗어 던지고 제 행복을 찾아 떠납니다!
여러분도 행복하세요~~!
`
console.log(write)

//사용법 2. 표현식 삽입
//파이썬의 f-string 표현법과 비슷함
let name = '사과'
let price = 100
console.log(`${name} 한 개 값은 ${price}입니다.`)

//이런 경우도 가능함
let x = 5
let y = 2
console.log(`${x} * ${y} = ${x * y}`)