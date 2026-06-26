// default export
// export default class MyButton{}

// named export
export default class Student {
  name = undefined;
  age = undefined;
  gender = undefined;

  constructor(argName, argAge, argGender) {
    this.name = argName;
    this.age = argAge;
    this.gender = argGender;
  }
}

// named export
export class Foo {
  constructor(argName) {
    this.name = argName;
  }
}

// export(Student, Foo);
