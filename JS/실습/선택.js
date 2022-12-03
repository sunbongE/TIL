var Title = document.getElementById('title'),
    list = document.getElementsByClassName('list'),
    ptags = document.getElementsByTagName('p'),
    pickme = document.querySelector('.list .pickme'),
    htag = document.querySelector('h1'),
    ptags2 = document.querySelectorAll('p'),
    firstspan = document.querySelector('p span');

console.log(Title)
console.log(list)
console.log(list[1]) // 인덱싱으로 접근가능
console.log(ptags)
console.log(pickme)
console.log(htag)
console.log(ptags2)
console.log(firstspan)

for (var i = 0; i < 4; i++) {
    console.log(i)
}