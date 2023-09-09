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
      console.log(responseData); //Todos los datos en la consola
      //console.log(responseData.abilities[0].ability.name); //Nombre y Habilidades
      document.getElementById("nombrePokemon").innerText =
        responseData.name.toUpperCase();
      document.getElementById("habilidadPokemon").innerText =
        responseData.abilities[0].ability.name.toUpperCase();
      document.getElementById("expPokemon").innerText =
        responseData.base_experience;
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

function setInnerText(elementID, innerText) {
  const element = document.getElementById(elementID);
  element.innerText = innerText;
}

function AJAXstarwars() {
  // Create a new XMLHttpRequest object
  const id = getRandomID();
  const url = "https://swapi.dev/api/people/" + id;
  //console.log(url);
  var xhr = new XMLHttpRequest();

  // Configure the request (GET request to a JSON endpoint)
  xhr.open("GET", url, true);

  // Define the callback function to handle the response
  xhr.onload = function () {
    if (xhr.status === 200) {
      // Parse the JSON response
      var responseData = JSON.parse(xhr.responseText);
      console.log(responseData);
      setInnerText("nombreStarWars", responseData["name"]);
      setInnerText("alturaSW", responseData["height"]);
      setInnerText("pesoSW", responseData["mass"]);

      document.getElementById("expPokemon").innerText =
        responseData.base_experience;
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

document.getElementById("obtenerPersonajes").addEventListener("click", () => {
  AJAXstarwars();
  AJAXpokemon();
});
