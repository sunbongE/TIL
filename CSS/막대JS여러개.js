'use strict';



let progressWap = document.querySelectorAll('.progress_wap');
progressWap.forEach(item => {
    // console.log(item)
    numAnimation(item);
});
function numAnimation(item) {
    let initialRate = 0;
    let bar_frame = item.querySelector('.bar_frame');
    let targetRate = item.getAttribute('data-num');
    let progressBar = item.querySelector('.bar');
    let progressRate = item.querySelector('span');
    let triggerPoint = item.offsetTop - 600;
    let excuted = false;
    window.addEventListener('scroll', function () {
        let scrollAmt = this.scrollY;
        // console.log(initialRate, targetRate)
        //console.log(triggerPoint, scrollAmt)

        if (scrollAmt > triggerPoint) {
            if (!excuted) {
                startNumberAnimation();
                excuted = true;
            }
        }
    })
    function startNumberAnimation() {
        let numAni = setInterval(() => {
            if (targetRate != 0) {

                initialRate++;
                if (initialRate == targetRate) {
                    // 멈추는 조건
                    clearInterval(numAni)
                }
                bar_frame.style.width = `${initialRate}%`;
                progressBar.style.width = `${initialRate}%`;
                progressRate.innerText = `${initialRate}%`;
            }
        }, 20);
    }
}
