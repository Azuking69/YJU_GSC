print = console.log;

let x = 2;
var a = 1;

function bar() {
  print(x);
}

function outer() {
  let y = 2;
  function inner() {
    let z = 3;
    print(x, y, z);
  }
  bar();
}
