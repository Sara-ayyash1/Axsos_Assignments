//1. Parens Valid
//Create a function that checks if a string has valid sets of parentheses.
// Valid parentheses must open before they close, and every opening parenthesis must have a corresponding closing one.
// Iterate through the string, using a counter to track the balance between open and close parentheses.
// Return false if you find a closing parenthesis before an opening one or if any parentheses are left unclosed at the end.

function parensValid(str) {
  let parentheses = 0;
  for (let i = 0; i < str.length; i++) {
    if (str[i] === "(") {
      parentheses++;
    } else if (str[i] === ")") {
      parentheses--;
    }
    if (parentheses < 0) {
      return false;
    }
  }
  return parentheses === 0;
}

console.log(parensValid("Y(3(p)p(3)r)s"));
console.log(parensValid("N(0(p)3"));
console.log(parensValid("N(0)t )0(k"));
//////////////////////////////////////////////

//2. Braces Valid
//Expand the concept from the previous challenge to include not just parentheses (), but also braces {}, and brackets [].
//The function should determine whether the entire sequence of parentheses, braces, and brackets is valid.
// Use a stack data structure to track opening symbols, and ensure each closing symbol matches the most recent opening one.

function bracesValid(str) {
  let stack = [];
  const matches = { ")": "(", "]": "[", "}": "{" };

  //We push openers, then pop and compare when we see a closer; if they don't match, we return false
  for (let char of str) {
    if (char === "(" || char === "[" || char === "{") {
      stack.push(char);
    } else if (char === ")" || char === "]" || char === "}") {
      let lastOpen = stack.pop();
      if (lastOpen !== matches[char]) {
        //Each closing bracket must match the last opened one using a Stack (LIFO).
        return false;
      }
    }
  }
  return stack.length === 0;
}
console.log(bracesValid("W(a{t}s[o(n{c}o)m]e)h[e{r}e]!"));
console.log(bracesValid("[(])"));
console.log(bracesValid("[sara])]"));
console.log(bracesValid("D(i{a}l[t]o)n{e"));

///////////////////////////////////////////////

// 3. Is Palindrome
// A palindrome is a string that reads the same forwards and backwards.
// Write a function that determines whether a string is a strict palindrome, considering all characters, including spaces, punctuation, and capitalization..
// For the strict version, compare characters from the beginning and end of the string, moving towards the center.
function Palindrome(str) {
  let start = 0;
  let end = str.length - 1;
  while (start < end) {
    if (str[start] !== str[end]) {
      return false;
    }
    start++;
    end--;
  }
  return true;
}
console.log(Palindrome("a x a"));
console.log(Palindrome("racecar"));
console.log(Palindrome("Dud"));
console.log(Palindrome("oho!"));
// Second Version:
// Modify the function to ignore spaces, punctuation, and capitalization.
// For the lenient version, clean the string by removing non-alphanumeric characters and converting everything to lowercase before comparison.
function PalindromeIgnore(str) {
  let cleanStr = str.toLowerCase().replace(/[^a-z0-9]/g, "");

  let start = 0;
  let end = cleanStr.length - 1;
  while (start < end) {
    if (cleanStr[start] !== cleanStr[end]) {
      return false;
    }
    start++;
    end--;
  }
  return true;
}
console.log(PalindromeIgnore("Able was I, ere I saw Elba"));
console.log(PalindromeIgnore("Dud"));
console.log(PalindromeIgnore("oho!s"));

///////////////////////////////////////////////

// 4. Longest Palindrome
// Expand on the palindrome concept by finding the longest palindromic substring within a given string.
// This challenge is not just about the entire string but also about identifying the longest sequence within it that reads the same forwards and backwards.
function longestPalindrome(str) {
  if (str.length < 1) return "";

  let longest = str[0];
  for (let i = 0; i < str.length; i++) {
    for (let j = i+1; j < str.length; j++) {
      const substring = str.substring(i, j );
      if (Palindrome(substring) && substring.length > longest.length) {
        longest = substring;
      }
    }
  }
  return longest;
}
console.log(longestPalindrome("what up, daddy-o?")); // "dad"
console.log(longestPalindrome("uh... not much")); // "u"
console.log(longestPalindrome("Yikes! my favorite racecar erupted!")); //"e racecar e"

// Second Version:
// Modify the function to ignore spaces, punctuation, and capitalization when searching for the longest palindromic substring.
// Use a nested loop to check every possible substring within the string, keeping track of the longest palindrome found. 
// For the lenient version, clean the string before checking for palindromic substrings, then map back to the original string to extract the correct segment.
function longestPalindromeIgnore(str) {
  let cleanChars = [];
  let originalIndices = [];

  //clean the string before checking for palindromic substrings
  for (let i = 0; i < str.length; i++) {
    if (/[a-z0-9]/i.test(str[i])) {
      cleanChars.push(str[i].toLowerCase());
      originalIndices.push(i); 
    }
  }

  if (cleanChars.length === 0) return "";

  let maxLen = 0;
  let start = 0;
  let end = 0;

  for (let i = 0; i < cleanChars.length; i++) {
    for (let j = i; j < cleanChars.length; j++) {
      let sub = cleanChars.slice(i, j + 1);
      
      if (Palindrome(sub) && sub.length > maxLen) {
        maxLen = sub.length;
        start = originalIndices[i];
        end = originalIndices[j];  
      }
    }
  }
  return str.slice(start, end + 1);
}
console.log(longestPalindromeIgnore("Hot puree eruption!")); // "t puree erupt"
console.log(longestPalindromeIgnore("Yikes! my favorite racecar erupted!")); // "e racecar e"