/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getConcatenation = function(nums) {
    const n = nums.length;
    let ans = new Array(2 * n);

    for(let i=0; i<n; i++){
        ans[i] = nums[i];
        ans[i+n] = nums[i];
    }

    return ans;
    
    
};