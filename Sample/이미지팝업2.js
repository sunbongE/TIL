const imgs = document.querySelectorAll('img');
let click = false; // 클릭 여부
let zoomLayer = 100; // 줌 배율 기본 값
let moved; // 움직임 여부
let moving = false; // 움직이는 중인지 여부
let click_position_X = 0; // 이미지 클릭한 위치
let click_position_Y = 0; // 이미지 클릭한 위치
let originX = 0; // 클릭한 이미지의 현재 left 값
let originY = 0; // 클릭한 이미지의 현재 top 값

let downListener = (ev) => { // 클릭 시
    moved = true;
    moving = false;

    originX = parseInt(getComputedStyle(ev.target)['left'].slice(0, -2));
    originY = parseInt(getComputedStyle(ev.target)['top'].slice(0, -2));
    click_position_X = ev.clientX;
    click_position_Y = ev.clientY;
}

let upListener = () => { // 마우스는 떼면 움직임 멈춤
    moved = false;
}

imgs.forEach(img => { // 이미지 마다 설정하기
    img.draggable = false; // 이미지 드래그 방지
    img.addEventListener('click', (ev) => {
        document.body.classList.add("noScroll");
        if (!click) {
            let copy = img.cloneNode();
            let pop = document.createElement('div');
            let zoom = document.createElement('div');
            let btn = document.createElement('button');
            copy.classList.add("zoomIn");
            pop.id = "pop";
            pop.classList.add("popup");
            pop.prepend(zoom);
            zoom.classList.add('zoom');
            zoom.prepend(copy);
            zoom.prepend(btn);
            btn.innerHTML = "&times;";
            btn.classList.add('btn', 'btn-danger', 'close');

            btn.addEventListener('click', () => {
                pop.classList.remove("show");
                setTimeout(() => {
                    pop.remove();
                    click = false;
                    document.body.classList.remove("noScroll");
                }, 300);
            });

            copy.addEventListener('click', (evt) => {
                if (!moved && !moving) {
                    if (copy.classList.contains("zoomOut")) {
                        copy.classList.replace("zoomOut", "zoomIn");
                    }
                    let zoomIn = evt.target;
                    zoomIn.style.cssText = `
                        width: ${zoomLayer}%;
                        top: ${evt.target.style.top};
                        left: ${evt.target.style.left};
                    `;
                    if (zoomLayer == 125) {
                        copy.classList.replace("zoomIn", "zoomOut");
                    }
                    if (zoomLayer > 125) {
                        zoomLayer = 100;
                        zoomIn.style.cssText = `
                            width: ${zoomLayer}%;
                            top: 0;
                            left: 0;
                        `;
                    }
                    zoomLayer += 25;
                }
            });

            copy.addEventListener('mousedown', downListener);
            copy.addEventListener('mousemove', evt => {
                if (moved) {
                    moving = true;
                    let oX = evt.clientX;
                    let oY = evt.clientY;
                    evt.target.style.cssText = `
                        top: ${originY + (oY - click_position_Y)}px;
                        left: ${originX + (oX - click_position_X)}px;
                        width: ${evt.target.style.width};
                    `;
                } else {
                    moving = false;
                    moved = false;
                }
            });
            window.addEventListener('mouseup', upListener);

            document.body.prepend(pop);
            setTimeout(() => {
                pop.classList.add('show');
            }, 300);
            click = true;
        }
    });
});