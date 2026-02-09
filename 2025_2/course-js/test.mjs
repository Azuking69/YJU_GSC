import Student, { Foo } from "./gsc/Student.mjs";

let stdList = [];
stdList.push(new Student("kim", 20, "M"));
stdList.push(new Student("Lee", 18, "M"));
stdList.push(new Student("Jung", 35, "F"));
stdList.push(new Student("Jeo", 40, "M"));

// stdList.forEach((v) => console.log(v.name));
// stdList.filter((v) => v.gender === "M").reduce((acc, v) => (acc += v.age), 0);

let sortedList = stdList.sort((a, b) => b.age - a.age > 0);
console.log(stdList.every((v) => v.gender === "M"));
