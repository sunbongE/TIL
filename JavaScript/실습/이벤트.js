var btn = document.getElementById('submit'),
    container = document.querySelector('.container');

btn.addEventListener('click', function () {
    //이벤트를 클릭하면 실제로 일어나는 일을 여기에 기술한다.
    btn.style.color = 'red';
});
// 이런 방법이 있고 html버튼에 onclick 으로 해도되지만 이방법은 바람직하지 않다고함
// 이유 웹표준을 어겨서 html구조 언어에 자바스크립트의 동적언어가 섞여있어서 그렇다고함.
container.addEventListener('mouseover', function () {
    console.log('마우스가 올라옴')
})
container.addEventListener('mouseenter', function () {
    console.log('마우스가 들어옴')
})
container.addEventListener('mouseleave', function () {
    console.log('마우스가 들어옴')
}) // 이를 통해 마우스의 움직임을 알수 있다.

window.addEventListener('keydown', function (e) {
    console.log(e.key)
    console.log(e.keyCode)
})
//여기에 나오는 키코드를 가지고 돔 조작을 할 수 있게 된다. 
//esc를 누르면 나가지거나 방향기를 누르면 어떤 동작을 하는 것이 가능해진다.
