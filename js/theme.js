document.addEventListener('DOMContentLoaded', () => {
    const themeToggle = document.getElementById('theme-toggle');
    const themeSwitch = document.querySelector('.theme-switch');
    const body = document.body;
    
    // 从 localStorage 获取保存的主题并立即应用
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        body.classList.add('dark-mode');
        themeToggle.checked = true;
    }

    // 切换主题的函数
    function toggleTheme() {
        const isDark = body.classList.toggle('dark-mode');
        localStorage.setItem('theme', isDark ? 'dark' : 'light');
        themeToggle.checked = isDark;
    }

    // 监听 checkbox 的 change 事件
    themeToggle.addEventListener('change', toggleTheme);

    // 监听整个开关的点击事件
    themeSwitch.addEventListener('click', (e) => {
        // 阻止事件冒泡，防止重复触发
        e.stopPropagation();
        toggleTheme();
    });
}); 