
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class GroupAnagramsSolution {
    @SuppressWarnings("Convert2Diamond")
    public List<List<String>> groupAnagrams(String[] strs) {
        
        Map<String, List<String>> result = new HashMap<>();

        for (String str : strs) {
            int[] count = new int[26];

            // count all the characters
            for (char c : str.toCharArray()) {
                count[c - 'a']++;
            }

            String key = Arrays.toString(count);
            result.putIfAbsent(key, new ArrayList<String>());
            result.get(key).add(str);
            
        }

        return new ArrayList<>(result.values());
    }
}
