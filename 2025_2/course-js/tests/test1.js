function bar() {
  print(){
    console.log(this);
  };
}

b1 = new Bar();
b1.prt(); // gsc
const f = b1.prtName;
f();
