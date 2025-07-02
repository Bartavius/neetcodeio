import java.util.ArrayList;
import java.util.List;

class NeetcodeSubset {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        res.add(new ArrayList<>()); // empty set

        for (int num : nums) {
            int size = res.size();
            for (int i = 0; i < size; i++) {
                List<Integer> set = new ArrayList<>(res.get(i));
                set.add(num);
                res.add(set);
            }
        }
        return res;
    }
}
