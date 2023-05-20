document
  .getElementById("user-form")
  .addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent form submission

    // Retrieve form data
    var name = document.getElementById("name").value;
    var password = document.getElementById("password").value;
    var address = document.getElementById("address").value;
    var gameCheckboxes = document.querySelectorAll(
      'input[name="game"]:checked'
    );
    var games = Array.from(gameCheckboxes).map(function (checkbox) {
      return checkbox.value;
    });
    var gender = document.querySelector('input[name="gender"]:checked').value;
    var age = document.getElementById("age").value;
    var file = document.getElementById("file").files[0];

    // Perform validation or other processing as needed

    // Display form data (this is just an example)
    console.log("Name: " + name);
    console.log("Password: " + password);
    console.log("Address: " + address);
    console.log("Games: " + games.join(", "));
    console.log("Gender: " + gender);
    console.log("Age: " + age);
    console.log("File: " + (file ? file.name : "Not uploaded"));

    // Reset form
    this.reset();
  });
