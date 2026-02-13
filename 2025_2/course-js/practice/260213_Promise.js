new Promise((resolve, reject) => {
  resolve("Executor: S");
  // reject("Excutor: F");
})
  .then(
    (result) => {
      console.log(`then-S: ${result}`);
    },
    (error) => {
      console.log(`then-T: ${error}`);
      throw new Error("Error!!!! Then");
    },
  )
  //   Exception Handling
  .catch((error) => console.log(`catch: ${error}`))
  .finally((result) => console.log(`finally: ${result}`));
