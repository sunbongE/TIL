const inbnt = document.querySelector('#in-bnt')
inbnt.addEventListener('click', function () {
    // ball container
    const ballcontainer = document.createElement('div')
    ballcontainer.classList.add('ball-container')
    //  random nums
    const nums = _.sampleSize(_.range(1, 46), 6)
    console.log(nums)

    for (num of nums) {
        // balldiv 
        const balldiv = document.createElement('div')
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

        ballcontainer.appendChild(balldiv)
        balldiv.appendChild(ball)
        console.log(balldiv)

        const result = document.querySelector('#result')
        result.appendChild(ballcontainer)
    }
    // reset bnt
    const resetbnt = document.querySelector('#reset-bnt')
    resetbnt.addEventListener('click', function () {
        result.innerHTML = ""
        console.log('@')
    })


})