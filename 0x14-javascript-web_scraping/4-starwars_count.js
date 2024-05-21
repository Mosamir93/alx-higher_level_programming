#!/usr/bin/node

const request = require('request');
const character = 'https://swapi-api.alx-tools.com/api/people/18/';
const url = process.argv[2];
function countMovies (url, character) {
  request.get(url, (err, response, body) => {
    if (err) {
      console.log(err);
      return;
    }
    const movies = JSON.parse(body).results;
    let count = 0;
    for (const movie of movies) {
      if (movie.characters.includes(character)) {
        count++;
      }
    }
    console.log(count);
  });
}
countMovies(url, character);
