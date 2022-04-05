#!/usr/bin/node
const Rectangle = require('./4-rectangle');

/**
 * Class Sqaure inherits from rectangle
 */

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    let row;
    for (let i = 0; i < this.height; i++) {
      row = '';
      for (let j = 0; j < this.width; j++) {
        row += c;
      }
      console.log(row);
    }
  }
}

module.exports = Square;
