// 1. Is Word Alphabetical
// Given a string, this function checks whether all the letters in the string are in alphabetical order.

function isWordAlphabetical(str) {
    str = str.toLowerCase().replace(/[^a-z]/g, ''); // Remove non-letter characters and lowercase
    for (let i = 0; i < str.length - 1; i++) {
        if (str[i] > str[i + 1]) {
            return false;
        }
    }
    return true;
}

// Examples
console.log(isWordAlphabetical("facetiously")); // true
console.log(isWordAlphabetical("arseniously")); // false

//////////////////////////////////////////////////

// 2. D Gets Jiggy
// This function takes a name as input, strips off the first letter, capitalizes the rest, and then appends the first letter at the end in a specific format.
function dGetsJiggy(name) {
    if (name.length < 2) return "";
    let firstLetter = name[0];
    let newName = name.slice(1).toUpperCase();
    return newName + " to the " + firstLetter + "!";
}

// Example
console.log(dGetsJiggy("Dylan")); // "YLAN to the D!"

//////////////////////////////////////////////////

// 3. Common Suffix
// Given an array of words, this function returns the largest suffix common to all words.

function commonSuffix(words) {
    if (words.length === 0) return "";
    let suffix = words[0];
    for (let i = 1; i < words.length; i++) {
        while (words[i].indexOf(suffix) !== words[i].length - suffix.length) {
            suffix = suffix.slice(1);
            if (suffix.length === 0) return "";
        }
    }
    return suffix;
}

// Examples
console.log(commonSuffix(["deforestation", "citation", "conviction", "incarceration"])); // "tion"
console.log(commonSuffix(["nice", "ice", "baby"])); // ""

//////////////////////////////////////////////////

// 4. Book Index
// Given a sorted array of page numbers where a term appears, this function produces an index string with ranges.
function bookIndex(pages) {
    let index = "";
    for (let i = 0; i < pages.length; i++) {
        let start = pages[i];
        while (i < pages.length - 1 && pages[i] + 1 === pages[i + 1]) {
            i++;
        }
        let end = pages[i];
        if (start === end) {
            index += start + ", ";
        } else {
            index += start + "-" + end + ", ";
        }
    }
    return index.slice(0, -2);
}

// Example
console.log(bookIndex([1, 13, 14, 15, 37, 38, 70])); // "1, 13-15, 37-38, 70"

//////////////////////////////////////////////////

// 5. Drop the Mike
// This function trims leading and trailing whitespace, capitalizes the first letter of each word, and returns the modified string unless the string contains "Mike". If "Mike" is found, it returns "stunned silence".

function dropTheMike(str) {
    str = str.trim();
    if (str.toLowerCase().includes("mike")) {
        return "stunned silence";
    }
    return str.replace(/\b\w/g, char => char.toUpperCase());
}

// Examples
console.log(dropTheMike(" hello world ")); // "Hello World"
console.log(dropTheMike(" Hey Mike ")); // "stunned silence"