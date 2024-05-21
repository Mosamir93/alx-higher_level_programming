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
  const printCharacters = (index) => {
    if (index === characters.length) {
      return;
    }
    const characterUrl = characters[index];
    request.get(characterUrl, (err, res, body) => {
      if (err) {
        console.log(err);
        return;
      }
      const character = JSON.parse(body).name;
      console.log(character);
      printCharacters(index + 1);
    });
  };
  printCharacters(0);
});
