const inbnt = document.querySelector('#in-bnt')
inbnt.addEventListener('click', function () {
    // 컨테이너 만들었고
    const ballcontainer = document.createElement('div')
    ballcontainer.classList.add('ball-container')
    //  공 만들고
    const nums = _.sampleSize(_.range(1, 46), 6)
    console.log(nums)

    for (num of nums) {
        const ball = document.createElement('div')
        ball.classList.add('ball')

        ball.innerText = num
        console.log(num)

        if (num <= 10) {
            ball.style.backgroundColor = 'orange'
        }
        else if (num <= 20) {
            ball.style.backgroundColor = 'blue'
        }
        else if (num <= 30) {
            ball.style.backgroundColor = 'red'
        }
        else if (num <= 40) {
            ball.style.backgroundColor = 'black'
        }
        else if (num <= 45) {
            ball.style.backgroundColor = 'green'
        }

        ballcontainer.appendChild(ball)
        console.log(ballcontainer)

        const result = document.querySelector('#result')
        result.appendChild(ball)
    }

    const resetbnt = document.querySelector('#reset-bnt')
    resetbnt.addEventListener('click', function () {
        result.innerHTML = ""
        console.log('@')
    })


})