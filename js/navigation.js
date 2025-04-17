document.addEventListener('DOMContentLoaded', function() {
    const tabNavigation = document.querySelector('.tab-navigation');
    const tabButtons = document.querySelectorAll('.tab-button');
    const contentSections = document.querySelectorAll('.content-section');

    // 滚动按钮到中间的函数
    function scrollButtonToCenter(button) {
        const navWidth = tabNavigation.offsetWidth;
        const buttonLeft = button.offsetLeft;
        const buttonWidth = button.offsetWidth;
        
        // 计算滚动位置：按钮左边距 - (容器宽度/2 - 按钮宽度/2)
        const scrollPosition = buttonLeft - (navWidth/2) + (buttonWidth/2);
        
        // 使用平滑滚动
        tabNavigation.scrollTo({
            left: scrollPosition,
            behavior: 'smooth'
        });
    }

    // 标签切换逻辑
    tabButtons.forEach(button => {
        button.addEventListener('click', () => {
            // 移除所有活动状态
            tabButtons.forEach(btn => btn.classList.remove('active'));
            contentSections.forEach(section => section.classList.remove('active'));

            // 添加新的活动状态
            button.classList.add('active');
            const targetSection = document.getElementById(button.dataset.section);
            if (targetSection) {
                targetSection.classList.add('active');
            }

            // 将选中的按钮滚动到中间
            scrollButtonToCenter(button);
        });
    });

    // 拖动相关变量
    let isDown = false;
    let startX;
    let scrollLeft;
    let lastX;

    // 鼠标按下事件
    tabNavigation.addEventListener('mousedown', (e) => {
        isDown = true;
        tabNavigation.style.cursor = 'grabbing';
        startX = e.pageX;
        lastX = e.pageX;
        scrollLeft = tabNavigation.scrollLeft;
        tabNavigation.classList.add('active-grab');
    });

    // 鼠标离开和松开事件的统一处理
    function stopDragging() {
        if (!isDown) return;
        isDown = false;
        tabNavigation.style.cursor = 'grab';
        tabNavigation.classList.remove('active-grab');

        // 找到当前激活的按钮并将其居中
        const activeButton = document.querySelector('.tab-button.active');
        if (activeButton) {
            scrollButtonToCenter(activeButton);
        }
    }

    tabNavigation.addEventListener('mouseleave', stopDragging);
    tabNavigation.addEventListener('mouseup', stopDragging);

    // 优化的鼠标移动事件
    tabNavigation.addEventListener('mousemove', (e) => {
        if (!isDown) return;
        e.preventDefault();

        const x = e.pageX;
        const dx = x - lastX;
        lastX = x;

        tabNavigation.scrollLeft -= dx;
    });

    // 触摸事件处理
    tabNavigation.addEventListener('touchstart', (e) => {
        startX = e.touches[0].pageX;
        scrollLeft = tabNavigation.scrollLeft;
        tabNavigation.classList.add('active-grab');
    });

    tabNavigation.addEventListener('touchmove', (e) => {
        if (!startX) return;
        const x = e.touches[0].pageX;
        const dx = x - startX;
        startX = x;
        tabNavigation.scrollLeft -= dx;
    });

    tabNavigation.addEventListener('touchend', () => {
        startX = null;
        tabNavigation.classList.remove('active-grab');
        
        // 触摸结束时也将激活的按钮居中
        const activeButton = document.querySelector('.tab-button.active');
        if (activeButton) {
            scrollButtonToCenter(activeButton);
        }
    });

    // 页面加载时初始化
    if (contentSections.length > 0) {
        contentSections[0].classList.add('active');
    }
    if (tabButtons.length > 0) {
        tabButtons[0].classList.add('active');
        // 页面加载时将第一个按钮居中
        scrollButtonToCenter(tabButtons[0]);
    }

    // 窗口大小改变时重新居中当前激活的按钮
    window.addEventListener('resize', () => {
        const activeButton = document.querySelector('.tab-button.active');
        if (activeButton) {
            scrollButtonToCenter(activeButton);
        }
    });

    // 添加滚动监听，处理导航栏的视觉效果
    let lastScrollTop = 0;
    window.addEventListener('scroll', () => {
        const currentScrollTop = window.pageYOffset || document.documentElement.scrollTop;
        const tabNavigation = document.querySelector('.tab-navigation');
        
        // 当滚动超过导航栏高度时添加阴影效果
        if (currentScrollTop > 0) {
            tabNavigation.classList.add('scrolled');
        } else {
            tabNavigation.classList.remove('scrolled');
        }
        
        lastScrollTop = currentScrollTop;
    }, { passive: true });
}); 