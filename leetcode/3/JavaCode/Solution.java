package JavaCode;

import java.util.HashSet;
import java.util.Set;

public class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        int ans = 0;
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j <= n; j++)
                if (allUnique(s, i, j)){
                    ans = Math.max(ans, j - i);
                } 
        return ans;
    }

    public boolean allUnique(String s, int start, int end) {
        Set<Character> set = new HashSet<Character>();
        for (int i = start; i < end; i++) {
            Character ch = s.charAt(i);
            if (set.contains(ch)) return false;
            set.add(ch);
        }
        return true;
    }
    public static void main(String[] args) {
        Solution test = new Solution();
        System.out.println(test.lengthOfLongestSubstring("pwwkew"));
        // System.out.println(test.lengthOfLongestSubstring("ckilbkd"));
        // System.out.println(test.lengthOfLongestSubstring("aab"));
        // System.out.println(test.lengthOfLongestSubstring(" "));
        // System.out.println(test.lengthOfLongestSubstring("au"));
        // System.out.println(test.lengthOfLongestSubstring("dvdf"));
        // System.out.println(test.lengthOfLongestSubstring("anviaj"));
        // System.out.println(test.lengthOfLongestSubstring("asjrgapa"));
        // System.out.println(test.lengthOfLongestSubstring("jbpnbwwd"));
        // System.out.println(test.lengthOfLongestSubstring("ohvhjdml"));
    }
}