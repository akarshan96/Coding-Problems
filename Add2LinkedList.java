//  https://leetcode.com/problems/add-two-numbers/submissions/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode prevNode = null;
        ListNode head = null;
        int carry = 0;
    
        while(true) {
            int sum = 0;
            if (l1 == null && l2 == null){
                if(carry == 1) {
                    ListNode node = new ListNode(1);
                    prevNode.next = node;
                }
                break;
            }
            if (l1 == null) {
                sum = l2.val + carry;
            }
            else if (l2 == null) {
                sum = l1.val + carry;
            }
            else {
                sum = l1.val + l2.val + carry;
            }
            if (sum >= 10) {
                sum = sum - 10;
                carry = 1;
            }
            else {
                carry = 0;
            }
            ListNode node = new ListNode(sum);
            if (prevNode == null) {
                prevNode = node;
                head = node;
            }
            else {
                prevNode.next = node;
                prevNode = node;
            }
            if (l1!= null)
                l1 = l1.next;
            if (l2 != null)
                l2 = l2.next;
        }
        return head;
    }
}
