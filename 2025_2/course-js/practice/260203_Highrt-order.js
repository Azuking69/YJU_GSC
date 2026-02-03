// Higher-order function
// input: fn
// output: fn
// Pros: Abstract and Resuable

let myList = [10, 20, 30, 40];

// 1) 현제 배열 값을 화면에 출력
// 10, 20, 30, 40
print = console.log;
print(myList);

// 2) 각 배열의 원소에 1을 더하다
// 요소 값이 변경 11, 21, 31, 41
for (let i = 0; i < myList.length; i++) {
  myList[i] = myList[i] + 1;
}
// myList[0] = myList[0] + 1;
// myList[1] = myList[1] + 1;
// myList[2] = myList[2] + 1;
// myList[3] = myList[3] + 1;

// 3) 현제 배열 값을 화면에 출력
// 11, 21, 31, 41
print(myList);

// 4) 각 배열의 원소에 2을 더하다
// 요소 값이 변경 13, 23, 33, 43
for (let i = 0; i < myList.length; i++) {
  myList[i] = myList[i] + 2;
}
// myList[0] = myList[0] + 2;
// myList[1] = myList[1] + 2;
// myList[2] = myList[2] + 2;
// myList[3] = myList[3] + 2;

// 5) 현제 배열 값을 화면에 출력
// 13, 23, 33, 43
print(myList);
