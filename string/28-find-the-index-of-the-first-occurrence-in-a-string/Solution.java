class Solution {
    public int strStr(String haystack, String needle) {
        int m = needle.length();
        int[] lps = new int[m];
        for (int i = 1, len = 0; i < m; i++) {
            while (len > 0 && needle.charAt(i) != needle.charAt(len)) {
                len = lps[len - 1];
            }
            if (needle.charAt(i) == needle.charAt(len)) {
                len++;
            }
            lps[i] = len;
        }
        for (int i = 0, j = 0; i < haystack.length(); i++) {
            while (j > 0 && haystack.charAt(i) != needle.charAt(j)) {
                j = lps[j - 1];
            }
            if (haystack.charAt(i) == needle.charAt(j)) {
                j++;
            }
            if (j == m) {
                return i - m + 1;
            }
        }
        return -1;
    }
}
