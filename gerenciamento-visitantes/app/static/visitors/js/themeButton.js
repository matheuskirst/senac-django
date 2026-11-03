function toggleThemeIcon(theme) {
    if (!theme) {
        return
    }

    let icon;
    if (theme == 'light') {
        icon = '#themeLightIcon';
    }
    else {
        icon = '#themeDarkIcon';
    }
    document.querySelector('svg use').setAttribute('href', icon)
}

let currentTheme = localStorage.getItem('theme');
toggleThemeIcon(currentTheme);

const button = document.getElementById('buttonToggleTheme');
button.addEventListener('click', function(e) {
    let currentTheme = localStorage.getItem('theme');

    if (!currentTheme) {
        return;
    }

    let theme;

    if (currentTheme == 'light') {
        theme = 'dark';
    }
    else {
        theme = 'light';
    }

    html.setAttribute('data-bs-theme', theme);
    localStorage.setItem('theme', theme);
    toggleThemeIcon(theme);
});
