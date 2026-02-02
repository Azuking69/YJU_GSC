print = console.log;

let myList1 = [100, 200, 300]; // dense array
let myList2 = [10, 20, 30]; // dense attay
myList1[100] = 400; // space array

for (let i = 0; i < myList1.length; i++) {
  print(myList1[i]);
}
for (let i = 0; i < myList2.length; i++) {
  print(myList2[i]);
}

print(`myList1: ${myList1}, length: ${myList1.length}`);
print(`myList2: ${myList2}, length: ${myList2.length}`);
