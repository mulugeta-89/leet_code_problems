class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        int n = nums.size();
        vector<int>arr2(2*n, 0);
        for(int i = 0;i < n; i++){
            arr2[i] = nums[i];
            arr2[i+n] = nums[i];
        }
        return arr2;
    }
};