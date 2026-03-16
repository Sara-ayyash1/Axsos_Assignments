function pizzaOven(crust, sauce, cheese, toppings) {
  var pizza = {};
  pizza.crust = crust;
  pizza.sauce = sauce;
  pizza.cheese = cheese; 
  pizza.toppings = toppings;
  return pizza;
}

var p1 = pizzaOven("deep dish", "traditional", ["mozzarella"],["pepperoni", "sausage"])
console.log(p1);

var p2 = pizzaOven("hand tossed", "marinara", ["mozzarella", "feta"],  ["mushrooms", "olives", "onions"])
console.log(p2);

var p3 = pizzaOven("thin tossed", "white sauce", ["permesan"],["chicken"])
console.log(p3);

var p4 = pizzaOven("hand tossed", "barbecue", ["cheddar"],  ["ham","onions"])
console.log(p4);

/*Create a function called randomPizza that uses Math.random() to create a random pizza! */
function getRandomNumber(array) {
  return array[ Math.floor(Math.random() * array.length)];
}

function randomPizza() {
  var crusts = ["deep dish", "hand tossed", "thin tossed"];
  var sauces = ["traditional", "marinara", "white sauce", "barbecue"];
  var cheese = ["mozzarella", "feta", "permesan", "cheddar"];
  var toppings = ["pepperoni", "sausage", "mushrooms", "olives", "onions","chicken", "ham",];

  return pizzaOven(
    getRandomNumber(crusts),
    getRandomNumber(sauces),
    [getRandomNumber(cheese)],
    [getRandomNumber(toppings), getRandomNumber(toppings)],
  );
}
console.log("Random Pizza", randomPizza());
