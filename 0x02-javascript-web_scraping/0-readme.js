#!/usr/bin/node
const fs = require('fs');
fs.readFile('cisfun', function (err, contents) {
    console.log(err)
    console.log(contents.toString());
});
