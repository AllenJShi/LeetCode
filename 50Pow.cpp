class Solution {
public:
    double myPow(double x, int n) {
        long long N = n;
        return N>=0 ? pow(x, N) : 1.0/pow(x, -N);
    }
    
    double pow(double x, long long N){
        if(N==0) return 1.0;
        double y = pow(x, N/2);
        return N%2 == 0 ? y*y : y*y*x;
    }
};