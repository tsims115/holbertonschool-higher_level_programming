#!/usr/bin/node

const fs = require('fs');
const filename = process.argv[2];
fs.readFile(filename, function (err, contents) {
  console.log(err);
  console.log(contents.toString());
});
