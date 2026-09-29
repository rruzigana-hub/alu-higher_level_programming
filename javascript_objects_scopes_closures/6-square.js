#!/usr/bin/node
const Square = require('./5-square');

class NewSquare extends Square {
  charPrint (c) {
    const char = c === undefined ? 'X' : c;
    for (let i = 0; i < this.height; i++) {
      let line = '';
      for (let j = 0; j < this.width; j++) {
        line += char;
      }
      console.log(line);
    }
  }
}

module.exports = NewSquare;
