function getRandomID() {
  const randomDecimal = Math.random();
  const randomInRange = randomDecimal * (50 - 1) + 1;
  return Math.floor(randomInRange);
}

function AJAXexample() {
  // Create a new XMLHttpRequest object
  const id = getRandomID();
  const url = "https://swapi.dev/api/people/" + id;
  console.log(url);
  var xhr = new XMLHttpRequest();

  // Configure the request (GET request to a JSON endpoint)
  xhr.open("GET", url, true);

  // Define the callback function to handle the response
  xhr.onload = function () {
    if (xhr.status === 200) {
      // Parse the JSON response
      var responseData = JSON.parse(xhr.responseText);
      console.log(responseData);

      // Acá se asignaría la información al HTML
    } else {
      console.error("Request failed with status:", xhr.status);
    }
  };

  // Send the request
  xhr.send();
}

function setInnerText(elementID, innerText) {
  const element = document.getElementById(elementID);
  element.innerText = innerText;
}

function AJAXpokemon() {
  // Create a new XMLHttpRequest object
  const id = getRandomID();
  const url = "https://pokeapi.co/api/v2/pokemon/" + id;
  //console.log(url);
  var xhr = new XMLHttpRequest();

  // Configure the request (GET request to a JSON endpoint)
  xhr.open("GET", url, true);

  // Define the callback function to handle the response
  xhr.onload = function () {
    if (xhr.status === 200) {
      // Parse the JSON response
      var responseData = JSON.parse(xhr.responseText);
      //console.log(responseData.abilities[0].ability.name); //Nombre y Habilidades
      setInnerText("nombrePokemon", responseData.name.toUpperCase());
      setInnerText(
        "habilidadPokemon",
        responseData.abilities[0].ability.name.toUpperCase()
      );
      setInnerText("expPokemon", responseData.base_experience);
      document.getElementById("imgPokemon").src =
        responseData["sprites"]["other"]["official-artwork"]["front_shiny"];

      // Acá se asignaría la información al HTML
    } else {
      console.error("Request failed with status:", xhr.status);
    }
  };

  // Send the request
  xhr.send();
}

function AJAXdigimon() {
  // Create a new XMLHttpRequest object
  const id = getRandomID();
  const url = "https://digimon-api.com/api/v1/digimon/" + id;
  var xhr = new XMLHttpRequest();

  // Configure the request (GET request to a JSON endpoint)
  xhr.open("GET", url, true);

  // Define the callback function to handle the response
  xhr.onload = function () {
    if (xhr.status === 200) {
      // Parse the JSON response
      var responseData = JSON.parse(xhr.responseText);
      /*
      document.getElementById("nombreDigimon").innerText = responseData.name;
      document.getElementById("tipoDigimon").innerText =
        responseData.types[0].type;
      document.getElementById("habilidadDigimon").innerText =
        responseData.skills[0].skill;*/
      setInnerText("nombreDigimon", responseData.name.toUpperCase())
      setInnerText("tipoDigimon", responseData.types[0].type)
      setInnerText("habilidadDigimon", responseData.skills[0].skill)
      document.getElementById("imagenDigimon").src =
        responseData.images[0].href;

      // Acá se asignaría la información al HTML
    } else {
      console.error("Request failed with status:", xhr.status);
    }
  };

  // Send the request
  xhr.send();
}

function AJAXnaruto() {
  // Create a new XMLHttpRequest object
  const id = getRandomID();
  const url = "https://www.narutodb.xyz/api/character/" + id;
  console.log(url);
  var xhr = new XMLHttpRequest();

  // Configure the request (GET request to a JSON endpoint)
  xhr.open("GET", url, true);

  // Define the callback function to handle the response
  xhr.onload = function () {
    if (xhr.status === 200) {
      var responseData = JSON.parse(xhr.responseText);
      console.log(responseData);
      setInnerText("nombreNaruto", responseData.name);
    } else {
      console.error("Request failed with status:", xhr.status);
    }
  };
  // Send the request
  xhr.send();
}

document.getElementById("obtenerPersonajes").addEventListener("click", () => {
  AJAXpokemon();
  AJAXdigimon();
  AJAXnaruto();
});
