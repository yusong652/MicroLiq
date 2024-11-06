class Particle {
  constructor(x, y, id) {
    this.id = id;
    this.position = createVector(x, y);
    this.velocity = p5.Vector.random2D(0,1);
    this.velocity.mult(random(0.2, 0.4));
    this.acceleration = createVector(0, 0);
    this.radiusMax = 16
    this.r = random(this.radiusMax/2, this.radiusMax);
    this.mass = 4.0/3.0 * Math.PI * Math.pow(this.r, 3);
  }
  // method to apply force
  applyForce(force) {
    let f = force.copy();
    f.div(this.mass);
    this.acceleration.add(f);
  }
  // method to update; 
  // Timestep is assumed to be 1.
  update() {
    this.velocity.add(this.acceleration);
    this.position.add(this.velocity);
    this.acceleration.mult(0);
  }
  edges() {
    console.log(width);
    if (this.position.x > width - this.r){
      this.position.x = width - this.r;
      this.velocity.x *= -1;
    } else if (this.position.x < this.r) {
      this.position.x = this.r;
      this.velocity.x *= -1;
    }
    if (this.position.y > height - this.r) {
      this.position.y = height - this.r;
      this.velocity.y *= -1;
    } else if (this.position.y < this.r) {
      this.position.y = this.r;
      this.velocity.y *= -1;
    }
  }
  collide(other){
    let impactVector = p5.Vector.sub(other.position, this.position);
    let d = impactVector.mag();
    if (d < this.r + other.r) {
      let overlap = d - (this.r + other.r);
      let dir = impactVector.copy();
      dir.setMag(overlap * 0.5);
      this.position.add(dir);
      other.position.sub(dir);
      d = this.r + other.r;
      impactVector.setMag(d);
      
      let mSum = this.mass + other.mass;
      let den = mSum * d * d;
      let vDiff = p5.Vector.sub(other.velocity, this.velocity);
      // Particle A
      let num = vDiff.dot(impactVector);
      let deltaVA = impactVector.copy();
      deltaVA.mult(2 * other.mass * num / den);
      this.velocity.add(deltaVA);
      //Particle B
      let deltaVB = impactVector.copy();
      deltaVB.mult(-2 * this.mass * num / den)
      other.velocity.add(deltaVB);
    }
  }
  show(){
    strokeWeight(3.2)
    circle(this.position.x, this.position.y, this.r*2);
  }
}