/**
 * @param {number} n
 * @return {number}
 */
var fib = function(n) {

    if(n === 0){
        return 0;
    }
    if(n === 1){
        return 1;
    }

    let firstElement = 0;
    let secondElement = 1;
    let result = 0;

    for(let i=2; i<=n; i++){
        result = firstElement + secondElement;
        firstElement = secondElement;
        secondElement = result;
    }

    return result;
    
};