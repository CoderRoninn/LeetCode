/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    const n = nums.length;
    const expectedSum  = n * (n + 1) / 2;
    let sum = 0;

    for(const number of nums){
        sum += number;
    }

    return expectedSum - sum;
    
};