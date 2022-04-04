#!/usr/bin/node

function max (a) {
  let max = a[0];
  let secondMax = a[0];
  for (let i = 0; i < a.length; i++) {
    if (a[i] > max) {
      max = a[i];
    }
  }
  for (let i = 0; i < a.length; i++) {
    if (a[i] > secondMax && a[i] < max) {
      secondMax = a[i];
    }
  }
  return (secondMax);
}

const args = process.argv;
const array = [];
for (let i = 2; args[i]; i++) {
  array.push(parseInt(args[i]));
}
if (array.length <= 1) {
  console.log(0);
} else {
  console.log(max(array));
}
