class Student {
  age = 20;
  prtAge = function () {
    console.log(this.age);
  };
}

let std1 = new Student();
std1.prtAge();

class Button {
  onclick = undefined;
}
let btn = new Button();
btn.onclick = std1.prtAge;
// btn.onclick();
btn.onclick.call(std1);
