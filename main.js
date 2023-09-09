function getRandomID() {
  const randomDecimal = Math.random();
  const randomInRange = randomDecimal * (50 - 1) + 1;
  return Math.floor(randomInRange);
}

function AJAXexample() {
  // Create a new XMLHttpRequest object --> Objeto que se va a encargar de hacer la solicitud
  const id = getRandomID();
  const url = "https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0";
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
      console.log(responseData.results);
      console.log(responseData.results[0]);
      console.log(responseData.results[3]);
      console.log(responseData.results[5].name); //Saber nombre

      // Acá se asignaría la información al HTML
    } else {
      console.error("Request failed with status:", xhr.status);
    }
  };

  // Send the request
  xhr.send();
}

AJAXexample();
