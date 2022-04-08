#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filename = process.argv[3];
request(url, function (e, response, body) {
  if (e) {
    console.error('error:', e);
  }
  const data = body;
  fs.writeFile(filename, data, (c, e) => {
    if (e) {
      console.log(e);
    }
  });
});
