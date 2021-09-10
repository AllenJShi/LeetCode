class Solution {
public:
    string shiftingLetters(string s, vector<int>& shifts) {
        
        /*
            this approach will cause too much memory and runtime when the string getting too large
        
        string ans = "";
        
        for(int j=0; j<s.size();j++){
            long long int subtotal = 0;
            for(int i=j;i<shifts.size();i++){
                subtotal += shifts[i];
            }
            
            int diff = 'z'-s.at(j);
            if(diff<subtotal){
                ans.push_back('a' + ((subtotal-diff-1)%26));
            }else{
                ans.push_back(s.at(j)+subtotal);    
            }
        }
        return ans;
        
        
        To reduce the iteration, we can start from the very end and keep record of the last shift incremental element and move backward then
        */
        
        int subtotal = 0;
        for (int i = s.size() - 1; i >= 0; i--){
            int diff = s[i] - 'a';
            if(i+1<s.size()){
                subtotal = (subtotal + shifts[i]) % 26;
            }else{
                subtotal = shifts[i];
            }
            s[i] = (diff + subtotal) % 26 + 'a';
        }
        return s;
    }
};