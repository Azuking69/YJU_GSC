function makeDelay(argMs) {
  let endTime = Date.now() + argMs;
  while (Date.now() < endTime) {}
  return Math.random() > 0.5;
}

let p = new Promise(
  // executor -> user defined function
  (resolve, reject) => {
    console.log("start");

    setTimeout(() => {
        if (Math.random > 0.5){
            resolve("S");
        }else{
            reject("F");
        }, 3000);
    console.log("end");
  }
);

p.then(
  (result) => console.log(result),
  (error) => console.log(error),
);
