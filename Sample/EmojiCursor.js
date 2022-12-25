
let images = ['🙂', '🎃', '🙃', '😁', '😎', '🥰', '🤩', '😴', '😶‍🌫️', '😑', '🤡', '🤓', '👽', '🐭']



document.addEventListener('mousemove', function (e) { // 문서안에서 마우스가 움직이면
    let body = document.querySelector('body'); // 바디를 잡고
    let emoji = document.createElement('span'); // span태그를 생성한다.
    let x = e.offsetX;                          // 왼쪽기준 오프셋 
    let y = e.offsetY;                          // 오른쪽기준 오프셋 

    emoji.style.left = x + 'px';            // 왼쪽기준 오프셋 px
    emoji.style.top = y + 'px';             // 오른쪽기준 오프셋 px

    let icon = images[Math.floor(Math.random() * images.length)];
    emoji.innerText = icon;

    let size = Math.random() * 50;
    emoji.style.fontSize = 5 + size + 'px';

    //get ramdom value for transform
    let max = 0;
    let min = 200;
    let randomValue = Math.floor((Math.random() * ((max + 1) - min)) + min);
    // console.log(randomValue)
    emoji.style.transform = 'translateX(' + randomValue + 'px)';


    body.appendChild(emoji); //이모지를 바디에 추가



    setTimeout(function () { //1초 후 추가된 이모지는 삭제한다.
        emoji.remove()
    }, 1000)
})