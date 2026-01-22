let x = 1;

function a_1() {
  let y = 2;
  function a_2() {
    let z = 3;
    console.log(x, y, z);
  }
  return a_2;
}

function b_1() {
  const bar = a_1();
  bar(); // a_2() -> 1, 2, 3
}

b_1();
