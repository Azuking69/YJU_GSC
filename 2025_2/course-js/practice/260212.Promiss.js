let p = new Promise(
  // Excutor: 비동기로 실행 -> user defined function
  () => {
    console.log("test");
    a("S");
    // b("F");
  },
);

p.then(
  (result) => console.log(result),
  (error) => console.log(error),
);
// 프로미스 겍체 생성 후 사용자로부터 받은 함수를 실행한다.

// p.then(/* OnResolved */, /* OnRejectted */);

// let p2 = new Promise();

// // Task A -> Task B -> Task C -> Task D
// p2.then().then().then().catch().finally();
