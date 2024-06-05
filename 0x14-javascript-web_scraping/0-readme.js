#!/usr/bin/node

// Import the 'fs' module to interact with the file system
const fs = require('fs');

// Retrieve the file path from the command-line arguments
const file = process.argv[2];

// Read the file with UTF-8 encoding
fs.readFile(file, 'utf-8', (error, data) => {
  if (error) {
// Print the error if any occurs
    console.error('Error reading file:', error);
    return;
  }
// Print the file content to the console
  console.log(data);
});
