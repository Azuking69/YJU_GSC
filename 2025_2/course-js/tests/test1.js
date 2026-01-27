const fn1 = function () {
  return x + y;
};
const fn2 = () => {
  return x + y;
};

fn1(1, 2);
fn2(3, 3);

console.log(function () {
  return x + y;
});
