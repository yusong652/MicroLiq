document.addEventListener('DOMContentLoaded', () => {
    // 主题切换功能
    const themeToggle = document.getElementById('theme-toggle');
    const switchWrapper = document.querySelector('.theme-switch-wrapper');
    const canvas = document.querySelector('#animation-container');
    
    // 添加初始类名
    switchWrapper.classList.add('initial');
    
    // 从 localStorage 恢复主题状态
    if (localStorage.getItem('dark-mode') === 'true') {
        document.body.classList.add('dark-mode');
        themeToggle.checked = true;
    }

    // 主题切换事件监听
    themeToggle.addEventListener('change', () => {
        document.body.classList.toggle('dark-mode');
        localStorage.setItem('dark-mode', themeToggle.checked);
    });
    
    // 处理滚动事件
    let scrollTimeout;
    window.addEventListener('scroll', () => {
        if (scrollTimeout) {
            window.cancelAnimationFrame(scrollTimeout);
        }

        scrollTimeout = window.requestAnimationFrame(() => {
            const canvasBottom = canvas.getBoundingClientRect().bottom;
            
            if (canvasBottom <= window.innerHeight) {
                switchWrapper.classList.remove('initial');
                switchWrapper.classList.add('scrolled');
            } else {
                switchWrapper.classList.remove('scrolled');
                switchWrapper.classList.add('initial');
            }
        });
    });
}); 