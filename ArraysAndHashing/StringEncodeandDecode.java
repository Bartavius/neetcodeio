
import java.util.ArrayList;
import java.util.List;

class Solution {

    private final String delimiter = "#";

    public String encode(List<String> strs) {
        String result = "";
        for (String word : strs) {
            result += String.format("%d%s%s", word.length(), delimiter, word);
        }
        System.out.println(result);
        return result;
    }

    public List<String> decode(String str) {
        List<String> words = new ArrayList<>();
        int currentIndex = 0;
        int length;
        String curr, upto;
        while (currentIndex < str.length()) {

            // getting the length up to delimiter
            upto = "";
            while (Character.isDigit(str.charAt(currentIndex))) {
                upto += str.charAt(currentIndex++);
            }
            currentIndex++;
            System.out.println(upto);
            length = Integer.parseInt(upto);
            System.out.println(upto);
            curr = "";
            for (int i = 0; i < length; i++) {
                curr += str.charAt(currentIndex++);
            }
            words.add(curr);
        }
        return words;
    }
}
