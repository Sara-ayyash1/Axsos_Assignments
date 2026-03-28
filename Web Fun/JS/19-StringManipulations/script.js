//1. String.concat
//The String.concat() method is used to concatenate multiple strings together, adding them to the end of the existing string. This method returns a new string that is the combination of all the input strings.

let greeting = "Hello";
let name = "Alice";
let punctuation = "!";
let fullGreeting = greeting.concat(", ", name, punctuation);
console.log(fullGreeting); // Output: "Hello, Alice!"

////////////////////////////////////////////////

// 2. String.slice
// The String.slice() method extracts a portion of a string and returns it as a new string. It takes two arguments:
//Syntax:String.slice(start, end)

let text = "Hello, World!";
console.log(text.slice(7, 12)); // Output: "World"
console.log(text.slice(-6));    // Output: "World!"
console.log(text.slice(-6, -1)); // Output: "World"

////////////////////////////////////////////////

//3. String.trim
//The String.trim() method removes whitespace characters (spaces, tabs, newlines) from both ends of a string. It returns a new string without leading and trailing whitespace.

let messyString = " \n hello goodbye \t ";
console.log(messyString.trim()); // Output: "hello goodbye"

////////////////////////////////////////////////

//4. String.split
//The String.split() method splits a string into an array of substrings based on a specified separator. The optional limit parameter specifies the maximum number of splits to perform.
//Syntax:String.split(separator, limit)
// separator: The delimiter where the string is split. If an empty string "" is used, the string is split between every character.
// limit (optional): The maximum number of splits to perform. Any additional substrings after the limit are discarded.

let sentence = "Hello, World! How are you?";
console.log(sentence.split(" ")); // Output: ["Hello,", "World!", "How", "are", "you?"]
console.log(sentence.split(" ", 3)); // Output: ["Hello,", "World!", "How"]
console.log(sentence.split(""));    // Output: ["H", "e", "l", "l", "o", ",", " ", "W", "o", "r", "l", "d", "!", " ", "H", "o", "w", " ", "a", "r", "e", " ", "y", "o", "u", "?"]

////////////////////////////////////////////////

// 5. String.search
// The String.search() method searches a string for a specified value (substring) and returns the index position of the first occurrence. If the value is not found, it returns -1.
let phrase = "Hello, World!";
console.log(phrase.search("World")); // Output: 7
console.log(phrase.search("Universe")); // Output: -1