#!/usr/bin/env node

// problem: return bool if input str is palidromatic
// solution: clean str with replace, split, reverse, join, compare

let s = 'anna'

s = s.toLowerCase();
let str = s.replace(/[^a-z0-9]/gi, '');
let strReverse = str.split('').reverse().join('');

console.log(str === strReverse);
