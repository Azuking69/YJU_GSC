let myList = [10, 200, 30, 400];

// 배열의 각 요소를 순회
// 어떤 조건을 만족하는 값만 새로운 배열으로 리턴
function filter(argList, argFn) {
  // 새로운 배열을 하나 생성
  let newList = [];

  // 입력 배열의 요소를 순회
  for (let value of argList) {
    // 어떤 조건을 만족하면 새로운 배열에 삽입
    if (argFn(value)) {
      newList.push();
    }
  }

  // 새로운 배열을 반환
  return newList;
}

// 100이상 값들만 리스토로 생성
newList = myList.filter((v) => v >= 100);
console.log(newList);
