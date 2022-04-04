#!/usr/bin/node

function factorial (num) {
  if (num <= 1) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

const args = process.argv;
let int1;
if (args[2]) {
  int1 = parseInt(args[2]);
}
if (isNaN(int1)) {
  int1 = 1;
}
console.log(factorial(int1));
