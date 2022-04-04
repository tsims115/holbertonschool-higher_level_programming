#!/usr/bin/node
const args = process.argv;
const len = args.length;
let int;
let flag = 0;
let row;
if (len === 3) {
  int = parseInt(args[2]);
} else {
  flag = 1;
}
if (isNaN(int) || flag === 1) {
  console.log('Missing size');
} else {
  for (let i = 0; i < int; i++) {
    row = '';
    for (let j = 0; j < int; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
