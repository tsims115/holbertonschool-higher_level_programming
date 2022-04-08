#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const urlToFind = 'https://swapi-api.hbtn.io/api/people/18/';
let count = 0;
request(url, function (e, response, body) {
  if (e) {
    console.error('error:', e);
  }
  const data = JSON.parse(body).results;
  for (let i = 0; i < data.length; i++) {
    for (let j = 0; j < data[i].characters.length; j++) {
      if (data[i].characters[j] === urlToFind) {
        count++;
      }
    }
  }
  console.log(count);
});
