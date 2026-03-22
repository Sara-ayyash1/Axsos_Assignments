var longestCommonPrefix = function(strs) {
    if (strs.length === 0) return "";

    for (let i = 0; i < strs[0].length; i++) {
        let char = strs[0][i]; 
 
        for (let j = 1; j < strs.length; j++) {
            if (strs[j][i] !== char) {
                return strs[0].substring(0, i);
            }
        }
    }
    return strs[0];
};

let strs = ["flower","flow","flight"]
console.log(longestCommonPrefix(strs));

let strs2 = ["dog","racecar","car"]
console.log(longestCommonPrefix(strs2));

// let strs3 = ["dog","d"]
// console.log(longestCommonPrefix(strs3));

// let strs4 = []
// console.log(longestCommonPrefix(strs4));


// let strs5 = [""]
// console.log(longestCommonPrefix(strs5));