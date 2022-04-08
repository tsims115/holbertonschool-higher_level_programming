#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;
request(url, function (e, response, body) {
  if (e) {
    console.error('error:', e);
  }
  console.log(JSON.parse(body).title);
});
