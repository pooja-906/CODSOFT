const passwordResult = document.getElementById('passwordResult');
const lengthSlider = document.getElementById('lengthSlider');
const lengthVal = document.getElementById('lengthVal');

const uppercaseEl = document.getElementById('uppercase');
const lowercaseEl = document.getElementById('lowercase');
const numbersEl = document.getElementById('numbers');
const symbolsEl = document.getElementById('symbols');
const strengthText = document.getElementById('strengthText');

const charSets = {
    uppercase: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    lowercase: 'abcdefghijklmnopqrstuvwxyz',
    numbers: '0123456789',
    symbols: '!@#$%^&*()_+~`|}{[]:;?><,./-='
};

// Update length display text when slider moves
lengthSlider.addEventListener('input', (e) => {
    lengthVal.innerText = e.target.value;
    generatePassword(); // Regenerate instantly for better UX
});

function generatePassword() {
    let length = +lengthSlider.value;
    let allowedChars = '';
    
    if (uppercaseEl.checked) allowedChars += charSets.uppercase;
    if (lowercaseEl.checked) allowedChars += charSets.lowercase;
    if (numbersEl.checked) allowedChars += charSets.numbers;
    if (symbolsEl.checked) allowedChars += charSets.symbols;

    if (allowedChars === '') {
        passwordResult.value = "Select an option";
        strengthText.innerText = '---';
        return;
    }

    let generatedPassword = '';
    for (let i = 0; i < length; i++) {
        const index = Math.floor(Math.random() * allowedChars.length);
        generatedPassword += allowedChars[index];
    }

    passwordResult.value = generatedPassword;
    updateStrength(length, allowedChars.length);
}

function updateStrength(length, poolSize) {
    // Basic entropy calculation logic
    if (length < 8 || poolSize < 30) {
        strengthText.innerText = 'Weak';
        strengthText.style.color = '#E53E3E';
    } else if (length < 14) {
        strengthText.innerText = 'Medium';
        strengthText.style.color = '#DD6B20';
    } else {
        strengthText.innerText = 'Strong';
        strengthText.style.color = '#38B2AC';
    }
}

async function copyToClipboard() {
    const password = passwordResult.value;
    if (password === '' || password === 'Click Regenerate' || password === "Select an option") return;
    
    try {
        await navigator.clipboard.writeText(password);
        alert('Password copied to clipboard!');
    } catch (err) {
        console.error('Failed to copy: ', err);
    }
}

// Generate an initial password on page load
window.onload = generatePassword;