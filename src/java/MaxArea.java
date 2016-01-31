package test;

public class MaxArea {
	public int maxArea(int[] height) {
        int s = 0, e = height.length - 1, max = Integer.MIN_VALUE;
        while (s < e){
        	max = Integer.max(max, Integer.min(height[s], height[e]) * (e - s));
        	if (height[e] > height[s])
        		s++;
        	else
        		e--;
        }
        return max;
    }

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}

