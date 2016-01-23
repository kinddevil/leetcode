package test;
import java.util.HashMap;
import java.util.Stack;
import java.util.Map;

public class VParentheses {
	public boolean isValid(String s) {
		Stack<String> stack = new Stack<String>();
		Map<String, String> m1 = new HashMap<String, String>(){{
			put("(", ")");
			put("[", "]");
			put("{", "}");
		}};
		Map<String, String> m2 = new HashMap<String, String>(){{
			put(")", "(");
			put("]", "[");
			put("}", "{");
		}};
		for (char i : s.toCharArray()){
			String ii = String.valueOf(i);
			if (m1.containsKey(ii)){
				stack.add(ii);
			} else if (m2.containsKey(ii)){
				if ( stack.isEmpty() || !m2.get(ii).equals(stack.pop())){
					return false;
				}
			}
		}
		if (stack.isEmpty())
			return true;
        return false;
    }
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		VParentheses v = new VParentheses();
		System.out.println(v.isValid("([abc)"));
	}

}

