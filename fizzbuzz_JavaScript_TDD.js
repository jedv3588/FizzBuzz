function isMultiple(num, mod){
  return num % mod === 0;
}

function main(){

  let output = "";

  for(let i = 1; i<=100; i++){

    switch(true){

        case isMultiple(i, 15):
            output = "FizzBuzz";
            break;

        case isMultiple(i, 3):
            output = "Fizz";
            break;

        case isMultiple(i, 5):
            output = "Buzz";
            break;

        default:
            output = i;
            break;
    }

  console.log(output);

 }

}


