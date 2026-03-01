document.addEventListener('DOMContentLoaded', () => {
    // Scroll-triggered reveal animations
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, {
        threshold: 0.15,
        rootMargin: '0px 0px -40px 0px'
    });

    // Observe research cards
    document.querySelectorAll('.research-card').forEach(el => observer.observe(el));

    // Observe fade-in sections
    document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));

    // Observe stagger-children containers
    document.querySelectorAll('.stagger-children').forEach(el => observer.observe(el));
});
