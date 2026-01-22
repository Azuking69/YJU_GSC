function bar() {
  let x = 1;
}

function foo() {
  let y = 2;

  function pos() {
    let z = 3;
  }
  pos();
  bar();
}
foo();
