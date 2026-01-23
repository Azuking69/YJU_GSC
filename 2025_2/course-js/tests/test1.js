function bar() {
  // OER -> global
}

function outer() {
  // OER -> global
  function inner() {
    // OER -> outer
  }
}
