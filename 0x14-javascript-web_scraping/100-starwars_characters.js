#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;
request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const characters = JSON.parse(body).characters;
  let actor;
  for (const character of characters) {
    request.get(character, (err, res, body) => {
      if (err) {
        console.log(err);
        return;
      }
      actor = JSON.parse(body).name;
      console.log(actor);
    });
  }
});
