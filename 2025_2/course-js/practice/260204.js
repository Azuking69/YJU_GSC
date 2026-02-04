// Higher-order function

let myList = [10, 20, 30];

// 배열을 순회하겠다
// 순회하면서 실행할 알고리즘은
// 각 요소 값을 사용자 함수에 입력하고,
// 이때 변환하는 값을 각 요소로 치환

function map(argList, argFn) {
  // 배열을 순회
  for (index in argList) {
    // 사용자 함수의 변환 값을 현재 요소 값으로 치환
    // 이때, 사용자 함수 호출 시, 현 요소값을 전달
    argList[index] = argFn(argList[index]);
  }
}

// let myFn = function (argValue) {
//   // my task
//   return argValue * 10;
// };

map(myList, function (argValue) {
  return argValue * 10;
});
