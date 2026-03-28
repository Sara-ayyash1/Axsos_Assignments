//1-Coin Change with Object
//Given a number representing U.S. cents, return an object that represents the optimal
// number of coins (quarters, dimes, nickels, and pennies) needed to make that amount.

function coinChange(cents) {
  let result = {
    quarters: 0,
    dimes: 0,
    nickels: 0,
    pennies: 0,
  };

  result.quarters = Math.floor(cents / 25);
  cents %= 25;

  result.dimes = Math.floor(cents / 10);
  cents %= 10;

  result.nickels = Math.floor(cents / 5);
  cents %= 5;

  result.pennies = cents;

  return result;
}

console.log(coinChange(94));

//2- Max/Min/Average with Object
// Given an array of numbers, return an object containing the maximum value, minimum value, and the average of the array.

function maxMinAverage(arr) {
  let result = {
    maximum: 0,
    minimum: 0,
    average: 0,
  };
  result.maximum = Math.max(...arr);
  result.minimum = Math.min(...arr);

  let sum = 0;
  for (let i = 0; i < arr.length; i++) {
    sum += arr[i];
  }
  result.average = sum / arr.length;

  return result;
}
console.log(maxMinAverage([1, 2, 3, 4, 5]));
