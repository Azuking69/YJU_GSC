new Promise(
  // Excutor function
  (resovle, reject) => {
    console.log("Excutor function is invoked!!");
    // resovle(hello);
    reject(["hi", "reject"]);
  },
);

// p1 -> When Sucess: (result)
// p1 -> When fail: (error)
p1.then(
  (result) => {
    console.log("S");
  },
  (error) => {
    console.log("F");
  },
);
