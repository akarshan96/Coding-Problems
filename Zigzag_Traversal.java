/**
 * https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal
 * Runtime: 1 ms, faster than 88.57% of Java online submissions for Binary Tree Zigzag Level Order Traversal.
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List list = new ArrayList<ArrayList<Integer>>();
        List queue = new ArrayList<TreeNode>();
        if(root == null) {
            return(list);
        }
        queue.add(root);
        List temp = new ArrayList<Integer>();
        temp.add(root.val);
        list.add(temp);
        int count = 0;
        boolean flag = true;
        while(!queue.isEmpty()) {
            List level = new ArrayList<Integer>();
            int size = ((ArrayList<ArrayList<Integer>>) list.get(count)).size();
            
            for(int i = 0; i < size; i ++) {
                TreeNode current = (TreeNode) queue.get(0);
                if(current.left != null) {
                    level.add(current.left.val);
                    queue.add(current.left);
                }
                if(current.right != null) {
                    level.add(current.right.val);
                    queue.add(current.right);
                }
                queue.remove(0);
            }
            
            if(!level.isEmpty()) {
                if(flag) {
                    Collections.reverse(level);
                    list.add(level); 
                    flag = false;
                }
                else {
                    list.add(level); 
                    flag = true;
                }
            }
            count ++;
        }
        
        return(list);
        
    }
}
