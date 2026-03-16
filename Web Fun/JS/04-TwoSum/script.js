let nums = [3,2,4];
let target = 6;

// function TwoSum(nums , target){
//   let output=[];
//   for(let i=0; i<nums.length ; i++){  
//     for(let x=i+1; x<nums.length ; x++){
//       if(nums[i]+nums[x]==target){
//         output.push(i,x);
//         return output;
//       }
//     }
//   } 
// }

// var result = TwoSum(nums , target);
// console.log(result);

///////////////////////////////

function TwoSum(nums , target){
  let map = new Map();
  for(let i=0; i<nums.length ; i++){  
    let currentNum = nums[i];
    let neededNum = target - currentNum;

    if(map.has(neededNum)){
        return [map.get(neededNum),i];
    }

    map.set(currentNum,i);
  } 
}
var result = TwoSum(nums , target);
console.log(result);

//Here in the Question the Key is the number and value is index(position of the number)
//map.set(key,value); 
//map.has(key);  => return false or true
//map.get(key);  => return the value