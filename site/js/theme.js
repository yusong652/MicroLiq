document.addEventListener('DOMContentLoaded', () => {
    const themeToggle = document.getElementById('theme-toggle');
    const switchWrapper = document.querySelector('.theme-switch-wrapper');

    // Restore theme from localStorage
    if (localStorage.getItem('dark-mode') === 'true') {
        document.body.classList.add('dark-mode');
        themeToggle.checked = true;
    }

    // Toggle handler
    themeToggle.addEventListener('change', () => {
        document.body.classList.toggle('dark-mode');
        localStorage.setItem('dark-mode', themeToggle.checked);
    });

    // Update toggle appearance on scroll (transparent over hero → solid over content)
    const container = document.getElementById('animation-container');
    let ticking = false;

    window.addEventListener('scroll', () => {
        if (!ticking) {
            window.requestAnimationFrame(() => {
                const heroBottom = container.getBoundingClientRect().bottom;
                if (heroBottom <= 60) {
                    switchWrapper.classList.add('scrolled');
                } else {
                    switchWrapper.classList.remove('scrolled');
                }
                ticking = false;
            });
            ticking = true;
        }
    }, { passive: true });
});
