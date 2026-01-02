/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    const originalNumber = x;
    let modifiedNumber = 0;

    while(x > 0){
        modifiedNumber = 10 * modifiedNumber + (x % 10);
        x = Math.floor(x / 10);
    }

    return modifiedNumber === originalNumber;
    
};