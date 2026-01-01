/**
 * @param {string[]} operations
 * @return {number}
 */
var finalValueAfterOperations = function(operations) {
    let output = 0;
    const len = operations.length;

    for(let i=0; i<len; i++){
        if(operations[i] == "++X"){
            output++;
        }else if(operations[i] == "X++"){
            output++;
        }else if(operations[i] == "--X"){
            output--;
        }else{
            output--;
        }
    }
    return output    
};