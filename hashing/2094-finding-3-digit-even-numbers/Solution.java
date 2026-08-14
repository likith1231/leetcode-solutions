import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] findEvenNumbers(int[] digits) {
        int[] count = new int[10];
        for (int d : digits) {
            count[d]++;
        }
        List<Integer> result = new ArrayList<>();
        for (int num = 100; num < 1000; num += 2) {
            int a = num / 100, b = num / 10 % 10, c = num % 10;
            count[a]--;
            count[b]--;
            count[c]--;
            if (count[a] >= 0 && count[b] >= 0 && count[c] >= 0) {
                result.add(num);
            }
            count[a]++;
            count[b]++;
            count[c]++;
        }
        return result.stream().mapToInt(Integer::intValue).toArray();
    }
}
