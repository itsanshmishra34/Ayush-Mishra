class Solution {
    public int totalNumbers(int[] digits) {
        Set<Integer> nums = new HashSet<>();

        for (int num = 100; num <= 998; num += 2) {
            int a = num / 100;
            int b = (num / 10) % 10;
            int c = num % 10;

            int[] temp = digits.clone();

            boolean valid = true;

            for (int d : new int[]{a, b, c}) {
                boolean found = false;

                for (int i = 0; i < temp.length; i++) {
                    if (temp[i] == d) {
                        temp[i] = -1;
                        found = true;
                        break;
                    }
                }

                if (!found) {
                    valid = false;
                    break;
                }
            }

            if (valid) {
                nums.add(num);
            }
        }

        return nums.size();
    }
}