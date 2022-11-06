// object
// 변수 하나는 1개의 값만 가질 수 있음
// 오브젝트는 키와 벨류의 집합체이다.
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
console.log(ellie.hasJob)


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

// Property value shorthand
const person1 = { name: 'a', age: 2 };
const person2 = { name: 'q', age: 21 };
const person3 = { name: 'w', age: 22 };
const person4 = new Person('elile', 30);
console.log(person4);

// 4. Constructor Function
function Person(name, age) {
    // 계산을 하지않고 순수하게 다른 객체를 만드는 함수들은 앞 글자를 대문자로 한다.
    this.name = name;
    this.age = age;
}


//in operator : 해당하는 오브젝트 안에 키가 있는지 없는지 확인하는 것
console.log('name' in ellie);       // true
console.log('age' in ellie);        // true
console.log('random' in ellie);     //false
console.log(ellie.random);          //undefined

//for..in vs for.. of
// for (key in obj)
// console.clear(); // 이전에 출력한거 지우기
for (key in ellie) {
    console.log(key)
}

// for (value of iterable) 
const array = [1, 2, 3, 4];
for (value of array) {
    console.log(value);
}

// Fun cloning
// object.assign(dest, [obj1, obj2, obj3...])
const user = { name: 'ellie', age: '20' };
const user2 = user;
console.log(user);
// 이때 user2의 user2.name='coder으로 변결하면 user의 값도 변경된다.


// 다른 복제 방법 
// 옛날에 쓰던 방식
const user3 = {};
for (key in user) {
    user3[key] = user[key]
}
console.log(user3)

// 요즘방식
const user4 = {};
Object.assign(user4, user);
console.log(user4)

// 다른 예시
const fruit1 = { color: 'red' };
const fruit2 = { color: 'blue', size: 'big' };
const mixed = Object.assign({}, fruit1, fruit2); // 뒤에 값이 덮어써진다.
console.log(mixed.color);
console.log(mixed.size);
