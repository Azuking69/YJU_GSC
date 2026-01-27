class Student {
  // class -> ES6, ECMA2015
  age = undefined;
  constructor(argAge) {
    this.age = argAge;
  }

  prtAge() {
    console.log(this.age);
  }
}

class Button {
  onclick = null;
}

btn = new Button();
std = new Student();

btn.onclick = std.prtAge;
btn.onclick(); // this broken
