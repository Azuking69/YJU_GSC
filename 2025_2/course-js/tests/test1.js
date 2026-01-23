// Java
int a = 2; // a -> int, static 
a = 2; // 오류

// JS or Python
let a = 2; // JS
a = 2; // Python

class Bar {
  constructor(argName = "gsc") {
    this.name = argName;
  }
}

b1 = new Bar();
console.log(b1.name);
