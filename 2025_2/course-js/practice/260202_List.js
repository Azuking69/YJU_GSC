print = console.log;

let myList1 = [100, 200, 300]; // dense array
let myList2 = [10, 20, 30]; // dense attay
delete myList1[1];
delete myList2[0];

print(`myList1: ${myList1}, length: ${myList1.length}`);
print(`myList2: ${myList2}, length: ${myList2.length}`);
