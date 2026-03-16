/* 1-Display odd numbers from 1 to 20 */
for(let i=1 ; i<=20 ; i++){
    if(i%2 != 0){
        console.log(i)
    }
}

/* 2-Decresing multiple of 3 (numbers from 100 down to 0) */
for(let i=100; i >= 0 ; i--){
    if(i%3 == 0){
        console.log(i);
    }
}

for(let i=99; i >= 0 ; i-=3){
    //console.log(i);
}

/* 3-Print the given sequence 4 , 2.5 , 1 , -0.5 , -2 , -3.5 */
for(let i = 4 ; i >= -3.5 ; i-=1.5){
    console.log(i);
}

/* 4-Sigma from 1 to 100 */
var sum = 0;
for(let i=1; i <=100 ; i++){
    sum+=i;
}
console.log(sum);

/* 5-Factorial multiplies nums from 1 to 12 */
var product = 1;
for(let i=1; i <=12 ; i++){
    product*=i;
}
console.log(product);
