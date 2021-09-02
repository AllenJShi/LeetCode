
// 构建一个flag变量来提示是否最后一个单词后面有空格，
// 如果是空格flag一直为false，for loop会一直跳过；如果不是最后一个空格，
// 则开始定位tail所在的位置，同时将flag调成true，表示一条过所有末尾空格，
// 第一个if条件功能完成；在第二个if条件中，若已知flag跳过末尾空格，再次碰到
// 的第一个空格将是最后一个单词的开头，长度即为tail-i；如果游历了一遍
// string，则只有一个单词，长度为tail+1，因为i从size-1开始

class Solution {
public:

    int lengthOfLastWord(string s) {
        bool flag = false;
        int tail;
        for(int i=s.size()-1;i>=0;i--){
            if(!flag && s[i]!=' '){
                flag = true;
                tail = i;
            }
            if(flag && s[i]==' '){
                return tail-i;
            }
        }
        return tail+1;
    }
};