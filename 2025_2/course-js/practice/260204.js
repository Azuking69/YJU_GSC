// Higher-order function
let myList = [10, 20, 30];

// 배열을 순회하겠다
// 순회하면서 실행할 알고리즘은 사용자 정의에 따라
function forEach(argList, argFn) {
  // 배열을 순회 첫번째 -> 마지막까지
  for (const value of argList) {
    // 사용자 알고리즘 실행
    argFn(value);
  }
}

let myFn = function (argValue) {
  // my task
  console.log(argValue);
};

forEach(myList, myFn); // 10, 20, 30
