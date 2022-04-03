//else if를 알면 switch를 배울 필요가 없다고 어느 유튜버가 그랬다.
//그러나 알면 편하기 때문에 적어둔다.
//default는 없어도 진행에 문제가 없음. case 문은 1개라도 있어야 됨.

//switch의 구성
document.write(`
switch의 구성은 다음과 같습니다.
switch(변수) {
    case 조건 1 :
        실행문
        break(혹은 continue);
    case 조건 :
        실행문
        break(혹은 continue);
    default:
        실행문
        break;
} `)

//예시 (구글링을 통해 가져옴)
//break문이 없으면 문법 오류가 생길 수 있음.
let x = 2 + 2
switch (x) {
    case 3:
        alert('비교하려는 값보다 작습니다.');
        break;
    case 4:
        alert('비교하려는 값과 일치합니다.');
        break
    case 5:
        alert('비교하려는 값보다 큽니다.')
    default:
        alert('어떤 값인지 파악이 되지 않습니다.')
}