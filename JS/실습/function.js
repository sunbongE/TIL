// 함수 사용법
 function printHello() { // 함수를 만들었음
    console.log('Hello');
 }
 printHello();  // 함수 호출

// 더 유용한 함수
// 파라미터로 메시지를 전달받으면 출력하는 모습
 function log(message) { // 함수를 만들었음
    console.log(message);
 }
 log('Hello@@');  // 함수 호출
 // 자스에는 타입이 없어서 전달하는 값이 문자인지 숫자인지 헷갈릴 수있다.
 // 그래서 타입스크립트를 배워야함..

 // Parameters
 function changname(obj) { // 이름을 바꾸는 함수 
    obj.name = 'coder'; // 엘리를 코더로 바꿈
 }
 const ellie = { name:'ellie' };  
 changname(ellie); // 함수호출
 console.log(ellie) // 콘솔에 출력

 // Default parameters ( added in ES6)
 // 두가지 파라미터를 받아와야 하는데 
 // 사용자가 from 파라미터를 보내지 않았을 때 unknown으로 기본값을 설정함
 //  
 function showMessage(message, from = 'unknown') {
    console.log(`${message} by ${from}`);
 }
 showMessage('Hi');

 // Rest parameters (added in ES6)
function printAll(...args) { // ...은 레스트 파라미터라고 하고 이것은 배열 형태로 전달받게 된다.
    for (let i=0; i < args.length; i++) {
        console.log(args[i]); 
    }
// 다른 문법 같은 결과
    for (const arg of args) {
        console.log(arg);
    }
// 다른 문법 같은 결과
args.forEach((arg) => console.log(arg));
}
printAll('dream','coding','ellie');

// Local scope
// 밖에서는 안을 볼 수 없고 안에서는 밖을 볼 수 있다.
let globalMessage = 'global'; // global variable
function printMessage() {
    let message = 'Hello';    // local variable
    console.log(message);
    console.log(globalMessage) // 안에서는 글로벌 메시지를 볼 수 있음
}
printMessage();
// console.log(message) 이거는 블럭 밖에서 호출해서 에러가 발생한다.
// 위 함수에는 return이 없어보이지만 실제로는 return undefined가 생략되어 있음


// Return a value
function sum(a,b) {
    return a + b;
}
const result = sum(1,2); // 3 
console.log(`sum: ${sum(1,2)}`);

// Early return , early exit
// bad
function upgradeUser(user) {
    if (user.point > 10) { // 블럭안에 로직을 작성하면 가독성이 떨어진다.
        // long upgrade logic....
    }
} 

// good
function upgradeUser(user) {
    if (user.point <= 10) { 
    // 그래서 조건이 맞지 않을 때 빠르게 함수 종료하고 뒤에 필요한 로직을 작성하는 것이 더 좋다
        return;
    }
    // long upgrade logic.... 
} // 


// function expression
const print = function () { // 이름이 없는 함수를 anonymous function 이라 함
    console.log('print');
};
print();
const printAgain=print;
printAgain();
const sumAgain = sum;
console.log(sumAgain(1,3));

// callback
function randomQuiz(answer, printYes, printNo) {
    if (answer=='love') {
        printYes();
    } else{
        printNo();
    }
}

// anonymous function
const printYes = function () {
    console.log('yes!');
};

// named function
// 디버그할 때 좀 더 유리한가봄
const printNo = function print() {
    console.log('no!');
    // print(); // 콜스텍이 넘어가서 에러가 난다.
};

randomQuiz('wrong', printYes, printNo);
randomQuiz('love', printYes, printNo);

// Arrow function
// 항상 이름이 없다.
// const simplePrint = function () {
//     console.log('simplePrint!');
// };
// 위코드를 이렇게 나타낼 수 있다.
const simplePrint = () => console.log('simplePrint');
const add = (a,b) => a+b;
const simpleMultiply = (a,b) => {
    // 블럭을 사용하면 리턴으로 값을 넘겨야 한다.
    return a*b;
};

// IIFE : Immediately Invoked Function Expression
// 함수를 선언함과 동시에 실행이 된다!
(function hello() {
    console.log('IIFE');
}) ();