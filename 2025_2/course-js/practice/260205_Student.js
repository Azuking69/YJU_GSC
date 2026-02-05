print = console.log;
// Getter / Setter -> a method to get or set avalue
//                    to the member variable(praivate)

class Student {
  #name = undefined;
  #age = undefined;
  constructor(argName, argAge) {
    this.#name = argName;
    this.#age = argAge;
  }
  // getter for name MV
  getName() {
    return `Hello ${this.#name}`;
  }
  // getter for age
  getAge() {
    return `Age: ${this.#age}`;
  }
}

let std1 = new Student("gsc", 20);
print(std1.getName(), std1.getAge()); // OK

std1.#name = 20; // Error
std1.#age = 20; // Error
