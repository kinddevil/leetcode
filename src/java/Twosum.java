import java.util.List;
import java.util.Map;
import java.util.HashMap;

public class Twosum {
    public int[] twoSum(int[] numbers, int target) {
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
		for (int i=0 ; i<numbers.length; i++ ){
			if ( map.containsKey(numbers[i]) ){
				return new int[]{map.get(numbers[i])+1, i+1};
			}else{
				map.put(target-numbers[i], i);
			}
		}
		return null;
    }

    public static void main(String argvi[]){
	Twosum t = new Twosum();
 	int[] nums = {2,7,9,11};
	int target = 9;
	int[] ret = t.twoSum(nums, target);
	for (int i : ret)
		System.out.println(i);
    }
}
