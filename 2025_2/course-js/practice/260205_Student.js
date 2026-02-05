print = console.log;
// Getter / Setter -> a method to get or set avalue
//                    to the member variable(praivate)

class Student {
  #name = undefined;
  #age = undefined;

  // getter for name MV
  getName() {
    return this.#name;
  }
  // setter for name MV
  setName(argName) {
    this.#name = argName;
  }
}

let std1 = new Student();
std1.setName = "GSC";
print(std1.getName());

std1.age = 20;
print(std1.age);
