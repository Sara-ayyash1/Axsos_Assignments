// Always Hungry
// Create a function that takes an array as input. Whenever the function encounters the value "food" in the array, 
// it should log "yummy" to the console. If "food" is not found in the array, the function should log "I'm hungry" once.

function alwaysHungry(arr) {
    if (!arr.includes("food")) {
        console.log("I'm hungry");
        return;
    }

    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === "food") {
            console.log("yummy");
        }
    }
}
   
alwaysHungry([3.14, "food", "pie", true, "food"]);
alwaysHungry([4, 1, 5, 7, 2]);

////////////////////////////////////////////////

// High Pass Filter
// Given an array and a cutoff value, create a new array that includes only the values greater than the cutoff.

function highPass(arr, cutoff) {
    var filteredArr = [];
    for(let i = 0 ; i < arr.length; i++){
        if(arr[i] > cutoff){
            filteredArr.push(arr[i]);
        }
    }
    return filteredArr;
}
var result = highPass([6, 8, 3, 10, -2, 5, 9], 5);
console.log(result); 

////////////////////////////////////////////////

// Better than average
// When provided with an array of numbers, determine how many numbers in the array are greater than the average of the numbers in the array.
function betterThanAverage(arr) {
    var sum = 0;
    // calculate the average
    for(let i = 0 ; i < arr.length; i++){
        sum+=arr[i];
    }
    let avg = sum/arr.length;

    var count = 0
    // count how many values are greated than the average
    for(let i = 0 ; i < arr.length; i++){
        if(arr[i] > avg){
           count+=1;
        }
    }
    return count;
}
var result = betterThanAverage([6, 8, 3, 10, -2, 5, 9]);
console.log(result); 

////////////////////////////////////////////////

// Array Reverse
// Create a function that reverses the elements in an array and then returns the reversed array.

// function reverse(arr) {
//     let left = 0;
//     let right = arr.length - 1;
    
//     while(left < right) {
//         let temp = arr[left];
//         arr[left] = arr[right];
//         arr[right] = temp;
        
//         left++;
//         right--;
//     }
//     return arr;
// }
 function reverse(arr) {
  let reversed = [];
  for (let i = arr.length - 1; i >= 0; i--) {
    reversed.push(arr[i]);
  }

  return reversed;
}
console.log("result");
var result = reverse(["a", "b", "c", "d", "e"]);
console.log(result);
// let arr =["a", "b", "c", "d", "e"]
// console.log(arr.reverse())

////////////////////////////////////////////////

// Fibonacci Array
// Please create a function that can generate an array containing Fibonacci numbers up to a specified length n. 
// Fibonacci numbers are determined by adding together the last two values in the sequence. 

function fibonacciArray(n) {
    if(n <= 0) return [];
    if(n === 1) return [0];
    var fibArr = [0, 1];
    for (var i = 2; i < n; i++) {
        fibArr.push(fibArr[i-1] + fibArr[i-2]);
    }
    return fibArr;
}
   
var result = fibonacciArray(10);
console.log(result); 