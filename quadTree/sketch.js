let particles = [];
var button;
let fade = 0;
let fadeAmount = 1;
let mouseIsPushed = false;

function setup() {
  window.scrollTo(0, 0);
  createCanvas(windowWidth, windowHeight/2);
  button = createButton('Clear particles');
  button.position(width-120, height);
  button.size(120, 30);
  button.mousePressed(clearParticles);
  // qtree.show();

  let numParticle = 60;
  for (let i = 0; i < numParticle; i++){
    let x = random(width);
    let y = random(height);
    particles.push(new Particle(x, y, i));
  }
}

// function draw() {
//   if (mouseIsPressed) {
//     let m = new Point(mouseX, mouseY);
//     qTree.insert(m);
//   }
//   background(0);
//   qTree.show()
// }

function clearParticles() {
  particles = [];
}

function showText() {
  if (fade<-100) fadeAmount = 1;
  if (fade>255) fadeAmount = -2;

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

function draw() {
  resizeCanvas(windowWidth, height);
  button.position(width-120, height);
  
  background(30, 160, 120);


  let boundary = new Rectangle(width/2, height, width/2, height);
  let qtree = new QuadTree(boundary, 4);

  if (mouseIsPressed && particles.length < 300 && mouseX<=width && mouseY<=height) {
    mouseIsPushed = true;
    let p = new Particle(mouseX, mouseY, particles.length);
    particles.push(p);
  }
  
  for (let p of particles) {
    let point = new Point(p.position.x, p.position.y, p);
    qtree.insert(point);
    p.update();
    p.edges();
    p.show();
  }

  qtree.show()
  
  for (let i=0; i < particles.length; i++){
    // for (let j = i + 1; j < particles.length; j++){
    //   particles[i].collide(particles[j]);
    // }
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
  if (!mouseIsPushed){
    showText();
  }

}

