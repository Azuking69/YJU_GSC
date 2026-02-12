let p = new Promise(
    // Excutor
);

p.then(/* OnResolved */, /* OnRejectted */);

let p2 = new Promise();

// Task A -> Task B -> Task C -> Task D
p2.then().then().then().catch().finally();