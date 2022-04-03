//물음표 연산자, 조건부 연산자, 혹은 삼항연산자라 불림
//문법은 아래와 같음
document.write('let 변수명 = (조건문) ? 참 : 거짓')

//예시
//연산자 우선순위 규칙에 의거 age > 18이 먼저 실행됨.
//따라서 조건문을 괄호로 감쌀 필요가 없음.
let okayAge = age > 18 ? "술을 마실 수 있습니다" : "아직 어려요."

//다중
//출처 : ko.javascript.info
let age = prompt('나이를 입력해주세요');

let message = (age < 3) ? '아가야 안녕?' :
    (age < 18) ? '안녕!' :
    (age < 100) ? '환영합니다!' :
    '나이가 아주 많으시거나, 나이가 아닌 값을 입력 하셨군요!';

alert(message);

//이걸 if로 환산하면 아래와 같습니다.
if (age < 3) {
    message = '아가야 안녕?'
} else if (age < 18) {
    message = '안녕!'
} else if (age < 100) {
    message = '환영합니다!'
} else {
    message = '나이가 아주 많으시거나, 나이가 아닌 값을 입력 하셨군요!'
}

//이걸 switch문으로 환산하면 아래와 같습니다.
switch(message) {
    case age < 3:
        alert('아가야 안녕?')
        break
    case age < 18:
        alert('안녕!')
        break
    case age < 100:
        alert('환영합니다!')
        break
    default:
        alert('나이가 아주 많으시거나, 나이가 아닌 값을 입력 하셨군요!')
}
alert(message)