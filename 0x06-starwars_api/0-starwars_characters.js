#!/usr/bin/node
const request = require('request');

// Get the Movie ID from command line argument
const movieId = process.argv[2];

// URL for the Star Wars API films endpoint
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  const movieData = JSON.parse(body);
  const characters = movieData.characters;

  // Loop through each character URL and fetch their name
  characters.forEach(characterUrl => {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error('Error:', charError);
        return;
      }
      const characterData = JSON.parse(charBody);
      console.log(characterData.name);
    });
  });
});
