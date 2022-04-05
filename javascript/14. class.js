//구성방법
document.write(`
class MyClass{
    constructor() {}
    method1() {}
    ...
}
`)

//예시
class noteBook {
    constructor(name, price, company) {
        this.name = name
        this.price = price
        this.company = company
    }
}
const noteBook1 = new noteBook('Mackbook', 2000000, 'Apple')

//가져오기
console.log(noteBook1)
console.log(noteBook1.name)
console.log(noteBook1.price)
console.log(noteBook1.company)


//메서드 : 클래스 내부에 정의된 서브 함수. 데이터와 멤버 변수에 대한 접근 권한을 갖는다.

class Product {
    constructor(name, price) {
        this.name = name
        this.price = price
    }

    printInfo() {
        console.log(`상품명: ${this.name}, 가격: ${this.price}원`)
    }
}

//객체 생성 및 메서드 호출
const notebook =  new Product('Mackbook', 2000000)
notebook.printInfo()


//객체 리터럴

const computer = {
    name: 'Apple Mackbook',
    price: 20000,
    printInfo: function() {
        console.log(`상품명: ${this.name}, 가격: ${this.price}원`)
    }
}

computer.printInfo()


//학원과제
class cloth {
    constructor(color, size, price) {
        this.color = color
        this.size = size
        this.price = price
    }

    printInfo() {
        console.log(`color : ${this.color}, size : ${this.size}, price : ${this.price}`)
    }
}

const coat = new cloth('navy', 'L', 200000)
const panth = new cloth('black', 'M', 10000)

coat.printInfo()
panth.printInfo()