class Solution {
public:
    int largestInteger(int n, int s) {
        if ((n * 9) < s) return -1;

        int ans = 0;

        for (int i = 0; i < n; i++) {
            int x = min(s, 9);
            s -= x;
            ans = ans * 10 + x;
        }

        return ans;
    }
};