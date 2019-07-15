'''
https://leetcode.com/problems/same-tree/
Runtime: 0 ms, faster than 100.00% of Java online submissions for Same Tree.
'''

class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if(p == null && q == null) return true;
        if(p == null || q == null) return false;
        
        return (p.val == q.val) && isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
        
    }
}
