//for문을 보실거면 10. for.js로
//do while은 준비중입니다.

//while문은 아래의 형태를 구성하고 있습니다.
document.write(`
while (조건문) {
    실행문
    기준변수 ++ *증감연산식
}
언젠가 조건문이 false가 되게끔 설정하면 됨.
만약 이를 빼먹을 경우, 무한루프에 빠짐.
무한루프에 빠질 때에는 컨트롤 + C로 강제종료 할 것
`)

//예시 (출처 : 스파르타코딩클럽)

let temperature = 20

while (temperature < 25) {
    console.log(`${temperature}도 정도면 적당한 온도입니다.`)
    temperature ++
}