let myList = [10, 20, 30];

let newList = myList.map((v) => v * 10);
console.log(myList, newList);

// function map(argList, argFn) {
//   for (index in argList) {
//     argList[index] = argFn(argList[index]);
//   }
// }

// map(myList, (v) => v * 10);
// console.log(myList); // 100, 200, 300
