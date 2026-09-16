class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ansh;
        for(int i =0;i<nums.size();i++){
            for(int j=0;j<i;j++){
                if (nums[i]+nums[j]==target){
                    ansh.push_back(i);
                    ansh.push_back(j);
                    return ansh;
                }
            }
        }
        return ansh;
    }

};