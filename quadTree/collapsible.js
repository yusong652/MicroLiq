document.addEventListener("DOMContentLoaded", function() {
    var coll = document.getElementsByClassName("chapter-title");

    for (let i = 0; i < coll.length; i++) {
        coll[i].addEventListener("click", function() {
            console.log("clicked", this); // 确保事件被触发
            this.classList.toggle("active");

            var content = this.nextElementSibling;
            while (content && content.nodeType === 3) { // 跳过空白文本节点
                content = content.nextSibling;
            }

            if (content && content.classList.contains("content")) {
                if (content.style.maxHeight && content.style.maxHeight !== "0px") {
                    content.style.maxHeight = null;
                } else {
                    content.style.maxHeight = content.scrollHeight + "px";
                }
            }
        });
    }
});