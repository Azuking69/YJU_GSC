function makeDelay() {
  while (Date.now) {}
}

console.log("10");

console.log("20");

setTimeout(() => {
  console.log("50");
}, 1000); // 비동기

console.log("30");

makeDelay(5000);

console.log("40");
