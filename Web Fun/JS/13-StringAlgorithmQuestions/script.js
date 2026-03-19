//1. Reverse a String
function reverseString(str) {
  let reversed = "";
  for (let i = str.length - 1; i >= 0; i--) {
    reversed += str[i];
  }

  return reversed;
}
console.log(reverseString("hello"));

//2. Count Vowels
function countVowels(str) {
  let count = 0;
  let lowerStr = str.toLowerCase();

  for (let i = 0; i < lowerStr.length; i++) {
    let char = lowerStr[i];

    if (
      char === "a" ||
      char === "e" ||
      char === "i" ||
      char === "o" ||
      char === "u"
    ) {
      count++;
    }
  }
  return count;
}
console.log(countVowels("hello"));

//3. Check Palindrome
function isPalindrome(str) {
  let reversed = "";

  // for (let i = str.length - 1; i >= 0; i--) {
  //     reversed += str[i];
  // }
  reversed = reverseString(str);

  if (str === reversed) {
    return true;
  }
  return false;
}
console.log(isPalindrome("madam"));
console.log(isPalindrome("hello"));

//4. Longest Word in a Sentence
function findLongestWord(sentence) {
  let words = sentence.split(" ");
  let longest = "";

  for (let i = 0; i < words.length; i++) {
    let currentWord = words[i];
    if (currentWord.length > longest.length) {
      longest = currentWord;
    }
  }
  return longest;
}
console.log(findLongestWord("I love solving algorithms"));

////////////////////////////////////////////
//String Algorithm Questions Using Switch Statements
//1:Convert a Letter Grade to Feedback
function getFeedback(grade) {
  let upperGrade = grade.toUpperCase();
  let result = "";

  switch (upperGrade) {
    case "A":
      result = "Excellent";
      break;
    case "B":
      result = "Good job";
      break;
    case "C":
      result = "You passed";
      break;
    case "D":
      result = "Need improvement";
      break;
    case "F":
      result = "Failed";
      break;
    default:
      result = "Invalid grade";
  }

  return result;
}

console.log(getFeedback("a"));
console.log(getFeedback("C"));

//2. Count Character Types in a String
function countCharacterTypes(str) {
  let counts = {
    vowels: 0,
    digits: 0,
    spaces: 0,
    others: 0,
  };

  for (let i = 0; i < str.length; i++) {
    let char = str[i].toLowerCase();
    switch (char) {
      case "a":
      case "e":
      case "i":
      case "o":
      case "u":
        counts.vowels++;
        break;
      case "0":
      case "1":
      case "2":
      case "3":
      case "4":
      case "5":
      case "6":
      case "7":
      case "8":
      case "9":
        counts.digits++;
        break;
      case " ":
        counts.spaces++;
        break;
      default:
        counts.others++;
    }
  }
  return counts;
}

console.log(countCharacterTypes("Hi 123!"));
