class Solution {
public:
    string longestPalindrome(string s) {
//         int n = s.size();
//         if(n<2) return s;
        
//         int max = 1;
//         int start = 0;
        
//         vector<vector<int>> p(n, vector<int>(n));
//         for(int i=0; i<n; i++){
//             p[i][i] = true;
//         }
        
//         for(int l=2; l<=n; l++){
//             for(int i=0; i<n; i++){
//                 int j=l+i-1;
//                 if(j>=n) break;
                
//                 if(s[i]!=s[j]){
//                     p[i][j] = false;
//                 }else{
//                     if(j-i<3) p[i][j]=true;
//                     else p[i][j] = p[i+1][j-1];
//                 }
                
//                 if(p[i][j] && j-i+1>max){
//                     max = j-i+1;
//                     start = i;
//                 }
//             }
//         }
//         return s.substr(start,max);
        
        
        int n = s.size();
        if(n<2) return s;
        int leftmost = 0;
        int rightmost = 0;
        int maxLen = 1;
        
        vector<vector<bool>> dp(n,vector<bool>(n));
        
        for(int r=1; r<n; r++){
            for(int l=0; l<r; l++){
                if(s[r]==s[l] && (r-l<3 || dp[l+1][r-1])){
                    dp[l][r] = true;
                    if(r-l+1>maxLen){
                        maxLen = r-l+1;
                        leftmost = l;
                        rightmost = r;
                    }
                }
            }
        }
        return s.substr(leftmost,maxLen);
    }
};