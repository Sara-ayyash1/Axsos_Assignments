//Do not use built-in methods unless specifically instructed.
//1. Remove Blanks => Task:Create a function that removes all spaces from a given string.
function removeBlanks(str) {
  let newStr = "";
  for (let i = 0; i < str.length; i++) {
    if (str[i] !== " ") {
      newStr += str[i];
    }
  }
  return newStr;
}

console.log(removeBlanks(" Pl ayTha tF u nkyM usi c "));
console.log(removeBlanks("I can not BELIEVE it's not BUTTER"));

//////////////////////////////////////////////

//2. Get Digits => Task:Create a function that extracts and returns the digits from a given string as an integer.
//Allowed Methods: =>  isNaN() ,Number(): is used to ensure the final result is an integer, not a string.
function getDigits(str) {
  let digits = "";
  for (let i = 0; i < str.length; i++) {
    if (str[i] !== " " && !isNaN(str[i])) {
      digits += str[i];
    }
  }
  return Number(digits);
}

console.log(getDigits("abc8c0d1ngd0j0!8"));
console.log(getDigits("0s1a3 y5w7h9a2t4?6!8?0"));

//////////////////////////////////////////////

// 3. Acronyms => Task:Create a function that converts a given string into its acronym. The acronym should consist of the first letter of each word, capitalized.
// Allowed Methods:=> .split() ,.toUpperCase()
function acronym(str) {
  let words = str.split(" ");
  let result = "";
  for (let i = 0; i < words.length; i++) {
    if (words[i].length > 0) {
      result += words[i][0];
    }
  }
  return result.toUpperCase();
}

console.log(acronym(" there's no free lunch - gotta pay yer way. ")); // Output: "TNFL-GPYW"
console.log(acronym("Live from New York, it's Saturday Night!")); // Output: "LFNYISN"

//////////////////////////////////////////////
//4. Count Non-Spaces => Task:Create a function that counts and returns the number of non-space characters in a given string.

function countNonSpaces(str) {
    let count = 0;
    for (let i = 0; i < str.length; i++) {
        // If the character is NOT a space, count it
        if (str[i] !== " ") {
            count++;
        }
    }
    return count;
}
console.log(countNonSpaces("Honey pie, you are driving me crazy")); // Output: 29
console.log(countNonSpaces("Hello world !")); // Output: 11

//////////////////////////////////////////////

//5. Remove Shorter Strings => Task:Create a function that filters an array of strings, returning only those strings that have a length greater than or equal to a specified value.
function removeShorterStrings(arr, minLength) {
    let newArr = [];
  for(let  i =0 ; i< arr.length; i++){
    if(arr[i].length >= minLength){
        newArr.push(arr[i]);
    }
  }
  return newArr;
}
console.log(removeShorterStrings(["Good morning", "sunshine", "the", "Earth", "says", "hello"],4,));
console.log(removeShorterStrings(["There", "is", "a", "bug", "in", "the", "system"], 3));