class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        // int n1 = word1.length();
        // int t = word1.length() < word2.length() ? word1.length() : word2.length();
        // string res="";
        // int i=0;
        // while(i < t){
        //     res += word1[0];
        //     res += word2[0];
        //     word2.erase(word2.begin());
        //     word1.erase(word1.begin());
        //     i++;
        // }
        
        // if(i==n1){
        //     res += word2;
        // }else{
        //     res += word1;
        // }
        
        // return res;

        //To optimize 
        int n1 = word1.length(), n2 = word2.length(), indx = 0;
        string res;
        while(indx < max(n1,n2)){
            if(indx < n1) res += word1[indx];
            if(indx < n2) res += word2[indx];
            indx++;
        }
        return res;
    }
};