#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (e, response, body) {
  if (e) {
    console.error('error:', error);
  }
  console.log('code:', response && response.statusCode);
});
