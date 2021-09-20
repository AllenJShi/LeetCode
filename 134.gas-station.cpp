/*
 * @lc app=leetcode id=134 lang=cpp
 *
 * [134] Gas Station
 */

// @lc code=start
class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int n = gas.size();
        
        for(int i=0; i<n;i++){
            int tank = gas[i];
            if(tank<0) continue;
            int j=i;
            while(tank-cost[j]>=0){
                tank += gas[(j+1)%n]-cost[j];
                j = (++j)%n;
                if(j==i) return i;
             }
             if(j<i) return -1;

             //here means j does not even walk to n
             i=j;
        }

        return -1;
    }
};
// @lc code=end

