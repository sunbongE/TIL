# JS

- 변수

var - 변수에 값 변경 가능

let - 제약이 없음 (일반적으로 많이 사용)

const - 변수의 값은 바뀔 수 없다.

```js

```



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



