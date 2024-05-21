#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get(url, { json: true }, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const tasks = body;
  const completedTasks = {};
  tasks.forEach(task => {
    if (task.completed) {
      if (!completedTasks[task.userId]) {
        completedTasks[task.userId] = 0;
      }
      completedTasks[task.userId]++;
    }
  });
  console.log(completedTasks);
});
