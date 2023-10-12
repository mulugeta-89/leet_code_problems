public class Solution {
    public int SumOfSquares(int[] nums) {
        int total = 0;
        for(int i = 1; i < nums.Length+1; i++){
            if(nums.Length%i == 0)
                total += nums[i-1]*nums[i-1];
        }
        return total;
    }
}