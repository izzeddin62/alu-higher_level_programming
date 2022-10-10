#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], (err, response, body) => {
  if (err) console.log(err);
  console.log(JSON.parse(body).results.filter(el => el.characters.includes('https://swapi-api.hbtn.io/api/people/18/')).length);
});
