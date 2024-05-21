#!/usr/bin/node

const request = require('request');
const id = 18;
const character = `/api/people/${id}/`;
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
      if (movie.characters.find(el => el.includes(character))) {
        count++;
      }
    }
    console.log(count);
  }
});
