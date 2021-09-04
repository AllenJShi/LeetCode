class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        //claim all global variables beforehand
        vector<vector<int>> ans(n, vector<int>(n,0));
        int row = 0, col = 0; //this will record the layer, (0,0) meaning the outmost, (1,1) meaning one layer inward
        int val = 1;
        int i, j; // initialize here due to future increment in the while loop
        int loop = n/2; // loop is to keep track of the inward spiral, the outmost layer is 0 and moving toward the center
        int mid = n/2; //mid will be used only if n is odd because, in that case, there will be a singular cell in the middle
        int margin = 1; //letting margin be 1 will allow to not count the corner at every turn
        
        while(loop--){
            for(i=col; i<col+n-margin; i++){
                ans[row][i] = val++;
            }
            for(j=row; j<row+n-margin; j++){
                ans[j][i] = val++;
            }
            for(;i>col;i--){
                ans[j][i] = val++;
            }
            for(;j>row;j--){
                ans[j][i] = val++;
            }
            margin += 2;
            row++;
            col++;
        }
        
        if(n % 2){
            ans[mid][mid] = val;
        }
        
        return ans;
    }
};