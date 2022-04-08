#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let userTasks = {}
request(url, function (e, response, body) {
  if (e) {
    console.error('error:', e);
  }
  data = JSON.parse(body);
  for (let i = 0; i < data.length; i++) {
    let task = data[i];
    let id = data[i].userId;
    if (task.completed === true) {
      if (!userTasks[id]) {
        userTasks[id] = 0;
      }
      userTasks[id] += 1;
    }
  }
  console.log(userTasks);
});
