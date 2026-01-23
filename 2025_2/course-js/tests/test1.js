function bar() {
  console.log(this);
}

function foo() {
  console.log(this);
  function pos() {
    console.log(this);
  }
  pos();
}
bar();
foo();
