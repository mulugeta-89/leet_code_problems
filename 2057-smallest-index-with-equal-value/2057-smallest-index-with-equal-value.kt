class Solution {
    fun smallestEqual(nums: IntArray): Int {
        for(i in 0..nums.size-1){
            if(i%10 == nums[i]){
                return i
            }
        }
        return -1
    }
}