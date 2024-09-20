#!/usr/bin/env node
const argv = process.argv.slice(2)
const film_id = argv[0]
const endpoint = `https://swapi-api.alx-tools.com/api/films/${film_id}`

async function getCharacters(_characters) {
    let characters = _characters
    await _characters.then(response => {
        characters = response
    })

    for (let character of characters) {
        await fetch(character)
        .then((response) => {
            return response.json()
        })
        .then((response) => {
            console.log(response.name)
        })
        .catch(() => {})

    }
}

async function getFilm(endpoint) {
    let characters;
    await fetch(endpoint)
    .then((response) => {
        return response.json()
    })
    .then((json) => {
        characters = json.characters
    })
    .catch()
    return characters;
}

async function allTogether() {
    getCharacters(getFilm(endpoint))
}

/* excute and boom */
allTogether()