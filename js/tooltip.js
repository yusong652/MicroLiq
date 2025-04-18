document.addEventListener('DOMContentLoaded', () => {
    console.log('Tooltip script loaded'); // 调试用

    const tooltip = document.getElementById('tooltip');
    const buttons = document.querySelectorAll('.tab-button');
    
    console.log('Found buttons:', buttons.length); // 调试用
    
    // 显示提示框
    function showTooltip(button, text) {
        console.log('Showing tooltip:', text); // 调试用
        tooltip.textContent = text;
        
        const buttonRect = button.getBoundingClientRect();
        const navRect = document.querySelector('.tab-navigation').getBoundingClientRect();
        const tooltipRect = tooltip.getBoundingClientRect();
        
        let left = buttonRect.left + (buttonRect.width / 2);
        
        // 检查左右边界
        left = Math.max(tooltipRect.width / 2 + 10, Math.min(left, window.innerWidth - tooltipRect.width / 2 - 10));
        tooltip.style.left = `${left}px`;
        
        // 检查上方空间并设置位置
        if (navRect.top < tooltipRect.height + 10) {
            tooltip.style.top = `${navRect.bottom}px`;
            tooltip.style.transform = 'translate(-50%, 0)';
            tooltip.classList.add('show-below');
            tooltip.classList.remove('show-above');
        } else {
            tooltip.style.top = `${navRect.top}px`;
            tooltip.style.transform = 'translate(-50%, -100%)';
            tooltip.classList.add('show-above');
            tooltip.classList.remove('show-below');
        }
        
        tooltip.classList.add('show');
    }
    
    // 隐藏提示框
    function hideTooltip() {
        console.log('Hiding tooltip'); // 调试用
        tooltip.classList.remove('show', 'show-above', 'show-below');
    }
    
    // 为每个按钮添加事件监听器
    buttons.forEach(button => {
        const tooltipText = button.getAttribute('data-tooltip');
        console.log('Adding listeners to button:', tooltipText); // 调试用
        
        button.addEventListener('mouseenter', () => {
            showTooltip(button, tooltipText);
        });
        
        button.addEventListener('mouseleave', hideTooltip);
        
        button.addEventListener('mousemove', (e) => {
            if (tooltip.classList.contains('show')) {
                showTooltip(button, tooltipText);
            }
        });
    });
}); 