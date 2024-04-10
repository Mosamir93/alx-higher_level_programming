#!/usr/bin/node
const dict = require('./101-data').dict;
function flip (dict) {
  return Object.keys(dict).reduce((acc, key) => {
    const value = dict[key];
    if (!Object.prototype.hasOwnProperty.call(acc, value)) {
      acc[value] = [];
    }
    acc[value].push(key);
    return acc;
  }, {});
}
const flipped = flip(dict);
console.log(flipped);
