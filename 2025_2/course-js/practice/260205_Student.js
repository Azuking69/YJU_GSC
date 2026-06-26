let print = console.log;
// Getter / Setter -> a method to get or set avalue
//                    to the member variable(praivate)

class Student {
  #name = undefined;
  #age = undefined;

  constructor(argName, argAge) {
    this.#name = argName;
    this.#age = argAge;
  }

  get name() {
    return this.#name;
  }
  get age() {
    return this.#age;
  }
  set name(argName) {
    this.#name = argName + "Hello";
  }
  set age(argAge) {
    this.#age = `Age: ${argAge}`;
  }
}

let std1 = new Student("gsc", 20);
print(std1.name, std1.age); // OK
std1.name = "YJU";
print(std1.name, std1.age); // OK
