// object
// 변수 하나는 1개의 값만 가질 수 있음
// object = {key : value};

// Literals and properties
const obj1 = {};               //'object literal' syntax
const obj2 = new Object();      // 'object constructor' syntax

function print(person) {
    console.log(person.name);
    console.log(person.age);
}

const ellie = { name: 'ellie', age: 4 };
print(ellie) // 함수 호출한거 

//자바스크립트에서는 이런 것도 가능하다.
ellie.hasJob = true;            // 선언되지 않은것을 만들 수가 있다. 지우는것도 가능
console.assert(ellie.hasJob)


//Computed properties
// key는 문자타입으로 받아와야함
console.log(ellie.name);  //
console.log(ellie['name']); //Computed properties 는 실시간으로 원하는 키 값을 받고있을 때 주로 사용한다.

ellie['hasJob'] = true;
console.log(ellie.hasJob);

function printValue(obj, key) { // 원하는 키를 사용자에게 받아 사용하는 함수
    console.log(obj.key); // undefined 
    console.log(obj[key]); // 
}
printValue(ellie, 'name');
printValue(ellie, 'age');





