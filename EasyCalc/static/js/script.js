
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

function backspace() {
    let currentText = screen.textContent;

    // Check if the text is not already '0' or 'Error'
    if (currentText !== '0' && currentText !== 'Error') {
        // Remove the last character from the text
        let newText = currentText.slice(0, -1);

        // If the text becomes empty, set it to '0'
        screen.textContent = newText || '0';
    }
}

