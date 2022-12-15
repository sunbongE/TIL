const imgs = document.querySelectorAll('img'); //이미지 태그로 전부 선택
let click = false; // 클릭 여부
let zoomLayer = 100; // 줌 배율 기본 값
let moved;  //움직임 여부
let moving = false; // 움직이는 중인지 여부
let click_position_X = 0; //이미지 클릭 위치
let click_position_Y = 0; //이미지 클릭 위치
let originX = 0; // 클릭한 이미지의 현재 left 값
let originY = 0; // 클릭한 이미지의 현재 top 값

let downListener = (ev) => {
    moved = true;
    moving = false;
    originX = parseInt(getComputedStyle(ev.target)['left'].slice(0, -2));
    originY = parseInt(getComputedStyle(ev.target)['top'].slice(0, -2));

    click_position_X = ev.clientX;
    click_position_Y = ev.clientY;
}

let upListener = () => {
    moved = false;
}
imgs.forEach(img => {
    img.draggable = false;// 드래그 방지
    img.addEventListener('click', (ev) => {
        document.body.classList.add('noScroll');
        if (!click) {
            let copy = img.cloneNode(); //이미지를 복제함
            let pop = document.createElement('div'); //div생성
            let zoom = document.createElement('div');
            let btn = document.createElement('button'); //버튼 생성
            copy.classList.add('zoomin'); //이미지에 줌인 이라는 클래스 줌
            pop.id = 'pop';                 //pop의 id가 pop인가봄..
            pop.classList.add("popup");     //pop에 popup클래스 줌
            pop.prepend(zoom);              //pop에 zoom을 넣은듯..
            // console.log(pop)
            zoom.classList.add('zoom');     //클래스를 줌으로 주고  
            zoom.prepend(copy);             // 복제한 사진과 버튼을 zoom안에 넣음
            zoom.prepend(btn);
            btn.innerHTML = "&times;"; // x 의 유니코드 문자아님
            btn.classList.add('btn', 'btn-danger', 'close') //부트스트랩 

            btn.addEventListener('click', () => { // x버튼이 클릭되면
                pop.classList.remove("show"); // opacity 0으로 변함
                setTimeout(() => { // 0.3초 후 pop제거하고 원래 상태로 돌아가기위한 작업.
                    pop.remove();
                    click = false;
                    document.body.classList.remove("noScroll");
                }, 300);
            });

            copy.addEventListener('click', (evt) => {
                if (!moved && !moving) {
                    if (copy.classList.contains("zoomOut")) {
                        copy.classList.raplace("zoomOut", "zoomIn");
                    }
                    let zoomIn = evt.target;
                    zoomIn.style.cssText = `
                    width:${zoomLayer}%;
                    top:${evt.target.style.top};
                    left:${evt.target.style.left};
                    `;
                    if (zoomLayer == 150) {
                        copy.classList.replace('zoomIn', 'zoomOut');
                    }
                    if (zoomLayer > 150) {
                        zoomLayer = 100;
                        zoomIn.style.cssText = `
                            width: ${zoomLayer}%;
                            top: 0;
                            left: 0;
                        `;
                    }
                    zoomLayer += 10;

                }
            });
            copy.addEventListener('mousedown', downListener);
            copy.addEventListener('mousemove', evt => {
                if (moved) {
                    moving = true;
                    let oX = evt.clientX;
                    let oY = evt.clientY;
                    evt.target.style.cssText = `
                    top: ${originY + (oY - click_position_Y)}px
                    left: ${originX + (oX - click_position_X)}px;
                    width: ${evt.target.style.width};
                    `;
                } else {
                    moving = false;
                    moved = false;
                }
            });
            window.addEventListener('mouseup', upListener)
            document.body.prepend(pop);
            setTimeout(() => {
                pop.classList.add('show');
            }, 300);
            click = true;

        }
    });
});