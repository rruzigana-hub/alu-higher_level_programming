#!/usr/bin/node
const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (!err) {
    const films = JSON.parse(body).results;
    let count = 0;
    for (const film of films) {
      for (const character of film.characters) {
        if (character.includes('/people/18') || character.endsWith('/18/') || character.endsWith('/18')) {
          count++;
          break;
        }
      }
    }
    console.log(count);
  }
});
