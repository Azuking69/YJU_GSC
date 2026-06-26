function delay(argMs) {
  let endTime = Date.now() + argMs;
  while (Date.now() < endTime) {}
}

export { delay };
