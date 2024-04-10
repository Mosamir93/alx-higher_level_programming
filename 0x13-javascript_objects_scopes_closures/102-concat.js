#!/usr/bin/node
const file1 = process.argv[2];
const file2 = process.argv[3];
const dest = process.argv[4];
const fs = require('fs');
const data1 = fs.readFileSync(file1, 'utf8');
const data2 = fs.readFileSync(file2, 'utf-8');
fs.writeFileSync(dest, data1 + data2);
