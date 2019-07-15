'''
https://leetcode.com/problems/valid-anagram
Runtime: 3 ms, faster than 94.23% of Java online submissions for Valid Anagram.
'''

class Solution {
    public boolean isAnagram(String s, String t) {
        int a = s.length();
        int b = t.length();
        if(a != b)
            return false;
        int count[] = new int[26];
        
        for(int i=0;i<a;i++)
        {
            count[s.charAt(i)-'a']++;
            count[t.charAt(i)-'a']--;

        }
        
        for(int i=0;i<26;i++)
            if(count[i] != 0)
                return false;

        return true;
    }
}
