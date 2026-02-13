new Promise((resolve, reject) => {});

let p2 = p1.then();
console.log(p2 instanceof Promise);
