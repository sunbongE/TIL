// 언어가 많이 유연해서 비 상식적인 코드를 실행했는데 use strict 선언하면 이를 방지해준다.
// added ECMAScript 5
// 성능개선을 기대할 수 있다.
'use strict';
let globalName = 'global name!';
{ // 여기 안에 값은 글로벌 함수로 접근 가능
    let name = 'ellie';
    console.log(name);
    name = 'hello';
    console.log(name);
}
console.log(name)
console.log(globalName)

// var 사용하지마!
// var 블럭 스콥을 무시해서 사용안하는게 나음
// var hoisting / 호이스팅이란?
// 어디에 선언했는지 상관없이 항상 가장 위로 선언을 끌어올리는 것

// constans  : 한번 선언하면 절대 변경이 안된다.

const char = 'c';
const brendan = 'brendan';
const greeting = 'hello' + brendan;

console.log(`value: ${greeting}, type:${typeof greeting}`);
const helloBob = `hi ${brendan}!`; // template literals (string)
console.log(`value: ${helloBob}, type: ${typeof helloBob}`)

// boolean
const canRead = true;
const test = 3<1; //false
console.log(`value: ${canRead}, type: ${typeof canRead}`);
console.log(`value: ${test}, type: ${typeof test}`);
///null
let nothing = null;
console.log(`value: ${nothing}, type: ${typeof nothing}`);

// nudefined
let x;
console.log(`value: ${x}, type: ${typeof x}`);

// symbol, create unique identifiers for objects
//고유한 식별자가 필요할 때 주로 사용
const symbol1 = Symbol('id');
const symbol2 = Symbol('id');
console.log(symbol1 === symbol2); // False

const gsymbol1 = Symbol.for('id');
const gsymbol2 = Symbol.for('id');
console.log(gsymbol1 === gsymbol2); // True
console.log(`value: ${symbol1.description}, type: ${typeof symbol1}`);
/// Dynamic typing
let text = 'hello';
console.log(text.charAt(0)); // h 인덱싱한거임
console.log(`value: ${text}, type: ${typeof text}`);
text = 1; //value: 1, type: number
console.log(`value: ${text}, type: ${typeof text}`);
text='7' + 5; // value: 75, type: string
console.log(`value: ${text}, type: ${typeof text}`);
text='8' / '2'; // value: 4, type: number
console.log(`value: ${text}, type: ${typeof text}`);
// console.log(text.charAt(0)); // error

// object
const taeho = {name:"taeho", age:21 };
// const 선언이라 taeho가 가르키는 object를 바꿀수는 없지만 그 안에 name,age 는 다른 값을 할당할 수 있다.
taeho.age = 27; // 값 변경 가능
console.log(taeho.age)





