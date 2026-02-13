try {
  console.log(start);

  // throw new Error("My Error");
} catch (exception) {
  console.log(`Exception: ${exception}`);
} finally {
  console.log("finally");
}
