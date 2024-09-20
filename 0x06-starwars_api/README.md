# Star Wars API

>question: Write a script that prints all characters of a Star Wars movie ([star wars api](https://swapi-api.alx-tools.com/)):
>
  > - The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”
  > - Display one character name per line in the same order as the “characters” list in the /films/ endpoint
  > - You must use the Star wars API
  > - You must use the request module

>goal: the goal is to use the old way of making request with the deprecated request module.

>main goal: The main goal is to demostrate your knowledge of writing asyncronous code with js inorder to keep the order in which the data is in the api in your result.

## Pseudocode
```
fetch film:
  extract characters array in film
    loop in characters
      fetch character on at a time 
```

## solution
> [request module](0-starwars_characters.js)
> 
> [with fetch](with_fetch.js)
