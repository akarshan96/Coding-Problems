/**
 * https://leetcode.com/problems/swap-nodes-in-pairs
 * Runtime: 0 ms, faster than 100.00% of Java online submissions for Swap Nodes in Pairs.
 *
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode swapPairs(ListNode head) {
        if(head == null) {
            return head;
        }
        
        ListNode current = head;
        ListNode next = current.next;
        ListNode prev = null;
        boolean flag = true;
        
        while(next!=null) {
            ListNode temp = next.next;
            current.next = temp;
            next.next = current;
            if(prev != null)
                prev.next = next;
            if(flag) {
                head = next;
                flag = false;
            }
            prev = current;
            current = current.next;
            if(current == null)
                break;
            next = current.next;

        }
        return head;
    }
}
