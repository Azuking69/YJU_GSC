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
    return this.#name;
  }
  // setter for name MV
  setName(argName) {
    this.#name = argName;
  }
  // getter for age
  getAge() {
    return this.#age;
  }
  // setter for age
  setAge(argAge) {
    if (argAge >= 0 && argAge <= 150) {
      this.#age = argAge;
      return true;
    }
  }
}

let std1 = new Student();
std1.setName = "GSC";
print(std1.getName());

std1.age = 20;
print(std1.age);
