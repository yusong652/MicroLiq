let particles = [];
let fade = 0;
let fadeAmount = 1;
let mouseIsPushed = false;
let isMouseOverCanvas = false;
var qtree;
var particleNumLmt;
var wall_x_min, wall_x_max, wall_y_min, wall_y_max;

function setup() {
  window.scrollTo(0, 0);

  let canvas = createCanvas(windowWidth, windowHeight * 0.7);
  canvas.parent('animation-container');

  let placeholder = document.getElementById('canvas-placeholder');
  let canvasElement = document.querySelector('#animation-container canvas');

  if (placeholder && canvasElement) {
    setTimeout(() => {
      canvasElement.style.opacity = '1';
      placeholder.style.opacity = '0';
      setTimeout(() => {
        if (placeholder && placeholder.parentNode) {
          placeholder.parentNode.removeChild(placeholder);
        }
      }, 600);
    }, 100);
  }

  wall_x_min = 0;
  wall_x_max = width;
  wall_y_min = 0;
  wall_y_max = height;
  let numParticle = 60;
  particleNumLmt = getParticleNumLmt();
  for (let i = 0; i < numParticle; i++) {
    let x = random(width);
    let y = random(height);
    particles.push(new Particle(x, y, i));
  }

  canvas.elt.addEventListener('mouseenter', () => { isMouseOverCanvas = true; });
  canvas.elt.addEventListener('mouseleave', () => { isMouseOverCanvas = false; });
}

function getParticleNumLmt() {
  return Math.floor(width * height / 1000);
}

function showText() {
  if (fade < -50) fadeAmount = 1;
  if (fade > 255) fadeAmount = -4;
  fade += fadeAmount;
  if (fade >= 0) {
    strokeWeight(0);
    textSize(14);
    fill(255, 255, 255, fade * 0.6);
    textAlign(LEFT, BOTTOM);
    text("Click to add particles", 20, height - 16);
  }
}

function collisionDetection() {
  for (let i = 0; i < particles.length; i++) {
    let p = particles[i];
    let range = new Rectangle(p.position.x, p.position.y, p.radiusMax * 2, p.radiusMax * 2);
    let others = qtree.query(range);
    for (let pointOther of others) {
      let pOther = pointOther.userData;
      if (p.id > pOther.id) {
        p.collide(pOther);
      }
    }
  }
}

function checkIfAddParticle() {
  if (!isMouseOverCanvas) return;
  if (!(mouseIsPressed && particles.length < particleNumLmt)) return;
  mouseIsPushed = true;
  let p = new Particle(mouseX, mouseY, particles.length);
  particles.push(p);
}

function updateQTree() {
  let boundary = new Rectangle(width, height * 2, width, height * 2);
  qtree = new QuadTree(boundary, 4);
  for (let p of particles) {
    let point = new Point(p.position.x, p.position.y, p);
    qtree.insert(point);
  }
  qtree.show();
}

function updateParticle() {
  collisionDetection();
  for (let p of particles) {
    p.update();
    p.edges(wall_x_min, wall_x_max, wall_y_min, wall_y_max);
  }
  for (let p of particles) {
    p.show();
  }
}

function windowResized() {
  resizeCanvas(windowWidth, windowHeight * 0.7);
  wall_x_max = width;
  wall_y_max = height;
  particleNumLmt = getParticleNumLmt();
}

function draw() {
  const isDarkMode = document.body.classList.contains('dark-mode');
  if (isDarkMode) {
    background(30, 40, 55);
  } else {
    background(30, 160, 120);
  }

  checkIfAddParticle();
  updateQTree();
  updateParticle();

  if (!mouseIsPushed) {
    showText();
  }
}

function mousePressed(event) {
  if (!isMouseOverCanvas) return;
}
