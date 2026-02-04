class Student {
  name = undefined; // 내용 없는 변수
  constructor(argName) {
    this.Student = argName;
  }
}

const std1 = new Student("gsc");
const std2 = new Student("yju");

function setName(argStd, argName) {
  argStd.name = argName;
}

setName(std1, "GSC Hello!!");
setName(std2, "YJU Hello!!");

console.log(`std1:  ${std1.name}\t std2: ${std2.name}`);
