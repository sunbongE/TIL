// document.addEventListener('DOMContentLoaded', function () {
//     document.getElementsByTagName('h1')[0].style.color = 'red';
// })

// $(document).ready(function () {
//     $('h1').css({ 'color': 'red' });
// });

$(function () {
    // 문서가 준비되면 할 일을 정의하는 곳
    $('h1').css('color', 'red'); //속성 한가지 바꿀 때
    // $('#typo .inner').css('text-decoration', 'underline');
    // $('#typo .inner').css('border-bottom', '5px solid red');
    // $('#typo .inner').css('transform', 'rotate(45deg)');
    // $('#typo .inner').css('opacity', 0.5); //수는 따옴표 안해도 되지만 퍼센트는 꼭해야함

    // $('#typo .inner').css({ // 여러가지 속성을 바꾸는 문법 / 하이픈을 줄일 수 있다..
    //     'text-decoration': 'underline',
    //     'border-bottom': '5px solid red',
    //     'transform': 'rotate(45deg)',
    //     'opacity': 0.5
    // })
    $('#typo .inner').css({ // 여러가지 속성을 바꾸는 문법 / 하이픈을 줄일 수 있다..
        textDecoration: 'underline',
        borderBottom: '5px solid red',
        transform: 'rotate(45deg)',
        opacity: 0.5
    })
})
