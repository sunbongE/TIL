/*
tab-content 안의 div들 모두 안보이도록 한다.

링크를 클릭하면 클릭한 그 요소의 href속성의 값을 변수 tabTarget에 저장
저장된 값에서 #을 삭제한다.
*/

var targetLink = document.querySelectorAll('.tab-menu a')
var tabContent = document.querySelectorAll('#tab-content div ')


for (var i = 0; i < targetLink.length; i++) {
    targetLink[i].addEventListener('click', e => {
        e.preventDefault
        var orgTarget = e.target.getAttribute('href')
        var tabTarget = orgTarget.replace('#', '')

        for (var x = 0; x < tabContent.length; x++) {
            tabContent[x].style.display = 'none';
        }
        document.getElementById(tabTarget).style.display = 'block';
        for (var j = 0; j < targetLink.length; j++) {
            // targetLink[j].className = ''
            targetLink[j].classList.remove('active')
        }
        e.target.classList.add('active')
    })

}


document.getElementById('tabs-1').style.display = 'block';


