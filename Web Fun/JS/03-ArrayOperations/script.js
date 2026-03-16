/* 1-Accessing Elements */
let colors = ["red", "blue", "green", "yellow", "purple"];
console.log(colors[0]);
console.log(colors[colors.length-1]);
console.log(colors[1]);
colors[2] = "orange";
console.log(colors);
/////////////////////////////////////////////////////////
/* 2-Traversing an Array */
let numbers = [10, 20, 30, 40, 50];
for (let i = 0; i < numbers.length; i++) {
  console.log(numbers[i]);
}
for (let i = numbers.length - 1; i >= 0; i--) {
  console.log(numbers[i]);
}
/////////////////////////////////////////////////////////
/* 3-Searching in an Array */
let numbers2 = [5, 10, 15, 20, 25];
if (numbers2.includes(25)) {
  console.log("Found at position "+numbers2.indexOf(25));
} else {
  console.log("Not Found");
}
/////////////////////////////////////////////////////////
/* 4-Sorting an Array */
let scores = [50, 20, 70, 10, 40];
scores.sort((a, b) => a - b);
console.log(scores);

scores.sort((a, b) => b - a);
console.log(scores);

let names = ["Shatha", "Sara", "Lina", "Sami", "Dalia"];
names.sort();
console.log(names);
/////////////////////////////////////////////////////////
/* 5-Inserting Elements */
let animals = ["dog", "cat", "rabbit"];
animals.push("elephant");
animals.unshift("lion");
animals.splice(2, 0, "tiger");
console.log(animals);
/////////////////////////////////////////////////////////
/* 6-Deleting Elements */
let fruits = ["apple", "banana", "cherry", "date"];
fruits.shift();
fruits.pop();
fruits.splice(fruits.indexOf("banana"), 1);
console.log(fruits);
/////////////////////////////////////////////////////////
/* 7-Combining Array */
let array1 = [1, 2, 3];
let array2 = [4, 5, 6];
let CombinArray = array1.concat(array2);
console.log(CombinArray);
/////////////////////////////////////////////////////////
/* 8-Splitting an Array */
let items = ["a", "b", "c", "d", "e"];
console.log(items.slice(0,3));
console.log(items.slice(3));
/////////////////////////////////////////////////////////
/* 9-Filtering Elements */
let numbers3 = [1, 5, 10, 15, 20, 25, 30];
let newNum = numbers3.filter((num) => num > 15);
console.log(newNum);
/////////////////////////////////////////////////////////
/* 10-Advanced Challenge */
let inputs = [1, 2, 2, 3, 4, 4, 5];
let uniqueInputs = [...new Set(inputs)];
console.log(uniqueInputs);

let n = 2;
let start = uniqueInputs.slice(-2);
let end = uniqueInputs.slice(0, uniqueInputs.length - n);
let rotate = start.concat(end);
console.log(rotate);
/////////////////////////////////////////////////////////
/* Bouns Challenge */
let arr1 = [1,2,3];
let arr2 = [4,5,6];
let output = [];
let pointer1 = 0;
let pointer2 = 0;

for (let i = 0; i<=arr1.length+arr2.length-1 ; i++){
  if(arr1[pointer1] < arr2[pointer2]){
    output.push(arr1[pointer1]);
    pointer1++;
  }
  else{
    output.push(arr2[pointer2]);
    pointer2++;
  }
}
console.log(output);
