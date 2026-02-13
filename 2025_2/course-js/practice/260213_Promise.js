let p1 = new Promise((resolve, reject) => {
  resolve("resolve!"); // reject("reject")
});

let p2 = p1.then(
  (result) => {
    console.log("p1 - resolve");
    return Promise.reject();
  },
  (error) => {
    console.log("p1 - resolve");
  },
);

p2.then(
  (result) => {
    console.log("p2 - resolve");
  },
  (error) => {
    console.log("p2 - resolve");
  },
);
