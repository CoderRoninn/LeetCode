/**
 * @param {number} celsius
 * @return {number[]}
 */
var convertTemperature = function(celsius) {

    //Declare kelvin and fahrenheit
    const kelvin = celsius + 273.15;
    const fahrenheit = celsius * 1.80 + 32.00;

    //Declare an empty array of size 2 and put kelvin and hafrenheit values into it
    const ans =  [];
    ans.push(kelvin);
    ans.push(fahrenheit);

    //Return ans array
    return ans;
    
};