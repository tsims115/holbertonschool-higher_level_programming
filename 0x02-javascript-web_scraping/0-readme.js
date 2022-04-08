#!/usr/bin/node

const fs = require('fs');
const filename = process.argv[2];
fs.readFile(filename, function (err, contents) {
  if (err) {
    console.log(err);
  } else {
    console.log(contents.toString());
  }
});
