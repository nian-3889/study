//변수(Variable) : 일종의 데이터 보관함.

//선언방법
var age
let country

//할당방법
//const는 선언과 동시에 할당하지 않으면 에러가 생김.
const user = 'nian'

//재할당 방법
age = 10 
country = 'korea'

//선언과 동시에 할당도 가능
var apple = 'red'
let orange = 'orange'
const lemon = 'lemon'

//var, let, const의 차이점

//var : 선언은 전역 혹은 함수 범위.
//let과 const : 선언은 블록범위.

//var와 let은 재할당이 가능하지만, const는 안 된다
//var는 변수 재선언이 가능하지만, let과 const는 안 된다.

//var는 호이스팅이 가능하다. let과 const는 안 된다.
//사실 let도 가능하지만 범주가 아예 다르다.