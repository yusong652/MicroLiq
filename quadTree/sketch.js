let particles = [];
let fade = 0;
let fadeAmount = 1;
let mouseIsPushed = false;
var qtree;
var button;
var particleNumLmt;
var wall_x_min, wall_x_max, wall_y_min, wall_y_max;
var isParticleUnderClearing = false;
let velocityBoundaryMovement = 0;
let accelerationBoundaryMovement = 0.0;

function setup() {
  window.scrollTo(0, 0);
  createCanvas(windowWidth, windowHeight*0.4);
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
  if (fade >= 0){

    strokeWeight(0);
    textSize(30);
    fill(255, 255, 255, fade);
    text("Press to add particles", 20, 30);
    textSize(12)
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
  if (!(mouseIsPressed && particles.length < particleNumLmt && mouseX<=width && mouseY<=height)) {
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
  background(30, 160, 120);
  checkIfAddParticle();
  checkIfClearParticles();
  updateQTree();
  updateParticle();
  

  if (!mouseIsPushed){
    showText();
  }
}
