/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function(x) {

    // Declare 2 variable named left and right for binary search
    let left = 0;
    let right = x;
    
    // The loop will continue as long as right is grater then left value 
    while(left <= right){
        //Declare middle variable and assign middle of the number line
        let middle = Math.floor((left + right) / 2);
        
        if(middle * middle === x){
            return middle;
        }
        //If x is grater then middle point we assign middle value + 1 to left
        else if(middle * middle < x){
            left = middle + 1;
        }
        //If x is less than middle point we assign middle value - 1 to right
        else{
            right = middle - 1;
        }
    }
    // In the last iteration right will be less then left so we are looking for rounded down value
    return right;


    
};