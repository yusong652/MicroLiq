class Point {
  constructor(x, y, userData) {
    this.x = x;
    this.y = y;    
    this.userData = userData;
  }
}

class Circle {
  constructor(x, y, r) {
    this.x = x;
    this.y = y;
    this.r = r;
    this.rSquared = this.r * this.r;
  }
  contains(point) {
    // Distance
    let d = Math.pow((point.x - this.x), 2) + Math.pow((point.y - this.y), 2)
    return this.rSquared > d;
  }
}

class Rectangle {
  constructor(x, y, w, h) {
    this.x = x;
    this.y = y;
    this.w = w;
    this.h = h;
  }
  contains(point) {
    return (point.x > this.x - this.w && 
           point.x <= this.x + this.w &&
           point.y > this.y - this.h &&
           point.y <= this.y + this.h);
  }
  intersects(range) {
    return !(range.x - range.w > this.x + this.w || 
             range.x + range.w < this.x - this.w ||
             range.y - range.h > this.y + this.h ||
             range.y + range.h < this.y - this.h);
  }
}

class QuadTree {
  constructor(boundary, n) {
    this.boundary = boundary;
    this.capacity = n;
    this.points = [];
    this.divided = false;
  }
  
  insert(point) {
    if (!this.boundary.contains(point)){
      return;
    }
    
    if (this.points.length < this.capacity) {
      this.points.push(point);
      return true;
    } else {
      if (!this.divided){
        this.subdivide();   
      }
      if (this.northwest.insert(point)){
        return true;
      } else if (this.northeast.insert(point)) {
        return true;
      } else if (this.southwest.insert(point)) {
        return true;
      } else {
        this.southeast.insert(point);
        return true;
      }
    }
  }
  
  subdivide() {
    let x = this.boundary.x;
    let y = this.boundary.y;
    let w = this.boundary.w;
    let h = this.boundary.h;
    let ne = new Rectangle(x + w/2, y - h/2, w/2, h/2);
    let nw = new Rectangle(x - w/2, y - h/2, w/2, h/2);
    let se = new Rectangle(x + w/2, y + h/2, w/2, h/2);
    let sw = new Rectangle(x - w/2, y + h/2, w/2, h/2);
    this.northwest = new QuadTree(nw, this.capacity);
    this.northeast = new QuadTree(ne, this.capacity);
    this.southwest = new QuadTree(sw, this.capacity);
    this.southeast = new QuadTree(se, this.capacity);
    this.divided = true;  
  }
  
  query(range, found) {
    if (!found) {
      found = [];
    }
    if(!this.boundary.intersects(range)) {
      // empty array
      return found;
    } else {
      for (let p of this.points) {
        if (range.contains(p)) {
          found.push(p);
        }
      }
      if (this.divided) {
        this.northwest.query(range, found);
        this.northeast.query(range, found);
        this.southwest.query(range, found);
        this.southeast.query(range, found);
      }
      return found;
    }
  }
  
  show() {
    stroke(255);
    noFill();
    rectMode("center");
    strokeWeight(1.6);
    rect(this.boundary.x, this.boundary.y, this.boundary.w * 2, this.boundary.h * 2);

    if (this.divided) {
      this.northwest.show();
      this.northeast.show();
      this.southwest.show();
      this.southeast.show();
    }
  }
}