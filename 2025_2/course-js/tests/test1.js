print = console.log;

function sayHello() {
  print("hello");
}

function helloSomething() {
  let name = "GSC";
  function bar() {
    print("hello" + name);
  }
  return bar;
}

let foo = helloSomething();
foo();

// let foo = helloSomething(core){
//   core();
//   function bar(){
//     print("hello 2");
//   }
//   return bar;
//   // return core
// }

// function hello(core) {
//   core();
// }

hello(sayHello);

// let saySomething = sayHello;
// saySomething();
