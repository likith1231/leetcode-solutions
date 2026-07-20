import java.util.Arrays;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        int[] last = new int[128];
        Arrays.fill(last, -1);
        int best = 0;
        for (int left = 0, right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            if (last[c] >= left) {
                left = last[c] + 1;
            }
            last[c] = right;
            best = Math.max(best, right - left + 1);
        }
        return best;
    }
}
