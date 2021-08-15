class Solution {
        unordered_map<char,string> keyboard{
            {'2',"abc"},
            {'3',"def"},
            {'4',"ghi"},
            {'5',"jkl"},
            {'6',"mno"},
            {'7',"pqrs"},
            {'8',"tuv"},
            {'9',"wxyz"}
        };
public:
    vector<string> letterCombinations(string digits) {
        if(digits.empty()){
            return {};
        }
        vector<string> ans;
        string combo;
        backtrack(ans, digits, 0, combo);
        return ans;
    }
    
    void backtrack(vector<string>& ans, string& digits, int index, string& combo){
        if(index == digits.size()){
            ans.push_back(combo);
        }else{
            char digit = digits[index];
            const string& values = keyboard.at(digit);
            for(const char& value:values){
                combo.push_back(value);
                backtrack(ans, digits, index+1, combo);
                combo.pop_back();
            }
        }
    }
};