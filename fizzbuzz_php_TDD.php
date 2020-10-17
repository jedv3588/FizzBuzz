<?php
// Probando para hacer un PR
$max_num = 100;

    function fizz_buzz($n){

        $output = '';
        
            switch(true){

                case($n % 15 === 0):
                    $output .= "FizzBuzz"."\n";
                    break;
        
                case($n % 3 === 0 ):
                    $output .= "Fizz"."\n";
                    break;
        
                case($n % 5 === 0 ):
                    $output .= "Buzz"."\n";
                    break;
        
                default:
                    $output .= $n."\n";
                    break;
            }
        
        return $output;
    }

for($i = 1; $i <= $max_num; $i++){
    echo $i." ".fizz_buzz($i);
    }
?>
