/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
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
                list.add(level);                
            }
            count ++;
        }    
        return(list);
        
        
    }
}
