#!/usr/bin/node

const request = require('request');
const url = 'https://swapi.dev/api/films/';
const movieId = process.argv[2];

request(`${url}${movieId}/`, (error, response, body) => {
  if (error) {
    return console.error('Error fetching movie data:', error);
  }
  if (response.statusCode !== 200) {
    return console.error(`Unexpected response status: ${response.statusCode}`);
  }

  const movie = JSON.parse(body);
  const characterUrls = movie.characters;

  characterUrls.forEach(url => {
    request(url, (charError, charResponse, charBody) => {
      if (charError) {
        return console.error('Error fetching character data:', charError);
      }

      const character = JSON.parse(charBody);
      console.log(character.name);
    });
  });
});
