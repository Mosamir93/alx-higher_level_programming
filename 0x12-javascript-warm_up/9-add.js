#!/usr/bin/node
const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);
const res = add(a, b);
console.log(res);
function add (a, b) {
  return a + b;
}
