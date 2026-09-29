#!/usr/bin/node
const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (!err) {
    const todos = JSON.parse(body);
    const result = {};
    for (const todo of todos) {
      if (todo.completed) {
        if (result[todo.userId]) {
          result[todo.userId]++;
        } else {
          result[todo.userId] = 1;
        }
      }
    }
    console.log(result);
  }
});
