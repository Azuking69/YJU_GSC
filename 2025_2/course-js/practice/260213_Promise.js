new Promise((resolve, reject) => {
  resolve("resolve!"); // reject("reject")
});

let p2 = p1.then(
  (result) => {
    console.log("p1 - resolve");
  },
  (error) => {
    console.log("p1 - resolve");
  },
);
