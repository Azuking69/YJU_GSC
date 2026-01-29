class Student {
  // 2) Instance Member method
  // 3) Class Member variable
  // 4) Class Member method

  // Constructor
  constructor(argAge) {
    // 1) Instance Member variable
    this.name = argAge;
  }
}

let std1 = new Student("kim");
let std2 = new Student("lee");

// 출력: kim lee
console.log(std1.name, std2.name);
