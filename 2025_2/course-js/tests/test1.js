class Student {
  age = 20;
  prtAge = function (argAge) {
    console.log(this.age);
  };
  prtAge2 = (argAge) => {
    // 실수에 쓰지 않은 방법
    console.log(this.age);
  };
  prtAge3(argAge) {
    console.log(this.age);
  }
}

let std1 = new Student();
std1.prtAge();

class Button {
  onclick = undefined;
}
let btn = new Button();
// btn.onclick = std1.prtAge;
// btn.onclick();
// btn.onclick.call(std1); // This brolen -> call, bind

btn.onclick = std1.prtAge2;
btn.onclick();

let test = std1.argAge2;
test();
