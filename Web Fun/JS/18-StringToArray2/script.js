// 1. Zip Arrays into Map
// An associative array (or map) is a data structure where each key maps to a specific value. In this task, we are given two arrays,
// and our goal is to create a map where the elements of the first array serve as the keys, and the corresponding elements of the second array serve as the values.

function zipArraysIntoMap(keysArray, valuesArray) {
    let map = {};
    for (let i = 0; i < keysArray.length; i++) {
        map[keysArray[i]] = valuesArray[i];
    }
    return map;
}

let arr1 = ["abc", 3, "yo"];
let arr2 = [42, "wassup", true];

console.log(zipArraysIntoMap(arr1, arr2)); 

///////////////////////////////////////////////////////////

// 2. Invert Hash
// In an associative array, the key represents a value, and the value is associated with that key. In this task,
//  we will swap the keys and values of the associative array.

function invertHash(obj) {
    let inverted = {};
    for (let key in obj) {
        inverted[obj[key]] = key;
    }
    return inverted;
}

let assocArr = { "name": "Zaphod", "charm": "high", "morals": "dicey" };
console.log(invertHash(assocArr)); 

///////////////////////////////////////////////////////////

// 3. Number of Values (without .length)
// Typically, we use the .length property to determine the size of arrays. However, objects do not have a .length property,
// and their keys are unordered. To count the number of values in an associative array, we can manually iterate over the object and count the keys.
function countValues(obj) {
    let count = 0;
    for (let key in obj) {
        count++;
    }
    return count;
}

let bandInfo = {
    band: "Travis Shredd & the Good Ol’ Homeboys",
    style: "Country/Metal/Rap",
    album: "668: The Neighbor of the Beast"
};
console.log(countValues(bandInfo)); 