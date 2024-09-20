#!/usr/bin/node

const argv = process.argv.slice(2);
const filmId = argv[0];
const request = require('request');

request(`https://swapi-api.alx-tools.com/api/films/${filmId}`, { json: true }, (err, res, body) => {
  if (!err && res.statusCode === 200) {
    const characters = body.characters;
    const fetchCharacter = (characterUrl) => {
      return new Promise((resolve, reject) => {
        request(characterUrl, { json: true }, (err, res, body) => {
          if (!err && res.statusCode === 200) {
            resolve(body);
          }
        });
      });
    };

    async function fetchData () {
      for (const character of characters) {
        const res = await fetchCharacter(character);
        console.log(res.name);
      }
    }
    fetchData();
  }
});
