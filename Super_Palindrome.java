/*
https://leetcode.com/problems/super-palindromes
*/
class Solution {
    
    public boolean isPalindrome(long num) {
        String text = String.valueOf(num);
        if (text == null) {
            return false;
        }
        int left = 0;
        int right = text.length() - 1;
        while (left < right) {
            if (text.charAt(left++) != text.charAt(right--)) {
                return false;
            }
        }
        return true;
    }
    
    public int superpalindromesInRange(String L, String R) {
        int count = 0;
        long l = (int) Math.sqrt(Long.parseLong(L));
        long r = (int) Math.sqrt(Long.parseLong(R));
        for(long n = l; n <= r; n++) {
            if(isPalindrome(n)) {
                if(isPalindrome(n*n))
                    count++;
            }
        }             
        return count;
        
    }
}
