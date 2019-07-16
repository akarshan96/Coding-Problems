'''
https://leetcode.com/problems/symmetric-tree
'''

class Solution {
    
    public boolean isSymmetricUtil(TreeNode t1, TreeNode t2) {
        if (t1 == null && t2 == null) return true;
        if (t1 == null || t2 == null) return false;
        return (t1.val == t2.val)
            && isSymmetricUtil(t1.right, t2.left)
            && isSymmetricUtil(t1.left, t2.right);
    }
    
    
    public boolean isSymmetric(TreeNode root) {
         return isSymmetricUtil(root, root);
    }
}
