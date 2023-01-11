# JS

- 변수

var - 변수에 값 변경 가능

var 사용하지마!

  블럭 스콥을 무시해서 사용안하는게 나음

 hoisting / 호이스팅이란?

- 어디에 선언했는지 상관없이 항상 가장 위로 선언을 끌어올리는 것

let - 제약이 없음 (일반적으로 많이 사용)

const - 한번 선언하면 절대 변경이 안된다.



- 함수

사용 예시

```js
// 방법 1
function add(a,b) {
    let temp = a+b;
    return temp
}

//방법 2
 ((a,b) => {return a+b})(1,2)
```



- 조건문

if , else if, else 이용가능

```js
if(money > 5000){
    ridetaxi(); // 참일 때
} else if(money > 2000) {
  	ridebus(); // 두번째 조건 
} else {
    walk();  // 거짓
}
```

실습

```js
let money = 6000  				// 변수 선언
if(money > 5000) {				// 참
    console.log("택시를 탄다");	 // print와 같은 거 console창에 뜸
} else {						// 거짓
    console.log("걸어간다")}
```



- 반복문

```js
//for (초기 값; 조건식; 증감식)
for (let i = 0; i < 10; i++) {
    console.log(i)
}
// 실전 사용 예시
arr = [1,2,3,4,5]
arr.forEach(element => {          // element : 이름짓기임
    console.log('나무 찍기'+element); // arr의 값을 하나 씩 뽑아온다!
});
```



# data type

### 숫자형

```js
//선언 방법은 어렵지 않게 그냥 숫자를 입력하면 된다.
const count = 17; // int
const size = 18.2 // decimal number

const infinity = 1/0;
const negativeinfinity = -1/0;
const nan = 'not a number' / 2; // NaN
const bigint = 1234567890123456789012345678901234567890; // over (-2**53)~ 2*53

```



### 문자

```js
const char = 'c';
const brendan = 'brendan';
const greeting = 'hello' + brendan;

console.log(`value: ${greeting}, type:${typeof greeting}`);
const helloBob = `hi ${brendan}!`; // template literals (string)
console.log(`value: ${helloBob}, type: ${typeof helloBob}`)
```





### Boolean

```js
// boolean
const canRead = true;
const test = 3<1; //false 
console.log(`value: ${canRead}, type: ${typeof canRead}`);
console.log(`value: ${test}, type: ${typeof test}`);
```



### null

```js
let nothing = null;
console.log(`value: ${nothing}, type: ${typeof nothing}`);
```



### undefined

```js
// nudefined
let x;
console.log(`value: ${x}, type: ${typeof x}`);
```





### symbol

```js
// symbol, create unique identifiers for objects
//고유한 식별자가 필요할 때 주로 사용
const symbol1 = Symbol('id');
const symbol2 = Symbol('id');
console.log(symbol1 === symbol2); // False
// 같게 하고싶다면 .for이용
const gsymbol1 = Symbol.for('id');
const gsymbol2 = Symbol.for('id');
console.log(gsymbol1 === gsymbol2); // True
// 출력
console.log(`value: ${symbol1}, type: ${typeof symbol1}`); 
// 이렇게 하면 에러가 난다.
console.log(`value: ${symbol1.description}, type: ${typeof symbol1}`);
///심볼을 출력할 때 항상 description 이용해야 한다.
```



## Dynamic typing

> 다이나믹 타입언어는 선언할 때 어떤 타입인지 선언하지않고 프로그램이 실행될 때 타입이 변경될 수 있는 것이다.

```js
let text = 'hello';
console.log(text.charAt(0)); // h 인덱싱한거임
console.log(`value: ${text}, type: ${typeof text}`);
text = 1; //value: 1, type: number
console.log(`value: ${text}, type: ${typeof text}`);
text='7' + 5; // value: 75, type: string
console.log(`value: ${text}, type: ${typeof text}`);
text='8' / '2'; // value: 4, type: number
console.log(`value: ${text}, type: ${typeof text}`);
console.log(text.charAt(0)); // error
```

이러게 타입이 런타임중 바뀌는 문제 때문에 타입스크립트가 나왔다고한다.

타입스크립트는 js에 타입이 올라간 형태라고 생각하면 된다.





## 

