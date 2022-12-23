// 제목을 클릭하면 제목의 부모에게 엑티브를 넣어주고 아래 바디가 나타나게 해준다
// 컬랩스 올 누르면 전부 접히는 것

var btnCollapse = document.getElementById('btn-collapse'),
    heading = document.getElementsByClassName('panel-heading'),
    question = document.getElementsByClassName('panel-question'),
    answer = document.getElementsByClassName('panel-body');

//제목을 클릭하면 할 일 heading -> 배열 형태임

for (var i = 0; i < heading.length; i++) { //헤딩들 마다 할 일 
    heading[i].addEventListener('click', e => {



        //클릭되면 모든 질문에 active 클래스를 빼준다.
        for (var j = 0; j < question.length; j++) { // question마다 할 일
            question[j].classList.remove('active')
        }

        //클릭한 타겟의 부모요소 선택
        e.target.parentNode.classList.add('active')

        activateBody();

    });
}
function activateBody() {
    // panel-body 모두 안보이도록 answer -> display:none;
    for (var x = 0; x < answer.length; x++) {
        answer[x].style.display = 'none';
    }



    //active panel-question 자식중 panel-body 나타나도록
    var activePanel = document.querySelector('.panel-question.active .panel-body');
    // console.log(activePanel)
    activePanel.style.display = 'block';
}
activateBody();

//btnCollapse 버튼을 클릭하면 모든 answer 안보이도록 해야함.
btnCollapse.addEventListener('click', () => {
    for (var s = 0; s < answer.length; s++) {
        answer[s].style.display = 'none';
    }
})