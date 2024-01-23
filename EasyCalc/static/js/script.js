alert('Hello from script.js!');

let screen = document.getElementById('screen');

function appendToScreen(value) {
    if (screen.textContent === '0' || screen.textContent === 'Error') {
        screen.textContent = value;
    } else {
        screen.textContent += value;
    }
}


function clearScreen() {
    screen.textContent = '0';
}

function calculate() {
    try {
        screen.textContent = eval(screen.textContent);
    } catch (error) {
        screen.textContent = 'Error';
    }
}
