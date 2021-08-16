class Solution {
public:
    int strStr(string haystack, string needle) {\
        //when needle is empty, return 0 directly
        if(needle.size() == 0){
            return 0;
        }
        
        //when not empty, do the following:
        int n = haystack.size(), m = needle.size();
        //create a next array and set it up for use
        int next[m];
        next[0] = 0;
        for(int i=1, j=0; i<m; i++){
            while(j>0 && needle[i]!=needle[j]){
                j = next[j-1];
            }
            if(needle[i]==needle[j]){
                j++;
            }
            next[i] = j;
        }
                                                
        //loop the haystack
        for(int i=0, j=0; i<n; i++){
            while(j>0 && haystack[i]!=needle[j]){
                j = next[j-1];
            }
            if(haystack[i]==needle[j]){
                j++;
            }
            if(j==m){
                return i-m+1;
            }
        }
        return -1;
    }
};