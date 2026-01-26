// setTimeout(// handler, time: ms);
// class -> ES6

var count = 0;

function increate() {
  count++;
  console.log(this);
}

setTimeout(increate, 1000);
