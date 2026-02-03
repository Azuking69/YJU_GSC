// Higher-order function
// input: fn
// output: fn
// Pros: Abstract and Resuable
print = console.log;

function forEach(argArray, argFn) {
  for (let i = 0; i < argArray.length; i++) {
    // print(argArray[i]);
    argFn(argArray[i]);
  }
}

function map(argArray, argFn) {
  for (let i in argArray) {
    argArray[i] = argFn(argArray[i]);
  }
}

let myList = [10, 20, 30, 40];

// 1) 현제 배열 값을 화면에 출력
// 10, 20, 30, 40
forEach(myList, (v) => process.stdout.write(`${v}\t`));
// myList.forEach((v) => process.stdout.write(`${v}\t`));

// 2) 각 배열의 원소에 1을 더하다
// 요소 값이 변경 11, 21, 31, 41
// map(myList, 1);
map(myList, (v) => {
  return v + 1;
});

// 3) 현제 배열 값을 화면에 출력
// 11, 21, 31, 41
forEach(myList, (v) => {
  process.stdout.write(`${v}\t`);
});

// 4) 각 배열의 원소에 2을 더하다
// 요소 값이 변경 13, 23, 33, 43
// map(myList, 2);
map(myList, (v) => {
  return v + 2;
});

// 5) 현제 배열 값을 화면에 출력
// 13, 23, 33, 43
forEach(myList, (v) => {
  process.stdout.write(`${v}\t`);
});
