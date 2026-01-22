function sayName() {
  console.log(this.name);
}

const a = { name: "Alice", sayName };
const b = { name: "Bob", sayName };

a.sayName(); // Alice
b.sayName(); // Bob
