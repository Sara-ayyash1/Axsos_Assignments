//1. Reverse String =>Task:Implement a function reverseString(str) that takes a string as an input and returns the string with its characters reversed.
//Constraint:Do not use the built-in reverse() method.

function reverseString(str) {
    let reverseStr= "";
    for(let i = str.length-1  ; i >=0 ; i--){
      reverseStr+=str[i];
    }
    return reverseStr;
}
console.log(reverseString("creature")); // "erutaerc"

/////////////////////////////////////////////////

//2. Remove Even-Length Strings =>Task:Create a function that removes strings of even lengths from a given array. The function should modify the array in place, removing all strings that have an even number of characters.
function removeEvenLengthStrings(arr) {
    for (let i = arr.length - 1; i >= 0; i--) {
        if(arr[i].length % 2 === 0)
        {
            arr.splice(i,1);
        }
    }
    return arr;
}
let arr = ["Nope!", "Its", "Kris", "starting", "with", "K!", "(instead", "of", "Chris", "with", "C)", "."];
removeEvenLengthStrings(arr);
console.log(arr); // ["Nope!", "Its", "Chris", "."]

/////////////////////////////////////////////////

//3. Integer to Roman Numerals
//Task: Create a function that converts a given positive integer (less than 4000) into its Roman numeral representation. Roman numerals use the following symbols:

function intToRoman(num) {

    if (num <= 0 || num >= 4000) {
        return "Invalid: Number must be positive integer (less than 4000)";
    }

    const romanData = [
        { v: 1000, s: "M" }, { v: 900, s: "CM" },
        { v: 500,  s: "D" }, { v: 400, s: "CD" },
        { v: 100,  s: "C" }, { v: 90,  s: "XC" },
        { v: 50,   s: "L" }, { v: 49,  s: "IL" }, { v: 40,  s: "XL" },
        { v: 10,   s: "X" }, { v: 9,   s: "IX" },
        { v: 5,    s: "V" }, { v: 4,   s: "IV" },
        { v: 1,    s: "I" }
    ];

    let result = "";

    // الطرح المتكرر". نبدأ من أكبر قيمة (1000) ونطرحها من الرقم حتى يصفر، وفي كل مرة نطرح نكتب الحرف المقابل"
    for (let i = 0; i < romanData.length; i++) {
        while (num >= romanData[i].v) {
            result += romanData[i].s;
            num -= romanData[i].v;
        }
    }

    return result;
}

console.log(intToRoman(349));  // "CCCIL"
console.log(intToRoman(444));  // "CDXLIV"

/////////////////////////////////////////////////
//4. Roman Numerals to Integer
//Task:
//Write a function that converts a Roman numeral string into its corresponding integer value.
// The function should correctly interpret Roman numeral rules

function romanToInt(roman) {
    const values = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    };
 
    let result = 0;
 
    for (let i = 0; i < roman.length; i++) {
        // Now this look-up will actually find the number
        let currentVal = values[roman[i]];
        let nextVal = values[roman[i + 1]];
 
        if (nextVal > currentVal) {
            result -= currentVal;
        } else {
            result += currentVal;
        }
    }
 
    return result;
}
console.log(romanToInt("III"));    // 3
console.log(romanToInt("DCIX"));   // 609
console.log(romanToInt("MXDII"));  // 1492