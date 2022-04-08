#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const userTasks = {};
request(url, function (e, response, body) {
  if (e) {
    console.error('error:', e);
  }
  const data = JSON.parse(body);
  for (let i = 0; i < data.length; i++) {
    const task = data[i];
    const id = data[i].userId;
    if (task.completed === true) {
      if (!userTasks[id]) {
        userTasks[id] = 0;
      }
      userTasks[id] += 1;
    }
  }
  console.log(userTasks);
});
