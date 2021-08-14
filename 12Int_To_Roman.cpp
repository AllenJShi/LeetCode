class Solution {
public:
    string intToRoman(int num) {
        int integers[] = {1000,900,500,400,100,90,50,40,10,9,5,4,1};
        string romans[] = {"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};
        string ans = "";
        for(int i = 0; i<size(integers); i++){
            while(num>=integers[i]){
                ans = ans + romans[i];
                num = num - integers[i];
            }
        }
        return ans;
    }
};