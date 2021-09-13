class Solution {
public:
    int maxNumberOfBalloons(string text) {
        if(text.size()<7) return 0;
        map<char,int> ans;
        
        for(auto& item : text){
            ans[item] += 1;
        }
        
        return min({ans['a'],ans['b'],ans['l']/2,ans['o']/2,ans['n']});
    }
};