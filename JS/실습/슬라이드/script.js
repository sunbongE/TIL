

// 변수 지정
var sliderWrapper = document.getElementsByClassName('container'),//클래스명 container
    sliderContainer = document.getElementsByClassName('slider-container'), //클래스명 slider-container
    slides = document.getElementsByClassName('slide'),//클래스명 slide
    slideCount = slides.length,//슬라이드의 개수
    currentIndex = 0, //슬라이드의 현재 몇번째인지 알 수 있다.
    topHeight = 0,
    navPrev = document.getElementById('prev'), // 아이디 prev
    navNext = document.getElementById('next');//아이디next
// console.log(slideCount)


//슬라이드의 높이 확인하여 부모의 높이로 지정하기

function calculateTallestSlide() { //전체 슬라이드의 높이중 가장 큰 값을 높이로 지정한 것이다.

    for (var i = 0; i < slideCount; i++) {
        if (slides[i].offsetHeight > topHeight) {
            topHeight = slides[i].offsetHeight;
        }
    }
    sliderWrapper[0].style.height = topHeight + 'px'; //높이는 px단위로 나와야 한다.
    sliderContainer[0].style.height = topHeight + 'px';
}

calculateTallestSlide();
//지금까지는 슬라이드가 겹쳐진 상태여서 left값을 각각 지정을 해줘야 한다.


// 슬라이드가 있으면 가로로 배열하기
// 0 100% 200% .....
for (var i = 0; i < slideCount; i++) {
    slides[i].style.left = i * 100 + '%'
}

// 슬라이드 이동 함수 
//currentIndex가 1 이면 sliderContainer.left = -100% 이런식의 변화가 필요하다.
function gotoSlide(idx) {
    sliderContainer[0].style.left = idx * -100 + '%';
    sliderContainer[0].classList.add('animated');
    currentIndex = idx

    // updateNav();
}

function updateNav() {
    if (currentIndex == 0) {
        navPrev.classList.add('disabled');
    } else {
        navPrev.classList.remove('disabled');
    }
    if (currentIndex == slideCount - 1) {
        navNext.classList.add('disabled');
    } else {
        navNext.classList.remove('disabled');
    }
}

// 버튼기능 업데이트 함수


// 버튼을 클릭하면 슬라이드 이동시키기
navPrev.addEventListener('click', e => {
    e.preventDefault();
    //gotoSlide(currentIndex - 1);
    //처음인데 이전 버튼을 누른다면 마지막으로
    if (currentIndex > 0) {
        gotoSlide(currentIndex - 1)

    } else {
        gotoSlide(slideCount - 1)

    }
})

navNext.addEventListener('click', e => {
    e.preventDefault();
    //gotoSlide(currentIndex + 1);
    if (currentIndex < slideCount - 1) {
        gotoSlide(currentIndex + 1)

    } else {
        gotoSlide(0)

    }
})


// 첫번째 슬라이드 먼저 보이도록 하기

gotoSlide(0)
//이게 없으면 0번째 페이지에서도 이전버튼이 있다. 왜냐면 함수가 실행조건이 아니기때문
