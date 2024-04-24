#!/usr/bin/node
class Rectangle {
	constructor (w, h) {
		if (w <= 0 || h <= 0) {
			return {}; // Return an empty object if w or h is not positive
		} else {
			this.width = w;
			this.width = h;
		}
	}
}
module.exports = Rectangle;
