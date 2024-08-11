#!/usr/bin/node

const request = require('request');
const url = 'https://swapi.dev/api/films/';
const movieId = process.argv[2];

const fetchCharacter = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        return reject(error);
      }

      try {
        const character = JSON.parse(body);
        resolve(character.name);
      } catch (Error) {
        return console.error('Failed to parse movie data:', Error);
      }
    });
  });
};

request(`${url}${movieId}/`, (error, response, body) => {
  if (error) {
    return console.error('Error fetching movie data:', error);
  }
  if (response.statusCode !== 200) {
    return console.error(`Unexpected response status: ${response.statusCode}`);
  }

  const movie = JSON.parse(body);
  const characterUrls = movie.characters;
  Promise.all(characterUrls.map(fetchCharacter))
    .then(characters => {
      characters.forEach(character => console.log(character));
    });
});
