/*
* - 변수 지정하기
* - 문서의 높이를 계산하고 원하는 부분이 상단에서 얼마큼 떨어져 있는지 offset 값을 계산하기
* - 스크롤과 클릭 이벤트 작성하기
*/
var btt = document.getElementById('back-to-top'),
    docElem = document.documentElement,
    offset,
    scrollPos,
    docHeight;

// 문서 높이 계산하기
// 2 가지 방법이 있음.
// docHeight = docElem.scrollHeight;
// docHeight = docElem.offsetHeight; // 문서의 높이
//브라우저마다 문서의 높이를 구하는 방식이 다르기때문에 이런 식으로 둘 중 큰 값을 문서의 높이로 설정한다.

docHeight = Math.max(docElem.offsetHeight, docElem.scrollHeight); //둘중에 높은 값을 가져온다.
console.log(docHeight);

scrollPos = docElem.scrollTop // 스크롤 양을 알 수 있음...

if (docHeight != '') {
    offset = docHeight / 4;
}
// 스크롤 이벤트 추가
window.addEventListener('scroll', function () { // 스크롤 양을 실시간으로 보여줌...
    scrollPos = docElem.scrollTop;
    console.log(scrollPos);

    // if문 축약형
    // 바뀌는값 = (조건) ? '참일 때' : '거짓일 때';
    btt.className = (scrollPos > offset) ? 'visible' : '';
    // if (scrollPos > offset) {
    //     btt.className = 'visible'
    // } else {
    //     btt.className = ''
    // }

});
btt.className = 'box' // 클래스를 대체하는 것 추가X

// 클릭 이벤트 추가
btt.addEventListener('click', function (e) {
    e.preventDefault() // 링크의 본연의 기능을 막는다.
    //부드럽게 올라갈 수 있게 함수 생성 
    scrollToTop();
})
function scrollToTop() {
    //일정시간마다 할 일
    //setInerval(할이, 시간);
    // 0.0015s =15
    // 윈도우의 스크롤 양이 0이 아닐 때
    // 실제 할일 = 윈도우의 스크롤 양을 조금씩 뺄거 : window.scrollBy(0, -55);
    // 스크롤 양이 0이면 멈춤 : clearInterval(이름);    
    var scrollInterval = setInterval(function () {
        if (scrollPos != 0) {
            window.scrollBy(0, -55)
        } else {
            clearInterval(scrollInterval)
        }
    }, 15)


}