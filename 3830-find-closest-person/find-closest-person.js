/**
 * @param {number} x
 * @param {number} y
 * @param {number} z
 * @return {number}
 */
var findClosest = function(x, y, z) {

    let distanceX, distanceY;

    distanceX = Math.abs(x-z);
    distanceY = Math.abs(y-z);

    if(distanceX > distanceY){
        return 2;
    } else if(distanceX < distanceY){
        return 1;
    }else{
        return 0;
    }
};