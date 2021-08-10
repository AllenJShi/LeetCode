class Solution {
public:
    string addStrings(string num1, string num2) {
        int i = num1.length()-1, j = num2.length()-1, carry = 0;
        string ans = "";
        while(i>=0||j>=0||carry!=0){
            int x = i>=0 ? num1[i]-'0':0;
            int y = j>=0 ? num2[j]-'0':0;
            int numAns = x + y + carry;
            ans.push_back('0'+numAns%10);
            carry = numAns/10;
            i -=1; j-=1;
        }
        reverse(ans.begin(),ans.end());
        return ans;
    }
};