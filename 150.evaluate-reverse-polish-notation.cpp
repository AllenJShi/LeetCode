/*
 * @lc app=leetcode id=150 lang=cpp
 *
 * [150] Evaluate Reverse Polish Notation
 */

// @lc code=start

class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> stack;
        int n = tokens.size();
        for (int i=0; i<n; i++){
            string& token = tokens[i];
            if (isNumber(token)){
                stack.push(atoi(token.c_str()));
            } else{
                int num2 = stack.top();
                stack.pop();
                int num1 = stack.top();
                stack.pop();

                switch (token[0]) {
                    case '+':
                        stack.push(num1+num2);
                         break;
                    case '-':
                        stack.push(num1-num2);
                        break;
                    case '*':
                        stack.push(num1*num2);
                        break;
                    case '/':
                        stack.push(num1/num2);
                        break;
                }
            }
        }
        return stack.top();
    }

    bool isNumber(string& token){
        return !(token=="+" || token=="-" || token=="*" || token=="/");
    }
};

// @lc code=end

