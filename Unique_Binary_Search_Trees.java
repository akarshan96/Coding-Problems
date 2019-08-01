//  https://leetcode.com/problems/unique-binary-search-trees/
//  Runtime: 0 ms, faster than 100.00% of Java online submissions for Unique Binary Search Trees.

class Solution {
    int[] memo;
    public int util(int n) {
        if(n == 0)
            return 1;
        if(n == 1)
            return 1;
        if(n == 2)
            return 2;
        if(memo[n] != 0) 
            return memo[n];
        int sum = 0;
        for(int i = 1; i <= n; i++) {
            sum = sum + util(i-1) * util(n-i);
        }
        memo[n] = sum;
        return sum;
    }
    
    public int numTrees(int n) {
         if(n == 0)
            return 1;
        if(n == 1)
            return 1;
        if(n == 2)
            return 2;
        
        memo = new int[n + 1];
        Arrays.fill(memo, 0);
        memo[0] = 1;
        memo[1] = 1;
        memo[2] = 2;
        
        return util(n);
    }
}
