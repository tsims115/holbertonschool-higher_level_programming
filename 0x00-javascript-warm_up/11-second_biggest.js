#!/usr/bin/node

function max (a) {
  const max = Math.max.apply(null, a);
  a.splice(a.indexOf(max), 1);
  return Math.max.apply(null, a);
}

const args = process.argv;
const array = [];
for (let i = 2; args[i]; i++) {
  array.push(parseInt(args[i]));
}
if (array.length <= 1) {
  console.log('0');
} else {
  console.log(max(array));
}
