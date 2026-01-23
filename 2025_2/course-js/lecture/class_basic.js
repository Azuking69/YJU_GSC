class Student {
  // Instance fields
  name = ""; // public instance field
  #age = 0; // private instance field

  // Static field (shared by the class)
  static count = 0;

  // Constructor
  constructor(argName = "", argAge = 0) {
    this.name = argName;
    this.#age = argAge;
    Student.count++;
  }

  // Instance method
  prtName() {
    console.log(this.name);
  }

  // Static method (class method)
  static prtCount() {
    console.log(Student.count); // or: console.log(this.count);
  }
}

const std1 = new Student("gsc", 10);
const std2 = new Student("ycjung", 20);

std1.prtName(); // gsc
std2.prtName(); // ycjung
Student.prtCount(); // 2
console.log(Student.count); // 2

// console.log(std1.#age); // SyntaxError:
// Private field '#age' must be declared in an enclosing class
