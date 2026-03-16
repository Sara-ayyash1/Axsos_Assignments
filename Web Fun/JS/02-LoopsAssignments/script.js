/*Print Numbers from 1 to 10*/ 
for (let i =1; i<=10; i++){
   console.log(i);
}

/*Reverse Counting from 10 to 1 */
for(let i =10; i >=1; i--){
   console.log(i);
}

/*Even Numbers between 1 and 20 */
for(let i=1; i<=20; i++){
    if(i%2 == 0){
        console.log(i);
    }
}

/*Odd Numbers between 1 and 20 */
for(let i=1; i<=20; i++){
    if(i%2 != 0){
        console.log(i);
    }
}

/*Sum Numbers between 1 and 10 */
let sum =0;
for(let i=1; i<=10 ; i++){
    sum += i;
}
console.log(sum);

/*FuzzBuzz from 1 to 30*/
for (i = 1; i <= 30; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
      console.log("FizzBuzz");
    } 
    else if (i % 3 === 0) {
      console.log("Fizz");
    } 
    else if (i % 5 === 0) {
      console.log("Buzz");
    } 
    else {
      console.log(i);
    }
}
