#!/usr/bin/node

const request = require('request');
const id = 18
const characterurl = `https://swapi-api.alx-tools.com/api/people/${id}/`;
const url = process.argv[2];
request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  if (response.statusCode === 200) {
    const movies = JSON.parse(body).results;
    let count = 0;
    for (const movie of movies) {
      if (movie.characters.includes(characterurl)) {
        count++;
      }
    }
    console.log(count);
  }
});
