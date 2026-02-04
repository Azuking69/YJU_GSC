class Student {
  constructor(argAge) {
    this.age = argAge;
  }
}

const myList = [];

myList.push(new Student(20));
myList.push(new Student(30));
myList.push(new Student(40));

let newList = myList.filter((v) => v.age >= 30);
console.log(newList);
