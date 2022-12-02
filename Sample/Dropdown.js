let dropdown = document.querySelector('.dropdown')
dropdown.onclick = function () {
    dropdown.classList.toggle('active');
}
function show(a) {
    document.querySelector('.text02').value = a;
}