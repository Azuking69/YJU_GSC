let p = new Promise((resolve, reject) => {
  // 비동기 작업 작성
  // - resolve: 비동기 작업이 성공했을 때 호출하는 함수
  // - reject : 비동기 작업이 실패했을 때 호출하는 함수
});

// then(onFulfilled, onRejected)
// - onFulfilled: Promise가 resolve 되었을 때 실행
// - onRejected : Promise가 reject 되었을 때 실행
//
// catch(onRejected)
// - Promise가 reject 되었고,
//   then에서 실패 콜백(onRejected)을 처리하지 않은 경우 실행
p.then(
  () => {}, // 성공 처리
  () => {}, // 실패 처리
).catch(() => {}); // 예외(실패) 처리
