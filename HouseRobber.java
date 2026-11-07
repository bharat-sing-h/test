import java.util.Random;

/**
 * House Robber.
 *
 * Given the amount of money in each house along a street, return the maximum
 * amount that can be robbed without robbing two adjacent houses.
 *
 * Approach: dynamic programming with two rolling values.
 *   best(i) = max(best(i - 1), best(i - 2) + nums[i])
 * where best(i) is the most money obtainable from houses 0..i.
 *
 * Time:  O(n)
 * Space: O(1)
 *
 * Edge cases handled:
 *   - null or empty array        -> 0
 *   - single house               -> its value (or 0 if negative)
 *   - two houses                 -> the larger one
 *   - all zeros                  -> 0
 *   - negative values            -> never robbed (skipping a house is always allowed)
 *   - very large values / long   -> sums kept in long, so no int overflow
 *     streets
 */
public class HouseRobber {

    public static long rob(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }

        long prev2 = 0; // best total up to house i - 2
        long prev1 = 0; // best total up to house i - 1

        for (int money : nums) {
            long current = Math.max(prev1, prev2 + money);
            prev2 = prev1;
            prev1 = current;
        }
        return prev1;
    }

    /** Exhaustive check over every valid set of houses; used only to verify rob(). */
    static long bruteForce(int[] nums) {
        if (nums == null) {
            return 0;
        }
        int n = nums.length;
        long best = 0; // robbing nothing is always allowed
        for (int mask = 0; mask < (1 << n); mask++) {
            if ((mask & (mask >> 1)) != 0) {
                continue; // two adjacent houses chosen
            }
            long sum = 0;
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) {
                    sum += nums[i];
                }
            }
            best = Math.max(best, sum);
        }
        return best;
    }

    private static int passed = 0;
    private static int failed = 0;

    private static void check(String name, int[] nums, long expected) {
        long actual = rob(nums);
        if (actual == expected) {
            passed++;
        } else {
            failed++;
            System.out.println("FAIL " + name + ": expected " + expected + ", got " + actual);
        }
    }

    public static void main(String[] args) {
        // Edge cases
        check("null input", null, 0);
        check("empty street", new int[] {}, 0);
        check("one house", new int[] {5}, 5);
        check("one house, zero money", new int[] {0}, 0);
        check("two houses, first larger", new int[] {7, 3}, 7);
        check("two houses, second larger", new int[] {3, 7}, 7);
        check("two equal houses", new int[] {4, 4}, 4);
        check("all zeros", new int[] {0, 0, 0, 0}, 0);
        check("all equal", new int[] {5, 5, 5, 5, 5}, 15);

        // Classic examples
        check("example 1", new int[] {1, 2, 3, 1}, 4);
        check("example 2", new int[] {2, 7, 9, 3, 1}, 12);
        check("greedy-by-parity trap", new int[] {2, 1, 1, 2}, 4);
        check("skip two in a row", new int[] {5, 1, 1, 5}, 10);
        check("middle is best", new int[] {1, 100, 1}, 100);
        check("ends are best", new int[] {100, 1, 1, 100}, 200);
        check("increasing", new int[] {1, 2, 3, 4, 5, 6}, 12);
        check("decreasing", new int[] {6, 5, 4, 3, 2, 1}, 12);

        // Negative values are simply never robbed
        check("single negative", new int[] {-5}, 0);
        check("all negative", new int[] {-1, -2, -3}, 0);
        check("mixed signs", new int[] {-1, 10, -1, 10, -1}, 20);

        // Overflow: these sums do not fit in an int
        int max = Integer.MAX_VALUE;
        check("two max values apart", new int[] {max, 0, max}, 2L * max);
        int[] bigStreet = new int[1_000_000];
        java.util.Arrays.fill(bigStreet, max);
        check("1,000,000 max-value houses", bigStreet, 500_000L * max);

        // Long street, to confirm linear time
        int[] longStreet = new int[10_000_000];
        for (int i = 0; i < longStreet.length; i++) {
            longStreet[i] = i % 2 == 0 ? 1 : 2;
        }
        check("10,000,000 houses", longStreet, 10_000_000L);

        // Random cross-check against brute force
        Random random = new Random(42);
        for (int t = 0; t < 20_000; t++) {
            int n = random.nextInt(19); // 0..18 houses
            int[] nums = new int[n];
            for (int i = 0; i < n; i++) {
                switch (random.nextInt(3)) {
                    case 0 -> nums[i] = random.nextInt(10);            // small values
                    case 1 -> nums[i] = random.nextInt(401);           // typical range
                    default -> nums[i] = random.nextInt();             // any int, incl. negative
                }
            }
            check("random #" + t, nums, bruteForce(nums));
        }

        System.out.println("Passed: " + passed + ", Failed: " + failed);
        if (failed > 0) {
            System.exit(1);
        }
    }
}
