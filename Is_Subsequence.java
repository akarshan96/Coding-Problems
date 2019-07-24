//  https://leetcode.com/problems/is-subsequence
//  6 ms, faster than 85.90% of Java online submissions for Is Subsequence.

class Solution {
    public boolean isSubsequence(String s, String t) {
        if(s.equals(""))
            return true;
        
        char[] sArr = s.toCharArray();
        char[] tArr = t.toCharArray();
        
        int si = 0;
        int ti = 0;
        
        int sLen = s.length();
        int tLen = t.length();
        
        if(sLen == 1 && tLen == 1) {
            return s.charAt(0) == t.charAt(0);
        }
                
        while(ti < tLen) {
            //System.out.print(si + "\t" + sArr[si] +  "\t" + ti + "\t" + tArr[ti] + "\n");
            
            if(sArr[si] == tArr[ti]) {
                si++;
            }
            
            if(si == sLen) {
                return true;
            }
            ti++;
        }
        return false;   
    }
}
