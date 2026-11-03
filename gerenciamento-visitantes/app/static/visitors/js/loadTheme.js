const savedTheme = localStorage.getItem('theme');
if (!savedTheme){
    savedTheme = 'light'
    localStorage.setItem('theme', savedTheme)
}

const html = document.querySelector('html');
html.setAttribute('data-bs-theme', savedTheme);
