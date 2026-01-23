let x = 10;

function f() {
  console.log(x); // x -> 10
  // 만약 JS가 동적 스코프 언어였다면,
  // x는 20 출력
}

function g() {
  let x = 20;
  f();
}

g();
