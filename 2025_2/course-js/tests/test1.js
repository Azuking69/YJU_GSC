// .js file

// JS {} -> create an object
foo = {
  name:"gsc", 
  prtName: function(){console.log()this.name};};

// 1) {} -> create an object
// 2) this.name = "gsc"
// 3) this.prtname = function(){console.log()this.name}

foo.prtName();
// class Bar {
//   constructor(argName = "gsc") {
//     this.name = argName;
//   }
// }

// b1 = new Bar();
// console.log(b1.name);
