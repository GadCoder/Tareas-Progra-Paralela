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

AJAXexample();
