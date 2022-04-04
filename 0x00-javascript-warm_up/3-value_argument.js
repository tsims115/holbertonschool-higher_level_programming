#!/usr/bin/node
let first_arg = process.argv[2];
console.log(first_arg);
if (first_arg === undefined) {
  console.log('No argument')
} else {
  console.log('School')
}
