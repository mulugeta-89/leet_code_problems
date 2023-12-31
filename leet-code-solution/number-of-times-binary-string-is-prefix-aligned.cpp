class Solution {
public:
    int numTimesAllBlue(vector<int>& flips) {
        int count; int counter; int sumi; int sol;
        count = counter = sumi = sol = 0;
        for(int i =0; i < flips.size();++i){
            sumi += flips[i];
            count += 1;
            counter += count;
            if(counter == sumi){
                sol += 1;
            }
        }
        return sol;
        
    }
};