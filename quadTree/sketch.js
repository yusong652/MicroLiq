let particles = [];
let fade = 0;
let fadeAmount = 1;
let mouseIsPushed = false;
let isMouseOverCanvas = false;
var qtree;
var button;
var particleNumLmt;
var wall_x_min, wall_x_max, wall_y_min, wall_y_max;
var isParticleUnderClearing = false;
let velocityBoundaryMovement = 0;
let accelerationBoundaryMovement = 0.0;

function setup() {
  window.scrollTo(0, 0);
  let canvas = createCanvas(windowWidth, windowHeight*0.4);
  
  // 先检查占位符元素是否存在
  let placeholder = document.getElementById('canvas-placeholder');
  if (placeholder) {
    // 初始时设置 canvas 为透明
    canvas.elt.style.opacity = '0';
    
    // 在 canvas 加载完成后执行过渡
    setTimeout(() => {
      // 再次检查占位符是否存在
      if (placeholder) {
        // 淡出占位符
        placeholder.style.opacity = '0';
        // 淡入 canvas
        canvas.elt.style.opacity = '1';
        // 移除占位符
        setTimeout(() => {
          if (placeholder && placeholder.parentNode) {
            placeholder.parentNode.removeChild(placeholder);
          }
        }, 300); // 与 CSS transition 时间相匹配
      }
    }, 100);
  } else {
    // 如果没有占位符，直接显示 canvas
    canvas.elt.style.opacity = '1';
  }

  document.getElementById("clearParticles").onclick = setClearParticlesOn;
  wall_x_min = 0;
  wall_x_max = width;
  wall_y_min = 0;
  wall_y_max = height;
  let numParticle = 60;
  particleNumLmt = getParticleNumLmt();
  for (let i = 0; i < numParticle; i++){
    let x = random(width);
    let y = random(height);
    particles.push(new Particle(x, y, i));
  }

  // 添加画布鼠标事件监听
  canvas.elt.addEventListener('mouseenter', () => {
    isMouseOverCanvas = true;
  });
  canvas.elt.addEventListener('mouseleave', () => {
    isMouseOverCanvas = false;
  });
}

function getParticleNumLmt(){
  return Math.floor(width * height / 1000);
}

function setClearParticlesOn(){
  isParticleUnderClearing = true;
  wall_x_max = width * 2;
}

function checkIfClearParticles(){
  if (isParticleUnderClearing && particles.length > 0) {
    clearParticles();
  } else {
    wall_x_max = width;
  }
  if (wall_x_min >= width){
    resetStateAfterClear();
  } 
}

function clearParticles() {
  a_var = 0.008;
  if (accelerationBoundaryMovement < 1){
    accelerationBoundaryMovement += a_var;
  }
  if (velocityBoundaryMovement < 32.0){
    velocityBoundaryMovement += accelerationBoundaryMovement;
  }
  wall_x_min += velocityBoundaryMovement;
}

function resetStateAfterClear(){
  isParticleUnderClearing = false;
  particles = [];
  mouseIsPushed = false;
  particleNumLmt = getParticleNumLmt();
  wall_x_min = 0;
  wall_x_max = width;
  wall_y_min = 0;
  wall_y_max = height;
}

function showText() {
  if (fade<-50) fadeAmount = 1;
  if (fade>255) fadeAmount = -4;

  fade += fadeAmount;
  if (fade >= 0) {
    strokeWeight(0);
    textSize(30);
    fill(255, 255, 255, fade);
    text("Press to add particles", 20, 30);
    textSize(12);
    text("QuadTree for collision detection", width-100, height, 160, 120);
  }
}

function collisionDetection(){
  for (let i=0; i < particles.length; i++){
    let p = particles[i];
    let range = new Rectangle(p.position.x, p.position.y,  p.radiusMax*2, p.radiusMax*2);
    let others = qtree.query(range);
    for (let pointOther of others){
      let pOther = pointOther.userData; 
      if (p.id > pOther.id){
          p.collide(pOther);
      }
    }
  }
}

function checkIfAddParticle(){
  if (!isMouseOverCanvas) return;  // 如果鼠标不在画布上，直接返回
  if (!(mouseIsPressed && particles.length < particleNumLmt)) {
    return; 
  }
  mouseIsPushed = true;
  let p = new Particle(mouseX, mouseY, particles.length);
  particles.push(p);
}

function updateQTree(){
  let boundary = new Rectangle(width, height*2, width, height*2);
  qtree = new QuadTree(boundary, 4);
  for (let p of particles) {
    let point = new Point(p.position.x, p.position.y, p);
    qtree.insert(point);
  }
  qtree.show()
} 

function updateParticle(){
  collisionDetection();
  for (let p of particles) {
    p.update();
    p.edges(wall_x_min, wall_x_max, wall_y_min, wall_y_max);
  }
  for (let p of particles) {
    p.show();
  }
} 

function draw() {
  resizeCanvas(windowWidth, height);
  
  // 检查深色模式
  const isDarkMode = document.body.classList.contains('dark-mode');
  
  // 根据模式设置背景色
  if (isDarkMode) {
    background(30, 40, 55);  // 深色模式使用深蓝色
  } else {
    background(30, 160, 120);  // 浅色模式使用绿色
  }
  
  checkIfAddParticle();
  checkIfClearParticles();
  updateQTree();
  updateParticle();
  
  if (!mouseIsPushed) {
    showText();
  }
}

function mousePressed(event) {
  // 如果鼠标不在画布上，不处理事件
  if (!isMouseOverCanvas) return;
  
  // 检查是否点击了清除按钮
  const clearButton = document.getElementById('clearParticles');
  if (clearButton && clearButton.contains(event.target)) {
    return false;
  }
}
