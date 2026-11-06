
import java.util.*;

class Solution {
    public int[] countServers(int n, int[][] logs, int x, int[] queries) {

        Arrays.sort(logs, (a, b) -> Integer.compare(a[1], b[1]));

        int[][] q = new int[queries.length][2];

        for (int i = 0; i < queries.length; i++) {
            q[i][0] = queries[i];
            q[i][1] = i;
        }

        Arrays.sort(q, (a, b) -> Integer.compare(a[0], b[0]));

        int[] ans = new int[queries.length];

        Map<Integer, Integer> map = new HashMap<>();

        int left = 0, right = 0;

        for (int[] query : q) {

            int start = query[0] - x;
            int end = query[0];

            while (right < logs.length && logs[right][1] <= end) {
                int server = logs[right][0];
                map.put(server, map.getOrDefault(server, 0) + 1);
                right++;
            }

            while (left < right && logs[left][1] < start) {
                int server = logs[left][0];

                map.put(server, map.get(server) - 1);

                if (map.get(server) == 0) {
                    map.remove(server);
                }

                left++;
            }

            ans[query[1]] = n - map.size();
        }

        return ans;
    }
}
