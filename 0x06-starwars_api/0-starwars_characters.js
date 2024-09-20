#!/usr/bin/env node
const argv = process.argv.slice(2);
const filmId = argv[0];
const endpoint = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

fetch(endpoint)
  .then((response) => {
    return response.json();
  })
  .then(data => {
    if (data.characters !== undefined) {
      async function getCharacter (characters) {
        for (const character of characters) {
          await fetch(character)
            .then(response => {
              return response.json();
            })
            .then(data => {
              console.log(data.name);
            }).catch(() => {});
        }
      }
      getCharacter(data.characters);
    }
  })
  .catch(() => {});
