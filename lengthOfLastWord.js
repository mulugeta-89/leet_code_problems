/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    s1 = s.split(" ")
    for(let i =s1.length-1; i >= 0; i--){
        if(s1[i] != ""){
            return s1[i].length
        }
    }
};