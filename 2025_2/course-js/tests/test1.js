// .js file
class Bar {
  constructor(argName = "gsc") {
    this.name = argName;
  }

  prtName() {
    console.log(this.name);
  }
}

b1 = new Bar();
b1.prtName(); // gsc
const f = b1.prtName;
f();
