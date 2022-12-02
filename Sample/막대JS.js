'use strict';
let progressWap = document.querySelector('.progress_wap'),
    triggerPoint = progressWap.offsetTop - 400,
    progressBar = progressWap.querySelector('.bar'),
    progressRate = progressWap.querySelector('span'),
    initialRate = 0,
    numAni = null,
    excuted = false,
    targetRate = parseInt(progressWap.getAttribute('data-num'));

window.addEventListener('scroll', function () {
    let scrollAmt = this.scrollY;
    console.log(initialRate, targetRate)
    console.log(triggerPoint, scrollAmt)

    if (scrollAmt > triggerPoint) {
        if (!excuted) {
            startNumberAnimation();
            excuted = true;
        }
    }
})

function startNumberAnimation() {

    numAni = setInterval(() => {
        initialRate++;
        if (initialRate == targetRate) {
            // 멈추는 조건
            clearInterval(numAni)
        }
        progressBar.style.width = `${initialRate}%`;
        progressRate.innerText = `${initialRate}%`
    }, 20);
}

