let p1 = new Promise(
  // Excutor function
  (resovle, reject) => {
    console.log("Excutor function is invoked!!");
    setTimeout(() => console.log("wait 3 seconds!!"), 3000);
    // resovle(hello);
    resovle("Hello");
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
