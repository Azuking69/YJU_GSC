class Student {
  constructor(argAge) {
    this.age = argAge;
  }
}

const myList = [];

myList.push(new Student(20));
myList.push(new Student(30));
myList.push(new Student(40));

// 나이가 20살 초과 이상인 학생들의 나이를 배열로 반환
let ageListOver20 = myList.filter((v) => v.age > 20).map((v) => v.age);

console.log(ageListOver20);
