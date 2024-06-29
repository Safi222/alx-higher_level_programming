#!/usr/bin/node

const dict = require('./101-data.js').dict;
const newDict = {};
for (const key in dict) {
  const val = dict[key];
  const arr = [];
  if (!(val in newDict)) {
    arr.push(key);
    newDict[val] = arr;
  } else { newDict[val].push(key); }
}
console.log(newDict);
