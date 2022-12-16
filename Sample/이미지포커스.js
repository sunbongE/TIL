// let tg = document.getElementsByClassName("tg")[0];
let tg = document.querySelector('.tg');
let imgPath = document.querySelector('.tg').getAttribute("data-image");
let photo = document.querySelector(".photo");
// console.log(photo)

photo.style.backgroundImage = `url(${imgPath})`;

//이미지 확대 (마우스 갖다댐)
tg.addEventListener("mouseover", function () {
    photo.style.transform = `scale(2)`; //2배확대
})

//이미지 축소 (마우스 벗어남)

tg.addEventListener("mouseout", function () {
    photo.style.transform = `scale(1)`; //크기복원
})

//마우스 따라 그림 이동
tg.addEventListener("mousemove", function (element) {
    // (현재마우스위치 - 이미지 기준좌표) / 기준너비 (최초 0, 0)
    let oriX = ((element.pageX - this.offsetLeft) / this.offsetWidth) * 100;
    let oriY = ((element.pageY - this.offsetTop) / this.offsetHeight) * 100;
    photo.style.transformOrigin = `${oriX}% ${oriY}%`; //이미지의 기준점을 새로 설정한 위치로 변경
})