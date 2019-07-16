'''
https://leetcode.com/problems/group-anagrams/
Runtime: 9 ms, faster than 77.79% of Java online submissions for Group Anagrams.
'''

class Solution {
    
    public List<List<String>> groupAnagrams(String[] strs) {        
        HashMap<String,List<String>> map = new HashMap<String,List<String>>();
        List<List<String>> result = new ArrayList<List<String>>();
        
        for(String s: strs) {
            char[] charArr = s.toCharArray();
            Arrays.sort(charArr);
            String newString = String.valueOf(charArr);
            if(map.get(newString) == null) {
                ArrayList<String> list = new ArrayList<String>();
                list.add(s);
                map.put(newString, list);
            }
            else {
                List<String> list = map.get(newString);
                list.add(s);
                map.put(newString, list);
            }
        }
        for (Map.Entry<String,List<String>> entry : map.entrySet())  
            result.add(entry.getValue());
        
        return result;
    }
}
