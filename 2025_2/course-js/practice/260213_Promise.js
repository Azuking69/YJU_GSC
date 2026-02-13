new Promise((resolve, reject) => {})
  .then(
    (result) => {},
    (error) => {},
  )
  .catch((error) => console.log(`catch: ${error}`))
  .finally((result) => console.log(`finally: ${result}`));
