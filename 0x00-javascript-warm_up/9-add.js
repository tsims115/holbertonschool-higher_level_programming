#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const args = process.argv;
let int1 = NaN;
let int2 = NaN;
if (args[2]) {
  int1 = parseInt(args[2]);
}
if (args[3]) {
  int2 = parseInt(args[3]);
}
console.log(add(int1, int2));
