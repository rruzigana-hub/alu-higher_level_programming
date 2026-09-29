#!/usr/bin/node
const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (!err) {
    const films = JSON.parse(body).results;
    let count = 0;
    for (const film of films) {
      if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
        count++;
      }
    }
    console.log(count);
  }
});
